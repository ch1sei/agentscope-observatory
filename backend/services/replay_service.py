"""Replay timeline boundary for normalized session events."""


class ReplayService:
    def prepare(self, session):
        events = sorted(session.get("events", []), key=lambda event: event.get("duration_ms", 0))
        return {"session_id": session.get("session_id"), "events": events, "mode": "synthetic"}

    def checkpoint(self, event):
        return {"event_id": event.get("id"), "label": event.get("label"), "replayable": True}

    def export_manifest(self, replay):
        return {"session_id": replay.get("session_id"), "event_count": len(replay.get("events", [])), "format": "preview-manifest"}
