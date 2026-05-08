# Storm Bear vault pilot ranking — 2026-05-07 (post-v63 mini-audit)

> **Purpose:** Authoritative consolidated ranking of pilot candidates accumulated across 61 wikis. Replaces scattered pilot-ranking mentions in `_state/03a-projects-v48-v61.md` and project entity files.
> **Last updated:** 2026-05-07 session 71+ continuation (post-v63 EARLY mini-audit)
> **Maintained by:** Storm Bear vault operator + Claude routine v2.1 Phase 6 vault sync

---

## Operator-deployment imbalance (acknowledged)

Per GOALS.md reflections: **"7 ranked pilots accumulated but 0 deployed"** — pattern-observation > operator-deployment ratio is unhealthy. v63 audit Pattern #76 Adversarial Subagent Review Architecture + Pattern #74 EARS-Format Requirements + Pattern #75 External-IDE-Methodology Lineage Type all registered N=1 stale-flagged could resolve faster via pilot evidence than via wait-for-corpus-ship cadence.

**Decision principle:** Pick top-3 and execute within 2-3 weeks; re-evaluate ranking thereafter.

---

## Top-3 active pilots (immediate decision targets)

### #1 — cc-sdd v61 (HIGH-OPERATIONAL, methodology layer)

**Subject:** [`gotalab/cc-sdd`](https://github.com/gotalab/cc-sdd) — multi-platform SDD harness with Agent Skills mode for 8 AI coding agents (Claude Code stable + 7 others)

**Why pilot:**
- Direct deployable for Storm Bear vault Claude Code workflow via `npx cc-sdd@latest --claude-skills` (Claude Code is vault primary tool)
- SDD methodology fits dual role (software dev + Scrum coach) — 3-phase approval gates ↔ Scrum sprint review boundaries
- 13-language i18n (incl. Japanese) → vault potential VN i18n contribution opportunity
- Adversarial subagent review architecture provides quality discipline beyond ad-hoc Claude Code
- Pattern #76 verification opportunity — cc-sdd is N=1 baseline; pilot evidence informs future audit

**Pilot scope:**
1. Install `npx cc-sdd@latest --claude-skills` in 1 sandbox vault project (~1h)
2. Run `/kiro-discovery` + `/kiro-spec-init` for 1 small feature (e.g., "extract markdown links from vault notes")
3. Compare against ad-hoc Claude Code workflow on same feature
4. Measure (1 week):
   - Discipline-overhead vs value-add
   - Anti-vibe-pragmatism (does `/kiro-discovery` skip spec when appropriate?)
   - Adversarial review catch-rate (defects prevented vs naive Claude Code)
   - Token cost (autonomous mode subagent dispatch)
5. Document `04 Reviews/(C) 2026-05-XX cc-sdd pilot findings.md`

**Expected duration:** ~1h setup + 1 week measurement + ~1h write-up = ~3h spread

**Pattern Library payoff:**
- Pattern #74 EARS-Format Requirements vault-applicability evidence
- Pattern #76 Adversarial Subagent Review Architecture observability
- Pattern #21 SDD Methodology promotion-rationale validation
- Storm Bear meta-entity Phase 0.9 criterion (b) operational-deployability hard evidence (vs claim)

---

### #2 — free-claude-code v60 (HIGH-OPERATIONAL, proxy layer — orthogonal to cc-sdd)

**Subject:** [`Alishahryar1/free-claude-code`](https://github.com/Alishahryar1/free-claude-code) — Anthropic Messages API ↔ 6 upstream provider proxy

**Why pilot:**
- Cost-reduction proxy for active Claude Code workflow (vault primary tool)
- 4-plugin Claude-Code augmentation stack composability (claude-hud + claude-context + claude-howto + free-claude-code = zero-conflict orthogonal-layer composition)
- Pattern #18 Layer 2 api-protocol-translation-proxy verification opportunity
- T4 9th archetype operational deployment

**Pilot scope:**
1. Setup proxy server (~1h)
2. Configure 1-2 alternative providers (DeepSeek / Kimi / Qwen) as fallback
3. Use in daily vault work for 1 week
4. Measure:
   - Cost reduction % vs Anthropic native API
   - Latency overhead (ms added by proxy)
   - Quality degradation alternative providers vs Sonnet/Opus baseline
   - Provider failover behavior (when 1 provider down)
5. Document `04 Reviews/(C) 2026-05-XX free-claude-code pilot findings.md`

**Expected duration:** ~1h setup + 1 week measurement + ~1h write-up = ~3h spread

**Orthogonal to cc-sdd v61:** Different layer (proxy-runtime vs methodology-discipline). Both pilots viable simultaneously; results inform separate Pattern Library entries.

**Pattern Library payoff:**
- Pattern #18 Layer 2 api-protocol-translation-proxy operational evidence
- Cost-discipline insight for vault Claude Code workflow
- Pilot-deferral imbalance reduction

---

### #3 — n8n v56 (MEDIUM-HIGH OPERATIONAL, T2 platform layer)

**Subject:** [n8n.io](https://n8n.io) — workflow automation platform with bidirectional MCP

**Why pilot:**
- T2 platform with 16 native LLM providers + 11 vector stores + bidirectional MCP (MCP Client + MCP Server Trigger)
- Storm-Bear-as-MCP-server experimentation possible
- 5 concrete vault use cases articulated:
  - Sprint metrics aggregation (Jira/Linear → DORA dashboard)
  - Retro Q&A automation (Slack → Notion)
  - Standup digest multi-channel → email + Slack DM
  - GitHub PR triage with AI
  - Vault content as MCP server consumed by other agents
- License acceptable for internal-business-use under SUL clause

**Pilot scope:**
1. n8n.cloud signup OR self-host (~1-2h depending on path)
2. Build 1 simple workflow (e.g., "GitHub PR notification → Slack with AI summary")
3. Test bidirectional MCP (Storm-Bear-content → MCP server → external agent consumes)
4. Measure:
   - Workflow build velocity vs custom code
   - Multi-tool integration friction
   - Cost vs value
5. Document findings

**Expected duration:** ~2-3h setup + 1-2 weeks measurement + ~1-2h write-up = ~6-8h spread (heavier than #1 + #2)

**Pattern Library payoff:**
- Pattern #18 bidirectional MCP at T2 evidence
- T2 platform as Storm Bear infrastructure layer evaluation

---

## Tier-2 pilots (defer to v66+ window)

### #4 — claude-howto v32 (MEDIUM, self-onboarding)

VN-diaspora authored Claude Code self-onboarding tool. Lighter pilot — read + try without major setup.

### #5 — claude-context v40 (MEDIUM, code-context layer)

Code-context augmentation for Claude Code. Plugin-stackable with cc-sdd if both pilots succeed.

### #6 — claude-hud v35 (MEDIUM, runtime-display layer)

Runtime status display for Claude Code. Plugin-stackable with cc-sdd + claude-context.

### #7 — graphify v16 (LOW-MEDIUM, knowledge-graph builder)

Knowledge-graph builder for Markdown vaults. Direct vault-relevance but heavier setup.

---

## Tier-3 pilots (research-only / not recommended for execution)

- **AutoGPT v59** — pilot relevance MEDIUM-LOW pending license-acceptability decision (PolyForm-Shield non-compete affects vault commercial-use)
- **OpenSpec v58** — Fission-AI pseudonymous-org SDD framework; methodology-overlapping with cc-sdd; pilot one or other not both
- **spec-kit v17** — Microsoft SDD; methodology-overlapping with cc-sdd; corporate-governance overhead may not fit solo-vault scenario

---

## Execution roadmap (operator decision point)

### Recommended path A — Sequential pilots (lowest risk)

1. **Week 1:** Pilot #1 cc-sdd v61 (3h spread)
2. **Week 2:** Pilot #2 free-claude-code v60 (3h spread)
3. **Week 3:** Decision point — continue with Tier-2 OR ship v62 wiki OR routine v2.2 codification
4. **v66 audit (~3 wikis from v63):** Pattern #74 + Pattern #76 promotion deliberation with pilot evidence

**Total pilot time:** ~6h spread over 2-3 weeks

### Recommended path B — Parallel pilots (faster, higher cognitive load)

1. **Week 1:** Pilot #1 cc-sdd v61 + Pilot #2 free-claude-code v60 setup simultaneously (2h combined setup)
2. **Week 1-2:** Both running in parallel during normal vault work
3. **Week 2:** Write-up both (2h combined)
4. **Week 3:** v62 wiki OR routine v2.2 codification

**Total pilot time:** ~4h spread over 2 weeks

**Trade-off:** Parallel risks confounding observations (which pilot caused observed effect?); sequential isolates pilot-by-pilot but slower.

### Recommended path C — Sequential with v62 wiki interleaving

1. **Week 1:** Pilot #1 cc-sdd v61 setup + measurement starts
2. **Week 1-2:** Ship v62 wiki (60-125 min) during pilot measurement
3. **Week 2:** Pilot #1 write-up
4. **Week 3:** Pilot #2 free-claude-code v60 setup + measurement starts

**Trade-off:** Best for momentum (no pause); requires v62 subject availability.

---

## Decision-making prompts (for next session)

**Pick path A/B/C OR alternative:**
- A — Sequential pilots, 2-3 weeks
- B — Parallel pilots, 2 weeks (higher confound risk)
- C — Pilots + v62 wiki interleaved
- D — Skip pilots entirely; ship v62 wiki + v63 routine v2.2 codification (stays in pattern-observation mode)
- E — Other (operator specifies)

**Quick start sequence for Path A:**
```bash
# Pilot #1 cc-sdd v61 setup
cd ~/sandbox/cc-sdd-pilot
npx cc-sdd@latest --claude-skills
# Then in Claude Code:
/kiro-discovery "extract markdown links from vault notes"
```

---

## Update history

| Date | Update | Author |
|---|---|---|
| 2026-05-07 (post-v63 audit) | Initial consolidated pilot-ranking document; replaces scattered mentions in state files; cc-sdd v61 added as #1, free-claude-code v60 as #2, n8n v56 as #3 | Claude routine v2.1 Phase 6 housekeeping (operator-elected F3) |
