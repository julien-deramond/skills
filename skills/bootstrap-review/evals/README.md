# bootstrap-review evals

Each case is a real twbs/bootstrap pull request, pinned to the commit that was reviewed, with what a
good review of that commit finds. The reference is a maintainer's review on GitHub, or a written
maintainer analysis for recent PRs (`case.yaml` says which).

Each case runs on a frozen snapshot of the PR, not on live GitHub, since later comments, commits and
releases hold the answer. `snapshots.tsv` gives each case's PR, reviewed commit, cutoff date and
merge base, and `scripts/bootstrap-pr-snapshot.py` builds the snapshot from them. Pin a case to the
commit the maintainer reviewed: a review comment's `original_commit_id`, not its `commit_id`, which
GitHub moves to the PR's latest commit. Graders check the trace too (`focus: trace`).

Every grader is one checkable statement. A case with several findings has one grader per finding,
and one for the decision. `radio-switch-radius-approve` is there to catch false alarms: the right
review approves it.

`cursor-utilities-feature` was added after the skill changed, as a held-out case.
