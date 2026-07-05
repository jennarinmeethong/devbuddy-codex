# .NET Upgrade

Use this reference for .NET target framework upgrades and breaking-change triage.

## Workflow

1. Identify current target frameworks, SDK pinning, workloads, package management, and CI/runtime images.
2. Establish a clean baseline build and test run before changing TFMs.
3. Update `TargetFramework` or `TargetFrameworks` deliberately.
4. Update Microsoft package families to the matching major version when required.
5. Restore, build, and fix compile errors before addressing runtime behavior changes.
6. Review infrastructure: `global.json`, Dockerfiles, CI setup, deployment scripts, and Visual Studio/tooling requirements.
7. Run tests and smoke-test runtime areas that are likely affected.

## High-Risk Areas To Check

- ASP.NET Core hosting, middleware, auth, OpenAPI, and DI validation.
- EF Core provider upgrades, migrations, query translation, and seeded data.
- System.Text.Json serialization behavior and source generation.
- HttpClientFactory handler behavior and logging.
- Cryptography and certificate APIs.
- Binary serialization, especially any `BinaryFormatter` usage.
- Native interop, container base images, and runtime configuration.
- Test runner changes between VSTest and Microsoft.Testing.Platform.

## Rules

- Do not upgrade across multiple major versions in one unverified leap unless the user explicitly accepts the risk.
- Do not treat a clean compile as a complete upgrade. Review behavior changes and deployment assets.
- Preserve multi-targeting when libraries still need older consumers.
- Record notable breaking-change decisions in `DecisionLog.md`.
