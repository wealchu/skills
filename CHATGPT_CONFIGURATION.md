# ChatGPT Work and Codex configuration

## Model selection

Read [MODEL_POLICY.md](MODEL_POLICY.md). Select GPT-6 Astra in the actual host and use its strongest supported reasoning setting. If it is not available, report that before model-dependent work; do not choose another provider or silently downgrade. A repository edit cannot change an already-running conversation's model.

## Skill use

Use the account's supported personal-skill installation flow to install or update selected skills in ChatGPT. A repository connection or index file alone is not installation. Read each requested SKILL.md and its dependencies; test an actual task after installation. For Codex CLI/IDE, the optional `install.sh` exports selected source skill folders to a workspace `.agents/skills` directory; it does not install personal ChatGPT skills or change account settings. Exports are not standalone: retain the full source checkout at the source_root recorded in each SOURCE.json, verify its source-skill hash, and run repository examples and resolve shared dependencies from that root. If the source moves or is missing, re-export after verifying the new location.

## Office MCP

The bundled server uses stdio and processes documents; it does not call a language model. Build from this fork in an authorized environment:

```bash
cd mcp-servers/office-mcp
npm ci
npm run build
```

For a Codex host that supports stdio, register the actual absolute path:

```bash
codex mcp add office-mcp -- node /absolute/path/to/skills/mcp-servers/office-mcp/dist/index.js
```

Verify that the host lists the server and can complete a harmless document read. Do not use an unpublished package name with npx. This fork's package is private and is run from reviewed source.

ChatGPT web requires a supported hosted MCP/plugin connection; a desktop JSON file or a local stdio path is not such a connection. Deploying a hosted adapter, authentication, and data access requires separate configuration and validation. Existing connected document tools may be used when appropriate.

## API

Set OPENAI_API_KEY through the environment's secure credential mechanism, never in a skill or chat. The runner reads that key only at invocation. Example from the repository root:

```bash
python3 scripts/openai_runner.py --instructions contract-review/SKILL.md --input contract.txt --dry-run
python3 scripts/openai_runner.py --instructions contract-review/SKILL.md --input contract.txt
```

Dry-run validates and displays the request without sending it. Remove dry-run only for an authorized live call. A ChatGPT subscription or successful dry-run does not prove API entitlement or live access.

References: [MCP](https://learn.chatgpt.com/docs/extend/mcp), [configuration](https://learn.chatgpt.com/docs/config-file/config-basic).
