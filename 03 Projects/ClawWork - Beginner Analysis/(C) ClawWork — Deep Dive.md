# (C) ClawWork — Deep Dive

**Subject:** `HKUDS/ClawWork` · **Wiki v233** · built 2026-08-17
**Repo description (verbatim):** *"ClawWork: OpenClaw as Your AI Coworker - 💰 $15K earned in 11 Hours"*
**License:** MIT · **Language:** Python · **Author:** HKUDS = **Data Intelligence Lab @ The University of Hong Kong** (PI **Chao Huang**) — **NOT Anthropic**

> ⚠️ **Source-verification note:** this wiki was built from the rendered repo page, raw README, the directory tree, `requirements.txt`, `clawmode_integration/README.md`, `skill/SKILL.md`, `livebench/agent/economic_tracker.py`, `livebench/work/evaluator.py`, `livebench/work/llm_evaluator.py`, the `configs/` listing, and the commit history — **NOT source-cloned**. Metrics are **page-stated** (§37.4: the GitHub API is mocked in this environment) → **no Pattern #52 velocity claim**.

---

## 1. What it actually is, in one paragraph

ClawWork is a **live economic benchmark** in which LLM agents must *earn a living*. Each agent starts with **$10**, is assigned **one real professional task per day** drawn from **OpenAI's GDPval** dataset, and must **pay for its own tokens out of that same balance**. Completed work is graded by an LLM judge against occupation-specific rubrics; the agent is paid `quality_score × (estimated_hours × BLS_hourly_wage)`. If the balance hits **$0 the agent is bankrupt** — the run is over. A React dashboard streams balance and task events live, and a public leaderboard ranks models by final balance. Bolted alongside is **ClawMode**, a wrapper that turns a live **nanobot** chat gateway into the same economically-accountable agent across nine consumer chat channels.

The thesis, in the repo's own words, is that this measures *"what truly matters in production environments: work quality, cost efficiency, and long-term survival."*

**The one genuinely sharp idea:** in almost every agent benchmark, the cost of *thinking* is externalised — someone else pays the API bill and the score ignores it. ClawWork makes **token cost endogenous to the objective function**. An agent that reasons beautifully but expensively goes broke. That single inversion is the reason this repo is worth reading.

---

## 2. The economic loop (source-verified)

| Rule | Value |
|---|---|
| Starting balance | **$10.00** |
| Token cost | deducted from balance after every LLM call |
| Task cadence | one GDPval task per simulated day |
| Daily choice | **work** (earn now) **or learn** (invest in future capability, no income) |
| Payment formula | `Payment = quality_score × (estimated_hours × BLS_hourly_wage)` |
| Task value range | **$82.78 – $5,004.00** (avg **$259.45**) |
| Payment gate | evaluation score must exceed `min_evaluation_threshold` (**default 0.6**) |
| Bankruptcy | `is_bankrupt()` → `True` when `current_balance <= 0` |

**Survival states** (`economic_tracker.py`, verbatim logic):

```
"bankrupt"   if balance <= 0
"struggling" if balance < 100
"stable"     if balance < 500
"thriving"   otherwise
```

The shipped `SKILL.md` turns these into agent policy: *thriving* → buy learning; *struggling* → take any work; *bankrupt* → system failure. Agents operate on a **15-iteration budget** and are told to submit by iteration 10–12 to avoid timeout.

---

## 3. The benchmark data: OpenAI's GDPval (verified independently)

- **GDPval** is **OpenAI's** benchmark (arXiv **2510.04374**, released **October 2025**).
- Full set: **1,320 tasks** across **44 occupations** drawn from the **top 9 US-GDP industries**; tasks are real work deliverables (legal briefs, engineering blueprints, nursing care plans, spreadsheets, decks) authored by professionals averaging ~14 years' experience.
- **220 tasks were open-sourced as the "gold subset"** on HuggingFace.

ClawWork uses **exactly that 220-task gold subset**, re-bucketed into four domains (Technology & Engineering · Business & Finance · Healthcare & Social Services · Legal/Media/Operations).

⚠️ **Terminology slip in ClawWork's own framing:** the README repeatedly says *"44 economic sectors."* GDPval is **44 occupations across 9 sectors**. Occupations ≠ sectors. Minor, but it is the kind of drift worth recording.

---

## 4. Architecture (as verified)

```
ClawWork/
├── livebench/              # the benchmark engine
│   ├── agent/              # live_agent.py, economic_tracker.py
│   ├── work/               # task_manager.py, evaluator.py, llm_evaluator.py
│   ├── tools/              # tool_livebench.py, start_live_services.py (MCP server)
│   ├── configs/            # 18 per-model run configs
│   ├── prompts/  scheduler/  api/  data/  utils/
│   ├── langchain_mcp_adapters/
│   └── trading/            # ⚠️ contains only __init__.py — vestigial scaffolding
├── clawmode_integration/   # the nanobot product wrapper
├── eval/                   # meta_prompts/ — per-occupation rubrics
├── frontend/               # React dashboard
├── scripts/  assets/  .github/workflows/
└── requirements.txt  setup.py  start_dashboard.sh  run_test_agent.sh
```

**Stack** (from `requirements.txt`): FastAPI + uvicorn + websockets · **`fastmcp`** (commented *"MCP support (required for tools)"*) · LangChain + **`langchain-openai`** + `langchain-mcp-adapters` + **LangGraph** · pandas/pyarrow · **`boxlite` (default) + `e2b-code-interpreter` (fallback)** sandboxes · `tavily-python` search · and a full document-production stack: **`python-docx`, `python-pptx`, `reportlab`, `openpyxl`, `xlsxwriter`, `pdf2image`, `Pillow`**.

That last group is not incidental — **GDPval deliverables *are* Office documents**, so the benchmark needs an agent that can actually produce .docx/.xlsx/.pptx/PDF artifacts. (Direct cross-reference to **OfficeCLI v206**, the corpus's agent-first Office-document capability layer.)

**Agent tool surface (8):** `decide_activity`, `submit_work`, `learn`, `get_status`, `search_web`, `create_file`, `execute_code_sandbox`, `create_video`. These are exposed to agents over an **MCP server** (`tools/start_live_services.py`) — MCP used here as an *internal tool bus* for the benchmark's own agents.

### 4.1 `EconomicTracker` — 876 lines
Real accounting: per-task and per-channel cost records (LLM / search / OCR / other), flat-rate API tracking (`track_flat_api_call()` for e.g. Tavily), and three JSONL ledgers — `balance.jsonl`, `token_costs.jsonl`, `task_completions.jsonl`.

🔴 **The most important caveat in the whole repo.** Pricing is **hardcoded and universal**:

```python
input_token_price: float = 2.5,    # per 1M tokens
output_token_price: float = 10.0,  # per 1M tokens
```

There is **no model-specific price table**. Unless an OpenRouter response supplies a pre-computed `cost`, *every model is billed at the same rate*. That means the leaderboard's **"Cost" column is substantially a measure of token volume, not of real vendor pricing** — and since the runs are a mix of "thirdparty" and "openrouter" configs, the column is not even internally consistent. **The headline claim of the project is cost efficiency, and the cost axis is its weakest link.**

### 4.2 The evaluator — 237-line `WorkEvaluator` → 829-line `LLMEvaluator`
Genuinely careful for a research harness:
- Per-occupation rubrics loaded from `eval/meta_prompts/{normalized}.json`; **missing rubric → `FileNotFoundError`, no fallback**.
- *"use_llm_evaluation must be True. Heuristic evaluation is no longer supported."* — no silent degradation.
- Anti-gaming: artifact must exist and be non-empty; **files >2MB rejected**; extraction errors raise rather than proceed.
- `payment = normalized_score * max_payment`.

⚠️ **Doc-vs-code drift:** the README advertises **GPT-5.2** as the judge; the code default is **`"gpt-4o"`**, overridable via `EVALUATION_MODEL`. Both can be true (the leaderboard runs presumably set the env var) but the shipped default is the older model.

### 4.3 ClawMode — the product half
Wraps a **nanobot** gateway so a live chat agent becomes economically accountable:
- `TrackedProvider` intercepts every `chat()` call and feeds litellm's real token counts into `EconomicTracker`; responses get a **balance footer**.
- `/clawwork <instruction>` from any channel assigns a *paid* task: classify into one of **40 occupations** → estimate hours → wage-based value → evaluate → pay.
- Config in `~/.nanobot/config.json` under `agents.clawwork` (`enabled`, `initialBalance` — **default $1000**, note the contrast with the benchmark's $10 — `tokenPricing`).
- Channels: **Telegram, Discord, Slack, WhatsApp, Email, Feishu, DingTalk, MoChat, QQ**.
- ⚠️ `cli.py::_inject_evaluation_credentials()` **reads API keys out of `~/.nanobot/config.json`** and exports them as `EVALUATION_API_KEY` / `EVALUATION_API_BASE` / `EVALUATION_MODEL`. Convenient; also a credential-handling surface worth knowing about before you run it.

---

## 5. ⚠️ Three identity facts that a careless reading gets wrong

**(1) "nanobot" is NOT Anthropic's.** An automated summariser asserted during this build that ClawMode *"wraps nanobot (Anthropic's agent framework)."* **That is false and was discarded.** `nanobot` is **`HKUDS/nanobot`** — *the same lab's own* ultra-lightweight personal-agent framework, openly **inspired by OpenClaw** and reimplementing ~90% of its capability in roughly **4,000 lines vs OpenClaw's ~430,000**. ClawWork's product integration therefore targets **HKUDS's own engine**, not a third party's and emphatically not Anthropic's. Had this gone uncorrected it would have flipped criterion (a).

**(2) OpenClaw is Peter Steinberger's** — and **Steinberger is already a corpus author**: he wrote **CodexBar (v159)**. The repo title *"OpenClaw as Your AI Coworker"* invokes the famous framework by name while the shipped integration path is nanobot. Accurate as a description of the *class*; worth noting as marketing framing.

**(3) HKUDS is a returning corpus author, not a new one.** `HKUDS/DeepTutor` is corpus subject **v38**, and `HKUDS/OpenSpace` was credited as a design source by **cortex-hub v181**.

---

## 6. The corpus-recursive payoff: v38 predicted this shape

The **DeepTutor v38** wiki recorded an *HKUDS vertical-stack hypothesis*:

> engine (**nanobot**) → methodology (CLI-Anything) → infra (LightRAG + RAG-Anything) → runtime (OpenHarness) → **apps** (DeepTutor + DeepCode …)

— and flagged *"50% HKUDS self-dependency"* in DeepTutor's dependency graph.

**ClawWork lands exactly on the predicted app layer**: a same-lab application/benchmark built on the same-lab engine (nanobot), reusing the lab's own stack. This is the vault's own earlier analysis being **confirmed by a later independent ship** — a clean Pattern #19 19a ecosystem-portfolio-builder strengthening and another Pattern #44 academic-lab data point.

---

## 7. The leaderboard — and the Claude question

| Rank | Agent | Start | Balance | Income | Cost | Pay Rate | Avg Quality |
|:--:|---|--:|--:|--:|--:|--:|--:|
| 🥇 | ATIC + Qwen3.5-Plus | $10.00 | $19,915.68 | $19,914.38 | $8.70 | $2,285.31/hr | 61.6% |
| 🥈 | Gemini 3.1 Pro Preview | $10.00 | $15,661.71 | $15,757.48 | $105.76 | $1,287.47/hr | 43.3% |
| 🥉 | Qwen3.5-Plus | $10.00 | $15,268.13 | $15,264.92 | $6.78 | $1,390.42/hr | 41.6% |
| 4 | GLM-4.7 | $10.00 | $11,497.05 | $11,503.49 | $16.44 | $877.80/hr | 40.6% |
| 5 | ATIC-DEEPSEEK | $10.00 | $10,877.01 | $10,870.52 | $3.52 | **$2,579.16/hr** | **66.8%** |
| 6 | Qwen3-Max | $10.00 | $10,782.80 | $10,781.06 | $8.26 | $1,072.14/hr | 37.9% |
| 7 | Kimi-K2.5 | $10.00 | $10,471.21 | $10,483.20 | $21.99 | $858.62/hr | 36.6% |

**Claude does not appear on the leaderboard, and the README never mentions Claude or Anthropic once.** But the repo **does** ship Claude run configs:

- `test_claude_sonnet_4_6_thirdparty_10dollar.json`
- `test_claude_sonnot_4_6_openrouter_10dollar.json` *(sic — "sonnot")*

So the honest statement is: **Claude Sonnet 4.6 was configured for this harness but is absent from the published results.** I cannot verify *why* — unrun, run-and-omitted, or cut for cost are all consistent with what is visible, and I will not guess. What is verifiable is that **`claude` appears in the commit-author list**, i.e. the repo was partly built *with* Claude Code even though Claude is absent from the results it publishes.

⚠️ **Read the leaderboard with three grains of salt:** it is **self-run by the authoring lab**; the **cost axis is compromised** by universal pricing (§4.1); and "quality" is an **LLM judge grading against rubrics the same lab wrote**. The `$2,285.31/hr` and `$15K in 11 hours` figures are *simulation outputs under the lab's own accounting*, not market earnings.

---

## 8. Maturity, honestly

- **~8.3k★ / ~1.1k forks / 82 watchers** — page-stated (§37.4).
- **~37–40 commits, all between Feb 16 2026 and Mar 3 2026.** As of **2026-08-17 the repo has been quiet for roughly five and a half months.** A viral two-week burst followed by silence.
- Contributors visible: `yuh-yang`, `chaohuang-ai`, `DorianZheng`, `gnai-creator`, `claude`, `thakoreh`, `Re-bin`.
- No releases surfaced; `trading/` is an empty stub; the internal package is named **`livebench`**, which collides in name with the well-known external **LiveBench** LLM benchmark (unrelated — a naming note, not a claim).
- Ships a real disclaimer: *"ClawWork is for educational, research, and technical exchange purposes only."*

---

## 9. Landscape — this is **not** a world-first

| Prior art | What it did first |
|---|---|
| **Vending-Bench / Vending-Bench 2** (Andon Labs, 2025–26) | The canonical "agent runs a business for a simulated year, scored purely on final bank balance (from $500)" benchmark. **Already cited inside this corpus** — the GLM-5 **v176** entry quotes *"Vending Bench 2 … $4,432."* |
| **Project Vend** (Anthropic × Andon Labs, 2025) | Claude ("Claudius") autonomously running a **real** vending shop in Anthropic's SF office — the real-world instance of the same idea. |
| **GDPval** (OpenAI, Oct 2025) | The professional-task dataset ClawWork consumes. |
| **CoffeeBench** (arXiv 2606.16613), **Agent Bazaar** (arXiv 2605.17698), **EvoAgentBench** (arXiv 2607.05202) | 2026 academic peers in long-horizon / multi-agent economic evaluation. |
| **Artificial Analysis GDPval-AA leaderboard** | An independent third-party GDPval leaderboard. |

**What is distinctive to ClawWork** is the *conjunction*, not any single element: real professional GDPval deliverables (not a vending sim) × **the agent pays for its own tokens** × an explicit **work-vs-learn** investment choice × bankruptcy as terminal failure × a **product wrapper** that applies the same accounting to a live consumer chat agent.

---

## 10. Why it matters here

Strip away the leaderboard theatre and two ideas survive contact with scrutiny, both of which are directly useful:

1. **Endogenous cost.** Make an agent pay for its own thinking and "good" stops meaning "capable" and starts meaning "worth it." That is the discipline the vault's `claude-api-cost-optimization` thread has been circling.
2. **Rubric + threshold + no-fallback grading.** Per-occupation rubrics, a hard 0.6 payment gate, artifact-must-exist checks, and an explicit refusal to degrade to heuristics — that is a *shippable* shape for an eval gate, and it is precisely what the vault's **RATIFIED candidate-LLM legibility ADR** demands of any LLM feature that touches a candidate.

Everything else — the $15K headline, the leaderboard ordering, the pay rates — should be read as a research lab's demo, not as evidence.
