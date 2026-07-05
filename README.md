# DevBuddy Codex

DevBuddy Codex is a Codex-native skill that guides coding agents through senior-engineering workflow: understand business intent, inspect architecture, produce decision-complete plans, make minimal maintainable changes, review work, and preserve durable project knowledge.

The installable skill lives in `skill/`. Repository-level files such as this README and validation scripts stay outside that folder so Codex loads only the skill materials it needs.

## Install Locally

Install or refresh the skill with the helper script:

```bash
./scripts/install-local.sh
```

Start a fresh Codex thread after installing so `$devbuddy` appears in the available skills list.

## Package

Create a distributable skill zip:

```bash
./scripts/package-skill.sh
```

The archive is written to `dist/devbuddy-codex-skill.zip` and contains a top-level `devbuddy/` skill folder.

## Initialize Project Memory

DevBuddy keeps project memory, ADRs, reports, and reusable tools outside this repository. To scaffold those runtime files in a target project:

```bash
python3 skill/scripts/devbuddy_scaffold.py --project-root /path/to/project
```

The script respects `devbuddy.config.md` when present, supports Obsidian vault mode, and otherwise creates `.devbuddy/` under the target project.

## Validate

Run the repository-local validator:

```bash
./scripts/validate-skill.sh
```

It validates the required `SKILL.md` frontmatter, skill name, description, Codex metadata, expected Plan Mode guidance, and absence of runtime memory files from `skill/`.

## Skill Contents

- `skill/SKILL.md`: Codex skill entrypoint and senior-engineering workflow.
- `skill/agents/openai.yaml`: Codex UI metadata and default prompt.
- `skill/agents/shared/`: role guidance for focused analysis, implementation, QA, testing, documentation, operations, and data work.
- `skill/workflows/`: analysis, planning, implementation, review, debugging, learning, and loop engineering workflows.
- `skill/references/`: stack routing, reusable tool conventions, and optional specialized skill routing.
- `skill/capabilities/`, `skill/principles/`, and `skill/templates/`: progressive references loaded only when useful.
- `skill/scripts/devbuddy_scaffold.py`: deterministic setup for project memory, ADRs, reports, and reusable-tool indexes.

Runtime project memory is intentionally not committed here. DevBuddy writes project memory to the location resolved by `devbuddy.config.md` or, by default, `.devbuddy/` in the target project.
