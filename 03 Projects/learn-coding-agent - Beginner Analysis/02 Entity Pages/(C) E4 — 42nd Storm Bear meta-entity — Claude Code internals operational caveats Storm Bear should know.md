# E4 — 42nd consecutive Storm Bear meta-entity: Claude Code internals operational caveats Storm Bear should know

> **Type:** Storm Bear vault meta-entity (per-wiki applicability check: PASS)
> **Wiki #53**
> **Streak:** 42nd consecutive Storm Bear meta-entity (v10-v53)
> **Framing:** Operational awareness for Storm Bear's daily Claude Code use — NOT pilot-candidate (research-only license blocks commercial Scrum coaching re-use)

---

## Per-wiki applicability check (v2.1 Phase 0.9 mandatory)

**APPLICABLE.** Reasoning:

1. **Storm Bear vault uses Claude Code as primary harness** — every wiki, every analysis, every routine execution runs through Claude Code
2. **Subject of v53 IS Claude Code** — most direct possible operational relevance
3. **Findings include operational caveats** that materially affect Storm Bear's daily use:
   - Telemetry without UI-exposed opt-out (every Storm Bear session sends env fingerprint + repo-URL hash + tool inputs to Anthropic + Datadog)
   - Undercover-mode (if Storm Bear operator were Anthropic employee, would auto-strip AI attribution; not applicable to Storm Bear but informational)
   - Remote killswitches (hourly polling can disable Claude Code features mid-session without user consent)
   - GrowthBook A/B assignment without explicit consent (Storm Bear sessions may receive different prompts/behaviors than baseline based on opaque experiment groups)
4. **Sister-archive to v21 system-prompts-leaks** which had Storm Bear meta-entity at outside-scope tier; consistent treatment
5. **Caveat**: Research-only license blocks commercial Scrum coaching re-use; Storm Bear can READ + LEARN + REFERENCE under fair-use research framing but cannot REPACKAGE for client deliverables

→ Meta-entity warranted. 42nd consecutive (v10-v53) = streak preserved.

---

## Operational caveats Storm Bear operator should know

### Caveat 1: Telemetry has no UI-exposed opt-out for direct API users

**Per Sanbu's analysis of Claude Code v2.1.88:**
- Direct Anthropic API users (Storm Bear's mode) cannot disable 1P telemetry via settings
- Every event sends: env fingerprint, process metrics, model in use, session ID, user ID, device ID, **SHA256-first-16-char repo-URL hash**, agent type, team name, parent session ID
- Tool inputs are truncated by default (512 chars strings / 4096 JSON / 20 array items / 2 levels nesting) but `OTEL_LOG_TOOL_DETAILS=1` env enables full capture

**For Storm Bear:**
- Anthropic has hashed-fingerprint of every git remote Storm Bear vault has been associated with (server-side correlation possible)
- Tool inputs Storm Bear passes to Claude Code are partly captured in telemetry (truncated)
- Per-event metadata is comprehensive enough for Anthropic to reconstruct Storm Bear's usage patterns
- Failed events are persisted to `~/.claude/telemetry/` for retry → check this directory periodically; understand what's pending
- **Operator action**: Run `ls ~/.claude/telemetry/` periodically; understand telemetry-disk-state; if privacy-critical session, check for opt-out env vars (third-party cloud providers Bedrock/Vertex disable; not applicable to direct API)

**Verification status**: All claims unverified by Anthropic; sample-verify before relying on specifics.

### Caveat 2: Remote killswitches can disable features mid-session

**Per Sanbu:**
- `GET /api/claude_code/settings` polled every 1 hour
- "Dangerous" remote-settings changes show blocking dialog → reject = `gracefulShutdownSync(1)` exits app
- 6+ killswitches can disable: bypass permissions, auto mode, fast mode, analytics sink, agent teams, voice mode

**For Storm Bear:**
- Long-running Storm Bear sessions (>1h) may receive remote-settings updates mid-work
- If Anthropic decides to disable a feature Storm Bear depends on (e.g., bypass permissions for vault-batch-edit operations), Storm Bear has no override
- If the dialog appears with dangerous-changes flag and Storm Bear rejects, Claude Code exits — work-in-progress may be lost
- **Operator action**: Save vault state frequently; commit mid-task; treat Claude Code as exit-able mid-session; do not assume hour-long uninterrupted state

### Caveat 3: GrowthBook A/B assignment without consent

**Per Sanbu:**
- Users assigned to experiment groups via GrowthBook without explicit consent
- Attributes sent: id / sessionId / deviceID / platform / organizationUUID / subscriptionType
- Internal `tengu_ant_model_override` flag can change model + effort + system prompt + custom aliases for ant-only users (different infrastructure, but illustrates capability)

**For Storm Bear:**
- Storm Bear sessions may behave differently across days/weeks based on opaque GrowthBook assignment
- Inconsistencies in Claude Code behavior may not be Storm Bear's bugs but A/B-group differences
- **Operator action**: When debugging Claude Code behavior anomalies, factor in possibility of A/B-group difference; cross-check against community reports; do not assume consistent baseline

### Caveat 4: Internal vs external user prompt asymmetry

**Per Sanbu (Pattern #2 in 02-hidden-features-and-codenames.md):**
- Anthropic employees (`USER_TYPE === 'ant'`) get materially better prompts:
  - "Err on side of more explanation" vs external "Be extra concise"
  - Required verification agent for non-trivial changes
  - Anti-over-comment dedicated prompts
  - Numeric anchors ("≤25 words between tools, ≤100 words final")
  - Capybara-v8 false-claims-mitigation patches
  - Internal-only tools (`REPLTool`, `TungstenTool`, `VerifyPlanExecutionTool`, agent-nesting)

**For Storm Bear:**
- Storm Bear (external user) gets a strictly-inferior product per Sanbu's analysis
- "Be extra concise" external-mode may explain truncated explanations Storm Bear sometimes sees
- False-claims rate is ~29-30% on Capybara v8 for external users vs Anthropic-internal who has dedicated mitigation patches → **explicitly verify Claude Code outputs** when claims are operationally critical
- Storm Bear cannot access internal-only tools
- **Operator action**: Do not assume Claude Code outputs are gold-standard; verify-before-act for important operational decisions; this aligns with vault rules (NEVER fabricate / NEVER silent-assume)

### Caveat 5: Numbat / KAIROS / voice mode roadmap

**Per Sanbu:**
- Next model: Numbat (codename confirmed via `@[MODEL LAUNCH]` markers in source)
- KAIROS: autonomous-agent mode with `<tick>` heartbeats, `SleepTool`, `PushNotificationTool`, `SubscribePRTool`, terminal-focus-aware behavior
- Voice mode: push-to-talk fully implemented but feature-flag-gated
- 17 unreleased tools waiting in source

**For Storm Bear:**
- Plan for upcoming model migration (Numbat may arrive within months); Pattern #18 vault refactor implications
- KAIROS would change Storm Bear's interaction model (autonomous + push-notification driven vs reactive + user-driven); evaluate fit when launched
- Voice mode is OAuth-only (no API key support per Sanbu); Storm Bear API-key mode wouldn't enable
- **Operator action**: Track Claude Code release notes for model migrations; do not let Pattern #18 infrastructure drift outpace vault integration

### Caveat 6: Repository fingerprinting via SHA256-first-16-char

**Per Sanbu:**
- Every event carries `repository remote URL hash (SHA256, first 16 chars)`
- Server-side correlation across users/sessions/devices possible

**For Storm Bear:**
- Every Claude Code session in a git-tracked directory (Storm Bear vault is git-tracked) sends a fingerprint of the git remote URL to Anthropic
- If Storm Bear vault git remote ever changes (renames, account moves, fork), correlation may persist or break depending on hash-of-new-URL
- Multiple operators on same vault would share the same repo-URL-hash → cross-operator correlation
- **Operator action**: Aware that Anthropic has telemetry-fingerprint of Storm Bear vault git remote; this is unavoidable for direct API users

---

## What this v53 wiki adds to Storm Bear's vault

### Direct utility (HIGH for operational awareness; LOW for content re-use)

- **Operational caveats** (above 6) directly inform Storm Bear daily Claude Code use
- **Architecture reference** (12 progressive harness mechanisms / 11 design patterns / src/ tree / data flow / permission system / sub-agent + swarm / context management / MCP integration / bridge / session persistence) is excellent Claude Code internals reference for building competing harnesses or understanding edge cases
- **Roadmap signals** (Numbat / KAIROS / voice / 17 unreleased tools) inform vault Pattern #18 evolution planning

### Indirect utility (HIGH for pattern discovery)

- **Pattern #38 38b NEW sub-variant** (single-tool-internals-deep-dive) — corpus structural insight
- **Pattern #29 29-absent-4 NEW sub-context** (research-only-non-commercial-restriction) — license-diversity formalization
- **Pattern #75 N=2 with mechanism-divergence caveat** — fork-amplification observational pattern
- **17-consecutive-wiki zero-registration streak NEW LONGEST in corpus** — discipline milestone
- **CORPUS-RECORD 168.2% fork inversion** — structural observation

### NOT a Storm Bear pilot candidate

- Research-only license blocks commercial Scrum coaching content re-use
- Static archive (abandoned 2026-04-01) — no maintenance path
- Subject IS Claude Code (not a tool to integrate; an analysis OF Storm Bear's existing tool)
- Storm Bear is already on Claude Code; no migration target
- Pilot ranking unaffected (top-11 unchanged from post-v52)

---

## Cross-references

- E1 — Core archive (5-doc content + roadmap)
- E2 — Pattern implications (#38 38b N=2 / #29 29-absent-4 / #75 N=2)
- E3 — Sanbu / sanbuphy.cn ecosystem + abandoned-day-2 mystery
- C2 — Full 5-doc content with verbatim quotes
- C3 — Author profile + research-only license + abandoned status
- 03 Beginner Guide — Bilingual VN+EN with operational caveats prominent
- 04 Phase 4b Deliverable — Comprehensive pattern + sister-archive comparison
- v21 system-prompts-leaks (sister-archive parent of Pattern #38)

---

## Cumulative Storm Bear meta-entity streak

**42 consecutive wikis** (v10 Karpathy ↔ v53 learn-coding-agent).

Pattern: every wiki since v10 has had a Storm Bear meta-entity per per-wiki-applicability check (v2.1 Phase 0.9). All 42 have passed the check, validating routine v2.1's per-wiki-evaluation discipline. **No false-positive applicability skips observed in 42 consecutive wikis.**
