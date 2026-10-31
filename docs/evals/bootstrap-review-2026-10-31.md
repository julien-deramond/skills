# bootstrap-review evals, iteration 1 (2026-10-31)

Ten cases, each run once with the skill and once without, on Opus. Two blind graders scored each run
against the case's graders, checked each run's main finding against the Bootstrap source, and picked
the review they'd rather post.

| | With skill | Without skill |
| --- | --- | --- |
| Grader statements passed | 30 of 33 (91%) | 29 of 33 (88%) |
| Preferred review (one tie) | 7 | 2 |
| Wrong claims found by graders | 2 | 3 |
| Tokens per run, mean | 130k | 114k |
| Time per run, mean | 5.1 min | 4.0 min |

| Case | With skill | Without skill | Preferred |
| --- | --- | --- | --- |
| css-grid-default-in-docs | 3/4 | 4/4 | without, slight |
| css-grid-variable-name | 3/3 | 3/3 | with, slight |
| datepicker-iso-submit | 4/4 | 3/4 | with, clear |
| form-adorn-focus-ring | 4/4 | 4/4 | with, slight |
| hardcoded-z-index | 3/3 | 3/3 | with, slight |
| is-selector-link-regressions | 3/3 | 3/3 | without, slight |
| nuget-prerelease-tags | 2/3 | 2/3 | with, slight |
| radio-switch-radius-approve | 3/3 | 3/3 | tie |
| unused-sass-variables | 2/3 | 2/3 | with, slight |
| vertical-button-group-corners | 3/3 | 2/3 | with, clear |

## What it says

- The graders barely separate the two: Opus without the skill already finds most of what the graders
  ask. The skill's gain shows in the comparisons, and the two clear wins came from evidence the skill
  asks for: compiling and rendering both sides (vertical button group) and more engines, the
  bundle budget and a working alternative (datepicker).
- The skill costs about 15% more tokens and 25% more time per review.
- Neither configuration reached two of the maintainer's own points: asking whether the team had
  agreed to the feature before adding variables (#41372), and whether prerelease tags should publish
  to NuGet at all (#41583).
- When the graders preferred the baseline, it was for a shorter posted review, or for a wrong claim
  in the skill run's review (a hover specificity claim on #40439).

## What to fix in the evals

- **Leaks.** The runs work on today's GitHub, so they can see what happened after the reviewed
  commit: the PR's later commits in `gh pr view --json commits`, its merged state, later releases and
  their CI logs, today's branches, later PRs on the same code. Batch 2 forbade reading today's
  branches, which helped, but the next iteration should give each run a snapshot (the diff, the PR
  description, the issue as it was) instead of live access.
- **Pinning.** A review comment's `commit_id` moves to the PR's latest commit; `original_commit_id` is
  the commit it was written on. The first #40797 case was pinned to the wrong commit, and became
  `css-grid-variable-name`: both runs found a wrong variable name the original review missed.
- **Harder graders.** Statements that a strong model passes without help don't measure the skill.
  The next cases should grade what the maintainer did better than the model: a scope question, the
  length and tone of the posted review, the alternative it offered.
- **Running them.** Subagents can't write a file named `report.md` (the harness refuses it), so most
  runs wrote their outputs through the shell. `claude plugin eval` runs each case as its own session
  and avoids that, and the parent session's context too.
