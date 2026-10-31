# Feedback: keep the full analysis on the PR (2026-10-31)

A maintainer's feedback on the review of #43233: an approval that only summarizes the checks loses
the analysis and the non-regression testing behind it. The review to post now has two parts, a short
message and a collapsed "Review notes" block with the full public analysis, and a PR description
carries the same collapsed notes.

New case: `bootstrap-review/evals/form-label-tokens-approve` (#43233 at its reviewed commit). The
length graders now leave the collapsed notes out, and four neighbouring cases gained a notes grader.

Tested on five cases, once with the changed skills and once with the previous version, graded blind:

| Case | Previous | Changed | Preferred |
| --- | --- | --- | --- |
| form-label-tokens-approve (new) | 3/6 | 6/6 | changed, clear |
| radio-switch-radius-approve | 4/5 | 5/5 | changed, clear |
| form-adorn-focus-ring | 6/7 | 7/7 | changed, slight |
| list-inline-margin (fix) | 5/7 | 6/7 | changed, slight |
| switch-lg-label (fix) | 5/8 | 8/8 | changed, clear |
| Total | 23/33 | 32/33 | changed in all 5 |

The new case fails without the change and passes with it, and no other case got worse.
