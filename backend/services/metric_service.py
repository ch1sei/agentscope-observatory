"""Metric aggregation boundary for the observability preview."""

from collections import defaultdict


class MetricService:
    def __init__(self):
        self.samples = defaultdict(list)

    def record(self, name, value, tags=None):
        self.samples[name].append({"value": value, "tags": tags or {}})

    def count(self, name):
        return len(self.samples.get(name, []))

    def values(self, name):
        return [item["value"] for item in self.samples.get(name, [])]

    def average(self, name):
        values = self.values(name)
        return sum(values) / len(values) if values else 0

    def summary(self):
        return {name: {"count": len(items), "average": self.average(name)} for name, items in self.samples.items()}
