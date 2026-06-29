# Eric Tech's 8-Skill Claude Code Stack: Ranked Pilot Methods for Storm Bear

> **Source:** Eric Tech — "8 Claude Code Skills Every Developer Needs in 2026" ([Va-U1dqhwzk](https://www.youtube.com/watch?v=Va-U1dqhwzk), 2026-04-24, 32:52, 10.3K views).
> **Originals (all `gh api`-verified 2026-06-29):** Superpowers `obra/superpowers` 240.9K★ · Skill Creator `anthropics/skills` 156.4K★ · GSD `gsd-build/get-shit-done`→`open-gsd/gsd-core` · G-Stack `garrytan/gstack` 117.8K★ · UI UX Pro Max `nextlevelbuilder/ui-ux-pro-max-skill` 97.6K★ · Awesome Design MD `voltagent/awesome-design-md` 94.1K★ + Google Stitch `design.md` · Playwright CLI/MCP (Microsoft) · Obsidian `kepano/obsidian-skills` 38.8K★ · /fix-ticket `EricTechPro/startup-claude-skills` 51★ · marketing `ericosiu/ai-marketing-skills`.
> **Date:** 2026-06-29. **Operator:** Storm Bear (Karpathy LLM-Wiki maintainer ×2 vaults + ~/.claude memory + Scrum coach + hireui/TalentAxis Goal #2).
> **Verification:** deep-dive + adversarial Workflow `wf_04da379d-ca9` (21 agents) + independent `gh api` ground-check. Full ledger: [source-provenance](../wiki/claude-code-skills-stack/source-provenance.md). Companion wiki: [claude-code-skills-stack](../wiki/claude-code-skills-stack/_index.md) (12 articles).

---

## Headline Insight

**You are the target user twice over.** (1) Skill #6 (Obsidian) is *literally the pattern you already run* — two LLM-Wiki vaults + a `~/.claude` memory; installing `kepano/obsidian-skills` is a format-fluency upgrade, not a new idea. (2) Skills #1/#5/#8 (Superpowers/Playwright/fix-ticket) are built for exactly the **real-software target you already have: hireui**.

So the video's value for you is **discipline + composition, not discovery**. The one genuinely new, high-leverage move is the **composition meta-move**: use the first-party **Skill Creator** to merge the best *stage* of three rival SDD frameworks (Superpowers brainstorm/TDD + G-Stack persona-review/security/QA + GSD context-isolation) into one custom skill — *and you already have a competing pilot (cc-sdd v61) to benchmark it against*. That's your fastest path to resolving Goal #2 with measured evidence, not vibes.

Two cautions before you spend a minute: the **design layer is already better-covered** by the Taste Skill you surfaced in [[ai-web-design-workflow]] (don't add a redundant design tool reflexively), and the **marketing skills are Eric Osiu's, not Eric Tech's** (and low-priority for you right now).

---

## ▶ Start Here (3-Step Sequence)

1. **Week 1 — Install `kepano/obsidian-skills` in both vaults (Flow B) + Superpowers on a throwaway repo (Flow A).** Zero-risk format-fluency upgrade for the vaults (~10 min) so Claude emits valid `.base`/`.canvas`/wikilinks during drains/audits; in parallel, `/plugin install superpowers@claude-plugins-official` on a sandbox to feel the brainstorm→plan→TDD pipeline. **Measure:** malformed-file rate in next compile; whether Superpowers' spec-first gate changes your output quality.

2. **Week 2 — hireui (Flow C): run ONE real ticket end-to-end through a TDD harness + Playwright CLI QA.** Pick a small TalentAxis ticket; drive it with Superpowers (or your already-ranked cc-sdd pilot) + `microsoft/playwright-cli` for screenshot+console QA. Stay inside hireui (GitNexus + I-2 agent-branch + I-8 operator-installs). **Measure:** discipline-overhead vs value; QA-report usefulness; token cost (CLI vs MCP).

3. **Week 3 — Build your own merged skill via Skill Creator (Flow A) and EVAL it against cc-sdd.** Compose: brainstorm=Superpowers · persona/security review=G-Stack `/plan-ceo-review`+`/cso` · context-isolation=GSD · QA=Playwright CLI · ship=G-Stack `/ship`, behind a ticket-classifier. Use Skill Creator's grader/comparator to benchmark *your* skill vs cc-sdd vs vanilla. **Measure:** pass-rate / tokens / latency — this is the Goal #2 evidence you've been missing.

---

## Ranked Methods Table

| Rank | Method | Flow | Effort | Value | First Step | Success Signal |
|------|--------|------|--------|-------|-----------|-----------------|
| 1 | **Install `kepano/obsidian-skills` in both vaults** | B | Low | High | Copy `skills/` into each vault's `.claude/skills/`; run a compile | Claude emits valid `.base`/`.canvas` + clean `[[wikilinks]]`; fewer malformed files |
| 2 | **Compose + EVAL your own `build-feature` skill (the meta-move)** | A | High | High | Skill Creator → enumerate Superpowers/GSD/G-Stack stages → build merged skill → benchmark vs cc-sdd | Merged skill beats components on pass-rate/tokens in Skill Creator benchmark |
| 3 | **Superpowers (or cc-sdd) TDD harness on one hireui ticket** | C | Med | High | `/plugin install superpowers@claude-plugins-official`; run a small TalentAxis ticket | Spec-first + TDD produces a mergeable PR with tests; overhead worth it |
| 4 | **Playwright CLI QA on hireui (not MCP)** | C | Med | High | Add `playwright-qa-cli` skill; run a flow; capture screenshots+console → QA report | QA report table with per-step evidence; ~4× cheaper than MCP confirmed |
| 5 | **Skill Creator → formalize a fuzzy autopilot skill + eval** | A | Med | High | Run Skill Creator on `yt-search`/`notebooklm`; write evals; benchmark | SKILL.md with assertions + pass-rate baseline; ready for routine v2.2 |
| 6 | **/fix-ticket *architecture* for hireui via official MCPs** | C | High | High | Wire Sentry MCP + Atlassian/Jira MCP + Vercel MCP; build reproduce→approve→fix→verify→ship skill | One real bug auto-driven to a reviewed PR with HITL approval gate |
| 7 | **G-Stack `/cso` security audit on hireui** | C | Low | High | Install `garrytan/gstack`; run `/cso` (OWASP+STRIDE) on a candidate-PII path | Security findings list for a PII-handling route; feeds hireui CONSTITUTION |
| 8 | **Skill Creator Create→Eval→Improve loop = routine v2.2 template** | B | Med | High | Adopt the 4-stage loop as the skill-authoring spec in routine v2.2 | routine v2.2 skill-authoring section drafted around eval-driven loop |
| 9 | **Design bake-off: Taste Skill vs UI UX Pro Max vs brand `DESIGN.md`** | C | Med | High | Run hireui Candidate-Detail screen through all three; compare to Figma SoT | One wins on Figma-parity; decision documented; redundant tools dropped |
| 10 | **Extract a TalentAxis `DESIGN.md` (codify brand tokens)** | C | Med | High | Build a `DESIGN.md` from the Figma handoff; version it; feed to the agent | Token-drift root cause (your spike) gets a single source of truth |
| 11 | **GSD context-isolation for long autopilot/vault runs** | B | Med | Med | Use `open-gsd/gsd-core` phase-isolation on a multi-source drain | Fewer context-rot failures on big compiles; STATE.md survives sessions |
| 12 | **SDD-framework comparison as a Scrum workshop** | D | Low | High | Teach Superpowers(TDD) vs GSD(context) vs G-Stack(persona) as 3 disciplines | Team can name when to use each; maps to your harness-engineering corpus |
| 13 | **Superpowers 2–5-min task slicing as sprint-slicing lesson** | D | Low | Med | Demo writing-plans output; map to backlog refinement | Coaches adopt bite-size-task + DoD-gating framing in refinement |
| 14 | **G-Stack persona panel as a review-discipline lesson** | D | Low | Med | Demo `/plan-ceo-review` + `/design-review` as multi-perspective review | Team runs structured pre-merge perspective reviews |
| 15 | **Telegram skill + reset-hook for remote hireui/vault runs** | A | Low | Med | Install official Telegram plugin; add a `/reset` fresh-context hook | Drive a long QA/compile from phone; clean context per session |
| 16 | **Pattern Library evidence: log Superpowers/G-Stack/GSD** | B | Low | Med | File as Pattern #21 (SDD) + #76 (adversarial review) evidence at next audit | 3 new SDD instances + persona/2-stage-review evidence recorded |
| 17 | **Awesome Design MD as deliverable-styling for autopilot reports** | B | Low | Low | Copy a clean `DESIGN.md` for HTML deliverables/slides | Autopilot HTML outputs get consistent, non-slop styling |
| 18 | **Playwright MCP for hireui Candidate-Detail pixel/Figma detail** | C | Med | Med | Use MCP (not CLI) for the one high-fidelity detail-comparison pass | Accurate detail diff vs Figma where CLI snapshots are too coarse |
| 19 | **`ccusage`/observability baseline before any harness pilot** | A | Low | Med | Run `ccusage` on `~/.claude` JSONL pre/post each pilot | Token/cost delta per harness measured (composes w/ cc-observability) |
| 20 | **Skill Creator description-optimization on your vault skills** | B | Low | Med | Run the analyzer's description-tuning on `(C) autopilot-research-routine` etc. | Skills trigger more reliably; fewer mis-fires |
| 21 | **Humanizer/SEO from `ai-marketing-skills` for TalentAxis site** | C | Low | Low | Vet + run 1–2 Eric-Osiu skills on TalentAxis marketing copy | Cleaner copy; only if/when a marketing motion exists |
| 22 | **`defuddle` (Obsidian skill) to replace ad-hoc web-extraction** | B | Low | Low | Use `defuddle` in ingestion for clean article→markdown | Cleaner raw/ ingests; one less bespoke scraper path |

---

## Detailed Methods by Flow

### **Flow A — Personal Claude Code Harness / SDD (build-your-own + measure)**

**A1. Compose + eval your own `build-feature` skill (the meta-move).** This is the single most valuable idea in the video applied to you. With Skill Creator: enumerate each framework's stages, then build one skill that routes brainstorm→Superpowers, persona+security review→G-Stack (`/plan-ceo-review`, `/cso`), context-isolation→GSD, execute(TDD+parallel)→Superpowers, QA→Playwright CLI, ship→G-Stack `/ship`, behind a ticket-classifier (small/med/large; UI/API/full/infra) that *skips* stages by work type. Then use Skill Creator's `grader`/`comparator` to benchmark it vs **cc-sdd** (your already-ranked #1 pilot) vs vanilla. **Success:** a documented expected-value table — this is your Goal #2 evidence.

**A2. Formalize a fuzzy autopilot skill via Skill Creator + evals.** Pick `yt-search` or `notebooklm`; run Create→Eval→Improve→Benchmark; write 10–20 assertions from real failures (your prompt-evaluation discipline). **Success:** eval-backed SKILL.md + a pass-rate baseline you can trend. Composes with the `evals/` harness (A1 anchor gate) — don't rebuild it.

**A3. Telegram skill + reset-hook for remote runs.** Install the official Anthropic Telegram plugin (`anthropics/claude-plugins-official`); add Eric's `/reset` fresh-context hook pattern. **Success:** drive a long hireui QA or vault compile from your phone with a clean context per session. (You've already piloted [[telegram-remote-control-stack]] Recipe A — this is the skill-ified version.)

**A4. `ccusage` baseline before/after each pilot.** Measure token/cost deltas per harness so "discipline overhead" is a number, not a vibe. **Success:** per-harness cost delta recorded; feeds [[claude-code-observability]] cache-hit-rate work.

---

### **Flow B — autopilot-research + Storm Bear Vaults (the Obsidian pattern is yours already)**

**B1. Install `kepano/obsidian-skills` in both vaults.** The highest value-to-effort move on the list. Copy `skills/` (obsidian-markdown / obsidian-bases / json-canvas / obsidian-cli / defuddle) into each vault's `.claude/skills/`. **Why:** you run the Karpathy LLM-Wiki pattern by hand-rolled `CLAUDE.md` rules; this makes the *agent* fluent in Obsidian's syntax so compiles/audits stop emitting malformed `.base`/`.canvas`/wikilinks. **Success:** zero malformed-format files in the next compile cycle. (Note: the skill is Steph Ango's *personal* repo, not official Obsidian — but it's MIT + by Obsidian's CEO; safe.)

**B2. Skill Creator's Create→Eval→Improve→Benchmark as the routine v2.2 skill-authoring spec.** You have 20 accumulated routine-v2.2 codification candidates. The eval-driven loop is a ready-made framework for the skill-authoring discipline section. **Success:** routine v2.2 draft adopts the 4-stage loop; the long-pending codification gets unblocked.

**B3. GSD context-isolation on big multi-source drains.** Use `open-gsd/gsd-core`'s phase-isolation (fresh 200K per executor) for large compiles to fight context rot. **Success:** fewer mid-compile context failures; STATE.md/CONTEXT.md persist across sessions. (Sibling to [[claude-code-memory-systems]] context-rot framing.)

**B4. Log the three SDD frameworks as Pattern Library evidence.** At the next Storm Bear mini-audit, file Superpowers/GSD/G-Stack as Pattern #21 (SDD Methodology Emergence) instances and G-Stack's persona + Superpowers' 2-stage per-task review as Pattern #76 (Adversarial Subagent Review) evidence. **Success:** 3 new SDD instances recorded; strengthens both patterns toward promotion.

**B5. `defuddle` + Awesome Design MD for ingestion + deliverables.** Use `defuddle` (in the Obsidian skill) for clean web→markdown ingests; copy a `DESIGN.md` for consistent autopilot HTML/slide styling. **Success:** cleaner `raw/` ingests; non-slop deliverable styling. Low priority.

**B6. Skill Creator description-optimization on existing vault skills.** Run the analyzer's description-tuning on `(C) autopilot-research-routine`, `yt-pipeline`, etc. **Success:** skills trigger more reliably (fewer mis-fires / missed triggers).

---

### **Flow C — hireui Goal #2 (TalentAxis SaaS — the real-software target)**

> Execute hireui-rooted (GitNexus + Figma MCP + I-8 operator-installs + I-2 agent-* branch + BMAD). Adopt *architectures*, not repos wholesale; audit any third-party skill before install.

**C1. Run ONE real ticket through a TDD harness (Superpowers or cc-sdd).** Smallest viable comparison: same ticket, Superpowers vs cc-sdd, measure discipline-overhead vs value. **Success:** a mergeable PR with tests; a defensible read on which harness fits hireui.

**C2. Playwright CLI QA (default) on a hireui flow.** Add the `playwright-qa-cli` skill (public, MIT); run a multi-phase pass capturing screenshot+console per step → QA report. Reserve **MCP** for the one high-fidelity Candidate-Detail/Figma detail pass. **Success:** QA-report table with per-step evidence; CLI's ~4× token saving confirmed on a real suite.

**C3. /fix-ticket architecture via official MCPs.** Build hireui's own bug-fix skill: Sentry MCP (logs) → Jira/Atlassian MCP (ticket) → reproduce (Playwright CLI) → research subagents → **plan + HITL approval** → fix (TDD) → verify (Playwright) → Vercel MCP (deploy) → ticket update + human-QA handoff. **Success:** one real bug auto-driven to a reviewed PR with the approval gate intact. This is the most hireui-shaped pattern in the whole video — but it's a *build-it-right spec* (hireui has no LLM yet), not a retrofit.

**C4. G-Stack `/cso` security audit on a candidate-PII path.** `garrytan/gstack` `/cso` runs OWASP Top-10 + STRIDE. Run it on a PII-handling route. **Success:** a findings list that feeds the hireui CONSTITUTION + your no-LLM-yet data-sovereignty plan (see [[cowork-third-party-inference]] BYOM).

**C5. Design bake-off: Taste Skill vs UI UX Pro Max vs brand `DESIGN.md`.** Run the Candidate-Detail screen (your refactor spike) through all three against the Figma source-of-truth. **Success:** one approach wins on Figma-parity; the others are consciously dropped (no tool sprawl). Likely winner per prior research: Taste Skill as the *gate* + a `DESIGN.md` as the *brand source*.

**C6. Extract + version a TalentAxis `DESIGN.md`.** Codify the real hireui brand tokens (navy/accent/Inter→Roboto/spacing/type) from the Figma handoff into one `DESIGN.md`. **Success:** the token-drift root cause from your Candidate-Detail spike gets a single source of truth the agent reads on every UI task.

**C7. Playwright MCP for the one pixel/Figma detail pass.** Where CLI disk-snapshots are too coarse, use MCP's richer state for the detail diff. **Success:** accurate detail comparison on the highest-fidelity screen.

---

### **Flow D — Scrum Coaching / Teaching Teams**

**D1. SDD-framework comparison workshop.** Teach the three real differentiators: Superpowers = TDD/execution discipline; GSD = per-agent context isolation; G-Stack = persona-based multi-perspective review + browser QA + security. **Success:** team can articulate *when to use each*; ties directly to your [[harness-engineering]] corpus.

**D2. Superpowers task-slicing → sprint-slicing.** Show `writing-plans` decomposing a feature into 2–5-min tasks with explicit verification; map to backlog refinement + Definition of Done. **Success:** coaches adopt bite-size-task + DoD-gating framing.

**D3. G-Stack persona panel → review discipline.** Demo `/plan-ceo-review` + `/design-review` as structured multi-perspective pre-merge review (vs one rubber-stamp). **Success:** teams run perspective reviews; reduces single-reviewer blind spots.

**D4. "Skills replace junior toil" — the honest version.** Use the video's "90% of junior jobs" claim as a *teaching foil*: the real signal is junior-hiring freezes + a shift toward review/QA roles, not elimination. **Success:** a balanced team conversation about where agents take routine toil vs where humans move up — not hype.

---

## What to Consciously SKIP (and Why)

- **Don't add a redundant design tool reflexively.** You already surfaced the **Taste Skill** ([[ai-web-design-workflow]]) + Anthropic's `frontend-design`. Run the C5 bake-off first; only keep what wins on Figma-parity. UI UX Pro Max and Awesome Design MD are alternatives, not additions-by-default.

- **Don't prioritize the "43 marketing skills."** They're **Eric Osiu's** (`ericosiu/ai-marketing-skills`), cited not authored, and you have no active consumer-SaaS marketing motion. The 0→1000-users attribution is unverifiable. Park it.

- **Don't install the *archived* GSD.** `gsd-build/get-shit-done` is archived — use **`open-gsd/gsd-core`**.

- **Don't copy Eric's `/fix-ticket` repo wholesale into hireui.** Adopt the *architecture* via official MCPs (Sentry/Jira/Vercel) under hireui's BMAD + I-2 + I-8 governance. His repo is a 51★ individual-author template — audit, don't import.

- **Don't believe "90% of junior jobs" or "trained on hundreds of datasets."** Hyperbole and a flat factual error respectively (UI UX Pro Max is a CSV reasoning engine). Cite the [source-provenance](../wiki/claude-code-skills-stack/source-provenance.md) corrections if you reuse these claims anywhere.

- **Don't treat the Obsidian skill as "official Obsidian" or "a RAG."** It's Steph Ango's *personal* repo and a *format-handling* skill; the RAG-like behavior is the Karpathy pattern *you already run*. Install it as a format upgrade, nothing more.

- **Don't run more than one harness pilot at a time without a baseline.** Measure with `ccusage` (A4) so "discipline overhead" is a number.

---

## Critic's Reframe

Eric Tech's video is a competent, genuine daily-driver tour — and a top-of-funnel for a paid Skool community ($19→$99/mo). The skills are real and mostly free; the *gating* is on his community/templates, not the core tools (verification confirmed his own skills are public). The framing inflations are the usual creator-economy tax: "90% of junior jobs", "trained on hundreds of datasets", "built by Obsidian" (it's the CEO personally, not the company), "43 skills I used" (someone else's).

For **you specifically**, the honest takeaway is smaller and sharper than "8 must-have skills": you already run the memory pattern (skill #6), already have the design lever (Taste Skill), and already have a better-scoped harness pilot queued (cc-sdd). The *one* thing the video adds that you haven't operationalized is the **compose-three-frameworks-then-eval-it** move — and that's valuable precisely because it forces a measurement (Skill Creator benchmarks) on the harness question you keep deferring. Do that against cc-sdd, on a real hireui ticket, and you convert "I'm sitting on N ranked pilots, 0 deployed" into actual Goal #2 evidence. Everything else here is reinforcement of disciplines you already track.

---

## Cross-Links to Sibling Wiki Topics

- **[claude-skills](../wiki/claude-skills/)** — the *other* "8 skills" video (Ben AI's meta-skills). Eric's Skill Creator and Ben's MCP Builder both live in the same first-party `anthropics/skills` repo. Compose, don't duplicate.
- **[ai-web-design-workflow](../wiki/ai-web-design-workflow/)** — the **Taste Skill** is your stronger design lever; C5 bake-off pits it against this video's design skills.
- **[harness-engineering](../wiki/harness-engineering/)** — Superpowers/GSD/G-Stack are individual-scale harness instances; Pattern #21/#76 evidence (B4).
- **[claude-code-memory-systems](../wiki/claude-code-memory-systems/)** — the Obsidian skill = the L1/L5 substrate; you already run L1+manual-L2 + two L5 vaults.
- **[prompt-evaluation](../wiki/prompt-evaluation/)** — Skill Creator's grader/comparator IS LLM-as-judge; compose with your `evals/` A1 gate (A1/A2).
- **[claude-api-cost-optimization](../wiki/claude-api-cost-optimization/)** — CLI-vs-MCP (~4×) + Superpowers v6.0 token cut; measure with [claude-code-observability](../wiki/claude-code-observability/).
- **[telegram-remote-control-stack](../wiki/telegram-remote-control-stack/)** — the Telegram skill, already piloted (A3).
- **[multi-agent-orchestration](../wiki/multi-agent-orchestration/)** — Superpowers parallel-agents / subagent-driven dev.

---

## Suggested Next Action

**This week:** B1 (install `kepano/obsidian-skills` in both vaults — ~10 min, zero risk) + A-sandbox Superpowers. **Report:** malformed-format-file rate change; did Superpowers' spec-first gate change your output?

**Week 2:** C1 + C2 on one hireui ticket (TDD harness + Playwright CLI QA), hireui-rooted under I-2/I-8. **Report:** discipline-overhead vs value; QA-report usefulness; CLI vs MCP token cost.

**Week 3:** A1 — build your merged `build-feature` skill and EVAL it against cc-sdd via Skill Creator. **Report:** the expected-value table (pass-rate/tokens/latency). *This is the Goal #2 evidence to bring to a mini-audit.*

**Decision to tee up:** after Week 3 you'll have a measured answer to "which SDD harness for hireui?" — Superpowers vs cc-sdd vs your-merged-skill — which finally moves "N ranked pilots / 0 deployed" forward.

---

**File prepared for Storm Bear's vault. The stack is mostly disciplines you already track — the win is composing them and *measuring* on real hireui work.**
