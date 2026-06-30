# (C) agency-agents — Pilot Methods Menu (24 ways to apply it to your flow)

> **Subject:** `msitarzewski/agency-agents` — 232 personality-driven **subagent** personas across 16 divisions, installed to `~/.claude/agents/` (Claude Code's subagent dir). v185 revisit. See `(C) v185 Revisit — Deep Dive + Delta + Verdict.md`.
> **Why this is a strong pilot target:** dead-center on Goal #1, **immediately + safely pilotable** — pure local markdown file-copies, **no network / no `curl|bash` / no binary / no telemetry** (source-verified). The real risk is *bloat + prompt-surface*, not supply-chain → install **selectively**, `--dry-run` first, read what you install. **This is the lowest-risk-to-apply pilot candidate of the recent run** and a clean path to your first *completed* pilot artifact since v153.
> **Primitive note:** these are **subagents**, not skills — they complement (don't replace) your `05 Skills/`. A subagent runs in its own context window with its own system prompt and returns a summary.

---

## THE STANDING FENCE (read once, applies to all methods)

1. **`install-snapshot` before any install** (snapshot `~`, save the diff as an uninstall checklist).
2. **Never install all 232** into `~/.claude/agents/` — it bloats your subagent list + context. Curate ~5–12 with `--agents-file`.
3. **`--dry-run` first**, always. Then `--path <scratch-dir>` to a throwaway before touching real config.
4. **Read the persona `.md` files you install** — they're plain markdown; check for anything you don't want in your context (prompt-injection surface; SECURITY.md forbids executable code in them, but read anyway).
5. **Skip Hermes** unless you use it (it edits `~/.hermes/config.yaml`, with a `.bak`).
6. **Pin the commit** (`2448583`) — there are no releases.
7. **For hireui:** follow ITS CONSTITUTION — operator-installs the skill registry (I-8), work on an `agent-*` branch (I-2), hireui-rooted, GitNexus-first. Don't install agency-agents globally and then touch hireui; install project-scoped into hireui's `.claude/agents/` on the branch.
8. **Don't stack rule-injectors.** Run agency-agents personas OR ponytail OR Superpowers OR agent-skills at a time while you evaluate — not all at once (you won't know what helped).

```bash
# canonical pilot setup (scratch first)
git clone --depth 1 https://github.com/msitarzewski/agency-agents ~/aa-pilot && cd ~/aa-pilot
./scripts/install.sh --tool claude-code --dry-run                 # see the plan
./scripts/install.sh --tool claude-code --path /tmp/aa-scratch \
  --agents-file my-agents.txt                                     # curated, to a throwaway dir
# my-agents.txt: one slug per line (frontend-developer / code-reviewer / testing-reality-checker …)
```

---

## GROUP A — First loop (lowest risk, ~10–30 min)

**M1 — Smoke test in a scratch repo.** `install-snapshot` → install 3 agents (`engineering-code-reviewer`, `engineering-frontend-developer`, `testing-reality-checker`) into a *scratch* project's `.claude/agents/` via `--agents-file` + project scope. Open Claude Code there and say *"Use the Code Reviewer agent on src/foo.ts."* Confirm the subagent fires and returns a focused review. **Goal:** prove the loop end-to-end, zero risk. *(Lands: Goal #1, the PILOT lever — your first applied pilot.)*

**M2 — Browse-only triage.** Don't install anything. Read the README division tables + ~15 persona files. Build YOUR shortlist: which of the 232 actually map to your work (dev + Scrum + recruitment SaaS). Candidates to read first: `engineering-code-reviewer`, `engineering-backend-architect`, `engineering-frontend-developer`, `engineering-prompt-engineer`, `engineering-minimal-change-engineer`, `engineering-codebase-onboarding-engineer`, `testing-reality-checker`, `project-management-sprint-prioritizer`, `design-ux-researcher`, `security-*`.

**M3 — Diff the format against your `05 Skills/`.** Read 3 persona files next to your own skill files. Note the format delta: agency uses `name`/`description`/`color`/`emoji`/`vibe` + Identity/Mission/Critical-Rules/Workflow/Deliverables/Metrics, as a **subagent**. Decide what's worth borrowing (M13–M16).

---

## GROUP B — Adopt high-value individual agents into your daily Claude Code

**M4 — Reality Checker as your merge gate.** Install `testing-reality-checker` and invoke it before merging vault ships or hireui PRs: *"Reality Checker: assess production-readiness of this change. Default to NEEDS WORK; require evidence."* Its "no fantasy approvals / require visual proof / 2-3 revision cycles" ethic **operationalizes your own `feedback_wiki_verify_independently` rule** as a reusable subagent. **Highest single-agent value for you.** *(Lands: prompt-eval + verify-independently threads.)*

**M5 — Code Reviewer + Security pass on hireui.** Install `engineering-code-reviewer` + a `security-*` agent; run them as a second-opinion review on a hireui PR (composes with your built-in `/code-review`). *(Lands: hireui Goal #2.)*

**M6 — Sprint Prioritizer / Project Shepherd for your Scrum-coach hat.** You ARE a Scrum coach — install `project-management-sprint-prioritizer` + the project-shepherd agent and use them to break down a real backlog into sprints with acceptance criteria. On-vocation, directly useful. *(Lands: Goal #1 + your day job.)*

**M7 — Prompt Engineer for your routine + hireui prompts.** Install `engineering-prompt-engineer`; use it to harden a vault routine prompt or a future hireui LLM prompt. *(Lands: your `prompt-evaluation` pilot thread + the hireui claude-api-cost-optimization spec.)*

**M8 — Codebase Onboarding Engineer (read-only) on hireui or the vault.** `engineering-codebase-onboarding-engineer` does read-only codebase exploration + factual explanation — pair it with hireui's GitNexus-first setup to get a fast factual map. Lowest-risk hireui touch. *(Lands: CC-memory / understanding-internals threads.)*

**M9 — Minimal Change Engineer = ponytail v168 echo.** `engineering-minimal-change-engineer` (minimum-viable diffs) is agency-agents' built-in code-minimalism agent. Run it on a hireui change to keep diffs tight (the same payoff you flagged for ponytail v168). Compare the two approaches.

---

## GROUP C — Multi-agent WORKFLOWS (the `examples/` recipes → your work)

**M10 — Run the `workflow-startup-mvp` pipeline on a real hireui feature.** The 7-agent sequenced recipe (Sprint Prioritizer → UX Researcher ∥ → Backend Architect → Frontend Developer + Rapid Prototyper → **Reality Checker midpoint gate** → Growth Hacker → **Reality Checker GO/NO-GO**). Drive ONE real hireui ticket through it on an `agent-*` branch. **This is the strongest path to your first completed multi-agent pilot artifact since v153 + direct Goal #2 evidence.** *(Lands: multi-agent-orchestration + hireui Goal #2 — the headline.)*

**M11 — Parallel-discovery (the `nexus-spatial-discovery` pattern) for a hireui feature.** Deploy 6–8 agents in parallel (Product Trend Researcher + Backend Architect + Brand Guardian + Growth Hacker + UX Researcher + Project Shepherd) to produce a full blueprint for a new hireui recruitment feature in one session. *(Lands: multi-agent-orchestration; mirrors your `multi-agent-orchestration` pilot thread's job-screener ≈ hireui recruitment-agent.)*

**M12 — Build a recruitment-screening workflow.** Your `multi-agent-orchestration` memory: the video's job-application-screener ≈ a hireui feature. Chain agents (e.g. a sourcing/intake agent → a screening agent → a Reality Checker gate) as a *design* for a hireui candidate-screening flow. hireui has no LLM yet → this is a build-it-right spec, not a retrofit. *(Lands: hireui Goal #2 + the `hireui_no_llm_yet` reality.)*

**M13 — CandidateDetailScreen refactor with an agent team.** Your locked CandidateDetail pilot: run `design-ux-researcher` + `engineering-frontend-developer` + `testing-reality-checker` over the "demo template" drift, then gate with the **Taste-Skill** redesign (your `ai-web-design` thread). agency's Reality Checker + the Taste-Skill compose into a design→code→verify loop. *(Lands: CandidateDetail refactor + ai-web-design threads.)*

**M14 — Key pattern: context-passing.** The examples are explicit that *agents don't share memory — paste the full prior output into the next prompt.* Practice this discipline on a 3-agent chain; it's the manual version of orchestration before you automate (M16).

---

## GROUP D — Borrow the MECHANISMS into your vault (meta / methodology — high leverage)

**M15 — Productize your vault roles AS subagents.** Adopt the agent file format (`name`/`description`/`vibe` + Identity/Mission/Critical-Rules/Workflow/Deliverables/Metrics) to author 2 vault subagents in `~/.claude/agents/`: a **"Wiki Maintainer"** (the routine v2.6 GOAL-ALIGNED INCLUDE evaluator) and a **"Collision Verifier"** (productizes `feedback_wiki_verify_independently_check_collisions` — grep `_state/`, dismiss confabulations). Subagents run isolated → ideal for the verify pass. **High leverage: turns your two most-repeated vault behaviors into reusable workers.**

**M16 — Port `check-agent-originality.sh` into your vault (the anti-inflation killer-app).** Its entity-neutralized 8-word-shingle Jaccard duplicate-detector is *exactly* the tool your routine's anti-re-accumulation discipline needs. Adapt it to flag near-duplicate entries in `05 Skills/` and the `_patterns/06` §C standalone registry — automated detection of the "phantom count" / draw-the-circle problem your routine fights by hand. **Possibly the single most valuable thing to steal from this repo for the vault.**

**M17 — Port the manifest-drift CI (`check-divisions.sh` / `check-tools.sh`).** A single-source-of-truth + consistency-checker for your vault state: CLAUDE.md shim head ↔ `_state/03c` index ↔ `_patterns/06` counts. Your shim already drifts (the "filename label lags at -v183" note, the recurring count reconciles). A `check-vault-state.sh` would catch shim/chapter/registry disagreement automatically. *(Lands: the recurring §F-tally reconcile + the overdue-audit bookkeeping.)*

**M18 — Adopt the Hermes lazy-router idea for context economy.** Don't preload skills/personas; a `search`/`inspect`/`load`/`delegate` router over an on-disk index (the Hermes plugin pattern) is the answer to your 584KB-CLAUDE.md context-pollution + cost pain. *(Lands: CC-memory + cost-optimization threads.)*

---

## GROUP E — hireui Goal-#2 specific (the deployment target)

**M19 — Curated project-scoped install into hireui.** On an `agent-*` branch, install ~6 agents into hireui's `.claude/agents/` (operator-installs per I-8): `engineering-code-reviewer`, `engineering-frontend-developer`, `engineering-backend-architect`, a `security-*`, `testing-reality-checker`, `engineering-codebase-onboarding-engineer`. `--dry-run` + read each first.

**M20 — One real ticket, end-to-end (the completed-artifact play).** Take a single real hireui ticket through M10's pipeline on the branch → ship → record it in `.pilot-log`. **This is the concrete "applied a vault subject to real software" evidence Goal #2 has been missing since v153.**

**M21 — Reality Checker as the hireui deploy gate.** Make `testing-reality-checker` the GO/NO-GO step before a hireui deploy (composes with your observability + prompt-eval threads). Require evidence per its mandate.

---

## GROUP F — Evaluate vs your existing stack / decide

**M22 — Primitive bake-off: subagents vs skills.** Head-to-head on one task: an agency-agents *subagent* (e.g. code-reviewer) vs an agent-skills v184 *skill* vs your own `05 Skills/` vs Superpowers. Which primitive (isolated-context subagent vs injected-knowledge skill) wins for which job? You now hold agent-skills v184 + agency-agents v185 — a real comparison deliverable for Goal #1. *(Lands: Goal #1 understanding.)*

**M23 — The "earned their keep" retro.** After a 2-week pilot, run a Scrum-style retro on the installed agents: which earned their keep, which were noise? Cull to a permanent ~5. (You're a Scrum coach — dogfood the ceremony on your own toolset.)

**M24 — Try the Desktop App + consider contributing back.** (a) Try `agency-agents-app` (Rust+Tauri 2 GUI) to manage installs + the install-ledger + file-modification-detection across tools — evaluate vs the shell installer. (b) Author a **"Scrum Coach"** or **"LLM-Wiki Maintainer"** agent (a genuine gap in their 232-roster), run `./scripts/check-agent-originality.sh` locally, and PR it — your expertise fills a real hole + closes the loop on Goal #1.

---

## Recommended sequence

**M1 (smoke test) → M4 (Reality Checker into daily use) → M10 (one hireui feature through the MVP pipeline = your first completed multi-agent pilot artifact) → M16 (port the originality detector into the vault).**

That ladder gives you, in order: proof the loop works (zero risk), one immediately-useful daily agent, a completed Goal-#2 artifact, and a high-leverage vault-meta tool. Everything else is optional depth.
