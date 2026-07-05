# Analyze Workflow

1. Classify the analysis goal and the smallest context needed.
2. Read project memory and relevant ADRs only when project-specific technical context, business rules, prior decisions, or durable lessons affect the analysis.
3. Inspect affected source code and tests only when current behavior, expected behavior, risks, or implementation planning depend on them.
4. Identify existing behavior and expected behavior from the smallest reliable evidence.
5. Map business rules and technical constraints that materially affect correctness.
6. Record unknowns that materially affect correctness.
7. Update relevant memory sections if durable project understanding was learned and the host workflow allows file edits. Use `templates/context-template.md` and `templates/business-template.md` under `reports/analysis/` when a durable analysis record is useful.

