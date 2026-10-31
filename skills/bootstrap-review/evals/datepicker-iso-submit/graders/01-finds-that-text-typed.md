---
type: llm
focus: trace
weight: 1
---

The review finds that text typed into the input is parsed with `new Date()`, so a day-first locale (en-GB, fr-FR, de-DE) submits the wrong date or none, with a probe or a table of locales as evidence.
