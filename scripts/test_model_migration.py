"""Offline regression tests for model routing, request handling, and workspace export."""
import copy
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError
import openai_runner as runner
import export_skills as exporter
import batch_create_skills as creator
import upgrade_skills_metadata as metadata


class ModelMigrationTests(unittest.TestCase):
    def test_text_request_uses_verified_target(self):
        payload = runner.build_request("Review evidence", "Sample task")
        self.assertEqual(payload["model"], "gpt-6-astra")
        self.assertEqual(payload["reasoning"], {"effort": "max"})
        self.assertEqual(payload["instructions"], "Review evidence")
        self.assertFalse({"temperature", "top_p", "max_tokens", "messages"} & payload.keys())

    def test_image_request_uses_responses_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            image = Path(tmp) / "sample.png"
            image.write_bytes(b"\x89PNG\r\n\x1a\n")
            content = [{"type": "input_text", "text": "Describe"}, runner.image_input(image)]
            payload = runner.build_request("Use visible evidence", content)
            self.assertEqual(payload["input"][0]["role"], "user")
            self.assertTrue(content[1]["image_url"].startswith("data:image/png;base64,"))

    def test_invalid_policy_fails_closed(self):
        policy = runner.load_policy()
        for key, value in [("provider", "other"), ("model", "unknown"), ("endpoint", "https://example.com"), ("reasoning_effort", "none"), ("fallback_models", ["other"])]:
            changed = copy.deepcopy(policy); changed[key] = value
            with self.subTest(key=key), patch.object(Path, "read_text", return_value=json.dumps(changed)):
                with self.assertRaises(ValueError): runner.load_policy()

    def test_no_key_sends_nothing(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(runner.request, "build_opener") as opener:
            with self.assertRaises(ValueError): runner.send_request(runner.build_request("Review", "Input"))
            opener.assert_not_called()

    def test_overrides_refused_before_network(self):
        original = runner.build_request("Review", "Input")
        for delta in [{"model": "different"}, {"reasoning": {"effort": "low"}}, {"temperature": 1}]:
            payload = original | delta
            with self.subTest(delta=delta), patch.object(runner.request, "build_opener") as opener:
                with self.assertRaises(ValueError): runner.send_request(payload)
                opener.assert_not_called()

    def fake_call(self, result):
        opener = MagicMock()
        opener.open.return_value.__enter__.return_value = io.StringIO(json.dumps(result))
        with patch.dict(os.environ, {"OPENAI_API_KEY": "offline-test-only"}), patch.object(runner.request, "build_opener", return_value=opener):
            value = runner.send_request(runner.build_request("Review", "Input"))
        return value, opener

    def test_completed_response_and_endpoint(self):
        result, opener = self.fake_call({"model": "gpt-6-astra", "status": "completed", "output": [{"type":"message", "content":[{"type":"output_text", "text":"Done"}]}]})
        self.assertEqual(runner.output_text(result), "Done")
        self.assertEqual(opener.open.call_args.args[0].full_url, runner.ENDPOINT)
        self.assertEqual(opener.open.call_args.args[0].method, "POST")

    def test_incomplete_and_wrong_model_refused(self):
        for result in [{"model":"gpt-6-astra", "status":"incomplete"}, {"model":"different", "status":"completed"}]:
            with self.subTest(result=result), self.assertRaises(RuntimeError): self.fake_call(result)

    def test_http_error_has_no_fallback(self):
        opener = MagicMock(); opener.open.side_effect = HTTPError(runner.ENDPOINT, 403, "denied", {}, None)
        with patch.dict(os.environ, {"OPENAI_API_KEY":"offline-test-only"}), patch.object(runner.request,"build_opener",return_value=opener):
            with self.assertRaisesRegex(RuntimeError,"no fallback"): runner.send_request(runner.build_request("Review","Input"))
        self.assertEqual(opener.open.call_count,1)

    def test_redirect_refused(self):
        with self.assertRaises(ValueError): runner.NoRedirect().redirect_request(None,None,302,"moved",{},"https://example.com")

    def test_generators_only_emit_target_model(self):
        for config in creator.SKILLS_TO_CREATE.values():
            generated = creator.create_skill_md(config)
            self.assertIn("models: [gpt-6-astra]", generated)
            self.assertIn("Model requirement", generated)
        generated = metadata.generate_enhanced_frontmatter("contract-review", {"name":"contract-review","description":"Test"})
        self.assertIn("gpt-6-astra", generated)
        self.assertEqual(generated.count("gpt-6-astra"), 2)

    def test_export_preserves_existing_files(self):
        selected = exporter.select_skills(["contract-review"], None)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)/"skills"
            exporter.export_skills(selected,target,True)
            self.assertFalse(target.exists())
            exporter.export_skills(selected,target)
            self.assertTrue((target/"contract-review"/"MODEL_POLICY.md").is_file())
            manifest = json.loads((target/"contract-review"/"SOURCE.json").read_text())
            self.assertFalse(manifest["standalone"])
            source = Path(manifest["source_root"])
            self.assertTrue((source/"scripts"/"openai_runner.py").is_file())
            self.assertTrue((source/"mcp-servers"/"office-mcp"/"knowledge"/"base"/"risk_patterns.json").is_file())
            original = (target/"contract-review"/"SKILL.md").read_bytes()
            with self.assertRaises(ValueError): exporter.export_skills(selected,target)
            self.assertEqual((target/"contract-review"/"SKILL.md").read_bytes(),original)

    def test_unknown_skill_cannot_escape_destination(self):
        with self.assertRaises(ValueError): exporter.select_skills(["../outside"],None)


if __name__ == "__main__":
    unittest.main()
