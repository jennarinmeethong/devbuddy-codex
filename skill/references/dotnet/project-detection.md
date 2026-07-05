# .NET Project Detection

Use this reference to understand a .NET repository before editing it.

## Files To Inspect

- `global.json`: SDK pinning, roll-forward policy, and .NET 10+ test runner selection.
- `.sln`, `.slnx`, `.slnf`: solution entry points and project grouping.
- `*.csproj`, `*.fsproj`, `*.vbproj`: SDK, target frameworks, package references, analyzers, nullable settings, implicit usings, output type, and project references.
- `Directory.Build.props`: shared build properties evaluated early.
- `Directory.Build.targets`: shared build targets evaluated late.
- `Directory.Packages.props`: central package management.
- `NuGet.config`: feeds, package source mapping, and restore behavior.
- `launchSettings.json`, `appsettings*.json`, Dockerfiles, and CI files: runtime and deployment conventions.

## Project Type Signals

| Signal | Likely project type |
| --- | --- |
| `Sdk="Microsoft.NET.Sdk.Web"` | ASP.NET Core app or Web API |
| `Microsoft.AspNetCore.*` packages | ASP.NET Core features |
| `Microsoft.EntityFrameworkCore.*` packages | EF Core data access |
| `Microsoft.NET.Test.Sdk`, `MSTest`, `xunit`, `NUnit`, `TUnit` | Test project |
| `UseMaui` or `net*-android` / `net*-ios` TFMs | .NET MAUI |
| `UseWPF` or `UseWindowsForms` | Windows desktop |
| `OutputType` = `Exe` | Executable app, worker, console, or test host |

## Baseline Questions

- Which SDK and target frameworks are actually in use?
- Is package management centralized?
- Is nullable enabled? Are warnings treated as errors?
- Which test platform is used: VSTest or Microsoft.Testing.Platform?
- Are build conventions centralized in Directory.Build files?
- Is the repo using analyzers, source generators, or custom MSBuild targets?

## Rules

- Preserve existing SDK style and project organization.
- Do not mix minimal APIs and controllers in one API project unless the repo already does.
- Do not add package versions to `.csproj` when central package management is active.
- Check multi-targeting before using APIs that only exist on one TFM.
- Prefer targeted project builds during iteration, then build the solution when risk requires it.
