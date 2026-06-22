# (C) serve-sim — Pilot Methods Menu (apply to your workflow)

> **AI-generated** (`(C)`). Companion to **[(C) serve-sim — Beginner Analysis](<(C) serve-sim — Beginner Analysis.md>)** (v183). 2026-06-22.
> **Purpose:** "show me many methods for my apply." 24 concrete ways to apply serve-sim to *your* workflow, grouped, tagged by **effort / risk / value**, with a recommended sequence and a security fence.
> **Your context that makes this unusually relevant:** **hireui** = a TalentAxis recruitment SaaS with an **Expo / React-Native mobile app** (the `CandidateDetailScreen` "demo template" visual-drift spike). serve-sim is built by the **Expo author**, auto-integrates with `npx expo start`, and lets an AI agent **see and drive** that running iOS app. This is a direct **Goal #2** lever, and it plugs straight into your **ai-web-design / Taste-Skill**, **candidate-detail-refactor**, **CC-observability**, and **multi-agent-orchestration** threads.

---

## 0. The one-paragraph "why this is a pilot, not just a wiki"

Every prior on-goal pilot candidate (SkillSpector, claude-tap, Agent-Reach, codebase-memory-mcp, devspace, …) was about *tooling around the agent*. serve-sim is different: it **changes what your agent can DO** — it gives Claude Code **eyes and hands on a running iOS app**. For the first time your agent can close the loop on a *visual* change: edit RN code → see the rendered screen → tap through it → notice the navy is wrong / the avatar is the wrong size → fix → look again. That is exactly the loop your `CandidateDetailScreen` refactor needs. **The PILOT lever still stands at zero piloted; serve-sim is a strong new candidate on it.**

**Legend:** 🟢 low / 🟡 medium / 🔴 high. **E** = effort, **R** = risk (security/footprint), **V** = value-to-your-goals.

---

## Group A — First loop (prove it works, lowest risk)

**A1. Localhost hello-loop on a throwaway Expo app.** `E 🟢 · R 🟢 · V 🟢` — In a **scratch** Expo project (NOT hireui), run `npx serve-sim`, open `localhost:3200`, confirm the stream + a manual `serve-sim type` / `gesture`. Goal: confirm the loop runs on your machine before touching real code. *(Prereq: `install-snapshot` first — see fence.)*

**A2. Install the Agent Skill into a scratch Claude Code, read it.** `E 🟢 · R 🟢 · V 🟡` — `/plugin marketplace add EvanBacon/serve-sim` in a *throwaway* Claude Code session; then **read `skills/serve-sim/SKILL.md`** to see exactly what it teaches the agent. This is also a great study artifact for *your own* skill-authoring (cf. SkillOpt v178, agent-skills-standard v76).

**A3. Have the agent describe the screen.** `E 🟢 · R 🟢 · V 🟡` — Point Claude Code (with a browser-vision tool, or via the `/.sim/ax` accessibility endpoint) at the stream and ask "describe what's on screen + list the tappable elements." Confirms perception works end-to-end before you ask it to *act*.

**A4. Read-only verification first.** `E 🟢 · R 🟢 · V 🟡` — Use serve-sim purely as an **observer**: agent takes a screenshot of a screen you built, you ask "does this match the spec?" No taps, no shell. Mirrors your "SkillSpector lowest-risk-first" pilot discipline.

---

## Group B — hireui mobile visual verification (the Goal #2 headline)

> All hireui work obeys its **CONSTITUTION**: run rooted in `/Users/Cvtot/monorepo/hireui`, **agent-`*` branch (I-2)**, **operator-only skill install (I-8)** — *you* install the serve-sim skill, the agent doesn't, **GitNexus-first**. (See memory `project_hireui_pilot_target`.)

**B1. ⭐ Visual diff the `CandidateDetailScreen` redesign.** `E 🟡 · R 🟡 · V 🔴` — Run hireui's iOS app under serve-sim; have Claude Code **screenshot the live screen and compare against the Figma handoff** (`apps/claude-design-handoff/.../design_handoff_mobile/`). This directly attacks the "demo template" drift you locked: navy `#1E2960→#002D79`, accent `#E8743C→#DC6803`, Inter→Roboto, avatar 72px, the 3-tab layout, timeline colors `#ECFDF5/#FEF2F2`. The agent *sees* the deviation instead of guessing.

**B2. Close the edit→see→fix loop on one screen.** `E 🟡 · R 🟡 · V 🔴` — Drive `/autopilot-phase` against the locked plan (`.cm/outputs/plans/phase-2-candidate-screen-rework.md`) but with serve-sim in the loop so each token/layout fix is **verified against the rendered screen** before the agent moves on. Turns the spike from "apply tokens blind" into "apply + confirm."

**B3. Tap through all 3 tabs.** `E 🟡 · R 🟡 · V 🔴` — Agent uses `serve-sim gesture`/`button` to navigate the 3-tab Candidate Detail (the locked Figma-deviation), screenshotting each, checking parity = data/behavior/copy (web) + layout (Figma r2). Catches per-tab regressions a static read misses.

**B4. Verify the timeline state colors live.** `E 🟢 · R 🟡 · V 🟡` — The verified timeline colors (`#ECFDF5` success / `#FEF2F2` error) are exactly the kind of thing that looks right in code and wrong on screen (opacity, dark mode, safe-area). Have the agent render the timeline in each state and confirm the pixels.

**B5. Empty / loading / error states.** `E 🟡 · R 🟡 · V 🟡` — Drive the app into edge states (no data, slow network via simulated conditions, error) and screenshot. RN edge states are notoriously under-tested; the agent can now *see* them.

**B6. Device-matrix screenshots.** `E 🟡 · R 🟡 · V 🟡` — `npx serve-sim "iPhone 17 Pro Max" "iPhone SE" "iPad Pro"` (multi-device) → agent screenshots the same screen on each → flags safe-area/Dynamic-Type/layout breaks. Cheap responsive-QA for free.

**B7. Camera-feature testing without a camera.** `E 🟡 · R 🟡 · V 🟡` — If hireui ever adds resume-photo / ID-capture / video-intro, `serve-sim camera <bundle-id> --file <fixture>` injects a deterministic synthetic feed so the agent can test camera flows in the simulator. Unique to serve-sim among the peers.

---

## Group C — Close the design → code → verify loop (ties your threads together)

**C1. ⭐ Taste-Skill redesign gate + serve-sim verify gate.** `E 🟡 · R 🟡 · V 🔴` — Your `ai-web-design` thread's headline B1 was "run hireui through the Taste Skill `redesign` gate." Pair it: **Taste Skill proposes the redesign → agent implements → serve-sim verifies the rendered result against the 62-point anti-slop gate**. Design-in and verify-out, both agent-run.

**C2. Spec → screenshot acceptance test.** `E 🟡 · R 🟡 · V 🟡` — Encode acceptance criteria ("avatar 72px, navy header, 3 tabs visible") and have the agent confirm each against a live screenshot — a lightweight, human-readable visual acceptance suite driven from your locked operator decisions.

**C3. Before/after evidence cards for PRs.** `E 🟢 · R 🟡 · V 🟡` — On each agent-`*` branch, capture before/after screenshots of the changed screen and attach to the PR. Turns "trust me it looks right" into reviewable evidence (matches your prompt-eval "evidence-first" discipline).

**C4. Feed serve-sim screenshots into a prompt-eval grader.** `E 🟡 · R 🟡 · V 🟡` — Your `prompt-evaluation` thread + `evals/` harness: add a visual-grading method where a screenshot is the artifact graded (anchor-validated, per your shipped A1 gate). Closes the eval loop on UI, not just text.

---

## Group D — Test generation & regression

**D1. Agent-authored UI smoke tests.** `E 🟡 · R 🟡 · V 🟡` — Have the agent explore the app via serve-sim and *write* a repeatable gesture/assert script (the `serve-sim-client` Gateway protocol) as a smoke test. Self-generated regression coverage.

**D2. Visual regression baseline.** `E 🟡 · R 🟡 · V 🟡` — Snapshot key screens as baselines; on later changes the agent diffs new screenshots vs. baselines and flags pixel drift (the cheap version of Panto-style RN visual regression).

**D3. Repro-from-bug-report.** `E 🟡 · R 🟡 · V 🟡` — Paste a bug report; agent drives serve-sim to reproduce the steps, screenshots the broken state, then fixes + re-verifies. The full perceive→act→verify loop on a real defect.

---

## Group E — Multi-agent / orchestration (your `multi-agent-orchestration` thread)

**E1. Verifier sub-agent.** `E 🟡 · R 🟡 · V 🟡` — In a multi-agent setup, dedicate one sub-agent as the **"eyes"**: it owns the serve-sim connection and answers "does the screen match X?" while the builder agent edits code. Clean separation (your B6/B7 orchestration methods).

**E2. Parallel device fan-out.** `E 🔴 · R 🟡 · V 🟡` — Multiple simulators (multi-device) each driven/observed by a worker agent for parallel screen verification. Mirrors your vault's own `parallel()` fan-out experiments.

**E3. Remote-Mac shared simulator.** `E 🔴 · R 🔴 · V 🟡` — serve-sim's "host on a remote mac and tunnel anywhere" lets a team (or several agents) share one hosted simulator. **High risk** (remote shell surface) — fence hard; LAN-only before any tunnel.

---

## Group F — Infra / advanced

**F1. Mount as Metro middleware in hireui dev.** `E 🟡 · R 🟡 · V 🟡` — `simMiddleware({ basePath: "/.sim" })` inside hireui's Expo dev server → the stream + control live on the same origin as the app; nothing extra to start.

**F2. CI screenshot artifacts (macOS runner only).** `E 🔴 · R 🟡 · V 🟡` — On a macOS/arm64 CI runner, boot a sim + serve-sim headless (`--no-preview --detach`) and emit screenshots as build artifacts. ⚠️ macOS-arm64-only — won't run on your Linux CI.

**F3. Accessibility-tree-first driving.** `E 🟡 · R 🟢 · V 🟡` — Prefer `/.sim/ax` (structured elements) over raw pixels where possible — more reliable element targeting, less vision cost (the ios-simulator-mcp strength, available here too).

---

## Group G — Vault-meta (dogfood / learning)

**G1. Study the Agent Skill as a skill-authoring exemplar.** `E 🟢 · R 🟢 · V 🟡` — A well-made, single-purpose Agent Skill from the Expo author = a model for your own `05 Skills/`. Pair with SkillOpt v178 (optimize a skill against a held-out set) and agent-skills-standard v76.

**G2. Compare against the peer crop as a landscape note.** `E 🟢 · R 🟢 · V 🟡` — A short note in the wiki comparing serve-sim vs agent-device / agent-simulator / ios-simulator-mcp / mobile-mcp — useful if you ever need Android too (serve-sim is iOS-only; mobile-mcp / agent-device cover both).

**G3. Watch for the corpus N=2.** `E 🟢 · R 🟢 · V 🟢` — The §C standalone is N=1; agent-device/agent-simulator are external peers. If you ever wiki one, this standalone promotes toward CONFIRMED. (Bookkeeping, not a workflow change.)

---

## Recommended sequence (your "lowest-risk-first" discipline, extended)

1. **A1 → A2 → A3/A4** — prove the loop on a *scratch* Expo app, read the skill, confirm perception. (One sitting, low risk.)
2. **B1** — point it at hireui's `CandidateDetailScreen` for a **read-only visual diff** vs the Figma handoff. (The single highest-value first real use.)
3. **B2/B3** — let the agent *act* (tap through tabs) and run the edit→see→fix loop on that one screen, on an **agent-`*` branch**.
4. **C1** — fold in the Taste-Skill redesign gate so design-in and verify-out are both agent-run.
5. Expand to **D1/D2** (regression baselines) and **E1** (verifier sub-agent) once the loop is trusted.

> serve-sim slots onto your existing pilot ladder **alongside Agent-Reach v174 / camofox v179** as a *capability* pilot (it adds an ability), but with a sharper Goal-#2 payoff than any of them because hireui is *literally an Expo app*. Lowest-risk first pilot overall remains **SkillSpector v169** (read-only over `05 Skills/`); serve-sim's read-only mode (A4/B1) is comparably safe and far more relevant to shipping hireui.

---

## Security fence (do this before any real use)

- **`install-snapshot` first**, then `npx serve-sim` — capture what it writes (the skill makes this its own checklist).
- **`npm-security-check`** `serve-sim` + `serve-sim-client` before install (new-ish package, single author, ships a compiled binary + a dylib).
- **LOCALHOST-ONLY** until you trust it. The control channel runs **arbitrary shell** (token-gated) and the design invites LAN/tunnel exposure → a leaked token + open tunnel = remote shell on your Mac. **No public tunnel** in a pilot.
- **Scratch project before hireui.** When you do use hireui: **operator installs the skill (I-8)**, work on an **agent-`*` branch (I-2)**, run rooted in the hireui repo (GitNexus + Figma MCP).
- **Pin the version** (`serve-sim@0.1.34`) — "no releases published," expect churn.
- **Camera injection uses `DYLD_INSERT_LIBRARIES`** (library injection into sim processes) — fine locally, but know it's there.
- Apple-Silicon macOS only; nothing here runs on your Linux CI.
