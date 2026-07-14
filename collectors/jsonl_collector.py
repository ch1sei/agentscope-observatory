"""JSONL collector with redaction and sampling boundaries."""

import json
import random
from dataclasses import dataclass
from typing import Iterable


@dataclass
class CollectorOptions:
    sample_rate: float = 1.0
    redact_keys: tuple[str, ...] = ("token", "secret", "password", "authorization")


class JsonlCollector:
    def __init__(self, options=None, rng=None):
        self.options = options or CollectorOptions()
        self.rng = rng or random.Random(0)

    def collect(self, lines: Iterable[str]):
        accepted = []
        for line_number, line in enumerate(lines, 1):
            if self.rng.random() > self.options.sample_rate:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                accepted.append({"event_type": "collector.error", "line": line_number, "error": str(exc)})
                continue
            accepted.append(self.normalize(event, line_number))
        return accepted

    def normalize(self, event, line_number=0):
        normalized = dict(event)
        normalized.setdefault("event_id", f"collected-{line_number}")
        normalized.setdefault("event_type", "unknown")
        normalized["attributes"] = self._redact(normalized.get("attributes", {}))
        return normalized

    def _redact(self, attributes):
        return {key: "[REDACTED]" if key.lower() in self.options.redact_keys else value for key, value in attributes.items()}
