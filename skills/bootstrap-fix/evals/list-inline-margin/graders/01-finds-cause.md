---
type: llm
focus: trace
weight: 1
---

The run finds that `var(--spacer) / 2`, used as the fallback inside `var(--list-inline-padding, …)`, is not computed: a division outside `calc()` is invalid there, so the declaration is dropped.
