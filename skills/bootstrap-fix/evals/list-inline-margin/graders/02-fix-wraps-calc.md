---
type: llm
focus: trace
weight: 1
---

The fix makes the fallback a valid value, for example `calc(var(--spacer) / 2)`, in `scss/content/_lists.scss`, and leaves `--list-inline-padding` working as an override.
