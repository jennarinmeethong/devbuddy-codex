# .NET New App Workflow

Use this workflow when the user wants a new .NET application, library, API, worker, test project, Blazor app, or MAUI app.

When an installed .NET-specific skill is available, prefer it for scaffolding and framework procedure (see `references/optional-specialized-skills.md`); use this workflow as the fallback and as the orchestration entry that returns to DevBuddy for planning, review, and memory.

1. Determine the intended app type, target framework, name, output path, and whether the user requested a specific template.
2. Check `dotnet --version` and `dotnet new list` when feasible. If a repo has `global.json`, respect its SDK.
3. Use `dotnet new <template>` with explicit `--name` and `--output` values.
4. Prefer common templates by intent:
   - Web API: `dotnet new webapi`
   - Minimal empty ASP.NET Core host: `dotnet new web`
   - Console tool: `dotnet new console`
   - Class library: `dotnet new classlib`
   - Worker service: `dotnet new worker`
   - MSTest/xUnit/NUnit test project: `dotnet new mstest`, `dotnet new xunit`, or `dotnet new nunit`
   - Blazor app: `dotnet new blazor`
   - MAUI app: `dotnet new maui` only when workloads are installed or the user accepts workload setup
5. If adding to an existing solution, run `dotnet sln <solution> add <project>` after project creation.
6. If package versions are centralized, add package versions to `Directory.Packages.props` instead of individual project files.
7. For Web APIs, load `references/dotnet/webapi.md` before adding endpoints, DTOs, OpenAPI, or error handling.
8. For test projects, load `references/dotnet/testing.md` before choosing runner packages or filters.
9. Run `dotnet restore` if package references changed, then `dotnet build`.
10. Run relevant tests with the platform-correct command before completion when tests exist.

Do not start a development server until the project is created, builds successfully, and the user asks to run it.
