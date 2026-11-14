---
# ═══════════════════════════════════════════════════════════════════════════════
# CHATGPT OFFICE SKILL - Enhanced Metadata Template v2.0
# ═══════════════════════════════════════════════════════════════════════════════
# 
# This template defines a Skill as a "Scenario-based Solution Guide"
# Skills tell AI "WHAT" to do and "HOW" to do it
# MCP tools provide "WITH WHAT" to accomplish tasks
#
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────────
# BASIC INFORMATION (Required)
# ─────────────────────────────────────────────────────────────────────────────────
name: skill-name
description: >
  A clear, concise description of what this skill does (1-2 sentences).
  Focus on the VALUE it provides to the user.
version: 1.0.0
author: wealchu
license: MIT

# ─────────────────────────────────────────────────────────────────────────────────
# CATEGORIZATION (Required)
# ─────────────────────────────────────────────────────────────────────────────────
category: legal  # Primary category: legal | hr | finance | sales | marketing | productivity | pdf | document | spreadsheet | presentation | workflow
tags:
  - contract      # Domain tags
  - review        # Action tags
  - risk-analysis # Feature tags
department: Legal  # Target department/user group

# ─────────────────────────────────────────────────────────────────────────────────
# AI MODEL COMPATIBILITY (Optional)
# ─────────────────────────────────────────────────────────────────────────────────
models:
  recommended:
    - gpt-6-astra
  compatible:
    - gpt-6-astra

# ─────────────────────────────────────────────────────────────────────────────────
# MCP TOOLS INTEGRATION (Required for tool-using skills)
# ─────────────────────────────────────────────────────────────────────────────────
# Skills are "solution guides" - MCP provides the actual tools
mcp:
  server: office-mcp  # Which MCP server provides the tools
  tools:              # Tools this skill uses (from office-mcp)
    - extract_text_from_pdf
    - extract_text_from_docx
    - analyze_document_structure
  optional_tools:     # Nice-to-have tools
    - create_docx
    - docx_to_pdf

# ─────────────────────────────────────────────────────────────────────────────────
# EXTERNAL DATA SOURCES (Optional - for data-driven skills)
# ─────────────────────────────────────────────────────────────────────────────────
# data_sources:
#   - name: Alpha Vantage
#     url: https://www.alphavantage.co/
#     type: api
#     api_key_required: true
#     rate_limit: "5 requests/minute (free tier)"
#   - name: Yahoo Finance
#     url: https://finance.yahoo.com/
#     type: web
#     api_key_required: false

# ─────────────────────────────────────────────────────────────────────────────────
# INPUT/OUTPUT SPECIFICATION (Recommended)
# ─────────────────────────────────────────────────────────────────────────────────
input:
  required:
    - type: file
      formats: [pdf, docx]
      description: The contract document to review
    - type: text
      name: party_role
      description: Which party you are (employee, contractor, buyer, etc.)
  optional:
    - type: text
      name: jurisdiction
      description: Legal jurisdiction (US, EU, China, etc.)
    - type: text
      name: concerns
      description: Specific areas of concern

output:
  primary:
    type: report
    format: markdown
    sections:
      - risk_summary
      - detailed_findings
      - recommendations
  artifacts:
    - type: file
      name: analysis_report.md
      description: Detailed analysis report

# ─────────────────────────────────────────────────────────────────────────────────
# SKILL CAPABILITIES (For discovery/matching)
# ─────────────────────────────────────────────────────────────────────────────────
capabilities:
  - contract_analysis
  - risk_identification
  - legal_compliance_check
  - negotiation_recommendations

# ─────────────────────────────────────────────────────────────────────────────────
# LANGUAGE SUPPORT
# ─────────────────────────────────────────────────────────────────────────────────
languages:
  - en  # English
  - zh  # Chinese

# ─────────────────────────────────────────────────────────────────────────────────
# RELATED SKILLS (For navigation/discovery)
# ─────────────────────────────────────────────────────────────────────────────────
related_skills:
  - nda-generator
  - offer-letter
  - proposal-writer
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# Skill Name

## Overview

[Clear explanation of what this skill does and when to use it]

**What I can do:**
- [Capability 1]
- [Capability 2]
- [Capability 3]

**What I cannot do:**
- [Limitation 1]
- [Limitation 2]

---

## How to Use Me

### Step 1: [First Step]
[Instructions]

### Step 2: [Second Step]
[Instructions]

### Step 3: [Third Step]
[Instructions]

---

## Domain Knowledge

[This is where the real value lives - embedded expertise, patterns, rules, best practices]

### [Knowledge Area 1]
[Details]

### [Knowledge Area 2]
[Details]

---

## Output Format

[Define the structure of outputs this skill produces]

```
## [Output Title]

### Section 1
[Content pattern]

### Section 2
[Content pattern]
```

---

## Examples

### Example 1: [Scenario]
**User**: [Example input]
**AI**: [Example output]

### Example 2: [Scenario]
**User**: [Example input]
**AI**: [Example output]

---

## Tips for Better Results

1. [Tip 1]
2. [Tip 2]
3. [Tip 3]

---

## Limitations

- [Limitation 1]
- [Limitation 2]
- [Limitation 3]

---

*Built by the ChatGPT Office Skills community. Contributions welcome!*
