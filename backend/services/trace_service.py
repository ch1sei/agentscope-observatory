"""Trace service contract for normalized agent events."""


class TraceService:
    def ingest(self, events):
        return {"accepted": len(events), "trace_id": "trace_preview"}

    def build_dag(self, session):
        return {"nodes": session.get("events", []), "edges": []}
