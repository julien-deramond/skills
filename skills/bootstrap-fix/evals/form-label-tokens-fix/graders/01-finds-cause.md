---
type: llm
focus: trace
weight: 1
---

The run finds that `scss/forms/_labels.scss` builds `$form-label-tokens` but never includes `tokens()` (and doesn't import the tokens mixin), so a Sass override of the map changes nothing.
