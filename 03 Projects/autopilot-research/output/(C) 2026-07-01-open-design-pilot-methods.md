# (C) Pilot methods — applying Open Design (and its originals) to your flow

> **Source:** wiki topic [[open-design/_index]] — CodingMenace demo (`QOqWZzecjuY`) + adversarially-verified deep-dives of Open Design and its "open source shoulders" (`wf_4a91a8b2-2bb`, 13 agents; + operator `gh api`/WebFetch ground-checks).
> **Operator context:** software dev + Scrum coach; deployment target **hireui** (TalentAxis recruitment SaaS, React/TS web+mobile; **no LLM in product yet**; CONSTITUTION with **I-2 agent-\* branch** + **I-8 operator-only installs** + **GitNexus-first**; **Candidate Detail** mobile refactor in flight with **drifted design tokens** navy `#1E2960`→`#002D79`, accent `#E8743C`→`#DC6803`, Inter→Roboto). Already running the **leonxlnx Taste Skill** anti-slop gate ([[../ai-web-design-workflow/_index]]). Two L5 vaults (Storm Bear + autopilot-research).
> **Goal #2 = *actually deploy* these methods into a real working flow.** Ranked by that leverage.

---

## The headline (if you do ONE thing this week)

**Codify hireui's drifted Candidate-Detail tokens as a portable `DESIGN.md` single source of truth — *steal the pattern, don't install anything* — then pilot Open Design on that one screen driven by your own Claude Code CLI, gated by your Taste Skill + huashu's anti-slop checklist.** This is the cheapest, most reversible, highest-Goal-#2 move: the `DESIGN.md` SoT **fixes the token-drift root cause** whether or not you ever adopt the tool, and the Open-Design pilot is **real "I deployed an agent-native design harness on a production screen" evidence** that composes with your **cc-sdd #1** and **ai-web-design-workflow (Taste Skill)** pilots. Everything else is optional depth on top of that.

---

## Ranking at a glance

| # | Method | Angle | Effort | Goal #2 |
|---|---|---|---|---|
| **A1** | Codify hireui tokens as a portable `DESIGN.md` SoT (steal, no install) | hireui | S–M | ★★★ |
| **A2** | Pilot Open Design on Candidate Detail via your own Claude Code CLI (staging) | hireui | M | ★★★ |
| **A3** | Two-gate anti-slop review: Taste Skill + huashu checklist before merge | hireui | S | ★★★ |
| **A4** | Comparison pilot: Open Design vs your Figma-handoff+Taste flow, measured | hireui | M | ★★★ |
| **A13** | "Design-System-as-Code" ADR anchoring Goal #2 | hireui | S | ★★★ |
| **B2** | Brand Asset Protocol → `brand-spec.md` (logo>product>UI>color) | hireui | S–M | ★★★ |
| **A5** | Figma → `DESIGN.md` one-way sync (DESIGN.md canonical, Figma a render target) | hireui | L | ★★ |
| **A6** | Multi-agent design eval: same `DESIGN.md`, Claude Code vs Cursor vs Codex | hireui | M | ★★ |
| **A8** | huashu Junior-Designer workflow (assumptions-first) before agent writes CSS | hireui | S | ★★ |
| **B1** | Install `huashu-design` standalone as a 2nd anti-slop gate | hireui/personal | S | ★★ |
| **B3** | Design Direction Advisor: 3 real prototypes, not 3 text debates | hireui/Scrum | M | ★★ |
| **A11** | "Design-token auditor" local MCP (reads `tokens.ts` ↔ Figma, flags drift) | hireui | L | ★★ |
| **A7** | HyperFrames token-walkthrough MP4 for the design handoff | hireui | M | ★ |
| **A9** | Steal the sandboxed-preview + live-tweaks UX → token playground | hireui | L | ★ |
| **A10** | `.claude/ONBOARDING.md`: how agents use `DESIGN.md`/`SKILL.md` in hireui | hireui | S | ★★ |
| **A12** | BYOA env-var swap pilot (`AGENT_CLI`) under I-2, `DESIGN.md` stable | hireui | M | ★ |
| **B4** | huashu 5-dimensional review as a design-quality scorecard | hireui/Scrum | S | ★ |
| **B5** | Adopt huashu's fact-verification-first (#0) for design decisions | hireui | S | ★ |
| **C1** | guizang/html-ppt standalone → auto-generate Scrum/sprint-review decks | Scrum | S–M | ★ |
| **C2** | Recruitment job-posting decks + social covers from hireui tokens | Scrum/hireui | M | ★ |
| **D1** | Steal "design systems are portable markdown" for the vault's own docs | vault | S | ★ |
| **D2** | Apply "skills are files + `od:` frontmatter" to the project-local skill registry | vault | S | ★ |
| **E1** | BYOA lens: your CLI is a swappable engine; the harness is the leverage | personal | S | ★★ |
| **E2** | Open Design as a personal prototyping surface for side-projects | personal | M | ★ |

**M0 (prerequisite for anything that installs/runs it):** `/npm-security-check` + `install-snapshot`, unset `POSTHOG_KEY`, keep `OD_BIND_HOST` loopback, sandbox against a staging mirror — see [[open-design/caveats-and-safety]] and [[open-design/install-and-setup]]. Inside hireui, **you** install (I-8); the agent proposes.

---

## Angle A — hireui Goal #2 (the deployment target)

### A1 — Codify hireui tokens as a portable `DESIGN.md` SoT ★★★ · S–M · *steal, no install*
**What:** Write one markdown file — `apps/mobile/.../DESIGN.md` (or `design-systems/hireui-talentaxis/DESIGN.md`) — as the canonical brand contract using Open Design's own 9 sections (color / typography / spacing / layout / components / motion / voice / brand / anti-patterns). Put the **reconciled Figma r2 values** in it (navy `#002D79`, accent `#DC6803`, Roboto scale, verified timeline colors `#ECFDF5`/`#FEF2F2`, avatar 72px). Reference it from every agent prompt + the CONSTITUTION.
**Why:** The token drift exists because there's no single authority — it's split across Figma, `tokens.ts`, and tacit knowledge. A `DESIGN.md` makes the contract **canonical, version-controlled, diff-able, and agent-readable**, so no agent can invent a fourth navy. This is the root-cause fix and needs **zero install**. → [[open-design/design-md-as-source-of-truth]]
**Output:** `DESIGN.md` in the repo + a one-line CONSTITUTION reference making it the SoT.

### A2 — Pilot Open Design on Candidate Detail via your own Claude Code CLI ★★★ · M
**What:** Do M0 first. On a **staging mirror** of hireui (or a throwaway `agent-*` worktree per I-2), run Open Design, let it PATH-detect your Claude Code CLI, feed it the A1 `DESIGN.md` + a Candidate-Detail brief (import a Figma/Claude-Design export if you have one), and generate a hi-fi mobile prototype. Compare to the current `CandidateDetailScreen.tsx`.
**Why:** This is the actual **Goal #2 deployment**: an agent-native design harness driven by *your* model, producing a real artifact on a production screen. It also stress-tests whether BYOA + `DESIGN.md` beats manual Figma-to-code.
**Output:** a generated prototype + a short `04 Reviews/`-style write-up (setup time, token-fidelity, drift caught). **Caution:** never point it at production data first; pre-1.0 tool (see caveats).

### A3 — Two-gate anti-slop review before merge ★★★ · S
**What:** Before shipping any Candidate-Detail change, run **both** gates: your **Taste Skill** 62-point critique *and* **huashu-design's anti-AI-slop checklist** (no purple gradients, no emoji-icons, no rounded-card+left-border cliché, no CSS silhouettes for real imagery, no generic dark palette; ✅ `text-wrap: pretty`, `oklch()`, real images, proper type rhythm). Record pass/fail per gate.
**Why:** Two independent anti-slop authorities catch more than one. huashu's list is *specific and grounded* (each ban is "this is a training-corpus average"), complementing Taste's scoring. → [[open-design/huashu-design-deep-dive]]
**Output:** a design-quality checklist gate wired into the Candidate-Detail DoD.

### A4 — Comparison pilot: Open Design vs your existing flow ★★★ · M
**What:** Run the *same* Candidate-Detail redesign brief through (a) your current 3-step **Figma → markdown → Claude Code + Taste** flow and (b) a 2-step **`DESIGN.md` → Open Design** flow. Measure across ~5 iterations: speed, token-drift incidents, token spend, and *your confidence*.
**Why:** Turns "should I adopt this?" into evidence, and produces a hireui ADR either way. Directly feeds Goal #2 ("build software with these tools" — with a measured before/after).
**Output:** `hireui/.cm/outputs/(C) figma-flow-vs-open-design-benchmark.md`.

### A13 — "Design-System-as-Code" ADR ★★★ · S
**What:** Write an Architecture Decision Record: *why hireui should treat its design system as portable `DESIGN.md`/`SKILL.md`* — version-controlled, agent-agnostic, unlocking multi-agent generation (Claude Code today, Cursor tomorrow). Anchor it to Goal #2 and the token-drift pain.
**Why:** Cheapest way to convert this research into a durable hireui decision; the north-star that A1/A5/A6 execute against.
**Output:** `hireui/.cm/outputs/(C) design-system-as-code-adr.md`.

### A5 — Figma → `DESIGN.md` one-way sync ★★ · L
**What:** A small tool/script (hireui-specific, GitNexus-aware) that reads the Figma r2 export (colors/spacing/type) and generates/updates `DESIGN.md`, warning if live `tokens.ts` diverges. Figma becomes a *render target* of the canonical `DESIGN.md`, not a competing authority.
**Why:** Automates A1's maintenance and permanently closes the drift loop. Higher effort; do after A1 proves the pattern.
**Output:** `hireui/.cm/figma-design-md-sync.ts` + drift warnings in CI.

### A6 — Multi-agent design eval ★★ · M
**What:** Same `DESIGN.md`, same Candidate-Detail brief, three engines via BYOA (Claude Code vs Cursor vs Codex). Measure which best honors the design-system constraints.
**Why:** Exploits Open Design's core BYOA capability to answer a real question — *does agent choice matter for design fidelity?* — cheaply. Data for Goal #2 + your harness-engineering interest.
**Output:** a small eval table; feeds your prompt-evaluation discipline ([[../prompt-evaluation/_index]]).

### A8 — huashu Junior-Designer workflow (assumptions-first) ★★ · S
**What:** Before the agent writes any CSS for a Candidate-Detail slice, require it to emit **assumptions + reasoning + placeholders** at the top and show them for approval (huashu core-philosophy #2). Only then build.
**Why:** "Understanding it wrong early is 100× cheaper to fix than late." Surfaces the 3-tabs/72px-avatar/timeline-color decisions before code — the exact failure mode of that screen. Mirrors grill-me/interview-first ([[../pocock-agentic-workflow/_index]], [[../how-we-claude-code/_index]]).
**Output:** an "assumptions-first" step in the Candidate-Detail agent runbook.

### A11 — "Design-token auditor" local MCP ★★ · L
**What:** Author a small MCP tool (wired into hireui's I-8 registry) that reads `tokens.ts`, cross-checks against the Figma r2 JSON / `DESIGN.md`, and flags drift (navy/accent/font/orphaned-spacing) with a remediation script.
**Why:** Turns drift detection into automation on every handoff. Borrows Open Design's "design files as a queryable API" idea without adopting the whole app.
**Output:** `hireui/.claude/mcp/(C) design-tokens-auditor.mcp.ts`.

### A7 — HyperFrames token-walkthrough MP4 ★ · M
**What:** Generate a ~60s motion walkthrough of the token before/after (color grid, spacing audit, type scale) via Open Design's HyperFrames; drop it in the design-handoff folder as onboarding.
**Why:** A handoff artifact Figma/Claude Design can't produce locally; useful for team alignment. Low Goal-#2 weight. **Caveat:** HyperFrames integration is README-described, not code-verified — treat as a spike.
**Output:** `design_handoff_mobile/(C) candidate-detail-tokens-review.mp4`.

### A9 — Token playground (steal the sandboxed-preview+tweaks UX) ★ · L
**What:** Replicate Open Design's live-tweaks side panel as a tiny internal tool: adjust navy/accent/spacing/font live and see Candidate Detail re-render, lock the winning combo back to `DESIGN.md`.
**Why:** Cuts design-decision time per iteration; a QoL win. High effort; do only if A1–A4 show the team iterating on tokens a lot.
**Output:** `apps/mobile/(C) design-token-live-editor.tsx`.

### A10 — `.claude/ONBOARDING.md` for hireui agents ★★ · S
**What:** One page: how to read `DESIGN.md` as the SoT, how to invoke the Candidate-Detail `SKILL.md`, how the Taste/huashu gates plug in, and (if adopted) how to `od mcp install claude-code` in hireui's context.
**Why:** Compounds knowledge — the next agent/teammate starts from this, not zero. Low effort, real leverage.
**Output:** `hireui/.claude/ONBOARDING.md` (shareable via the onboarding-guide flow).

### A12 — BYOA env-var swap pilot under I-2 ★ · M
**What:** Add an `AGENT_CLI` switch to the agent-\* harness so the same `DESIGN.md`/`SKILL.md` can be driven by Claude Code → Cursor → OpenCode without change; run a Phase-0 proof + Phase-1 verify.
**Why:** Dogfoods BYOA/harness-over-model in hireui's own harness. Low Goal-#2 weight; high architectural value.
**Output:** `hireui/.claude/settings.json` `AGENT_CLI` config + pilot-log entry.

---

## Angle B — Steal the methodology, not the tool

### B2 — Brand Asset Protocol → `brand-spec.md` ★★★ · S–M
**What:** Run huashu-design's **5-step Brand Asset Protocol** for TalentAxis: Ask → search official channels → download assets → verify+extract → **codify `brand-spec.md`** (logo > product images > UI > color > font). Feed the verified HEX values into A1's `DESIGN.md`.
**Why:** It's the *methodology* behind `DESIGN.md` and it grounds the token values in **real brand authority** (not guesses/memory) — the thing hireui lacks. Reverses the usual "start from colors" trap. → [[open-design/huashu-design-deep-dive]]
**Output:** `brand-spec.md` feeding `DESIGN.md`.

### B1 — Install `huashu-design` standalone as a 2nd anti-slop gate ★★ · S
**What:** `npx skills add alchaincyf/huashu-design` (MIT; no Open Design needed) and add it alongside your Taste Skill.
**Why:** A second, independent anti-slop authority (from a different author) — see A3. Standalone install, small surface.
**Output:** huashu-design skill registered (per I-8, you install).

### B3 — Design Direction Advisor: 3 real prototypes, not 3 text debates ★★ · M
**What:** When the team can't agree on a Candidate-Detail direction, generate **3 true visual prototypes** via huashu's 3-logic approach: (1) forced-random style, (2) real-world reference (LinkedIn/Indeed recruitment UX), (3) best-designer philosophy (Stripe-grade). Pick from the *real thing*.
**Why:** Eliminates abstract debate; a great Scrum-facilitation move too. Uses the same data/copy each time.
**Output:** 3 prototype variants + a decision note.

### B4 — huashu 5-dimensional review scorecard ★ · S
**What:** Score Candidate-Detail on philosophy consistency / visual hierarchy / execution detail / functionality / innovation (0–10), mapped to recruitment (brand trust / scannable info / token precision / tap accuracy / differentiation), with a Keep/Fix/Quick-Wins summary.
**Why:** Communicates design quality to stakeholders as metrics, not vibes. Pairs with A3.
**Output:** a reusable design-review scorecard.

### B5 — Adopt fact-verification-first (#0) for design decisions ★ · S
**What:** Before accepting any "the brand color is X" claim, verify against a real source (brand site / Figma SoT / marketing), per huashu's highest-priority principle.
**Why:** Same anti-fabrication discipline this vault enforces, applied to design. Cheap habit; prevents drift-from-memory.
**Output:** a one-line rule in the design DoR.

---

## Angle C — Decks for Scrum coaching

### C1 — guizang/html-ppt standalone → Scrum/sprint-review decks ★ · S–M
**What:** Use `lewislulu/html-ppt-skill` (MIT — 36 themes/31 layouts/presenter mode) or `op7418/guizang-ppt-skill` to auto-generate sprint-review / retro / phase-plan decks from markdown, driven by your Claude Code CLI. HTML-first, zero-build, export PPTX/PDF.
**Why:** Directly useful for your Scrum-coach work; no Open Design needed. **⚠️ License:** guizang-ppt is **AGPL-3.0** upstream — fine for internal use, mind copyleft if you redistribute; html-ppt is MIT (safer to reuse). → [[open-design/the-originals]]
**Output:** a repeatable "markdown → deck" skill for coaching briefings.

### C2 — Recruitment job-posting decks + social covers ★ · M
**What:** Generate on-brand job-posting one-pagers / social covers from hireui's `DESIGN.md` + job data (deck + image skills).
**Why:** Reduces design-to-marketing handoff friction; `DESIGN.md` keeps it on-brand without a designer. Product-adjacent, lower Goal-#2 weight.
**Output:** a job-posting deck template.

---

## Angle D — Vault (autopilot-research + Storm Bear)

### D1 — Steal "design systems are portable markdown" for the vault ★ · S
**What:** Note the pattern lesson: a design system (or any spec) as one portable markdown file beats a tool-locked artifact. Apply to how the vault documents its own conventions/skills.
**Why:** Reinforces the Karpathy LLM-Wiki ethos this whole vault runs on (files > databases). Meta-value.
**Output:** a short note in the topic; candidate lesson for the Pattern Library.

### D2 — "Skills are files + `od:` frontmatter" for the project-local skill registry ★ · S
**What:** Consider adding lightweight frontmatter (mode/scenario/default_for) to the autopilot-research project-local skills so vault-level triggers can discover/route them more precisely — mirroring Open Design's `SKILL.md` `od:` extension.
**Why:** Small ergonomics win for `/loop`/`/schedule` discovery.
**Output:** frontmatter proposal for `skills/`.

---

## Angle E — Personal Claude Code harness

### E1 — BYOA lens: your CLI is a swappable engine ★★ · S
**What:** Internalize the thesis: the model is a *slot*; your leverage is the harness (skills + `DESIGN.md` + prompts). Audit where you're chasing models vs improving the harness.
**Why:** Same harness-over-model insight as [[../pocock-agentic-workflow/_index]] / [[../harness-engineering/_index]], now demonstrated by a design tool. Cheap mindset shift with compounding payoff.
**Output:** a personal note; informs A12.

### E2 — Open Design as a personal prototyping surface ★ · M
**What:** For your own low-stakes side-projects, use Open Design as a general prompt→prototype→export tool (native desktop app, your Claude Code CLI).
**Why:** Learn the tool's ergonomics on non-critical work before any hireui pilot. Do M0 hygiene first.
**Output:** familiarity + a feel for whether it earns a hireui pilot.

---

## Skip-list (what NOT to do)

- **Don't point Open Design at hireui production data / expose the daemon beyond localhost on day one.** Pre-1.0, "SSRF protection" unconfirmed in code, spawns your CLI. Sandbox + loopback only (M0). → [[open-design/caveats-and-safety]]
- **Don't trust the README's "MIT" for the bundled guizang-ppt** — the upstream is **AGPL-3.0**. Verify the actual `LICENSE` before redistributing any deck output; prefer html-ppt (MIT) if in doubt.
- **Don't fork multica** — it's **NOASSERTION** (no reuse grant). Learn the pattern, don't lift the code.
- **Don't repeat the video's/marketing numbers** ("27K stars", "31 skills", "261 plugins") — cite live `gh api` figures with a date; they're stale/inflated.
- **Don't replace your Taste Skill flow wholesale** before A4 proves Open Design wins — run them side-by-side first.
- **Don't adopt Open Design as a hard dependency** — it's ~2 months old, pre-1.0, 11 minor versions in 2 months (format churn risk). Steal patterns (A1/B2) that survive even if you drop the tool.

## Critic's reframe (the honest "do this")

Most methods here are *design-hygiene* or *exploration* — Goal #2 needs a **shipped artifact**. Collapse to a two-week, evidence-producing sprint:

1. **Week 1 (no install):** **B2** (Brand Asset Protocol → `brand-spec.md`) → **A1** (codify `DESIGN.md` SoT) → **A13** (Design-System-as-Code ADR). This alone fixes the token-drift root cause and is durable.
2. **Week 2 (sandbox pilot):** M0 hygiene → **A2** (Open Design on Candidate Detail via your Claude Code CLI, staging mirror) → **A3** (Taste + huashu two-gate review) → **A4** (measure vs your current flow).
3. **Carry-forward:** **A10** (`ONBOARDING.md`) + **A5** (Figma→`DESIGN.md` sync) become permanent; **A6/A12** (multi-agent/BYOA) when you want harness data; decks (**C1**) whenever you next run a sprint review.

That's the smallest path to a real **"I codified our design system as portable `DESIGN.md`, piloted an agent-native design harness on a production screen with my own Claude Code CLI, and here's the measured before/after"** write-up — file it in `04 Reviews/` as Goal-#2 evidence, composing with the **cc-sdd #1** and **ai-web-design-workflow (Taste Skill)** pilots.

> **Suggested next action:** start **B2 → A1** this week (zero install, fixes the drift), open the **A13 ADR** to capture the decision, and book a Week-2 checkpoint to run the **A2 sandbox pilot** with M0 hygiene done first.
