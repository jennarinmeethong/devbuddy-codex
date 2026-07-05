# Angular New App Workflow

Use this workflow when the user wants a new Angular application.

When an installed Angular-specific skill is available, prefer it for scaffolding and framework procedure (see `references/optional-specialized-skills.md`); use this workflow as the fallback and as the orchestration entry that returns to DevBuddy for planning, review, and memory.

1. Determine whether the user requested a specific Angular version.
2. If a version is specified, use `npx @angular/cli@<requested_version> new <app-name> --interactive=false` and add flags from the request.
3. If no version is specified, check for an existing Angular CLI with `ng version`.
4. If `ng version` succeeds, use `ng new <app-name> --interactive=false` and add flags from the request.
5. If `ng version` fails, use `npx @angular/cli@latest new <app-name> --interactive=false` and add flags from the request.
6. Prefer `--ai-config=agents` unless another assistant config clearly matches the environment or the user asks for one.
7. Choose common flags from explicit requirements:
   - `--style=scss|css|less`
   - `--routing`
   - `--ssr`
   - `--prefix=<prefix>`
   - `--skip-tests` only when explicitly requested
8. After creation, load the generated AI configuration and project conventions before adding features.
9. Use Angular CLI generation for additional artifacts, then augment generated code to meet the product need.
10. Run `ng build` before completion when feasible and fix build errors.

Do not start the dev server until features are built or the user asks to run it.
