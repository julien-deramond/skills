# bootstrap-review evals

Each case is a real twbs/bootstrap pull request, pinned to the commit that was reviewed, with what a
good review of that commit finds. The reference is a maintainer's review on GitHub, or a written
maintainer analysis for recent PRs (`case.yaml` says which).

The prompt tells the run not to read the PR's comments and reviews, since they hold the answer.
Graders check the trace too (`focus: trace`), so a run that finds a point by reading a later comment
should fail that grader.

Every grader is one checkable statement. A case with several findings has one grader per finding,
and one for the decision. `radio-switch-radius-approve` is there to catch false alarms: the right
review approves it.
