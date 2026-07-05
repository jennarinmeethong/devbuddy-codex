# Implementation Workflow

1. Confirm the approved plan.
2. Make the smallest scoped change.
3. Follow existing project patterns.
4. If a command is unavailable, ask before switching to another command or package manager.
5. Add or update focused tests based on risk. Place newly created tests in a dedicated `tests/` folder unless the repository already has a clear intentional test layout.
6. Avoid unrelated refactors and formatting churn.
   - When the change is clearly recurring work, consider capturing it as a reusable tool per `references/reusable-tools.md` instead of redoing it by hand each time.
   - When the work is repetitive and verification-driven (for example fixing until tests pass, or applying one change across many files), consider running it as Loop Engineering per `workflows/loop-workflow.md`.
7. After code changes, name the targeted unit, integration, or UI automation checks that cover the changed behavior and ask whether to run them when test execution was not already approved.
8. When tests are run, capture the command, result, key failure lines, and artifact paths. Use `templates/qa-test-summary-template.md` under `reports/qa/` when a durable QA summary is useful.
9. Summarize changes and verification.
