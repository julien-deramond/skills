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
- **Compiled CSS**: when the change alters the compiled CSS, paste the `diff -u` of
  `dist/css/bootstrap.css` in a `diff` block. Link the deploy preview pages that show the change
  (`https://deploy-preview-<n>--twbs-bootstrap.netlify.app/docs/<version>/…`) once the PR number
  exists.
- **Then only what matters**: how it works where the diff doesn't say, why this approach over the
  alternative, a known limit, what couldn't be verified when it matters.
- Plain paragraphs. Headings only when the PR covers several topics that read better apart.
- The caller's attribution or disclosure line ends it, when it has one.

## What it never holds

- Sections like "What was done", "How to review", "Test plan" or "Checklist" of your own (the
  repository's PR template, when it has one, still applies).
- Instructions to the reviewer: no "Decide", no "Try it" checkout commands, no "read file X".
- A list of the checks that passed: CI shows them.
- A restatement of the diff line by line.

## Length

Most fixes need under 150 words outside the tables and code blocks. A fix that needs more usually
needs a clearer change.
