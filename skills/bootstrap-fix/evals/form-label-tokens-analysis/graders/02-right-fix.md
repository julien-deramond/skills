---
type: llm
focus: trace
weight: 1
---

The analysis names the right fix: `@include tokens($form-label-tokens)` on both `.form-label` and `.col-form-label`, with the `mixins/tokens` import, and nothing beyond what that needs.
