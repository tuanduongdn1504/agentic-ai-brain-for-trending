# (C) ClawWork — Pilot Methods Menu (wiki v233)

**Honest framing up front.** ClawWork is a **read-and-borrow** subject, not a tool to adopt. It is a research benchmark from an academic lab, quiet for ~5.5 months, whose headline numbers are self-run and whose cost axis is methodologically broken (universal hardcoded token pricing). **Two ideas inside it are genuinely worth taking**; the rest is a demo. This menu is right-sized to that reality — **14 methods, not a padded 24** — and most of them cost nothing to run.

**⭐ One-thing path: A1 → B5 → D9.**

---

## A · Read & learn (zero install, zero risk)

**A1 ⭐ — Read the economic loop and the evaluator (~45 min).**
Two files carry the whole idea: `livebench/agent/economic_tracker.py` (876 lines — the balance/cost/bankruptcy ledger) and `livebench/work/llm_evaluator.py` (829 lines — per-occupation rubrics, the 0.6 payment gate, the no-fallback rule). Read them in that order and the design clicks: *an agent whose reasoning is billed against the same balance its output earns.* This is the corpus's best short lesson in making cost a first-class objective rather than an afterthought.

**A2 — Read `clawmode_integration/skill/SKILL.md`.**
A compact, well-formed agent skill that encodes a *policy* (four financial states → four behaviours) plus an iteration budget. Useful as a template for any skill that has to make an agent behave differently under different resource conditions.

**A3 — Read the GDPval paper (arXiv 2510.04374), not ClawWork's summary of it.**
44 occupations × real professional deliverables × BLS wages is a genuinely interesting artifact in its own right — a structured map of *which knowledge work is being measured against AI*. Go to the source; ClawWork's README miscalls occupations "sectors."

**A4 — Read the prior art to calibrate the hype.**
Andon Labs' **Vending-Bench** and Anthropic's **Project Vend** ("Claudius") did economic-survival agents first, and Project Vend has the better failure stories (Claudius giving stock away below cost, hallucinating payment details). Ten minutes here inoculates you against the `$15K in 11 hours` framing.

---

## B · Borrow the patterns (zero install — the highest-ROI band)

**B5 ⭐ — Lift the "rubric + hard threshold + no fallback" eval gate into hireui's LLM-feature spec.**
The shape, verbatim from source: per-category rubric loaded from a file → **missing rubric raises, it does not degrade** → artifact must exist, be non-empty, and be under a size cap → score normalised 0–1 → **no payment/no pass below 0.6** → *"heuristic evaluation is no longer supported."*
That is exactly the discipline the **RATIFIED candidate-LLM legibility ADR** demands: a gate that is explicit, file-backed, auditable, and that **fails closed**. Write it into the spec for hireui's first LLM feature (Match-Explain / candidate summariser).

**B6 — Make token cost endogenous: a per-feature cost ledger for hireui.**
Steal the inversion, not the code. Any hireui LLM feature should carry a running cost record and a stated value threshold — *this feature must be worth more than it costs to run.* Composes directly with the live **`claude-api-cost-optimization`** thread and the **ccusage → OTel → Grafana** measurement layer already identified as the pilot's instrumentation.
⚠️ And take ClawWork's *mistake* as the lesson too: **price per model, never universally.** Its leaderboard is undermined by exactly the shortcut you must not copy.

**B7 — Borrow the four-state resource policy for agent behaviour.**
`thriving / stable / struggling / bankrupt` is a clean pattern for any long-running agent that consumes a budget: change strategy by resource band rather than running one policy until you hit the wall. Directly portable into the loop-budget discipline already running in the vault (80% → report-only, 100% → stop).

**B8 — Borrow the "invest vs earn" turn structure for autonomous loops.**
The work-or-learn daily choice is a compact way to give a long-horizon agent an explicit exploration budget. Worth a note in the loop-engineering v189 pilot alongside the existing L0→L3 ladder.

---

## C · Hands-on, scratch only (real money, low value)

**C9 — Run one agent for a short window on a throwaway key.**
`pip install -r requirements.txt`, set `OPENAI_API_KEY`, `./start_dashboard.sh` + `./run_test_agent.sh`, open `localhost:3000`. Use one of the shipped `*_10dollar.json` configs. You will see the ledger and the dashboard work.
**Be clear about what you get:** you are paying real API money to watch a simulation whose accounting you already understand from reading it. **A1 gives you ~90% of the value at 0% of the cost.** Do this only if you specifically want to see the loop live.

**C10 — Run the Claude Sonnet 4.6 config and fill the gap in their leaderboard.**
`test_claude_sonnet_4_6_thirdparty_10dollar.json` ships but **no Claude row is published**. Running it is the single most interesting *empirical* thing available here — and it is the one result the repo does not give you. ⚠️ Fix the pricing first (see C11) or the cost column will be meaningless.

**C11 — If you run anything, patch the price table first.**
`input_token_price=2.5 / output_token_price=10.0` is applied to every model. Replace with real per-model rates before believing any "Cost" or "$/hr" figure you produce.

**C12 — Do NOT run ClawMode against a live account.**
The nanobot wrapper reads API keys out of `~/.nanobot/config.json` and re-exports them, attaches to nine consumer chat channels, and lets `/clawwork` assign tasks that execute code. If you ever try it: throwaway keys, a scratch nanobot config, a single private channel, sandbox on.

---

## D · hireui / Goal #2

**D9 ⭐ — Wire the cost-vs-value gate into hireui's first LLM feature.**
Combine **B5** (rubric + threshold + fail-closed) and **B6** (per-feature cost ledger) into one ADR on an `agent-*` branch: *no hireui LLM feature ships without (i) a file-backed rubric, (ii) a hard pass threshold, (iii) a measured per-call cost, and (iv) a documented value threshold it must beat.* This is a real, small, shippable Goal-#2 artifact that needs **zero** ClawWork code and composes with the standing candidate-LLM legibility ADR.

**D10 — Read GDPval's occupation set as recruitment-domain intelligence.**
44 occupations, professionally-authored deliverables, wage-anchored. For a recruitment product, *which roles are being benchmarked against AI, and how well AI does on their actual work products* is directly relevant market intelligence. Read-only; no pipeline.

**D11 ⚠️ — The hard fence: do NOT score candidates this way.**
ClawWork's structure (classify into an occupation → estimate hours → apply a wage → have an LLM grade the artifact → pay proportionally) is seductive and **must not be pointed at humans**. Automated wage/quality scoring of people is squarely the EU AI Act Annex III high-risk path the vault's ADR exists to prevent. **Borrow the shape for grading the AI's own output; never for grading a candidate.**

---

## F · Vault meta

**F12 — File the §C mint and its NO-MINT alternative for the overdue audit.**
The audit is badly overdue (last v212; v213→v233 all shipped since). This row — *Economic-Survival Agent Benchmark*, N=1, corpus-first-for-surface / not world-first — is a genuine judgment call and should be re-opened, not inherited.

**F13 — Record the v38 prediction-confirmation.**
The DeepTutor v38 wiki's *HKUDS vertical-stack hypothesis* (engine nanobot → infra LightRAG → **apps**) is confirmed by ClawWork landing on the app layer. That is the vault's own earlier analysis being validated by a later independent ship — worth a Pattern #19 19a / #44 note.

**F14 — Note the eval-surface gap the corpus still has.**
ClawWork is the corpus's first *benchmark* subject; llm-space v221 is its first *eval workbench*. There is still no subject covering the standard agent evaluation suites (SWE-bench, Terminal-Bench, τ-bench) that the corpus repeatedly *cites* but has never studied. A live gap worth a future intake.

---

## Fence (if you run anything at all)

`install-snapshot` before `pip install -r requirements.txt` · **NOT source-cloned → treat as untrusted until inspected** · scratch venv + throwaway API key · keep the sandbox (boxlite/E2B) enabled — the agent **executes generated code** · never point ClawMode at a real nanobot config or a live chat account · patch the per-model price table before believing any cost figure · pin the commit (no releases; repo quiet since 2026-03-03) · MIT, so the *patterns* are free to borrow by hand · hireui stays behind its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first) and takes **design only** — there is no hireui component here.
