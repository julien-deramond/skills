---
type: llm
focus: trace
weight: 1
---

The run confirms the cause: `.form-control`'s `display: flex` makes Chrome's internal date-time box a flex item, so `::-webkit-calendar-picker-indicator` sits right after the value.
