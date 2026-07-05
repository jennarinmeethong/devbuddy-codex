# Optional Specialized Skills

Use this reference when the user asks whether to install Angular or .NET skills separately, asks which specialized skill to use, or wants the agent to prefer installed skills over bundled references.

These skills are optional. This senior developer skill works without them by using bundled references under `references/angular/` and `references/dotnet/`. If a matching specialized skill is installed and visible in the current session, prefer it for framework-specific procedures, scripts, or deeper details, then return to this skill for business analysis, planning, review, and memory updates.

Do not depend on any temporary or local source checkout at runtime.

## Source Collections

- .NET skills: [dotnet/skills](https://github.com/dotnet/skills)
- Angular skills: [angular/skills](https://github.com/angular/skills)

## Angular

| Specialized area | Use when | Bundled fallback |
| --- | --- | --- |
| Angular project guidance | Angular workspace analysis, components, services, signals, DI, routing, rendering, accessibility, styling, testing, CLI, migrations, or new app setup | `capabilities/understand-angular-project.md`, `workflows/angular-new-app-workflow.md`, `references/angular/*` |

## .NET Core And Application

| Specialized skill or area | Use when | Bundled fallback |
| --- | --- | --- |
| `csharp-scripts` | Running file-based C# apps or small C# experiments without creating a project | `capabilities/understand-dotnet-project.md` |
| `dotnet-pinvoke` | Native interop, P/Invoke signatures, marshaling, and platform invocation issues | `references/dotnet/diagnostics.md`, `references/dotnet/project-detection.md` |
| `nuget-trusted-publishing` | NuGet package publishing and trusted publishing setup | `references/dotnet/project-detection.md`, `references/dotnet/msbuild.md` |
| `convert-to-cpm` | Migrating package versions to Central Package Management | `references/dotnet/project-detection.md`, `references/dotnet/msbuild.md` |

## ASP.NET Core And Blazor

| Specialized skill or area | Use when | Bundled fallback |
| --- | --- | --- |
| `dotnet-webapi` | ASP.NET Core Web API endpoints, OpenAPI, DTOs, HTTP semantics, and API error handling | `references/dotnet/webapi.md` |
| `configuring-opentelemetry-dotnet` | ASP.NET Core tracing, metrics, logging, OTLP exporters, and trace correlation | `references/dotnet/diagnostics.md` |
| `minimal-api-file-upload` | File uploads in ASP.NET Core minimal APIs | `references/dotnet/webapi.md` |
| `convert-blazor-server-to-webapp` | Migrating Blazor Server apps to newer Blazor Web App patterns | `references/dotnet/project-detection.md` |
| Blazor component skills | Blazor components, auth, data fetching, prerendering, JS interop, component coordination, and new Blazor projects | `capabilities/understand-dotnet-project.md`, `references/dotnet/webapi.md` |

## .NET Data

| Specialized skill or area | Use when | Bundled fallback |
| --- | --- | --- |
| `optimizing-ef-core-queries` | EF Core query performance, N+1 query issues, tracking modes, compiled queries, SQL shape, or database load from LINQ | `references/dotnet/ef-core.md` |

## .NET Testing

| Specialized skill or area | Use when | Bundled fallback |
| --- | --- | --- |
| `run-tests` | Running or filtering `dotnet test`, VSTest vs Microsoft.Testing.Platform detection, TRX/reporting, blame, or multi-TFM test runs | `references/dotnet/testing.md` |
| `filter-syntax` and `platform-detection` | Test filter syntax or test platform/framework detection details | `references/dotnet/testing.md` |
| `writing-mstest-tests` | Writing MSTest tests | `references/dotnet/testing.md` |
| Test migration skills | Migrating MSTest, xUnit, VSTest, or Microsoft.Testing.Platform projects | `references/dotnet/testing.md`, `references/dotnet/upgrade.md` |
| Test quality skills | Coverage analysis, assertion quality, test anti-patterns, smell detection, test tagging, test gap analysis, maintainability, static dependency detection, or testability wrappers | `references/dotnet/testing.md` |

## .NET MSBuild And NuGet

| Specialized skill or area | Use when | Bundled fallback |
| --- | --- | --- |
| `binlog-generation` and `binlog-failure-analysis` | Generating or analyzing MSBuild binary logs | `references/dotnet/msbuild.md` |
| Build performance skills | Cold/warm/no-op baselines, build performance diagnostics, incremental builds, parallelism, graph builds, MSBuild server, evaluation performance, or bin/obj clashes | `references/dotnet/msbuild.md` |
| MSBuild authoring skills | Directory.Build organization, target authoring, extension points, generated files, item management, property patterns, anti-patterns, modernization, or project reference resolution | `references/dotnet/msbuild.md` |
| Template engine skills | Authoring, validating, discovering, comparing, instantiating, or improving `dotnet new` templates | `workflows/dotnet-new-app-workflow.md`, `references/dotnet/msbuild.md` |

## .NET Diagnostics, MAUI, AI, And Upgrade

| Specialized skill or area | Use when | Bundled fallback |
| --- | --- | --- |
| `analyzing-dotnet-performance`, `dotnet-trace-collect`, `dump-collect`, or `microbenchmarking` | Runtime performance, traces, dumps, counters, hangs, crashes, or benchmark design | `references/dotnet/diagnostics.md` |
| Apple or Android crash symbolication skills | Symbolicating .NET runtime frames in Apple crash logs or Android tombstones | `references/dotnet/diagnostics.md` |
| .NET MAUI skills | MAUI project health, app lifecycle, CollectionView, data binding, DI, safe area, Shell navigation, or theming | `capabilities/understand-dotnet-project.md`, `references/dotnet/diagnostics.md` |
| .NET AI skills | MCP server creation/debugging/testing/publishing in C#, AI technology selection, ML.NET, Microsoft.Extensions.AI, ONNX, RAG, or agentic workflows | `capabilities/understand-dotnet-project.md` |
| .NET upgrade skills | .NET version upgrades, nullable reference migrations, AOT compatibility, or Thread.Abort migration | `references/dotnet/upgrade.md` |
