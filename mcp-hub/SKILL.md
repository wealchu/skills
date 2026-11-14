---
# ═══════════════════════════════════════════════════════════════════════════════
# CHATGPT OFFICE SKILL - Enhanced Metadata v2.0
# ═══════════════════════════════════════════════════════════════════════════════

# Basic Information
name: mcp-hub
description: "Access 1200+ AI Agent tools via Model Context Protocol (MCP)"
version: "1.0"
author: wealchu
license: MIT

# Categorization
category: workflow
tags:
  - mcp
  - hub
  - tools
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
  - tool_discovery
  - mcp_integration

# Language Support
languages:
  - en
  - zh
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# Mcp Hub Skill

## Overview

This skill provides access to 1200+ MCP (Model Context Protocol) servers - standardized tools that extend AI capabilities. Connect ChatGPT to filesystems, databases, APIs, and document processing tools.

## How to Use

1. Describe what you want to accomplish
2. Provide any required input data or files
3. I'll execute the appropriate operations

**Example prompts:**
- "Access local filesystem to read/write documents"
- "Query databases for data analysis"
- "Integrate with GitHub, Slack, Google Drive"
- "Run document processing tools"

## Domain Knowledge


### MCP Architecture

```
ChatGPT ←→ MCP Server ←→ External Resource
        (Protocol)      (Files, APIs, DBs)
```

### Popular Document MCP Servers

| Server | Function | Stars |
|--------|----------|-------|
| **filesystem** | Read/write local files | Official |
| **google-drive** | Access Google Docs/Sheets | 5k+ |
| **puppeteer** | Browser automation, PDF gen | 10k+ |
| **sqlite** | Database queries | Official |

### Configuration Example

Use the installed Google Drive connection for authorized Drive tasks. Do not install a guessed MCP package. For this repository's document server, follow CHATGPT_CONFIGURATION.md and verify the actual connection in the chosen host.


### MCP Tool Discovery

Browse available servers:
- [mcp.run](https://mcp.run) - MCP marketplace
- [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)
- [mcp-awesome.com](https://mcp-awesome.com)

### Using MCP in Skills

```python
# MCP tools become available to ChatGPT automatically
# Example: filesystem MCP provides these tools:

# read_file(path) - Read file contents
# write_file(path, content) - Write to file
# list_directory(path) - List directory contents
# search_files(query) - Search for files
```


## Best Practices

1. **Only enable MCP servers you need (security)**
2. **Use official servers when available**
3. **Check server permissions before enabling**
4. **Combine multiple servers for complex workflows**

## Installation

```bash
# Install required dependencies
pip install python-docx openpyxl python-pptx reportlab jinja2
```

## Resources

- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
- [ChatGPT Office Skills Hub](https://github.com/wealchu/skills)
