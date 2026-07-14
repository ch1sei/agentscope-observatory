"""Small standard-library configuration loader for local observability runs."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ObservatoryConfig:
    storage: str = "sqlite://./var/observatory.db"
    retention_days: int = 30
    sample_rate: float = 1.0
    redact_arguments: bool = True
    adapters: list[str] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, mapping):
        telemetry = mapping.get("telemetry", {})
        runtime = mapping.get("runtime", {})
        return cls(
            storage=runtime.get("storage", cls.storage),
            retention_days=int(runtime.get("retention_days", cls.retention_days)),
            sample_rate=float(telemetry.get("sample_rate", cls.sample_rate)),
            redact_arguments=telemetry.get("capture_tool_arguments") == "redacted",
            adapters=list(mapping.get("adapters", [])),
        )

    def validate(self):
        if not 0 < self.sample_rate <= 1:
            raise ValueError("sample_rate must be between 0 and 1")
        if self.retention_days < 1:
            raise ValueError("retention_days must be positive")
        return self


def load_preview_config(path: str | Path):
    """Load the small YAML-like file without adding a YAML dependency."""
    values = {"runtime": {}, "telemetry": {}, "adapters": []}
    section = None
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.endswith(":"):
            section = line[:-1]
            continue
        if line.startswith("-"):
            values[section or "adapters"].append(line[1:].strip())
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            values.setdefault(section, {})[key.strip()] = value.strip().strip('"')
    return ObservatoryConfig.from_mapping(values).validate()
