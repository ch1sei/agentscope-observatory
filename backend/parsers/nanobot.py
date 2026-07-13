"""Placeholder adapter for Nanobot JSONL events."""


def parse(lines):
    return [{"source": "nanobot", "raw": line} for line in lines]
