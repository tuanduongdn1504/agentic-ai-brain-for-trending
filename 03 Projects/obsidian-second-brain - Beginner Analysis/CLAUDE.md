# obsidian-second-brain — Project Context

**Subject:** [`eugeniughelbur/obsidian-second-brain`](https://github.com/eugeniughelbur/obsidian-second-brain) — "one brain, four CLIs, 43 commands. A cross-CLI skill for Obsidian that runs on Claude Code, Codex CLI, Gemini CLI, and OpenCode."
**Wiki version:** v134 (Routine **v2.6**).
**Status:** SHIPPED 2026-06-01. **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL + (b) **STRONG** + (c) STRONG + (d) **STRONGEST**. **§35 STAYS CLEAR** (window → {v132 GA, v133 OG, v134 GA} = 1 OG ≤ 1; v134 goal-aligned avoids the re-breach flagged at v133).

## One-line

A **cross-CLI Claude Code skill** (also Codex CLI / Gemini CLI / OpenCode) that operates an **Obsidian vault as a living, self-rewriting "second brain."** 43 commands across 4 layers (Operations 28 / Thinking 7 / Context Engine 1 / Research 7; 39 cross-platform + 3 Claude-only Google-Calendar). One canonical codebase compiles to 4 CLI-native builds via `scripts/build.sh`. **Explicitly positions itself as "an evolution of Karpathy's LLM Wiki pattern"** — ingesting a source *rewrites 5–15 existing pages* instead of appending; `/obsidian-reconcile` resolves contradictions; `/obsidian-synthesize` writes cross-source synthesis pages unprompted; 4 scheduled background agents (morning / nightly close / weekly review / vault-health) "compound your vault while you sleep." ~8,500-line monolithic `SKILL.md`. MIT; Python 76% + Shell 22% + HTML 2%. By **Eugeniu Ghelbur** (AI Automation Engineer @ Single Grain; X @eugeniu_ghelbur; Substack "The AI Operator"). **~1,700★ / first public release ~Apr 5 2026 (~8 wks) / ~30★/d → lower-edge SUSTAINED-MODERATE-HIGH** ("1,000+ stars in 7 weeks" per README). ⚠️ created_at inferred from the release timeline (the sandbox blocked the GitHub API).

## Why it's the most on-the-nose corpus subject for *this* vault

This skill is, almost line-for-line, **the productized/installable form of what Storm Bear does by hand in this vault.** Compare its `SKILL.md` rules to this vault's `CLAUDE.md`:
- "The vault is designed for **future-Claude to read and reason over, not for human review**" ↔ the vault's whole premise (Karpathy LLM-wiki for the LLM, not the human).
- "**Never claim absence from memory, never fabricate**; mark unknowns as TBD rather than inventing" ↔ the vault rule "NEVER fabricate information — if you don't know, say so."
- Rewrite-not-append + contradiction reconciliation + synthesis pages ↔ the wiki-maintainer jobs (update entity pages, flag contradictions, file synthesis).
- AI-first frontmatter + recency markers ("as of 2026-04, source-url") + mandatory wikilinks ↔ the vault's citation + cross-reference discipline.
- **Bi-temporal facts** (`timeline:` arrays preserving both event-time and when-the-vault-learned-it) — a discipline this vault does NOT yet have (CORPUS-FIRST; filed as a Library-vocab standalone).

## Pattern Library impact

**PRIMARY: Pattern #57 corpus-recursive-at-methodology-influence-layer → N=3** (PROMOTION-ELIGIBLE; formal promotion DEFERRED to the imminent ~v134–v135 audit). v94 Understand-Anything (**consume** — builds a knowledge graph from a codebase, designed for Karpathy-pattern LLM wikis) + v118 OpenHuman (**generate** — productized Karpathy-LLM-wiki desktop app) + **v134 obsidian-second-brain (generate — the PUREST instance: a Claude Code skill that operates your *existing* Obsidian vault as a self-rewriting Karpathy-LLM-wiki).** Broad event-class → N=3; the "generate" sub-vector → N=2 (v118+v134). **This is the genuine 3rd instance the thread was waiting for** — and notably the one **v132 supermemory was correctly DECLINED for** (supermemory is a fact-extraction memory DB, not a Karpathy-LLM-wiki/markdown vault; v134 *is* one). NOT manufactured. ⚠️ The v120 audit held this at N=2 PROVISIONAL because v94/v118 are "different vectors, not yet one confirmed class" — the audit decides promote-broad-class vs split-into-consume(N=1)+generate(N=2). I register + flag, I do **not** unilaterally promote.

**SECONDARY (observations; §28-disciplined — filed as ACTS):**
- **NEW Library-vocab standalone (N=1, FILED to registry 06 section C):** **"Bi-Temporal Fact Discipline in an Agent-Maintained Knowledge Vault"** — `timeline:` arrays that never-overwrite, preserving both *event-time* and *vault-learned-time* for audit/history queries. CORPUS-FIRST; promotion-eligible at N=2. (1 standalone ≤ 2 cap.)
- **Pattern #84 84c.2 "CLI-generates-native-formats-from-canonical-source" N+1** (the v76 agent-skills-standard sub-mechanism) — `scripts/build.sh --platform [codex-cli|gemini-cli|opencode]` compiles one source → Claude/Codex/Gemini/OpenCode native formats + per-CLI dispatchers (CLAUDE.md / AGENTS.md / GEMINI.md). CONFIRMED sub-mechanism, note only.
- **Library-vocab #12 LLM-routing artifacts N+1** (CLAUDE.md + AGENTS.md + GEMINI.md + SKILL.md). CONFIRMED, note only.
- **Pattern #18 B1 MCP** N+1 — MCP server is one of 3 vault-access methods (SessionStart hook / MCP / filesystem fallback).
- **Pattern #82 quantitative-marketing** — "1,000+ stars in 7 weeks", "43 commands", "4 CLIs", trending badge.
- **Pattern #66 supply-chain** — `curl -fsSL …/quick-install.sh | bash` (classic caution) + optional BYOK research keys (xAI/Perplexity/Gemini/YouTube/OpenAI). Load-bearing for the pilot trust assessment.

**Honest non-claims:**
- **(a) FAILs honestly** — not laundered into a Moldovan/Eastern-European (a)-sub-axis (per §25 / v98 / v112 / v113 diaspora precedent, no new axis minted).
- **(b) STRONG not STRONGEST** — the domain is PKM/knowledge-management, not software-dev *shipping* (the `/obsidian-architect` code-doc command is the only direct software-dev surface); plus influencer/marketing positioning and a `curl|bash` footprint that operates on your vault.
- **Pattern #57 N=3 is a REGISTRATION + promotion-eligibility flag, NOT a unilateral promotion** (audit decides; honest about the consume-vs-generate vector question).
- **NOT an agentskills.io 57k implementer** — it ships its OWN `quick-install.sh` + `build.sh`, with no evidence of `npx skills add` / agentskills.io registration. (Closer to v121 CodexKit's "parallel distribution mechanism" framing, but for Claude/Codex/Gemini/OpenCode.) Do not count it in the 57k chain.
- **NOT a Pattern #52 promotion** — ~30★/d × ~57d = lower-edge SUSTAINED-MODERATE-HIGH, not EXTREME.
- **Only 1 new Library-vocab standalone** (bi-temporal), within §28 ≤2; otherwise Pattern-layer / CONFIRMED-item notes.
- **NO Pattern Library state change at ship** (46 confirmed / 8 Library-vocab CONFIRMED unchanged; the Pattern #57 promotion is the audit's call).

## §35 ceiling status (v2.6)

Ceiling was **CLEAR** entering this ship (after v133, window {v131 GA, v132 GA, v133 OG} = 1 OG). **v134 = GOAL-ALIGNED INCLUDE → window scrolls to {v132 GA, v133 OG, v134 GA} = 1 OG ≤ 1 → STAYS CLEAR (§35.3).** This is exactly the move that **avoids the re-breach flagged at v133** (a 2nd consecutive off-goal at v134 would have made it 2 OG). No override; v134 is not an override (override-frequency triggers unchanged: lifetime 4, 3-in-30 last tripped at v127).

## Streak (v2.5 §32 forward / v2.6)

Historical **"49+3\*" frozen @v125**. Forward: **`GA:3 · OG:4 [1 ov]` → `GA:4 · OG:4 [1 ov]`** (v134 = 4th GOAL-ALIGNED PASS under v2.5/v2.6; the consecutive-GA stream restarts at 1 after v133 broke the v131→v132 run). Override subset `[1 ov]` UNCHANGED.

## Files

- `02 Wiki/index.md` — wiki page.
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` — GOAL-ALIGNED INCLUDE gate (a/b/c/d) + §35 ceiling-stays-clear analysis.
- `01 Analysis/(C) Pattern-Library-Phase-4b-Pattern-57-corpus-recursive-N3.md` — Pattern #57 N=3 corpus-recursive PRIMARY + bi-temporal standalone + secondaries + the honest consume-vs-generate vector question for the audit.

## Pilot note

**The single highest-value pilot candidate in corpus history for *this* operator — and the one with the sharpest collision risk, so fence it hard.** It is literally an installable Claude Code skill that would operate THIS vault's exact substrate (Obsidian + Claude + Karpathy-LLM-wiki). But: (i) `curl|bash` install that **rewrites 5–15 of your files per write** = high footprint; (ii) its "AI-first, for-future-Claude-not-human-review" notes + auto-reconcile **actively rewrite hand-curated pages** — a direct philosophy clash with this vault's "ask before editing my notes" + careful hand-curation discipline; (iii) it overlaps heavily with what Storm Bear already does by hand. **Recommended: a fenced READ + scratch-vault pilot, NOT an install on the real KJ OS Template vault.** Read `SKILL.md` + `architecture.md` first as a methodology study (it's the closest external articulation of this vault's own operating model — especially the bi-temporal-facts and synthesis-agent mechanics worth *borrowing by hand*), then trial `/obsidian-init` on a THROWAWAY Obsidian vault via `install-snapshot`, to evaluate the self-rewrite/reconcile/synthesis loop without risking the real corpus. Complements (doesn't replace) the still-un-piloted v126 compound-engineering (dev process) + v131 harness (team generator) + v132 supermemory (memory layer).
