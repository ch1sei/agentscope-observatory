# AgentScope Observatory

> Framework-agnostic observability, replay, evaluation, and operations workspace for agent systems.

AgentScope Observatory is a product-shaped prototype for understanding what an agent did, why it did it, what changed during execution, and where a run became slow, expensive, unreliable, or risky.

## Product Surface

- Full execution timeline from prompt intake to final response
- Model request, tool call, memory write, file change, and error events
- Session traces with correlation IDs and parent-child relationships
- DAG and waterfall views for multi-step workflows
- Token, latency, cost, retry, and success-rate metrics
- File system and memory snapshot comparison
- Session replay with step-by-step evidence inspection
- Framework adapter contracts for Nanobot, OpenClaw, and Hermes
- Agent, model, tool, environment, and version comparison
- Incident annotations, saved views, and exportable reports
- Retention, sampling, redaction, and workspace configuration

## Console Areas

### Overview

The overview page summarizes sessions today, active sessions, tool success rate, median and p95 latency, token consumption, estimated spend, warnings, retries, and policy events.

### Trace Explorer

Trace Explorer is designed to show expandable execution timelines, parent-child spans, model and tool boundaries, request previews, retry markers, error origins, recovery paths, and searchable metadata.

### Session Replay

Replay presents a session as an inspectable sequence. Each step can expose the request, response, selected tool, observed result, state transition, and related evidence.

### Diff Workspace

The diff workspace is intended to compare memory, files, tool permissions, context size, model runs, and agent versions against the same fixture.

### Comparisons

Comparison views cover Model A versus Model B, agent version N versus N+1, framework adapters, baseline versus optimized prompts, and evaluation fixtures.

## Event Model

The intended normalized event envelope looks like this:

```json
{
  "event_id": "evt_001",
  "session_id": "sess_8f31c2",
  "trace_id": "trace_01",
  "parent_id": null,
  "event_type": "tool.call",
  "name": "browser.search",
  "status": "ok",
  "started_at": "2026-07-13T10:00:00Z",
  "duration_ms": 4300,
  "attributes": {},
  "redactions": []
}
```

Adapters can translate JSONL logs, hook output, callback payloads, or exported traces into this framework-neutral shape.

## Architecture

```text
Agent runtime / framework hooks
            |
            v
Collectors -> Normalized event envelope -> Parsers
                                           |
                                           v
                              Trace / Metric / Diff services
                                           |
                                           v
                            Dashboard / Replay / Reports
```

## Repository Layout

```text
agentscope-observatory/
├── backend/                 API, storage, models, parsers, services
├── collectors/              Hook and log collection boundary
├── config/                  Workspace configuration examples
├── examples/                Synthetic sessions and fixtures
├── frontend/                Static observability console
├── tests/                   Test layout placeholder
└── docs/                    Roadmaps and operations notes
```

## Configuration

`config/observatory.yaml` demonstrates storage, retention, sampling, token capture, redaction, file diffs, and framework adapters.

Important settings include `retention_days`, `capture_tool_arguments`, `capture_file_diffs`, `sample_rate`, and `adapters`.

## Local Preview

No packages are installed and no model files are downloaded.

```bash
conda env create -f environment.yml
conda activate agentscope-observatory
```

The environment file intentionally declares no dependencies. Open `frontend/index.html` directly in a browser to view the static console.

## Roadmap

- Normalize event envelopes across framework adapters
- Add trace ingestion health and retention controls
- Add saved queries and workspace filters
- Add replay evidence panels
- Add report export and review annotations
- Add evaluation-run comparison and regression alerts
- Add redaction policies for secrets and personal data
- Add local, team, and hosted deployment profiles

## Prototype Scope

This is an architectural and visual prototype. The dashboard uses synthetic data, service modules are interface placeholders, and the project is not presented as a production-ready telemetry backend.
