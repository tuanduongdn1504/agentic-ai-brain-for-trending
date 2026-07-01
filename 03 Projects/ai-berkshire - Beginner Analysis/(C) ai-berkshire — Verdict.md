# (C) ai-berkshire — Routine Verdict (v187)

> LLM Wiki Routine **v2.6**. Verdict produced **INLINE + hand-verified** per `feedback_wiki_verify_independently_check_collisions`. Source-reading + upstream research delegated to **3 read-only agents** (safe/factual: repo mechanics, the four-masters upstream philosophy, the repo's own knowledge docs — ~161K subagent-tokens total); **all corpus-fact / collision / identity claims verified BY HAND** (grep over `_state/` + `_patterns/` + `03 Projects/` + WebFetch of the repo page). Clone source-verified at commit `0222260`.

## Subject

`xbtlin/ai-berkshire` — *"AI 时代的伯克希尔: 基于 Claude Code / Codex 的价值投资研究框架"* / *"Value Investing Research Framework for the AI Era."* A **domain-vertical (value-investing) agent-skill collection** for Claude Code + Codex: 18 skills + 8 Python tools + a 3-layer (Skill/Agent/Tool) architecture systematizing four investing masters (Buffett / Munger / Duan Yongping / Li Lu). MIT; 7.7k★/973 forks/1 release (page-stated §37.4). Author `xbtlin` = a bare handle (individual Chinese value-investor/creator).

## Verdict: **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts UNCHANGED **46/11**

| Axis | Call | Basis |
|---|---|---|
| **(a) Storm-Bear-connection** | **FAIL** (clean) | `xbtlin` = bare handle, not Anthropic ((a)-7 is Anthropic-only). A Chinese-name/heritage inference is NOT an (a)-rescue (v159→v186 discipline); the English `README_EN.md` (product-locale-inclusion) is NOT relied upon per the strict rule. First `xbtlin` author → a **#19 19a** data-point. Matches the v168/v172/v173 bare-handle FAILs. |
| **(b) Goal-relevance (keys the tier)** | **STRONG** (on the agent-engineering substrate; ⚠️ MODERATE on the domain — operator-reviewable) | It **is** a Claude-Code-first (+Codex) **domain-vertical skill collection** — the exact agent substrate the vault studies — and an unusually rich exemplar of **persona-differentiated parallel multi-agent orchestration + cross-harness skill distribution + deterministic-tool-offload + a verification/exit gate + forced-verdict discipline**, all of which land on your live **multi-agent-orchestration** + **CC-memory-systems** + **agent-skills** pilot threads and are directly portable to software / hireui. **STRONG-not-STRONGEST** because: third-party; a persona-prompt collection; and its *domain* is value investing, **not** software development (the specific Goal-#1 target). The **domain-weighted (b) MODERATE** reading is defensible and recorded operator-reviewable — but either way GOAL-ALIGNED under §31, and the precedent is clear: the Domain-Vertical-Skill-Collection instances (SEO v64, academic v90, cybersecurity v98) were all goal-aligned INCLUDEs *as skill-collection exemplars regardless of vertical*. |
| **(c) Engineering substance** | **STRONG** | 18 skills × cross-harness (canonical `skills/*.md` → generated Codex skills + prompts via sync scripts, `--check` drift mode) + 8 zero-dep Python tools (exact-decimal `financial_rigor.py` w/ Benford; `report_audit.py` 15%-sample publish gate w/ CI exit code; screener/backtest/scrapers) + real multi-agent parallel orchestration (`TeamCreate`/`Task` `run_in_background`) + ~100+ real reports + documented anti-bias principles. **Caveat:** the *hard* investing knowledge is the four masters' philosophy (packaged, not invented); the returns are unverified; some tools are thin scrapers; README sample outputs are self-admittedly illustrative. |
| **(d) Corpus fit** | **STRONG** | financial-services **v141** (finance-domain neighbor) · skill-collection genre (karpathy v63 / mattpocock v57 / CodexKit v121 / claude-seo v64 / agent-skills v184) · multi-persona subagent library (agency-agents v185) · 4-review-personas + doubt-driven-dev (agent-skills v184) · #84 84c cross-harness · #12 routing artifacts · the T1 Domain-Vertical-Skill-Collection sub-archetype itself. |

## Pattern outcome: **NO MINT** — instance-strengthening of a CONFIRMED sub-archetype

**Instance-strengthening of the CONFIRMED T1 `Domain-Vertical-Skill-Collection` sub-archetype** (promoted at v101; defn: *"T1 subjects that codify a complete domain-vertical via N-skill collection at single-repo scope, with per-skill metadata + a cross-skill routing artifact"*). ai-berkshire adds the **finance / value-investing vertical** to the cross-vertical set {SEO v64 · academic-research v90 · cybersecurity v98 · [4th]}. Exact N-tally (→5?) is **audit bookkeeping**, recorded not self-incremented. **No new top-level pattern (max #85), no new §C standalone, counts UNCHANGED 46/11.**

**Why no §C mint** (the camofox v179 / v180 / v181 anti-"draw-the-circle" discipline): the distinctive facets — a **domain-expert adversarial persona panel** (echoes agency-agents v185 §C persona library + agent-skills v184's 4 review personas + the vault's own 3-lens+critic), **deterministic-tool-offload as a mandatory gate** (a nice engineering idea, but within the general tool-use paradigm), a **publish/exit verification gate** (the doubt-driven-dev / verify-rule motif), and a **real-money track record** (unverified) — are each *within an existing family*. Minting on their conjunction would be the generalize-to-fit over-claim declined at camofox v179. A candidate facet ("a single-domain 4-real-master adversarial research team") is recorded as a **DEFERRED watch axis**, not minted at N=1.

### Secondary observations (NOT minted)
- **#19 19a** — first `xbtlin` author data-point.
- **T1 Domain-Vertical-Skill-Collection** instance-strengthening (finance vertical) — see above.
- **#84 84c** provider-agnostic-by-design — one canonical `skills/*.md` → generated Codex skills + Codex prompts + installed Claude commands via sync scripts (`--check` drift mode). **NO N-bump** per v86; **NOT** the ponytail v168 "14-platform native-rule-file" mechanism (this is a 2-harness generate-and-install pipeline).
- **#12 LLM-routing-artifacts** high-density — `CLAUDE.md` + `AGENTS.md` + `ai_CLAUDE.md` (the last = a hand-maintained session-memory file, an L2/L3 artifact relevant to your **CC-memory-systems** thread).
- **Multi-agent parallel orchestration** cross-ref — `TeamCreate`/`TaskCreate`/`Task(run_in_background)`, 4-agent (investment-team/earnings-team) + 7-agent (private-company-research) fan-outs + team-lead synthesis — lands on your **multi-agent-orchestration** pilot thread.
- **#66 supply-chain / dual-use** — MIT; tools are **zero-dependency Python stdlib** (safe); `financial_rigor.py`'s `calc` uses `eval()` behind a char-allowlist (minor sandbox note); `xueqiu_scraper.py` = Playwright scraper of a Chinese finance site (ToS/dual-use); install scripts copy skills into `~/.claude/commands/` + `~/.codex/skills/`; ⚠️ **the README recommends `claude --dangerously-skip-permissions`** — a real footgun to flag on any pilot.

### NON-claims
- **NOT corpus-first** for finance/investing agent tooling — financial-services **v141** (Anthropic-official) precedes in the finance domain.
- **NOT a new top-level pattern** (max #85).
- **NOT #52** — 7.7k★/973 forks/1 release page-stated, NOT API-verified (§37.4) → velocity unestablishable. The +69%/+66%/¥1.46M returns are **unverified marketing** (no trade logs; README examples self-admittedly illustrative), NOT a #52 basis.
- **NOT #57** — cites Buffett/Munger/Duan Yongping/Li Lu (real-world investing masters, NOT corpus subjects) + names Claude Code/Codex as harnesses it targets; mentions ≠ recursion.
- **NOT #18 B1-MCP** — a skill/command collection + CLI tools, not an MCP server (the roadmap lists *future* MCP data feeds, not shipped).
- **NOT a new §C standalone** (see above).

## Tier

**T1 Skill/Methodology Collection** (Domain-Vertical flavor) — the karpathy v63 / mattpocock v57 / CodexKit v121 / claude-seo v64 / agent-skills v184 family.

## Streak / ceiling

Streak **GA:47 → GA:48** *(per operator direction, consistent with v176/v186 GLM-5/DeepSpec handling; under the OFF-GOAL reading of those two → GA:46·OG:13)*. **§35 CLEAR** — window {v185 GA, v186 GA, **v187 GA**} = 0 OG. **33 consecutive goal-aligned ships v153→v187** (GA reading). Lifetime operator overrides = 10 (unchanged); v153→v187 = zero overrides.

## inflation_check

Discipline **HELD** — 0 mints; max #85; counts 46/11 unchanged; §C surface unchanged; the Domain-Vertical-Skill-Collection N-bump recorded-not-self-incremented; no double-count (the multi-agent + persona + cross-harness facets are cross-refs, not separate mints); the "generalize-to-fit" §C mint DECLINED; the unverified returns kept as NON-claims.
