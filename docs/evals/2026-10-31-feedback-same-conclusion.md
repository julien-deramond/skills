# Feedback: one conclusion, the same work (2026-10-31)

A maintainer's feedback: analyzing an issue, fixing it and reviewing a PR for it should reach the same
conclusion, with the same tests, analysis and cross-references. The conclusion can be to refuse the
issue, to confirm it and open the right fix, or, for a PR, to approve it, ask for changes, supersede it
with its author as co-author, or close it. The two skills shared their criteria but decided in their
own words, and the depth of work differed: the fix ran the most checks, the review searched the most
cross-references, and an analysis without a branch had no minimum.

The change adds `bootstrap-review/references/conclusion.md`: the same work on every way in, the same
reasons to stop early, the conclusions, and the decision a PR gets from how far it is from the
conclusion. bootstrap-review reaches the issue's conclusion before it judges the PR and checks as
much as a fix does. bootstrap-fix covers analyses, gains the search for related work, and gives an
open PR on the same issue the same decision a review would.

A new case, `bootstrap-fix/evals/form-label-tokens-analysis`, analyzes #43231 and expects what the fix
of that issue and the review of #43233 find. `form-label-tokens-approve` gained graders for the other
token maps and the impact, `otp-readonly-guards` for the events and the variants: the work the
matching fix does. Graded blind, once with the current skills and once with the changed ones:

| Case | Current | Changed | Preferred |
| --- | --- | --- | --- |
| form-label-tokens-analysis | 5/6 | 6/6 | changed, slight |
| form-label-tokens-approve | 7/8 | 7/8 | current, slight |
| otp-readonly-guards | 7/9 | 7/9 | changed, clear |

All six runs reached the same conclusion as the other ways in: the label bug confirmed with the same
two-line fix and `$drawer-backdrop-tokens` as a separate problem, #43233 approved, #43251 sent back for
the `<fieldset disabled>` case. The changed OTP review counted `input.bs.otpInput` on both sides and
found that the PR's new <kbd>Delete</kbd> branch fires it when nothing is deleted, the regression the
merged #43252 later shipped; the current one copied that branch into its own fix. The changed analysis
checked the docs usages of the labels; the current one didn't.

Still open: neither review checked the docs examples of the labels or the OTP variants, and the
changed OTP review asked to drop guards that can't run where the grader expected an optional note.
