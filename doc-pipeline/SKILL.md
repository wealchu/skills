---
# ═══════════════════════════════════════════════════════════════════════════════
# CHATGPT OFFICE SKILL - Enhanced Metadata v2.0
# ═══════════════════════════════════════════════════════════════════════════════

# Basic Information
name: doc-pipeline
description: "Chain document operations into reusable pipelines"
version: "1.0"
author: wealchu
license: MIT

# Categorization
category: workflow
tags:
  - pipeline
  - workflow
  - document
  - automation
department: All

# AI Model Compatibility
models:
  recommended:
    - gpt-6-astra
  compatible:
    - gpt-6-astra

# Skill Capabilities
capabilities:
  - document_workflow
  - pipeline_automation

# Language Support
languages:
  - en
  - zh
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# Doc Pipeline Skill

## Overview

This skill enables building document processing pipelines - chain multiple operations (extract, transform, convert) into reusable workflows with data flowing between stages.

## How to Use

1. Describe what you want to accomplish
2. Provide any required input data or files
3. I'll execute the appropriate operations

**Example prompts:**
- "PDF → Extract Text → Translate → Generate DOCX"
- "Image → OCR → Summarize → Create Report"
- "Excel → Analyze → Generate Charts → Create PPT"
- "Multiple inputs → Merge → Format → Output"

## Domain Knowledge


### Pipeline Architecture

```
Stage 1      Stage 2      Stage 3      Stage 4
┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
│Extract│ → │Transform│ → │ AI   │ → │Output│
│ PDF  │    │  Data  │    │Analyze│   │ DOCX │
└──────┘    └──────┘    └──────┘    └──────┘
     │           │           │           │
     └───────────┴───────────┴───────────┘
                 Data Flow
```

### Pipeline DSL (Domain Specific Language)

```yaml
# pipeline.yaml
name: contract-review-pipeline
description: Extract, analyze, and report on contracts

stages:
  - name: extract
    operation: pdf-extraction
    input: $input_file
    output: $extracted_text
    
  - name: analyze
    operation: ai-analyze
    input: $extracted_text
    prompt: "Review this contract for risks..."
    output: $analysis
    
  - name: report
    operation: docx-generation
    input: $analysis
    template: templates/review_report.docx
    output: $output_file
```

### Python Implementation

```python
from typing import Callable, Any
from dataclasses import dataclass

@dataclass
class Stage:
    name: str
    operation: Callable
    
class Pipeline:
    def __init__(self, name: str):
        self.name = name
        self.stages: list[Stage] = []
    
    def add_stage(self, name: str, operation: Callable):
        self.stages.append(Stage(name, operation))
        return self  # Fluent API
    
    def run(self, input_data: Any) -> Any:
        data = input_data
        for stage in self.stages:
            print(f"Running stage: {stage.name}")
            data = stage.operation(data)
        return data

# Example usage
pipeline = Pipeline("contract-review")
pipeline.add_stage("extract", extract_pdf_text)
pipeline.add_stage("analyze", analyze_with_ai)
pipeline.add_stage("generate", create_docx_report)

result = pipeline.run("/path/to/contract.pdf")
```

### Advanced: Conditional Pipelines

```python
class ConditionalPipeline(Pipeline):
    def add_conditional_stage(self, name: str, condition: Callable, 
                               if_true: Callable, if_false: Callable):
        def conditional_op(data):
            if condition(data):
                return if_true(data)
            return if_false(data)
        return self.add_stage(name, conditional_op)

# Usage
pipeline.add_conditional_stage(
    "ocr_if_needed",
    condition=lambda d: d.get("has_images"),
    if_true=run_ocr,
    if_false=lambda d: d
)
```


## Best Practices

1. **Keep stages focused (single responsibility)**
2. **Use intermediate outputs for debugging**
3. **Implement stage-level error handling**
4. **Make pipelines configurable via YAML/JSON**

## Installation

```bash
# Install required dependencies
pip install python-docx openpyxl python-pptx reportlab jinja2
```

## Resources

- [Custom Repository](https://github.com/wealchu/skills)
- [ChatGPT Office Skills Hub](https://github.com/wealchu/skills)
