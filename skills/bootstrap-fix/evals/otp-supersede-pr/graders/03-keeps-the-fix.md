---
type: llm
focus: trace
weight: 1
---

The fix stops Chromium's `beforeinput` from editing a readonly field, stops a disabled input from remembering a tap on `pointerdown`, and handles Delete like Backspace, each with a test that fails on the base.
