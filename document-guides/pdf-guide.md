# PDF documents

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

Inventory pages and distinguish selectable text from scanned images. Inspect significant tables and figures visually. Preserve original files. Validate page count, reading order, text completeness, and the appearance of every edited page.

Use [pdf-extraction](../pdf-extraction/SKILL.md). Verify actual tool availability before making capability claims.
