#!/usr/bin/env python3
"""Run authorized text/vision tasks with the verified OpenAI model; never fall back."""
import argparse
import base64
import json
import os
from pathlib import Path
import sys
from urllib import request, error

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://api.openai.com/v1/responses"


def load_policy():
    policy = json.loads((ROOT / "model-policy.json").read_text())
    if (policy.get("provider") != "openai"
            or policy.get("model") != "gpt-6-astra"
            or policy.get("reasoning_effort") != "max"
            or policy.get("endpoint") != ENDPOINT
            or policy.get("fallback_models") != []):
        raise ValueError("Model policy differs from the verified release; reverify before calling.")
    return policy


def image_input(path):
    path = Path(path)
    mime = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}.get(path.suffix.lower())
    if mime is None:
        raise ValueError("Use a PNG, JPEG, or WebP image.")
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return {"type": "input_image", "image_url": f"data:{mime};base64,{data}"}


def build_request(instructions, content):
    policy = load_policy()
    if not isinstance(instructions, str) or not instructions.strip():
        raise ValueError("Nonempty instructions are required.")
    if not content or not isinstance(content, (str, list)):
        raise ValueError("Nonempty task text or image content is required.")
    task = content if isinstance(content, str) else [{"role": "user", "content": content}]
    return {"model": policy["model"], "reasoning": {"effort": policy["reasoning_effort"]},
            "instructions": instructions, "input": task}


class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Unexpected API redirect refused; no provider fallback is permitted.")


def send_request(payload, *, timeout=600):
    policy = load_policy()
    if set(payload) != {"model", "reasoning", "instructions", "input"}:
        raise ValueError("Use the validated request builder; extra request overrides are not supported.")
    if payload["model"] != policy["model"] or payload["reasoning"] != {"effort": policy["reasoning_effort"]}:
        raise ValueError("Model or reasoning override refused.")
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY is not configured; no request was sent.")
    req = request.Request(ENDPOINT, data=json.dumps(payload).encode(),
                          headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, method="POST")
    opener = request.build_opener(NoRedirect())
    try:
        with opener.open(req, timeout=timeout) as response:
            result = json.load(response)
    except error.HTTPError as exc:
        raise RuntimeError(f"OpenAI request failed (HTTP {exc.code}); no fallback was attempted.") from None
    except error.URLError:
        raise RuntimeError("OpenAI connection failed; no fallback was attempted.") from None
    returned = result.get("model", "")
    if returned != policy["model"] and not returned.startswith(policy["model"] + "-"):
        raise RuntimeError("Response model does not match the verified target.")
    if result.get("status") != "completed":
        raise RuntimeError("Response is not completed; do not treat partial output as a finished task.")
    return result


def output_text(response):
    parts = []
    for item in response.get("output", []):
        if item.get("type") == "message":
            for part in item.get("content", []):
                if part.get("type") == "output_text":
                    parts.append(part["text"])
                elif part.get("type") == "refusal":
                    parts.append(part.get("refusal", "Request declined."))
    if not parts:
        raise RuntimeError("No user-facing text was returned; inspect the response before continuing.")
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instructions", required=True, type=Path)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--image", type=Path)
    parser.add_argument("--dry-run", action="store_true", help="Print the request without sending it (may contain task text).")
    args = parser.parse_args()
    text = args.input.read_text()
    content = [{"type": "input_text", "text": text}, image_input(args.image)] if args.image else text
    payload = build_request(args.instructions.read_text(), content)
    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(output_text(send_request(payload)))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
