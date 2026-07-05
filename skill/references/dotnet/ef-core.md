# EF Core

Use this reference for EF Core data access, query behavior, and performance.

## First Checks

- Locate `DbContext`, entity configuration, migrations, repositories/services, and query call sites.
- Identify provider package: SQL Server, PostgreSQL, SQLite, Cosmos DB, in-memory, or another provider.
- Check whether tracking defaults, split query behavior, lazy loading, global filters, and migrations are configured centrally.

## Query Rules

- Avoid N+1 queries. Use projection, `Include`, `ThenInclude`, explicit loading, or `AsSplitQuery()` based on data shape.
- Prefer projections for API/read models so only needed columns are fetched.
- Use `AsNoTracking()` for read-only queries. Use `AsNoTrackingWithIdentityResolution()` when duplicate entity instances matter.
- Use `Any()` for existence checks instead of `Count() > 0`.
- Keep `Where`, `Select`, `OrderBy`, `Skip`, and `Take` in the database query before materialization.
- Avoid `ToList()` before filters or inside projections unless there is a deliberate boundary.
- Use `ExecuteUpdateAsync` and `ExecuteDeleteAsync` for bulk updates/deletes when supported and appropriate.
- Use `FromSqlInterpolated` rather than string interpolation with `FromSqlRaw`.

## Migrations And Seeding

- Do not create or apply migrations without confirming the intended schema change.
- For seeded data, avoid volatile values such as `DateTime.Now`, `DateTime.UtcNow`, or `Guid.NewGuid()` in `HasData`.
- Inspect pending migrations and startup migration behavior before changing deployment-sensitive code.

## Verification

- Enable SQL logging locally when diagnosing query shape.
- Confirm query count and generated SQL for performance changes.
- Run tests that cover data access behavior and migrations when available.
