---
# ═══════════════════════════════════════════════════════════════════════════════
# CHATGPT OFFICE SKILL - Enhanced Metadata v2.0
# ═══════════════════════════════════════════════════════════════════════════════

# Basic Information
name: n8n-workflow
description: "Automate document workflows with n8n - 7800+ workflow templates"
version: "1.0"
author: wealchu
license: MIT

# Categorization
category: workflow
tags:
  - n8n
  - workflow
  - automation
  - integration
department: All

# AI Model Compatibility
models:
  recommended:
    - gpt-6-astra
  compatible:
    - gpt-6-astra

# Skill Capabilities
capabilities:
  - workflow_automation
  - integration

# Language Support
languages:
  - en
  - zh
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# N8N Workflow Skill

## Overview

This skill enables document workflow automation using **n8n** - the most popular workflow automation platform with 7800+ community templates. Chain document operations, integrate with 400+ apps, and build complex document pipelines.

## How to Use

1. Describe what you want to accomplish
2. Provide any required input data or files
3. I'll execute the appropriate operations

**Example prompts:**
- "Automate PDF → OCR → Translation → Email workflow"
- "Watch folder for new contracts → Review → Notify Slack"
- "Daily report generation from multiple data sources"
- "Batch document processing with conditional logic"

## Domain Knowledge


### n8n Fundamentals

n8n uses a node-based workflow approach:

```
Trigger → Action → Action → Output
   │         │         │
   └─────────┴─────────┴── Data flows between nodes
```

### Key Node Types

| Type | Examples | Use Case |
|------|----------|----------|
| **Triggers** | Webhook, Schedule, File Watcher | Start workflow |
| **Document** | Read PDF, Write DOCX, OCR | Process files |
| **Transform** | Code, Set, Merge | Manipulate data |
| **Output** | Email, Slack, Google Drive | Deliver results |

### Workflow Example: Contract Review Pipeline

Use folder intake → PDF extraction → OpenAI Responses HTTP request → reviewed report storage. Outbound notification remains subject to explicit authorization.

Configure an HTTP Request step using POST to `https://api.openai.com/v1/responses`, JSON content type, and an OpenAI credential stored in the workflow's credential store. The version-specific n8n node must be checked before importing a workflow; this is a request-body example, not an importable workflow export.

```json
{
  "model": "gpt-6-astra",
  "reasoning": {"effort": "max"},
  "instructions": "Review the supplied contract; distinguish facts, risks, and missing evidence.",
  "input": "[authorized extracted contract text]"
}
```

Read output_text content from completed message items in the response's `output` array. On authentication, model-access, rate-limit, or request errors, report failure; do not switch providers or models.


### Self-Hosting vs Cloud

| Option | Pros | Cons |
|--------|------|------|
| **Self-hosted** | Free, full control, data privacy | Maintenance required |
| **n8n Cloud** | No setup, auto-updates | Costs at scale |

```bash
# Docker quick start
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```


## Best Practices

1. **Start with existing templates, customize as needed**
2. **Use error handling nodes for reliability**
3. **Store credentials securely with n8n's credential manager**
4. **Test workflows with sample data before production**

## Installation

```bash
# Install required dependencies
pip install python-docx openpyxl python-pptx reportlab jinja2
```

## Resources

- [n8n Repository](https://github.com/n8n-io/n8n)
- [ChatGPT Office Skills Hub](https://github.com/wealchu/skills)
