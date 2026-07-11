# (C) Pilot methods — System Thinking (Thầy Hoàng / Naur 1985) → your working flow

> **Source topic:** [[system-thinking-ai-coding]] (video `t8_M8Ql1Q1I`, 2026-06-29) + the original resource **Peter Naur, "Programming as Theory Building" (1985)**.
> **Date:** 2026-07-07 · **For:** Storm Bear (software dev + Scrum coach; Goal #2 = ship real software with these tools).
> **What this talk actually gives you:** not a tool, but a **vocabulary + a training regimen** — the **3 golden questions** (a gate) and the **4 practice steps** (a habit), grounded in Naur's claim that *the program is the theory in your head; code is only its shadow; a program dies when the theory-holding team disperses.*

## How to read this

- **24 methods** across 5 tracks: **A** hireui (Goal #2) · **B** vault + autopilot-research pipeline · **C** personal Claude Code harness · **D** Scrum coaching · **E** evals/measurement.
- Each is tagged **effort** (S/M/L) and **value**, with the concrete artifact it produces. Almost everything here is **zero-install** — the whole point of the talk is that the leverage is in *habits and gates*, not tooling.
- hireui methods respect its CONSTITUTION (agent-`*` branches per I-2, operator-only skills per I-8, GitNexus-first, BMAD harness) — they are specs/gates for **you** to run inside hireui, not writes I make from here.

---

## ★ Headline recommendation (start here)

1. **A1 — The 3 golden questions as a hireui "definition-of-ready + PR gate"** (S effort, high value). One checklist, zero install, and it directly hardens the exact failure mode the talk describes for AI-generated code.
2. **A2 — "Design-before-prompt" + "reverse-review (make the AI write the docs, then you validate them)"** layered into the *running* Candidate-Detail refactor (S/M). This is the single most transferable technique in the video and it fights the token-drift you already flagged on that screen.
3. **A4 — The "theory-rebuild doc" as the anti-dead-program ritual for hireui's first LLM feature** (M). Naur's insight applied where it matters most: the match/explanation service you're about to build should ship with a human-held theory, not just working code.

Everything else deepens or generalizes these three.

---

## Track A — hireui (Goal #2: ship real software)

### A1 — 3 golden questions as a Definition-of-Ready + PR-review gate `S · high`
- Add three questions to the hireui PR template / ticket DoR (see [[three-golden-questions]]):
  1. **State ownership** — where does this feature's state live, and *who is the single owner*? (Two owners = the time-bomb.)
  2. **Feedback** — what signal tells us it's healthy vs. erroring, and where is error logic collected?
  3. **Blast radius** — what breaks if we delete this component? Can you trace it *without running it*?
- **Artifact:** `.github/pull_request_template.md` additions + a DoR line. Merge-block if any answer is "I don't know."
- **Why it fits:** it's a review rubric for *AI-generated* code specifically — the "runs fine at 20 users, dies at scale" defect the talk audits. Maps to hireui's BMAD gates.

### A2 — Design-before-prompt + reverse-review on the Candidate-Detail refactor `S/M · high`
- Before prompting: **draw the boxes+arrows** for Candidate-Detail (components, data flow, where the drifted tokens actually resolve). "If you can't draw it, you don't understand it — and the AI invents the parts you didn't draw" ([[four-practice-steps]]).
- After generating: don't merge fast — **make the agent write/refresh the doc + tests for the changed area, then you validate the doc** and ask back ("why this token path? what breaks if r1 tokens leak in?").
- **Why it fits:** your own spike root-caused Candidate-Detail as *drifted tokens + a half-finished r1→r2 migration* — a textbook "no theory in anyone's head" symptom. This forces the theory back in.

### A3 — hireui's first LLM feature written spec-first (WHAT/WHY before HOW) `M · high`
- The match-explanation service (from the [[miai-cv-matching-agent]] + [[mosh-ai-powered-apps]] threads) is your leading first-LLM-feature candidate. Write the **spec-as-scaffolding** first: problem, constraints, trade-offs, **definition of success, and the error scenarios you must test** — before any prompt.
- Sits cleanly behind the Mosh **A2 vendor seam** and the assistive-not-decisional rule from the miai thread.
- **Artifact:** a one-page spec in hireui's BMAD flow → feeds cc-sdd/OpenSpec if you pilot those.

### A4 — The "theory-rebuild doc" (anti-dead-program ritual) `M · high`
- Naur: a program *dies* when the team holding its theory disperses ([[naur-programming-as-theory-building]]). For any AI-heavy hireui module, keep a short **THEORY.md**: *how it maps to the recruitment domain, why each part is what it is, what's safe to change.*
- Make the agent draft it, you edit it, and treat "can a new dev revive this from THEORY.md?" as the real done-check.
- **Why it fits:** it's the cure for the exact risk of shipping AI-written features into a SaaS you'll maintain for years.

### A5 — Chaos-delete audit of one "impressive but suspicious" hireui area `S · med`
- Pick a screen that *looks* done (Candidate-Detail is the obvious one). For 3–4 key files, ask: **"if I delete this, what breaks?"** Anything you can't answer is a documented cognitive hole → a ticket.
- **Artifact:** a short `output/`-style audit note listing the holes. Cheap, and it produces a real backlog.

### A6 — "Easy, not cheap" tech-debt line in the hireui harness `S · med`
- Add a standing constraint to hireui's `CLAUDE.md`/BMAD rules: *AI may make code easy; it does not make it cheap — no God components (>~300 lines mixing concerns), no missing rate-limiting/error-handling on new endpoints, no UI designed before its data model.* These are the specific debts the talk audited.
- Pairs with the committed-secret/prod-gap grep-gate from [[fullstack-docker-cicd]].

---

## Track B — vault + autopilot-research pipeline

### B1 — Add a "draw-it / theory check" step to the compile routine `S · med`
- The autopilot routine already builds articles; add a micro-gate: for any *architecture/system* topic, the compile must answer "can we draw the system as boxes+arrows?" before shipping the article. Prevents shipping a summary you don't actually understand.

### B2 — Reverse-review discipline for wiki claims (already partly live) `S · med`
- Formalize what happened this session: the [[four-practice-steps]] step-4 ("make the AI explain, then validate") *is* the refute-first verify pattern — and today it caught a verifier's mis-correction of the Harvard-62M study. Add "verify the *correction*, not just the claim" to the digest/skeptic prompt templates (sibling to the discard-as-garble guard).

### B3 — Naur "programming-as-theory-building" as a Storm Bear observation-track anchor `M · med`
- This is the corpus' first pure-thesis Naur restatement. Queue an observation-track note for the v66+ mini-audit: *theory-retained-in-humans-not-lines-emitted* as a recurring principle (it under-writes harness-engineering, elicit-verifiable-agent-dsl, agent-memory-architecture). See [[caveats-and-corrections]].

### B4 — Spec-as-scaffolding for the pipeline's own new features `S · low`
- Eat your own dog food: the next change to the autopilot routine gets a 5-line WHAT/WHY/success/error-cases spec before code. Cheap habit; mirrors the talk's step 2.

---

## Track C — personal Claude Code harness

### C1 — "Design-before-prompt" as a plan-mode default `S · med`
- Make plan-mode / a `/design` step mandatory for any non-trivial task: force the boxes+arrows (or ERD) *before* the first edit prompt. This is [[four-practice-steps]] step 1 as a harness habit; complements your v189 loop.

### C2 — A `/reverse-review` skill (make the agent defend the diff) `M · med`
- A small skill that, on an important diff, asks the agent: *explain each change, the risk you weighed, extensibility, the trade-off* — then writes/updates the doc for the touched area. You validate. Turns step-4 into a one-command ritual.

### C3 — Compiler-vs-LLM "always verify" as a loop invariant `S · med`
- Bake the [[compiler-vs-llm]] point into the loop/PR-babysitter: nothing AI-authored merges without an explicit verification step (test run, or a human check). "Same prompt, different answer" is *why*, not paranoia. You already run a PR-babysitter (v189) — this is a one-line policy add.

### C4 — Weekend "hand-code from memory" muscle rep `S · low`
- The talk's juniors-advice generalizes: once a week, re-implement one small thing by hand from memory to keep the system-thinking muscle alive. A personal-discipline note, not tooling. Low value-density but zero cost and genuinely on-thesis.

---

## Track D — Scrum coaching (your strongest non-code leverage)

### D1 — Teach the 3 golden questions as a team DoR ritual `S · high`
- The three questions are a ready-made **facilitation tool**: run them in refinement for any AI-assisted story. They make "is this actually understood?" concrete and non-personal. See [[three-golden-questions]].

### D2 — "AI-as-patient-teacher, not homework-machine" for junior onboarding `M · high`
- The talk's junior strategy is a curriculum: teach juniors to ask AI *why/trade-offs/plan-with-pros-and-cons*, not "write my code," + a weekly hand-code rep. Pairs directly with the VN junior-onboarding angle from [[hoidanit-fullstack-vibe-coding]]. **Artifact:** a one-page onboarding guide.
- Grounded in real 2026 hiring data ([[junior-crisis-and-hiring-2026]]): IBM is *tripling* entry-level hiring because firms can't refill the senior pipeline — a strong, verified talking point for advocating apprenticeship over "just use AI."

### D3 — The "struggle-school is severed" retro prompt `S · med`
- Run a team retro on: *what friction did AI remove that used to teach us — and how do we replace that learning deliberately?* Turns the talk's thesis into a team-improvement action.

### D4 — Reframe "velocity" as theory-retained, not lines-shipped `M · med`
- Coaching move drawn from Naur: a team that ships AI code nobody understands is accruing invisible risk (a "dead program" that still runs). Introduce a health signal — *can someone other than the author explain why each part is what it is?* — alongside velocity.

---

## Track E — evals / measurement

### E1 — Turn the 3 golden questions into a repo-scannable checklist eval `M · med`
- You already have an `evals/` harness (anchor-validation gate shipped in `bin/autopilot-drain.py`). Add a lightweight eval that, for a changed module, checks the three answers are *documented somewhere* (state owner named, error path present, blast-radius note). Systematizes "always verify."

### E2 — Reverse-review as a graded eval for the match feature `M · high`
- For hireui's first LLM feature, make "the agent can produce a correct THEORY.md + passing tests for its own output" a scored gate — the eval-first, recruiter-labeled-pairs discipline from the miai thread, now with a *comprehension* axis, not just accuracy.

### E3 — Jagged-frontier probe: log where the model is silently wrong `S · med`
- Keep a running note (per the [[code-vs-architecture-and-tech-debt]] jagged-frontier point) of tasks where the model looked confident but was wrong on hireui work. Over a few weeks this *maps your frontier* — the highest-value cheap measurement here.

---

## Skip-list (what NOT to adopt from this video)

- **The VPS-self-hosting / "devs go to the chicken coop" end-state** — that's the bootcamp's upsell. Weigh managed-vs-self-hosted on merits ([[fullstack-docker-cicd]], [[self-hosted-devops-oss]]); don't self-host hireui just because a talk framed it as mastery.
- **"Prompting keeps getting easier / needs less context"** — a directional opinion, contested by the context-/harness-engineering literature ([[harness-engineering]], [[claude-md-12-rules]]). Don't downgrade your CLAUDE.md/harness investment on this claim.
- **"20–30% of devs will survive" / "only a few remain"** — motivational, uncited. Don't quote as data.
- **Buying the bootcamp to get the method** — the method *is* the 3 questions + 4 steps, fully captured here for free. Buy the course only if you want the community/accountability, not the content.
- **Waterfall-reading of "finish the whole design in your head before coding"** — Naur's actual view is *iterative* theory-building ([[naur-programming-as-theory-building]] fidelity table). Design-before-prompt ≠ big-design-up-front.

---

## Critic reframe (the strongest objection, answered honestly)

- **"This is just 'think before you code' with new nouns — is there anything here I don't already know?"**
  Largely, yes, you know the principles. The value is threefold: (1) it gives you **crisp, teachable artifacts** (3 questions, 4 steps) that a Scrum coach can drop into refinement/onboarding tomorrow; (2) it names the AI-specific failure mode precisely — *the program is born dead when the AI writes it and no theory lands in a human* (Naur), which is a sharper frame than "tech debt"; (3) it's **verified** — the empirical spine (jagged frontier, Harvard-62M, IBM 3×) is real, so you can cite it in coaching without hedging.
- **"So the honest ROI?"** The gate (A1) and the reverse-review habit (A2) are near-free and directly attack the drift you already found on Candidate-Detail. The rest is reinforcement. If you do *nothing else*, do A1 + A2 this week and D1/D2 in your next coaching cycle.

---

## Suggested first action

Adopt **A1 (3-question PR/DoR gate)** and **A2 (design-before-prompt + reverse-review)** on the *running* Candidate-Detail work — both zero-install, both inside hireui's existing BMAD/PR flow — and slot **D1/D2** into your next Scrum onboarding cycle. Then, when you spec hireui's first LLM feature, wrap it in **A3 + A4** so it ships with a theory a human holds, not just code that runs.
