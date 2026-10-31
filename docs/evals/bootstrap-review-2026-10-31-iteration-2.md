# bootstrap-review evals, iteration 2 (2026-10-31)

Eleven cases, each run once with the skill and once without, on Opus, then scored by two blind
graders. Three things changed since [iteration 1](bootstrap-review-2026-10-31.md):

- **Frozen snapshots.** Each run got the PR as it was at review time and nothing else, built by
  `scripts/bootstrap-pr-snapshot.py`. That's the description as of that date, the commits up to the
  reviewed one, the diff, CI at that commit, the linked issues with their earlier comments, and the
  base tree without history. There was no network. The graders found no use of later information.
- **Harder graders.** Every case gained a grader on the posted review's length. Three cases gained
  one on what the maintainer did better: the bundle budget, the controls the fix also covers, and a
  wrong specificity claim. One held-out case was added, `cursor-utilities-feature` (#42088).
- **Skill changes.** Every claim in the posted review rests on evidence. A feature needs a
  maintainer's yes in the issue first. The posted review stays under 150 words for one finding and
  under 300 for several. A release workflow raises the prerelease question. A claim about which rule
  wins is measured, not worked out.

| | With skill | Without skill |
| --- | --- | --- |
| Grader statements passed | 48 of 50 (96%) | 37 of 50 (74%) |
| Without the length graders | 39 of 39 | 33 of 39 (85%) |
| Preferred review | 10, one tie | 0 |
| Wrong claims found by graders | 1 | 3 |
| Posted review, median words | 188 | 274 |
| Tokens per run, mean | 123k | 105k |
| Time per run, mean | 3.9 min | 3.3 min |

| Case | With skill | Without skill | Preferred |
| --- | --- | --- | --- |
| css-grid-default-in-docs | 5/5 | 5/5 | with, slight |
| css-grid-variable-name | 4/4 | 4/4 | with, slight |
| cursor-utilities-feature (held out) | 3/4 | 1/4 | with, clear |
| datepicker-iso-submit | 6/6 | 5/6 | with, clear |
| form-adorn-focus-ring | 6/6 | 6/6 | with, slight |
| hardcoded-z-index | 4/4 | 3/4 | with, slight |
| is-selector-link-regressions | 5/5 | 3/5 | with, clear |
| nuget-prerelease-tags | 3/4 | 2/4 | with, clear |
| radio-switch-radius-approve | 4/4 | 4/4 | tie |
| unused-sass-variables | 4/4 | 2/4 | with, clear |
| vertical-button-group-corners | 4/4 | 2/4 | with, clear |

## What it says

- With the snapshots and the new graders, the two configurations separate: the graders preferred
  the skill's review in every case but one tie, against seven of ten in iteration 1.
- The baseline's six misses outside the length graders:
  - Two are on the feature-agreement question (#41372, #42088).
  - One is on the prerelease question (#41583).
  - One is on pointing to the Utilities API (#42088).
  - Two are evidence from one side only (#40488, #40439). It worked the PR's result out from the Sass
    instead of building it, which it did do in iteration 1.
- The held-out case is the best sign that the agreement rule generalizes: the skill recommended
  closing an unagreed feature and pointed to the Utilities API. The baseline asked for cleanup of a
  feature nobody had agreed to. It's one case.
- The skill still went over the word limit twice (185 words where 150 was the limit, 251 where 250 was).

## Limits

- **One run per configuration.** The baseline built both sides in iteration 1 and didn't in
  iteration 2. That swing is noise, and it decides two of the clear preferences.
- **The new rules came from iteration 1's failures.** The graders on agreement, prereleases and length
  test what the skill was just told to do. Only the held-out case checks that beyond its source.
- **The limits are this skill's preference.** The skill knows the word limits, and the baseline
  doesn't, so those graders measure a style the skill asks for.
- **The skill costs more.** About 17% more tokens and 20% more time per review.

## Next

- Three runs per configuration on the cases that decided a preference, to measure the variance.
- More held-out cases from the review history, written before any change to the skill.
- Run with `claude plugin eval`, one session per case, when it's available here.
