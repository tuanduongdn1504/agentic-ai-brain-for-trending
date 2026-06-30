# pocock-agentic-workflow

> **Topic index.** Matt Pocock's agentic-engineering philosophy, as laid out in a long-form conversation with David Ondrej. The through-line: **stop obsessing over the model; invest in the *harness*** — the prompts, skills, codebase, and workflow you actually control. AI has eaten *tactical* programming (writing the code); your edge is now *strategic* programming (designing the system the agents work in). Work **AFK** (away-from-keyboard) through a **queue** of scoped tasks, not an infinite loop, and push the human-in-the-loop checkpoints as far right as you safely can.
>
> **Entry point:** [nQwJVHCtDDY](https://www.youtube.com/watch?v=nQwJVHCtDDY) — **"Matt Pocock's Agentic Engineering Workflow (just copy him)"**, a **1:02:24 podcast/interview** on the **David Ondrej** channel (uploaded 2026-06-18, 245,765 views, sponsored by SerpApi). Guest = **Matt Pocock** ([aihero.dev](https://www.aihero.dev/)). Full 12,548-word transcript read.
>
> **⚠️ Not the workshop.** This is the *conversational podcast*, **distinct from** Matt's separate ~96-minute **"Workflow for AI Coding"** talk at **AI Engineer 2026** (April 2026). The workshop-only content — *Smart Zone / ~100k-token ceiling*, *Frederick Brooks "The Design of Design"*, *tracer bullets*, the *4-role Planner/Implementation/Reviewer/Merger* architecture — is **NOT in this podcast** and is **not** attributed to it here. See [[pocock-agentic-workflow/source-provenance]].
>
> **Originals (deep-dived against primary sources):** **[mattpocock/sandcastle](https://github.com/mattpocock/sandcastle)** (`@ai-hero/sandcastle`, the AFK sandbox orchestrator) · **[mattpocock/skills](https://github.com/mattpocock/skills)** (teach / grill-me / to-prd, 150.8K★) · **John Ousterhout — *A Philosophy of Software Design*** (tactical vs strategic) · **Geoffrey Huntley — the Ralph loop** (ghuntley.com/ralph) · **Richard Sutton — *The Bitter Lesson*** · **[obra/superpowers](https://github.com/obra/superpowers)** (Jesse Vincent, 241.7K★ — the model-in-control contrast) · **Vygotsky's Zone of Proximal Development** · **[aihero.dev](https://www.aihero.dev/)**.
>
> **Verification:** Workflow `wf_4562f245-5bc` (23 agents: 11 deep-reads + 11 adversarial verifiers + synthesis; ~931K tokens, 411 tool calls) + operator `gh api` / `yt-dlp` ground-checks. **Two verifiers misfired** (one declared Sand Castle "fabricated" and the podcast "unverifiable" because it couldn't reach GitHub/YouTube) — **overridden** by direct `gh api` + `yt-dlp` ground truth. Several deep-read confabulations (a fake "$10.42/hr" Ralph metric, a "Sourcegraph/Yegge" bio, a "vomit" naming story, an "engineering-zoom-out" skill, a "two-prd" skill) were **caught and stripped**. Full ledger in [[pocock-agentic-workflow/source-provenance]].

---

## Articles

- [[pocock-agentic-workflow/overview]] — who's who (Ondrej × Pocock), the thesis chain in one screen, and Matt's one-line closing prescription: **delete everything → blank slate → observe → layer back only the procedures *you* choose**.
- [[pocock-agentic-workflow/harness-over-model]] — **the central argument.** The F1-engine analogy, "50/50 not 90/10," token-spend = codebase architecture, **DX vs AX** (agent experience), model-agnostic harness, don't-chase-new-models, and the *Bitter Lesson* tension (and why it's miscalibrated — harness ≠ hand-engineered domain knowledge).
- [[pocock-agentic-workflow/strategic-vs-tactical]] — **Ousterhout's** tactical-vs-strategic framework + Matt's AI extension ("AI ate tactical; be strategic"), "**your skills are the ceiling on what AI can do**," and the **Knowledge / Skills / Wisdom** trichotomy.
- [[pocock-agentic-workflow/skills-procedures-vs-abilities]] — **procedures** (user-invoked) vs **abilities** (model-invoked); the **description-leak** problem + `disable-model-invocation`; **stateful vs stateless** skills; the **teach** skill (ZPD); **grill-me** as plan-mode; the **superpowers** (obra) contrast; install command.
- [[pocock-agentic-workflow/afk-queues-not-loops]] — **AFK vs human-in-the-loop**; "**queues, not loops**"; the **Ralph** loop (Huntley) and Steinberger's popularization; pushing HITL checkpoints right; auto-merging trivial PRs but spot-checking the reviewer-AI; **self-improving systems** ("if someone keeps stealing your bike, buy a lock").
- [[pocock-agentic-workflow/sandcastle-deep-dive]] — **the load-bearing original.** `@ai-hero/sandcastle` mechanism: 5 sandbox providers, 6 agent providers, `run()` / `fork()`, three branch strategies, the **security nuance** (bind-mount ≠ documented guarantee), and the **GitHub-Actions reality** (Matt's "agent-review" is *his repo's internal CI*, not a published reusable action).
- [[pocock-agentic-workflow/the-originals]] — provenance of every cited idea: Ousterhout, Huntley/Ralph, Sutton, obra/superpowers, Vygotsky/ZPD, aihero.dev — **who originated what**, with the corrections.
- [[pocock-agentic-workflow/caveats-and-disagreements]] — **the critic layer.** David's three pushbacks (swap-the-engine-and-everything-improves; better models find *deeper* bugs; do-both), where Matt is stating *opinion* not fact, and the claims that are unverified.
- [[pocock-agentic-workflow/source-provenance]] — the verified-vs-corrected ledger, the two-video distinction, the verifier-misfire overrides, and the **don't-re-fabricate** list.

## Pilot methods (how to apply this to your flow)

A ranked menu of **23 methods + a skip-list + a critic's reframe** lives in **`output/(C) 2026-06-30-pocock-agentic-workflow-pilot-methods.md`**, across four angles: **hireui Goal #2** (blank-slate harness, grill-me-as-plan-mode, codebase-as-harness AX audit on the Candidate Detail refactor, a Sand Castle spike), **personal Claude Code** (procedure-first skill hygiene, `disable-model-invocation` audit, model-discipline), the **autopilot/Storm Bear vaults** (queues-not-loops already lives here; teach skill; self-improving review loop), and **Scrum coaching** (strategic-vs-tactical as the new seniority axis; DX=AX; enthusiasm-beats-experience hiring).

## Cross-topic links

- [[../harness-engineering/_index]] — the **org-scale** sibling (Lopopolo): "humans steer, agents execute." Pocock is the **individual-scale** articulation of the same harness-over-model thesis.
- [[../autonomous-loops-human-in-the-loop/_index]] — AFK loops, Ralph, goal-driven cycles, the thin HITL slice — Pocock's "queues not loops" is the sharper reframe.
- [[../workflow-ai-coding/_index]] — already features Pocock + the Ralph loop + grill-me-vs-plan-mode; this topic is the deep single-source treatment.
- [[../claude-skills/_index]] · [[../claude-code-skills-stack/_index]] — skills landscape; superpowers (obra) and grill-me appear in both.
- [[../claude-code-memory-systems/_index]] — **stateful skills** (teach) = file-as-memory; Ralph's file-system-as-state is the same lineage (Karpathy LLM Wiki).
- [[../claude-api-cost-optimization/_index]] — "optimize token spend = improve codebase architecture, then a cheaper model succeeds."
- [[../how-we-claude-code/_index]] — the *Bitter Lesson* also appears there (as Arno's analogy); grill-me ≈ interview-first specs; agent-native verification = a richer review surface.
- [[../ai-engineering/_index]] — demo→production discipline; the strategic layer Pocock keeps for the human.
- [[../prompt-evaluation/_index]] — the "review the system that produces the code, not just the code" loop = eval/verify discipline.
- [[../claude-code-observability/_index]] — "observability into your harness" is exactly what review gives you.

## Key Takeaways

- **Harness > model (but 50/50, not 90/10).** You control the prompts, skills, codebase, and workflow far more than you control the model. Invest there. The engine matters; so does everything around it.
- **AI ate tactical programming; your edge is strategic programming** (Ousterhout). You're now the *general*, orchestrating an "infinite fleet of tactical programmers." **Your skills are the ceiling on what AI can do.**
- **Procedures over abilities.** Prefer **user-invoked** skills you drive (grill-me, to-prd) over model-invoked ones; every model-invoked skill **leaks its description into context** — use `disable-model-invocation: true` to keep the human in control and the context lean.
- **Queues, not loops; AFK, not babysitting.** Development is a queue of scoped tasks worked by parallel agents (Sand Castle), with **human checkpoints pushed as far right as is safe** — and you still **review the *system* that produces the code**, not just the code.
- **The contrarian closer:** *delete every skill / plugin / MCP / CLAUDE.md / AGENTS.md → go to a blank slate → observe the agent → layer back only the procedures you deliberately choose.* Then delegate implementation to AFK agents.
