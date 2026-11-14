---
# ═══════════════════════════════════════════════════════════════════════════════
# CHATGPT OFFICE SKILL - Enhanced Metadata v2.0
# ═══════════════════════════════════════════════════════════════════════════════

# Basic Information
name: md-slides
description: ">"
version: "1.0"
author: wealchu
license: MIT

# Categorization
category: presentation
tags:
  - markdown
  - slides
  - marp
department: All

# AI Model Compatibility
models:
  recommended:
    - gpt-6-astra
  compatible:
    - gpt-6-astra

# MCP Tools Integration
mcp:
  server: office-mcp
  tools:
    - md_to_pptx

# Skill Capabilities
capabilities:
  - markdown_slides
  - presentation_generation

# Language Support
languages:
  - en
  - zh
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# Markdown Slides Skill

## Overview

This skill enables creation of presentations from pure Markdown using **Marp**. Write slides in familiar Markdown syntax and export to PDF, PPTX, or HTML with professional themes.

## How to Use

1. Write or provide Markdown content
2. I'll format it for Marp with proper directives
3. Export to your preferred format (PDF/PPTX/HTML)

**Example prompts:**
- "Convert my notes to a presentation"
- "Create slides from this markdown"
- "Build a pitch deck using markdown"
- "Generate PDF slides from this outline"

## Domain Knowledge

### Basic Syntax

```markdown
---
marp: true
---

# First Slide

Content here

---

# Second Slide

- Bullet 1
- Bullet 2
```

### Themes

```markdown
---
marp: true
theme: default  # default, gaia, uncover
---
```

### Directives

```markdown
---
marp: true
theme: gaia
class: lead        # Centered title
paginate: true     # Page numbers
header: 'Header'   # Header text
footer: 'Footer'   # Footer text
backgroundColor: #fff
---
```

### Images

```markdown
![width:500px](image.png)
![bg](background.jpg)
![bg left:40%](sidebar.jpg)
```

### Columns

```markdown
<div class="columns">
<div>

## Left

Content

</div>
<div>

## Right

Content

</div>
</div>
```

## Example

```markdown
---
marp: true
theme: gaia
paginate: true
---

<!-- _class: lead -->

# Project Update

Q4 2024 Review

---

# Highlights

- Revenue: +25%
- Users: +50%
- NPS: 72

---

# Roadmap

| Q1 | Q2 | Q3 | Q4 |
|----|----|----|-----|
| MVP | Beta | Launch | Scale |

---

<!-- _class: lead -->

# Thank You!

questions@company.com
```

## CLI Usage

```bash
# Install
npm install -g @marp-team/marp-cli

# Convert
marp slides.md -o presentation.pdf
marp slides.md -o presentation.pptx
marp slides.md -o presentation.html
```

## Resources

- [Marp Documentation](https://marp.app/)
- [GitHub](https://github.com/marp-team/marp)
