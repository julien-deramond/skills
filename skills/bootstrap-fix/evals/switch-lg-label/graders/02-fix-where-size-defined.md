---
type: llm
focus: trace
weight: 1
---

The fix is small in each file and sits where the large size is defined (`scss/forms/_switch.scss`, plus `_check.scss` and `_radio.scss` when they share the cause): it removes or corrects the fixed block margin of the large size, without changing the default and small sizes.
