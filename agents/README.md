# ChatGPT Office Agents

> Pre-configured AI personas with specialized skills for specific roles.

## What Are Agents?

**Agents** are pre-packaged AI personas that combine:
- **Personality**: Tone, style, and communication preferences
- **Skills**: Curated set of abilities from the skills library
- **Knowledge**: Domain-specific expertise and rules
- **Tools**: MCP tool access for document operations

Think of agents as "digital employees" you can deploy to handle specific tasks.

## Available Agents

| Agent | Role | Skills | Platforms |
|-------|------|--------|-----------|
| [Legal Specialist](./legal-specialist/) | Contract Review & Legal Ops | contract-review, nda-generator | All |
| [Data Analyst](./data-analyst/) | Excel Analysis & Reporting | data-analysis, dcf-valuation | All |
| [Admin Assistant](./admin-assistant/) | Email & Calendar Management | email-drafter, meeting-notes | All |
| [Research Analyst](./research-analyst/) | Deep Research & Company Analysis | deep-research, company-research | All |
| [Content Creator](./content-creator/) | Writing & Marketing Content | content-writer, seo-optimizer | All |

## Quick Start

### 1. Choose an Agent

Browse the agents above and find one that matches your needs.

### 2. Load in the supported host

Use [ChatGPT configuration](../CHATGPT_CONFIGURATION.md) and select GPT-6 Astra. Read the chosen AGENT.md and the listed skills, knowledge files, and tool requirements. Agent files are specifications, not a verified deployment.

For the OpenAI API, assemble the required dependencies into the instructions before calling the shared runner. The runner does not automatically load referenced files or execute MCP tools.

```bash
python3 scripts/openai_runner.py --instructions prepared-agent-instructions.md --input task.txt --dry-run
```


### 3. Start Chatting

Verify that the host loaded the persona and required skills with a representative task; listing them in AGENT.md does not load them automatically.

## Agent vs Skill

| Aspect | Skill | Agent |
|--------|-------|-------|
| **What** | Single capability | Complete persona |
| **Contains** | Instructions for one task | Personality + multiple skills |
| **Use when** | You know exactly what task | You want a consistent assistant |
| **Example** | `contract-review` skill | `legal-specialist` agent |

## Creating Custom Agents

### 1. Copy the Template

```bash
cp -r agents/_template agents/my-agent
```

### 2. Edit AGENT.md

Configure:
- **Personality**: How the agent communicates
- **Skills**: Which skills to equip
- **Knowledge**: Domain expertise to include
- **Platforms**: Where to deploy

### 3. Validate the configuration

Verify skill and knowledge paths, available tools, selected model, and representative outputs in the authorized host. Use the runner's dry-run first; separately record any live test.

### 4. Use in the configured host

Connect only approved tools and communication channels. A persona description does not authorize sending messages or modifying external records.


## Agent Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Agent (AGENT.md)                                       │
│  ┌─────────────────────────────────────────────────────┤
│  │ Personality: tone, style, language                  │
│  ├─────────────────────────────────────────────────────┤
│  │ Skills[]: contract-review, nda-generator, ...       │
│  ├─────────────────────────────────────────────────────┤
│  │ Knowledge[]: risk_patterns, jurisdictions, ...      │
│  ├─────────────────────────────────────────────────────┤
│  │ MCP Tools[]: extract_pdf, create_docx, ...          │
│  └─────────────────────────────────────────────────────┘
└─────────────────────────────────────────────────────────┘
```

## Contributing

We welcome new agent configurations! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

### Ideas for New Agents

- [ ] HR Manager - Recruiting, onboarding, performance reviews
- [ ] Sales Rep - Lead research, proposal writing, CRM
- [ ] Finance Controller - Invoice processing, expense tracking
- [ ] Customer Success - Support tickets, onboarding guides
- [ ] Project Manager - Task tracking, status reports

---

**Made with ChatGPT Office Skills.**
