# (C) OpenMontage — Pilot Methods Menu (24 ways to apply it)

> **Your ask:** *"pilot to apply knowledge into my working flow, show me many methods for my apply."*
> **The honest framing first.** OpenMontage is a **video-production** system, so it does **not** directly advance your software goal *as a video tool*. Its real value for you is that it's a working, 30.3k★ **reference implementation of agent-first engineering** — and *those patterns steal directly into your Claude Code / vault / hireui workflow*. So this menu is deliberately weighted: **Group B (steal the patterns) is the on-goal gold**; Groups A/C/D are supporting.
>
> **Fence (applies to anything that installs or spends):** `install-snapshot` first · inspect `Makefile` + `.env.example` before `make setup` · run on a **scratch machine/dir** · start on the **$0 free/local path** (Piper + free stock + Remotion + FFmpeg) or in **`CAP` budget mode with a low cap + provider-side spend limits** · **never** `--dangerously-skip-permissions` · **AGPL-3.0 is a blocker for any hireui *productization*** (fine for internal demos/marketing + pattern-stealing) · on hireui follow its CONSTITUTION (I-8 operator-installs, I-2 `agent-*` branch, GitNexus-first) · **pin commit `1188e1b`**.

---

## Group A — Read & learn (zero-risk, do this first) — ~1–2h, no install

| # | Method | What you do | Advances |
|---|---|---|---|
| **A1** | **Read the architecture spine** | Read `README.md` → `PROJECT_CONTEXT.md` → `AGENT_GUIDE.md` (688 lines) → `docs/ARCHITECTURE.md`. Internalize the one idea: *the coding agent is the runtime; intelligence lives in Markdown skills + YAML manifests; code does only deterministic offload + schema + state.* | Goal #1 (understand agent-first design) |
| **A2** | **Read the two meta-skills** | `skills/meta/reviewer.md` (CHAI + slideshow-risk scoring) + `skills/meta/checkpoint-protocol.md` (resume + approval gates). These are the transferable quality machinery. | Goal #1; agent-skills thread |
| **A3** | **Read one pipeline end-to-end** | Open `pipeline_defs/animated-explainer.yaml` + its `skills/pipelines/explainer/*-director.md` set. See how a YAML manifest routes stage→skill→tool→checkpoint with `required_tools` / `success_criteria` / `checkpoint_required`. | Goal #1; multi-agent-orchestration |
| **A4** | **Read the craft skills** | `skills/creative/storytelling.md`, `skills/core/color-grading.md`, `skills/creative/screen-recording.md`, `skills/core/subtitle-sync.md`. Harvest the durable knowledge (Muller misconception-first, Mayer segmenting, Murch hierarchy, 150–160 WPM, screen-demo craft). | Personal/vault knowledge |

---

## Group B — Steal the agent-engineering patterns (Goal #1 — THE GOLD) — the real payoff

Each row = a mechanic in OpenMontage you re-implement (by hand, no install) in your **vault** and/or **hireui** Claude Code workflow.

| # | Pattern (source) | How you apply it | Advances |
|---|---|---|---|
| **B1** | **YAML-pipeline-as-workflow-spec** (`pipeline_defs/*.yaml`) | Write a `workflow.yaml` for a real hireui flow (e.g. `spec → plan → build → review → verify → ship`) with per-stage `required_tools` / `success_criteria` / `checkpoint_required` / `human_approval`. Your Claude Code reads it as the orchestration spec instead of you re-explaining the flow each time. Composes with your existing **cc-sdd** + **how-we-Claude-Code** threads. | multi-agent-orchestration; **Goal #2 (hireui)** |
| **B2** | **Agent-first split** (intelligence in MD/YAML, code = deterministic only) | Audit your vault + hireui harness: move creative/policy logic into readable skills/manifests; keep code to schema-validation + state. This is *literally your LLM-Wiki pattern generalized* — a strong validation that your approach is state-of-the-art. | Goal #1; CC-memory-systems |
| **B3** | **Deterministic-tool-offload contract** (`tools/base_tool.py`) | Adopt the `BaseTool` contract idea for hireui's own agent tools: uniform metadata (name / cost_estimate / runtime / determinism / `fallback_tools` / `agent_skills`) + a `ToolResult` (`success / data / cost_usd / duration`). Lets the agent orchestrate safely without trusting tool names. The ai-berkshire v187 `financial_rigor.py` offload, generalized. | Goal #1/#2 |
| **B4** | **Reviewer meta-skill + CHAI + scored gate** (`skills/meta/reviewer.md`) | Port the *shape*: a `code-review.md` skill that produces **A**ccurate (cite exact file:line) / **C**omplete (pattern-scan the class) / Constructive (propose a fix or downgrade to "investigation") findings, with a scored rubric + a **fail/revise threshold** (their slideshow-risk 6-dim / ≥4.0-fail model → your own dimensions: correctness / security / perf / maintainability). | Goal #1/#2; agent-skills; prompt-eval |
| **B5** | **Decision-log with `options_considered`** (`decision_log.schema.json`) | For every material agent choice in hireui, log `{options_considered:[{label,score,reason,rejected_because}], selected, reason, confidence}`. It's ADRs-for-agents — forces deliberate, auditable decisions. Wire it into your `.pilot-log`. | Goal #2; observability |
| **B6** | **Estimate→reserve→reconcile budget guard** (`cost_tracker.py`) | Build the 3-phase cost lifecycle into any expensive hireui/vault agent loop: estimate all downstream calls → reserve + approval-gate at a per-action threshold → reconcile actual spend; modes observe/warn/cap. Directly advances your **claude-api-cost-optimization** spec (hireui has no LLM yet → build-it-right). | **claude-api-cost-optimization**; Goal #2 |
| **B7** | **Checkpoint / resume primitive** (`checkpoint-protocol.md`) | Persist stage artifacts as JSON with `status: in_progress` + `partial_progress` (`completed_ids`) so a long hireui agent run resumes without redoing work — and gates on human approval at creative stages. | multi-agent-orchestration; Goal #2 |
| **B8** | **framework-smoke CI harness** (`framework-smoke.yaml` + `test_phase0_contracts.py`) | Add a minimal **no-execution** contract test to your own YAML-driven harness (or hireui's BMAD): validate manifest/schema/checkpoint mechanics *without* running expensive tools. Cheap, fast, catches contract breakage early. | Goal #2; prompt-eval |
| **B9** | **Cross-harness thin-pointer distribution** (`CLAUDE.md`/`CURSOR.md`/… → `AGENT_GUIDE.md`) | Consolidate your per-harness rule files into thin pointers delegating to ONE shared guide (you already run this vault on `CLAUDE.md`; add `AGENTS.md` as the portable superset per your Antigravity/open-design threads). **#84 84c** in practice — but add the drift-check they lack (a test that each pointer references the shared guide). | Goal #1; agent-skills |
| **B10** | **Scored 7-dimension provider selector** (the Selector Pattern) | For any multi-vendor choice in hireui (OCR / embedding / model routing), score providers across weighted dimensions + log the decision — no hardcoded chains, no silent defaults. Pairs with **cc-switch**-style backend routing. | claude-api-cost-optimization; Goal #2 |

---

## Group C — Actually make video (domain-transfer; off the software goal but genuinely usable) — needs install

| # | Method | What you do | Advances |
|---|---|---|---|
| **C1** | **$0 free/local smoke test** | Scratch machine → `make setup` (inspect first) → run a short piece on the **free path** (Piper TTS + Remotion + FFmpeg, no paid keys). Prove the agent-first loop end-to-end at zero spend. | Understand-by-doing |
| **C2** | **hireui product-demo video** | Use the **`screen-demo`** pipeline (+ the screen-recording craft: 4K→1080p, cursor highlight, 1.5–2× code zoom, silence-removal) to produce a polished hireui/TalentAxis walkthrough. A *real* marketing artifact from your real product. | Goal #2 (adjacent — marketing) |
| **C3** | **Explain your own LLM-Wiki method** | Feed the `animated-explainer` pipeline a brief on Karpathy's LLM-Wiki pattern (your vault's thesis) → a short explainer, using misconception-first structure. Dogfoods the craft + markets your method. | Vault/personal |
| **C4** | **Real-footage documentary path** | Try `documentary-montage` (BETA): build a CLIP corpus from Archive.org/NASA/Wikimedia → retrieve real clips → compose. Shows the retrieve-then-compose pattern (see B-adjacent D2) on real assets, $0. | Understand retrieval-first |
| **C5** | **Localization / dub** | `localization-dub` pipeline for a VN-language version of a demo (your locale) — WhisperX word-level subs + TTS. | Personal/marketing |
| **C6** | **Cost-anchor experiment** | Reproduce one paid demo (e.g. a $0.15 FLUX+Remotion short) with provider-side caps; compare actual vs estimated spend to calibrate the budget-guard you built in **B6**. | claude-api-cost-optimization |

---

## Group D — Vault-meta & craft knowledge (zero-risk)

| # | Method | What you do | Advances |
|---|---|---|---|
| **D1** | **Adopt CHAI review criteria in the vault** | Fold Accurate/Complete/Constructive into your own review discipline + your `feedback_wiki_verify` rule — findings must cite the exact artifact and propose a fix or downgrade to "investigation." | Vault quality |
| **D2** | **Retrieve-then-compose as a RAG lens** | Note the pattern (build a corpus → semantic-retrieve real assets → compose from real material, not generate-from-scratch) as a design principle for hireui RAG features + the vault's own memory/GitNexus retrieval. | Goal #2; CC-memory |
| **D3** | **Apply the craft to any content you ship** | Use misconception-first + Mayer segmenting + Murch's emotion>story>rhythm hierarchy + 150–160 WPM whenever you make a talk, README, or demo. Tool-independent, durable. | Personal |
| **D4** | **Log OpenMontage as the media-production reference** | It's the corpus's first **Agent-First Generative-Media Production System** (§C mint N=1); revisit if you ever need agentic media generation, and watch the class for a 2nd instance. | Vault/corpus |

---

## Recommended ladder (blunt)

1. **A1 → A2 → A3** (read the architecture + meta-skills + one pipeline) — ~1–2h, zero risk. You'll immediately recognize your own LLM-Wiki pattern reflected back at industrial scale.
2. **B1 + B6** — the two highest-leverage steals: a `workflow.yaml` orchestration spec for a real hireui flow, and the estimate→reserve→reconcile **budget guard** wired into your `claude-api-cost-optimization` spec (hireui has no LLM yet → build it right). Do these on an `agent-*` branch = a concrete **Goal-#2 pilot artifact** (still zero completed pilots since v153).
3. **B4 + B5 + B8** — a 4-dimension code-review meta-skill with a scored gate + a decision-log + a framework-smoke contract test. This is the "senior-engineering discipline as agent skills" layer, complementing your **agent-skills v184** thread.
4. *Optional, off-goal:* **C1 → C2** — free smoke test, then a real hireui product-demo video (a usable marketing artifact).

**Do NOT** pilot the paid video generation against real-money accounts without provider-side caps, and **do NOT** productize OpenMontage inside hireui (AGPL-3.0). The value for you is the **architecture**, not the pixels.
