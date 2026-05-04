# claude-howto - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto) — **"A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value."**

**28,186 stars (#10 in corpus — between HF agents-course 27,995 v26 and awesome-design-md 60K v25; ~10,000 wiki corpus position), 3,445 forks (12.2% — higher than median), 124 watchers (subscribers), 30 open issues, MIT, Python (primary tooling lang for scripts/EPUB build), markdown-heavy content, main-branch, created 2025-11-07 (~5.5 months), pushed 2026-04-16.** Latest documented version: v2.1.112 (per README badge).

Owner: **Luong NGUYEN (luongnv89)** — Vietnamese-named engineer based in **Paris, France**. Bio: *"Software Engineer / AI, Cybersecurity / Learn, Build, Share and Connect"*. Company: **Montimage** (cybersecurity firm). Blog: luongnv.com. Medium: medium.com/@luongnv89. Twitter: @luongnv89. GitHub account since 2013-01-16. **116 public repos, 642 followers.** VN diaspora in France — distinct from VN-in-VN (codymaster/Tody Le v12 is HCMC-based).

**Companion repos under same owner (ecosystem-layer individual signal):**
- `claude-howto` (28,186 — this wiki)
- `asm` (214 stars, MIT, TypeScript) — *"The universal skill manager for AI coding agents"*
- `skills` (58 stars, MIT) — *"Supercharge your AI agents/bots with reusable skills"* (referenced in claude-howto "Additional Resources")
- `asm-registry` (0 stars) — *"the skill registry for asm"*
- `sleek-ui` (111 stars) — *"The Unsplash of design systems for AI agents"*
- `context-stats` (92 stars, MIT) — *"Understand how you use Claude Code, and spend less doing it"*
- `ccl` (11 stars, MIT) — *"Hit your limit? Need privacy? Just swap the model"*
- `music-cli` (61 stars, MIT) — *"A command-line music player for coders"*
- `better-shot` (BSD-3) — screenshot editor
- `vscode-markdown-preview` (15 stars, MIT) — Zed-inspired markdown preview
- `unsloth-mlx` (Apache-2.0) — *"Bringing the Unsloth experience to Mac users via Apple's MLX framework"* (CROSS-CORPUS reference to Unsloth v23)
- `vibe-coding` (6 stars) — *"A living repository for vibe coders"* (self-identifies with vibe-coding — Pattern #51 Vibe-Coding Spectrum data point)
- `textwiz-feedback` / `custats-feedback` — feedback repos for macOS menubar apps (commercial products hinted)

**Scope status: T1 Agent-as-assistant — 10TH T1 ENTRANT (largest tier in corpus) + 2ND VN-AUTHORED T1 IN CORPUS (after codymaster v12) + 1ST VN-DIASPORA-AUTHORED (France-based) + individual with ecosystem-layer companion-repo archetype.**

**Positioning:** *"Master Claude Code in a Weekend"* — structured learning path (11-13 hours full path, 15-minute onboarding) with 10 tutorial modules, visual Mermaid diagrams, copy-paste templates, interactive self-assessment quizzes. Anti-thesis to official Anthropic docs: *"The official docs describe features — but don't show you how to combine them."*

**Core product:**
- **10 tutorial modules** — Slash Commands / Memory / Skills / Subagents / MCP / Hooks / Plugins / Checkpoints / Advanced Features / CLI Reference
- **Module-numbered folder convention** (`01-slash-commands/` … `10-cli/`) — different sequence from beginner roadmap (modules ordered by alphabetical subject, roadmap ordered by learning difficulty)
- **Copy-paste templates** — slash commands (`optimize.md`, `pr.md`, `generate-api-docs.md`), CLAUDE.md variants (project/directory/personal), skills (`code-review/`, `brand-voice/`, `doc-generator/`), subagents (`code-reviewer.md`, `test-engineer.md`, `documentation-writer.md`, `secure-reviewer.md`, `implementation-agent.md`), MCP configs (`github-mcp.json`, `database-mcp.json`, `filesystem-mcp.json`, `multi-mcp.json`), hook scripts (`format-code.sh`, `pre-commit.sh`, `security-scan.sh`, `log-bash.sh`, `validate-prompt.sh`, `notify-team.sh`), plugins (`pr-review/`, `devops-automation/`, `documentation/`)
- **Mermaid diagrams** showing how each feature works internally
- **Interactive self-assessment** — `/self-assessment` and `/lesson-quiz [topic]` slash commands ship WITH the guide (quiz as tutorial mechanism — CORPUS-FIRST observation)
- **EPUB generation** — `uv run scripts/build_epub.py` creates offline ebook
- **4-language i18n** — English / Tiếng Việt (VN) / 中文 (Simplified Chinese) / Українська (Ukrainian) — novel combo (VN+CN+UK)
- **Claude Code 2.1+ compatibility** — synced with every Claude Code release; model-compatible with Sonnet 4.6 + Opus 4.7 + Haiku 4.5
- **25 hook events documented** — `PreToolUse / PostToolUse / PostToolUseFailure / PermissionRequest` + `SessionStart / SessionEnd / Stop / StopFailure / SubagentStart / SubagentStop` + `UserPromptSubmit / TaskCompleted / TaskCreated / TeammateIdle` + `ConfigChange / CwdChanged / FileChanged / PreCompact / PostCompact / WorktreeCreate / WorktreeRemove / Notification / InstructionsLoaded / Elicitation / ElicitationResult`
- **Testing infrastructure** — pytest + Ruff + Bandit + mypy + Codecov (unusual for a guide/tutorial repo; signals production-grade maintenance)
- **Medium blog integration** — references author's Medium blog posts for each module (first corpus framework with explicit Medium-blog pipeline)

**Intellectual lineage cited:** Boris Cherny's X/Twitter workflow post (*"The creator of Claude Code shares his systematized workflow"*) — Boris Cherny = Anthropic engineer, corpus-new person not previously cited. Also references Anthropic official docs + MCP protocol spec + author's own companion `skills` repo.

**Origin story (inferred):** Created 2025-11-07 — roughly 2 months after Claude Code's broader public rollout. Luong's personal pedagogical project growing to 28K stars in 5.5 months (~5,100 stars/month sustained; NOT extreme-velocity, but solidly Community-Viral Scale Path per Pattern #27).

**v2.1 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **T1 Agent-as-assistant (10th T1 entrant — largest tier extends further)** |
| **Archetype** | **Solo VN-diaspora-authored individual with ecosystem-layer companion-repo portfolio** — hybrid of Pattern #17 individual-led-dev variant + Pattern #20 solo-broad dictionary row + NEW **VN-diaspora** sub-variant (Pattern #55 Korean analog) |
| **Scale tier** | **Large (20-60K)** — 28K stars |
| **Primary lang** | Python (scripts/EPUB) + markdown (content) — content-primary |
| **Packaging** | Git clone + copy-paste (no npm/pip publish for main product) + optional `uv run scripts/build_epub.py` for offline ebook |
| **Origin story** | Individual-pedagogical-project + community-viral (Community-Viral Scale Path, Pattern #27) |
| **Methodology** | Pedagogical-tutorial (progressive learning path with quizzes) — feature-framework (similar to ECC v1) |
| **Governance file count** | **5-6 (heavy for T1)** — README + LICENSE + CONTRIBUTING.md + CODE_OF_CONDUCT.md + SECURITY.md + .github/TESTING.md (explicit) |
| **Agent/skill count** | **~10 modules + ~10 slash commands + ~5 subagents + ~4 MCP configs + ~6 hook scripts + 3 plugins + 3 CLAUDE.md variants = ~40 template files** (smaller than codymaster v12's 79 skills; comparable to ECC v1's ~30 pattern files) |
| **i18n** | **4 languages — EN + VN + CN-Simplified + Ukrainian** (novel combo; VN+UK unusual) |
| **Intellectual influence** | Boris Cherny (Anthropic) workflow post (CORPUS-FIRST Boris Cherny citation) + Anthropic docs + MCP spec + author's `skills` sibling repo |
| **Agent platforms** | Claude Code (SINGLE-PLATFORM focus — unlike gstack v3, codymaster v12's multi-platform) |

**Tier placement rationale:** T1 Agent-as-assistant — claude-howto IS a feature-framework + copy-paste template library for Claude Code specifically. Direct peer with ECC v1 (feature-pattern library), Superpowers v2 (methodology + skill library), gstack v3 (virtual-team-as-methodology), GSD v5 (SDD methodology), BMAD v11 (AI-agile methodology at scale), codymaster v12 (VN-authored solo assistant), spec-kit v17 (corporate SDD), agency-agents v18 (personality-driven agent library), OMC v27 (Korean multi-runtime orchestrator). 10th T1 entrant.

**Cross-wiki siblings (MANDATORY cross-references):**

Primary:
- **codymaster v12** (Tody Le, VN-in-VN T1) — **#1 sibling** — first VN-authored T1 in corpus; claude-howto = 2nd VN-authored; comparison essential for Pattern #55 analog / NEW VN-Regional-Archetype candidate
- **ECC v1** (affaan-m, feature-framework) — closest structural peer (copy-paste template library; modular organization)
- **Superpowers v2** (Jesse Vincent, methodology + skills) — secondary peer (skill library + workflow stages)
- **OMC v27** (Yeachan Heo, Korean multi-runtime) — Pattern #55 Korean Regional Archetype anchor; claude-howto = VN-Regional-Archetype analog

Secondary:
- **gstack v3** (Garry Tan virtual-team) — T1 6-way ancestor
- **GSD v5** (TÂCHES SDD) — methodology-lineage cousin
- **BMAD v11** (BMad LLC BMM) — methodology T1 at scale
- **spec-kit v17** (GitHub corporate) — T1 corporate peer
- **agency-agents v18** (Reddit-viral 82.9K) — T1 community-viral peer

Pattern-relevant:
- **awesome-mcp-servers v31** (Fiegel/Glama ecosystem-layer-with-commercial) — Pattern #17 peer
- **graphify v16** (safishamsi/penpax.ai) — Pattern #17 solo-brand ecosystem-layer peer
- **crawl4ai v29** (unclecode solo-enterprise at T4) — Pattern #20 dictionary peer (similar scale ~64K)

**v2.1 Phase 0.5 expanded pattern pre-check:**

1. **Overlap pre-check:** Would "VN-Regional-Archetype T1" overlap >70% with existing? Pattern #55 Korean covers Korean-specific; pattern says *"Distinct from US-authored and VN-authored (codymaster)"* — implicitly acknowledges VN-archetype exists but N=1 at v27. Now at N=2 (codymaster + claude-howto), candidate SHOULD register. Overlap with #55 is structural analog (same pattern family, different region). **Consolidation-forward consideration:** rather than register #70 VN-Regional-Archetype as standalone, propose **meta-pattern #70 Regional-Archetype-Registry T1** wrapping Korean (#55 N=1→observable-subset) + VN (N=2 codymaster + claude-howto) + implicit CN (TrendRadar v19 though T4, not T1) as sub-variants. However: Pattern #55 remains N=1; only VN hits N=2 at v32. **Decision: register VN-Regional-Archetype T1 as NEW #70 at N=2 (structurally-unambiguous-N=2 promotion-candidate), cross-reference to Pattern #55, propose meta-pattern consolidation at next audit when Korean reaches N=2.**

2. **Un-stale check:** Any stale candidates that claude-howto un-stales? Also revive-check for retired (#14, #16, #23, #25 retired at v27 audit)?
   - #21 SDD Methodology Emergence (STALE N=2 single-tier since v25) — claude-howto is NOT SDD-methodology; no un-stale
   - #45 Dual-Licensing / #46 Duo-Founder (STALE v29 audit) — single MIT, solo author; no un-stale
   - #52 Extreme-Viral-Velocity (STALE v31 mini-audit) — 28K/5.5mo = ~5K/mo = NOT extreme; no un-stale
   - **Revive checks (RETIRED patterns at v27 audit):**
     - #14 Alignment-Theory Visibility (RETIRED) — no alignment framing; no revive
     - #16 Skill Dependency Locking (RETIRED) — tutorial repo; no version-locked skill manifest; no revive
     - #23 AI-Disclosure Policy (RETIRED) — CONTRIBUTING.md lacks AI-disclosure despite being Claude-Code-focused; no revive (strengthens retirement rationale)
     - #25 Personality-Driven Agent Design (RETIRED) — 5 subagents are ROLE-based (code-reviewer, test-engineer, etc.); no revive

3. **Counter-evidence check:**
   - Pattern #17 5-variant table — does claude-howto fit existing variant or suggest new one? Luong's ecosystem portfolio (13+ companion repos) matches **variant 1 individual-led-dev** (Karpathy, hiyouga) with commercial-product hints (TextWiz, CUStats macOS menubar apps) suggesting variant-with-commercial-companion emergence. May strengthen Pattern #50 Commercial-Funnel (confirmed v31) with 3rd data point.
   - Pattern #24 SECURITY.md at T1 — claude-howto has SECURITY.md (per README "CODE_OF_CONDUCT.md + SECURITY.md") → 4th SECURITY.md T1 data point (after graphify v16 + spec-kit v17 + agency-agents v18). Strengthens.
   - Pattern #22 AGENTS.md — does claude-howto have AGENTS.md? README doesn't mention; check in Cluster 2. Likely absence (uses README + CLAUDE.md variants as primary governance).
   - Pattern #8 Research-Benchmark — claude-howto has self-assessment quizzes = NEW form of benchmarking (educational-assessment-quiz, distinct from research-benchmark + course-leaderboard). Potential 9th data point refinement or new candidate.

4. **Consolidation-forward discipline:**
   - VN-Regional-Archetype + Pattern #55 Korean → meta-pattern Regional-Archetype-Registry candidate: only 1 at N=2 so far; insufficient for meta-pattern consolidation yet
   - Interactive self-assessment → may be NEW Pattern #71 candidate (Interactive Self-Assessment as Tutorial Mechanism) — single-observation stale-risk-flagged at registration
   - Boris Cherny lineage → Pattern #19 archetype 1 strengthening (individual-author lineage); 6th touchpoint; NOT new candidate

**v2.1 Phase 0.6 candidate overlap pre-check:** See above. Proposed new candidates:
- **#70 VN-Regional-Archetype T1** (structurally-unambiguous-N=2 at registration; cross-refs #55 Korean analog)
- **#71 Interactive Self-Assessment as Tutorial Mechanism** (N=1 stale-risk-flagged; distinct from #8 Research-Benchmark + #53 Multi-Framework BYO)

Deferring (consolidation-forward):
- Boris Cherny as intellectual-influence node → strengthens Pattern #19 archetype 1, not new candidate
- SECURITY.md 4th data point → strengthens Pattern #24, not new candidate
- Luong ecosystem-portfolio → strengthens Pattern #17 variant 1 + Pattern #50 (potential 3rd data point)

**Phase 0.9 Storm Bear meta-entity applicability:** **YES** — claude-howto is a *pedagogical framework* (teaching Claude Code features + combinations). Storm Bear vault = operator's own Claude Code usage for Scrum coaching. Direct applicability: (1) operator is VN-diaspora-adjacent (developer in VN ecosystem); (2) tutorial modules map to Storm Bear agent development; (3) 4-language including VN makes VN-primary onboarding native; (4) self-assessment concept may apply to Storm Bear wiki-quality evaluation. Meta-entity warranted — **21st consecutive Storm Bear meta-entity** (routine v2.1 first execution feature).

**Phase 4b routing decision:** Primary mode = **T1 N-way extension with regional-archetype-N=2 validation** (extends T1 from N=9 to N=10 + establishes VN-Regional-Archetype N=2). Secondary mode = **cross-corpus solo-VN-authored peer comparison** (codymaster v12 direct comparison; VN-in-VN vs VN-in-diaspora sub-variant analysis). Deliverable: ~550-700 lines.

**Novel elements at v32 (corpus-firsts):**
1. **2nd VN-authored T1 framework** (after codymaster v12)
2. **1st VN-diaspora-authored framework** (Luong in Paris vs codymaster/Tody Le in HCMC)
3. **Boris Cherny first citation** in corpus (Claude Code creator workflow post)
4. **Interactive self-assessment slash commands** shipped with tutorial (`/self-assessment`, `/lesson-quiz [topic]`)
5. **EPUB offline ebook build** via `uv run scripts/build_epub.py` (first corpus offline ebook format)
6. **4-language i18n EN+VN+CN+Ukrainian** novel combo (Ukrainian unusual; ties 4-language tier but different subset)
7. **Mermaid-diagram-primary pedagogy** (visual-first explanation as PRIMARY teaching modality; quantitatively heavier diagram usage than prior corpus)
8. **Medium-blog-integrated learning pipeline** (10 blog posts authored by Luong linked from modules)
9. **Testing infrastructure for a TUTORIAL repo** (pytest + Ruff + Bandit + mypy + Codecov — treats content as code)
10. **Explicit version-synced-with-Claude-Code** badge (v2.1.112 = Claude Code release)
11. **25 hook event types documented** (most comprehensive hook event taxonomy in corpus)
12. **"Master Claude Code in a Weekend" framing** — weekend-length onboarding commitment (novel time-framing)
13. **Multi-CLAUDE.md variant pattern** — project/directory/personal CLAUDE.md distinct files (first corpus explicit 3-scope documentation)
14. **VN-diaspora author archetype** (Montimage Paris + VN name + EN-primary README but VN-README available) — 11th organizational archetype if registering

**Risk/ethical framing considerations:**
- **Low risk** — MIT + tutorial content + real named author with public identity + company affiliation + multi-language support
- **Minor supply-chain note:** subagent + skill + hook templates are copy-paste to user's `.claude/` — users should review before deploying (tutorial-genre standard caveat, not unusual)
- **No perverse incentive** — free forever + no commercial tier visible (Luong's commercial products are separate: TextWiz/CUStats/better-shot macOS apps)

**Phase 4b routing = T1 10-way extension + VN-Regional-Archetype N=2 validation deliverable.**

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.1.md` (**32nd auto-execution, 14th v2-era execution, FIRST v2.1-era execution**):

- **Ingest sources via WebFetch + curl** — README + VN README + CONTRIBUTING (to verify) + GitHub API + author profile + companion repos
- **Cross-reference với 31 sibling wikis** — primarily codymaster v12 (VN-authored peer) + ECC v1 (feature-framework structure) + Superpowers v2 (skill library) + OMC v27 (regional-archetype analog) + Pattern #55 Korean reference
- **Phase 4b = T1 10-way extension + VN-Regional-Archetype N=2 + ecosystem-layer individual + Boris Cherny lineage deliverable**
- **Beginner angle** — VN operator + developer + Scrum coach evaluating Claude Code onboarding path

**Prime directive:** Outcome = wiki + VN-Regional-Archetype N=2 candidate + Pattern #17/#20/#24/#50 strengthening + 2 new candidates (conservative) + fact-verification clean.

## Process — routine `llm-wiki-routine-v2.1.md`

7 phases. FIRST v2.1-era execution. Phase 4b = T1 10-way + VN-Regional-Archetype N=2 deliverable.

## Key People / Organization

- **Luong NGUYEN (luongnv89)** — Paris-based VN-diaspora engineer, Montimage cybersecurity firm, Medium blogger
- **Companion-repo portfolio:** asm / skills / sleek-ui / context-stats / ccl / music-cli / unsloth-mlx / vibe-coding + 108 other repos
- **Commercial products hinted:** TextWiz + CUStats macOS menubar apps (feedback repos public, products themselves closed-source)
- **Cross-project:** 31 sibling wikis. This is 32nd.

## Folder Structure

```
claude-howto - Beginner Analysis/
├── CLAUDE.md
├── 00 Sources/     01 Analysis/
├── 02 Wiki/        03 Published/
├── 04 Reviews/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 31 siblings MANDATORY** — especially codymaster v12 (VN peer direct comparison) + ECC v1 (feature-framework structural peer) + OMC v27 (Pattern #55 analog) + Pattern #17/#20 ecosystem-layer peers
- **Pattern Library direct update** — register VN-Regional-Archetype N=2 + Interactive Self-Assessment N=1-stale-flagged + strengthen Pattern #17/#19/#20/#24/#50 + check un-stale #23

## Current Status

> **Last updated:** 2026-04-22
> **Status:** ✅ **COMPLETE** — 32nd LLM Wiki, FIRST v2.1-era execution, T1 10-way extension, VN-Regional-Archetype N=2 candidate + Pattern #70 + #71 registered

### Expected milestones

- [x] Phase 0 Pre-flight (completed — 12-axis classified, overlap pre-checked, un-stale checked, counter-evidence flagged)
- [x] Phase 1 Scaffold
- [x] Phase 2 Source ingestion (3 clusters)
- [x] Phase 3 Entity pages (4)
- [x] Phase 4a Beginner published guide (~460 lines VN+EN bilingual)
- [x] Phase 4b **T1 10-way extension + VN-Regional-Archetype N=2 validation deliverable** (~700 lines)
- [x] Phase 5 Iteration log v32 + PATTERN_LIBRARY.md direct update (with fact-verification — caught #23 stale→retired labeling; fixed in 6 files)
- [x] Phase 6 Vault file updates (CLAUDE + GOALS + PATTERN_LIBRARY)
