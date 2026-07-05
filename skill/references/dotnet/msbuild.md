# MSBuild And Project Files

Use this reference for `.csproj`, `.props`, `.targets`, restore/build issues, binlogs, and build performance.

## First Checks

- Inspect project files plus `Directory.Build.props`, `Directory.Build.targets`, `Directory.Packages.props`, `NuGet.config`, and `global.json`.
- Determine whether the project is SDK-style.
- Check target frameworks, package management, project references, nullable settings, analyzers, generated files, and custom targets.

## Project File Rules

- Put shared early properties in `Directory.Build.props`.
- Put target-framework-dependent or late-bound settings in `Directory.Build.targets` when needed.
- With central package management, keep versions in `Directory.Packages.props`.
- Use conditional defaults so projects can override shared properties.
- Avoid hardcoded `bin` and `obj` paths. Prefer MSBuild properties such as `$(OutputPath)`, `$(IntermediateOutputPath)`, and `$(BaseIntermediateOutputPath)`.
- For generated files, write to intermediate output, add generated sources to the right item group, and register outputs in `FileWrites` when clean support matters.

## Build Diagnostics

- Generate a binlog for unclear build failures or performance issues: `dotnet build /bl:{} -m`.
- In PowerShell, escape braces if needed: `/bl:{{}}`.
- Use `-m` for parallel builds unless the repo disables it for a reason.
- Establish cold, warm, and no-op baselines before optimizing build performance.
- For slow no-op builds, look for custom targets missing `Inputs` and `Outputs`.
- For evaluation slowness, inspect globs, imports, property functions, and very large preprocessed output.

## Common Anti-Patterns

- Replacing SDK target chains instead of appending to `$(XxxDependsOn)`.
- Unquoted conditions that break when properties are empty.
- Restating SDK defaults in every project.
- Adding duplicate package versions across many projects when CPM should be used.
- Using `Exec` when a built-in MSBuild task exists.
- Dynamically creating `ProjectReference` items inside targets, which can break graph builds.

## Verification

- Run a targeted `dotnet build` while iterating.
- Run solution-level build after shared build file changes.
- Capture a binlog when diagnosing non-obvious failures.
