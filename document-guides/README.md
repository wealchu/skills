# ChatGPT document guides

These guides are maintained for this fork. They are not official OpenAI skills and do not prove that a tool is installed. Use the relevant installed document skill and approved tools in the current environment.

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

- [Word documents](docx-guide.md) — [docx-manipulation](../docx-manipulation/SKILL.md)
- [Excel spreadsheets](xlsx-guide.md) — [xlsx-manipulation](../xlsx-manipulation/SKILL.md)
- [PowerPoint presentations](pptx-guide.md) — [pptx-manipulation](../pptx-manipulation/SKILL.md)
- [PDF documents](pdf-guide.md) — [pdf-extraction](../pdf-extraction/SKILL.md)
- [Internal communications](internal-comms.md) — [email-drafter](../email-drafter/SKILL.md)
- [Document coauthoring](doc-coauthoring.md) — [docx-manipulation](../docx-manipulation/SKILL.md)
