# (C) dsh-anchored-standard — Pilot Methods Menu

**Wiki v238 · 2026-08-18**

**Honest framing up front:** there is **nothing here to install**. This is a dead (maintenance-only from 2026-08-17) v0.1.0 agent preset for **DeepSeek Harness**, pinned to `0.1.0-rc.5`, targeting **DeepSeek V4 Pro**, whose headline benefit **two independent replications failed to confirm**. Claude appears in it only as a `CLAUDE.md` digest that the preset *deletes*.

So this menu is mostly **read**, **borrow**, and **one genuinely worthwhile experiment on your own setup** using a first-party Claude feature. It is short on hands-on rungs because the subject honestly doesn't have them — padding it would be dishonest.

⭐ = recommended · ⚠️ = fenced or discouraged · 🔴 = don't

---

## A — Read & learn (zero install, zero risk)

**⭐ A1. Read the three-lever finding + issue #6.** (~30 min) The core claim: DeepSeek V4 Pro's *reasoning style* is conditioned by the API-visible tool catalog on request #1. The sharpest datum is issue #6: **~9 KB of auto-injected skill catalog took a reproducible effect from ~81% to 0/9.** Read §4 and §7 of the Deep Dive; you do not need the repo.

**⭐ A2. Read §5 of the Verdict — the evidence table — before believing anything.** (~10 min) Style effect: established (9/9). Quality effect: **not** established (+3.3, 95% CI **[−2.6, +9.3]**, ANOVA ns) — and a second replication found **no correlation** between trajectory and score, disputing even the style effect on current weights. This is the part the repo's tagline ("Project2 98/99") does not tell you.

**A3. Read `FAREWELL.md`.** (~10 min, Chinese; translated in the Deep Dive §2) The most valuable 2.7 KB in the repo. A 3,500-star author writing *"this number doesn't equal my personal technical ability"*, reframing the whole project as *"filling gaps for the official team"*, and naming its own obsolescence condition (train on diverse harnesses — cf. Kimi K3).

**A4. Read `HANDOFF-2.md`.** (~45 min) A genuinely good engineering-pitfalls document — see B7 for what to take from it.

**A5. Read the openinterpreter v223 wiki alongside this one.** (~20 min) Two subjects, same premise (a model's performance depends on the harness it was tuned against), opposite responses (swap the whole harness vs. find one lever inside one harness), both converging on Kimi K3, neither citing the other. The most interesting pairing in the recent corpus.

---

## B — Borrow patterns (zero install, high ROI)

**⭐ B5. Write a tool-surface hygiene rule into `CLAUDE.md`.** (~20 min — **highest ROI on this list**) The vault currently treats its ~54K-token tool catalog purely as a *context-budget* problem. Add the second reason: the surface may also be a **reasoning** variable. Draft rule:

> The connected MCP tool catalog is a reasoning variable, not only a token cost. Prefer the smallest tool surface that can do the job; add tools deliberately, not by default. When a session's reasoning quality matters more than its breadth, start narrow and widen on demand.

Fence it honestly in the note itself: measured on DeepSeek V4 Pro, style effect established, quality effect unproven.

**⭐ B6. Steal the fail-soft/fail-fast split.** (~15 min) `tool-bootstrap.mjs` degrades to the full catalog with a one-time warning when a bootstrap tool is missing (*"a composition drift can never brick every request of a session"*) but throws **at mount** on an invalid `promoteOn`. **Fail-soft at runtime, fail-fast at config time.** A clean rule for the vault's own skills and any hireui LLM feature.

**⭐ B7. Lift `HANDOFF-2.md`'s evaluation discipline into the vault's own eval practice.** (~40 min) The four best lessons:
- **Measure the artifact the downstream consumes, not the pre-cleaned one.** Their quality gate examined pre-cleansing data while verification checked post-cleansing → marginal templates passed the gate and failed verification.
- **Small-n honesty as a habit** — label n=1–4 results *exploratory*, and tag every run with its invariants (harness version, OS, API source, model version).
- **Design probes that isolate one variable at one request per trial** (`probe-clone-runner.mjs`: create → seed → one follow-up → cancel on first assistant message → classify → exit).
- **Beware silent checkpoint drift** — 1/4 one day vs 1/1 the day before, hypothesised as a model-alias switch. Validate with n≥4 before spending.

Composes with **ClawWork v233**'s fails-closed eval gate and **loop-engineering v189**'s REJECT-first verifier.

**B8. Borrow the "blank the family, don't enumerate the sources" principle.** (~10 min) `context-gate` blanks the whole `SystemPrompt.context()` family rather than stripping named sources, so an unknown third-party injection is suppressed by default rather than slipping through. The right default for any allowlist you write.

**B9. Note the vendored-adapter precedent.** (~10 min) When a host's abstraction doesn't expose the knob you need (`tool_choice`), `toolchoice-adapter.mjs` vendors a protocol-faithful subset of the official adapter and registers a **sibling route** rather than monkey-patching — and discloses it in `NOTICE`. A legitimate escape hatch pattern, with the attribution done properly.

---

## C — Hands-on, on your own setup (the one real experiment)

**⭐ C11. Trial Anthropic's Tool Search Tool + `defer_loading: true` on your own Claude Code, and MEASURE it.** (~2–3 h) This is the payoff. `defer_loading` **strips deferred tools from the initial system prompt** and loads them only when searched — the same shape this preset builds by hand, shipped first-party, documented at 77K → 8.7K tokens on the first request. Method:
1. Pick 3 representative real tasks from your own work (a wiki-build step, a hireui ticket, a vault grep-and-synthesise).
2. Run each with your current full MCP catalog; capture token spend via the **ccusage → OTel → Grafana** layer you already have queued.
3. Re-run with the bulk of the catalog deferred behind tool search.
4. Compare **both** axes: tokens *and* your own judgement of output quality.
Pairs directly with the `claude-api-cost-optimization` thread and gives that thread a second dimension it currently lacks.

**⚠️ C12. Trim MCP servers as an infrastructure fix — and now with a second reason.** (~30 min) The vault already needs this: **the Workflow tool failed this session** with all 18 subagents at ~207.2K against a 200K ceiling, and the shim is only ~7K tokens (~30KB) over. Trimming connected servers lowers the ~54K tool-catalog floor. This subject supplies the additional argument that the catalog may also be costing reasoning quality.

**⚠️ C13. Only if you actually run DSH:** install `preset/` per the README, then verify with the repo's own checklist — export the session JSONL and confirm the first `request/header` shows `tools: ["bash","str_replace_editor"]` and no AGENTS.md/skill-catalog messages. Fence: `install-snapshot` first; the preset has *"the same trust level as shell access"*; pinned to rc.5; **do not** use the prefab modes (see 🔴 below).

---

## D — hireui / Goal #2

**⭐ D14. Add "pin and measure your request surface" to the hireui LLM ADR.** (~45 min) The deepest transferable idea in this subject: **the model was RL-trained under one harness condition and degrades under the harness users actually run.** For hireui that becomes a policy line: *the request surface (system prompt, tool schema, injected context) is part of the model's behaviour contract; a change to the surface is a change to behaviour and must be versioned, pinned, and re-evaluated — not treated as configuration.* Slots into the **RATIFIED candidate-LLM legibility ADR** and composes with the eval-gate-outside-the-prompt rule from v209.

**D15. Reuse B7's eval discipline for hireui's first LLM feature.** (~1 h) Match-Explain / candidate-summariser needs exactly this: probes that isolate one variable, invariant tagging, small-n honesty, and a gate measuring the artifact that actually ships. On an `agent-*` branch per hireui's CONSTITUTION (I-2 / I-8 / GitNexus-first).

**🔴 D16. Do NOT use anything from this subject in a candidate-facing path.** The whole point of the preset is to manipulate the model's cognitive style via an undocumented conditioning effect whose benefit is unproven. Candidate-facing inference must be **fixed, legible, audited, human-in-loop and eval-gated** per the ratified ADR. This is the opposite of legible.

---

## E — Vault-meta

**⭐ E17. File the shim-size finding as the #1 housekeeping item, now with a precise target.** (~15 min) Not "compact the shim" — **the shim is ~7K tokens (~30KB) over the ceiling that blocks the Workflow tool.** This ship's head was written compact and v237's demoted to help. One more modest pass should restore multi-agent workflow capability, which has been down since v200.

**E18. Record the cost-economics data-point.** (~15 min) A research project killed by a ~6× inference price rise on a ~$1.70 evaluation round. The lesson for the vault's own loops and pilots: **budget the evaluation, not the build.** Feeds LV-C2 and the `loop-budget` skill.

**E19. Flag the v140 §C row to the audit.** (~10 min) *"Graduated / Least-Privilege Tool-Exposure"* has sat at N=1 since v140 with a *"5-wiki stale-watch ~v155"* long blown (~98 wikis). The audit should **retire or generalise** it — generalising to cover staged tool exposure regardless of rationale would make v238 its N=2 and resolve this ship's boundary question in one move. **Not self-executed** — a promotion or retirement is an audit act.

**E20. Record the Pattern #83 sub-flavour question.** (~10 min) This is **author-accepted third-party provenance correction** (issue #60 forced the fix), which is a stronger form than volunteering one's own gaps. Possibly a new 83 sub-mechanism — for the audit to decide.

---

## F — Optional / landscape

**F21. Skim the sibling ecosystem** — `dsh-routing-suite` (~5.7k★, *"first-turn tool injection"* + a dual-attractor policy paper) and `J-Space-Cognition-Suite` (model-agnostic inference-time cognitive control as a Skill, with effects reported across Claude too). If the class matures, J-Space is the more interesting future subject precisely because it claims cross-family effects.

**F22. Read the prior art directly** — Anthropic's Tool Search Tool docs; arXiv:2604.21816 (tool gating + lazy schema loading); arXiv:2506.22058 (*Lost at the Beginning of Reasoning*). These are the durable sources; this repo is the applied anecdote.

---

## 🔴 Do not

- **Do NOT install the prefab modes.** They seed **80 KB / 212 KB of another person's recorded model reasoning** into your session as history, with stale tool results replayed verbatim (only `skill_search` is re-rendered live). That is a self-inflicted context-injection surface, and the README itself warns both templates *"contain real model reasoning."*
- **Do NOT cite "Project2 98/99."** The repo's own issue #60 retracted the attribution; the runs used a different composition, and nobody has reproduced the number.
- **Do NOT run `custom-bash.mjs` on Windows expecting sandboxing** — its own description says it *"runs without OS sandbox confinement on Windows (no landlock); treat output as untrusted."*
- **Do NOT trust the third-party directories.** `deepseekdocs.com` lists 3,382★ and **no license** against the repo's MIT; `dshplugin.dev` doesn't surface it at all. The repo is authoritative (the v236 lesson, again).

---

## ⭐ The one-thing path

**A1 → B5 → C11**

Read the three-lever finding and issue #6 (30 min, zero install). Write the tool-surface hygiene rule into `CLAUDE.md` (20 min). Then trial `defer_loading` on your own Claude Code and measure it (2–3 h) — the first-party version of this preset's whole idea, on the model you actually use, answering a question your infrastructure has already been asking you.
