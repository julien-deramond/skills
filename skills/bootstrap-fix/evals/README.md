# bootstrap-fix evals

Each case is an issue the team fixed, frozen as it was just before the fix PR opened: the issue
and its earlier comments, the items it references, and the repository tree before the fix.
`snapshots.tsv` pins them, and `scripts/bootstrap-issue-snapshot.py` builds each snapshot. The
graders describe what the merged fix did and what a good fix PR holds; a different fix that works
as well can pass, and the graders say so where the issue's own suggestion differs from the merged fix.
