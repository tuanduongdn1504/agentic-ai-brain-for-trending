## Patterns đã verified work / Verified Patterns

> Patterns đã được prove qua real project — Claude phải ưu tiên dùng thay vì re-derive từ đầu.

### 1. LLM Wiki pattern (Karpathy) — ✅ proven 2026-04-17

**Verified trong project:** `03 Projects/Everything Claude Code - Beginner Analysis/`

Build persistent knowledge wiki cho topic phức tạp, LLM maintain tất cả cross-references. Pattern generalize cho mọi topic có ≥5 sources + ≥3 months lifespan + clear ownership.

**Skill reference:** `05 Skills/llm-wiki-ingest.md` — codified 13-section entity page format + workflow 5 phases.

**Evidence:** 18 files deliverable trong 1 session (14 wiki + 1 published + 2 contribution docs + 1 iteration log). Knowledge compounds, cross-references emerge naturally, contradictions surface qua verification.

**Khi dùng:** user có topic phức tạp muốn build knowledge base; hỏi "dùng LLM Wiki pattern không?" thay vì treat như note thường.

### 2. Brain-setup interview (5 rounds) — ✅ proven 2026-04-17

Generate CLAUDE.md qua structured interview. File root này được sinh ra bằng skill này.

**Skill reference:** `05 Skills/brain-setup.md`

### 3. New project scaffolding — ✅ proven 2026-04-17

Template duplication + 6-question interview → project folder với CLAUDE.md + COMMANDS.md + numbered folders.

**Skill reference:** `05 Skills/new-project.md`

### 4. LLM Wiki Routine (autonomous orchestration) — ✅ proven 2026-04-18, **v2 codified 2026-04-19**

**Verified trong 18 projects** (v1-v18), production-stable across **16 distinct Phase 4b routing modes**.

Routine pattern = orchestration meta-skill. User input = 1 source URL. Routine autonomous handles toàn bộ 7 phases (Pre-flight → Scaffold → Sources → Entities → Beginner Guide → Phase 4b deliverable → Iteration log → Vault updates) trong ~2h (velocity plateau 13 consecutive wikis v6-v18).

**Skill references:**
- **`05 Skills/llm-wiki-routine-v2.1.md`** — **ACTIVE** (consolidated 2026-04-22 from ~205 cumulative action items across v19-v31 + v29 full audit + v30 direct updates + v31 mini-audit)
- `05 Skills/llm-wiki-routine-v2.md` — v2 (superseded 2026-04-22, retained for history)
- `05 Skills/llm-wiki-routine.md` — v1 (superseded 2026-04-19, retained for history)

**Evidence:** Pattern proven 18× across 16 distinct Phase 4b routing modes. Shipped 18 wikis covering **5-tier taxonomy** (T1 Assistant N=8, T2 Service N=2, T3 Education N=1, T4 Bridge N=3, T5 Application N=3) + outside-scope. **Only T3 remains at N=1** for full 5/5 validation.

**v2 changes from v1:**
- 12-axis Phase 0 classification (archetype, lineage, methodology, governance, etc.)
- 16-mode Phase 4b routing (vs 3 in v1)
- Consolidation guard (blocks new wikis when candidate:confirmed > 2:1 or action-backlog > 100)
- Pattern Library integration (Phase 5 updates `PATTERN_LIBRARY.md` directly)
- Cross-wiki absence detection (presences AND absences as signal)
- External URL resolution (fetch referenced catalogs/guides)
- Branch fallback (main → master → v4 → dev on 404)
- Storm Bear meta-entity as routine feature (9+ consecutive wikis)
- New BLOCKED_CONSOLIDATION status

**v2.1 changes from v2 (2026-04-22):**
- **5 structural-promotion criteria** (up from 2): default ≥3-cross-tier / structural-N=2 / spectrum-N=2 / variant-within-pattern-N=2 / **meta-pattern-at-N=3-consolidation**
- **4 new Pattern Library mechanisms:** OBSERVATION-TRACK sub-category / absorption-retirement / un-stale mechanism / counter-evidence-driven refinement
- **Audit cadence reform:** mini-audit at 0.95:1 / full audit at 1.05:1 (replaces v2's >1:1 trigger)
- **Mini-audit protocol** codified as reusable routine (validated v31)
- **Pre-registration overlap pre-check** (>70% overlap → reject/consolidate)
- **Consolidation-forward registration discipline** (register meta-pattern not 3rd standalone)
- **N=1 stale-risk-flagging at registration**
- **Storm Bear meta-entity per-wiki evaluation** (not blanket obligation since v29)
- **Supply-chain awareness protocol** (Pattern #66 transitive trust-boundary framing)
- **Fact-verification protocol** (pre-Phase-6 numbered-pattern re-check; v31 lesson)
- **Operator-facing backlog discipline** (escalate deferred vault actions at 5+ sessions)
- **Stream-timeout resume protocol** (delegated builds can resume from partial completion; v31 validated)
- **Phase 4b routing modes expanded** from 16 to ~25 (added: tier-completion-milestone / counter-evidence-refinement / un-stale-mechanism / meta-pattern-consolidation / protocol-directory-meta-reference / etc.)
- **Ratio notation clarified:** ratio = active/confirmed; lower is healthier
- Velocity plateau preserved: 26 consecutive wikis at ~2h (v6-v31)

**Khi dùng:** User nói "LLM wiki cho <URL>" → invoke v2.1 routine, autonomous execute. Consolidation guard (with reformed cadence) runs first.

**Meta-insight:** Routines compound differently than skills. Skill = knowledge. Routine = execution automation. v2 is the product of 18 wikis × 102+ action items consolidated into operational protocol.

