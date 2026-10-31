# Own skills, pinned sources, flat folders

Date: 2026-10-31. Status: accepted.

## Context

The skills in use today are a mix of hand-written ones and copies of public skills. The copies change
upstream without notice, and the hand-written ones take ideas from several places without saying
which. The goal is one repository of skills that are all our own versions, that can go public, and
that keep track of what each one owes to other work.

## Decision

- **Every skill is our own version.** A public skill that works well as it is can still be used
  as it is, but it isn't stored here. What a skill here takes from elsewhere is a source.
- **`sources.toml` pins every source** with what was taken from it, in words specific enough to
  tell whether a later change upstream touches it. Watching sources means diffing from the pinned
  commit or date and asking that question, not "is there a new version?".
- **Flat `skills/<name>/` folders, with status and category as metadata.** Bucket folders
  (`engineering/`, `in-progress/`) would make every change of status or category a move and a
  broken link.
- **Evals in each skill, in the `claude plugin eval` layout**, from real cases with a known outcome.
- **Private first.** The repository went public on 2026-10-31, once its first skill did better than
  no skill on its evals and nothing in it named private material.

## Consequences

- Splitting a skill later (a generic review out of `bootstrap-review`) is moving a reference file
  into a new skill and its evals with it.
- A watcher is still to build: read `sources.toml`, diff each source since its pin, and open an
  issue when the change touches what was taken.
- Licences: a source whose text is copied keeps its licence and credit. Ideas rewritten in our words
  carry a credit in the skill's README.
