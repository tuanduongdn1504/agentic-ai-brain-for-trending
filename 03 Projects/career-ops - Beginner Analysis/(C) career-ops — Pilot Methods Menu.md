# (C) career-ops — Pilot Methods Menu (LLM Wiki v200)

**24 concrete ways to apply career-ops into your working flow**, laddered from zero-risk reading → borrow-by-hand → hands-on scratch → hireui (Goal #2) → personal use → vault-meta. Each names what it lands on and what it costs.

> **The frame that matters:** career-ops is the **domain-exact inverse of hireui**. hireui scores *candidates for employers*; career-ops scores *employers for candidates* and generates ATS-optimized CVs to *beat* employer ATS filters. So career-ops gives you three distinct kinds of value for hireui: (1) **red-team** — what candidates will do to beat your screening; (2) **mirror-design** — a ready-made scoring/legitimacy/comp rubric to flip onto the employer side; (3) **ethics/compliance mirror** — the EU-AI-Act/GDPR/human-in-the-loop/no-fabrication posture a high-risk employment SaaS must build. Plus a fourth: you can just **use it for your own career** (Surface E).

> **⭐ One-thing path: B5 → C11 → D16.** Steal the anti-fabrication + Sources-of-Truth rules into `CLAUDE.md` (zero install) → run a scratch evaluation to see the loop → build hireui's first LLM feature (a Match-Explain / candidate-scoring rubric) on the mirrored architecture, on an `agent-*` branch.

---

## Surface A — Read & learn (zero risk, ~1–3 h)

**A1 — Read the scoring brain as an agent-design masterclass.** Read `modes/_shared.md` + `modes/oferta.md` from the pinned clone. Internalize four transferable moves: the **exclusive Sources-of-Truth boundary**, the **anti-fabrication rule** ("tool-of-trade conflation is the most common fabrication pattern"), the **subagent cost guardrail** ("single-pass workers, never nest, never call recursive research — can burn tens of millions of tokens"), and the **1–5 avg-of-blocks rubric**. *(Goal #1; the richest hour.)*

**A2 — Read the data contract + self-updater** (`DATA_CONTRACT.md`, `update-system.mjs`, `tracker.mjs`). See "files are canonical, databases are derived" (RFC #918) + the USER/SYSTEM path separation shipped as a product design — it's your own LLM-Wiki files-as-brain philosophy, externally validated. *(Goal #1 + vault-meta.)*

**A3 — Read Block G + the comp-reliability taxonomy** (`_shared.md` §Posting Legitimacy + §Company Type). A worked example of scoring a *fuzzy, adversarial* signal (ghost jobs, inflated comp) with a MANDATORY ethical framing ("present signals, never accusations"). Directly relevant to any hireui trust/quality feature. *(Goal #2.)*

**A4 — Read `voice-dna.md`** — the two-tier anti-AI-slop guardrail (banned vocab + the negative-parallelism "FATAL" rule). Compare against ponytail v168 / the vault's own writing. *(Goal #1 + vault-meta.)*

---

## Surface B — Borrow the patterns (zero install, highest ROI)

**B5 — ⭐ Port the anti-fabrication + Sources-of-Truth rules into the vault's `CLAUDE.md` and any hireui LLM-feature spec.** career-ops's two rules ("NEVER claim the user authored X unless attributed"; "keywords get reformulated, never fabricated — silence beats manufactured detail") are the single best anti-hallucination discipline in the corpus for any system that generates claims *about a person from their documents* — exactly hireui's candidate-matching problem. Zero install. *(Goal #1 + #2; highest ROI.)*

**B6 — Steal the subagent cost guardrail into the vault's loop/agent discipline.** "Any subagent is a single-pass worker; never nest; never invoke recursive research skills." A one-paragraph rule that composes with loop-engineering v189's budget guard + the vault's own multi-agent workflows. *(Goal #1; cost thread.)*

**B7 — Adopt "files are canonical, databases are derived" as an explicit hireui data-design ADR.** When hireui stores candidate scores/notes, make the human-diffable record the source of truth and any DB a rebuildable index — the RFC #918 pattern. *(Goal #2; vault-meta.)*

**B8 — Steal the deterministic-tool-offload split.** career-ops keeps the *judgment* in Markdown (the LLM brain) and offloads *mechanics* to ~50 zero-LLM Node scripts (match/dedup/reserve/salary/repost). Mirror this in hireui: LLM decides, deterministic code computes/validates/persists. Composes with ai-berkshire v187's `financial_rigor.py` pattern. *(Goal #1 + #2.)*

**B9 — Borrow the Block-G legitimacy rubric as a hireui "posting/candidate trust" spec.** The 3-tier / 8-signal / "present-signals-not-accusations" structure is a template for any hireui feature that must flag something risky (a suspicious profile, a low-quality req) *fairly*. *(Goal #2.)*

**B10 — Borrow the comp-reliability taxonomy** (10 company types × 4 tiers; split advertised vs base vs variable) into hireui's comp/offer features or your Scrum-coaching salary conversations. *(Goal #2 + personal.)*

---

## Surface C — Hands-on scratch trials (low risk; install first)

**C11 — ⭐ Install into a scratch dir and run ONE real evaluation.** `install-snapshot` → `npx @santifer/career-ops init` in a *scratch* directory → drop a throwaway `cv.md` → open Claude Code → paste one real job URL → watch the observe→score→generate→track loop. See what a mature agent-first pipeline feels like end-to-end. *(Goal #1; proves the loop. Fence below.)*

**C12 — Run the zero-token scan + the budget path.** `node scan.mjs --dry-run` (zero Claude tokens) then a single eval via `node gemini-eval.mjs` (free tier) or `ollama-eval.mjs` (fully local). Measure the token/cost of one evaluation against career-ops's "~4,500 tokens / <$0.001 with DeepSeek" claim — a concrete cost-optimization data point. *(Goal #1; cost thread.)*

**C13 — Generate one ATS PDF and inspect the defensive-ATS mechanics.** Run `generate-pdf.mjs` on a sample payload; open the PDF; try a literal keyword search to confirm the ligature/font-normalization actually prevents "veriﬁcation"-style extraction misses. A reusable lesson for any PDF hireui ever generates (offer letters, candidate reports). *(Goal #1 + #2.)*

**C14 — Diff a `_custom.md` scoring override.** Add a `modes/_custom.md` with a custom Scoring Rule and confirm the rubric changes without editing a system file — a live demo of the data-contract "customize the user layer" pattern. *(Goal #1.)*

**C15 — Run `match-star.mjs` on a scratch story bank.** A zero-LLM STAR-matcher; useful raw material for a Scrum-coaching interview-prep exercise and a study of deterministic scoring. *(personal + Goal #1.)*

---

## Surface D — hireui / Goal #2 (the real payoff; behind the CONSTITUTION fence)

> hireui has **no LLM integration yet** → these are *build-it-right specs*, not retrofits. All work on an `agent-*` branch (I-2), operator-installs-skills (I-8), rooted in the hireui repo, GitNexus-first. See the memory `project_hireui_pilot_target`.

**D16 — ⭐ Spec hireui's first LLM feature — "Match-Explain / candidate-role scoring" — by MIRRORING career-ops's rubric onto the employer side.** career-ops scores a role against a CV; hireui scores a candidate against a role. Flip the 5-dimension + archetype + posting-legitimacy structure, keep the anti-fabrication + Sources-of-Truth rules verbatim, add the mosh vendor-seam (memory `project_mosh_ai_powered_apps_pilot_thread`). Composes with the `miai-cv-matching` Match-Explain thread. A spec doc + a prototype on an `agent-*` branch = **the first completed Goal-#2 pilot artifact since v153.** *(Goal #2; the headline.)*

**D17 — Red-team hireui's screening against career-ops.** Run career-ops on a scratch CV targeting a hireui-hosted role (or a synthetic one), then ask: does hireui's screening reward the ATS-keyword-optimized CV over a substantively stronger but plainer one? Where career-ops wins, hireui has a robustness gap. *(Goal #2; adversarial.)*

**D18 — Draft hireui's EU-AI-Act / responsible-AI gate from career-ops's ethics mirror.** hireui is a commercial employer-side candidate-screening SaaS = the EU AI Act's **high-risk employment** category. career-ops's LEGAL_DISCLAIMER (§2 GDPR, §6 EU AI Act, non-discrimination, human-in-the-loop, no-fabrication) is a mirror of hireui's obligations. Convert it into a hireui responsible-AI gate spec (transparency + human oversight + non-discrimination + provenance). Composes with the mlsysbook v197 responsible-AI-for-hiring content + the ai-berkshire v187 "AI Hiring Committee." *(Goal #2; compliance.)*

**D19 — Adopt "never-auto-submit / human-in-the-loop" as a hireui product invariant.** career-ops bakes it into code (`prepare-application.mjs` "never POSTs"). hireui's analogue: never auto-reject/auto-advance a candidate — the AI recommends, a human decides. Write it as a product constraint. *(Goal #2.)*

**D20 — Prototype a hireui posting/req quality-checker from Block G.** Flip Block G (candidate detecting ghost jobs) into hireui detecting low-quality/scam *reqs* posted by employers — same 3-tier / signal-weighted / present-signals-fairly structure. *(Goal #2.)*

**D21 — Use career-ops's data-contract + report schema as the template for hireui's candidate-report storage.** Human-diffable Markdown reports (`reports/NNN-*.md` + a Machine-Summary YAML) + a derived SQLite index; atomic report-number reservation for concurrent writes. Directly portable to how hireui persists AI-generated candidate assessments. *(Goal #2.)*

---

## Surface E — Personal use (your own career; off the software goal but genuinely useful)

**E22 — Actually run your own job search through it.** As a software developer + Scrum coach, point career-ops at real roles: it will score them 1–5 against your CV, flag ghost jobs, and generate tailored CVs you review + send yourself. The honest ethos (filter-not-spray, never-submit, no-fabrication) makes it a defensible personal tool. Fence: your PII → your chosen provider; review every generated line. *(personal.)*

**E23 — Use the STAR story-bank + interview-prep modes for your own (and your coachees') interview prep.** `match-star.mjs` + `interview-prep/` = a reusable behavioral-interview toolkit; the STAR+Reflection framing ("juniors describe what happened, seniors extract lessons") is a Scrum-coaching artifact. *(personal + coaching.)*

---

## Surface F — Vault-meta (follow-ups the ship opens)

**F24 — Write the "agent-first operational pipeline" synthesis + watch the class for N=2.** career-ops v200 joins OpenMontage v188 as an "agent-first end-to-end operational pipeline (coding-agent-as-runtime, deliverable = artifacts)" in a distinct domain. Log the pattern; if a third appears (a 3rd agent-first operational pipeline in yet another domain), the class is promotion-eligible. Also log the vault-meta resonance (career-ops's "files are canonical, DB derived" = the vault's own founding pattern shipped as a product) and re-confirm the NO-MINT alternative at the badly-overdue ~v192 audit. *(vault-meta.)*

---

## The fence (mandatory before any install)

- **`install-snapshot` + `npm-security-check @santifer/career-ops`** before `npx @santifer/career-ops init` (the `postinstall` downloads ~170 MB Chromium via Playwright; 4 minimal deps; node:sqlite needs Node ≥22.5).
- **Scratch dir + throwaway CV** for the first run (C11) — never point it at real PII until you trust the loop.
- **BYO provider key, review every generated line** — the tool warns AI "may fabricate skills/history; you must manually verify."
- **ToS:** it scrapes *public no-auth* ATS APIs only; do not extend it to scrape login-gated platforms or to mass-apply.
- **hireui work:** DESIGN/spec-only until hireui chooses to add LLM spend; on an `agent-*` branch (I-2), operator-installs-skills (I-8), rooted in hireui, GitNexus-first — per its CONSTITUTION.
- **Pin the commit:** `e9bacc48` (v1.18.0) for reproducibility.

---

**Ladder in one line:** A1 (read the brain) → **B5** (steal the anti-fabrication rules, zero install) → **C11** (one scratch evaluation) → **D16** (mirror the rubric into hireui's first LLM feature on an `agent-*` branch) — with E22 as the honest personal use and F24 as the vault-meta follow-up.
