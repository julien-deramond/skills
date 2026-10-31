---
type: llm
focus: trace
weight: 1
---

The guards check disabled with `matches(':disabled')` (or an equivalent that covers an input inside `<fieldset disabled>`), not the `disabled` property alone, and a test covers the fieldset case.
