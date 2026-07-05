# Loop Engineering Workflow

Use this workflow when the task is repetitive and verification-driven, so it benefits from an autonomous `execute -> verify -> refine` cycle rather than a single pass. Typical cases: applying the same change across many files, a migration, fixing until a build or test suite is green, or hunting an intermittent failure.

Loop Engineering trades away step-by-step approval for speed, so it only earns that trade when the loop is bounded and observable. The point of this workflow is to keep the loop safe: it must know when to stop, and it must stop and ask when it stops making progress or is about to do something it cannot easily undo.

## When to enter

- The user invokes `$devbuddy` with a loop request, or clearly asks to "keep going until" a condition holds. Enter Loop Engineering directly.
- The task looks loop-shaped (see above) but the user did not ask for a loop. Say why it looks loop-shaped and ask before entering. Do not auto-start a loop.
- Implementation inside the loop still respects the normal plan-approval gate: if the loop will change code and a plan was required, get the plan approved first.

## Entry: define the guardrails up front

Before the first iteration, agree on and state:

1. Goal: what "done" means in one sentence.
2. Exit condition: a concrete, testable signal that ends the loop (for example "`dotnet test` passes", "all N files migrated", "the target endpoint returns 200"). If you cannot name a testable exit condition, do not loop.
3. Verification command: the exact check run each iteration to measure progress toward the exit condition.
4. Max iterations: a cap that ends the loop even if the exit condition is never met, so a stuck loop is bounded.

## Each iteration

1. Make the smallest change that should move toward the exit condition.
2. Run the agreed verification command.
3. Record a one-line iteration summary: what changed, the result, and the next intended step. Keep these summaries so the loop's history is visible and a stuck loop is easy to spot.

## Stop and report

Stop the loop and hand back to the user when any of these is true:

- The exit condition is met.
- The max iteration count is reached.
- The same failure repeats without measurable progress (the loop is stuck; more iterations will not help).
- The next step needs a hard-to-reverse or out-of-scope action: deleting data, a schema or data migration, an external or networked call, or a dependency/package change. Surface it and ask rather than doing it inside the loop.

## On exit

- Summarize the iterations run, the final state, and whether the exit condition was met.
- Name the verification evidence (command, result, key failure lines) as the implementation workflow requires.
- Update project memory when the loop produced durable knowledge: a recurring failure mode or proven fix in `KnowledgeBase.md`, a durable trade-off in `DecisionLog.md`. This keeps Loop Engineering consistent with the Definition of Done.
