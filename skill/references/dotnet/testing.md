# .NET Testing

Use this reference for running, filtering, or troubleshooting .NET tests.

## Detect Platform First

Check these files before choosing a command:

- `global.json`: .NET 10+ can set `"test": { "runner": "Microsoft.Testing.Platform" }`.
- Test `.csproj`: framework packages and `TestingPlatformDotnetTestSupport`.
- `Directory.Build.props`: shared test platform properties.
- `Directory.Packages.props`: centrally managed test package versions.

## Platform Signals

| Signal | Platform |
| --- | --- |
| `global.json` has `test.runner = Microsoft.Testing.Platform` | MTP on SDK 10+ |
| `TestingPlatformDotnetTestSupport` is `true` | MTP on SDK 8/9 |
| `Microsoft.NET.Test.Sdk` with adapter packages and no MTP signal | VSTest |

## Command Shapes

- VSTest: `dotnet test [path] --filter "<expr>" --logger trx`
- MTP on SDK 8/9: `dotnet test [path] -- <mtp args>`
- MTP on SDK 10+: `dotnet test --project <path> <mtp args>` or `dotnet test --solution <path> <mtp args>`

## Common Mistakes

- Do not use `--logger trx` for MTP. Use `--report-trx` when the TRX extension is available.
- Do not use `--report-trx` for VSTest. Use `--logger trx`.
- Do not put MTP args before `--` on SDK 8/9.
- Do not use `-- --arg` on SDK 10+ MTP.
- Do not use VSTest filter syntax for xUnit v3 on MTP when framework-specific flags are required.
- If the user asks for a subset, inspect category/trait attributes and run a filtered subset instead of the whole suite.

## Framework Tags

| Framework | Common category attribute |
| --- | --- |
| MSTest | `TestCategory` |
| NUnit | `Category` |
| xUnit | `Trait` |
| TUnit | `Category` |

Report the command used and summarize failures by test name, assertion, and likely cause.
