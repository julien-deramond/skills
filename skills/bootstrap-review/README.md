# bootstrap-review

Reviews a twbs/bootstrap pull request or branch the way a core maintainer does. It produces a report
for the maintainer who decides (what the PR is, where it stands, the findings with their evidence,
the recommendation) and the review text to post for the author.

It never writes on GitHub and never runs code from a pull request opened outside the core team. It
checks those by writing its own probes and its own version of the fix on the base branch.

## Use

Ask for a review of a PR ("review twbs/bootstrap#43150") or of the current branch in a Bootstrap
checkout. A caller that keeps reviews in its own files gives its format, and the skill fills it.

## How it's built

`SKILL.md` holds the process and the hard rules. The references split along the lines a later split of
the skill would follow:

- `method.md`: how to reach findings, for any code review.
- `frontend.md`: CSS, markup, accessibility and browser checks, for any front-end project.
- `bootstrap.md`: Bootstrap's own checks, on top of the project's `AGENTS.md` and skills, which the
  review reads from the base branch at run time.
- `untrusted.md`: the rules for pull requests from outsiders.
- `report.md`: the formats of the report and the review.

## Evals

`evals/` holds cases from real Bootstrap pull requests, each pinned to the commit that was reviewed,
with what a good review of it finds. Run them with `claude plugin eval` or the skill-creator workflow,
with the skill and without it.

## Credits

The two separate review axes (spec and standards) come from Matt Pocock's
[code-review](https://github.com/mattpocock/skills/tree/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/code-review)
skill (MIT). Verifying each finding before reporting it comes from Claude Code's built-in
`/code-review`. Both are rewritten here, not copied. The rest comes from reviews of Bootstrap pull
requests. [`sources.toml`](../../sources.toml) lists every source with the commit read.
