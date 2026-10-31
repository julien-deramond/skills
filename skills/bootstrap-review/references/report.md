# The report and the review

Two texts: the report for the maintainer who decides, the review for the author. A caller's own
format (file names, metadata, a required footer) replaces the form below, not the content.

## The report

A maintainer reads it cold, between other things, and decides from it without opening the PR.

```markdown
# [twbs/bootstrap#<n>](https://github.com/twbs/bootstrap/pull/<n>) <title>

**What it is.** Two to four sentences: what the PR changes and why, its key line quoted, who wrote
it, the issue it fixes.

**Where it stands.** Who waits on whom and since when, CI, conflicts, the related issues, PRs and
branches with links. What was run and what wasn't (the PR's code is never run when it's untrusted).

**Findings.** The cause, found from the code, then each finding numbered with its severity and axis,
its evidence (lines linked at the pinned commit, probes, measurements in a table), and the fix it
calls for. What you couldn't check, in one sentence.

**Directions.** Only when there are several fixes to compare: a small table of what each changes,
its size and its trade-off.

**Recommendation.** The decision and why, the alternative and what it would cost.

**Next action.** The exact steps for the maintainer, naming every GitHub write and the text it uses.
```

Plain paragraphs. Bullets only for a list of parallel things, tables for states and directions.

## The review

What the maintainer posts on the PR, nothing around it. It reads like a maintainer wrote it: short,
kind and specific.

Keep it under 150 words for one finding and under 300 for several, code blocks aside. The detail
lives in the report: the review names the finding and its fix, and doesn't repeat the evidence
tables or the list of what was checked.

- Open with a short thanks to the author by handle, then the decision within the first three
  sentences ("The
  fix works for the docs example, but I'd rather…").
- One request per paragraph, or a short list of what's missing (a test, the docs, lint). Each request
  says why, in one sentence, with the line or the measurement behind it.
- Show the change: a ` ```suggestion ` block for a small edit on a line, a code block for anything
  larger.
- Mark what's optional as optional ("not a blocker", "could be a follow-up").
- Say what was checked when the approval rests on it ("Tested in Chrome and Firefox; the
  compiled CSS is identical except for the new rule").
- Ask, don't order: "Could you…".
- A call that belongs to someone else on the team names the team or asks them.
- Closing: thank the author, give the reason and the pointer (the issue to discuss first, the PR that
  supersedes it), and say a new PR is welcome when it is.
- When the review was drafted by an agent, it ends with the disclosure line the caller requires.

Don't restate the PR to its author, pad it with praise or list every check that passed.

## Line comments

When the review has line comments, list them apart, one per line: `path:line: text`. The review body
must stand on its own without them.

## Approvals

An approval of a non-trivial PR says in one sentence what was verified. A trivial one ("Good catch,
thanks @author") is enough when the diff is its own evidence.
