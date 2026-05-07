# Overnight Drain Setup

Configures launchd UserAgent to run `autopilot-drain.py` at a scheduled time, wrapped in `caffeinate -i` to prevent idle sleep.

## Files

| File | Purpose |
|---|---|
| `autopilot-drain.py` | Python orchestrator: drains pending topics from `raw/topics-queue.md` → writes `raw/<date>-<slug>.md` per topic + updates queue |
| `autopilot-drain.sh` | Bash wrapper: activates venv + runs Python under `caffeinate -i -m` + captures stdout/stderr to `loop-log/` |
| `~/Library/LaunchAgents/com.cvtot.autopilot-research.plist` | launchd UserAgent — fires the wrapper at scheduled time |

## Why caffeinate, not pmset?

- `caffeinate -i` prevents idle sleep **only while the wrapped process runs**. Auto-releases when drain exits.
- `pmset -a sleep 0` modifies system-wide power policy and persists until reverted. Riskier + requires sudo.
- Display sleep is independent — `caffeinate -i` does NOT prevent display sleep, so the screen still goes dark.

## Scheduling

Edit `<plist>` → `StartCalendarInterval` block:
```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Hour</key><integer>23</integer>
    <key>Minute</key><integer>0</integer>
</dict>
```

For one-shot tonight: pick a future time on today.
For recurring nightly: same plist, just don't unload it after the run.

After editing the plist, reload it:
```bash
launchctl unload ~/Library/LaunchAgents/com.cvtot.autopilot-research.plist
launchctl load ~/Library/LaunchAgents/com.cvtot.autopilot-research.plist
launchctl list | grep cvtot   # verify loaded
```

## Manual drain (skip launchd)

```bash
cd "/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research"
source bin/autopilot-env.sh
caffeinate -i -m python bin/autopilot-drain.py
```

Or:
```bash
caffeinate -i -m bin/autopilot-drain.sh
```

## Dry-run

```bash
python bin/autopilot-drain.py --dry-run    # see what would be drained, no API calls
python bin/autopilot-drain.py --max 1      # drain just the first pending topic
```

## Output

Per topic: `raw/<YYYY-MM-DD>-<slug>.md` containing:
- Source video list (6 from yt-search top-15)
- NotebookLM summary
- 4 ask-output sections: Trends / Outliers / Gaps / Takeaways

Per run: `loop-log/(C) <date>-<hh>-autopilot-overnight.md` with run log.

The drain does NOT compile to wiki/ articles — that's the next-morning Claude Code session step.

## Idempotency / resume

If a run is interrupted, re-running skips topics whose output file already exists in `raw/`. Move the file out of the way to force a re-drain.

## Disabling

```bash
launchctl unload ~/Library/LaunchAgents/com.cvtot.autopilot-research.plist
```

Or simply delete the plist file.

## Troubleshooting

- **No fire at scheduled time:** check `launchctl print gui/$(id -u)/com.cvtot.autopilot-research`. Common cause: scheduled time is in the past — for one-shot use, pick a future minute.
- **`notebooklm` auth failed:** run `notebooklm auth check` interactively. Refresh login if needed before scheduling.
- **`yt-dlp` missing:** install via `brew install yt-dlp` or `pip install yt-dlp`. Must be on PATH for the launchd EnvironmentVariables.
- **Permissions:** the launchd UserAgent runs as the logged-in user, not root. It can read/write anywhere that user can.
