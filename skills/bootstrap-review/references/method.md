# Review method

How to reach findings a maintainer can trust. Nothing here is specific to Bootstrap.

## Two axes

Judge the change on two questions, and keep them apart until the recommendation:

- **Spec.** Does it do what the issue asked? All of it, nothing more, and at the cause? List what's
  missing or partial, what wasn't asked for (scope creep), and what looks done but is wrong. Quote the
  issue line each finding rests on. With no issue, the PR description is the spec, and the review
  says so. A fix must cover its topic globally: when the same cause affects sibling components,
  sizes or variants that the PR leaves alone, the fix is incomplete, and the review asks for all of
  them in the same PR.
- **Standards.** Does it follow the project's documented rules and the way the code around it
  already works? Cite the rule or the existing code for each finding. Skip what a linter or CI
  already enforces, unless CI fails.

A change can pass one and fail the other: right code for the wrong problem, or the right fix in the
project's wrong idiom. Tag each finding with its axis, so one doesn't hide the other.

## Find the cause first

Before judging the fix, reproduce the problem and find its cause in the code yourself. The PR's
title and description are a claim. They often describe the symptom ("the border loses its color")
when the cause is elsewhere ("the focus ring of another rule wins the cascade"). A fix for a
misnamed problem can work by accident, miss cases, or add code next to the rule that should change.

## Evidence

Each finding carries the evidence for it:

- **A line**, linked at the pinned commit: `https://github.com/<owner>/<repo>/blob/<sha>/<path>#L<a>-L<b>`.
- **A probe** you wrote from scratch: a small page, a script, a test. Keep it, with its output,
  where the caller keeps evidence, and link it.
- **A measurement**, not an impression: a computed style, a `FormData` entry, a parsed value, a byte
  count, a diff of the build. Put several states side by side in a table (state, before, after).
- **The rendering**, for anything visual: the same page, width, theme and state on both sides.

Say once, in a sentence, what you didn't check (other browsers, dark mode, a mode of the component),
and whether it could change the conclusion.

## Severity

Every finding gets one:

- **Blocking.** Wrong behaviour, a regression, a broken API or markup contract, an accessibility
  failure against a named criterion, a security risk, or a change on the wrong release line.
- **Should change.** Small, in scope, and best fixed in this PR: a missed sibling case, dead or
  redundant code, a wrong default in the docs, a missing test.
- **Optional.** A suggestion or a follow-up. Say it's optional.

## Disprove before you report

Take each finding and try to break it: read the code path again, run the probe on the base too,
look for the rule or the test that already covers it. Then read the posted review sentence by
sentence against the evidence. A finding that doesn't survive is dropped, not
softened. A finding you believe but couldn't confirm is reported as such ("not reproduced").

## Directions

When there's more than one reasonable fix (another open PR, a branch, a simpler change), compare
them: what each changes, its size, the trade-off, whether it breaks anything. Prefer the smallest
change in the place that already handles the case over a new block beside it. Don't invent
directions to have a comparison: one clear fix is one direction.

## Cost against benefit

Weigh what the change buys against what it costs: how often the problem comes up, who hit it, who is
waiting, and the code maintainers will keep. Closing is a valid outcome of a review, with the reason
and the comment drafted, when the problem is rare and cheap to handle by hand, already solved
elsewhere, or out of the project's scope.

## Tests

A change in behaviour comes with a test that fails before it and passes after. Check the PR's tests
for the cases that matter, not only the happy path: a test suite that only types valid input can't
catch a parser that misreads half the inputs.
