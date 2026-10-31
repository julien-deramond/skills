# Feedback: check a JavaScript change's events (2026-10-31)

A maintainer's fix superseding #43251 shipped a regression (#43252, fixed by #43255): a
<kbd>Delete</kbd> with nothing after the caret still fired `input` and, on a full code, `complete`
again. Its impact check compared the value, the active slot and the DOM on every variant, but never
counted the component's events. The fix now checks a JavaScript change's events and public methods
on both sides with real input, including the keys and calls that change nothing, in the probe and in
a unit test.

The `bootstrap-fix/evals/otp-supersede-pr` case gained an events grader. Graded blind, once with the
current skill and once with the changed one:

| Case | Current | Changed | Preferred | Events counted on both sides |
| --- | --- | --- | --- | --- |
| otp-supersede-pr | 6/8 | 5/8 | changed, slight | current: `input` only; changed: `input` and `complete` |
| strength-text-color | 5/6 | 6/6 | changed, slight | current: no; changed: yes (`strengthChange`, 30 on each side) |

Both runs of `otp-supersede-pr` passed the events grader this time. The two runs of the same case
in the `<kbd>` round, made with the skill before this rule, both kept the regression. Across the
four runs without the rule, one counted the events and one avoided the regression. With it, both
runs counted them. `otp-supersede-pr`'s changed run lost a point on the description's length (233
words against 200), not on the fix. Both of its runs still missed `<fieldset disabled>` and the
OTP variants, so those graders stay open.
