# The report and the review

Two texts: the report for the maintainer who decides, the review for the author and everyone who
reads the PR later (a short message, with the full public analysis collapsed under it). A caller's own
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

What the maintainer posts on the PR, nothing around it. It has two parts: the message, then the
review notes.

Keys are `<kbd>` elements in both parts (sentences, tables and lists alike): a key the reader
presses is `<kbd>Delete</kbd>`, a typed character `<kbd>9</kbd>`, a combination
`<kbd>Shift</kbd>+<kbd>Tab</kbd>`, never a bare word or inline code. Before you hand the review over,
search it for key names (Backspace, Delete, Tab, Enter, Escape, the arrows) and typed characters. Code
blocks and ` ```suggestion ` blocks keep their code as it is.

### The message

It reads like a maintainer wrote it: short, kind and specific. There's no word count: it holds what
the author needs to act on, each finding with its fix, and nothing else. It ends by pointing to the
notes; the evidence goes in the notes.

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

Don't restate the PR to its author or pad it with praise.

### The review notes

The full analysis goes on the PR too, so it isn't lost: whoever lands on the PR later, from
`git blame` or an issue, sees what was verified and can check it again. It sits under the message,
in a closed block:

```markdown
<details>
<summary><b>Review notes</b>: what was checked, and how to check it again</summary>

…

</details>
```

Written for a public reader, it holds:

- The cause, with the lines linked at the reviewed commit.
- The evidence: the compiled CSS diff in full, measured values in a table (case, before, after), the
  engines tested.
- Screenshots in Before | After pairs, referenced by file name (`![before: the vertical group at
  900px](before.png)`): whoever posts the review attaches the files, so GitHub hosts them.
- Each behaviour change, in a sentence.
- Every check run with its result, and what wasn't checked.
- Related findings outside the PR, a line each.
- A nested closed block, "How to check it again": the probe page, the Sass or the script, as code.

It never holds the next action, labels or metadata, anything private (a private repository, notes,
names of internal tools), local paths, or a link the untrusted-PR rules forbid. A request for
changes keeps its requests in the message and its evidence in the notes. For a trivial PR whose diff
is its own evidence, the notes are a few lines.

## Line comments

When the review has line comments, list them apart, one per line: `path:line: text`. The review body
must stand on its own without them.

## Approvals

An approval of a non-trivial PR says in one sentence what was verified, and the notes show it. A
trivial one ("Good catch, thanks @author") is enough when the diff is its own evidence.
