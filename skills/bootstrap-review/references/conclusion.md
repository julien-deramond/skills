# One conclusion per issue

An issue has one right conclusion. Analyzing the issue, fixing it and reviewing a PR for it are three
ways to reach that conclusion. All three reach the same one, with the same work. Only what you hand
over differs: an analysis gives the conclusion, a fix gives the branch, a review gives the decision on
the PR.

## The same work, whatever the way in

Do all of it before you decide, in this order:

1. **Read the whole thread and look for related work.** The issue, its comments, the items it links,
   duplicates and earlier answers (`gh search issues "<key words>" -R twbs/bootstrap`), and other open
   PRs or branches on the same issue or the same files (`gh search prs "<key words>" -R twbs/bootstrap`).
   Note who waits on whom, and since when. When a search isn't possible, say so.
2. **Pin the release line and load the project's rules from the base**, not from memory.
3. **Reproduce from scratch on the base**, find the cause in the code, then every place the same cause
   lives (sibling components, every size and variant, the docs examples, RTL copies).
4. **Reach the conclusion** (below).
5. **When it's confirmed, define the right fix**: the smallest change in the place that already handles
   the case, every place the cause lives, its test, its docs, and the backport to the other release line.
6. **Check the right fix.** Write it in a scratch copy of the base even when you hand over no branch,
   and check it the way a fix is checked: the checks the change touches, the compiled CSS diff from a
   build of both sides, before and after evidence for a visual change, and the impact on every
   component it touches (all states, sizes, variants, docs usages and odd cases, and for JavaScript
   its events and methods, counted on both sides). A review runs the same checks on the PR's change,
   rebuilt from scratch when the PR is untrusted.
7. **Try to disprove each claim** before you keep it.

**Stop early for the same reasons on every way in**, and give the reason: the item is suspicious, it's a
question, a duplicate or already fixed (with the link), it doesn't reproduce, it's a feature nobody on
the team agreed to yet, or, for a PR, it doesn't build, fails lint, or targets the wrong branch or
repository. Don't run the rest of the work after a stop.

## The conclusion

One of these, with its evidence:

- **Refused**, with one reason: by design (the docs say so), already fixed (the commit or PR), can't
  reproduce, a duplicate (the issue), a question or a support request, out of scope, a v5 change that
  isn't a patch-level fix, or more code than the problem justifies.
- **Waiting on a maintainer**: a feature (a new class, option, variable, utility or component) with no
  maintainer's yes in the issue, or a choice of scope, design or breaking change. Give the options and
  the one you recommend. When the options are implementations, each one is a direction.
- **Confirmed**: the bug, its cause, and the right fix. When there are several reasonable fixes, the
  directions (three at most) and the recommended one. Don't invent directions: one clear fix is one.

## A PR against the conclusion

Reach the issue's conclusion on your own first, then measure the PR against it. With no linked issue,
the PR's description is the issue.

| The PR against the conclusion | Decision |
| --- | --- |
| The issue is refused, or waits on a maintainer | Close or comment, with the reason and the pointer (the docs, the duplicate, the issue to discuss first) |
| The same fix: the same cause, every place it lives, its test and docs, nothing else, checks pass | Approve, with optional suggestions at most |
| The same direction, with gaps the author can close in this PR (a missed place, a test, docs, the project's idiom, a rebase) | Request changes, each gap with its fix |
| The right issue, but the fix is wrong or too far to close with review comments, or the author stopped answering, and the work is worth keeping (the cause, the report, the tests) | Supersede it: the right fix on a branch of your own, with the author in a `Co-authored-by:` trailer and "Supersedes #<n>" in its description. The review says so and thanks the author |
| Far from the conclusion, with nothing to keep | Close, with the reason and the pointer to the right fix |

## An earlier conclusion

When an analysis, a fix or a review of the same issue already exists, do the work anyway, then compare.
When yours differs, say which one is right and why.
