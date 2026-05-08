# cc-sdd — Beginner Analysis

> **Subject:** [`gotalab/cc-sdd`](https://github.com/gotalab/cc-sdd) — "Turn approved specs into long-running autonomous implementation. A minimal, adaptable SDD harness with Agent Skills for Claude Code, Codex, Cursor, Copilot, Windsurf, OpenCode, Gemini CLI, and Antigravity."
> **Wiki version:** v61
> **Build date:** 2026-05-07
> **Routine:** `llm-wiki-routine-v2.1` (Storm Bear vault)

---

## Phase 0 — Probe summary

### 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | T1 (Assistant — SDD harness for AI coding agents) |
| **Archetype** | solo-Japanese-author with ecosystem-portfolio (gotalab — 21 repos including skillport / uxaudit / claude-code-marimo) |
| **Scale tier** | small (3.3K stars / 241 forks / 429 commits / 16 open issues) |
| **Primary lang** | TypeScript 99.6% (npm-distributed CLI installer) |
| **Packaging tool** | npm (`npx cc-sdd@latest`) |
| **Origin story** | methodology-lineage (Kiro IDE → multi-agent harness) **CORPUS-FIRST KIRO LINEAGE** |
| **Methodology** | SDD (Spec-Driven Development) — **3rd independent SDD-centered framework in corpus** (after GSD v5 + spec-kit v17; OpenSpec v58 partial-overlap) |
| **Governance file count** | 4 (README + AGENTS.md + CLAUDE.md + CHANGELOG.md) |
| **Agent/skill count** | ~6 primary skills (kiro-discovery / kiro-spec-batch / kiro-impl / kiro-review / kiro-debug / kiro-verify-completion) + ~11 v2.x commands |
| **i18n coverage** | 13 languages (English + Japanese + Traditional Chinese + 10 more — Greek added v2.0.5) |
| **Intellectual influence cited** | Kiro IDE (AWS-affiliated, methodology lineage) + agentic SDLC + EARS requirements format |
| **Agent platforms supported** | **8 platforms** (Claude Code stable / Codex stable / Cursor beta / Copilot beta / Windsurf beta / OpenCode beta / Gemini CLI beta / Antigravity experimental) |

### Tier placement decision

**T1 (Assistant — SDD harness for AI coding agents).** Justified by:
- Subject IS a methodology-implementation framework, not a translator (T4) or service (T2)
- Direct sibling to spec-kit v17 (T1 official Microsoft SDD) and OpenSpec v58 (T1 pseudonymous-Fission-AI SDD)
- Multi-platform deployment is a distribution mechanism, not the core function
- Skills/commands ARE the product (`.kiro/` directory is the spec contract surface)

**Alternative considered:** T4 framing (bridge between Kiro IDE methodology and 8 multi-agent platforms). Rejected — bridge is the deployment, methodology is the substance. Same call as OpenSpec v58.

### Phase 4b primary routing mode

**🎯 PRIMARY: UN-STALE MECHANISM applied to Pattern #21 SDD Methodology Emergence**

Pattern #21 has been STALE-CANDIDATE since v25 audit (8 wikis past v17 spec-kit with no new SDD-centered framework). Promotion criterion: *"1+ more framework centering Spec-Driven Development, ideally at different tier."* Re-evaluation flagged for "v60+ wiki OR if independent SDD-centered framework emerges at T2-T5".

**cc-sdd v61 satisfies the un-stale criterion (independent author + independent org + independent intellectual lineage):**

| SDD framework | Tier | Org | Lineage | Wiki |
|---|---|---|---|---|
| GSD (get-shit-done) | T1 | gsd-build | feature-shaped SDD | v5 |
| spec-kit | T1 | GitHub/Microsoft (corporate) | corporate SDD constitution | v17 |
| OpenSpec | T1 | Fission-AI (pseudonymous-org) | per-tool format-translation SDD | v58 |
| **cc-sdd** | **T1** | **gotalab (solo-Japanese)** | **Kiro IDE → multi-platform Skills harness** | **v61** |

**4 independent SDD-centered frameworks across 4 distinct organizational archetypes** (solo-product-line + corporate + pseudonymous-org + solo-international). All T1 — but criterion phrasing says *"ideally at different tier"* (preference, not gate). Strong un-stale + N=4 cross-archetype evidence justifies recommending **promotion at next mini-audit** under criterion #2 structural-unambiguity-at-N=2 OR criterion #5 meta-pattern-at-N=3-consolidation if SDD methodology meta-pattern formulation chosen.

**Note on stale-flag history:** v60 mini-audit (2026-05-07) explicitly considered un-staling Pattern #21 via gsd-2 v54 → REJECTED for fact-verification reason (gsd-2 = same lineage as GSD v5; aidevops v47 verified NOT SDD-centered). cc-sdd is **structurally distinct** — neither successor nor variant of any prior SDD framework in corpus. The un-stale that v60 audit rejected on lineage grounds, v61 resolves on independence grounds.

### Secondary routing modes

- **Cross-corpus citation strengthening** — Pattern #57 57c forward-citation. cc-sdd CHANGELOG mentions Ralph Loop deprecation + Kiro IDE lineage; README compares to 8 agent platforms (not direct corpus citations but ecosystem peers)
- **Solo-international archetype extension** — corpus-first solo-Japanese T1 author (prior solo archetypes: solo-VN codymaster v12, solo-Korean OMC v27, solo-CN TrendRadar v19; **adds Japan as 4th solo-regional T1 archetype**)
- **Multi-platform skill distribution at 8 platforms** — strengthens Pattern #18 protocol-translation T4-archetype-correlated trend AND OpenSpec v58 30+ tools per-tool format translation (cc-sdd at 8 vs OpenSpec at 30+ — different scale, same mechanism)
- **Pattern #51 vibe-coding pole nuance** — cc-sdd is anti-vibe (favoring SDD discipline) BUT explicitly acknowledges vibe-coding's legitimate use cases ("/kiro-discovery can legitimately conclude that no specification is needed"). More nuanced than spec-kit v17's pure anti-vibe stance — counter-evidence-driven refinement candidate

### Phase 0.9 Storm Bear meta-entity check

**STRICT 1-of-4 inclusion check (post-v55 amendment):**

| Criterion | Result | Evidence |
|---|---|---|
| (a) Author archetype peer | **PASS** (borderline) | gotalab solo-Japanese "Agentic AI Engineer / Data Analyst" — solo-Asian-diaspora at established-but-still-individual scale (151 followers, 21 repos) — comparable to vault-publishing scenario |
| (b) Operational tool for vault | **PASS** (strong) | cc-sdd directly deployable for Storm Bear vault Claude Code projects via `npx cc-sdd@latest --claude-skills` — Skills mode IS Claude Code primary install target — works for vault Scrum-coaching software-build workflows |
| (c) Methodology-influence-node | **PASS** | SDD methodology directly cited by other corpus frameworks (spec-kit v17 + OpenSpec v58 + GSD v5); cc-sdd is 3rd-4th independent implementer of SDD methodology |
| (d) In-corpus reference | **PARTIAL** | cc-sdd README/docs do not directly cite spec-kit/OpenSpec/GSD by name — but ecosystem-peer (all SDD harnesses) at structural-citation level. Conservative count = FAIL strict-textual-citation. Liberal count = PASS structural-peer |

**Decision: 3-of-4 PASS** (conservative count: a/b/c pass with d partial = ≥1 PASS clean). **INCLUDE Storm Bear meta-entity** as 4th entity slot.

**Streak counter:** Storm Bear meta-entity streak post-v59 41-streak break and v60 RESTART at 1 → v61 advances to **2 (consecutive post-amendment-window)**.

**5-instance Phase 0.9 post-amendment window updates:** v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS / v61 PASS = **6-instance window 83% INCLUDE rate** validates STRICT amendment regularly satisfiable AND disciplined-skip works as designed (1 SKIP at v59 AutoGPT 0/4).

---

## Pattern Library implications (preview)

**Direct candidates / strengthenings (Phase 5 will register):**

1. **Pattern #21 SDD Methodology Emergence — UN-STALE → promotion-recommendation** (most-impactful audit decision); 4 independent SDD-centered T1 frameworks across 4 archetypes (corporate / pseudonymous / solo-Japanese / solo-product-line)
2. **Pattern #18 protocol-translation strengthening** — cc-sdd 8-platform Skills format translation extends v60 free-claude-code 6-provider API translation + v58 OpenSpec 30+ tools per-tool format translation; Layer 2 sub-archetype "agent-platform-format-translation-installer" candidate (cc-sdd N=1 first observation; promotion-eligible if 2nd observation appears)
3. **Pattern #51 Vibe-Coding spectrum NUANCE** — cc-sdd is anti-vibe-with-pragmatic-acknowledgment (counter-evidence narrowing scope); could refine pattern to acknowledge non-binary spectrum (anti-vibe-pure vs anti-vibe-pragmatic)
4. **Pattern #55 sub-archetype (solo-regional T1 archetype) strengthening** — Japan added as 4th regional archetype (after solo-CN TrendRadar v19, solo-Korean OMC v27, solo-VN codymaster v12); Pattern #55 was Korean-specific; consider promoting to solo-East-Asian-individual meta-archetype OR keeping per-region distinct
5. **Pattern #19 ecosystem-portfolio-first-mover** — gotalab has 4 pinned ecosystem-portfolio products (cc-sdd + skillport + uxaudit + claude-code-marimo) all in Claude Code / Agent Skills space; strengthens N=2 first-mover-authority-without-lineage observation from v60

**Counter-evidence / refinement candidates:**

- **Pattern #57 57c-anti-pattern-foil** — cc-sdd does NOT explicitly cite spec-kit/OpenSpec by name (CHANGELOG mentions deprecating Ralph Loop dependency, but no foil-style critique of corpus subjects). Falls in 57c-conservative-attribution if any indirect ecosystem reference exists; otherwise no contribution

**Cross-wiki standards check:**

- **OpenClaw runtime:** NOT mentioned (consistent with most corpus subjects)
- **Hermes runtime:** NOT mentioned
- **MCP:** NOT explicitly mentioned in ingested docs (skillport sibling product DOES support MCP per gotalab profile — adjacent to cc-sdd but not cc-sdd itself)
- **AGENTS.md:** YES, ships `AGENTS.md` (consistent with v55+ corpus convention; AGENTS.md content identical-style to CLAUDE.md per v60 #22c sub-variant pattern)

---

## Sources ingested (Phase 2 will write cluster summaries)

1. README.md (English) — multi-platform installer + Skills mode + workflow walkthrough
2. CLAUDE.md (project root) — agentic SDLC + 3-phase approval + steering/specs structure
3. AGENTS.md — cross-agent compatibility note + autonomy heuristic
4. CHANGELOG.md — v0.0.1 → v3.0.2 release history (major shifts: v2.0.0 template unification + v3.0.0 Skills mode primary)
5. docs/guides/spec-driven.md — SDD philosophy + 4-phase workflow + boundary-first design
6. docs/guides/why-cc-sdd.md — positioning / "right-sizing" + when NOT to use SDD
7. docs/guides/skill-reference.md — 6 primary skills (kiro-discovery / kiro-spec-batch / kiro-impl / kiro-review / kiro-debug / kiro-verify-completion)
8. docs/guides/command-reference.md — v2.x command set (~11 commands across steering / spec / validation / utility categories)

---

## Cross-wiki siblings (mandatory cross-references)

**Direct SDD methodology peers (T1):**
- [spec-kit v17](../spec-kit%20-%20Beginner%20Analysis/) — Microsoft official SDD with 9-article constitution + 80+ marketplace
- [OpenSpec v58](../OpenSpec%20-%20Beginner%20Analysis/) — Fission-AI pseudonymous-org SDD with 30+ tools per-tool format translation
- [get-shit-done (GSD) v5](../get-shit-done%20-%20Beginner%20Analysis/) — feature-shaped SDD predecessor
- [gsd-2 v54](../gsd-2%20-%20Beginner%20Analysis/) — GSD v5 successor (same gsd-build lineage)

**Adjacent T1 SDD-elements / methodology peers:**
- [BMAD-METHOD v11](../BMAD-METHOD%20-%20Beginner%20Analysis/) — BMM methodology (different from SDD but methodology-shaped peer)
- [aidevops v47](../aidevops%20-%20Beginner%20Analysis/) — verified NOT SDD-centered at v54 audit (good contrast)

**Multi-platform deployment peers:**
- [free-claude-code v60](../free-claude-code%20-%20Beginner%20Analysis/) — 6-provider API protocol translation (T4 archetype 9th)
- [n8n v56](../n8n%20-%20Beginner%20Analysis/) — 16-LLM multi-platform routing
- [mattpocock-skills v57](../mattpocock-skills%20-%20Beginner%20Analysis/) — Agent Skills builder for Claude Code

**Agent Skills ecosystem peers:**
- [awesome-claude-skills](../awesome-claude-skills%20-%20Beginner%20Analysis/) — Claude Skills directory
- [agent-skills-of-vercel](../agent-skills-of-vercel%20-%20Beginner%20Analysis/) — Vercel agent skills
- [oh-my-claudecode](../oh-my-claudecode%20-%20Beginner%20Analysis/) — Claude Code add-on collection

**Solo-regional T1 archetype peers:**
- [codymaster v12](../codymaster%20-%20Beginner%20Analysis/) — solo-VN T1 (Pattern #55 VN sub-archetype)
- [TrendRadar v19](../TrendRadar%20-%20Beginner%20Analysis/) — solo-CN multi-tier
- [oh-my-claudecode (OMC) v27](../oh-my-claudecode%20-%20Beginner%20Analysis/) — solo-Korean T1 (Pattern #55 Korean archetype)

---

## Build status

| Phase | Status |
|---|---|
| Phase 0 (probe) | ✅ COMPLETE |
| Phase 1 (scaffold) | ✅ COMPLETE |
| Phase 2 (sources) | ⏳ in progress (3 cluster summaries) |
| Phase 3 (entities) | pending (4 entity pages) |
| Phase 4a (beginner guide) | pending |
| Phase 4b (un-stale-mechanism deliverable) | pending |
| Phase 5 (iteration log + Pattern Library update) | pending |
| Phase 6 (vault sync) | pending |
