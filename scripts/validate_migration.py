#!/usr/bin/env python3
"""Validate the provider migration without network access or credentials."""
import ast
import json
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []
skills = list(ROOT.glob("*/SKILL.md"))
agents = list(ROOT.glob("agents/*/AGENT.md"))


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


for path in skills + agents:
    try:
        text = path.read_text()
        header = yaml.safe_load(text.split("---", 2)[1])
        models = header.get("models", header.get("model"))
        if set(strings(models)) != {"gpt-6-astra"}:
            errors.append(f"{path.relative_to(ROOT)}: model metadata differs from the pinned policy")
        if "Model and execution requirement" not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing executable model instruction")
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")

retired_protocol = re.compile(r"n8n-nodes-base\.openAi|n8n-nodes-base\.anthropic", re.I)
legacy = re.compile(r"claude|anthropic|sonnet|haiku|\bopus\b|gpt[-_ ]?[0-5]|gemini|gpt-6-astra-vision", re.I)
exempt = {"LICENSE", "THIRD_PARTY_NOTICES.md", "scripts/validate_migration.py"}
for path in ROOT.rglob("*"):
    if not path.is_file() or any(x in path.parts for x in [".git", "node_modules", "__pycache__", ".agents"]):
        continue
    relative = path.relative_to(ROOT).as_posix()
    if path.suffix == ".json":
        try: json.loads(path.read_text())
        except Exception as exc: errors.append(f"{relative}: invalid JSON: {exc}")
    if path.suffix == ".py":
        try: ast.parse(path.read_text())
        except SyntaxError as exc: errors.append(f"{relative}: invalid Python: {exc}")
    if relative not in exempt and path.suffix in {".md", ".mdc", ".py", ".sh", ".toml"}:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if retired_protocol.search(line): errors.append(f"{relative}:{number}: legacy model node; use the documented Responses request")
            if legacy.search(line): errors.append(f"{relative}:{number}: retired or unverified model/provider reference")

package = json.loads((ROOT/"mcp-servers/office-mcp/package.json").read_text())
lock = json.loads((ROOT/"mcp-servers/office-mcp/package-lock.json").read_text())
if not package.get("private") or lock["name"] != package["name"] or lock["packages"][""]["name"] != package["name"]:
    errors.append("MCP package identity/private flag is inconsistent")
if lock["version"] != package["version"] or lock["packages"][""]["version"] != package["version"]:
    errors.append("MCP package versions differ")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Validated {len(skills)-1} skills, one skill template, {len(agents)-1} agents, one agent template, model metadata, JSON, Python, and package identity.")
