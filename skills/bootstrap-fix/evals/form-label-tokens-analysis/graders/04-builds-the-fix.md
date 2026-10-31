---
type: llm
focus: trace
weight: 1
---

The analysis writes the right fix in a scratch copy and builds both sides, and shows the compiled CSS diff (a default build gains only the `--bs-label-margin-bottom` declarations, since the `null` tokens are dropped), not a diff worked out on paper.
