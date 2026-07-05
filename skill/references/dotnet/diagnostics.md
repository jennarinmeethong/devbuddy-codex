# .NET Diagnostics

Use this reference for .NET runtime performance, hangs, crashes, memory, CPU, tracing, and dump collection.

## First Checks

- Identify OS, runtime version, deployment model, container status, process name/PID, and whether the issue is local, CI, staging, or production.
- Clarify symptom: high CPU, memory growth, GC pressure, slow requests, startup failure, crash, hang, deadlock, or build-time performance.
- Prefer low-impact collection first for production systems.

## Tool Selection

| Symptom | Typical tool |
| --- | --- |
| High CPU or slow requests | `dotnet-trace`, EventPipe, profiler |
| Memory growth or GC pressure | `dotnet-counters`, `dotnet-dump`, heap analysis |
| Crash | crash dump, createdump, Windows Error Reporting, container dump config |
| Hang or deadlock | full dump, thread stacks |
| Live counters | `dotnet-counters monitor` |
| Benchmarking code paths | BenchmarkDotNet |

## Collection Rules

- Avoid collecting dumps with secrets unless the user understands the risk.
- In containers, confirm writable paths and permissions for dump output.
- For production, time-box tracing and document overhead.
- Keep raw artifacts out of source control unless explicitly intended.
- Summarize findings with evidence: timestamps, counters, stacks, traces, or benchmark numbers.

## Verification

- Compare before/after measurements for performance fixes.
- For crashes and hangs, confirm the mitigation changes the observed failure mode.
- For benchmarks, separate warmup, release configuration, and realistic inputs from toy measurements.
