---
name: bootstrap-fix
description: Turn a twbs/bootstrap issue into a fix a maintainer can open as a pull request in minutes - reproduce it, find the cause, write the smallest fix in the project's conventions with its test, and write the PR description - or say why no fix should be made. Use it whenever asked to fix a Bootstrap issue ("fix #<n>", "prepare a branch for this bug"), to prepare the alternative approach a review asked for, to compare competing directions as working branches, or to write or rewrite the description of a Bootstrap PR. Covers v6 (`main`), v5 (`v5-dev`) and the frozen docs (`gh-pages`). Install it with bootstrap-review, whose references it reads.
metadata:
  author: Julien Déramond
  version: "2026.10.31"
  status: draft
  category: fix
---

# Bootstrap fix

A fix is ready when a maintainer can read its description, look at the diff, and open the PR
without redoing any of the work. That means the cause is found, the fix covers the topic everywhere it
reaches, each change is the smallest one in the place that already handles the case, its impact
is checked on everything it touches, the checks pass, and the description says what
a reviewer needs and nothing else.

You produce, per direction, a **branch** with one commit (two at most) and its **PR description**,
plus a short **report** for the maintainer. When the caller gives its own output contract (branch
names, file names, metadata, where to push), follow it for the form and this skill for the content.

## Hard rules

- **Never write on twbs/bootstrap.** No push, PR, comment or label there. Push only where the caller
  says. The maintainer opens the PR.
- **Reproduce from scratch.** Never check out, apply or run code from an outside contributor's PR,
  and never open the links an issue or a PR gives. Write your own reproduction on the base branch,
  with only the repository's own build.
- **Write the fix yourself, on the upstream base.** Another PR on the same issue is something to
  compare with, never code to copy.
- **`dist/` is never part of a fix.** Builds rewrite it: revert it before every commit
  (`git checkout -- dist js/dist`).
- **Never claim a check you didn't run.**

## Process

1. **Pin the line.** Find which release line the issue is about and read the code there: `main` is
   v6, `v5-dev` is v5, `gh-pages` holds the frozen docs of old versions (`docs/5.2`, `docs/4.6`).
   The branches were renamed on 2026-10-08: older threads use `main` for v5 and `v6-dev` for v6.
2. **Decide whether a fix should exist.** No branch for: by design, can't reproduce, a duplicate,
   a question, out of scope, a v5 change that isn't a patch-level fix, or a change that costs more
   code than the problem justifies. A feature (a new class, option, variable, utility or component)
   needs a maintainer's yes in the issue first. Say which, with the reason, and stop.
3. **Reproduce, then find the cause.** Write the smallest page or test that shows the problem on the
   base. Find the line that causes it. The issue's title often names the symptom: fix the cause.
   Then find every place the same cause lives: the fix is global, never one component at a time.
4. **Load the project's rules from the base, not from memory.** `AGENTS.md`, `.github/CONTRIBUTING.md`
   and, on v6, the project skill for the area (`skills/bootstrap-component`, `-component-js`,
   `-color-system`, `-utility-api`, `-v5-v6-migration`). Then bootstrap-review's
   `references/bootstrap.md` and `references/frontend.md` for what those don't say.
5. **Choose the directions.** One clear fix is one branch. When there are several reasonable fixes
   (a maintainer's "we could do A or B", another open PR, a docs-only option), make one branch per
   direction, three at most, each from the upstream base. Don't invent directions.
6. **Write the fix** ([references/fix.md](references/fix.md)): the smallest change, in the place that
   already handles the case, with its test and its docs, applied everywhere the topic reaches.
7. **Check it** ([references/fix.md](references/fix.md), "Checks"): run what the change touches,
   build both sides when the output changes, and take the before and after evidence for a visual
   change. Then check the impact on every component the change touches: all states, usages and odd
   cases ([references/fix.md](references/fix.md), "The impact").
8. **Commit** one commit, two at most, with a message in the repository's style that says why.
9. **Write the PR description** ([references/pr-description.md](references/pr-description.md)), with
   the checks and the evidence in its collapsed notes, and the report: the cause, each direction with its trade-off, the recommended one, and what you
   couldn't check.
