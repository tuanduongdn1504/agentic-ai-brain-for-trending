# Scheduling + the app-open constraint

The most-discussed limitation across the corpus, plus two distinct workarounds. High-leverage for any operator wanting Cowork tasks to behave like real cron jobs.

## Source

- Raw: [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md), §Trends-6 + §Outliers-1

## The constraint (majority view, N=4 of 6 speakers)

- **Tech With Tim, Bart Slodyczka, Stefan Wirth** all explicitly state: for a scheduled task to execute, **computer must be on AND Claude desktop app must be open**
- **Jack Roberts** illustrates the failure mode: if your laptop is closed at 08:00 and a task is scheduled then, the task **waits until you open the machine at 10:00** — late, not skipped
- The lesson: standard Cowork scheduling is not actually background autonomy; it's "trigger when conditions are met, possibly hours late"

## Workaround #1 — Kenny Liao's cron-tool plugin

- Identifies the app-open requirement as a **"drawback"** worth eliminating
- Built a **custom plugin** that uses **native system cron tools** (macOS `launchd` / Linux `cron`) to run scheduled tasks in the **background via Claude Code**, NOT via the Cowork desktop UI
- Removes the dependency on Cowork desktop entirely; the task runs even if the user is fully logged out
- Trade-off: requires Claude Code (developer tool) — not viable for the non-technical Cowork persona

## Workaround #2 — Jack Roberts's Railway alternative

- Suggests scheduling tasks on **Railway** (cloud PaaS, https://railway.app)
- Allows automations to run **regardless of whether your laptop is open**
- Trade-off: cloud cost + setup complexity; only briefly mentioned in his course, not demonstrated

## Why this matters for the vault

- The vault's own `/loop` skill (recurring tasks) and `/schedule` skill (cloud agent / Anthropic-hosted cron) directly address the same pain point Kenny Liao + Jack Roberts work around
- See [[external|Storm Bear: routine v2.2 / autopilot-research]] — uses the same launchd cron pattern Kenny describes for nightly drains
- The autopilot-research project's `bot-start.sh` and overnight launchd setup are a real-world implementation of Workaround #1 — Vietnamese practitioner Tu Ba Khuym is in the same cluster (see [[../harness-engineering/_index]])

## Comparison table

| Approach | Background mode? | Dev skill needed? | Cost shape | Reliability |
|---|---|---|---|---|
| Stock Cowork scheduling | NO (app must be open) | NO | Cowork sub | Misses runs while laptop closed |
| Kenny Liao cron plugin | YES (local) | YES (Claude Code) | Cowork sub + zero extra | Runs while logged in; misses if laptop off |
| Jack Roberts Railway | YES (cloud) | YES (PaaS) | Cowork sub + Railway $ | Runs regardless of laptop state |
| Vault `/schedule` (Anthropic-hosted) | YES (cloud) | NO | Anthropic-managed | Closest match to "background autonomy" with no local dep |

## Key Takeaways

- Stock Cowork scheduling is a **"foreground autonomy"** model — it executes when conditions are met, including the user being present
- Two practitioner workarounds exist (Kenny's cron, Jack's Railway) — both require some technical lift
- The **app-must-be-open** constraint is the strongest argument for using `/schedule` (vault skill) rather than Cowork's built-in scheduling for any task that must run while the user is away
- The corpus is unanimous (N=6) that the constraint is real; only Kenny names it as a drawback worth fixing rather than a feature of the product

## Related

- [[overview]] — Cowork product positioning
- [[skills-to-plugins-pipeline]] — Kenny's cron plugin is itself a Cowork plugin
- [[../autonomous-loops-human-in-the-loop/_index]] — vault topic on the broader pattern
- [[external|Storm Bear: Setting up /loop + /schedule]] — vault docs on the alternative
