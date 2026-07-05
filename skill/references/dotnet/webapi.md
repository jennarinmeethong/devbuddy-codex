# ASP.NET Core Web API

Use this reference for ASP.NET Core HTTP API work.

## First Checks

- Identify API style: controllers, minimal APIs, or endpoint groups. Follow the existing style.
- Inspect `Program.cs`, route registration, DI setup, OpenAPI setup, validation, exception handling, and existing DTOs.
- Avoid exposing EF Core entities directly in request or response bodies.

## Endpoint Rules

- Use correct HTTP semantics:
  - `GET` single: `200 OK` or `404 Not Found`
  - `GET` list: `200 OK`
  - `POST` create: `201 Created` with a `Location` header
  - `PUT` update: `200 OK`, `400 Bad Request`, or `404 Not Found`
  - `DELETE`: `204 No Content`, `404 Not Found`, or `409 Conflict`
- Accept and forward `CancellationToken` through async calls.
- Prefer immutable DTOs such as `sealed record` types when compatible with project style.
- Use `DateTimeOffset` for API date/time values unless the domain requires another representation.
- For minimal APIs, prefer `TypedResults` and explicit `Results<T1,T2>` return types when multiple result types are possible.

## OpenAPI And Errors

- For .NET 9+ new APIs, prefer built-in OpenAPI with `AddOpenApi()` and `MapOpenApi()`.
- Do not introduce Swashbuckle into a .NET 9+ project unless the repo already uses it or the user asks.
- Add endpoint names, summaries, descriptions, and response metadata where the project uses OpenAPI.
- Prefer centralized error handling with `AddProblemDetails()` and `UseExceptionHandler()` for ASP.NET Core 8+.
- Do not leak internal exception messages in production Problem Details.

## Verification

- Run `dotnet build`.
- Run relevant API tests if present.
- Add or update `.http` files when the repo uses them for manual API checks.
