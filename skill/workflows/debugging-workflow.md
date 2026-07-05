# Debugging Workflow

Use this workflow when the task is to explain or fix incorrect behavior, a failing test, a crash, or a performance regression.

1. Reproduce the problem from the smallest reliable trigger, and capture the exact symptom, inputs, and environment.
2. Read only the code, tests, memory, and ADRs on the path between the trigger and the symptom.
3. Narrow the fault to the smallest failing unit before proposing any change, so the fix targets the cause rather than a symptom.
4. State the most likely cause as a hypothesis and confirm it with evidence (a log, a failing assertion, a minimal repro) before editing.
5. Make the smallest change that removes the cause. Avoid unrelated refactors while the bug is in flight.
6. Add or update a focused test that fails before the fix and passes after, so the bug cannot silently return.
7. Assess regression risk: name the behavior the change could affect and the checks that cover it.
8. Summarize the cause, the fix, and the verification. Record a durable lesson in `KnowledgeBase.md` only when the failure mode is likely to recur.
