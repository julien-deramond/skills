#!/usr/bin/env python3
"""Freeze a twbs/bootstrap issue as it was before its fix, for a fix eval case.

    python3 -I scripts/bootstrap-issue-snapshot.py <issue> <cutoff ISO date> <base commit> <out dir>

Writes into <out dir>:
  github/issue-<n>.md   the issue as it was at the cutoff, with the comments posted before it
  github/ref-<n>.md     each issue or PR it references, as it was at the cutoff (PRs without their diff)
  base/                 the repository tree at <base commit>, without git history

Needs `gh` (read-only calls) and a twbs/bootstrap clone at ~/twbs/bootstrap that has the commit.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = "twbs/bootstrap"
CLONE = Path.home() / "twbs" / "bootstrap"


def gh(*args):
    return json.loads(subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout)


def body_at(number, cutoff):
    """The body of an issue or PR as it was at the cutoff, from its edit history."""
    query = f'{{repository(owner:"twbs",name:"bootstrap"){{issueOrPullRequest(number:{number}){{... on Issue{{body userContentEdits(first:100){{nodes{{editedAt diff}}}}}} ... on PullRequest{{body userContentEdits(first:100){{nodes{{editedAt diff}}}}}}}}}}}}'
    node = gh("api", "graphql", "-f", f"query={query}")["data"]["repository"]["issueOrPullRequest"]
    edits = [e for e in node["userContentEdits"]["nodes"] if e["diff"] is not None]
    if not edits:
        return node["body"] or ""
    before = [e for e in edits if e["editedAt"] <= cutoff]
    return (before[0] if before else edits[-1])["diff"] or ""


def item(number, cutoff):
    issue = gh("api", f"repos/{REPO}/issues/{number}")
    if issue["created_at"] > cutoff:
        return None, ""
    kind = "PR" if "pull_request" in issue else "issue"
    text = body_at(number, cutoff)
    comments = [c for c in gh("api", f"repos/{REPO}/issues/{number}/comments", "--paginate") if c["created_at"] <= cutoff]
    doc = [f"# twbs/bootstrap#{number} ({kind}): {issue['title']}", "", f"- Author: @{issue['user']['login']}, opened {issue['created_at']}", "", text.strip() or "(empty)", ""]
    for c in comments:
        doc += [f"## Comment by @{c['user']['login']}, {c['created_at']}", "", c["body"].strip(), ""]
    return "\n".join(doc), text + "\n".join(c["body"] for c in comments)


def main():
    number, cutoff, base_commit, out = sys.argv[1:5]
    out = Path(out)
    (out / "github").mkdir(parents=True, exist_ok=True)
    doc, text = item(number, cutoff)
    (out / "github" / f"issue-{number}.md").write_text(doc)
    refs = re.findall(r"(?<![\w/])#(\d{4,6})\b", text) + re.findall(r"github\.com/twbs/bootstrap/(?:issues|pull)/(\d+)", text)
    for ref in sorted({int(r) for r in refs} - {int(number)}):
        try:
            ref_doc, _ = item(ref, cutoff)
        except subprocess.CalledProcessError:
            continue
        if ref_doc:
            (out / "github" / f"ref-{ref}.md").write_text(ref_doc)
    base = out / "base"
    base.mkdir(exist_ok=True)
    archive = subprocess.run(["git", "-C", str(CLONE), "archive", base_commit], check=True, capture_output=True).stdout
    subprocess.run(["tar", "-x", "-C", str(base)], input=archive, check=True)
    print(f"{out}: {len(list((out / 'github').glob('ref-*.md')))} referenced item(s)")


if __name__ == "__main__":
    main()
