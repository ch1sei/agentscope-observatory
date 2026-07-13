# AgentScope Observatory

Framework-agnostic observability and session replay console for agent systems.

This repository is a product-shaped prototype. It is intentionally dependency-free: no packages are installed and no model files are downloaded. The included data is synthetic and the backend modules are interface placeholders for future implementation.

## Product Surface

- Agent execution timeline and trace graph
- Token, latency, cost, and tool success telemetry
- File and memory diff inspection
- Session replay and framework comparison
- Exportable incident and evaluation reports

## Local Environment

```bash
conda env create -f environment.yml
conda activate agentscope-observatory
```

The environment file currently declares no packages. The console can be previewed by opening `frontend/index.html` directly.
