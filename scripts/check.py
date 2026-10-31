#!/usr/bin/env python3
"""Check the repository: skill metadata, links to references, eval cases, sources and prose.

Run from anywhere: python3 -I scripts/check.py
"""

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
STATUSES = {"draft", "beta", "stable"}
SOURCE_KINDS = {"git", "release", "url", "corpus"}
errors = []


def error(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def frontmatter(path):
    """Read a flat YAML frontmatter block (keys, one level of nesting, quoted or plain values)."""
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None, text
    data, parent = {}, None
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, _, value = line.strip().partition(":")
        value = value.strip().strip('"')
        if line.startswith("  ") and parent is not None:
            data[parent][key] = value
        elif value == "":
            parent = key
            data[key] = {}
        else:
            parent = None
            data[key] = value
    return data, text[match.end():]


def check_skill(folder):
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        error(folder, "no SKILL.md")
        return
    meta, body = frontmatter(skill_md)
    if meta is None:
        error(skill_md, "no frontmatter")
        return
    if meta.get("name") != folder.name:
        error(skill_md, f"name {meta.get('name')!r} isn't the folder name {folder.name!r}")
    description = meta.get("description", "")
    if not description:
        error(skill_md, "no description")
    elif len(description) > 1024:
        error(skill_md, f"description is {len(description)} characters, over 1024")
    info = meta.get("metadata", {})
    for key in ("author", "version", "status", "category"):
        if not info.get(key):
            error(skill_md, f"metadata.{key} is missing")
    if info.get("status") and info["status"] not in STATUSES:
        error(skill_md, f"metadata.status {info['status']!r} isn't one of {sorted(STATUSES)}")
    if info.get("version") and not re.fullmatch(r"\d{4}\.\d{1,2}\.\d{1,2}", info["version"]):
        error(skill_md, "metadata.version isn't YYYY.M.D")

    linked = set(re.findall(r"\]\((references/[^)#]+)", body))
    for target in linked:
        if not (folder / target).exists():
            error(skill_md, f"links to {target}, which doesn't exist")
    references = folder / "references"
    if references.exists():
        for ref in references.glob("*.md"):
            if f"references/{ref.name}" not in linked:
                error(ref, "isn't linked from SKILL.md")
            if re.search(r"\]\((?:\.\./)?references/|\]\([a-z-]+\.md\)", ref.read_text()):
                error(ref, "links to another reference (SKILL.md is the index)")

    evals = folder / "evals"
    if evals.exists():
        for case in sorted(p for p in evals.iterdir() if p.is_dir()):
            check_case(case)


def check_case(case):
    if not re.fullmatch(r"[a-z][a-z0-9-]*", case.name):
        error(case, "case name must be lowercase letters, digits and hyphens")
    prompt = case / "prompt.md"
    if not prompt.exists() or not prompt.read_text().startswith("---\n"):
        error(case, "prompt.md is missing or has no settings block")
    yaml = case / "case.yaml"
    if not yaml.exists():
        error(case, "case.yaml is missing")
    else:
        text = yaml.read_text()
        if 'schema_version: "1.1"' not in text:
            error(yaml, 'needs schema_version: "1.1"')
        if f"name: {case.name}\n" not in text:
            error(yaml, "name must match the folder")
        if "expected_outcome:" not in text:
            error(yaml, "expected_outcome is missing")
    graders = sorted((case / "graders").glob("*.md")) if (case / "graders").exists() else []
    if not graders:
        error(case, "no grader")
    for grader in graders:
        if not re.fullmatch(r"\d\d-[a-z0-9-]+\.md", grader.name):
            error(grader, "grader name must be NN-few-words.md")
        meta, body = frontmatter(grader)
        if meta is None or "type" not in meta:
            error(grader, "grader needs its frontmatter block (type, focus, weight)")
        elif not body.strip():
            error(grader, "grader has no statement")


def check_sources(skill_names):
    path = ROOT / "sources.toml"
    try:
        data = tomllib.loads(path.read_text())
    except (OSError, tomllib.TOMLDecodeError) as exc:
        error(path, f"can't read: {exc}")
        return
    ids = set()
    for source in data.get("source", []):
        sid = source.get("id", "?")
        if sid in ids:
            error(path, f"{sid}: duplicate id")
        ids.add(sid)
        kind = source.get("kind")
        if kind not in SOURCE_KINDS:
            error(path, f"{sid}: kind {kind!r} isn't one of {sorted(SOURCE_KINDS)}")
        if kind == "git":
            if not source.get("repo") or not source.get("path"):
                error(path, f"{sid}: a git source needs repo and path")
            if not re.fullmatch(r"[0-9a-f]{40}", source.get("commit", "")):
                error(path, f"{sid}: a git source needs the full commit read")
        elif not source.get("read"):
            error(path, f"{sid}: needs the date it was read")
        if not source.get("took", "").strip():
            error(path, f"{sid}: says nothing about what was taken")
        for name in source.get("informs", []):
            if name not in skill_names:
                error(path, f"{sid}: informs {name!r}, which isn't a skill")


def check_prose():
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") or part.endswith("-workspace") for part in path.relative_to(ROOT).parts):
            continue
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if "—" in line or " -- " in line:
                error(path, f"line {number}: em dash (rewrite the sentence)")


def main():
    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir() and not p.name.endswith("-workspace")) if SKILLS.exists() else []
    for folder in folders:
        check_skill(folder)
    check_sources({folder.name for folder in folders})
    check_prose()
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s).")
        return 1
    print(f"OK: {len(folders)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
