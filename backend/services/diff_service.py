"""Snapshot comparison boundary for files and memory."""


class DiffService:
    def compare(self, before, after):
        before = before or {}
        after = after or {}
        keys = sorted(set(before) | set(after))
        return {
            "added": [key for key in keys if key not in before],
            "removed": [key for key in keys if key not in after],
            "changed": [key for key in keys if key in before and key in after and before[key] != after[key]],
            "status": "preview",
        }

    def summarize(self, diff):
        return {"added": len(diff.get("added", [])), "removed": len(diff.get("removed", [])), "changed": len(diff.get("changed", []))}
