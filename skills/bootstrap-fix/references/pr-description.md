# The PR description

Write it for a reviewer who has never seen the issue. They read it once, then the diff.

**Plain paragraphs, always.** Bootstrap's `AGENTS.md` asks for bulleted PR descriptions, and the
repository has a PR template with headings and checkboxes. This skill follows neither, by the
maintainers' choice: the description is the paragraphs below, the way their own merged fixes read.
Where the caller's or the project's rules disagree on anything else, those rules win.

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

## What it never holds

- Sections like "What was done", "How to review", "Test plan" or "Checklist", or the repository's PR
  template.
- Instructions to the reviewer: no "Decide", no "Try it" checkout commands, no "read file X".
- A list of checks outside the notes.
- A restatement of the diff line by line.

## Length

Most fixes need under 150 words outside the tables, code blocks and notes. A fix that needs more
usually needs a clearer change.
