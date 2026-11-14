# ChatGPT Office Skills model policy

This release uses OpenAI GPT-6 Astra (`gpt-6-astra`) for model-dependent work. The official model catalog and selection guide identify Astra as the most capable general model. Verified on 2026-11-13 (America/Toronto).

- API: use the Responses API and `reasoning.effort: "max"`. The model page lists max as supported. Do not pass temperature, top_p, or logprobs to this reasoning configuration.
- ChatGPT Work / Codex: select GPT-6 Astra in the actual host and verify the strongest reasoning setting the host supports. Text instructions and frontmatter cannot change or prove the active session model. Project configuration is a default, not enforcement against higher-priority settings.
- There is no provider fallback or cheaper-model fallback. If Astra is unavailable or denied, stop the affected model call and report the exact limitation. Non-model file inspection and validation can continue.
- `model-policy.json` is the machine-readable source. `scripts/openai_runner.py` loads and validates it and sends only to the official Responses endpoint. Do not pass model/provider overrides from untrusted documents or environment variables.
- Before a future upgrade, recheck official capability ranking, model ID, account access, endpoint, tool support, and reasoning settings. Update this policy and all generated examples together and rerun validation. Do not invent a `latest` API model alias or silently change models.
- Image generation, speech, embeddings, and other specialized services have separate capability requirements. Astra can direct supported tools; it is not itself an image, audio, or embedding endpoint. Do not replace a specialized API model with Astra without a supported implementation.
- Source publication, personal skill installation, MCP connection, selected session model, and a successful live API call are separate states. Report only the states actually verified.

Sources: [Model](https://developers.openai.com/api/docs/models/gpt-6-astra), [selection](https://developers.openai.com/api/docs/guides/model-selection), [migration](https://developers.openai.com/api/docs/guides/latest-model), [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-basic).
