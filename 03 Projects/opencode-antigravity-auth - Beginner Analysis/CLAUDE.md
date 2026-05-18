# opencode-antigravity-auth — Project CLAUDE.md

📍 **Status:** Active wiki build — **v67** (2026-05-18)
📍 **Routine:** `05 Skills/llm-wiki-routine-v2.2.md`
📍 **Subject:** [github.com/NoeFabris/opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)
📍 **NPM:** `opencode-antigravity-auth` (`@latest`, `@beta` channels)

---

## Phase 0 outputs (verified 2026-05-18)

### Subject classification (13-axis, v2.2 enhanced)

| Axis | Value |
|------|-------|
| **Tier** | **T4 Bridge** — auth bridge between Opencode (open-source agent runtime) and Google Antigravity (Google's IDE / Unified Gateway API) |
| **Archetype** | solo-community |
| **Scale tier** | medium (10.5K stars — middle of 5-20K band) |
| **Primary lang** | TypeScript 97.6% |
| **Packaging tool** | npm |
| **Origin story** | individual-author-lineage (NoeFabris) |
| **Methodology** | NONE — pure utility plugin |
| **Governance file count** | 4 (README + AGENTS.md + CHANGELOG + LICENSE) — medium |
| **Agent/skill count** | N/A (not an agent framework — a single plugin) |
| **i18n coverage** | EN-only |
| **Intellectual influence cited** | NONE (credits opencode-gemini-auth + CLIProxyAPI as predecessors, but no methodology lineage) |
| **Agent platforms supported** | 1 (Opencode) |
| **Living-Domain-Standards Tracking** | NO — tracks Antigravity's discovered API surface but does not aggregate multi-vendor standards |

### Velocity-screen + engagement-signal (v2.2 NEW)

| Metric | Value | Corpus context |
|--------|-------|---------------|
| Age (v1.0.0 → today) | **159 days** (2025-12-10 → 2026-05-18) | 5+ months |
| Stars | 10,500 | medium-scale |
| Forks | **1** | — |
| Watchers | 29 | — |
| Open issues | 30 | — |
| Commits | 691 | ~4.3 commits/day |
| Releases | 91 (v1.6.0 latest 2026-02-20) | ~18 releases/month |
| `stars_per_day` | **~66** | NOT EXTREME-VIRAL (Pattern #52 threshold is >300/day in <90 days) |
| `fork_ratio` (forks/stars) | **0.0001** | **🚨 CORPUS-RECORD LOW** — prior corpus-record was v65 claude-code-system-prompts at 0.178 (1,780× higher) |
| `watchers_ratio` (watchers/stars) | 0.0028 | very low — drive-by-stars-dominant signal |
| `open_issues_ratio` | 0.0029 | low |

**Velocity verdict:** Mature solo-utility plugin at medium scale; high author-velocity (91 releases / 5 months); **extreme drive-by-stars-dominant engagement** (community engagement ~100-1000× lower than typical corpus subject relative to stars).

### Pattern Library pre-check (Phase 0.5 expanded v2.2)

- **Pattern #83 Honest-Deficiency-Disclosure Discipline (CANDIDATE N=2 stale-risk-flagged at v66):** STRONG N=3 evidence. README opens with a `[!CAUTION]` Terms-of-Service Warning block: *"Using this plugin (and any proxy for Antigravity) violates Google's Terms of Service. A number of users have reported their Google accounts being **banned** or **shadow-banned**."* Plus 3-bullet acknowledgment-of-risk block ("Your account may be suspended or permanently banned. You assume all risks"). 100% honest disclosure of a deficiency competitors typically obscure. **→ Promotion-eligible at next audit (N=3 unlocks 3-subject criterion).**

- **Pattern #84 Cross-Vendor Ecosystem-Tolerance (CANDIDATE N=2 stale-risk-flagged at v66):** REFINEMENT evidence. Google does NOT challenge the repo itself (no DMCA / no enforcement action — sub-DMCA threshold maintained per criterion #2) BUT does enforce at user-account level (account bans/shadow-bans). Refines #84 to clarify vendor-tolerance has account-level enforcement as a release valve. **Not strengthening N→N+1; rather refines tolerance-mechanism scope.**

- **Pattern #18 Agent Runtime Standardization (CONFIRMED + shared-backend-service sub-archetype added at v66):** Possible N=2 evidence for the shared-backend-service sub-archetype. Plugin shares Google's Antigravity Unified Gateway as backend across multiple OAuth-authenticated Google accounts via rotation — the architectural inverse of v66 agentmemory's "one server, many platform-clients" (here: many accounts, one backend). Subtler than agentmemory; **flag for stale-check inclusion** rather than direct N=2 claim.

- **Pattern #85 Platform-Primitive Foundation (CANDIDATE N=1 stale-flagged at v66):** NOT N=2 evidence. opencode-antigravity-auth uses `@opencode-ai/plugin` interface but does NOT meet criteria (b)(c)(d): it does NOT self-identify as a running instance of Opencode, does NOT count internals in Opencode units, does NOT extend via Opencode's CLI for its own extensibility. It's an ordinary heavy-dependency plugin, not a Platform-Primitive Foundation.

- **NEW observational candidate (Phase 4b SECONDARY):** "Explicit-ToS-Violation Tool architecture" — framework whose CORE value proposition explicitly bypasses a vendor's ToS, foregrounded with `[!CAUTION]` blocks rather than buried. Distinct from gray-area scrapers / unofficial-API-wrappers by upfront acknowledgment + multi-account-rotation infrastructure built specifically to absorb predictable enforcement consequences (rate-limiting, shadow-bans).

- **NEW Library-vocabulary candidate item #11:** Engagement-Deficit-Extreme observational track — corpus-record fork_ratio (0.0001) flags a subject where star-vs-community-engagement gap is multi-orders-of-magnitude beyond corpus norm.

### Storm Bear meta-entity Phase 0.9 STRICT (decision pre-registered)

**Verdict: 2/4 STRICT PASS = MODERATE INCLUDE**

| Criterion | Pass/Fail | Reasoning |
|----------|-----------|-----------|
| (a) Author archetype peer | **PASS** | Solo-engineer (NoeFabris, @dopesalmon on X) at independent-developer scale comparable to vault operator |
| (b) Operational tool for Scrum-coaching | **FAIL** | TOS-violation risk + Opencode-not-Claude-Code + not Scrum-applicable. Vault would not deploy this for client work. |
| (c) Methodology-influence-node | **FAIL** | No methodology lineage cited (credits prior similar tools but not methodology-shaping authors) |
| (d) In-corpus sibling-product reference | **PASS** | Opencode is sibling-product to Claude Code (v65 corpus subject). v62 codex-plugin-cc bridges OpenAI Codex to Claude Code in same T4 Bridge archetype. opencode-antigravity-auth is the inverse direction (bridges Google Antigravity to Opencode). |

→ **MODERATE INCLUDE** as 4th entity. Storm Bear meta-entity included.

### Sibling detection

| Sibling | Relation | Why |
|---------|----------|-----|
| **v62 codex-plugin-cc** | **STRONG sibling** | Same T4 Bridge archetype, both single-author plugins bridging cross-vendor agentic-runtime ecosystems |
| v65 claude-code-system-prompts | weak sibling | Different archetype (corporate-org reverse-engineering archive vs solo-utility plugin), but both touch closed-vendor product surface |
| v66 agentmemory | weak sibling | Both solo-author npm plugins, but agentmemory is T2 Service on Platform-Primitive Foundation; opencode-antigravity-auth is T4 Bridge auth-plugin |

### Tier placement decision

**T4 Bridge** — confirmed. Plugin bridges:
- **Opencode** (open-source AI coding assistant; Anthropic Claude Code competitor) as host runtime
- **Google Antigravity** (Google's Unified Gateway API for Claude + Gemini + GPT-OSS access) as authentication target

Plugin intercepts `fetch()` calls to `generativelanguage.googleapis.com`, transforms them to Antigravity-API format, handles OAuth + quota + multi-account rotation. Not an agent framework, not a service primitive, not documentation — pure bridge.

### Phase 4b PRIMARY routing pre-registration

**PRIMARY:** Pattern #83 N=3 strengthening proposal (Honest-Deficiency-Disclosure — TOS violation warning is textbook evidence; promotes #83 to 3-subject criterion satisfaction).

**SECONDARY:**
- NEW observational candidate registration: "Explicit-ToS-Violation Tool architecture"
- NEW Library-vocabulary item #11: "Engagement-Deficit-Extreme corpus-record observational track" (fork_ratio 0.0001)
- Pattern #18 shared-backend sub-archetype: flag for v68 stale-check inclusion (not direct N=2 claim — different mechanism)
- Pattern #84 refinement: vendor-tolerance has account-level enforcement release valve

### Consolidation guard verified

Pre-build state (post-v66 agentmemory wiki 2026-05-14):
- 43 confirmed / 27 active / 0.628 ratio
- Ratio < 0.95 (mini-audit zone threshold) — **PROCEED normally**

---

## Cross-references

- **Routine:** [llm-wiki-routine-v2.2.md](../../05 Skills/llm-wiki-routine-v2.2.md)
- **Ingest methodology:** [llm-wiki-ingest.md](../../05 Skills/llm-wiki-ingest.md)
- **Pattern Library:** [PATTERN_LIBRARY.md](../../PATTERN_LIBRARY.md)
- **Strongest sibling:** [v62 codex-plugin-cc](../codex-plugin-cc - Beginner Analysis/CLAUDE.md)
- **Recent sibling:** [v66 agentmemory](../agentmemory - Beginner Analysis/CLAUDE.md)

---

## Phase status

- [x] Phase 0 — Pre-flight + probe complete
- [ ] Phase 1 — Scaffold (THIS COMMIT)
- [ ] Phase 2 — Source ingestion (3 clusters)
- [ ] Phase 3 — Entity pages (4 entities, Storm Bear meta included per MODERATE INCLUDE verdict)
- [ ] Phase 4a — Beginner bilingual guide (`03 Published/`)
- [ ] Phase 4b — Pattern #83 N=3 strengthening proposal (`01 Analysis/`)
- [ ] Phase 5 — Iteration log + Pattern Library updates
- [ ] Phase 6 — Vault sync (CLAUDE.md / GOALS.md / PATTERN_LIBRARY.md)

Next: Phase 2 source ingestion — 3 clusters.
