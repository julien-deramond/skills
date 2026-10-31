---
type: llm
focus: trace
weight: 1
---

The fix fires no `input.bs.otpInput` or `complete.bs.otpInput` event for a key that changes nothing (<kbd>Delete</kbd> after the last character, <kbd>Backspace</kbd> before the first one), and the report shows it was checked: the events counted on the base and on the fix, in a probe or a unit test, not only the value and the DOM.
