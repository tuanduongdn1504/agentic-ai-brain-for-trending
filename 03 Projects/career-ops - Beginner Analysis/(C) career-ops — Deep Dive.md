# (C) career-ops — Deep Dive (LLM Wiki v200)

> **Subject:** `santifer/career-ops` — *"Open-source AI job search: scan job portals, score listings A-F, tailor your CV, track applications — runs locally in your AI coding CLI."*
> **Author:** Santiago Fernández de Valderrama (`@santifer`, `hi@santifer.io`, santifer.io) — Head of Applied AI at **Zinkee** (Spain), ex-founder (Santifer iRepair, 2009–2025, exited). **NOT Anthropic.**
> **License:** MIT (© 2026 Santiago Fernández de Valderrama) + a `TRADEMARK.md` governing the "career-ops" name. **Version:** v1.18.0. **Stack:** JS 70.4% / TS 20.5% / Go 6.6%. **Source-verified at commit `e9bacc48` (clone, 2026-07-08).**
> **This is the 200th LLM-Wiki ship.** Built per routine v2.6. Verdict produced **inline + hand-verified** (a 13-agent read-only workflow did source + web research ONLY; every corpus/collision/identity/mint claim + all load-bearing quantitative facts verified BY HAND — see the Verdict's confabulation log).

---

## The one-sentence thesis

career-ops turns **any AI coding CLI** (Claude Code first) into a **candidate-side job-search command center**: paste a job URL or JD, and the agent classifies the role, scores it 1–5 against *your* CV, generates an ATS-optimized tailored PDF, checks the posting isn't a ghost job, and files it into a tracked application pipeline — **entirely on your machine, and it never submits anything for you.**

The framing that makes it worth a wiki (README, verbatim):

> *"Companies use AI to filter candidates. **I just gave candidates AI to choose companies.**"*

**That is the domain-exact inverse of hireui** (the operator's Goal-#2 recruitment SaaS, which scores candidates *for employers*). Same domain — hiring — opposite actor. That inversion is the whole reason this ship matters to the working flow (see the Pilot Methods Menu).

---

## What it actually is (not what the README markets)

The README sells "A-F scoring (10 weighted dimensions)." The **code** is more modest and more honest — and I document the code, not the marketing:

- **The "brain" is Markdown, not code.** The evaluation logic lives in `modes/*.md` prompt files, executed by whichever AI coding CLI you point at the repo. `modes/_shared.md` is the scoring core; `modes/oferta.md` is the A–G evaluation flow. **The coding agent IS the runtime** — there is no Python/JS orchestrator driving the evaluation; the CLI reads the prompts + your `cv.md` and reasons. (`ARCHITECTURE.md`: *"The logic lives in Markdown prompt files under `modes/`, executed by whatever AI coding CLI you use … No single model is hardcoded."*)
- **The deterministic mechanics are ~50 single-job Node scripts** (`*.mjs` at the repo root), most **zero-LLM**: the scanner, the PDF renderer, the tracker, the dedup/merge/reconcile utilities, the salary analyzer, the repost detector, the STAR matcher, the report-number reserver. "One script = one job; `*.test.mjs` sits next to what it tests" (`ARCHITECTURE.md`).
- **The optional surfaces:** a Go Bubble Tea TUI dashboard (`dashboard/`) and an alpha Next.js web UI (`web/`) — both read the *same* canonical files, both are isolated from the core.

So the accurate label is an **agent-first, end-to-end, candidate-side job-search / career-operations pipeline** — the OpenMontage v188 shape ("the coding agent IS the runtime, deliverables are artifacts, over a deterministic-tool substrate") applied to job search instead of video production.

---

## The five layers (component map)

```
You paste a job URL or JD
        │
   ┌────▼──────────┐   Discovery ── scan.mjs + providers/*.mjs (~53 modules) ── ZERO Claude tokens (pure HTTP+JSON to public ATS APIs) ── --verify does a Playwright liveness pass
   │  1. DISCOVERY │
   └────┬──────────┘
   ┌────▼──────────┐   Evaluation ── modes/_shared.md (scoring core) + modes/oferta.md (A-G blocks) + your cv.md ── reasoning, not keyword-matching
   │  2. SCORING   │
   └────┬──────────┘
   ┌────▼──────────┐   Generation ── generate-pdf.mjs (Playwright HTML→PDF) | build-cv-latex.mjs (LaTeX) | generate-cover-letter.mjs ── ATS-safe templates + fonts + voice-dna.md
   │  3. GENERATION│
   └────┬──────────┘
   ┌────▼──────────┐   Tracking ── data/applications.md (SoT) + reports/NNN-*.md + tracker.mjs/merge/dedup/reconcile/normalize/reserve-report-num ── strict data contract + SQLite derived index
   │  4. TRACKING  │
   └────┬──────────┘
   ┌────▼──────────┐   Self-update ── update-system.mjs ── refreshes SYSTEM_PATHS only, never touches USER_PATHS
   │  5. UPDATE    │
   └───────────────┘
   (optional) Go TUI dashboard + alpha Next.js web UI — both read the same canonical files
```

### 1. Discovery — `scan.mjs` + `providers/` (zero-token)

`scan.mjs` header (verbatim): *"Zero-token portal scanner with a plugin-based provider layer … Zero Claude API tokens — pure HTTP + JSON."* Each `providers/*.mjs` exports `{ id, detect(entry), fetch(entry, ctx) }`; adding a job source = drop a `.mjs` in `providers/`.

- **Hand-counted: ~53 real provider modules** (59 files, ~6 `_`-prefixed helpers) — Greenhouse, Ashby, Lever, BambooHR, Breezy, Personio, Phenom, Avature, Comeet, Workday-class, plus board aggregators (arbeitnow, echojobs, himalayas, jobicy, nofluffjobs, justjoin, larajobs, hackernews, 4dayweek…) and a `local-parser.mjs` for custom sources. ⚠️ **Doc-vs-code:** the README says "21 provider modules" — an undercount; the `providers/` dir holds ~53.
- `scan.mjs --verify` launches Playwright *after* the API pass to drop expired postings before they hit `pipeline.md`; `--throttle`/`--headed-fallback` for anti-bot hosts. Auth-gated/login sources are **deliberately out of core** (they belong in the plugin layer).
- A `_trust-validator.mjs` + `fingerprint-core.mjs` catch untrustworthy feeds + cross-listings/reposts at scan time.

### 2. Scoring — `modes/_shared.md` + `modes/oferta.md` (the domain IP; hand-read)

**The real rubric (code-authoritative, corrected from the README):**
- **A 1–5 global score**, computed by default as the **average of the block scores** (`oferta.md:404`: *"Score: match average (1-5) … Default (if absent or silent): average of block scores"*), user-overridable via `modes/_custom.md → Scoring Rules`.
- **5 weighted dimensions** (`_shared.md`): Match-with-CV, North-Star alignment (fit to the user's target archetypes), Comp (vs market), Cultural signals, Red flags. *(⚠️ A workflow agent's "25/20/15/15/15/10% + a 6th 'intuition' dimension" is **unverified/confabulated** — no such fixed weights exist in the source; the default is a plain average of block scores. Documented honestly.)*
- **Score interpretation** (`_shared.md`): 4.5+ = apply immediately · 4.0–4.4 = worth applying · 3.5–3.9 = only with a specific reason · **below 3.5 = recommend against**. ⚠️ The README markets "recommend against below 4.0" — the code cutoff is **3.5**.
- **The report structure is 7 blocks A–G** (`oferta.md`): A Role Summary (+ culture screen + geo-mismatch), B Match-with-CV (gap mitigation), C Level & Strategy, D Comp & Demand, E Customization Plan, F Interview Plan (STAR+Reflection), **G Posting Legitimacy** (+ H Draft Application Answers).
- **6 archetypes** (`_shared.md`): AI Platform/LLMOps · Agentic/Automation · Technical AI PM · AI Solutions Architect · AI Forward Deployed · AI Transformation — each with JD keyword signals. (These are the author's own AI-role archetypes; the README explicitly says *"Change the archetypes to backend engineering roles"* — the taxonomy is meant to be customized.)

**Block G posting-legitimacy (scam / ghost-job detection):** three tiers (High Confidence / Proceed with Caution / Suspicious) over 8 reliability-weighted signals (posting age, apply-button-active, tech-specificity, requirements-realism, layoff-news, reposting-pattern, salary-transparency, role-company-fit). ⚠️ **It does NOT affect the 1–5 score — it is a separate qualitative assessment** (`_shared.md:65`; a workflow agent's "Block G caps the score at 3.5 as a hard veto" is **contradicted by the source** and is documented as a confabulation). Its framing is **MANDATORY-ethical:** *"NEVER present findings as accusations of dishonesty. Present signals and let the user decide. Always note legitimate explanations."*

**Comp-reliability taxonomy:** 10 company types × 4 reliability tiers; splits an advertised figure into base / variable / stable-cash / non-cash; *"Never present advertised compensation as real take-home pay unless the source explicitly supports it."*

**The genuinely excellent part — the Global Rules (this is the transferable gold):**
- **Anti-fabrication (verbatim):** *"NEVER claim the user authored a project, repo, library, tool, framework, or open-source artefact unless explicitly attributed … Tool-of-trade conflation (user uses X → user built X) is the most common fabrication pattern and is forbidden."*
- *"Keywords get reformulated, never fabricated. Reorder, reframe, emphasise — but never invent … Silence on a topic beats manufactured detail."*
- **Exclusive Sources-of-Truth boundary:** only `cv.md` + `article-digest.md` + `profile.yml` + `_profile.md` + `writing-samples/` + `interview-prep/` + `_custom.md` are content sources; *"Auto-memory, parent-directory repos, and cross-session inferences are out of scope."*
- **Subagent cost guardrail (verbatim):** *"Any subagent you spawn is a single-pass worker: it MUST NOT spawn further subagents, and MUST NOT invoke other skills — especially recursive research skills … Those fan out into nested agents and can burn tens of millions of tokens on one run."*
- **NEVER: submit applications on behalf of the candidate.**

### 3. Generation — ATS CVs, cover letters, PDFs

Two parallel PDF pipelines (well-cited by the workflow, line numbers verified against templates):
- **HTML→PDF via Playwright** (`generate-pdf.mjs`): the default path; base64 font-inlining; `normalizeTextForATS()` converts em-dashes/smart-quotes/zero-width/arrows/bullets to ASCII; **ligatures disabled** because Headless Chromium substitutes `fi/fl` with Unicode glyphs `U+FB01/02/03` that ATS text extractors mis-decode ("veriﬁcation" → keyword miss).
- **LaTeX** (`build-cv-latex.mjs`→`generate-latex.mjs`): ASCII-only, explicit CJK-rejection, tectonic/pdflatex auto-detect, structure validation.
- **The bundled Space Grotesk / DM Sans woff2 fonts are deliberately NOT used in the ATS-optimized CV path** — variable fonts inject spurious inter-word spaces at PDF-extraction time (`"SUM M ARY"`), corrupting keyword parsing; a Liberation-Sans/Helvetica/Arial stack is used instead.
- **Keyword injection is NOT in the render layer** — it happens upstream in the agent's payload phase, gated by the anti-fabrication rules above; **ATS optimization here is *defensive* (make the PDF machine-readable), not *injective* (stuff fake keywords).** This meaningfully softens the "gaming ATS" dual-use concern.
- **Voice DNA** (`voice-dna.md`): a two-tier anti-slop writing guardrail. Tier 1 = HARD RULES (banned AI vocab like "delve/paradigm/harness"; **negative-parallelism ban** — *"'This isn't X. This is Y' … the single most reliable tell of AI-generated text … FATAL = one violation rejects the entire output"*; no em-dashes) applied to ALL generated text; Tier 2 = conversational voice applied only to cover letters/outreach, never CV/ATS text. *"Accuracy always wins over style."* `_profile.md` overrides `voice-dna.md`.
- **Cover letters:** four interactive angle prompts (opening / profile-intro / problems / achievements) → draft-in-chat approval → A4 PDF via the same pipeline. Draft-only.

### 4. Tracking + the data contract + self-updater (the maturity core)

- **Files are canonical, databases are derived** (RFC #918; `tracker.mjs:4–21`, verbatim): *"data/applications.md stays the source of truth. The SQLite DB is a derived index, built and rebuilt from the markdown — safe to delete at any time."* Rationale: *"at hundreds of rows, a markdown table degrades … a `|` inside a cell shifts every column after it."* — **This is the vault's own LLM-Wiki files-as-brain philosophy, shipped as a product design.**
- **Strict system/user data contract** (`DATA_CONTRACT.md`, `update-system.mjs`): **USER_PATHS** (17 categories — `cv.md`, `config/`, `data/`, `reports/`, `output/`, `jds/`, `_profile.md`, `interview-prep/`, `writing-samples/`…) are **never** touched by updates; **SYSTEM_PATHS** (200+ — `modes/*.md`, `*.mjs`, templates, dashboard, docs) are safely auto-replaced. The updater checks every git-modified file against USER_PATHS and **aborts + reverts only system files** if a user file was touched. `updater-migration-tests.mjs` enforces no path overlap. *"If a file is in the User Layer, no update process may read, modify, or delete it."*
- **Self-updater sophistication:** `update-system.mjs` backs up to a timestamped branch, walks its own relative-import closure before re-execing the new updater (so a new import can't break the upgrade — `ERR_MODULE_NOT_FOUND` guard), then checks out only SYSTEM_PATHS.
- **Concurrency:** `reserve-report-num.mjs` uses `open(O_CREAT|O_EXCL)` sentinel files to atomically claim the next report number (fixes race #749 — two Claude Code windows/batch workers can't collide).
- **9 canonical statuses** (`templates/states.yml`): evaluated / applied / responded / interview / offer / rejected / discarded / skip / hired. `merge`/`dedup`/`normalize`/`reconcile` keep the tracker consistent; `role-matcher.mjs` provides the shared fuzzy title-match so merge and dedup can't diverge.

### 5. The "beyond the CV" domain engines (the differentiated candidate-side IP — hand-read)

Mostly **zero-LLM, deterministic** — the "files are the brain, Node offloads the mechanics" discipline:
- **`salary-gap.mjs`** — Desired vs Advertised vs Actual comp analyzer; append-only observations, trust-tier fold (`contract > offer-letter > recruiter-verbal > user`).
- **`detect-reposts.mjs`** — flags a company+role appearing 2+ times with different URLs in a 90-day window (fuzzy title match) = the same opening re-listed = stale/ghost signal.
- **`followup-cadence.mjs`** — computes follow-up cadence for active applications, flags overdue.
- **`invite-match.mjs`** — matches a pasted recruiter interview-invite (often "Schedule your phone screen" with no role) to the right tracker row; *"a silent wrong guess is worse than showing a short ranked list."*
- **`reply-matcher.mjs`** — deterministically maps email replies to tracker entries (handles Chinese names too).
- **`match-star.mjs`** — zero-LLM ATS behavioural-question matcher; scores your STAR stories (`interview-prep/story-bank.md`) against a question, returns the top match at ATS paste length (250–500 words).
- **`classify-tier.mjs`** — seniority classifier (intern/entry/mid/senior, weighted keywords).
- **`prepare-application.mjs`** — ATS auto-fill for Greenhouse/Ashby/Lever; **"Never POSTs anything — the user reviews the output, opens the apply URL, and submits themselves."** *(The never-auto-submit guardrail, baked into code, not just the disclaimer.)*

---

## Multi-CLI + cost architecture

- **One canonical skill, seven+ CLIs.** `.agents/skills/career-ops/SKILL.md` (the open agent-skill standard, agentskills.io) is **symlinked** from `.claude/`, `.opencode/`, `.qwen/`, `.grok/`, `.antigravitycli/` (and a text-file fallback for `.kimi/`), so all CLIs read one canonical 27-subcommand router with zero drift. `AGENTS.md` is the canonical instruction file; `CLAUDE.md`/`CODEX.md`/`OPENCODE.md`/`GEMINI.md`/`KIMI.md` are thin wrappers. Supported: Claude Code (first-class, "Built with Claude Code" badge) / OpenCode / Antigravity (Gemini) / Codex / Qwen / Kimi / Grok / GitHub Copilot.
- **Model-agnostic evaluation + a genuine budget story.** The same scoring prompts run headless against four backends via standalone scripts: `gemini-eval.mjs` (Gemini free tier, 15 RPM / 1M tok/day), `ollama-eval.mjs` (100% local), `openai-eval.mjs` (any OpenAI-compatible endpoint), `openrouter-runner.mjs` (multi-provider, auto-rotating free models + a persistent blacklist). **Discovery is zero-token** (pure HTTP), liveness is checked before evaluation, and `docs/RUNNING_ON_A_BUDGET.md` documents a full evaluation at **~4,500 tokens / <$0.001 with DeepSeek V3**. This is a strong `claude-api-cost-optimization` exemplar.

---

## Maturity, security, and honest caveats

- **Tests:** 66 test files, **513+ `pass()` assertions** in `test-all.mjs` (`ARCHITECTURE.md` says "500+ checks"), 57 provider-specific tests, `verify-pipeline.mjs` (10 data-integrity checks), `doctor.mjs` preflight. CI: 11 GitHub Actions — `test` + CodeQL (JS/TS + Go) required, CodeRabbit reviews every PR, Renovate, release-please, SBOM, a **hard-blocking `no-user-data.yml`** that scans every PR for user-layer files and blocks the merge (a technical enforcement of the data contract).
- **Security = BENIGN install / BENIGN data-privacy / MODERATE-but-conservatively-handled dual-use.** Install: `postinstall` downloads Chromium via Playwright (~170 MB, transparent, CI-skipped); `npx @santifer/career-ops init` clones + installs; 4 minimal deps (`@google/generative-ai`, `dotenv`, `js-yaml`, `playwright`). Privacy: PII stays local, sent only to your chosen provider, **zero telemetry** (`LEGAL_DISCLAIMER.md` §2). Dual-use: Playwright scrapes *public no-auth* ATS APIs; the disclaimer explicitly prohibits scraping-restricted-platforms + spamming + mass-apply, and *"maintainers actively reject contributions that facilitate ToS violations."* The résumé "optimization" is defensive-ATS + honest-reformulation (not fabrication), and **never-auto-submit is enforced in code** (`prepare-application.mjs`). ⚠️ One open item: the `dependency-review` CI is currently `continue-on-error: true` pending a GitHub Settings change (issue #343); `node:sqlite` needs Node ≥22.5.
- **Governance:** BDFL (`@santifer`) + a 5-tier earned-role contributor ladder + identity verification; 2 core contributors (`@bracketouverte` scan/ATS, `@piscespieces` docs) + Discord guide members; 15 README translations; Trademark/Governance/Code-of-Conduct/Maintainers/Security docs; v1.3.0→**v1.18.0**, multiple releases/week.
- **Honest limitations:** (1) the *hard AI* is the underlying CLI/model — career-ops orchestrates prompts + deterministic scripts, it doesn't build a model; (2) the case-study metrics (README: *"740+ job offers evaluated, 100+ tailored CVs, landed a Head of Applied AI role"*; a variant figure "631 evaluated / 66 recommended / 12 interviews" appears elsewhere) are **self-stated marketing**, web-corroborated (Business Insider, WIRED Greece) but not independently verifiable per-number; (3) stars/velocity are **page/web-stated only** (repo page ~59.2k★; web says "46k in first month") — the harness mocks the GitHub API (§37.4), so **no viral-velocity claim**; (4) it's a ~3-month-old, launch-viral project with **one active maintainer** (a single point of failure), so "sustained" is partly aspirational despite the governance scaffolding.

---

## Why it earns a wiki (the short version)

1. **Goal #1 (agents for software dev):** a mature, Claude-Code-first, agent-native operational system — one of the richest agent-engineering exemplars in the corpus (agent-first "the CLI is the runtime" + the open agent-skill standard + multi-CLI-via-symlink + deterministic-Node-offload + a strict data contract + a self-updater + zero-token cost design + a subagent cost guardrail + anti-fabrication provenance rules).
2. **Goal #2 (hireui):** the **domain-exact inverse** of hireui — a candidate-side scoring/tailoring engine that is directly informative for (a) red-teaming what candidates will do to beat hireui's screening, (b) mirroring career-ops's scoring/legitimacy/comp rubric into hireui's own candidate-matching, and (c) modelling the EU-AI-Act / GDPR / non-discrimination / human-in-the-loop ethics posture hireui (a high-risk employment-category SaaS) must build. **The sharpest Goal-#2 subject since serve-sim v183 — arguably sharper.**

See **(C) career-ops — Verdict** for the 4-criteria call + pattern outcome, and **(C) career-ops — Pilot Methods Menu** for the 24 ways to apply it.
