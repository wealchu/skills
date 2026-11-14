# ChatGPT Office Skills migration

Source baseline: `wealchu/skills` main commit `9c4c7d5cd2813a8936bf2c9fdb174ea883b85a11`.

The collection is named ChatGPT Office Skills. Active model instructions, 136 skill definitions, five agents, their templates, generators, configuration guidance, and API examples use OpenAI GPT-6 Astra. The API runner pins `gpt-6-astra`, maximum reasoning, and the Responses endpoint, and refuses provider/model overrides, redirects, incomplete responses, and silent fallback.

The document guides are newly written and maintained by this fork. Original copyright, provenance, Git history, and historical binary fixtures remain intact. The MCP server implementation and bundled JavaScript remain byte-identical to the baseline; its package metadata and deployment instructions have changed.

Validation performed in the cloud workspace: 12 offline regression tests; all skill/agent model metadata; retired model/provider/protocol scan; JSON and Python syntax; package identity; generator output; export dependency manifest, no-overwrite behavior, and unknown-skill rejection. GitHub Actions repeats the migration checks on pull requests and main pushes. A passing migration check does not validate every business example or certify engineering/legal conclusions.

No paid model request was sent. Personal skill installation, live account model access, active session selection, and MCP connections require separate observable verification. The source export retains a dependency on the complete checkout and is explicitly not a standalone installation package. No account-wide automation or governance setting is changed by this repository migration.
