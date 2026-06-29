# Pilot methods — applying the GPT-5.5/Taste-Skill web-design workflow to your flows

> **Source:** [[ai-web-design-workflow/_index]] — Lukas Margerie "Redesigning Websites with GPT-5.5 & Images 2.0" ([PFO01z7Qe38](https://www.youtube.com/watch?v=PFO01z7Qe38)) + a double deep-dive of its four originals ([Taste Skill](https://github.com/leonxlnx/taste-skill), GPT-5.5/Codex, ChatGPT Images 2.0, Seedance 2.0), adversarially verified (Workflow `wf_8b23bf2d-231`, 14 agents). Verification log: [[ai-web-design-workflow/source-provenance]].
> **Date:** 2026-06-20.
> **Your flows (from vault + memory):** **(A)** your **Claude-Code skills / `~/.claude`** setup; **(B)** **hireui** — the Goal-#2 recruitment SaaS (TalentAxis frontend; Claude Code + BMAD; CONSTITUTION I-2 agent-* branches + I-8 operator-only skill registry; GitNexus-first; **no LLM in product yet**); **(C)** the **autopilot-research vault** (HTML `output/` deliverables); **(D)** your **writing/prose** across both vaults; **(E)** **Scrum coaching / team**.
> **24 methods, ranked.** Each has the source pattern, a concrete first step, and a success signal.
>
> **The headline:** the video is an OpenAI/Codex demo, but **the only durable, transferable asset is the [[ai-web-design-workflow/taste-skill-deep-dive|Taste Skill]]** — an MIT, ~47K★ design-discipline skill that **runs natively in Claude Code**. And the video's "Codex beats Claude at front-end" is **contradicted by evidence** (Opus rates more polished; Altman acknowledged GPT-5.5 trailed on front-end at launch). So the play for a Claude shop is: **adopt the skill, stay on Claude, ignore the OpenAI framing.** The single highest-leverage move is **B1 — run hireui's frontend through the Taste Skill's 62-point redesign gate.**

---

## ▶ Start here (recommended sequence)

1. **Today, ~20 min, zero risk:** **A1** — install the Taste Skill in Claude Code on a *throwaway* page (`npx skills add https://github.com/leonxlnx/taste-skill`), run `/redesign`, and see the 62-point gate in action. Pin a commit; you can fork it (it's MIT).
2. **This week, highest leverage (Goal #2):** **B1 + B2** — on a hireui **`agent-*` branch**, run the TalentAxis frontend through the Taste Skill audit and capture before/after; then bank the **62-point pre-flight as a hireui design-QA gate** in `_bmad-output`. (Operator installs the skill — **I-8**.)
3. **Make the gate *real*, not vibes:** **A4** — turn the code-checkable subset (em-dash, Inter-default, 3-equal-cards, `window.addEventListener('scroll')`) into a grep linter + a Claude Code hook, so "passes the gate" is enforced, not asserted.
4. **Before you trust any of it for client work:** **B5** — a 3-task Claude-vs-Codex bake-off on your `evals/` harness, so the model choice rests on *your* data, not a 7-minute video.

---

## Ranked table

| # | Method | Flow | Effort | Value | Why it ranks here |
|---|---|---|---|---|---|
| **B1** | Run hireui's frontend through the Taste Skill `redesign` gate | B hireui | Med | **High** | Goal #2; a real frontend + a free, portable quality lever |
| **A1** | Install + try the Taste Skill in Claude Code (throwaway page) | A skills | **Low** (~20m) | **High** | The whole topic's payload; zero-risk, Claude-native |
| **B2** | Adopt the 62-point pre-flight as hireui's design-QA gate (BMAD) | B hireui | Low | **High** | Turns "looks AI-made" into a checkable merge gate |
| **A4** | Code-checkable subset → grep linter + Claude Code hook | A skills | Med | **High** | Makes the manual gate an actual gate; reusable everywhere |
| **A2** | Fork + own the 62-point checklist as your skill (de-risk leonxlnx) | A skills | Low–Med | **High** | Pseudonymous author = bus-factor; MIT lets you own it |
| **B5** | Claude-vs-Codex 3-task bake-off on `evals/` (your data) | B hireui | Med | **High** | Kills the video's unsupported "Codex wins" claim with evidence |
| **A3** | Compose with Anthropic `frontend-design` skill + Claude Design | A skills | Low | Med–High | The first-party Claude-native analogs; keep the better discipline |
| **A5** | Adopt the one-line "Design Read" handshake before any UI build | A skills | Low | Med–High | Cheap brief-inference discipline; prevents cliché defaults |
| **D1** | "AI tells = mechanical checks" as a unified anti-slop lint (prose + UI) | D writing | Low | Med–High | Composes em-dash ban with Humanizer / signs-of-AI-writing |
| **B3** | Image-restyle sub-loop for hireui marketing/careers pages | B hireui | Med | Med | Real use; tool-agnostic; respects "no LLM in product" (build-time) |
| **C1** | Use the Taste Skill for the vault's HTML `output/` deliverables/Artifacts | C vault | Low | Med | Your "front-end slides" analog; instant polish on one-pagers |
| **E2** | Teach "the skill is the moat, not the model" (model-agnostic adoption) | E coaching | Low | Med | The single most transferable lesson from this video |
| **B7** | One-design-system discipline to align TalentAxis components | B hireui | Med | Med | Reduces UI drift; concrete from the rubric |
| **E3** | Teach the model-comparison discipline (don't trust single-prompt demos) | E coaching | Low | Med | Generalizes B5; agent-literacy for teams |
| **A6** | Steal the rubric's *named* anti-patterns into your code-review checklist | A skills | Low | Med | The catalogue is reusable beyond the skill |
| **D2** | Add the em-dash ban to vault/human-facing prose (soft version) | D writing | Low | Med | Ironic-but-real: your wiki leans on em-dashes |
| **B4** | Muted hero-video background for hireui's public landing | B hireui | Med | Low–Med | Nice-to-have; weigh against CWV/perf cost |
| **E1** | Teach "vibe-designing" + the 5-step loop as an AI-literacy lesson | E coaching | Low | Med | Sharp framing for design/PM teams adopting AI |
| **C2** | Generate replacement section imagery for vault deliverables | C vault | Low | Low–Med | Optional polish; any image model |
| **A7** | Wire the redesign gate as a `verify`/eval step before frontend merges | A skills | Med | Med | Closes the loop with [[prompt-evaluation/_index]] |
| **B6** | Constitution-compliant adoption (I-2 branch, I-8 operator-install) | B hireui | Low (rule) | **High** (guard) | Prevents a real governance violation |
| **D3** | Lift the rubric's image rule ("never div-fake screenshots, real images") | D/B | Low | Low–Med | Concrete content-honesty rule |
| **E4** | Run a team "design-tell hunt" workshop using the 62-point list | E coaching | Low | Med | Turns the checklist into a shared team rubric |
| **A8** | Track the Taste Skill upstream for new variants (image-to-code, brandkit) | A skills | Low | Low | Cheap awareness; the repo ships 13 variants |

---

## A — Your Claude-Code skills / `~/.claude` (adopt + adapt the Taste Skill)

> The Taste Skill is **Anthropic SKILL.md format** with a `.claude-plugin/plugin.json` — it installs and runs in **Claude Code** exactly as in Codex. This is where you capture the value with zero OpenAI dependency. Full anatomy: [[ai-web-design-workflow/taste-skill-deep-dive]].

### A1 — Install + try the Taste Skill in Claude Code ⭐
- **Pattern:** `npx skills add https://github.com/leonxlnx/taste-skill` (or `--skill "design-taste-frontend"` for just the core); restart to pick it up; run the `redesign` command on a page.
- **Apply:** spin a throwaway Next.js/Tailwind page, generate a generic landing, then run the skill and watch the 62-point pre-flight reshape it (em-dash purge, hero discipline, real images, no 3-equal cards).
- **First step:** install on a scratch repo today; pin the current commit (`git` the installed files) so an upstream change can't silently shift behavior.
- **Success signal:** the redesigned page is visibly "less AI-generated" *and* you can name *which* checklist items fired.

### A2 — Fork + own the 62-point checklist as your own skill ⭐
- **Pattern:** the rubric's value is a **named catalogue of LLM design tells → binary checks**; the author (`leonxlnx`) is pseudonymous (bus-factor), but it's **MIT**.
- **Apply:** extract the 62-point pre-flight + the dial definitions into a *your-namespace* skill you maintain; treat the upstream as a reference, not a dependency.
- **First step:** copy `skills/taste-skill/SKILL.md` into your skills repo, trim to the rules you actually enforce, add a header crediting leonxlnx (MIT).
- **Success signal:** your design discipline survives the upstream repo going dark.

### A3 — Compose with Anthropic's first-party design surfaces
- **Pattern:** Anthropic ships a **`frontend-design`** skill (in `github.com/anthropics/skills`, see [[claude-skills/source-provenance]]) and **Claude Design** (launched 2026-04-17, for prototypes/wireframes/visuals).
- **Apply:** run the same brief through the Taste Skill *and* `frontend-design`; keep whichever discipline produces cleaner output, or stack them (Taste Skill's mechanical gate + first-party generative defaults).
- **First step:** diff the two on one page; note where they agree (these are robust rules) vs disagree.
- **Success signal:** you have a Claude-native design stack you trust, no Codex needed.

### A4 — Turn the gate's code-checkable subset into a linter + hook ⭐
- **Pattern:** the 62-point pre-flight is a **manual** checklist (no shipped linter) — but a chunk of it is deterministically grep-able.
- **Apply:** write a small script that fails on `—` (em-dash) in built output, `Inter` as default font, three-equal-column card patterns, `window.addEventListener('scroll'`, missing `prefers-reduced-motion`; wire it as a [[claude-code-hooks/_index|PostToolUse/Stop hook]] (or CI gate).
- **First step:** start with the **em-dash grep** — one line, catches the #1 tell, instantly useful on prose *and* UI.
- **Success signal:** an em-dash or `window.addEventListener('scroll')` can't reach a merge without a loud failure.

### A5 — Adopt the one-line "Design Read" handshake
- **Pattern:** *"Reading this as: \<page kind\> for \<audience\>, \<vibe\>, leaning \<system/aesthetic\>"* — stated **before** any UI code (Taste Skill Section 0).
- **Apply:** make it a standing rule in your frontend `CLAUDE.md`/skill so the agent declares its read first; you catch a wrong interpretation in one line, not after a full build.
- **First step:** add the one-liner requirement to hireui's frontend agent instructions.
- **Success signal:** you correct a misread brief *before* code, not after.

### A6 — Steal the named anti-patterns into your code-review checklist
- **Pattern:** the rubric names the failures (3-equal cards, fake-screenshot divs, AI-purple gradients, Inter-default, mixed icon families).
- **Apply:** add these as explicit line-items to your frontend PR review template (vault + hireui).
- **First step:** paste the "Layout / Typography / Content" bans into your review checklist.
- **Success signal:** reviewers flag "this is the 3-equal-card default" by name.

### A7 — Wire the redesign gate as a verify/eval step
- **Pattern:** the gate is a quality bar; make passing it *measured*, per [[prompt-evaluation/_index]] (LLM-as-judge against the 62 items).
- **Apply:** before a frontend PR merges, run an eval that scores the diff against the checklist and trends the score.
- **First step:** encode 10 of the 62 items as an eval rubric; baseline current pages.
- **Success signal:** redesign quality is a number you can trend, not a vibe.

### A8 — Track the upstream for useful variants
- **Pattern:** the repo ships **13 variants** (image-to-code, brandkit, minimalist, brutalist, imagegen-frontend-web/mobile…).
- **Apply:** keep a note; pull `image-to-code-skill` if you ever screenshot→code, `brandkit` if hireui formalizes brand tokens.
- **First step:** skim the variant list once; note which map to a real future need.
- **Success signal:** you reach for the right variant when a need appears, instead of rediscovering it.

---

## B — hireui (Goal #2 — the headline target, it has a real frontend)

> hireui has a **TalentAxis frontend**, runs Claude Code + BMAD, and is **Claude-centric with no product LLM yet** — so this is build-time dev-tooling, fully within the rules. Respect the CONSTITUTION: **I-2** (work on `agent-*` branches), **I-8** (only the operator installs skills), GitNexus-first. Follow hireui's rules, not the vault's. [[hireui pilot target|memory: project_hireui_pilot_target]]

### B1 — Run TalentAxis frontend through the Taste Skill redesign gate ⭐⭐
- **Pattern:** the video's core move — `redesign` audits an existing site across 8 dims (typography/color/layout/interactivity/content/components/iconography/code-quality) and fixes in priority order (font → color → hover → layout → component → states → motion).
- **Apply:** on an `agent-*` branch, point the skill at one TalentAxis page (e.g. the candidate dashboard or the public landing), capture before/after screenshots + the checklist diff.
- **First step:** **operator** installs the skill (I-8); branch per I-2; run `redesign` on one page; do NOT let an agent auto-install it.
- **Success signal:** a measurably cleaner page + a list of named fixes you'd otherwise have eyeballed.

### B2 — Adopt the 62-point pre-flight as hireui's design-QA gate ⭐
- **Pattern:** an **all-or-nothing** mechanical checklist (em-dash=0, hero discipline, WCAG AA 4.5:1, one design system, real images, dark mode, reduced motion…).
- **Apply:** drop a trimmed checklist into `_bmad-output/runbooks/` as hireui's frontend "definition of done"; require it on frontend PRs.
- **First step:** create `frontend-design-qa-gate.md` with the ~20 items that matter for TalentAxis; reference it in the BMAD frontend workflow.
- **Success signal:** frontend PRs are checked against named criteria before merge.

### B5 — Claude-vs-Codex bake-off on your own `evals/` harness ⭐
- **Pattern:** the video's "Codex beats Claude" is a single-prompt opinion (evidence favors Opus 4.7 for front-end). Don't inherit the claim — *measure*.
- **Apply:** pick 3 representative hireui redesign tasks; run Claude Code (Opus 4.8) and (optionally) Codex/GPT-5.5 on each; score with the 62-point gate + your `evals/` graders + token cost + latency.
- **First step:** define the 3 tasks + the scorecard; run the Claude arm first (your default), Codex only if you want the comparison.
- **Success signal:** your model choice for client-facing frontend work rests on your data — and you can cite it.

### B3 — Image-restyle sub-loop for hireui marketing/careers pages
- **Pattern:** "redesign this section as an image from page context + a reference" → feed back to the agent → swap in. Tool-agnostic (any image model).
- **Apply:** for employer-branding / careers landing sections that need real imagery (not div-fakes), generate section images and have Claude Code swap them in at build time.
- **First step:** try it on one marketing section; keep generated assets in the repo, not a live API call (no product LLM).
- **Success signal:** a marketing page with real, on-brand imagery instead of placeholder boxes.

### B4 — Muted hero-video background for the public landing
- **Pattern:** animate a hero image (Seedance/Veo/Runway) → **mute** (audio is on by default) → embed as `<video>` background.
- **Apply:** only if hireui's landing wants motion; weigh Core Web Vitals (video weight) and reduced-motion compliance.
- **First step:** prototype on a branch; measure LCP/CLS before/after; gate on `prefers-reduced-motion`.
- **Success signal:** a hero that adds life without tanking performance or accessibility — or a clear "not worth it" decision.

### B6 — Constitution-compliant adoption (guardrail) ⭐
- **Pattern:** hireui rules: **I-8** operator-only skill registry, **I-2** agent-* branch policy, GitNexus-first.
- **Apply:** *you* install/vet the Taste Skill (run a quick supply-chain check — `npm-security-check` / `install-snapshot`); agents only *use* it on `agent-*` branches.
- **First step:** snapshot-install the skill yourself; record it in hireui's operator skill registry; never instruct an agent to `npx skills add`.
- **Success signal:** the skill is adopted without violating I-2/I-8.

### B7 — One-design-system discipline for TalentAxis
- **Pattern:** "one design system per project, never mix" (14 official options incl. Radix, shadcn/ui, Tailwind).
- **Apply:** audit TalentAxis for mixed component sources / icon families; converge on one.
- **First step:** inventory current UI libs + icon packages; pick one family; flag the rest for migration.
- **Success signal:** consistent components + a single icon family across the app.

---

## C — autopilot-research vault (HTML deliverables)

### C1 — Use the Taste Skill for HTML `output/` deliverables / Artifacts
- **Pattern:** the skill makes any LLM-built HTML page look non-generic — your equivalent of the video's "front-end slides."
- **Apply:** when you ship a pilot dashboard, a one-pager, or an Artifact from a vault topic, run it through the redesign gate.
- **First step:** next time you build an HTML deliverable, apply the em-dash ban + hero discipline + real-images rule.
- **Success signal:** vault deliverables look intentional, not auto-generated.

### C2 — Generate replacement section imagery for deliverables
- **Pattern:** the restyle-from-reference image loop (any image model).
- **Apply:** for a polished deliverable, generate real section images instead of placeholder divs.
- **First step:** try it on one report; keep assets local.
- **Success signal:** a deliverable with real imagery you'd be happy to share.

---

## D — Writing / prose discipline (transfers beyond UI)

### D1 — "AI tells = mechanical checks" as a unified anti-slop lint ⭐
- **Pattern:** the skill's whole thesis — *the "AI-generated look" is diagnosable as named tells, each a binary check.* This generalizes from UI to prose.
- **Apply:** unify the **em-dash ban** with the **Humanizer** + Wikipedia "Signs of AI writing" ([[claude-skills/original-wikipedia-signs-of-ai-writing]]) into one "anti-AI-tell" lint for human-facing output.
- **First step:** assemble a one-page tell-list (em-dash, "it's not just X — it's Y", "delve", three-equal structures) and a grep for the mechanical ones.
- **Success signal:** human-facing deliverables stop reading as machine-written.

### D2 — Em-dash discipline for vault / human-facing prose
- **Pattern:** the #1 LLM tell (this very vault, and these wiki files, lean on em-dashes heavily).
- **Apply:** keep em-dashes for *internal* vault notes (fine), but strip them from anything client/team-facing.
- **First step:** add an em-dash check to your deliverable-export step.
- **Success signal:** external docs read as human-authored.

### D3 — Lift the "real images, never fake-screenshot divs" content rule
- **Pattern:** the rubric bans div-based fake screenshots + pure-text minimalism + hand-rolled decorative SVGs.
- **Apply:** a content-honesty rule for any page you ship (vault or hireui).
- **First step:** add "no placeholder/fake imagery in shipped pages" to your DoD.
- **Success signal:** no more "obviously a placeholder" sections in shipped work.

---

## E — Scrum coaching / team

### E1 — Teach "vibe-designing" + the 5-step loop as AI literacy
- **Pattern:** the [[ai-web-design-workflow/overview|5-step loop]] (scaffold → taste-gate → restyle images → animate → swap) is a clean teaching artifact.
- **Apply:** a one-slide lens for design/PM teams: where the agent helps, where human taste + a checklist must gate.
- **First step:** turn the loop diagram into a one-pager.
- **Success signal:** a team adopts the loop *with* a quality gate, not just "let the AI design it."

### E2 — Teach "the skill is the moat, not the model" ⭐
- **Pattern:** the durable asset was a **portable skill**, not a model choice; everything vendor-specific decays fast.
- **Apply:** coach teams to invest in **portable discipline (skills/checklists)** over chasing the latest model.
- **First step:** use this video as the case study — "they switched models; what actually moved quality was the skill."
- **Success signal:** a team builds a reusable skill/checklist instead of arguing about Claude-vs-GPT.

### E3 — Teach the model-comparison discipline
- **Pattern:** the video's "Codex wins" is a single-prompt anecdote; real comparison needs N tasks + a scorecard (B5).
- **Apply:** teach teams to run their own small bake-offs before standardizing on a model.
- **First step:** share the B5 mini-protocol (3 tasks, a scorecard).
- **Success signal:** a team makes a model decision from evidence, not a YouTube demo.

### E4 — A "design-tell hunt" workshop with the 62-point list
- **Pattern:** the checklist is a ready-made shared rubric.
- **Apply:** run a session where the team audits their own product against the list and fixes the top offenders.
- **First step:** pick 15 items, audit one team's page live.
- **Success signal:** the team leaves with a prioritized design-debt backlog.

---

## What to consciously SKIP (and why) — the discipline half

- **Don't switch to Codex/OpenAI for this.** The video's "Codex builds better landing pages" is a single-prompt opinion; multi-prompt evidence + Altman's own launch note favor **Opus 4.7** for front-end. You lose nothing — and likely gain — by staying on Claude Code. ([[ai-web-design-workflow/original-gpt-5-5-codex]])
- **Don't paste the 87KB SKILL.md into `CLAUDE.md`.** That's ~26K tokens on *every* message. Use the on-demand **skill** mechanism (progressive disclosure). ([[claude-api-cost-optimization/_index]])
- **Don't treat the 62-point gate as automated.** It's a manual checklist; make a code-checkable subset real via **A4**, treat the rest as agent self-check + human review.
- **Don't auto-install the skill in hireui.** I-8 = operator-only skill registry; vet it yourself (`npm-security-check` / `install-snapshot`) first. ([[B6]])
- **Don't buy a Seedance/Higgsfield subscription** unless you have a real hero-video need — the image/video sub-loops are nice-to-haves, not the point.
- **Don't trust the product numbers blind.** GPT-5.5 "1M context" is unverified (400K is real), "~40% fewer tokens" is OpenAI self-report, Images-2.0 "QR codes" was a fabrication we dropped. Verify before you cite. ([[ai-web-design-workflow/source-provenance]])

## Critic's reframe (the contrarian read)

The sharpest thing in this video isn't a tool — it's an accidental proof that **"AI design slop" is mechanically diagnosable.** A pseudonymous dev wrote down the ~60 specific ways LLM front-ends look generic, turned each into a binary check, and got 47K stars — because *naming the failure modes* is more valuable than any model upgrade. That's the same move you already make in the vault (Pattern Library = named patterns; the 12-rule CLAUDE.md = named failure modes) and in [[prompt-evaluation/_index]] (graders = named quality dimensions). **The transferable insight: don't ask the model for "good taste" — encode the *absence* of specific bad taste as checks, and gate on them.** That works for UI, prose, code review, and evals alike. The model is interchangeable; the **checklist is the asset** — and it's the one thing the video's creator didn't build but smartly borrowed.

## Cross-links

- [[ai-web-design-workflow/_index]] (source topic) · [[ai-web-design-workflow/taste-skill-deep-dive]] (the centerpiece) · [[ai-web-design-workflow/the-redesign-workflow]] (the recipe) · [[ai-web-design-workflow/source-provenance]] (what's verified).
- Composes with: [[claude-skills/_index]] (SKILL.md format + the Humanizer + Anthropic `frontend-design`) · [[prompt-evaluation/_index]] (eval the redesign / the bake-off harness) · [[claude-api-cost-optimization/_index]] (skill token footprint) · [[codex/_index]] (the Claude-vs-Codex framing) · [[harness-engineering/_index]] (the-skill-is-the-harness) · [[graphify-codebase-graph/_index]] (sibling 2026-06-20 "double deep-dive" topic).

## Suggested next action

Do **A1 right now** — `npx skills add https://github.com/leonxlnx/taste-skill` on a throwaway page in Claude Code (~20 min, zero risk, fully Claude-native), run `/redesign`, and watch the 62-point gate work. Then this week do **B1 + B2** on a hireui `agent-*` branch (you install the skill — I-8): run the TalentAxis frontend through the redesign gate, capture before/after, and bank the 62-point pre-flight as hireui's frontend design-QA gate. When you want the gate enforced rather than asserted, say the word and I'll **scaffold A4** — an em-dash/Inter/3-equal-cards grep linter wired as a Claude Code hook. Tell me which page in hireui to start with and I'll prep the B1 run.
