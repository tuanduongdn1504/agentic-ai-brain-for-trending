# (C) Pilot methods — hoidanit-fullstack-vibe-coding → your workflow

> **Source topic:** `wiki/hoidanit-fullstack-vibe-coding/` (compiled 2026-07-04; verify `wf_b1314fa6-590`, deepen/review `wf_8bf5253d-aa2`)
> **What the topic gives you:** four transferable disciplines (docs-first-AI-second · error triage · version pinning · beginner pedagogy/cohort harness) + a live VN series building an e-commerce app **with an AI consultation agent** — the same shape as hireui's Goal-#2 first LLM feature.
> **Ranked menu. Each method: what / how / effort / measure. Compose freely; the headline path is marked ★.**

---

## A — hireui / Goal #2 (agent-harness constraints + the consult-agent parallel)

**A1 ★ Docs-first constraint line in the hireui harness** — Add one behavioral constraint to the constraints-bank you're already running on Candidate-Detail (from the JSM pilot): *"Project initialization, dependency adds/upgrades, and tool config follow the official docs for the pinned version; cite the doc page in the diff. AI proposes; docs decide."* Zero install, ~10 min (hireui rules per its CONSTITUTION, agent-* branch). **Measure:** count of dependency-related agent misfires before/after over 2 weeks.

**A2 ★ Error-triage guardrail line** — Second constraint line: *"Fix ERRORs. List WARNINGs (audit/deprecation) in the report; never auto-fix warnings unless the task says so."* Protects surgical diffs in the v189 PR-babysitter loop and keeps the Candidate-Detail diffs reviewable. ~5 min. **Measure:** warning-churn lines in agent diffs; babysitter noise rate (feeds the v189 <20% noise bar).

**A3 Pin-and-verify dependency guard** — Eric's pin discipline + your existing `npm-security-check` skill composed: agent must quote the exact registry version (`registry.npmjs.org/<pkg>/latest`) and pin it (no `^`/`@latest`) in sandbox/hireui work. Directly addresses the class of failure in your lint-staged version-gate incident. ~15 min to encode as a rule; compose with install-snapshot for globals. **Measure:** zero drift-class breakages in pilot branches.

**A4 ★ The consult-agent parallel (Goal-#2 spec input)** — The series' end-boss feature — "AI Agent hỗ trợ tư vấn sản phẩm" on a boring CRUD app — is hireui's candidate-consultation agent with the nouns swapped. Action now: add one section to the running first-LLM-feature spec thread (Mosh A2-seam → A1-summarizer → A6-evals; agent-memory A1 files-first): *scope the AI as ONE feature of the boring app, never the app*. Action later: ingest the series' agent episode when it lands (see C2) as the beginner-grade reference implementation to sanity-check your scoping against. ~30 min now.

**A5 Version-matched docs for agent context** — When the agent works hireui's Node backend, point it at docs *for the pinned major* (Eric's read-old-docs skill, harness-encoded): keep a `docs-versions.md` (or AGENTS.md block) mapping core deps → doc URLs at the right version. ~30 min. **Measure:** fewer wrong-API-version suggestions.

## B — personal Claude Code harness

**B1 "If docs can answer, docs answer" — 13th-rule candidate** — Your vault CLAUDE.md Rule 5 says "if code can answer, code answers." Eric's stated position is its documentation sibling; his cross-platform-test-coverage rationale is the strongest argument form (docs are the better-*tested* artifact, not just fresher). Trial it as a project-level rule in one repo before promoting to the 12-rule block (Rule-set changes deserve their own deliberation per your conventions). ~10 min to trial.

**B2 Warning-chasing token audit** — Instrument one week of your own sessions (ccusage / loop-log) and count tokens spent on warnings nobody asked about. If it's >5% of agent output tokens, A2's rule graduates from hireui to your global settings. ~20 min setup, composes with the observability pilot (C1 ccusage).

**B3 Freeze-the-substrate pre-flight** — Before any multi-session agentic refactor: pin toolchain versions + commit the lockfile *first* (you already pin commits in the v189 fence — extend to toolchain). One checklist line in your loop conventions. ~5 min.

## C — vault / autopilot-research / Storm Bear

**C1 VN-ASR garble rule → yt-pipeline skill** — This topic re-confirmed: Vietnamese auto-captions systematically garble tool names + version numbers ("Clot Code", TS/ESLint cross-contamination). Add to `(C) yt-pipeline.md`: *"VN-source numeric/tool-name claims require a second source before quoting; flag caption-derived items explicitly."* You now have 4+ VN sources; this is a standing hazard class. ~10 min.

**C2 ★ Series subscription (live-topic tracking)** — First LIVE weekly series in the wiki. Add to `raw/topics-queue.md`: *"TODO: re-drain PLPTXD_6Mbmh4 when episode ≥5 lands (yt-dlp playlist check); PRIORITY when the AI-consult-agent episode ships."* The routine has no subscription primitive — this queue line is the minimum viable version (a v2 routine candidate if it recurs). ~5 min.

**C3 Storm Bear Pattern-Library feed (v66+ mini-audit queue)** — Two observations to queue: (1) **vibe-branding/discipline-content inversion** — a series *named* vibe coding that teaches anti-vibe discipline; evidence for the Pattern #51 spectrum reformulation already on the v66 agenda (sibling of v61's anti-vibe-with-pragmatic-acknowledgment). (2) **Pattern #55 VN archetype**: first first-party VN commercial-educator source (73b sub-variant strengthening; Eric ≈ VN Mosh). Queue lines only — no audit now. ~10 min.

**C4 Cohort-harness template note** — Doc + Drive starters + weekly livestream = a zero-LMS teaching harness. File as a `00 Notes/` candidate for your own future teaching (see D-block) — the interesting part is the *evolving single doc* as syllabus-of-record (a human GOALS.md).

## D — Scrum coaching / team enablement (unusually strong fit this topic)

**D1 ★ VN junior-onboarding curriculum decision** — You coach VN teams; this is a free, vetted (by this verify pass), VN-language, AI-era beginner series teaching *discipline inside vibe coding*. Decision: adopt episodes 1–4 as the junior-dev onboarding track, wrapped with your own two additions (A1 docs-first rule + A2 triage as working agreements). ~1h to review ep-1/ep-2 digests + write a 1-page track doc. **Measure:** onboarding time-to-first-verified-PR for the next junior.

**D2 Error-triage dojo + warning budget** — 15-minute team dojo on INFO/WARN/ERROR triage; then a sprint-level "warning budget" (warnings are backlog items with a cap, not mid-task detours). Turns Eric's beginner lesson into a team working agreement with a burndown. ~1h prep.

**D3 Docs-first as an AI-adoption working agreement** — For teams adopting AI assistants: *"AI-generated setup/config changes must link the official doc they follow."* It's the most enforceable anti-hallucination rule that fits in one sentence — reviewable in PRs, no tooling needed. **Measure:** AI-assisted setup incidents per sprint, before/after.

**D4 Weekly build-together cadence** — The Monday-19:30 90-minute build-livestream format, internalized: a weekly 1h "build together" session on a real team project (screen-shared agent driving, triage narrated). Cheap engagement mechanism; the format itself is the import, not the content.

## E — evals / measurements

**E1 ★ Docs-vs-AI-init bake-off** — Test Eric's core claim empirically on your `evals/` harness: scaffold the same NestJS (or hireui-stack) app twice — (a) agent free-styling from its own knowledge, (b) agent constrained to docs-first + pins. Score: deviations from official scaffold, errors hit, tokens, wall-clock. This is a *measured* answer to "does docs-first actually matter with 2026 models," and a Goal-#2 evidence artifact in the cc-sdd/JSM bake-off family. ~2-3h.

**E2 Warning-churn measurement** — The A2/B2 rule, quantified across a week of v189 babysitter runs: % of diff lines touching non-requested warning fixes. Feeds the L1→L2 graduation evidence.

**E3 VN-ASR garble-rate sample** — Across your 4 VN sources: sample 20 caption-derived numeric/tool-name claims vs verified ground truth; publish the error rate into the wiki as the standing correction factor for VN sources. ~1h; makes C1's rule evidence-backed.

---

## Skip list (deliberate non-actions)

- **Don't adopt the series' stack** (MySQL/Workbench/NestJS-as-choice) anywhere — hireui has its own stack; Workbench's "beginner standard" status is contested anyway.
- **Don't buy the paid courses** for yourself — the free series + your corpus already covers this tier; revisit only if D1 juniors need the Claude Code course specifically.
- **Don't downgrade your own tooling** to the student stack (Copilot+Gemini) — it's a cost-tier for cohorts, not a recommendation for you.
- **Don't build the e-commerce app** — track it (C2), don't clone it.

## Critic reframe (what this topic is NOT)

The four disciplines are beginner-scale restatements of things your corpus already holds at senior scale (docs-first ≈ Rule 8 read-before-write + Rule 5's sibling; pinning ≈ harness-engineering vendoring; triage ≈ Rule 3 surgical changes). The *new* value is: (1) the **VN-language teachable form** — D-block is where this topic uniquely pays; (2) the **live series arc toward a beginner-grade AI-consult-agent build** on your stack family (A4/C2); (3) the **testable claim** behind docs-first (E1). If you do only three things: **A1+A2 (15 min, running work) → C2 (5 min) → D1 (decide this week)**.

## Suggested next action

Apply A1+A2 to the hireui constraints-bank in the current Candidate-Detail session (agent-* branch, CONSTITUTION rules), add the C2 queue line, then decide D1 after skimming the ep-1/ep-2 digests in `raw/`.
