# obsidian-second-brain — Wiki (v134)

> `eugeniughelbur/obsidian-second-brain` · **"one brain, four CLIs, 43 commands."** · A cross-CLI Claude Code skill that operates an Obsidian vault as a **living, self-rewriting second brain**: a source rewrites 5–15 existing pages instead of appending, contradictions reconcile automatically, synthesis pages write themselves, and 4 scheduled agents "compound your vault while you sleep." **Explicitly positioned as "an evolution of Karpathy's LLM Wiki pattern."**

**(C) Claude-generated wiki page.** Fetched 2026-06-01 (GitHub repo page + README + SKILL.md + releases). Routine **v2.6, wiki #134.** Phase 0.9: **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL, (b) **STRONG**, (c) STRONG, (d) **STRONGEST**. **§35 STAYS CLEAR** (window → {v132 GA, v133 OG, v134 GA} = 1 OG ≤ 1 — a goal-aligned v134 avoids the re-breach flagged at v133). ⚠️ created_at/exact-stars inferred from the release timeline + README (the sandbox blocked the GitHub API; figures are best-effort, not API-verified).

---

## Identity

| Field | Value |
|---|---|
| Repo | [`eugeniughelbur/obsidian-second-brain`](https://github.com/eugeniughelbur/obsidian-second-brain) |
| What | **Cross-CLI Claude Code skill** that turns an Obsidian vault into a self-rewriting, self-maintaining "second brain" — NOT an Obsidian plugin (it operates the vault from *outside* Obsidian, via the CLI's filesystem/MCP access) |
| Tier / archetype | **T1 Assistant Skill** (one cohesive multi-command skill, 4-CLI build) — sits in the **corpus-recursive-at-methodology-influence thread** (generate sub-vector: v118 OpenHuman + v134) |
| Stars / forks | **~1,700★ / ~192 forks** (fork_ratio ~0.11) *(README: "1,000+ stars in 7 weeks")* |
| Created / age | **first public release v2.2.0 ~2026-04-05**; latest **v0.10.0 "The Architect" 2026-05-31** → **~8 weeks** as of 2026-06-01. ⚠️ created_at inferred from releases (API blocked) |
| Velocity | **~30 stars/day → lower-edge Pattern #52 SUSTAINED-MODERATE-HIGH** (25–150/d band; ~57d). NOT EXTREME, NOT a #52 promotion |
| License | **MIT** |
| Language | **Python 76.1%** + **Shell 21.6%** + **HTML 2.3%** |
| Distribution | `curl -fsSL …/scripts/quick-install.sh \| bash` → `/obsidian-init` (Claude Code); other CLIs via `bash scripts/build.sh --platform [codex-cli\|gemini-cli\|opencode]` |
| Default branch | `main` |
| Author | **Eugeniu Ghelbur** — AI Automation Engineer @ **Single Grain** (US digital-marketing agency); X **@eugeniu_ghelbur**, LinkedIn, Substack **"The AI Operator."** Moldovan/Romanian name; location undeclared |
| Versioning note | **Renumber/rebrand event:** releases ran v2.2.0→v4.0.0 (Apr 5–9) then **reset to v0.5.0 (Apr 26)** and continued v0.6→v0.10. A deliberate reset, not cross-file drift |

## What it is

A skill that fixes the gap between **daily Claude/CLI sessions** (start from scratch, forget everything) and **Obsidian notes** (sit unused, append-only). It lets the agent read, write, and *reason over* a vault and actively maintain it. Its thesis, in the author's words: an **"evolution of Karpathy's LLM Wiki pattern"** where *"every source updates existing pages instead of just appending new ones. Contradictions reconcile automatically. Your vault compounds while you sleep."*

**43 commands across 4 layers** (39 cross-platform + 3 Claude-only Google-Calendar):
- **Operations (28)** — `/obsidian-init`, save/ingest, `/obsidian-reconcile` (resolve contradictions), `/obsidian-synthesize`, export, maintenance, `/obsidian-architect` (scans a codebase and maintains architecture notes — the v0.10.0 "Architect" release).
- **Thinking Tools (7)** — `/obsidian-challenge`, `/obsidian-emerge`, `/obsidian-connect`, `/obsidian-panel` (challenge ideas, surface patterns, bridge domains).
- **Context Engine (1)** — loads identity + state at session start.
- **Research Toolkit (7)** — `/x-read`, `/x-pulse`, `/research`, `/research-deep`, `/notebooklm`, `/youtube`, `/podcast` (optional BYOK: xAI / Perplexity / Gemini / YouTube / OpenAI; v0.9.0 added free key-less research).

**The operating model (from `SKILL.md`, ~8,500 lines, ~200 sections):**
- **Vault access**: SessionStart hook · MCP server · filesystem fallback (3 methods).
- **13 Core Operating Principles** + Write Rules.
- **AI-first notes**: *"the vault is designed for future-Claude to read and reason over, not for human review"* — every note carries a 10-second relevance preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`), recency markers (`"as of 2026-04, source-url"`), and mandatory wikilinks.
- **Bi-temporal facts**: when a fact changes, never overwrite — append to a `timeline:` array preserving both *event time* and *when the vault learned it* (history + audit queries).
- **Two-Output Rule**: every interaction produces BOTH a conversational answer AND a vault update propagating the insight everywhere it belongs.
- **Search-before-creating / never-fabricate**: exhaust search before writing a new note; mark unknowns TBD; documented anti-patterns = *false absence* (assuming a note doesn't exist) + *fabrication* (inventing facts/rates/dates/relationships).
- **Propagation**: one write touches **5–15 files** via parallel subagents.
- **4 scheduled background agents**: morning · nightly close · weekly review · vault-health (orphan-heal + contradiction sweep).
- **Hooks**: PostCompact (background saves), PostToolUse (AI-first validation), SessionStart (vault access).

**Multi-CLI architecture**: one canonical codebase, `scripts/build.sh` compiles to 4 platform-native outputs — Claude Code (slash commands + `CLAUDE.md` dispatcher), Codex/OpenCode (`.codex/commands/` + `AGENTS.md` auto-routing), Gemini CLI (`.gemini/commands/` + `GEMINI.md`). The vault rules (AI-first notes, frontmatter, wikilinks) stay identical across all four. Top-level: `adapters/ commands/ hooks/ scripts/ references/ examples/ tests/ media/ .github/` + `README.md CHANGELOG.md CLAUDE.md SKILL.md architecture.md pyproject.toml install.sh`.

## Why it's in the corpus

**GOAL-ALIGNED INCLUDE** (v2.5 §31 tier — (b) passes, so this is the corpus's core, not an off-goal capture):

- **(a) FAIL** — Eugeniu Ghelbur is a **Moldovan/Romanian-named developer at a US marketing agency (Single Grain)**; location undeclared. Not a VN/Asian cultural-peer; not (a)-7 (no vault-substrate vendor relationship). Possibly a corpus-first Eastern-European locale, but undeclared + US-employer → WEAK-geographic, **not load-bearing**, and **no new (a) sub-axis is minted** (per §25 and the v98/v112/v113 diaspora precedent of not coining per-locale axes). Clean FAIL.
- **(b) STRONG** — this is the crux, and it passes well. It's a **multi-harness Claude Code skill** (the corpus's core medium) whose subject is **autonomous knowledge agents** (4 scheduled background agents + parallel subagents), directly serving goal #1's "master Claude and autonomous agents." It is also **the single most directly-applicable-to-this-vault subject in corpus history** — the KJ OS Template vault *is* a hand-maintained Obsidian + Claude + Karpathy-LLM-wiki, and this skill automates exactly that (self-rewrite, reconcile, synthesize, lint/health, notes-for-future-Claude). **NOT STRONGEST**, honestly, because: (i) the domain is **PKM/knowledge-management, not software-dev shipping** (only `/obsidian-architect` is a direct software-dev surface); (ii) **influencer/marketing positioning** ("compounds while you sleep", trending badge, a Substack funnel); (iii) the install is a **`curl|bash` skill that rewrites 5–15 of your files per write** — non-trivial footprint/trust. STRONG is the goal-aligned tier and clears §35 on its own — no inflation needed.
- **(c) STRONG** — a genuine **skill-authoring exemplar**: an ~8,500-line `SKILL.md`, 43 commands across 4 layers, a 4-CLI build system (one canonical source → native formats + dispatchers), hooks, scheduled agents, 13 principles, bi-temporal facts, the Two-Output Rule, and documented anti-patterns. Directly studyable for "how to author a large multi-harness Claude skill."
- **(d) STRONGEST** — the **highest connectivity of any recent ship**: it **explicitly extends Karpathy's LLM Wiki** (the corpus's ECC v1/v78 foundational anchor *and* this vault's premise) on the **Obsidian** substrate (the vault's literal home), implementing the exact maintainer jobs (rewrite-not-append, reconcile contradictions, synthesis, health/orphan-heal). It is the **3rd instance of the corpus-recursive-at-methodology-influence thread** (v94 consume + v118 generate + **v134 generate, purest**). Plus multi-harness Pattern #84 (84c.2), Library-vocab #12 routing artifacts (CLAUDE/AGENTS/GEMINI/SKILL), Pattern #18 B1 MCP, and the research-toolkit BYOK/aggregator threads.

## Pattern Library contribution (summary)

- **PRIMARY — Pattern #57 corpus-recursive-at-methodology-influence-layer → N=3** (PROMOTION-ELIGIBLE; promotion DEFERRED to the imminent ~v134–v135 audit). v94 Understand-Anything (consume) + v118 OpenHuman (generate) + **v134 (generate — the purest: a Claude Code skill that operates an existing Obsidian vault AS a self-rewriting Karpathy-LLM-wiki)**. Broad class → N=3; generate sub-vector → N=2 (v118+v134). **This is the genuine 3rd instance — the one v132 supermemory was correctly *declined* for** (memory DB ≠ Karpathy-LLM-wiki; v134 *is* one). NOT manufactured. The v120 audit's open question (one confirmed class vs consume(N=1)+generate(N=2)) is the audit's call.
- **SECONDARY (observations; §28-disciplined):**
  - **NEW Library-vocab standalone (N=1, FILED to registry 06 §C):** **"Bi-Temporal Fact Discipline in an Agent-Maintained Knowledge Vault"** — `timeline:` arrays preserving event-time + vault-learned-time, never-overwrite. CORPUS-FIRST; promotion-eligible at N=2. (A discipline this vault does *not* currently have — worth borrowing by hand.)
  - **Pattern #84 84c.2 "CLI-generates-native-formats-from-canonical-source" N+1** (`build.sh --platform`; the v76 sub-mechanism).
  - **Library-vocab #12 LLM-routing artifacts N+1** (CLAUDE.md + AGENTS.md + GEMINI.md + SKILL.md dispatchers).
  - **Pattern #18 B1 MCP** N+1 (MCP server = 1 of 3 vault-access methods).
  - **Pattern #82 quantitative-marketing** ("1,000+ stars in 7 weeks", "43 commands", "4 CLIs", trending badge).
  - **Pattern #66 supply-chain** (`curl|bash` quick-install + optional BYOK research keys).
- **Honest non-claims:** **(b) STRONG not STRONGEST** (PKM domain + influencer positioning + curl|bash footprint); **Pattern #57 N=3 is a registration + promotion-eligibility flag, not a unilateral promotion** (audit decides; honest about the consume-vs-generate vector question); **NOT an agentskills.io 57k implementer** (own `quick-install.sh`/`build.sh`, no `npx skills add` evidence); **NOT a Pattern #52 promotion** (~30★/d lower-edge); **only 1 new Library-vocab standalone** (bi-temporal, within §28 ≤2); **NO Pattern Library state change at ship** (the #57 promotion is the audit's call).

## Pilot

**The single highest-value pilot candidate in corpus history for *this* operator — and the one with the sharpest collision risk. Fence it hard.** It is literally an installable Claude Code skill that would operate THIS vault's exact substrate (Obsidian + Claude + Karpathy-LLM-wiki). Three caveats make a naive install dangerous: (i) `curl|bash` that **rewrites 5–15 of your files per write**; (ii) its "AI-first, for-future-Claude-not-human-review" notes + auto-reconcile would **actively rewrite your hand-curated pages**, which directly clashes with this vault's "**ask before editing my notes**" + hand-curation discipline; (iii) heavy overlap with what Storm Bear already does by hand.

**Recommended path — fenced READ + scratch-vault, NOT an install on the real KJ OS Template vault:**
1. **Read** `SKILL.md` + `architecture.md` as a methodology study — it's the closest external articulation of this vault's own operating model. The **bi-temporal-facts** mechanic and the **synthesis/reconcile scheduled-agent** loop are the two ideas most worth *borrowing by hand* into the vault's own routine.
2. **Trial** `/obsidian-init` on a **throwaway** Obsidian vault via `install-snapshot` (snapshot home → install → keep the uninstall checklist), to watch the self-rewrite/reconcile/synthesis loop run on disposable notes.
3. Only after that, consider whether any piece (e.g. a bi-temporal-fact convention, a contradiction-sweep checklist) is worth porting into the vault by hand — *without* handing the real corpus to an auto-rewriting agent.

Complements (does not replace) the still-un-piloted **v126 compound-engineering** (dev process), **v131 harness** (team generator), and **v132 supermemory** (memory layer).

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-Pattern-57-corpus-recursive-N3.md`.*
