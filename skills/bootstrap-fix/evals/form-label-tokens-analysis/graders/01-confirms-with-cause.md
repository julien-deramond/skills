---
type: llm
focus: trace
weight: 1
---

The analysis confirms the bug and finds that `scss/forms/_labels.scss` builds `$form-label-tokens` but never includes `tokens()` (and does not import the tokens mixin), so a Sass override of the map changes nothing, shown with a build or a probe, not from reading the Sass alone.
