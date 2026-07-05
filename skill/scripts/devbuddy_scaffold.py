#!/usr/bin/env python3
"""Scaffold DevBuddy project memory, report, ADR, and reusable-tool folders."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


MEMORY_FILES = {
    "Context.md": "# Context\n\n## Architecture\n\n## Modules\n\n## Data Models\n\n## Dependencies\n\n## Runtime Behavior\n\n## Test Strategy\n",
    "BusinessContext.md": "# BusinessContext\n\n## Domains\n\n## Users\n\n## Workflows\n\n## Business Rules\n\n## Edge Cases\n",
    "DecisionLog.md": "# DecisionLog\n\n## Decisions\n\n",
    "KnowledgeBase.md": "# KnowledgeBase\n\n## Lessons\n\n",
}

REPORT_DIRS = [
    "reports/analysis",
    "reports/implementations",
    "reports/lessons-learned",
    "reports/plans",
    "reports/qa",
    "reports/reviews",
]


def parse_simple_config(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    data: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip("'\"")
        if value:
            data[key.strip()] = value
    return data


def resolve_memory_root(project_root: Path, config_path: Path, explicit_memory_root: str | None) -> tuple[Path, bool]:
    if explicit_memory_root:
        root = Path(explicit_memory_root).expanduser()
        return (root if root.is_absolute() else project_root / root), False

    config = parse_simple_config(config_path)
    if config.get("obsidian_vault"):
        vault = Path(config["obsidian_vault"]).expanduser()
        if not vault.exists():
            raise SystemExit(f"Obsidian vault does not exist: {vault}")
        subfolder = config.get("obsidian_subfolder") or project_root.name
        return vault / subfolder, True

    if config.get("memory_root"):
        root = Path(config["memory_root"]).expanduser()
        return (root if root.is_absolute() else project_root / root), False

    return project_root / ".devbuddy", False


def write_file(path: Path, content: str, overwrite: bool, created: list[str], skipped: list[str]) -> None:
    if path.exists() and not overwrite:
        skipped.append(str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created.append(str(path))


def memory_content(name: str, body: str, project: str, obsidian: bool, memory_root: Path) -> str:
    if not obsidian:
        if name == "Context.md":
            return body + f"\n## DevBuddy\n\nResolved memory root: `{memory_root}`\n"
        return body
    stem = Path(name).stem
    frontmatter = f"---\ntags: [devbuddy, {project}]\naliases: [{project} {stem}]\n---\n\n"
    links = "\n\nRelated: [[Context]], [[BusinessContext]], [[DecisionLog]], [[KnowledgeBase]]\n"
    return frontmatter + body + links


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=".", help="Target project root. Defaults to the current directory.")
    parser.add_argument("--config", help="Path to devbuddy.config.md. Defaults to <project-root>/devbuddy.config.md.")
    parser.add_argument("--memory-root", help="Override memory root. Relative paths resolve under project root.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing memory/index files.")
    args = parser.parse_args()

    project_root = Path(args.project_root).expanduser().resolve()
    config_path = Path(args.config).expanduser().resolve() if args.config else project_root / "devbuddy.config.md"
    memory_root, obsidian = resolve_memory_root(project_root, config_path, args.memory_root)
    memory_root.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    skipped: list[str] = []

    for filename, body in MEMORY_FILES.items():
        write_file(
            memory_root / filename,
            memory_content(filename, body, project_root.name, obsidian, memory_root),
            args.overwrite,
            created,
            skipped,
        )

    for directory in ["docs/adr", "tools", *REPORT_DIRS]:
        path = memory_root / directory
        path.mkdir(parents=True, exist_ok=True)
        created.append(str(path))

    write_file(
        memory_root / "tools" / "README.md",
        "# Reusable Tools\n\nIndex project-local tools here. Each entry should include purpose, runtime, command, inputs, and expected output.\n",
        args.overwrite,
        created,
        skipped,
    )

    if obsidian:
        index = (
            f"---\ntags: [devbuddy, {project_root.name}]\naliases: [{project_root.name} DevBuddy]\n---\n\n"
            f"# {project_root.name} DevBuddy\n\n"
            "- [[Context]]\n"
            "- [[BusinessContext]]\n"
            "- [[DecisionLog]]\n"
            "- [[KnowledgeBase]]\n"
        )
        write_file(memory_root / f"{project_root.name} DevBuddy.md", index, args.overwrite, created, skipped)

    print(json.dumps({"memory_root": str(memory_root), "obsidian": obsidian, "created": created, "skipped": skipped}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
