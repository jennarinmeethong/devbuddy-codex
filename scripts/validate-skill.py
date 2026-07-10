#!/usr/bin/env python3
"""Validate the DevBuddy Codex skill without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill"
SKILL_MD = SKILL / "SKILL.md"
OPENAI_YAML = SKILL / "agents" / "openai.yaml"
SCAFFOLD_SCRIPT = SKILL / "scripts" / "devbuddy_scaffold.py"
INSTALL_SCRIPT = ROOT / "scripts" / "install-local.sh"
PACKAGE_SCRIPT = ROOT / "scripts" / "package-skill.sh"
MEMORY_FILES = {
    "Context.md",
    "BusinessContext.md",
    "DecisionLog.md",
    "KnowledgeBase.md",
    "plan.md",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    data: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        if not raw.strip():
            continue
        if ":" not in raw:
            fail(f"Unsupported frontmatter line: {raw}")
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        data[key] = value
    return data


def main() -> int:
    if not SKILL_MD.exists():
        fail("skill/SKILL.md is missing")
    if not OPENAI_YAML.exists():
        fail("skill/agents/openai.yaml is missing")
    if not SCAFFOLD_SCRIPT.exists():
        fail("skill/scripts/devbuddy_scaffold.py is missing")
    if not INSTALL_SCRIPT.exists():
        fail("scripts/install-local.sh is missing")
    if not PACKAGE_SCRIPT.exists():
        fail("scripts/package-skill.sh is missing")

    skill_text = SKILL_MD.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_text)

    if set(frontmatter) != {"name", "description"}:
        fail(f"SKILL.md frontmatter keys must be exactly name and description, got {sorted(frontmatter)}")
    if frontmatter["name"] != "devbuddy":
        fail("Skill name must be devbuddy")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", frontmatter["name"]):
        fail("Skill name must be lowercase hyphen-case")
    if not frontmatter["description"] or len(frontmatter["description"]) > 1024:
        fail("Skill description must be present and at most 1024 characters")
    if "<" in frontmatter["description"] or ">" in frontmatter["description"]:
        fail("Skill description must not contain angle brackets")

    required_skill_text = [
        "## Codex Plan Mode",
        "<proposed_plan>",
        "Do not edit repo-tracked files",
        "## GPT-5.6-Aware Execution",
        "references/gpt-5.6.md",
        "lowest sufficient model tier and effort",
        "agents/shared/orchestration.md",
        "references/reusable-tools.md",
        "scripts/devbuddy_scaffold.py",
        "workflows/loop-workflow.md",
    ]
    missing = [needle for needle in required_skill_text if needle not in skill_text]
    if missing:
        fail(f"SKILL.md is missing expected Codex guidance: {missing}")

    gpt_56_reference = SKILL / "references" / "gpt-5.6.md"
    if not gpt_56_reference.exists():
        fail("skill/references/gpt-5.6.md is missing")
    gpt_56_text = gpt_56_reference.read_text(encoding="utf-8")
    required_gpt_56_text = [
        "Sol",
        "Terra",
        "Luna",
        "Programmatic Tool Calling",
        "Delegated model selection",
        "https://openai.com/index/gpt-5-6/",
    ]
    missing_gpt_56 = [needle for needle in required_gpt_56_text if needle not in gpt_56_text]
    if missing_gpt_56:
        fail(f"gpt-5.6.md is missing expected guidance: {missing_gpt_56}")

    openai_text = OPENAI_YAML.read_text(encoding="utf-8")
    required_openai_text = [
        'display_name: "DevBuddy"',
        'short_description: "Senior engineering workflow for Codex"',
        "Use $devbuddy",
    ]
    missing_meta = [needle for needle in required_openai_text if needle not in openai_text]
    if missing_meta:
        fail(f"agents/openai.yaml is missing expected metadata: {missing_meta}")

    forbidden = [path.name for path in SKILL.iterdir() if path.name in MEMORY_FILES]
    if forbidden:
        fail(f"Runtime memory files must not be committed in skill/: {forbidden}")

    scaffold_text = SCAFFOLD_SCRIPT.read_text(encoding="utf-8")
    required_scaffold_text = [
        "docs/adr",
        "reports/analysis",
        "reports/implementations",
        "reports/lessons-learned",
        "reports/plans",
        "reports/qa",
        "reports/reviews",
        "Reusable Tools",
        "obsidian_vault",
    ]
    missing_scaffold = [needle for needle in required_scaffold_text if needle not in scaffold_text]
    if missing_scaffold:
        fail(f"devbuddy_scaffold.py is missing expected setup features: {missing_scaffold}")

    claude_refs = []
    for path in SKILL.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
            text = path.read_text(encoding="utf-8")
            if any(token in text for token in ("Claude Code", ".claude", "canonical Claude")):
                claude_refs.append(str(path.relative_to(ROOT)))
    if claude_refs:
        fail(f"Codex skill contains Claude-specific references: {claude_refs}")

    print("OK: DevBuddy Codex skill is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
