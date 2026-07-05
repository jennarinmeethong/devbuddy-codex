# Understand Angular Project

Use this capability when the task targets Angular code or a repository contains Angular markers such as `angular.json`, `@angular/core`, `@angular/cli`, `ng`, standalone components, Angular routes, or Angular templates.

If the current session exposes an installed Angular-specific skill that matches the task, use that specialized skill for Angular procedure and API details, then return to the senior developer workflow for planning, review, and memory updates. If no matching specialized skill is available, use the bundled references below.

When choosing whether to install or delegate to a separate Angular skill, see `references/optional-specialized-skills.md`.

Before giving Angular guidance:

- Identify the Angular version from `package.json`, `ng version`, lockfiles, or generated project files.
- Inspect existing architecture before adding code: standalone vs NgModule usage, routing shape, state strategy, forms strategy, styling approach, testing stack, SSR/hydration setup, and CLI conventions.
- Prefer Angular CLI generation for components, services, directives, pipes, routes, guards, interceptors, resolvers, interfaces, enums, and classes.
- Follow the existing app pattern when maintaining a project. For new Angular v21+ forms, prefer signal forms unless the project already standardizes on reactive or template-driven forms.
- Run `ng build` after Angular code changes when feasible, then fix build errors before completion.

Load only the relevant Angular references:

- Components: `references/angular/components.md`, `inputs.md`, `outputs.md`, `host-elements.md`
- Reactivity: `signals-overview.md`, `linked-signal.md`, `resource.md`, `effects.md`
- Forms: `signal-forms.md`, `reactive-forms.md`, `template-driven-forms.md`
- Dependency injection: `di-fundamentals.md`, `creating-services.md`, `defining-providers.md`, `injection-context.md`, `hierarchical-injectors.md`
- Routing and rendering: `define-routes.md`, `loading-strategies.md`, `show-routes-with-outlets.md`, `navigate-to-routes.md`, `route-guards.md`, `data-resolvers.md`, `router-lifecycle.md`, `rendering-strategies.md`, `route-animations.md`
- Accessibility: `angular-aria.md`
- Styling and animation: `component-styling.md`, `tailwind-css.md`, `angular-animations.md`
- Testing: `testing-fundamentals.md`, `component-harnesses.md`, `router-testing.md`, `e2e-testing.md`
- Tooling: `cli.md`, `migrations.md`, `mcp.md`

If creating a new Angular application, use `workflows/angular-new-app-workflow.md` before generating files.
