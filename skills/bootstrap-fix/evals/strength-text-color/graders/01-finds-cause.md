---
type: llm
focus: trace
weight: 1
---

The run finds that the JavaScript sets an inline `--strength-color` on the text element pointing to a variable that doesn't exist (`--danger-text` and the like), and that the text sits next to `.strength`, so it can't use the meter's color.
