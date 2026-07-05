# Tech Stack Routing

Use this reference when a task names a language, framework, runtime, package manager, file extension, or project convention that affects whether DevBuddy should route work to `frontend`, `backend`, or both.

## Routing Rules

- Keep `frontend` and `backend` as the primary subagent roles. Do not create or require one subagent per framework.
- Detect stacks from the user request first, then confirm from repo evidence such as manifests, lockfiles, project files, extensions, imports, route files, build config, and tests.
- Prefer an installed specialized skill when the current session exposes one that directly matches the detected stack and task.
- Use bundled references only when they exist and match the task. For stacks without bundled deep references, rely on repo inspection, ecosystem conventions, and project docs.
- Route cross-stack work to both roles when UI behavior and server/runtime behavior are both part of correctness.
- In subagent output, include detected stack, selected role, and whether an installed specialized skill, bundled reference, or repo/project fallback was used.

## Stack Ownership

| Stack or signal | Primary role | Add role when | Bundled fallback |
| --- | --- | --- | --- |
| Angular, Angular CLI, `ng`, signals, Angular routing, Angular forms | `frontend` | Backend API or server runtime behavior is part of the task | `capabilities/understand-angular-project.md`, `workflows/angular-new-app-workflow.md`, `references/angular/*` |
| React, JSX, TSX, Vite React, Create React App | `frontend` | API, SSR server code, persistence, or runtime config is part of the task | Repo patterns and tests |
| Next.js, App Router, Pages Router, React Server Components | `frontend` | API routes, server actions, auth/session, caching, deployment runtime, or persistence are part of the task | Repo patterns and tests |
| Vue, Vue Router, Pinia, Vue SFC | `frontend` | Backend API or server runtime behavior is part of the task | Repo patterns and tests |
| Nuxt, Nitro, server routes | `frontend` | Nitro/server routes, auth/session, caching, deployment runtime, or persistence are part of the task | Repo patterns and tests |
| Svelte, SvelteKit, stores | `frontend` | SvelteKit endpoints, server load functions, auth/session, deployment runtime, or persistence are part of the task | Repo patterns and tests |
| jQuery, legacy DOM scripts, plugins | `frontend` | Backend templates, APIs, or server-rendered data contracts are part of the task | Repo patterns and tests |
| Blazor components, Razor components, `.razor` UI | `frontend` | EF Core, ASP.NET Core hosting, APIs, auth, persistence, or runtime behavior is part of the task | `capabilities/understand-dotnet-project.md`, `references/dotnet/*` |
| .NET, C#, ASP.NET Core, Web API, EF Core, MSBuild, NuGet | `backend` | Blazor or Razor UI behavior is part of the task | `capabilities/understand-dotnet-project.md`, `workflows/dotnet-new-app-workflow.md`, `references/dotnet/*` |
| Java, Spring, Gradle, Maven, JVM services | `backend` | UI templates or frontend app behavior is part of the task | Repo patterns and tests |
| Go, `go.mod`, Gin, Echo, Fiber, net/http | `backend` | UI templates or frontend app behavior is part of the task | Repo patterns and tests |
| Rust, Cargo, Axum, Actix, Rocket, Tauri backend | `backend` | Tauri/web UI behavior is part of the task | Repo patterns and tests |
| Node.js, Express, Fastify, NestJS, Hono, Koa | `backend` | React/Vue/Svelte/Angular UI behavior is part of the task | Repo patterns and tests |
| Python, Django, Flask, FastAPI, async workers | `backend` | Templates or frontend app behavior is part of the task | Repo patterns and tests |

## Ambiguity Defaults

- If a framework spans frontend and backend, route by affected behavior rather than framework name alone.
- If the task is only about visual behavior, forms, client routing, component state, accessibility, or frontend tests, use `frontend`.
- If the task is about APIs, persistence, validation, auth/session enforcement, runtime config, diagnostics, performance, or backend tests, use `backend`.
- If the task changes a contract between UI and API, use both roles or ask one role to inspect the boundary explicitly.
