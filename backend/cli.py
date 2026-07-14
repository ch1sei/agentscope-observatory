"""Command-line entry point for a dependency-free preview run."""

import argparse
import json
from pathlib import Path

from backend.runtime.health import HealthState
from collectors.jsonl_collector import JsonlCollector


def main(argv=None):
    parser = argparse.ArgumentParser(prog="observatory")
    parser.add_argument("--input", type=Path)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args(argv)
    health = HealthState()
    lines = args.input.read_text(encoding="utf-8").splitlines() if args.input else []
    events = JsonlCollector().collect(lines)
    for event in events:
        health.record(event.get("event_type", "unknown"))
    payload = health.report()
    payload["events"] = len(events)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
