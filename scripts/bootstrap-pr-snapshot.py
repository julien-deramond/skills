#!/usr/bin/env python3
"""Freeze a twbs/bootstrap pull request as it was at one commit and one date, for an eval case.

    python3 -I scripts/bootstrap-pr-snapshot.py <pr> <commit> <cutoff ISO date> <merge base> <out dir>

Writes into <out dir>:
  github/pr.md        title, author, base, the description as it was at the cutoff, the PR's commits
                      up to <commit> (none after it), the files it changes
  github/diff.patch   git diff <merge base> <commit>
  github/checks.md    CI results recorded for <commit>
  github/issue-<n>.md each issue the description references, as it was at the cutoff, with the
                      comments posted before it
  base/               the repository tree at <merge base>, without git history

Needs `gh` (read-only calls) and a twbs/bootstrap clone at ~/twbs/bootstrap that has both commits.
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


def git(*args, **kw):
    return subprocess.run(["git", "-C", str(CLONE), *args], check=True, capture_output=True, **kw).stdout


def body_at(kind, number, cutoff):
    """The body of an issue or PR as it was at the cutoff, from its edit history."""
    field = "pullRequest" if kind == "pr" else "issue"
    query = f'{{repository(owner:"twbs",name:"bootstrap"){{{field}(number:{number}){{body createdAt userContentEdits(first:100){{nodes{{editedAt diff}}}}}}}}}}'
    node = gh("api", "graphql", "-f", f"query={query}")["data"]["repository"][field]
    edits = [e for e in node["userContentEdits"]["nodes"] if e["diff"] is not None]
    if not edits:
        return node["body"] or ""
    before = [e for e in edits if e["editedAt"] <= cutoff]
    # Edits come newest first; the oldest edit holds the original text.
    return (before[0] if before else edits[-1])["diff"] or ""


def main():
    pr, commit, cutoff, merge_base, out = sys.argv[1:6]
    out = Path(out)
    (out / "github").mkdir(parents=True, exist_ok=True)

    info = gh("api", f"repos/{REPO}/pulls/{pr}")
    in_range = set(git("rev-list", f"{merge_base}..{commit}", text=True).split())
    commits = [c for c in gh("api", f"repos/{REPO}/pulls/{pr}/commits", "--paginate") if c["sha"] in in_range]
    files = git("diff", "--stat", merge_base, commit, text=True)
    body = body_at("pr", pr, cutoff)
    lines = [
        f"# twbs/bootstrap#{pr}: {info['title']}",
        "",
        f"- Author: @{info['user']['login']} ({info['author_association'].lower()})",
        f"- Base branch at the time: `{info['base']['ref']}`",
        f"- Reviewed commit: `{commit}` (merge base `{merge_base}`)",
        f"- Opened: {info['created_at']}. This snapshot is the state at {cutoff}.",
        "",
        "## Description",
        "",
        body.strip() or "(empty)",
        "",
        "## Commits up to the reviewed one",
        "",
        *[f"- `{c['sha'][:12]}` {c['commit']['message'].splitlines()[0]}" for c in commits],
        "",
        "## Files",
        "",
        "```",
        files.rstrip(),
        "```",
    ]
    (out / "github" / "pr.md").write_text("\n".join(lines) + "\n")
    (out / "github" / "diff.patch").write_bytes(git("diff", merge_base, commit))

    runs = gh("api", f"repos/{REPO}/commits/{commit}/check-runs", "--paginate").get("check_runs", [])
    status = gh("api", f"repos/{REPO}/commits/{commit}/status").get("statuses", [])
    checks = [f"# CI recorded for `{commit[:12]}`", ""]
    checks += [f"- {r['name']}: {r['conclusion'] or r['status']}" for r in runs]
    checks += [f"- {s['context']}: {s['state']} ({s['description'] or ''})" for s in status]
    if len(checks) == 2:
        checks.append("No CI results are recorded for this commit any more.")
    (out / "github" / "checks.md").write_text("\n".join(checks) + "\n")

    refs = re.findall(r"(?<![\w/])#(\d{4,6})\b", body) + re.findall(r"github\.com/twbs/bootstrap/(?:issues|pull)/(\d+)", body)
    for number in sorted({int(n) for n in refs} - {int(pr)}):
        try:
            issue = gh("api", f"repos/{REPO}/issues/{number}")
        except subprocess.CalledProcessError:
            continue
        if issue["created_at"] > cutoff:
            continue
        kind = "PR" if "pull_request" in issue else "issue"
        text = body_at("pr" if kind == "PR" else "issue", number, cutoff)
        comments = [c for c in gh("api", f"repos/{REPO}/issues/{number}/comments", "--paginate") if c["created_at"] <= cutoff]
        doc = [f"# twbs/bootstrap#{number} ({kind}): {issue['title']}", "", f"- Author: @{issue['user']['login']}, opened {issue['created_at']}", "", text.strip() or "(empty)", ""]
        for c in comments:
            doc += [f"## Comment by @{c['user']['login']}, {c['created_at']}", "", c["body"].strip(), ""]
        (out / "github" / f"issue-{number}.md").write_text("\n".join(doc))

    base = out / "base"
    base.mkdir(exist_ok=True)
    archive = git("archive", merge_base)
    subprocess.run(["tar", "-x", "-C", str(base)], input=archive, check=True)
    print(f"{out}: {len(commits)} commit(s), {len(list((out / 'github').glob('issue-*.md')))} linked item(s)")


if __name__ == "__main__":
    main()
