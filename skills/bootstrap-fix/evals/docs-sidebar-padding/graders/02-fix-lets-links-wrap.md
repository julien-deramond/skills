---
type: llm
focus: trace
weight: 1
---

The fix lets the sidebar links wrap (for example `white-space: normal` on `.bd-sidebar .nav-link` in `site/src/scss/_sidebar.scss`) or an equivalent change that removes the scrollbar without hiding content, rather than only removing the padding.
