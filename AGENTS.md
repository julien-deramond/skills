# Working in this repository

This repository holds agent skills: one folder per skill under `skills/`, in the
[Agent Skills](https://agentskills.io) format. Read the
[best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
before writing or changing one.

Run `python3 -I scripts/check.py` before every commit. It must pass.

## A skill's folder

- `skills/<name>/SKILL.md`. The frontmatter has `name` (the folder name, kebab-case), `description`
  (what it does and when to use it, at most 1024 characters, written so an agent picks the skill at the
  right moment) and `metadata`: `author`, `version` (the date of the last change, `"YYYY.M.D"`),
  `status` (`draft`, `beta` or `stable`) and `category`. The body stays short: the process and the
  hard rules. Details go in `references/`.
- `skills/<name>/references/*.md`. One topic per file, each named from `SKILL.md` with the moment to
  read it. A reference never points to another reference: `SKILL.md` is the index.
- `skills/<name>/evals/<case>/`. One folder per test case in the layout `claude plugin eval` reads:
  `prompt.md` (a settings block, then the prompt), `case.yaml` (`schema_version: "1.1"`, `name`,
  `expected_outcome`) and `graders/NN-<words>.md` (one checkable statement each). A case comes from
  real work: a pull request, an issue or a session where the right outcome is known.
- `skills/<name>/README.md`. For people, not loaded by agents: what the skill is for, how to call it,
  and the credits.

Categories are metadata, not folders, so a skill moves to another category without changing its path.

## Sources

Every skill is our own version. When a skill takes something from a source (another skill, a project's
docs, a post), `sources.toml` gets an entry:

- `id`, `kind` (`git`, `release`, `url` or `corpus`) and where it lives (`repo` and `path` with the
  `commit` read, or `url` with the `read` date).
- `informs`: the skills that took something from it.
- `took`: what was taken, in plain words, specific enough to tell whether a later change upstream
  touches it.
- `license` when text or code was copied, not only an idea. Copied text follows its licence.

When a skill is changed after reading a newer version of a source, move that source's `commit` or
`read` date with it. A source that's read at run time (a project's own `AGENTS.md`, say) is still
listed, so a change there can be checked for skills that repeat it.

Private material (a private repository, notes) can be a source, but nothing in this repository names
it beyond a short description, and no private text is copied into a skill.

## Evals before changes

A change to a skill's behaviour is checked against its evals, with the skill and without it, before
it's merged. A new idea from a source or a post gets in when it does better on the evals, or when it
adds a case the skill failed. When a skill fails on real work, add that case first.

## Writing

Plain English, for every file: short sentences, active voice, one point per paragraph, contractions.
No em dashes. A skill speaks to the agent ("Read the diff"), a README to a person.
