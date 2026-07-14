"""Health and readiness probes for the preview runtime."""

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class HealthState:
    started_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    events_seen: int = 0
    errors_seen: int = 0
    adapters: dict = field(default_factory=dict)

    def record(self, event_type):
        self.events_seen += 1
        if event_type.endswith("error"):
            self.errors_seen += 1

    def report(self):
        return {"status": "degraded" if self.errors_seen else "healthy", "started_at": self.started_at, "events_seen": self.events_seen, "errors_seen": self.errors_seen, "adapters": self.adapters}
