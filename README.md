# DevBuddy Codex

DevBuddy Codex is a Codex-native skill that guides coding agents through senior-engineering workflow: understand business intent, inspect architecture, produce decision-complete plans, make minimal maintainable changes, review work, and preserve durable project knowledge.

The installable skill lives in `skill/`. Repository-level files such as this README and validation scripts stay outside that folder so Codex loads only the skill materials it needs.

## Install Locally

Install or refresh the skill by copying `skill/` to your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills/devbuddy"
rsync -a --delete --exclude '.DS_Store' skill/ "${CODEX_HOME:-$HOME/.codex}/skills/devbuddy/"
```

Start a fresh Codex thread after installing so `$devbuddy` appears in the available skills list.

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

Runtime project memory is intentionally not committed here. DevBuddy writes project memory to the location resolved by `devbuddy.config.md` or, by default, `.devbuddy/` in the target project.
