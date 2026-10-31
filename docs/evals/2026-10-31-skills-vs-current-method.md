# The skills against the current method (2026-10-31)

The question: are `bootstrap-review` and `bootstrap-fix` at least as good as the method maintainers
already use for Bootstrap, written down as a guide for agents? Each case ran once with the skill and
once with that guide, on Opus, on the same frozen snapshot with no network. Blind graders scored
each run, checked the claims against the source, and picked the one they'd rather post. For fixes,
they applied and built each recommended patch and compared it with the fix the team merged.

## Reviews: 11 pull requests

| | Skill | Current method |
| --- | --- | --- |
| Grader statements passed | 48 of 50 (96%) | 42 of 50 (84%) |
| Without the length graders | 39 of 39 | 37 of 39 |
| Preferred review | 11 (6 clear, 5 slight) | 0 |
| Wrong claims found | 1 | 2 |
| Tokens and time per run | 123k, 3.9 min | 124k, 3.7 min |

Both methods found the same problems. The skill won on two things:

- **Evidence from both sides.** In #40488 and #40439 the current method worked out the PR's effect
  from the Sass or from specificity math. The skill built and measured it.
- **Shorter posted reviews.** Six of the current method's eight misses are the length limit. The
  current method never sets one, so this grader measures a preference the skill states.

One grader also counted the "Generated with Claude Code" line at the end of a posted review as a
weakness. The current method requires that line, so the comparison leans slightly against it.

## Fixes: 6 issues the team fixed

| | Skill | Current method |
| --- | --- | --- |
| Grader statements passed | 24 of 30 (80%) | 24 of 30 (80%) |
| Preferred fix | 4, all slight | 2, both slight |
| Patches that apply and build | 6 of 6 | 6 of 6 |
| Tokens and time per run | 147k, 7.1 min | 150k, 6.2 min |

The fixes themselves are a tie. Both found the real cause in every case. In #43065 both patches are
byte-identical to the merged fix. In four cases the two methods compiled to the same CSS. Where they
went past the merged fix (#43174: `display: block` on `.form-control` and flex only on
`.form-adorn`; #43179: the same margin fix for the large checkbox and radio), they did it the same
way.

The points were lost on two things both methods share:

- **The PR description.** The skill followed Bootstrap's `AGENTS.md` and wrote bullets three
  times, and used the repository's PR template once. The current method went over 200 words four
  times.
- **Scope.** Both removed unused negative-margin keys in #43002, and both fixed the large checkbox
  and radio next to the switch in #43179. The graders counted these as out of scope. The skill
  tells it to fix the same pattern where it repeats, so this is a rule to settle, not a slip.

## Verdict

- **Reviews:** better than the current method. The gain is measured evidence and shorter reviews,
  not more findings.
- **Fixes:** as good as the current method, not better yet. Two rules decide the next gain: the PR
  description format for twbs/bootstrap, and whether a fix's siblings belong in the same PR.

## Limits

- One run per configuration and per case.
- The review runs with the skill come from iteration 2, regraded here with the current method's
  runs. Same snapshots, same skill version.
- Some runs shared the desktop app's browser pane, and one run's script ran in another run's tab.
  The next round should give each run its own headless browser only.
