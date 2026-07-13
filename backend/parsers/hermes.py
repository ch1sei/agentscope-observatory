"""Placeholder adapter for Hermes events."""


def parse(lines):
    return [{"source": "hermes", "raw": line} for line in lines]
