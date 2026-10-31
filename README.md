# Skills

Agent skills by [Julien Déramond](https://github.com/julien-deramond), written from his own work as a
Bootstrap maintainer and open source developer. Each skill follows the
[Agent Skills](https://agentskills.io) format, so Claude Code, Codex and the other agents that read
`SKILL.md` can use it.

Every skill here is my own version. Other people's skills, docs and posts are sources: each skill
records what it took from them in [`sources.toml`](sources.toml), pinned to the commit or the date it
was read, so a change upstream can be weighed against what this repository took.

## Skills

| Skill | What it does | Status |
| --- | --- | --- |
| [bootstrap-review](skills/bootstrap-review/SKILL.md) | Review a twbs/bootstrap pull request or branch the way a core maintainer does: evidence for every finding, then approve, request changes or close. | draft |

A skill's `status` is `draft` (being tuned against its evals), `beta` (used every day, still
changing) or `stable`.

## Install

```bash
npx skills add julien-deramond/skills --skill bootstrap-review
```

Or copy or link `skills/<name>/` into your agent's skills folder (`.claude/skills/` for a project).

## Layout

```
skills/<name>/
  SKILL.md          what the agent loads
  references/*.md   loaded on demand, named in SKILL.md
  evals/<case>/     test cases in the `claude plugin eval` layout
  README.md         for people: what it's for, credits
sources.toml        every source a skill took something from, pinned
docs/adr/           decisions about this repository
scripts/check.py    checks the layout, the metadata, the sources and the evals
```

[AGENTS.md](AGENTS.md) has the rules for changing a skill.
