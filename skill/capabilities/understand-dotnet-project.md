# Understand .NET Project

Use this capability when the task targets .NET, C#, ASP.NET Core, Blazor, MAUI, EF Core, MSBuild, NuGet, `dotnet test`, or when the repository contains markers such as `.sln`, `.slnx`, `.csproj`, `.fsproj`, `.vbproj`, `global.json`, `Directory.Build.props`, `Directory.Build.targets`, `Directory.Packages.props`, or `NuGet.config`.

If the current session exposes an installed .NET-specific skill that matches the task, use that specialized skill for .NET procedure and API details, then return to the senior developer workflow for planning, review, and memory updates. If no matching specialized skill is available, use the bundled references below.

When choosing whether to install or delegate to a separate .NET skill, see `references/optional-specialized-skills.md`.

Before giving .NET guidance:

- Identify the SDK from `global.json` and `dotnet --version` when commands are feasible.
- Identify target frameworks from project files, including multi-targeting via `TargetFrameworks`.
- Inspect project type from the SDK attribute and package references: Web SDK, WindowsDesktop SDK, test packages, EF Core packages, MAUI workloads, Blazor packages, or worker templates.
- Prefer the repository's existing style for solution layout, nullable settings, analyzers, package management, testing, logging, DI, and API shape.
- Use `dotnet` CLI commands that match the project type and SDK version. Avoid adding packages or migrations until project conventions are known.
- Run `dotnet build` after code or project-file changes when feasible. Run targeted tests for behavior changes, then broader tests when risk is medium or higher.

Load only the relevant .NET references:

- Project detection and repo shape: `references/dotnet/project-detection.md`
- ASP.NET Core Web APIs and endpoint changes: `references/dotnet/webapi.md`
- EF Core data access and query performance: `references/dotnet/ef-core.md`
- Test running, filters, and test platform detection: `references/dotnet/testing.md`
- MSBuild, project files, binlogs, build performance, and Directory.Build files: `references/dotnet/msbuild.md`
- Version upgrades and breaking-change triage: `references/dotnet/upgrade.md`
- Diagnostics, traces, dumps, and runtime performance investigation: `references/dotnet/diagnostics.md`

If creating a new .NET application or project, use `workflows/dotnet-new-app-workflow.md` before generating files.
