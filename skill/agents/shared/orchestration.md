# DevBuddy Agent Orchestration

## Purpose

Keep DevBuddy's main agent responsible for business understanding, planning, approval, implementation discipline, review, and memory updates while using focused agents only when they reduce risk or context load.

## Main Agent Responsibilities

- Read the user request and DevBuddy entrypoint before planning; load memory, ADRs, source, and tests only when they materially affect the task.
- Decide whether the work is small enough to handle directly or large enough to route through a focused role.
- Provide subagents only the goal, relevant paths or areas, constraints, and expected output.
- Integrate subagent findings into one business-aware plan or final answer.
- Preserve DevBuddy's memory, review, approval, and definition-of-done rules.

## Subagent Routing

Use a subagent when the task benefits from bounded, focused work:

- Use `analyze` for read-only discovery, affected-area mapping, risk discovery, and implementation planning.
- Use `ba` for business requirements, stakeholders, workflows, domain rules, acceptance criteria, prioritization, and business readiness.
- Use `sa` for system analysis, architecture boundaries, module responsibilities, API or integration contracts, data flow, runtime behavior, non-functional requirements, and architecture risk.
- Use `frontend` for Angular, React, Next.js UI, Vue, Nuxt UI, Svelte, jQuery, Blazor UI, UI behavior, accessibility, responsive behavior, visual consistency, routing, state, forms, and frontend tests.
- Use `backend` for .NET, ASP.NET Core, Java, Go, Rust, Node.js, Python, APIs, data models, persistence, runtime configuration, security, diagnostics, performance, and backend tests.
- Use `qa` for post-change quality review, regression risk, missing tests, acceptance checks, and verification strategy.
- Use `tester` for test case design, manual or automated test execution, defect reproduction, test data, acceptance validation, regression suites, and test evidence summaries.
- Use `docs` for README files, usage guides, migration notes, changelogs, skill docs, adapter docs, and documentation consistency.
- Use `data` when correctness depends on data shape, migrations, ownership, query behavior, compatibility, or integrity.
- Use `operations` only when the user explicitly asks for operations, DevOps, infrastructure, release, deployment, hosting, CI/CD, Docker, runtime environment, or operational readiness help.

Do not select `operations` automatically for generic build failures, test failures, backend configuration, scripts, Dockerfiles, or deployment-adjacent files unless the user's request clearly names an operations intent.

Avoid subagents when the task is narrow, the main agent already has enough context, or the routing overhead would exceed the benefit.

When a task names a stack or when role ownership is ambiguous, read `references/tech-stack-routing.md` and route by affected behavior. Use both `frontend` and `backend` for cross-stack work such as Next.js, Nuxt, SvelteKit, or Blazor when UI behavior and server/runtime behavior both affect correctness.

## Context Contract

When routing work, include only:

- The specific goal and success criteria.
- Relevant files, folders, symbols, commands, or user-facing workflow.
- Current mode and mutation constraints.
- Required output shape.
- Any known business rules, assumptions, or unresolved questions.

Do not send broad repository context, long logs, or unrelated memory unless it is required for correctness.

## Output Contract

Focused agents should return concise findings:

- Business and technical summary.
- Detected stack, selected role, and whether an installed specialized skill, bundled reference, or repo/project fallback was used.
- Files or areas inspected.
- Findings with file references when applicable.
- Risks, unknowns, and confidence.
- Recommended next steps or tests.

Do not paste full files or long command output. Summarize evidence and cite the smallest useful reference.

## Skill Mapping

- Use DevBuddy for senior-engineering workflow, architecture, planning, implementation discipline, review, memory, and multi-stack routing.
- Use `references/tech-stack-routing.md` to select `frontend`, `backend`, or both for Angular, React, Next.js, Vue, Nuxt, Svelte, jQuery, Blazor, .NET, Java, Go, Rust, Node.js, Python, and similar stacks.
- Use more specific installed stack skills when available, then return to DevBuddy for trade-offs, review, and learning.
- Use document, PDF, spreadsheet, image, browser, plugin, or skill-creation skills only when the task matches those domains.

## Token Policy

- Treat general skill questions as skill-only tasks: inspect relevant skill instructions or resources and skip project memory, ADRs, source, and tests.
- Load `Context.md`, `BusinessContext.md`, `DecisionLog.md`, and `KnowledgeBase.md` only for project-specific technical context, business rules, prior decisions, or reusable lessons.
- Inspect source and tests only for implementation, review, debugging, planning, or project-specific analysis.
- Prefer targeted source inspection over broad reads.
- Search before opening large files.
- Load references only when the current task needs them.
- Keep subagent prompts narrow and outputs compact.
- Summarize logs and test output instead of copying them verbatim.
- Reuse existing findings rather than asking multiple agents to read the same files.
