# Reusable Tools

Use this reference when a task is the kind of work that will recur, so it is worth capturing as a small, parameterized tool the agent can rerun later instead of redoing the work by hand each time. Examples: extracting the same shape of data from many files, a repeated project-wide scan or count, reshaping a report format, or any check the agent finds itself performing more than once.

Building a tool is the `Build` rung of the `Delete -> Simplify -> Reuse -> Refactor -> Build` heuristic, so it is a last resort, not a first instinct. Build a tool only when reuse is genuinely likely (roughly two or more future uses). One-off work stays inline; do not create a tool for something you will run once.

## Preflight: choose the language

1. Prefer Python. Check availability with `python3 --version` or `python --version`.
2. If Python is missing, ask the user which SDKs or runtimes the machine has (for example C#/.NET, bun, Node.js, bash) and choose a language that is actually installed. Do not silently assume one.
3. If nothing suitable is available, stay inline and do the work directly rather than blocking on a tool.

Record the chosen language and its runtime in the tool's index entry so a future session knows what the tool needs before trying to run it.

## Location and discovery

- Generated tools live in a `tools/` folder at the resolved memory root (the same directory as `Context.md`, resolved via `Memory Location` in `SKILL.md`). They are project-local runtime state, not part of the version-controlled skill, so they are not synced across installs.
- Maintain `tools/README.md` as the index. One line per tool: name, purpose, language/runtime, and when to use it. This is what makes tools discoverable — without it, tools get created and forgotten, and reuse never happens.
- Start each tool file with a short header docstring: purpose, inputs/arguments, output shape, and when to use it.

## Design rules

- Make the tool dynamic: parameterize it (read arguments from the command line) so one tool covers a family of similar tasks rather than a single hardcoded case.
- Prefer the standard library or built-ins of the chosen language and avoid extra dependencies, so the tool keeps working without a package install.
- Print only the minimal result the caller needs, in a stable shape. This keeps tool output cheap to consume, consistent with the orchestration Token Policy.

## Reuse and rebuild guard

- Before building anything, read `tools/README.md`. If a matching tool already exists, use it or extend it instead of writing a duplicate.
- Before running an existing tool, confirm its runtime/SDK is still present. If the runtime is gone, ask whether to rebuild the tool in an available language rather than silently rewriting it.
