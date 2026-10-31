# bootstrap-fix

Turns a twbs/bootstrap issue into a fix branch a maintainer can open as a pull request, with its PR
description, or says why no fix should be made. It reproduces the problem from scratch, fixes the
cause in the place that already handles the case, runs the checks the change touches, and takes
the before and after evidence for a visual change.

Install it with [bootstrap-review](../bootstrap-review/README.md): it reads that skill's
`bootstrap.md` and `frontend.md` for Bootstrap's conventions and the front-end checks.

## Use

Ask for a fix ("fix twbs/bootstrap#<n>", "prepare the alternative branch the review asked for") in a
Bootstrap checkout. A caller that keeps fixes in its own place (another remote, its own file names)
gives its contract, and the skill fills it.

## Evals

`evals/` holds issues the team fixed, each frozen as it was before the fix, with what the merged fix
did. `snapshots.tsv` pins each case. They run with the skill and against another method on the
same snapshot.

## Credits

The method comes from fixes prepared for Bootstrap issues and the PR description rules used for
them. [`sources.toml`](../../sources.toml) lists the sources.
