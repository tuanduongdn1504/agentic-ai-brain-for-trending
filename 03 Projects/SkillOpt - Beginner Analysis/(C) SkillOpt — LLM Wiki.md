# (C) SkillOpt — LLM Wiki

> **Wiki ship v178** · built 2026-06-22 · branch `wiki/v178-skillopt`
> Subject: **`microsoft/SkillOpt`** — https://github.com/microsoft/SkillOpt
> Verdict: **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG
> Tier: **T2 Service** (self-hosted Python research tool / framework)
> Pattern outcome: **1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1)** — "Text-Space Skill Optimizer." Counts UNCHANGED **46 / 10**.

---

## 1. One-paragraph summary

**SkillOpt** is a Microsoft Research project: *"a text-space optimizer that trains reusable natural-language skills for frozen LLM agents through trajectory-driven edits, validation-gated updates, and deployable `best_skill.md` artifacts."* Its thesis, verbatim: **"Train agent skills like you train neural networks — with epochs, (mini-)batchsize, learning rates, and validation gates — but without touching model weights."** It treats **the skill document as the trainable state of a frozen agent** and improves it with a real training loop (rollout → reflect → edit → validate). A *separate optimizer model* turns scored rollouts into bounded **add / delete / replace** edits on a single skill doc, and **a candidate edit is accepted only when it strictly improves a held-out validation score**. The output is a deployable `best_skill.md` (≈300–2,000 tokens) that runs against the **unchanged** target model with **zero inference-time overhead**.

This is the corpus's **first systematic *optimizer* for agent skills** — distinct from every prior skill subject, which either *authors*, *standardizes*, *scans*, or *loosely self-revises* skills. SkillOpt brings deep-learning optimization discipline (held-out validation, learning-rate budgets, meta-updates) to the natural-language artifact that drives a coding agent.

---

## 2. What it is, precisely

| Field | Value | Provenance |
|---|---|---|
| Repo | `microsoft/SkillOpt` | repo page |
| Tagline | "a text-space optimizer that trains reusable natural-language skills for frozen LLM agents…" | repo description (verbatim) |
| README hook | "Train agent skills like you train neural networks … but without touching model weights." | README (verbatim) |
| Paper | *"SkillOpt: Executive Strategy for Self-Evolving Agent Skills"*, Yang et al. (2026), **arXiv 2605.23904** | README BibTeX + Microsoft Research publication page + HuggingFace papers |
| Author | **Microsoft** (a Microsoft Research project) | repo / MS Research page |
| License | **MIT** | repo page |
| Languages | **Python 86.6% / HTML 12.2% / Shell 1.2%** | repo page (page-stated) |
| Distribution | **PyPI** — `pip install skillopt` | README |
| Version | **v0.1.0** (June 2, 2026), **1 release** | repo page (page-stated, §37.4) |
| Stars / forks | **8.6k ★ / 828 forks** | repo page (page-stated, NOT API-verified — §37.4) |
| Related projects (MS) | `gbrain`, `gbrain-evals`, `darwin-skill` | README |

**What "agent skill" means here:** a compact natural-language **skill document** (the SKILL.md / Claude-Skills-style artifact) that instructs a frozen model how to do a task — *not* model weights, *not* a fine-tune. SkillOpt optimizes that document.

---

## 3. How it works — the training-loop-in-text-space

SkillOpt borrows the *shape* of neural-network training but operates entirely in **text space**:

```
        ┌──────────────────────────────────────────────────────────┐
        │  SKILL DOCUMENT  (the "trainable state", best_skill.md)    │
        └──────────────────────────────────────────────────────────┘
                 ▲                                          │
                 │  bounded add/delete/replace edits        │  used by
                 │  (gated by a textual learning-rate       ▼
                 │   budget)                         ┌──────────────┐
        ┌────────────────┐   scored rollouts        │ FROZEN target │
        │ OPTIMIZER model │◀─────────────────────────│ model (Claude/│
        │ (proposes edits)│                          │ GPT-5.5/…)    │
        └────────────────┘                           └──────────────┘
                 │                                          │
                 │  accept edit ONLY IF                     │ runs the task,
                 ▼  held-out validation score improves      ▼ produces trajectories
        ┌────────────────────────────────────────────────────────────┐
        │  rollout  →  reflect  →  edit  →  VALIDATE (held-out gate)    │
        │  + rejected-edit buffer  + epoch-wise slow/meta update       │
        └────────────────────────────────────────────────────────────┘
```

**The deep-learning vocabulary, mapped to text:**

| Neural-net concept | SkillOpt's text-space analogue |
|---|---|
| Trainable weights | The natural-language **skill document** |
| Gradient step | A bounded **add / delete / replace** edit to the doc, proposed by an *optimizer model* from scored rollouts |
| Learning rate | A **textual learning-rate budget** controlling edit magnitude |
| Epochs / batch / mini-batch | Epoch-wise iteration over task batches |
| Validation set / early stopping | A **held-out validation gate** — an edit is *accepted only when it strictly improves* the held-out score |
| Optimizer state / momentum | A **rejected-edit buffer** (remembers failed edits) + an **epoch-wise slow / meta update** for stability |
| Frozen backbone | The **target model is never touched** — no weight updates |
| Inference cost of the trained artifact | **Zero inference-time overhead** — the skill doc adds no extra model calls at deploy time |

The crucial discipline is the **validation gate**: this is what separates SkillOpt from "let an LLM rewrite its own prompt and hope it's better." Edits that don't *measurably* improve held-out performance are rejected. That's the single most important design choice and the source of the corpus-first novelty (§6).

---

## 4. Where it runs — models, harnesses, benchmarks

- **Target models (7):** OpenAI, Azure, **Claude**, Qwen, MiniMax, **GPT-5.5**, Codex. *(GPT-5.5 is the headline benchmark target; **Claude is a first-class supported backend**.)*
- **Execution harnesses (3):** Direct chat · **Codex CLI** (Codex exec) · **Claude Code CLI** (Claude Code exec).
- **Benchmarks (6 built-in):** referenced as "six benchmarks" (not individually enumerated in the README excerpt).
- **WebUI dashboard:** the HTML 12.2% — a monitoring dashboard for training runs.

**Headline quantified claim (Microsoft's own numbers, page-stated, unreplicated):**
> "Across **six benchmarks, seven target models, and three execution harnesses**, SkillOpt is **best or tied-best on all 52 evaluated (model, benchmark, harness) cells**, and on GPT-5.5 lifts the average no-skill accuracy by **+23.5 points in direct chat, +24.8 inside the Codex agentic loop, and +19.1 inside Claude Code**."

⚠️ These are the authors' own benchmarks — treat as page-stated and unreplicated (Library-vocab #20 *Token-Economy-Quantification* QUALIFIED-ADJACENT; see §7).

---

## 5. The verdict (routine v2.6, §31 2-tier INCLUDE keyed on (b))

**GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.**

### (a) Anthropic / cultural-peer axis — **FAIL (clean, no axis)**
Microsoft is a major US corporation / research lab, not Anthropic ((a)-7 is Anthropic-only), and not the individual cultural-peer axis. This is a **declared-non-Anthropic-institution** — the same situation as Google v140 / ByteDance v143 / NVIDIA v169 / OpenBMB v175 / Kilo AI v177. No heritage rescue (the v159→v177 discipline + standing rec (ii)).

⚠️ **Microsoft is a RETURNING corpus author, NOT corpus-first** (verified by collision grep): **`markitdown` v28** (`microsoft/markitdown`, T4 corporate-narrow-utility) and **`spec-kit` v17** (`github/spec-kit` — GitHub is Microsoft-owned, "corporate-official") both precede it. SkillOpt is plausibly the first **Microsoft *Research*** subject and the first Microsoft *agent-skills* subject, but that is a thin sub-distinction — recorded as a **#19 19a returning-institution data-point**, NOT a new (a) axis and NOT a corpus-first claim.

### (b) Goal-relevance — **STRONG (this keys the tier)**
Main goal: *"Master Claude and autonomous agents for software development."* SkillOpt sits **dead-center on the agent-skills substrate**:
- It optimizes **agent skills** — the *exact* artifact this vault produces in `05 Skills/` (SKILL.md documents). The vault's whole operating model is "skill files driving a coding agent"; SkillOpt is a principled way to *improve* those documents.
- It **runs on Claude** (first-class target model) and **Claude Code CLI** (one of 3 harnesses; +19.1-point lift reported inside Claude Code).
- It is a **methodology + tool**, directly pilotable into the vault's own skills (optimize a routine skill against a held-out validation set).

**STRONG-not-STRONGEST**, because: it's Microsoft Research (third-party / competitor lab); it's multi-model with **GPT-5.5 as the headline target** (Claude is one backend among seven); and Goal #1 centers Claude *specifically*. This is a **clear tier above GLM-5 v176's (b) MODERATE** (a raw competitor model with "nothing to pilot but swap the backend") — SkillOpt is an applicable tool *operating on the vault's own substrate*. GOAL-ALIGNED is unambiguous here.

### (c) Engineering substance — **STRONG**
A real optimizer engine, not a wrapper: rollout→reflect→edit→validate loop, textual learning-rate budget, rejected-edit buffer, epoch-wise slow/meta update, held-out validation gates, bounded add/delete/replace edits, **6 benchmarks × 7 target models × 3 harnesses**, a WebUI dashboard, a PyPI package, and a backing **arXiv paper**. Python-primary (86.6%). **Caveat: young** — v0.1.0, 1 release, ~3 weeks old at fetch.

### (d) Cross-reference density — **STRONG**
Lands on the **agent-skills cluster** (SkillSpector v169 / ponytail v168 / agent-skills-standard v76 / book-to-skill v137 / Odysseus v136 / nature-skills v119 / the Anthropic `skill-creator`); the provider-agnostic axis (#84 84c); the optimizer-research lineage it *contrasts with* (#43); and the quantified-claim track (Library-vocab #20).

---

## 6. Pattern outcome — 1 NEW §C standalone (CORPUS-FIRST, N=1)

**MINT:** *"Text-Space Skill Optimizer — Training-Loop Optimization of a Frozen Agent's Natural-Language Skill Document via Validation-Gated Edits"* (skill doc as trainable state; rollout→reflect→edit→validate; bounded add/delete/replace; textual learning-rate; **held-out validation gate**; deployable `best_skill.md`; zero inference-time overhead).

**Why it's corpus-first.** Every prior corpus subject that touches "skills" does something *other* than optimize them with a validation-gated training loop:

| Prior subject | What it does to skills | Why SkillOpt is distinct |
|---|---|---|
| **Odysseus v136** | "self-evolving SKILL.md" (Hermes-lineage) | **Closest neighbor — and the precise foil.** SkillOpt's own motivation contrasts itself against *"evolved through loosely controlled self-revision."* Odysseus = loosely-controlled self-revision; SkillOpt = the **disciplined training-loop version with a held-out validation gate** that *rejects* non-improving edits. |
| **SkillSpector v169** | defensive-security **scanner** (vets a skill before install) | Scans for *safety*, doesn't optimize *quality*. Opposite job. |
| **ponytail v168** | hand-authored behavior **ruleset** (code-minimalism) | A fixed, human-written skill — not an optimizer that learns one. |
| **agent-skills-standard v76** | a **standard / codification** | Defines the format; doesn't improve a document's task performance. |
| **book-to-skill v137 / skill-creator** | **authoring / generation** ("one-shot by a strong LLM") | The exact baselines SkillOpt's motivation calls out as *not* behaving "like a deep-learning optimizer for the skill itself." |
| **Pattern #43 Optimizer-Research Integration Velocity** (LlamaFactory v22 / Unsloth) | integrates **weight-space** optimizers (GaLore, RL methods, quantization) into training-INFRA | **Opposite space.** SkillOpt touches **no weights** — it optimizes a text document. NOT a #43 instance. |

The defining axis = the **conjunction**: (text-space, no weight updates) × (a *training loop* with epochs / learning-rate / batches) × (a *held-out validation gate* that accepts edits only on measured improvement) × (a deployable zero-overhead `best_skill.md` artifact). Two of those — the *validation-gated* discipline and the *trainable-skill-document* framing — are each corpus-first.

- **§28 discipline:** 1 new standalone (≤2-per-wiki cap honored). **PROMOTION-ELIGIBLE at N=2** (a second validation-gated skill optimizer).
- **NOT a new top-level pattern** (max stays **#85**; the same anti-inflation that rejected #86/#88 at v168 — a single N=1 novel capability is a §C standalone, not a top-level pattern).

---

## 7. Secondary observations (NOT minted)

- **#19 19a — returning-institution data-point.** First Microsoft *Research* / Microsoft *agent-skills* subject, but Microsoft has authored corpus subjects before (markitdown v28, spec-kit v17). Bookkeeping only.
- **#84 84c — provider-agnostic-by-design** (7 target models × 3 harnesses; the optimized skill *transfers across model scales and harnesses*). LLM-agnostic. **NO N-bump** (per v86). **Explicitly NOT** the v168 ponytail "14-platform native-rule-file distribution" mechanism — SkillOpt optimizes a *single* skill doc and transfers it; it doesn't distribute rule files into many clients.
- **Library-vocab #20 Token-Economy-Quantification — QUALIFIED-ADJACENT.** The +23.5 / +24.8 / +19.1 lifts and "52/52 cells best-or-tied" are the authors' own benchmarks, page-stated and unreplicated → **N stays 4, bump deferred** (the v168 / v172 / v175 precedent).
- **#18 adjacency** (multi-backend). Closer to #84 84c than to #18 B1-MCP; SkillOpt is not an MCP server.
- **Agent-skills quality / safety / authoring cluster cross-reference** — SkillOpt is the **optimize** vertex of a forming quadrant: *author* (book-to-skill v137 / skill-creator) → *standardize* (agent-skills-standard v76) → *scan/secure* (SkillSpector v169) → **optimize (SkillOpt v178)**.

---

## 8. Non-claims (honest negatives)

- **NOT corpus-first Microsoft** — markitdown v28, spec-kit v17 precede it.
- **NOT Pattern #52** (viral velocity) — 8.6k★ / 828 forks / v0.1.0 / 1 release are **page-stated, NOT API-verified** (§37.4) → velocity unestablishable. *(8.6k★ on a ~3-week-old repo is suggestive, but the routine cannot make a #52 claim on mocked-API metrics.)*
- **NOT Pattern #57** (corpus-recursive) — it uses Claude Code / Codex as **execution harnesses it optimizes against** (clients/targets), not influences it cites; the integrated `gbrain` / `gbrain-evals` / `darwin-skill` are Microsoft's own related projects, not corpus subjects. Mentions ≠ recursion (the v172/v173/v174 discipline).
- **NOT Pattern #43** — weight-space optimizer-research in training-infra; SkillOpt is text-space, no weights.
- **NOT a new top-level pattern** (max #85).
- **NOT #18 B1-MCP** (not an MCP server).

---

## 9. §37 fact-provenance

| Fact | Provenance |
|---|---|
| Tagline / README hook / training-loop mechanism / target models / harnesses / `best_skill.md` / zero-overhead | **STATED** (github.com/microsoft/SkillOpt repo page + raw README, as of 2026-06) — verified by 2× WebFetch |
| Paper title / authors / arXiv 2605.23904 / "Executive Strategy for Self-Evolving Agent Skills" | **STATED / MEDIUM** (README BibTeX + Microsoft Research publication page + HuggingFace papers — independently surfaced via WebSearch) |
| Languages 86.6/12.2/1.2 · MIT · v0.1.0 (Jun 2 2026) · PyPI `pip install skillopt` | **STATED** (repo page) |
| 8.6k★ / 828 forks / 1 release | **PAGE-STATED, NOT API-VERIFIED** (§37.4 — GitHub API is mocked) → NOT a #52 claim |
| Benchmark lifts (+23.5 / +24.8 / +19.1) and 52/52 cells | **AUTHORS' OWN, UNREPLICATED** numbers |
| Microsoft is a returning author (markitdown v28 / spec-kit v17) | **VERIFIED** by collision grep over `_state/*.md` |
| Text-space skill optimizer is corpus-first | **VERIFIED** by collision grep over `_patterns/*.md` (no prior optimizer/DSPy/TextGrad/validation-gate standalone; #43 is weight-space) |

---

## 10. Pilot note

**On-goal and genuinely pilotable** — SkillOpt could optimize **this vault's own skill documents** (e.g., a routine skill or a project SKILL.md) against a held-out validation set, with Claude / Claude Code as the harness. It's a **methodology/capability pilot** in the spirit of ponytail v168 (it changes how the vault's skills *perform*), not a read-only observer.

**Setup cost is non-trivial**, though: it needs an *optimizer model* + a *target model* + a *benchmark / held-out validation set* to run — more than a one-command install. And it's Microsoft-authored with GPT-5.5 as the headline target (Claude is one of three harnesses).

**Fence:** `install-snapshot` + `npm-security-check`-equivalent inspection of the **PyPI** package before `pip install skillopt` + a **scratch skill + small validation set** first + run with the **Claude Code** harness + **pin v0.1.0** (1 release, young).

**Ladder placement:** a strong *capability/methodology* pilot, but heavier setup than the read-only SkillSpector v169 (which stays the lowest-risk first pilot). Slots in alongside the on-goal methodology pilots (ponytail v168), behind the lightweight read-only ones (SkillSpector v169 first; claude-tap v173 second).

---

## 11. Bottom line

A clean, high-quality, **on-goal** ship. SkillOpt is the corpus's first *optimizer* for agent skills — it brings held-out-validation discipline to the natural-language artifact that drives a coding agent, treating the skill document as trainable state and refusing edits that don't measurably help. The load-bearing call is the **1 new §C standalone** ("Text-Space Skill Optimizer," CORPUS-FIRST, N=1), cleanly distinct from the *author / standardize / scan / loosely-self-revise* skill subjects that came before — and explicitly distinct from the **weight-space** optimizer-research of Pattern #43. (a) FAILs honestly (returning Microsoft author, not corpus-first), so the INCLUDE rests on (b)(c)(d). Counts unchanged **46 / 10**; §C surface ≈34 → ≈35; streak **GA:40** (25 consecutive goal-aligned ships v153→v178, GA reading).

**Suggested next action:** review + merge the wiki branch chain — `wiki/v178-skillopt` sits on `wiki/v177-kilocode`, itself on the unmerged v176→v168 chain; merging v178 brings the whole cumulative state along. Then, on the standing PILOT lever: SkillOpt is a natural **methodology pilot** — once SkillSpector v169 (`--no-llm`, read-only) has proven the loop, point SkillOpt at one real vault skill with a small held-out set and measure whether validation-gated edits beat the hand-authored version.
