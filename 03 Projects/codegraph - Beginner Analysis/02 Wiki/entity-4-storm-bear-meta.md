# Entity 4 — Storm Bear meta-entity (MODERATE INCLUDE 2/4)

> Phase 0.9 STRICT 2/4 PASS · Breaks v68 + v69 WEAK modal-streak · Pilot-candidate-relevant

## Phase 0.9 STRICT verdict — restated

**Verdict: 2/4 STRICT PASS = MODERATE INCLUDE**

| Criterion | Pass/Fail | Reasoning |
|----------|-----------|-----------|
| (a) Author archetype peer | ❌ **FAIL** | Colby McHenry is solo software-developer with 15+ years experience; NOT explicit Scrum-coach archetype. Storm Bear is dev + Scrum coach; conservative call is (a) requires both. |
| (b) Operational tool for Scrum-coaching | ✅ **PASS** | codegraph augments Claude Code (vault substrate) with pre-indexed code intelligence — vault-deployable for Storm Bear's vault maintenance + coding work (especially TypeScript-heavy hireui-harness). Similar framing to v66 agentmemory pilot-candidacy. |
| (c) Methodology-influence-node | ❌ **FAIL** | codegraph is tooling-influence, not methodology-influence; vault routine v2.x not shaped by codegraph approach. No methodology-citation chain. |
| (d) In-corpus sibling reference | ✅ **STRONG PASS** | README + CLAUDE.md cite **Claude Code (vault substrate) + Cursor + Codex (v62 corpus subject) + OpenCode (v67 corpus subject)** — 2 corpus subjects + Claude Code substrate. STRONGER (d) than v68 zero (1 sub-org + dep) and v69 CloakBrowser (2 corpus subjects). |

→ **MODERATE INCLUDE (2/4)** — breaks v68 + v69 WEAK modal-streak. Strength categorization continues to discriminate empirically.

## Streak observation

Post-v64-RESET window now 6 consecutive PASS with spectrum diversity restored:

| Wiki | Subject | Strength | STRICT PASS count |
|------|---------|----------|-------------------|
| v65 | claude-code-system-prompts | STRONGEST | 3/4 |
| v66 | agentmemory | STRONG | 4/4 |
| v67 | opencode-antigravity-auth | MODERATE | 2/4 |
| v68 | vercel-labs/zero | WEAK | 1/4 |
| v69 | CloakBrowser | WEAK | 1/4 |
| **v70** | **codegraph** | **MODERATE** | **2/4** |

**Spectrum distribution v65-v70:**
- STRONGEST: 1
- STRONG: 1
- MODERATE: 2 (v67 + v70)
- WEAK: 2 (v68 + v69)
- SKIP: 0

**WEAK is no longer modal at v70** — strength categorization continues to discriminate across distinct relevance levels. 14-instance Phase 0.9 post-amendment window v57-v70 = 12 PASS / 2 SKIP = **85.7% INCLUDE rate**.

## Storm Bear lessons codegraph teaches the vault operator

### Lesson 1: Pre-indexed-context-layer is corpus-novel + vault-relevant

codegraph's core insight — pre-index a codebase once + query the graph instead of re-exploring at runtime — applies directly to vault maintenance scenarios:

- **Vault code-bases:** hireui-harness, codeclaude experiments, etc. — codegraph pre-indexing would accelerate Claude Code exploration
- **Vault wiki corpus:** Markdown files (not codegraph's target language) — codegraph doesn't apply
- **Vault chapter files in `_state/` + `_patterns/`:** Plain text + markdown — not codegraph target

**Vault-deployable scope:** TypeScript codebases (hireui-harness primary). Narrow but real value-add for Claude Code coding work on those projects.

### Lesson 2: Quantitative-benchmark-marketing scales across product categories

codegraph leads with "94% fewer tool calls / 77% faster / 100% local." v69 CloakBrowser led with "0.9 reCAPTCHA / Pass Turnstile / 30+ sites." Different domains, similar marketing-positioning strategy.

**For Storm Bear's vault publishing:** When publishing vault tools/skills/observations, lead with quantitative claims if measurable. Numbers signal serious investment + invite verification (or falsification).

**Sister observation:** N=2 evidence for OC-M "Quantitative-Benchmark-Marketing" observational candidate (v69 CloakBrowser + v70 codegraph).

### Lesson 3: MCP-multi-platform is becoming corpus-default for T2 Service

agentmemory v66 (15+ platforms) + codegraph v70 (4 platforms) — both T2 Service MCP-multi-platform shape. When vault publishes future T2-shaped tooling, MCP-multi-platform-via-one-binary is the corpus-validated pattern.

**For Storm Bear's vault tooling:** If vault ships an agent-augmentation MCP server, expect to maintain per-platform config-target writes. Plan for the maintenance cost (codegraph's v0.7.7 → v0.7.8 same-day fix-cycle illustrates).

### Lesson 4: Synchronicity-discipline applies at multiple modes

codegraph's CLAUDE.md mandates 3-file MCP-tool-behavior sync (server-instructions.ts + instructions-template.ts + .cursor/rules/codegraph.mdc). v68 zero mandates behavioral-sync (examples + docs + tests + contracts).

**Two synchronicity modes:**
- **OC-E1 behavioral-synchronicity** (v68 zero) — code-behavior alignment across surfaces
- **OC-E2 configuration-synchronicity** (v70 codegraph) — config-file alignment across surfaces

Both are file-synchronicity-discipline but at different layers. For vault tooling, behavioral-sync matters when shipping examples + tests; config-sync matters when shipping per-platform configs.

### Lesson 5: Solo-individual passion-projects can reach corpus-scale

Colby McHenry is solo developer with 5K+ stars on codegraph in 4 months. Similar shape to corpus N=4 sub-archetype 19a (founder-personal lineage): rohitg00 / AgriciDaniel / unclecode / colbymchenry.

**For Storm Bear's pattern flywheel:** Solo-individual-multi-product-portfolio is a real corpus shape. The vault operator's Storm Bear identity fits this archetype potentially. Pattern #19 19a continues to strengthen at corpus level.

## Vault pilot candidacy assessment

codegraph is a **HIGH-relevance vault pilot candidate** comparable to v66 agentmemory:

| Axis | codegraph (v70) | agentmemory (v66) |
|------|-----------------|-------------------|
| Vault-deployable scope | TypeScript codebases (hireui-harness) | Vault as memory-substrate |
| Setup complexity | Low (`npx codegraph install --target=claude`) | Higher (MCP server setup + iii-engine deployment) |
| Value-add per session | Token savings (94% fewer tool calls) for coding work | Memory persistence across vault sessions |
| Risk profile | Low — read-only indexing; no vault state mutation | Medium — memory layer mutates state |
| Reversibility | High — `codegraph uninit` cleans up | Medium — depends on memory storage |

**codegraph appears LOWER-risk than agentmemory** for pilot deployment. Recommended sequence:
1. **codegraph pilot first** (lower setup cost; immediate token-savings; reversible)
2. **agentmemory pilot second** (higher value but higher risk; benefit from codegraph experience)

Both should be **fenced pilots** (scratch projects, not production vault) per v66 agentmemory recommendation framework.

## Phase 0.9 observation: (a) FAIL is the typical limiter

Across the post-v64-RESET window, (a) author-archetype-peer FAILS are the most common limiter. This is **vault-operator-specific**:

- Storm Bear is dev + Scrum coach
- Corpus subjects are mostly developer-only or developer-with-other-roles
- Few corpus subjects are explicitly Scrum-coach-also

**Routine v2.3 calibration consideration:** Should (a) be relaxed to "primary-author-role-overlap-with-vault-operator" rather than strict identity? Under relaxed (a), codegraph's Colby McHenry (developer) would PASS (a) — leading to v70 STRONG (3/4) verdict instead of MODERATE (2/4).

**v70 data point captured:** Current (a) interpretation discriminates correctly (developer-only ≠ peer-of-Storm-Bear-developer-coach). Calibration question remains open.

## Sister-subject comparison

| Wiki | Subject | Phase 0.9 | (d) source |
|------|---------|-----------|-----------|
| v67 | opencode-antigravity-auth | MODERATE 2/4 | (d) PASS via 2 corpus subjects (Opencode + Antigravity) + (b) PASS via "operational tool" framing |
| v68 | vercel-labs/zero | WEAK 1/4 | (d) PASS via v51 Vercel umbrella + @vercel/sandbox dep |
| v69 | CloakBrowser | WEAK 1/4 | (d) PASS via 2 corpus subjects (browser-use v34 + crawl4ai v29) + fork |
| **v70** | **codegraph** | **MODERATE 2/4** | **(d) STRONG PASS via 2 corpus subjects (Codex v62 + OpenCode v67) + Claude Code substrate citation + (b) PASS via vault-deployable framing** |

v70 has the STRONGEST (d) of the post-v64-RESET window — 2 corpus subjects + substrate citation + actual benchmark-testing against substrate codebase. Combined with (b) PASS for pilot-candidacy framing = MODERATE 2/4.

## What's NOT a Storm Bear lesson here

To maintain "NEVER fabricate" discipline:

- **NOT a vault-routine maintenance lesson** — codegraph doesn't shape routine v2.x evolution
- **NOT a Scrum-coaching methodology lesson** — the tool is purely technical
- **NOT a NEW Pattern Library Pattern** — codegraph's contribution is within-pattern strengthening (Pattern #18 sub-mechanism B N=3 at MCP variant)
- **NOT a corpus-archetype-defining subject** — solo-individual + T2 Service + MCP-multi-platform is corpus-typical at v70

These would over-extend the (b) + (d) PASS criteria. Storm Bear lessons stay anchored at the pre-indexed-context + MCP-multi-platform + synchronicity-discipline + pilot-candidacy levels where the criteria genuinely support them.
