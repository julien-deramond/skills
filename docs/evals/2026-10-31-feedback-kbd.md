# Feedback: keys as `<kbd>` elements (2026-10-31)

A maintainer's feedback on #43252: a key the reader presses is a `<kbd>` element in every GitHub text,
issues and PRs alike. The PR description and the review now write <kbd>Delete</kbd>, a typed
<kbd>9</kbd> or <kbd>Shift</kbd>+<kbd>Tab</kbd>, in sentences, tables, lists and the notes, and check
the text for key names before handing it over. Titles and code blocks are left as they are.

New case: `bootstrap-review/evals/otp-readonly-guards` (#43251 at its reviewed commit). The
`bootstrap-fix/evals/otp-supersede-pr` case gained a `<kbd>` grader.

Graded blind, once with the current skills and once with the changed ones:

| Case | Current | Changed |
| --- | --- | --- |
| otp-readonly-guards (new) | 5/7 | 6/7 |
| form-adorn-focus-ring | 7/7 | 7/7 |
| otp-supersede-pr (fix) | 4/7 | 5/7 |

The changed review of the new case still left two keys bare: a typed character in a table and a key
in a parenthesis. The rule then named tables and typed characters and added the check before handing
the text over. One more run of that case with it wrote all 15 keys as `<kbd>` and passed the grader
(6/7 by a non-blind check; it missed the optional point on the `focus()` test).

The `<kbd>` grader failed with the current skills in both cases that have it. No case got worse.

Two more things came out of these runs. The first changed review found a regression the PR's
<kbd>Delete</kbd> handling brings (`input` and `complete` fire when nothing is deleted); the rerun
didn't, so that's run-to-run variance, not this change. And both fix runs, current and changed,
missed the `<fieldset disabled>` case the `otp-supersede-pr` graders ask for.
