---
type: llm
focus: trace
weight: 1
---

The fix moves the indicator to the inline end for all five types (`date`, `datetime-local`, `month`, `week`, `time`), either by the issue's `display: block` for those types or by positioning the indicator at the inline end, and it uses logical properties.
