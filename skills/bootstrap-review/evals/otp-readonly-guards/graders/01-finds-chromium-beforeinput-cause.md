---
type: llm
focus: trace
weight: 1
---

The review finds that the bug is real and why: `_handleBeforeInput` cancels `beforeinput` and writes the character itself without checking the input, and Chromium fires `beforeinput` for typed text in a `readonly` input, so typing changes a readonly field there (Firefox and WebKit don't fire it). The claim rests on a probe or a measurement, not on reading alone.
