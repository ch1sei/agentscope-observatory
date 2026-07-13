"""Placeholder adapter for OpenClaw events."""


def parse(lines):
    return [{"source": "openclaw", "raw": line} for line in lines]
