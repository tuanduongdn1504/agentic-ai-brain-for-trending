# Storm Bear Vault — HIGH pilot + display-layer plugin genre implications

**Entity type:** Storm Bear meta-entity (24th consecutive, v10-v35)
**Subject:** What claude-hud means for Storm Bear operator's workflow, corpus taxonomy, and strategic decisions
**First documented:** 2026-04-23 (v35 wiki creation)

---

## 1. One-sentence definition

claude-hud is a **HIGH-priority, near-zero-friction pilot** for Storm Bear operator (immediate ROI in context-budget visibility during long wiki builds), and it introduces a **NEW T1 sub-classification observation** — display-layer plugin genre — distinct from the 11 prior broad-scope T1 entrants in corpus.

---

## 2. Why Storm Bear meta-entity applicability (Phase 0.9 evaluation)

Per v2.1 Phase 0.9 (per-wiki applicability evaluation, introduced v29):

**YES, include Storm Bear meta-entity.** Reasons:

1. **Immediate operator workflow relevance** — Storm Bear vault builds are Claude Code sessions. Context-budget visibility addresses a recurring Storm Bear operator pain (mid-build `/compact` surprises, unexpected /context exhaustion during long wiki phase executions).
2. **Pattern #18 reinforcement mechanism** — Storm Bear's Claude Code engagement strategy already depends on Claude Code's runtime standardization; statusline extension-point is a new consumption surface worth understanding.
3. **Zero-friction pilot candidate** — 3-command install + 5-minute try-out. Lower evaluation cost than any prior T1 pilot in corpus.
4. **24th consecutive Storm Bear meta-entity** — v10 Karpathy meta-peak established the pattern; v10-v35 = 26 consecutive wikis with meta-entity.
5. **Primitive-count flagging inaugural wiki** — Storm Bear process discipline itself is the story as much as the target.

---

## 3. Pilot recommendation: NEW RANK #1 or #2

### Pilot ranking at v35 (refreshed)

1. **claude-hud v35 🆕 — immediate utility** (5-minute install, immediate ROI for context-budget visibility)
2. spec-kit v17 — methodology for Scrum workflows
3. claude-howto v32 — self-onboarding meta-ROI
4. OMC v27 — multi-runtime orchestration
5. BMAD v11 — VN methodology at scale
6. OpenHands v30 — SWE-agent platform
7. markitdown v28 — Scrum doc ingestion utility
8. crawl4ai v29 — web research utility
9. claude-code-best-practice v34 — 82-tip vault CLAUDE.md refactor reference
10-14. gws / codymaster / multica / graphify / agency-agents

**Ranking rationale — claude-hud jumps to top:**
- **Install cost:** ~5 minutes (lowest in corpus)
- **Evaluation cost:** Immediate — first Claude Code session after install reveals value
- **Uninstall cost:** ~2 minutes if not valuable
- **Commitment:** None — purely observational plugin, doesn't reshape workflow

No other pilot candidate has this friction profile. spec-kit/claude-howto/OMC/BMAD all require hours-to-weeks of engagement to evaluate value. claude-hud is minutes-to-sessions.

---

## 4. Concrete Storm Bear use cases

### Use case 1: Context-budget visibility during long wiki builds

**Problem:** Storm Bear's typical LLM Wiki v35-style build (13 files, 2h target) involves 20-40+ tool invocations per Claude Code session. Context window fills unpredictably based on file sizes and WebFetch responses. Running out of context mid-Phase-4b causes mandatory `/compact` which loses detail.

**claude-hud solution:** Line 2 shows `Context █████░░░░░ 45%` continuously. Green/yellow/red threshold colorization (≤70 / 70-85 / >85) gives at-a-glance health awareness.

**Expected workflow change:** When yellow hits mid-phase, operator can proactively break phase to write interim output before /compact forces a reset.

### Use case 2: Subagent visibility

**Problem:** When Storm Bear operator invokes Task tool (subagents), no mid-flight visibility — only end-of-session Task output review.

**claude-hud solution:** `showAgents: true` → Line 4 shows `◐ explore [haiku]: Finding auth code (2m 15s)` during subagent runs. Model + description + elapsed time visible.

**Expected workflow change:** Operator can intervene if subagent stalls or drifts, rather than waiting for completion to realize.

### Use case 3: Tool invocation pattern observation

**Problem:** When observing Claude Code's own behavior for meta-purposes (e.g., evaluating Phase 2 efficiency), no real-time tool-call visibility.

**claude-hud solution:** `showTools: true` → Line 3 shows `◐ Edit: auth.ts | ✓ Read ×3 | ✓ Grep ×2`. Running + aggregated completed.

**Expected workflow change:** Operator sees tool-mix in real time (Read-heavy vs Edit-heavy phases).

### Use case 4: Todo progress tracking (if operator uses TodoWrite)

**Problem:** Todo-based multi-step work plans lose visibility without querying TodoWrite state.

**claude-hud solution:** `showTodos: true` → Line 5 shows `▸ Fix authentication bug (2/5)` — current in_progress + completion count.

**Expected workflow change:** Operator sees progress without asking.

### Use case 5: Session duration awareness

**Problem:** Storm Bear's 2h velocity plateau target requires rough time awareness. Terminal clock works but requires glance-away.

**claude-hud solution:** `showDuration: true` → appends `⏱️ 5m` to session info.

**Expected workflow change:** Minor; in-frame duration awareness without glance.

---

## 5. Install + 1-week evaluation protocol (recommended)

### Day 0 (5 min)

```
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/claude-hud:setup  (choose "Essential" preset)
```

Restart Claude Code.

### Days 1-3 (observation)

Default 2-line HUD. Observe:
- Does context bar color shift during actual workflows?
- Are the yellow-70% / red-85% thresholds right for Storm Bear's use?
- Does display feel ambient or distracting?

### Days 4-5 (optional lines)

Enable one at a time:
- Day 4: `showTools: true`
- Day 5: `showAgents: true`

Observe if they add value or noise.

### Day 6 (todos + duration)

- Enable `showTodos: true` if using TodoWrite workflows
- Enable `showDuration: true` for 2h-plateau tracking

### Day 7 (decision)

- **Keep** if net-positive signal-to-noise
- **Uninstall** via `/plugin uninstall claude-hud` if not valuable
- **Configure** final stable preset if keeping

---

## 6. Caveats for Storm Bear operator

1. **API-key mode may hide usage line** — per README, `rate_limits` stdin field only populated for subscriber accounts. If Storm Bear uses API-key-only mode, usage line won't appear. Check first.
2. **Bedrock/Vertex hide usage + cost** — per README, `Bedrock`/`Vertex` provider labels hide usage. If Storm Bear routes via AWS/GCP, usage line suppressed.
3. **Heavy governance overhead** — claude-hud has 7 governance files for a 3-month solo project. Not a risk but may indicate over-engineering. Not actionable for operator, but noted.
4. **Solo bus-factor** — if Jarrod goes dark, MIT + bounded scope = forkable, but depends on community takeover. Low risk for scope of claude-hud.
5. **3-month-old project** — still Unreleased v0.1.0 per package.json; CHANGELOG last released v0.0.12 April 4. Some config-surface churn recent. Check CHANGELOG before relying on specific config key.

---

## 7. Display-layer plugin genre — taxonomy implication for Storm Bear corpus

### Observation

claude-hud is the **1st display-layer plugin** in T1 corpus. Prior 11 T1 entrants are broad-scope:

| Wiki | T1 entrant | Scope breadth |
|------|-----------|---------------|
| v1 | ECC (affaan-m) | Feature framework (broad) |
| v2 | Superpowers (Jesse Vincent) | Methodology (broad) |
| v3 | gstack (Garry Tan) | Role-based (broad) |
| v5 | GSD (TÂCHES) | Methodology + context-engineering (broad) |
| v11 | BMAD (BMad Code LLC) | Full Agile methodology (broad) |
| v12 | codymaster (Tody Le) | Vibe framework (broad, 79 skills) |
| v17 | spec-kit (GitHub) | SDD methodology (broad) |
| v18 | agency-agents (msitarzewski) | 144-agent library (broad) |
| v27 | oh-my-claudecode (Yeachan Heo) | Multi-runtime orchestrator (broad) |
| v32 | claude-howto (Luong Nguyen) | Tutorial / how-to guide (broad) |
| v34 | claude-code-best-practice (Shayan Rais) | Best-practices aggregator (broad) |
| **v35** | **claude-hud (Jarrod Watts)** | **Narrow-utility display-layer plugin** |

### Proposed T1 scope-axis

**Broad methodology** ← Mid skill-library → **Narrow utility plugin**

- **Broad methodology:** Superpowers, BMAD, spec-kit, GSD (philosophy + workflow + roles)
- **Mid skill-library:** codymaster (79 skills), agency-agents (144 agents), OMC (19 agents + 15 skills), claude-howto (45 templates), claude-code-best-practice (82 tips)
- **Narrow utility plugin:** **claude-hud v35** (single-purpose: display statusline)

### Emergence hypothesis

Claude Code's native plugin marketplace primitive (v2.0+ era) may catalyze **narrow-utility display-layer T1 plugins** as a distinct sub-genre. Display-layer plugins compete on execution quality, not methodological breadth.

**Predictive claim:** If claude-hud's viral success is legible to ecosystem, expect 2-5 more narrow-utility display-layer plugins to emerge in next 6 months (notification plugins, command-palette plugins, progress-tracker plugins, etc.).

**Registration decision at v35:** N=1 observation. NOT registered as new candidate per consolidation-forward discipline. **If 2nd narrow-utility display-layer plugin reaches 5K+ stars within 6 months, consider registering as T1 sub-classification candidate.**

---

## 8. Corpus milestone flags

At v35 build:

- **35th LLM Wiki** — corpus milestone continues
- **4th v2.1-era routine execution** — v2.1 mechanisms (primitive-count flagging + consolidation-forward overlap rejection + fact-verification) all tested this build
- **30 consecutive wikis at ~2h velocity plateau** (v6-v35)
- **24th consecutive Storm Bear meta-entity** (v10-v35)
- **T1 extends to N=12** with NEW sub-classification observation (display-layer plugin genre)
- **Pattern #59 STRENGTHENS to N=2** (promotion-candidate at next mini-audit)
- **Primitive-count flagging inaugural use** — discipline added session 41, exercised first at v35

---

## 9. Strategic implications for Storm Bear v36+

### Short-term (next 1-2 wikis)

1. **Pilot claude-hud immediately** — 5-minute install + 1-week evaluation. Low cost, immediate signal.
2. **Address backlog** — v27 diagnostic HIGH bundle now deferred 12+ sessions (v28 / v29 / v30 / v31 / v31-mini / v32 / v32-mini / v33 / v34 / mini-audit-trigger-check / v35). **BLOCKING-RECOMMENDATION at v35.** Next session should execute this before new wikis.

### Mid-term (v36-v40)

1. **Watch for 2nd display-layer plugin T1** — if emerges, register sub-classification candidate.
2. **Watch for 2nd marketplace-only 59b variant** — claude-hud is current sole 59b; if OMC-style 59a remains dominant, 59b may be outlier not variant.
3. **Mini-audit trigger watch** — ratio 0.79:1 has 0.16 buffer to 0.95:1 mini-audit trigger. Current budget: ~2-3 new candidates before hit.

### Long-term (v40+)

1. **If claude-hud pilot successful** — Storm Bear operator becomes informed user of Claude Code plugin ecosystem. May surface additional plugin pilots.
2. **If display-layer plugin genre proliferates** — Storm Bear corpus may need T1 sub-taxonomy revision (scope-axis formalization).

---

## 10. Counter-evidence observation surfaced: Pattern #12

Pattern #12 (Governance-Depth Correlates with Organization) currently at *corporate → heavy governance, solo → light governance*. claude-hud is **counter-evidence** (solo-author + 3-month-old + 7 governance files).

**Possible explanations:**
1. Solo-with-professional-aspiration (author anticipates scale)
2. Anthropic-ecosystem-norm (CC community defaults toward heavier governance)
3. GitHub template-instantiation (unintentional governance-heavy bootstrap)

**Action at v35:** NOT refined. Observational only. Flag for N=2 watch. If 2nd solo-heavy-governance-at-early-age emerges, consider Pattern #12 multi-axial refinement (org × age × ecosystem-norm).

---

## 11. Open questions specific to Storm Bear meta

- Does Storm Bear operator's VN-diaspora / VN-Scrum-coach identity benefit from claude-hud's language-opt-in pattern (zh opt-in)? Probably yes — reinforces that default-EN + opt-in-others is a viable i18n strategy for Storm Bear's eventual public-facing content.
- Is claude-hud a template for a future "Storm Bear wiki-build HUD" showing Phase progress, current cluster, pattern-check status, etc.? Plausible but large effort.
- If Storm Bear vault publishes wiki-building tooling, would marketplace-native distribution (Pattern #59) be natural? Yes, but requires packaging as Claude Code plugin.

---

## 12. Action items from v35 for operator

1. **Install claude-hud and pilot 1 week** — high-priority, low-cost
2. **Execute v27 diagnostic HIGH bundle** — BLOCKING-RECOMMENDATION at v35 (12 sessions deferred)
3. **Mini-audit trigger watch** — ratio 0.79:1, buffer 0.16 to trigger
4. **Observe display-layer plugin emergence** — flag any 2nd data point in next 3 wikis
5. **Primitive-count check adoption confirmed** — v35 established template; future wikis should include section 13 in iteration logs

---

## 13. Provenance

- Storm Bear corpus history synthesized from root CLAUDE.md (v1-v34 state)
- Pilot ranking derived from comparative assessment of v1-v34 entrants
- Display-layer plugin genre proposal synthesized at v35 from scope-axis analysis
- Pattern #12 counter-evidence observation derived from governance cluster in v35 build

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 3 — 24th consecutive Storm Bear meta-entity.*
