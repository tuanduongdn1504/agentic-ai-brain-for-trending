#!/usr/bin/env python3
"""
Audit-log hook for Claude Code (PostToolUse + PreToolUse triggers).

Logs every tool invocation to ~/.claude/channels/telegram/audit.log as JSONL.
Designed for the autopilot-research project — fires for any session launched
from this project's directory (per .claude/settings.json hook config), which
includes both `claude` (interactive) AND `claude --channels` (telegram bot).

Output line format (JSONL):
    {"ts":"2026-05-08T...Z","event":"PostToolUse","tool":"Bash",
     "session":"abc12def3456","cwd":"/.../autopilot-research",
     "input":{"command":"ls","description":"..."},"ok":true}

Filter telegram-triggered calls later with:
    grep '"tool":"mcp__plugin_telegram' ~/.claude/channels/telegram/audit.log
or check session_id correlation against the telegram channel session.

Hook MUST exit 0 quickly — never block the session. All errors swallowed.
"""
import datetime as dt
import json
import os
import sys

LOG = os.path.expanduser("~/.claude/channels/telegram/audit.log")

try:
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    d = json.load(sys.stdin)
    ti = d.get("tool_input") or {}
    tr = d.get("tool_response") or {}
    out = {
        "ts": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "event": d.get("hook_event_name", "?"),
        "tool": d.get("tool_name", "?"),
        "session": str(d.get("session_id", "?"))[:12],
        "cwd": d.get("cwd", ""),
        "input": {k: str(v)[:200] for k, v in list(ti.items())[:5]} if isinstance(ti, dict) else None,
        "ok": (not bool(tr.get("isError"))) if isinstance(tr, dict) and tr else None,
    }
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(out, ensure_ascii=False) + "\n")
except Exception:
    # Never block the session — silent failure is acceptable for an audit hook
    pass

sys.exit(0)
