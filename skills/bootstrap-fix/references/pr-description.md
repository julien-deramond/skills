# The PR description

Write it for a reviewer who has never seen the issue. They read it once, then the diff.

**Plain paragraphs, always.** Bootstrap's `AGENTS.md` asks for bulleted PR descriptions, and the
repository has a PR template with headings and checkboxes. This skill follows neither, by the
maintainers' choice: the description is the paragraphs below, the way their own merged fixes read.
Where the caller's or the project's rules disagree on anything else, those rules win.

**Keys are `<kbd>` elements.** In the description, its notes and the reply on the issue (sentences,
tables and lists alike), a key the reader presses is `<kbd>Delete</kbd>`, a typed character
`<kbd>9</kbd>`, a combination `<kbd>Shift</kbd>+<kbd>Tab</kbd>`, never a bare word or inline code.
Before you hand the text over, search it for key names (Backspace, Delete, Tab, Enter, Escape, the
arrows) and typed characters. Titles show HTML as text, so a title names the key in words. Code
blocks keep their code as it is.

## Form

- **Title**: what the change does, in the style of the repository's merged PRs ("Fix invalid division
  in the list-inline-item margin").
- **Opening**: the problem and the fix in a few sentences, then `Fixes #<n>` when the PR fixes all
  of the issue, `Refs #<n>` when it fixes part of it. Never link or name an issue in a private
  repository.
- **Before and after**, right after the opening, for a visual change: a two-column table
  (`| Before | After |`), one row per pair, then one sentence on what the pictures show.
- **Compiled CSS**: when the change alters the compiled CSS, the `diff -u` of
  `dist/css/bootstrap.css` goes in the notes below, in a `diff` block. Link the deploy preview pages
  that show the change (`https://deploy-preview-<n>--twbs-bootstrap.netlify.app/docs/<version>/…`)
  once the PR number exists.
- **Then only what matters**: how it works where the diff doesn't say, why this approach over the
  alternative, a known limit, what couldn't be verified when it matters.
- Plain paragraphs. Headings only when the PR covers several topics that read better apart.
- **The notes**, last, in a closed block, so the checks stay on the PR without crowding it (below).
- The caller's attribution or disclosure line ends it, when it has one.

## The notes

```markdown
<details>
<summary><b>Notes</b>: what was checked, and how to check it again</summary>

…

</details>
```

Written for a public reader, they hold the compiled CSS diff, the measured values before and after
(a table), the impact checked on each component the change touches, every check run with its
result, what wasn't checked, and a nested closed block, "How to check it again", with the probe page,
Sass or script as code. Screenshots are referenced by file name and attached by whoever opens the PR.
They never hold anything private, local paths, or the maintainer's next steps.

## The reply on the issue

When the analysis confirms the bug, explains it, or says no fix should be made, the reply on the
issue keeps the same evidence in public: a short message, then a closed block.

- **The message**: thank the reporter, say what was confirmed or decided in the first sentence, and
  point to the PR that fixes it (or say one is coming, or why there won't be one). As long as what
  the reporter needs, and no longer.
- **The notes**, in `<details>` with a summary such as `<b>Notes</b>: the reproduction, the cause,
  and how to check it again`: the reproduction (the page, the Sass or the steps, as code), the cause
  with the lines linked, the measured values or screenshots before and after, what the fix changes
  and its limits, the same pattern found elsewhere, and what wasn't checked.

The same rules as the PR notes apply: nothing private, no local paths, screenshots referenced by
file name for whoever posts. A reply that only asks the reporter for a reproduction, or answers a
question from the docs, has no notes.

## What it never holds

- Sections like "What was done", "How to review", "Test plan" or "Checklist", or the repository's PR
  template.
- Instructions to the reviewer: no "Decide", no "Try it" checkout commands, no "read file X".
- A list of checks outside the notes.
- A restatement of the diff line by line.

## Length

No word count. The description is as long as what the reviewer needs (the problem, the fix, why it's
done this way, its limits) and no longer: no padding, no diff restated, nothing the notes already
hold. A fix that needs a long explanation usually needs a clearer change.
