# (C) ai-token-monitor — Pattern Library Phase 4b (v158)

**Outcome: NO change to confirmed counts (46 patterns / 9 Library-vocab CONFIRMED). PRIMARY = 1 NEW section-C standalone (social-leaderboard layer). SECONDARY = T2 observability sub-archetype → N=5 / metering sub-flavor → N=4. §28: 1 new standalone (≤2); registry 06 ACTUALLY edited (rule-5).**

## PRIMARY — 1 NEW section-C standalone (N=1, CORPUS-FIRST)
**"Social/Competitive Leaderboard for AI-Coding Usage (shared-backend token-metering + dev-vs-dev comparison + chat)."**
- The corpus-first axis: a token/cost monitor that **inverts the local/private default** — it uploads usage to a **shared Postgres backend** (PLpgSQL in the stack confirms it) to power a **dev-vs-dev leaderboard** (daily/weekly/monthly), **chat** for leaderboard members, GitHub-style activity heatmaps, and monthly/yearly **recap cards** (top model, busiest day, streaks). Gamified, social, competitive — a "Strava for AI-coding usage."
- Distinct from: the **local/private metering tools** (v89 VibeCodingTracker, v109 cclog-cli, v157 ClaudeBar — all local, no social layer) and the **local-first privacy-conscious pets** (v154 agentpet, v155 openpets). No prior corpus subject shares usage to a backend for social comparison.
- **Honest privacy note:** this is a real trade-off (your usage leaves the machine for the social features) — recorded as the defining axis, not buried. The local token-tracking works without opting into the social layer.
- **Action:** filed to registry 06 §C, N=1, PROMOTION-ELIGIBLE at N=2; time-aware stale-watch (≥15 wikis AND ≥30 days). §28 cap: 1 of ≤2 new standalones used.

## SECONDARY — T2 "AI-Agent Observability/Metering Tool" sub-archetype → N=5 (metering sub-flavor → N=4)
- Sub-archetype members now (N=5): v89 VibeCodingTracker + v109 cclog-cli + v154 agentpet + v157 ClaudeBar + **v158 ai-token-monitor**.
- The **metering/usage/cost/quota sub-flavor** now N=4: v89 (usage+cost) + v109 (logs/metrics) + v157 (quota) + **v158 (token+cost)** — robustly PROMOTION-ELIGIBLE. (The ambient-pet sub-flavor stays N=3: v154/v155/v156 = the desktop-pet-surface standalone.)
- Tier-sub-archetype layer (state + audit queue). Recommend the audit CONFIRM the sub-archetype + formalize the two sub-flavors (metering N=4 vs ambient-pet N=3), and reconcile the ambient-pet/desktop-pet-standalone overlap (flagged at v157).

## Observations (NOT minted)
1. **Tauri-but-NOT-LV-C7** — ai-token-monitor is a Tauri v2 app, but it **observes** (monitors token usage); it does **not** control/manage the agent like the LV-C7 management-GUIs (v73 cc-switch / v117 CodexPlusPlus / v153 ai-switcher). Explicitly NOT counted toward LV-C7 (the observe-vs-control line; cf. v118 OpenHuman adjacent-not-counted, agentpet's "not LV-C7" note). Observation.
2. **JSONL-session-parsing-as-mechanism** — parses Claude Code / Codex / OpenCode session JSONL via file watchers = the v89 VibeCodingTracker log-parsing observability mechanism (Pattern #84 84c.1 "provider-agnostic via log-parsing at observability layer"). N+1 instance note.
3. **Pattern #84 cross-tool** — 3 providers (Claude Code / Codex / OpenCode). N+1 instance note.
4. **Webhook alerts** (Discord / Slack / Telegram) — a notification/out-of-band-signal sub-mechanism. Observation.
5. **Privacy-inversion** — shared backend vs the local-first prior monitors (v89/v109/v154/v155/v157). The defining contrast of the new standalone; also a #66-adjacent supply-chain/data-flow note. Observation.
6. **NOT a Pattern #52 claim** — 227★, creation date unstated → velocity/age unestablished; metrics not API-verified (§37.4).
7. **Niche-saturation meta-signal (now 6):** v153 ai-switcher + v154 agentpet + v155 openpets + v156 clawd-on-desk + v157 ClaudeBar + v158 ai-token-monitor = **6 consecutive "manage/monitor AI coding tools" ships, ZERO piloted.** This one is genuinely additive (the social-leaderboard mint + metering N=4) — but the audit is critically overdue with FIVE ripe promotion calls. Observation for the operator.

## §28 accounting
- New standalones filed: **1** (social/competitive leaderboard) — within the ≤2 cap.
- Sub-archetype strengthenings: **1** (T2 observability N=4 → N=5; metering sub-flavor → N=4).
- Registry 06 edited: **YES** (rule-5) — new §C standalone row added; §F running-log updated.
- Confirmed counts UNCHANGED: **46 patterns / 9 Library-vocab CONFIRMED.** Tracked PROVISIONAL surface ≈23 → ≈24 (+1 standalone). **Audit queue now carries FIVE ripe promotion calls:** LV-C7 Tauri-management-GUI N=3 (v153) · T2 observability sub-archetype N=5 / metering N=4 (v158) · ambient-pet sub-flavor N=3 = desktop-pet-surface standalone N=3 (v156) [reconcile overlap] · the social-leaderboard standalone N=1 (new, watch) · (plus the standing MCP-B1 review + 7-in-20 override review).
