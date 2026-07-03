# Pilot methods — applying agent-memory architecture to your working flows

> **Source topic:** `wiki/agent-memory-architecture/` (Sean Chen whiteboard + CoALA / Generative Agents / MemGPT-Letta / LangMem deep-dive + verified ChatGPT/Claude production memory)
> **Date:** 2026-07-03
> **Ranking basis:** Goal #2 leverage (hireui deployment evidence) > zero-install leverage > cost > novelty
> **Companion menus this composes with (don't duplicate):** claude-code-memory-systems 17 methods (operator tooling), mosh-ai-powered-apps (vendor-seam chatbot), ai-engineering 21 (demo→production discipline), prompt-evaluation (eval harness)

---

## ▶ Start here (recommended sequence)

1. **A1 — Write hireui's memory-layer spec, files-first** (~2h, zero install) — the Goal #2 artifact.
2. **C1 — Name and tune your own consolidation gate** (~45m) — turns the memory system you already run into a measured system.
3. **A2 — Prototype the candidate-memory store on the Anthropic memory tool** (~half day) — the first running memory code in hireui's stack.
4. Then pick from B/D/E as taste dictates.

---

## Ranked table

| # | Method | Flow | Cost | Payoff |
|---|--------|------|------|--------|
| A1 ⭐ | hireui memory-layer spec (files-first) | hireui | ~2h | Goal #2 design artifact |
| C1 ⭐ | Name + tune your consolidation gate | personal | ~45m | Measured memory hygiene |
| A2 ⭐ | Memory-tool prototype (candidate memory) | hireui | ~½ day | First running memory code |
| A3 ⭐ | Episodic log schema for recruiter–candidate interactions | hireui | ~1h | Unlocks A4/A5 |
| A4 | Two-stage consolidation gate (Haiku compress → Opus curate) | hireui | ~½ day | Cost-safe memory quality |
| A5 | Supersede-don't-append memory ops + citations | hireui | design rule | Anti-confabulation |
| A6 | Memory evals before shipping (LoCoMo-style probes) | hireui | ~½ day | Verifiable memory |
| A7 | Defer-the-vector-DB decision memo | hireui | ~30m | Avoids premature infra |
| B1 ⭐ | Adopt the substrate decision rule as a design checklist | all | ~15m | One-page discipline |
| B2 | Profile-vs-collection split for semantic memory | hireui/vault | design rule | Right-sized retrieval |
| B3 | Injection-over-retrieval for small memory (ChatGPT pattern) | hireui | design rule | Simpler v1 |
| B4 | Effective-context budgeting (150–400K rule) | all | ~15m | Context-rot insurance |
| C2 | Generative-Agents-style importance scoring on memory writes | personal | ~1h | Smarter memory triage |
| C3 | Episodic layer: transcript search as recall memory | personal | ~30m | Complete triad |
| C4 | Memory-quality probes after each consolidation | personal | ~30m | Catches lossy drift |
| D1 | The vault IS the architecture — label the parts | vaults | ~30m | Shared vocabulary |
| D2 | Reflection-with-citations for wiki promotion | vaults | design rule | Anti-fabrication |
| D3 | Dreams-style reorganize pass for `_state/` chapters | Storm Bear | ~1h | Dedup + supersession |
| E1 | Teach the taxonomy as a design-review vocabulary | Scrum | ~1h prep | Team literacy |
| E2 | "Memory or context?" triage question in refinement | Scrum | free | Cheaper designs |
| E3 | Vendor-claims literacy: mechanism vs product behavior | Scrum | ~30m | Better tech choices |
| F1 | Letta sandbox spike (sleep-time agents) | sandbox | ~2h | See the real thing |
| F2 | Watch-list: AutoDream / Dreaming V3 evals / Mem0-Zep | vault | ~10m | Cheap future option |
| F3 | Voice-screening agent memory spec (composes with jsm D2) | hireui | ~1h | Future feature seed |

---

## A — hireui Goal #2: the memory layer for the first LLM feature

*hireui has no LLM yet ([[project_hireui_no_llm_yet]]); the planned first features (candidate-feedback summarizer per the Mosh thread; voice screening per the JSM thread) all need a memory story. This block is the design work, reality-checked against how the vendors actually build memory.*

### A1 — Write hireui's memory-layer spec, files-first ⭐
Author `hireui/_bmad-output/runbooks/agent-memory-spec-<date>.md` mapping the four memories onto recruitment: **procedural** = the feature's system prompt + skills (versioned in repo); **semantic** = durable candidate/recruiter/org facts ("candidate C prefers remote", "role R closed") — stored as **structured rows/files, NOT a vector DB** (the Anthropic pattern; hireui already has Postgres); **episodic** = the interaction log (interviews, feedback, messages) hireui *already has* — the spec's job is deciding what the agent may read, not building new storage; **working memory** = the per-request context assembly budget. Include the substrate decision rule from `rag-vector-stores-and-context-limits`. Do it in the hireui repo under its CONSTITUTION (I-2 branch, .pilot-log).
**Success:** a reviewable spec that names each memory, its store, its consolidation trigger, and its retrieval path — before any code.

### A2 — Prototype candidate memory on the Anthropic memory tool ⭐
`memory_20250818` is GA — no beta header. Build the course-style chatbot seam (Mosh A2 vendor seam) + the memory tool with a per-candidate `/memories/<candidate_id>/` handler backed by hireui's own storage; path-traversal validation per the docs. Claude then reads/writes candidate memory files itself — zero retrieval infrastructure.
**Success:** a demo where session 2 knows what session 1 learned about a candidate, with the memory visible/auditable as plain text. GDPR note: memory files are personal data — deletion must cascade.

### A3 — Episodic log schema for recruiter–candidate interactions ⭐
Define the append-only event schema (who/what/when + free-text + importance score) for agent-visible history. Steal from Generative Agents: creation timestamp + last-access timestamp + LLM-rated importance 1–10.
**Success:** one table/collection the consolidation gate (A4) can consume.

### A4 — Two-stage consolidation gate: Haiku compresses, Opus curates
Implement the gate as a background job (NOT count-based): trigger = nightly timer (the claude.ai pattern) or importance-sum ≥ threshold (the GA pattern). Stage 1: Haiku 4.5 compresses the day's episodic events per candidate into digests. Stage 2: Opus curates digests into the semantic store with the three Dreams verbs — merge duplicates, supersede stale values, surface insights — each fact citing its source events (A5).
**Success:** semantic store stays small and current; token cost per candidate per day measured (composes with the claude-api-cost-optimization spec).

### A5 — Memory ops discipline: supersede-don't-append + citations
Design rule for A2/A4: consolidated facts must (1) replace superseded values rather than accumulate, (2) carry source-event IDs. Directly prevents Letta's two named failure modes (generic-and-lossy / overly-specific) and gives you an audit trail for GDPR/spec review.
**Success:** every fact in the semantic store answers "says who, when?"

### A6 — Memory evals before shipping
Extend the `evals/` harness (prompt-evaluation thread): seed a synthetic candidate history, run the agent across N sessions, probe recall ("what did the candidate say about relocation in session 1?"), tense-maintenance ("is the interview upcoming or done?" — the Dreaming-V3 problem class), and stale-fact supersession. Score with the grading discipline already piloted.
**Success:** a memory scorecard that runs in CI before the feature ships — the eval-first Goal #2 pattern.

### A7 — The defer-the-vector-DB memo
One page: vector search enters ONLY when (a) semantic store per scope exceeds what injection affords, or (b) cross-candidate similarity queries become a feature. Until then: files/rows + injection. Cite the census table (ChatGPT: injection; Anthropic: files; Letta archival: vectors).
**Success:** the team can say "no pgvector yet" with receipts — infrastructure deferred deliberately, not forgotten.

---

## B — Files-first discipline (portable design rules, zero install)

### B1 — The substrate decision rule as a one-page checklist ⭐
Post in hireui's docs + vault: **small + always-relevant → inject wholesale; curated + auditable → files; large + heterogeneous → vector RAG.** Per memory type, not per system.

### B2 — Profile vs collection split (LangMem's distinction)
For every semantic memory: is it a *profile* (one continuously-updated doc — inject it) or a *collection* (many items — retrieve top-k)? Candidate summary = profile; past feedback quotes = collection. Prevents the classic mistake of embedding a profile.

### B3 — Injection-over-retrieval for v1 (the ChatGPT pattern)
If a candidate's entire semantic memory is <2K tokens, skip retrieval entirely and inject it into every request — deterministic, cacheable (stable prefix → prompt-caching discount), debuggable. Add retrieval only when injection stops fitting.

### B4 — Budget to effective context, not advertised
Adopt 150–400K as the working assumption for "safe" context on 1M-class models (Chroma context-rot), and cite Lost-in-the-Middle for why key facts go at the top/bottom of assembled context. Applies to hireui prompts AND vault chapter budgets (<35K rule already encodes this instinct).

---

## C — Your own memory system (you already run this architecture)

### C1 — Name and tune your consolidation gate ⭐
Your `~/.claude` memory = semantic store; session transcripts = episodic log; `consolidate-memory` skill = explicit-trigger Dream; MEMORY.md 200-line budget = working-memory constraint. Pilot: run `/consolidate-memory` on a schedule (e.g., weekly or after every ~5 sessions — a real gate instead of ad-hoc), and after each run apply the two Letta failure-mode probes: are merged notes going generic? are one-off notes over-specific? Log one line per run.
**Success:** 3 consolidation runs with before/after MEMORY.md line counts + a kept/generic/lost tally.

### C2 — Importance scoring on memory writes
When saving a memory, rate importance 1–10 (Generative Agents) in the frontmatter description. Consolidation then has a triage signal: high-importance facts survive merges verbatim; low-importance ones are candidates for pruning.

### C3 — Complete the triad: transcripts as recall memory
You already have Letta-style "recall memory" — session transcripts searchable via the session-search tool. Convention: before writing a new memory about a recurring theme, search transcripts once — write the *pattern*, not the instance (that's episodic→semantic distillation done manually).

### C4 — Post-consolidation probes
After each `/consolidate-memory`: ask 3 recall questions whose answers you know live in memory ("what's the hireui branch policy?"). Miss = the consolidation was lossy; restore from git.

---

## D — The vaults (autopilot-research + Storm Bear ARE this architecture)

### D1 — Label the parts
Add a short section to the project CLAUDE.md mapping: `raw/` = episodic inbox; `wiki/` = semantic store; `loop-log/` = episodic run log; `skills/` = procedural; compile = the consolidation gate; `_master-index.md` = the always-injected dossier. Costs 30 minutes; gives every future session (and the Scrum talk, E1) precise shared vocabulary.

### D2 — Reflection-with-citations as the promotion rule
Generative Agents' insight-with-evidence-citations IS the wiki's source-provenance discipline — make it explicit for promotion: no claim enters Storm Bear's curated wiki without its episodic citations (raw file, URL, verdict). Already mostly true; writing it down makes it enforceable.

### D3 — A Dreams-style reorganize pass for `_state/`
The Storm Bear `_state/` chapters are consolidation output that has never been *re*-consolidated (the "03a filename out-of-date" item is a known symptom). Pilot one Dreams pass over a single chapter: merge duplicates, replace superseded values, surface insights — with a diff for operator review. (Respect the ask-before-editing rule: propose, don't auto-apply.)

---

## E — Scrum coaching / team practice

### E1 — Teach the taxonomy as design-review vocabulary
A 15-minute whiteboard (the video's own format, corrected): four memories + the gate + the substrate table. Teams reviewing AI features then ask crisp questions: "which memory is this?", "what's the consolidation trigger?", "why a vector DB and not files?"

### E2 — The "memory or context?" triage question
In refinement, when someone says "the agent should remember X": is X per-request context (assemble it), semantic memory (store + consolidate), or procedural (put it in the prompt/skill)? Most "memory" requests dissolve into context assembly — cheaper by an order of magnitude.

### E3 — Vendor-claims literacy exercise
Case study from this topic: the video's "this is how ChatGPT and Claude work" vs the teardowns/docs. Lesson for teams: product *behavior* (remembers me) ≠ *mechanism* (vector RAG) — verify mechanism claims against primary docs before copying an architecture.

---

## F — Sandbox / watch-list

### F1 — Letta sandbox spike
`letta-ai/letta` (Apache-2.0, 23.6K★) locally: one agent + sleeptime agent; watch core-memory blocks rewrite themselves. Best hands-on feel for dual-agent consolidation before building A4. Sandbox-vault only (I-8 governs hireui installs).

### F2 — Watch-list entries
(1) "AutoDream" in official Claude Code docs/changelog — if it ships, C1 becomes partially automatic; (2) independent Dreaming V3 evals; (3) Mem0/Zep-Graphiti — only if A7's conditions trigger; (4) RecMem / Anatomy-of-Agentic-Memory papers for the A4 design.

### F3 — Voice-screening memory spec
If the JSM-thread D2 voice-screening agent advances, its memory needs are exactly this topic: per-candidate semantic profile + per-call episodic log + post-call consolidation (a call IS a natural gate trigger — consolidate at hang-up). One page now saves a retrofit later.

---

## What to consciously SKIP (and why)

- **Skip building a vector database for hireui v1** — every production assistant-memory system examined (ChatGPT, all four Claude surfaces) ships without one; A7 documents the re-entry conditions.
- **Skip Mem0/Zep/OpenBrain-style hosted memory now** — same reasoning as claude-code-memory-systems D14: user-facing cross-tool memory is a later decision; don't outsource the layer that IS your product's moat (candidate data).
- **Skip count-based gates ("every 20 conversations")** — no production precedent; use timers, importance sums, or natural boundaries (call end, session end).
- **Skip re-piloting the operator-tooling methods** — the claude-code-memory-systems menu (A1 reorganize ritual, B5 semantic retrieval, etc.) already covers them; this menu is the builder-side complement.
- **Skip fine-tuning/memory-native RL** (Letta's research frontier) — years away from a two-person SaaS's needs.

## Critic's reframe (the contrarian read)

The consolidation gate is the video's hero, but the deep-dive's quiet lesson is the opposite end: **the best first memory system is no memory system** — hireui's episodic data already lives in Postgres, and a well-assembled context window (B3 injection + prompt caching) covers the v1 feature with zero new moving parts. Memory infrastructure earns its complexity only when sessions must *learn* across time. So the truly minimal pilot is: A1's spec concluding "v1 needs context assembly, not memory" — and that conclusion, written down with receipts, is itself the Goal #2 artifact. Also hold the skepticism symmetrically: this wiki's "files beat vectors" finding describes *assistant* memory at two vendors — if hireui's roadmap includes semantic candidate search (a real recruitment feature), the vector DB enters through the product door, not the memory door.

## Cross-links

- [[../wiki/agent-memory-architecture/_index]] — the topic this menu operationalizes
- [[../wiki/claude-code-memory-systems/_index]] + its 17-method menu — operator-tooling complement
- [[../wiki/mosh-ai-powered-apps/_index]] — the chatbot seam A2 builds on
- [[../wiki/ai-engineering/_index]] — Ch.6 memory in the demo→production frame
- [[../wiki/claude-api-cost-optimization/_index]] — caching + context economics for A4/B3
- [[../wiki/prompt-evaluation/_index]] — the eval harness A6 extends

## Suggested next action

Do A1 this week (~2h, zero install): write hireui's memory-layer spec files-first, ending with the explicit defer-the-vector-DB decision (A7 folded in). Then C1's first named consolidation run on your own memory. Together they cost an afternoon and produce both a Goal #2 artifact and a measured improvement to the system you use every day.
