---
type: llm
focus: trace
weight: 1
---

The fix adds `@include tokens($form-label-tokens)` to both `.form-label` and `.col-form-label`, with the `mixins/tokens` import, and nothing beyond what that needs.
