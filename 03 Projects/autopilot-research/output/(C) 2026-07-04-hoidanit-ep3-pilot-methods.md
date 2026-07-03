# (C) Pilot methods — hoidanit ep-3 (MVP + environment + frontend init) → Storm Bear workflows

> **Source knowledge:** `wiki/hoidanit-fullstack-vibe-coding/` ep-3 deepening (2026-07-04): [[mvp-scoping-method]] · [[frontend-env-setup-workflow]] · [[vite-react-init-workflow]] · [[version-pinning-procedure]] — verified via `wf_f3c7237f-4c4`.
> **Relationship to the ep-4 menu:** this menu is ep-3-specific and COMPOSES with `(C) 2026-07-04-hoidanit-vibe-coding-pilot-methods.md` (19 methods). No duplicates: where the ep-4 menu already has a method (docs-first constraint = old-A1, error-triage = old-A2, series subscription = old-C2, VN onboarding = old-D1, docs-vs-AI-init bake-off = old-E1), this menu extends rather than repeats.
> **Ranked headline picks at the bottom.**

---

## A — hireui (Goal #2 target; obeys hireui CONSTITUTION I-2/I-8; all zero-install)

**A1 — Pin-procedure constraint line into the hireui harness.** Add one line to the harness constraints (beside the ep-4 docs-first + error-triage lines): *"Dependency changes: start from a committed baseline; list updates before applying (`ncu`-style); prefer exact pins over `^`/`~` for anything an agent will later reason about; the package-manifest diff is a first-class review artifact in the PR."* Eric's stated rationale is agent-native: a fix valid on one substrate may not replicate on a drifted one. Cost: ~10 min. Measure: do agent-authored dependency PRs become reviewable-at-a-glance?

**A2 — MVP-scope the first LLM feature with the AI-draft → human-red-pen procedure.** Before building the candidate-summarizer (mosh-thread A2-seam → A1-summarizer plan), run ep-3's scoping method verbatim: prompt the model for the feature's MVP checklist → audit it for the missing structural item (Eric caught "user management"; yours might be auth-scoping or PII handling) → write the curated checklist + **defer-list-with-reasons** into the feature spec. Cost: 1 session. Artifact: a scope doc the CONSTITUTION reviewers can gate on.

**A3 — "Deferred (with reasons)" as a spec convention.** Adopt the COD-style cut pattern: every hireui feature spec ends with deferred items, each carrying a stated reason (cost / complexity / covered-elsewhere / market-informed). Composes with jsm-six-file Scope-Limits. Cost: template edit.

**A4 — Dependency-drift audit (read-only).** Run an `ncu`-style list-only pass over hireui's manifests: count range-char deps vs pins, note the widest drifts. No changes — a report for deciding pin policy. Operator-run per I-8. Cost: ~30 min. Output: drift table in the pilot log.

**A5 — Frontend-dependency sustainability check.** The Tailwind datum (usage all-time-high, revenue −80%, 75% eng layoffs Jan 2026) is a live warning that AI codegen decouples usage from maintainer income. One-pager: hireui's core frontend deps → funding model → bus-factor → what breaks if maintenance stalls. Cost: ~1h. (Not an argument to drop Tailwind — an argument to *know* your substrate's health.)

## B — this pipeline / personal harness (self-improvement from this ship's own findings)

**B1 — Patch the digest/verify prompts against the "discard-as-garble" misfire. [HEADLINE]** This ship proved the failure: the ep-4 pass DISCARDED "Vite acquired by Cloudflare" as caption garble — it was real, 18 days old. Add to the digest-agent + verifier prompt templates (in the routine skill + workflow snippets): *"Before discarding a claim as garble, if it is a date-sensitive news/ecosystem claim (acquisition, release, pricing, shutdown), run ONE search; discard only after the search comes back empty."* Cost: ~10 min. Prevents a demonstrated, recurring class. Prime-directive material.

**B2 — Codify "baseline commit before any tool mutates" as a loop invariant.** Eric teaches beginners exactly the posture agent-supervision needs: commit → tool acts → read the diff → keep/discard. Write it into the autopilot routine + pilot skills as an explicit invariant line (it is practiced ad hoc today). Cost: ~15 min.

**B3 — Exact-pin the pipeline's own env.** `.venv` deps (notebooklm-py etc.) and any scaffold the sandbox creates: strip ranges, pin exact, record registry timestamps in `raw/_inventory.md` env notes. Low urgency; do at next env rebuild.

**B4 — Adopt the release-URL-pattern trick for tool installs.** Ep-3's nodejs.org/download/release/vX.Y.Z URL-swap teaching generalizes: prefer direct versioned release URLs (pin + provenance in one string) over "download latest" pages in any setup doc this vault writes. Cost: writing habit.

## C — vault + Storm Bear corpus

**C1 — Open the "overturned-discard ledger" as a wiki convention.** This ship added a `⚠️ OVERTURNED` section to the topic's caveats file. Adopt it corpus-wide: when a later pass proves a discarded claim true, the overturn gets logged as loudly as a correction. Instrumented prime directive. Cost: convention note in the routine skill.

**C2 — Queue the AI-breaks-docs-funded-OSS observation for the v66 Storm Bear mini-audit.** Tailwind (docs traffic −40%, revenue −80% while usage peaks) is the package-ecosystem edition of google-zero-open-web's zero-click mechanism. Two independent instances = observation-track candidate ("AI answer-layers sever usage from the funding surface"). Queue line only (scope clamp — no Storm Bear writes from here).

**C3 — Ep-5 ingest with a date.** Ep-3/4 cadence is now deterministic: live Mondays 19:30 ICT, VOD Wednesdays. Ep-5 (React fundamentals; react.dev/learn/thinking-in-react per the doc) lands ~Wed 2026-07-08; the AI-consultation-agent episode later in the series remains the high-value target. Update the `raw/topics-queue.md` line with the concrete date. Cost: 1 line.

## D — Scrum coaching / team practice

**D1 — Sprint-0 MVP workshop template from the ep-3 procedure.** AI drafts the MVP checklist in front of the team → team red-pens it (find the missing user-management-class item) → defer-list-with-reasons → paste into the sprint doc. Add the canonical nuance Eric omits: a validated-learning question per kept feature ("what does shipping this teach us about users?"). Ready-to-run 45-min workshop.

**D2 — Env-literacy onboarding module (extends ep-4 menu's D1).** Ep-3's middle hour is a complete junior curriculum: platform-vs-tool ("don't study the OS"), LTS/EOL/even-major policy, one-version rule, terminal literacy, npm-registry mental model. For VN juniors it's already in Vietnamese, first-party, free. Action: link ep-3 + the two wiki articles into the onboarding doc draft.

**D3 — Diff-reading drill as agent-readiness training.** Eric's git segment doubles as the minimum agent-supervision skill: if you can't read the package.json diff, you can't supervise the tool that wrote it. Team drill: every AI-generated change reviewed as before/after diff; discard-changes practiced as the undo. Pairs with D1 of the multi-agent-orchestration menu.

## E — evals / measurement (`evals/` harness)

**E1 — Substrate-drift fix-reproducibility eval.** Eric's pinning rationale is testable: take one known error + its AI fix on a pinned scaffold; replay the same prompt on a range-drifted scaffold N months newer; measure fix-replication rate. Small (5–10 cases), novel — directly prices the "pin for AI reproducibility" claim.

**E2 — Token-cost leg for the docs-vs-AI-init bake-off (extends ep-4 menu's E1).** Eric's third docs-first reason is quantifiable: AI-init a Vite React app vs `npm create vite` + download-starter; record output tokens, wall-clock, and post-init error count. One evening; produces the number his claim implies.

---

## Skip list (deliberate non-adoptions, with reasons)
- **Vanilla-CSS-first / no-Tailwind** — beginner pedagogy, not production guidance; hireui keeps its stack (but see A5).
- **COD / e-commerce feature specifics** — domain mismatch; only the *defer-with-reasons* pattern transfers.
- **nvm-windows / Windows Terminal material** — operator is on macOS.
- **Buying Copilot at "$15"** — figure remains refuted ($10 Pro); tool-selection thread already settled (Claude Code).
- **Re-scaffolding anything with create-vite today expecting the video's dep list** — template has drifted to oxlint; use the wiki's template-drift note instead.

## Critic reframe (steelman against this menu)
The obvious objection: "this is beginner content; the operator runs a 60-wiki pipeline and a production SaaS." The steelman flips it: ep-3's procedures are **agent-supervision primitives dressed as beginner lessons** — baseline commit, diff-as-review, pinned substrate, AI-draft-human-audit. The most junior-looking material in the series is precisely what generalizes to supervising agents (Eric says so himself: "AI will do this git part for you — learn it manually first"). The risk in this menu is not low value; it's *redundancy* — several methods (B2, D3) formalize things partially practiced. The mitigation is that formalizing them (constraint lines, invariant lines) is exactly what makes them survive context resets — this vault's founding lesson.

## Ranked headline (if you only do three)
1. **B1** — patch the discard-as-garble misfire into the pipeline prompts (10 min; prevents a demonstrated failure; prime directive).
2. **A1 + A2 together** — pin-procedure constraint line + MVP-red-pen scoping on the first LLM feature (zero install; rides the already-headlined hireui thread from the ep-4 menu).
3. **E2** — token-cost leg of the init bake-off (one evening; converts the series' most-quoted claim into a measured number).

## Suggested next action (Storm Bear prime directive)
Do B1 now (it edits this project's own skill files — inside scope, 10 minutes), then take A1+A2 into the next hireui session alongside the ep-4 menu's constraint lines. Ep-5 lands ~Wed 2026-07-08 (C3): one queue line today keeps the series thread warm.
