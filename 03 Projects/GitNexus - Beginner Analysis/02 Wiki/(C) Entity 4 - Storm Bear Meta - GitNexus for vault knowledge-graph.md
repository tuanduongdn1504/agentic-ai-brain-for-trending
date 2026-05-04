# (C) Entity — Storm Bear Meta: GitNexus for Vault Knowledge-Graph

> **Category:** Storm Bear operator strategic meta-entity (22nd consecutive)
> **Tier:** Vault-level applicability
> **Wiki:** v33
> **Date:** 2026-04-23

---

## 1. One-line summary

GitNexus v33 represents the second direct-applicability knowledge-graph tool in the Storm Bear corpus (after graphify v16), offering browser-native + MCP-integrated vault indexing but gated by PolyForm Noncommercial license for commercial Scrum-coaching use — making this a pattern-observation asset + free-personal-exploration candidate, not a production-commercial tool.

## 2. Storm Bear vault structure (brief)

- **32 wiki projects** (pre-v33) → **33 with GitNexus**
- **Each wiki:** ~10 files across `00 Sources/ 01 Analysis/ 02 Wiki/ 03 Published/ 04 Reviews/`
- **Total files:** ~330 across corpus (under GitNexus 5K browser limit)
- **Cross-wiki references:** MANDATORY per routine — ~300+ inter-wiki links via `[[Wiki Name]]` syntax
- **Pattern Library:** 33 confirmed + 24 active candidates + 5 stale + 6 retired + 1 observation-track (v32 post-mini-audit state)
- **Vault = de facto large knowledge codebase** — wikis ≈ modules, entities ≈ functions, patterns ≈ interfaces

## 3. What would GitNexus extract from Storm Bear vault?

### Markdown parsing
- GitNexus is code-focused (tree-sitter 14 languages); Markdown is NOT in the 14
- **Direct use case BLOCKED:** GitNexus won't index vault markdown as code
- **Workaround:** convert Obsidian `[[Wiki Name]]` links to code-like imports (pre-processing) — effort-heavy

### Alternative: use MCP tools against a synthetic code representation
- Generate TypeScript "index.ts" files from vault structure
- Each wiki → TypeScript module with exports for entities and references
- GitNexus indexes these — provides MCP tools to query the derived graph

**Verdict:** NOT a direct fit for vault (markdown not code); workable with pre-processing.

## 4. What graphify v16 DOES that GitNexus v33 doesn't

**graphify v16 directly supports markdown-heavy vaults:**
- Graphify documentation says: *"any folder of code, docs, papers, images, or videos"*
- Obsidian markdown export = native-aligned output
- Python-local = no browser memory limit
- **Direct fit:** graphify for vault; GitNexus for pure-code repos

**Operator recommendation:**
- For Storm Bear vault knowledge-graph: **graphify v16** (correct tool)
- For codebases operator writes: **GitNexus v33** (browser or CLI, Claude Code integrated)
- For both: parallel pilots, different use cases

## 5. Storm Bear vault applicability matrix

| Use case | GitNexus fit | graphify fit | Notes |
|----------|--------------|--------------|-------|
| Index vault markdown → knowledge graph | ❌ (code-only) | ✅ (content-agnostic) | graphify's advantage |
| MCP query during Claude Code sessions | ⚠️ (pre-processing required) | ⚠️ (MCP server output supported) | Both could; graphify lower effort |
| Visualize cross-wiki links | ⚠️ (needs code-synthesis) | ✅ (native Obsidian export) | graphify wins |
| Index operator's codebase projects | ✅ (direct) | ✅ (direct) | Both work; tool preference |
| Browser-native quick demo | ✅ (gitnexus.vercel.app) | ❌ (pip local only) | GitNexus wins |
| Commercial Scrum consulting workflow | ⚠️ (PolyForm gate) | ✅ (MIT unrestricted) | graphify commercial-friendlier |

**Bottom line:** graphify v16 remains the operator's primary vault-indexing tool recommendation.

## 6. PolyForm Noncommercial commercial-gate analysis for operator

### Operator scenarios

| Scenario | Commercial? | PolyForm status |
|----------|-------------|-----------------|
| Personal vault exploration | No | ✅ Free |
| Self-directed Scrum learning | No | ✅ Free |
| Writing blog posts about GitNexus | No (content for public knowledge) | ✅ Free |
| Preparing for paid Scrum gig via vault research | ⚠️ Gray zone (research for commercial work) | ⚠️ Clarify |
| Using GitNexus during paid Scrum consulting session | ⚠️ Commercial use | ⚠️ Commercial license |
| Bundling GitNexus with Storm Bear commercial product | ⚠️ Commercial distribution | ⚠️ Commercial license |

**Gray zone recommendation:** email `founders@akonlabs.com` with use case if operator pursues any commercial scenario.

### Comparison with graphify v16 (MIT)
- graphify MIT = unrestricted commercial use + redistribution
- GitNexus PolyForm = commercial gate
- **For a Scrum consultant's toolbox:** graphify offers legal clarity; GitNexus requires per-engagement license thinking

## 7. Pattern observations relevant to Storm Bear operator

### Pattern #31 Open-Core (CONFIRMED v24, N=4 at v33)
- **Operator learning:** 4 viable open-core license strategies observed. If Storm Bear ever open-sources tooling with commercial-gate intent, 4 reference models exist.

### Pattern #72 PolyForm Noncommercial Commercial-Gate (NEW v33 candidate)
- **Operator learning:** standardized non-OSI license family exists and is emerging. Alternative to custom-written research licenses.

### Pattern #17 Ecosystem-Layer (CONFIRMED v15)
- **Operator learning:** Abhigyan single-flagship-project-with-commercial-entity variant. Different from ecosystem-portfolio variant (Luong v32, Karpathy, safishamsi).
- **Storm Bear applicability:** operator's Scrum coaching practice could follow single-flagship model (deep investment in 1 product + commercial entity) vs ecosystem-portfolio model.

### Pattern #27 Community-Viral Scale Path (CONFIRMED v21)
- **Operator learning:** 28.5K stars in 8.5 months = sustained-community-viral (~3.3K/mo). Achievable via: clear-problem-framing (nervous-system metaphor) + quality OSS + MCP-layer distribution + solving a real agent-context gap.

### Pattern #18 MCP Agent Runtime Standardization (CONFIRMED v15)
- **Operator learning:** MCP with 16 tools is high bar. Storm Bear tooling (if any) could expose MCP to Claude Code with fewer tools and still be useful.

## 8. Strategic framing for operator

### Option A: Free personal pilot
- Install GitNexus CLI, index local codebases operator is working on
- Observe MCP integration quality, compare with graphify
- No legal risk (personal use)

### Option B: Observational only
- Read wiki, don't install
- Extract pattern observations for vault
- Zero legal exposure

### Option C: Commercial-use evaluation
- Email `founders@akonlabs.com` with specific use case
- Get pricing for Scrum-consulting tier
- Compare with graphify alternative before commitment

### Option D: Build own (extract patterns, not tool)
- Use tree-sitter + NetworkX + MCP-server boilerplate to build Storm Bear specific knowledge-graph tool
- MIT-license own tooling
- Pattern #31 N=4 provides 4 commercial-strategy templates if monetization desired later

**Recommended starting point:** **Option B observational** + prepare for Option A free pilot if vault-indexing becomes operator priority.

## 9. Cross-wiki operator relevance

### T4 7-way comparison: which tool for which operator need?

| Need | Best fit | Notes |
|------|----------|-------|
| Vault knowledge graph (markdown-heavy) | **graphify v16** | MIT, Python-local, Obsidian-native |
| Personal codebase graph for Claude Code | **GitNexus v33** | Hooks, 16 MCP tools, browser-native |
| Google Workspace automation | **gws v13** | Apache, Google-backed, Rust |
| File → markdown for LLM ingestion | **markitdown v28** | MIT, Microsoft corporate |
| Web content scraping for LLM | **crawl4ai v29** | Apache-2.0, Python Playwright |
| CN news monitoring | **TrendRadar v19** | GPL-3.0, Python, 11 CN platforms |
| NotebookLM API access | **notebooklm-py v7** | MIT, Python, solo maintainer |

**Operator toolkit mix recommendation:**
- Primary: markitdown v28 + graphify v16 (document ingestion + vault graph; both MIT)
- Secondary: crawl4ai v29 (web research for client discovery)
- Evaluate: GitNexus v33 (personal codebase only; PolyForm gate for commercial)

## 10. Meta-entity reflection

### Storm Bear meta-entity pattern (22nd consecutive, per v2.1 Phase 0.9 applicability)

**Why meta-entity warranted at v33:**
- GitNexus is semantically a vault-adjacent tool (knowledge graph + MCP + browser-native)
- Direct comparison with graphify v16 which operator has already considered running on vault
- PolyForm license has operator-action implications (decision-tree for Scrum-consulting)
- Pattern #31 validates at N=4 across 4 orthogonal axes — corpus-level structural milestone

**Why meta-entity could have been skipped:**
- GitNexus is code-only (not direct vault fit)
- graphify v16 remains preferred vault tool
- PolyForm commercial-gate complicates operator adoption

**Decision:** include (22nd consecutive) — balanced pattern-observation value + operator decision-tree value justifies inclusion.

## 11. Pilot ranking update

Post-v33 Storm Bear operator pilot ranking (no changes for top tools; GitNexus enters low-priority):

| # | Tool | Wiki | Rationale |
|---|------|------|-----------|
| 1 | spec-kit | v17 | Methodology |
| 2 | OMC | v27 | Scrum-ceremony alignment |
| 3 | BMAD | v11 | VN methodology |
| 4 | markitdown | v28 | Direct Scrum-doc ingestion |
| 5 | crawl4ai | v29 | Web research utility |
| 6 | graphify | v16 | Vault knowledge graph (MIT) |
| 7 | gws | v13 | Google Workspace automation |
| 8 | codymaster | v12 | VN peer-category |
| 9 | multica | v15 | Team UX Linear-analog |
| 10 | agency-agents | v18 | 144-agent library |
| 11 | **GitNexus** | **v33** | **Code-only + PolyForm commercial-gate** |

**Verdict:** GitNexus is #11 (lowest-priority pilot) because:
- Markdown-vault not direct fit (graphify v16 better at #6)
- PolyForm commercial-gate friction
- Code-only focus limits Storm Bear vault applicability

**Pattern observation value HIGH (4th Pattern #31 data point, first PolyForm, 16 MCP tools), pilot value LOW.**

## 12. Strategic recommendation

### Near-term (next 1-2 sessions)
- **DEFER GitNexus pilot** — graphify v16 remains preferred vault tool
- **CONTINUE observation** — any future PolyForm-family adoption triggers Pattern #72 un-stale
- **EXTRACT patterns** — Pattern #31 N=4 license-strategy observations are operator learnings

### Mid-term (next 5 sessions)
- **ESCALATE v27 diagnostic HIGH bundle** — now deferred 9 sessions (v28/v29/v30/v31/v31-mini/v32/v32-mini/v33). BLOCKING-RECOMMENDATION per v2.1 operator-facing backlog discipline.
- **Monitor for 2nd PolyForm-family observation** — un-stale trigger for Pattern #72

### Long-term
- **If operator monetizes Storm Bear content:** Pattern #31 N=4 provides license-strategy templates (PolyForm Noncommercial being one of four)

## 13. Cross-wiki references

- [[graphify - Beginner Analysis]] v16 — preferred vault knowledge-graph tool (MIT); Karpathy /raw folder answer
- [[Everything Claude Code - Beginner Analysis]] v1 — feature-framework T1 for Claude Code workflows
- [[markitdown - Beginner Analysis]] v28 — document-ingestion for vault (MIT)
- [[crawl4ai - Beginner Analysis]] v29 — web-research utility (Apache)
- [[claude-howto - Beginner Analysis]] v32 — Claude Code tutorials (MIT)
- [[OpenHands - Beginner Analysis]] v30 — Pattern #31 N=3 data point (MIT + enterprise directory)
- [[fish-speech - Beginner Analysis]] v20 — Pattern #31 N=1 data point (custom research license)
- [[Skyvern - Beginner Analysis]] v24 — Pattern #31 N=2 data point (AGPL-3.0)

## 14. Pattern Library updates for Phase 5

- Register **#72 PolyForm Noncommercial Commercial-Gate License** (N=1 stale-risk-flagged)
- Strengthen **#31 Open-Core Commercial Entity** to N=4 (4 license strategies now observed)
- Strengthen **#17 Ecosystem-Layer Organizations** — 10th data point (single-flagship-with-commercial-entity variant); potential variant refinement at next audit
- Strengthen **#20 Solo-Scale Ceiling Dictionary** — NEW ROW: Solo-student-at-T4-with-commercial-company (28.5K/8.5mo)
- Strengthen **#27 Community-Viral Scale Path** — 10th data point (sustained-community-viral ~3.3K/mo)
- Strengthen **#18 MCP Agent Runtime Standardization** — largest per-project MCP exposure (16 tools)
- Note: Indian regional observation (Abhigyan Guwahati) — NOT registered as candidate (consolidation-forward: cross-tier premature; #55/#70 are T1-specific; observation kept in wiki narrative)

## 15. Meta-observations

- 22nd consecutive Storm Bear meta-entity (per v2.1 Phase 0.9 per-wiki applicability evaluation)
- First corpus wiki where meta-entity concludes with OPERATOR PILOT #11 (lowest) ranking — balanced honest framing + value acknowledgment
- Pattern #31 at N=4 + Pattern #72 registration = cleanest license-ecosystem observation since v20 fish-speech non-OSI introduction
