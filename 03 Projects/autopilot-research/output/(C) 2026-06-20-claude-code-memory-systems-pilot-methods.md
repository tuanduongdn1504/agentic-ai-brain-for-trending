# Pilot methods — applying the 6-level Claude Code memory taxonomy to your working flows

> **Source:** [[claude-code-memory-systems/_index]] — Simon Scrapes "Every Claude Code Memory System Compared" ([UHVFcUzAGlM](https://www.youtube.com/watch?v=UHVFcUzAGlM)) + direct deep-dives of the originals ([Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [Connolly](https://www.youngleaders.tech/p/how-i-finally-sorted-my-claude-code-memory)/[Huryn](https://substack.com/@huryn/note/c-216337711), [MemSearch](https://github.com/zilliztech/memsearch), [MemPalace](https://github.com/MemPalace/mempalace), [claude-mem](https://github.com/thedotmack/claude-mem), [OpenBrain](https://github.com/NateBJones-Projects/OB1)). Verification: [[claude-code-memory-systems/source-provenance]].
> **Date:** 2026-06-20.
> **Your flows (from vault + memory):** **(A)** your **personal `~/.claude` operational memory** (you run L1 + a hand-maintained L2); **(B)** the **autopilot-research vault** (this project — it *is* L5); **(C)** the **Storm Bear curated vault** (also L5, larger); **(D)** **hireui** — your Goal-#2 SaaS (per-repo memory, no LLM yet); **(E)** **Scrum coaching / team**.
> **17 methods, ranked.** Each has a video/original pattern, a concrete first step, and a success signal.
>
> **The headline:** you are **not a beginner here.** You already run **L1 + a manual L2** (your `~/.claude/.../memory/MEMORY.md` is textbook Connolly/Huryn) and both vaults **are L5**. So the win isn't "adopt a system" — it's **(1) automate the L2 upkeep you do by hand, (2) add L3 semantic retrieval so your vaults scale, and (3) consciously *not* adopt L4/L6.** Full map: [[claude-code-memory-systems/your-current-setup-mapping]].

---

## ▶ Start here (recommended sequence)

1. **Today, ~10 min, you already have the tool:** **A1** — run the **`/consolidate-memory`** skill over your `~/.claude/.../memory/` files. That skill *is* Karpathy's "lint" + Connolly's "reorganize memory": merge duplicates, fix stale facts, prune the index. You have 7 memory files accreting since 2026-06-02; this is overdue and free.
2. **This week, highest structural leverage:** **A3 + A4** — audit `MEMORY.md` against the **200-line budget**, split overloaded notes into **domain/tools** files, and **promote** a mature cluster (e.g. your "vault shell flaky workarounds") from a memory note into an actual **skill** (the L2 domain→plugin lifecycle).
3. **The scaling fix for your vaults:** **B5** — add **semantic retrieval** over the autopilot wiki (the `_master-index.md` is now a wall of paragraphs — that's context rot *in the index itself*). Pilot MemSearch or `qmd` on a copy.

---

## Ranked table

| # | Method | Flow | Effort | Value | Why it ranks here |
|---|---|---|---|---|---|
| **A1** | Run `/consolidate-memory` (= the "reorganize memory"/lint ritual) | A personal | **Low** (~10m) | **High** | You own the tool; memory files overdue for a pass |
| **A3** | Audit `MEMORY.md` vs 200-line budget; split to domain/tools | A personal | Low | **High** | Enforces the one discipline L2 is built on |
| **B5** | Semantic retrieval over the vault (MemSearch / `qmd`) | B autopilot | Med | **High** | `_master-index.md` bloat = context rot; retrieval won't scale on read-the-index alone |
| **A4** | Promote a mature memory cluster → a Skill (domain→plugin) | A personal | Med | **High** | The L2 lifecycle; turns recurring facts into reusable capability |
| **D10** | Build hireui's per-repo operational memory *right* | D hireui | Med | **High** | Goal #2; do L2 properly before the repo grows |
| **B6** | Compress the bloated `_master-index.md` (index-first lint) | B autopilot | Low–Med | Med–High | The index *is* the retrieval mechanism — keep it scannable |
| **A2** | (Optional) custom `additionalContext` injection hook | A personal | Med | Med | Native auto-memory already injects for you — only if you outgrow it |
| **C8** | Frame Pattern-Library audits as Karpathy "lint" + add a cadence | C SB vault | Low | Med | You already audit; name the ritual + schedule it |
| **B7** | Add a real `log.md`/promotion log discipline | B autopilot | Low | Med | loop-log ≈ this; make ingest/query/lint entries uniform |
| **E12** | The 6-level taxonomy as a team/client decision aid | E coaching | Low | Med | "Which level does your team need?" is a sharp framing |
| **A5** | Adopt the daily-note + dreaming split for fast-moving work | A personal | Med | Med | L3's short-term/long-term model; promotion of recurring facts |
| **C9** | Codify "chapter < 35K tokens" as the explicit anti-context-rot rule | C SB vault | Low | Med | You already did the `_state/` refactor — make the rule explicit |
| **E13** | Shared domain/tool `.md` files for a team's Claude usage | E coaching | Med | Med | L2's team-sharing; granular shared context |
| **B11** | Schedule the vault's reorganize/lint as a nightly autopilot phase | B autopilot | Med | Med | "Dreaming" as a cron, bounded by the routine |
| **D14** | Flag the L6/Mem0 decision for *hireui's future user-facing memory* | D hireui | Low (note) | Med | When hireui adds AI, end-user memory is a product choice |
| **A15** | Keep operational memory (L1/2/3) and the research wiki (L5) separate | A/B | Low (rule) | **High** | The video's real lesson; prevents two systems rotting into one |
| **E16** | Teach "context rot" + the 200-line rule as an agent-literacy lesson | E coaching | Low | Med | The most transferable concept for non-experts |

---

## A — Your personal `~/.claude` operational memory (you run L1 + manual L2)

> Your `~/.claude/projects/-Users-Cvtot-KJ-OS-Template/memory/MEMORY.md` is the **native auto-memory index** (L1) maintained with **L2 discipline** (one-fact files, `**Why:**`/`**How to apply:**`, `[[links]]`, typed). You already get **auto-injection** from the native harness (recalled memories show up in `<system-reminder>` blocks). So your gaps are **upkeep + structure**, not injection.

### A1 — Run the "reorganize memory" / lint ritual (you have the skill) ⭐
- **Pattern:** L2's **`reorganize memory`** (dedupe / merge / split / re-sort / re-index in plan mode) = Karpathy's **lint** = your installed **`anthropic-skills:consolidate-memory`** skill ([[claude-code-memory-systems/level-2-reliable-recall-hooks]]).
- **Apply:** run it periodically over `~/.claude/.../memory/`. Plan-mode equivalent: review proposed merges/deletions before applying.
- **First step:** invoke **`/consolidate-memory`** now (7 files since 2026-06-02, none consolidated).
- **Success signal:** duplicate/stale entries merged or pruned; `MEMORY.md` index lines match the files that exist.

### A3 — Enforce the 200-line budget + the domain/tools split ⭐
- **Pattern:** project `MEMORY.md` has a **~200-line budget**; entries are **date/what/why**; cross-project facts go to `general.md`, tool quirks to `tools/{tool}.md`, topic knowledge to `domain/{topic}.md` ([[claude-code-memory-systems/level-2-reliable-recall-hooks]]).
- **Apply:** audit your `MEMORY.md` line count; any note doing two jobs gets split; classify by your existing types (`reference`≈tools, `project`/`feedback`≈domain).
- **First step:** count lines in `MEMORY.md`; if > ~150, move the longest pointer's content into a dedicated topic file and leave a one-line index entry.
- **Success signal:** `MEMORY.md` stays a lean index; no single memory file mixes unrelated topics.

### A4 — Promote a mature memory cluster into a Skill ⭐
- **Pattern:** the L2 **domain lifecycle** — *staging* (`domain/{name}/`) → *promotion* (package as a skill/plugin) → *pointer* (memory file points at the plugin) ([[claude-code-memory-systems/level-2-reliable-recall-hooks]]); mirrors [[claude-cowork/skills-vs-plugins-hierarchy]].
- **Apply:** find a memory note that's really a *procedure*, not a fact, and turn it into a skill.
- **First step:** your **`project_vault_shell_flaky_workarounds`** memory (stub rtk / no `cd` / route git output to a file / verify via `git log`) is a recurring *workflow* — promote it to a `vault-shell-safe-git` skill (use `anthropic-skills:skill-creator`); leave the memory note as a one-line pointer.
- **Success signal:** the workaround fires reliably as a skill instead of relying on the memory note being recalled.

### A2 — (Optional) a custom `additionalContext` injection hook
- **Pattern:** L2's `.py`+`.sh`+`settings.json` **PreToolUse** hook injecting `MEMORY.md` via `additionalContext` ([[claude-code-memory-systems/level-2-reliable-recall-hooks]]).
- **Honest caveat:** the **native auto-memory already injects** relevant memories for you — so this is **lower value for your specific setup** than it is for someone on a custom `.claude/memory/` tree. Only build it if you move to a custom structure or find native recall missing things.
- **First step:** *don't build it yet.* Instead, note in your memory whether native recall ever misses a fact you know is filed — that's the trigger to revisit.
- **Success signal:** you can point to a concrete native-recall miss before adding the hook (evidence-first, per Rule 1).

### A5 — Adopt the daily-note + "dreaming" split for fast-moving threads
- **Pattern:** L3/OpenClaw's **short-term (per-day notes) vs long-term (`memory.md`)** split, with **dreaming** promoting recurring items ([[claude-code-memory-systems/level-3-semantic-search]]).
- **Apply:** for active pilot threads (you have several open — prompt-eval, multi-agent, cowork-3p), keep a dated running note; let `/consolidate-memory` promote the durable facts into typed memories.
- **First step:** start one dated note for the current week's pilots; at week end, consolidate.
- **Success signal:** durable decisions survive in typed memories; daily churn doesn't bloat `MEMORY.md`.

### A15 — Keep operational memory and the research wiki **separate** ⭐ (rule)
- **Pattern:** the video's core critique — **L5 is a knowledge base, not operational memory** ([[claude-code-memory-systems/level-5-knowledge-base-llm-wiki]]).
- **Apply:** never merge the two. `~/.claude/.../memory/` answers *"how do I work / what did I decide"*; the vaults answer *"what do I know about topic X."* Don't stuff research synthesis into `MEMORY.md`, don't ask the wiki for operational recall.
- **First step:** add a one-line memory note recording this boundary as a standing rule.
- **Success signal:** neither system drifts into the other's job over the next month.

---

## B — autopilot-research vault (it *is* Level 5)

> This vault is a faithful, industrialized Karpathy LLM Wiki: `raw/` (read-only) + `wiki/` (LLM-owned) + `_master-index.md` + per-topic `_index.md` + `[[links]]` + compile/query/audit + loop-log. The originals tell you exactly how to keep it healthy *and* where it's straining.

### B5 — Add semantic retrieval over the wiki ⭐
- **Pattern:** Karpathy: the **`index.md` read-first** retrieval works to ~100 sources, then add a **hybrid search tool (`qmd` — BM25+vector+LLM rerank) via CLI/MCP**; MemSearch is the Claude-Code-native version ([[claude-code-memory-systems/level-5-knowledge-base-llm-wiki]], [[claude-code-memory-systems/level-3-semantic-search]]).
- **Apply:** you're past 20 topics and the `_master-index.md` is a wall of paragraphs — read-the-index retrieval is creaking. Add semantic search over `wiki/`.
- **First step:** pilot `qmd` (or MemSearch in a throwaway repo pointed at a copy of `wiki/`) and compare a few real queries vs grepping the index.
- **Success signal:** a "which topic covered X?" query returns the right article *faster/more accurately* than reading `_master-index.md`.

### B6 — Compress the `_master-index.md` (index-first lint)
- **Pattern:** the index **is** the retrieval mechanism — it must stay **scannable** ([[claude-code-memory-systems/level-5-knowledge-base-llm-wiki]]). Right now each topic entry is a dense paragraph; the index itself now risks context rot.
- **Apply:** keep a **terse one-line** master index (topic + 1 sentence + link); push the rich detail down into each topic's `_index.md` (where it already lives).
- **First step:** draft a "lite" `_master-index.md` variant (one line per topic) and see if navigation improves; keep the detailed version as a sibling if useful.
- **Success signal:** the master index fits in a glance; drill-down detail still one click away.

### B7 — Uniform ingest/query/lint log discipline
- **Pattern:** Karpathy's **`log.md`** — append-only, uniformly prefixed (`## [date] ingest | Title`) for parseable history ([[claude-code-memory-systems/level-5-knowledge-base-llm-wiki]]).
- **Apply:** your `loop-log/` is close; standardize the entry prefix across loop-logs so the history is greppable.
- **First step:** adopt a consistent `## [YYYY-MM-DD] <verb> | <topic>` line at the top of each loop-log.
- **Success signal:** you can reconstruct the vault's history by grepping one pattern.

### B11 — Schedule reorganize/lint as a nightly autopilot phase ("dreaming" as cron)
- **Pattern:** L3's **dreaming** = automatic background consolidation ([[claude-code-memory-systems/level-3-semantic-search]]); your routine already has an audit phase.
- **Apply:** add a bounded lint pass to the `/schedule autopilot nightly` cron (orphan pages, stale claims, missing cross-refs) — the vault's own dreaming.
- **First step:** add a Phase-5b "lint" step to `(C) autopilot-research-routine.md` that writes findings to `output/` (don't auto-edit; report, per your audit rule).
- **Success signal:** a nightly run surfaces ≥1 real gap without you asking.

---

## C — Storm Bear curated vault (Level 5, at scale)

### C8 — Name the audit ritual "lint" + put it on a cadence
- **Pattern:** Karpathy's **lint** verb (contradictions / stale claims / orphans / missing cross-refs / data gaps) ([[claude-code-memory-systems/level-5-knowledge-base-llm-wiki]]).
- **Apply:** your Pattern-Library mini-audits *are* lint passes — frame them that way and you inherit Karpathy's checklist as the audit template.
- **First step:** at the next mini-audit (v66 cadence), run the explicit 5-item lint checklist alongside the pattern-promotion work.
- **Success signal:** the audit catches a stale claim or orphan it would otherwise have missed.

### C9 — Codify "chapter < 35K tokens" as the explicit anti-context-rot rule
- **Pattern:** **context rot** is why you refactored a 146K-token `CLAUDE.md` into `_state/` chapters ([[claude-code-memory-systems/overview]]).
- **Apply:** that refactor *is* this video's lesson, already proven in your own history. Make the rule explicit so it doesn't regress.
- **First step:** confirm the `_state/` chapter-size invariant is written down as a rule (it's described in CLAUDE.md — promote it to a hard "never exceed" line).
- **Success signal:** no chapter creeps back over the threshold.

---

## D — hireui (Goal #2, the real build target)

> hireui has its own CONSTITUTION (agent-* branch policy, operator-only skill registry, GitNexus-first) + BMAD harness + `.pilot-log`, and **no LLM integration yet**. So memory here = **build the dev-workflow memory right**, plus a forward note for when the product gains AI.

### D10 — Build hireui's per-repo operational memory *properly* ⭐
- **Pattern:** L2 **per-project `MEMORY.md`** (200-line budget, date/what/why, domain/tools split) ([[claude-code-memory-systems/level-2-reliable-recall-hooks]]).
- **Apply:** give hireui a disciplined repo memory that respects its CONSTITUTION — decisions, gotchas, env quirks captured as you build, not after.
- **First step:** ensure `hireui/.claude/` (or its BMAD equivalent) has a lean `MEMORY.md` index + topic files; reconcile with `.pilot-log` so they don't duplicate. Follow hireui's rules, not the vault's.
- **Success signal:** a cold Claude session in hireui loads the right context without you re-explaining the CONSTITUTION/architecture.

### D14 — Flag the L6/Mem0 decision for hireui's *future user-facing* memory
- **Pattern:** L6 (OpenBrain vs Mem0) is the **cross-tool / product memory** choice ([[claude-code-memory-systems/level-6-cross-tool-brain]]).
- **Apply:** when hireui adds an AI feature that needs to *remember a user/candidate across sessions*, that's a product-architecture decision (own-it Postgres+pgvector vs hosted Mem0) — and it composes with the **data-sovereignty** thread from [[cowork-third-party-inference/_index]] (candidate PII).
- **First step:** add a one-line note to hireui's runbooks: "user-facing memory = pgvector-own-it vs Mem0; decide at feature-design, weigh PII sovereignty." No build now.
- **Success signal:** the decision is captured, not rediscovered under deadline.

---

## E — Scrum coaching / team practice

### E12 — The 6-level taxonomy as a team/client decision aid
- **Pattern:** the video's whole framing — *which* memory level fits *which* need ([[claude-code-memory-systems/overview]] decision guide).
- **Apply:** a one-slide lens for teams adopting Claude Code: "Start at L1; add the L2 hook when files grow; most should stop there; go L3+ only on real evidence."
- **First step:** turn the overview decision guide into a one-pager for a team you coach.
- **Success signal:** a team picks a level deliberately instead of cargo-culting a tool.

### E13 — Shared domain/tool `.md` files for a team's Claude usage
- **Pattern:** L2 **team-sharing** — sync `domain/`/`tools/` markdown so teammates inherit granular context ([[claude-code-memory-systems/level-2-reliable-recall-hooks]]).
- **Apply:** a team keeps shared tool-config + domain-knowledge `.md` files in a repo; everyone's Claude gets the same operational memory.
- **First step:** propose a `team-memory/` repo with `tools/` + `domain/` for one squad.
- **Success signal:** a new teammate's Claude is productive on the team's stack without a manual brain-dump.

### E16 — Teach "context rot" + the 200-line rule as agent literacy
- **Pattern:** **context rot** + keep-the-index-lean is the single most transferable concept ([[claude-code-memory-systems/overview]], [[claude-code-memory-systems/level-1-native]]).
- **Apply:** the highest-leverage thing a non-expert can learn — *more context ≠ better recall; load less, at the right time.*
- **First step:** use the "don't stuff the whole brand guide into CLAUDE.md" example in your next coaching session.
- **Success signal:** someone trims their bloated `CLAUDE.md` after the lesson.

---

## What to consciously SKIP (and why) — the discipline half

- **L4 (MemPalace):** verbatim recall is **opaque** (not readable markdown) — it fights your whole own-it/version-control philosophy. Adopt only on a concrete "exact words from weeks ago" need you don't currently have.
- **L6 (OpenBrain/Mem0):** you live mostly inside Claude Code; you don't tool-switch constantly. It adds setup + monthly cost + per-query latency + an off-laptop DB for a problem you don't have. (Exception: a *hireui product* feature — D14.)
- **claude-mem over MemSearch:** if you do pilot L3, prefer the **markdown-first** option; claude-mem's dashboard/MCP DB is a heavier bet you don't need.
- **Even the author stops at L3** — and his use case (multi-tool Agentic OS) is broader than yours. **L1+L2 automated + L3 on the vaults is your complete endpoint.**

## Critic's reframe (the contrarian read)

The sharpest insight in the video isn't a tool — it's the claim that **L5 (LLM Wiki) is the wrong tool for operational memory**, aimed squarely at people like you who've gone all-in on a wiki. Take it seriously: if you ever feel the autopilot/Storm Bear vaults *failing* you, it's probably because you asked an L5 research system to do L1/L2 operational recall. The fix is never "a bigger wiki" — it's **routing the question to the right system.** Your two-vault + `~/.claude`-memory split is already correct; the risk is letting the boundary blur. (And note the counter-signal: LangChain is *productizing* the LLM Wiki as agent "Context Hub" — [[agent-development-lifecycle/_index]] — so L5 is being validated *for the research/context job*, not retired.)

## Cross-links

- [[claude-code-memory-systems/_index]] (source topic) · [[claude-code-memory-systems/your-current-setup-mapping]] (where you stand) · [[claude-code-memory-systems/source-provenance]] (what's verified).
- Composes with: [[claude-api-cost-optimization/_index]] (context rot = the same enemy) · [[prompt-evaluation/_index]] (eval a retrieval change before trusting it) · [[claude-code-hooks/_index]] (the L2–L4 hook primitive) · [[ai-operating-system/_index]] (sister taxonomy) · [[cowork-third-party-inference/_index]] (D14's PII-sovereignty thread).

## Suggested next action

Do **A1 right now** — run **`/consolidate-memory`** over your `~/.claude/.../memory/` files (~10 min, you already have the skill, it's overdue). Then this week do **A3 + A4** (200-line audit + promote the `vault-shell-flaky-workarounds` note into a real skill). When you're ready for the scaling work, say the word and I'll **scaffold B5** — stand up semantic retrieval (`qmd` or MemSearch) over a copy of the autopilot `wiki/` and benchmark it against the current read-the-index flow. Tell me which and I'll start.
