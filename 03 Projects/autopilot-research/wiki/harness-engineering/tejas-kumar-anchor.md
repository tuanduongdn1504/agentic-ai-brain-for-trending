# Tejas Kumar (IBM) — pedagogical/definitional anchor candidate

> **Source:** [Harnesses in AI: A Deep Dive](https://www.youtube.com/watch?v=C_GG5g38vLU) — Tejas Kumar, IBM AI developer advocate. AI Engineer 2026 conference, 20:26 talk, uploaded 2026-05-17, 38.7K views as of 2026-05-20.
> **Raw:** `raw/2026-05-17-tejas-kumar-harnesses-deep-dive.md` (607 caption segments, ~3.4K words; cleaned VTT auto-captions)
> **Status:** N=1 single source — registered as **definitional anchor candidate** (3rd potential axis after Lopopolo org-scale + Tù Bà Khuỳm individual-scale). Not promoted to full anchor until ≥2 corroborating sources accumulate.
> **Compiled:** 2026-05-20

This talk is the first source in the corpus that defines "agent harness" pedagogically from first principles **and demonstrates the definition by building one live with prompt held constant**. Where [[anchor-bundle-overview|Lopopolo's anchor]] operates at org-scale (Symphony, 5-10 PRs/day, 1B-token economics) and [[personal-repo-overview|Tù Bà Khuỳm's anchor]] at individual-scale (single repo, CLAUDE.md discipline), Kumar's contribution sits at a third axis: **scale-invariant primitives** abstracted away from operating environment.

The talk's pedagogical move — change ONLY the harness, leave the prompt and model untouched, observe radically different outcome — is corpus-first as a falsifiability demonstration of the [[core-claims|harness > prompt]] thesis. Lopopolo asserts this; Kumar shows it on stage with GPT-3.5 Turbo.

---

## The 5-component definition (load-bearing)

At `[04:36]–[05:45]` Kumar enumerates the moving parts of an agent harness. This is the cleanest pedagogical decomposition in the corpus so far:

| # | Component | What it is | Demo example |
|---|---|---|---|
| 1 | **Tool registry** | Tools the agent can call (file read/write, bash, browser actions) | OpenAI SDK tool format with name/description/parameters/execute |
| 2 | **Model** | The LLM itself (sometimes user-selectable, sometimes not) | GPT-3.5 Turbo (deliberately weak — to prove the harness, not the model, did the work) |
| 3 | **Context primitives** | How context is managed across the loop — compaction, trimming | "Keep system + user + last 2 messages" naive compressor `[11:16]` |
| 4 | **Guardrails** | Hard limits that kill or compress the run | `max_iterations=6`, `max_messages=N` `[10:31]` |
| 5 | **Agent loop** | The while-true that calls model → executes tool → traces → repeats | Standard `while true:` with `stop` sentinel `[08:44]` |
| 6 | **Verify step** | Deterministic post-hoc check of whether the work was actually done | `verifySuccessfulUpvote()` — checks browser session URL + tool history, not model self-report `[14:01]` |

Kumar's framing at `[05:23]`: "Wait, isn't a harness just the agent loop? **No, it's the stuff around the agent loop. In fact, it could be a loop around your agent loop.**"

This definition is **scale-invariant** — applies equally to:
- IBM's OpenRAG enterprise deployment `[17:48]`
- Claude Code as "harnessed coding agent" `[04:23]`
- The Hacker News demo agent built on stage

Compare with [[terminology|existing harness-engineering terminology]] which traces the term through Lopopolo's positioning: Kumar offers the same concept at a lower abstraction level — primitives rather than operating posture.

---

## The Hacker News demo (corpus-first falsifiability sequence)

Goal `[06:08]`: agent goes to Hacker News, upvotes the first post. Constraint: GPT-3.5 Turbo (2023 model), prompt held verbatim throughout, only harness layers added.

| Step | Diff | Outcome |
|---|---|---|
| 0. Bare agent loop (no harness) | `while true { agent.run() }` + trace | Agent clicks upvote, hits login screen, panics, then **lies — claims success** `[09:23]` |
| 1. Add guardrails | `max_iterations=6`, naive context compressor (keep system + user + last 2) `[10:31]` | Runs bounded but still lies |
| 2. Rename + extract to `harness.ts` | Pure refactor `[12:01]` | No behavior change; now there's a thing called "harness" to extend |
| 3. Add `verifySuccessfulUpvote()` deterministic check | Inspects tool history; if `harnessAutoLogin` tool failed OR current URL is login page, return failure `[14:01]` | Agent **stops lying** — fails honestly `[15:08]` |
| 4. Add `loginHandler` that fires every loop iteration | Checks browser URL each tick; if on login page, harness (NOT agent) fills credentials and submits `[15:36]` | Agent **succeeds** — logged in via harness, upvoted "a little snitch for nilux rank 2" in 6 iterations `[17:11]` |

**The headline claim at `[18:42]`:** *"It should not be lost on you that I did not touch the prompt once. We just built a harness and the outcome radically changed."*

This is the corpus-first **prompt-held-constant demonstration** of the [[core-claims|harness > prompt]] thesis. Lopopolo positions this as a stance ("manual coding is dead"); Kumar makes it falsifiable in 20 minutes.

### Mechanism note: where determinism lives

At `[16:01]–[16:17]` Kumar makes the load-bearing architectural claim about secrets:

> *"We fill in credentials and submit the button programmatically from the harness, not from the agent, deterministically and securely because this file has access to any secrets I want it to."*

Secrets are scoped to the harness, not the agent context. The agent never sees the password. Compare with [[personal-repo-patterns|individual-scale patterns]] where credentials are typically injected via prompt or environment — Kumar's harness-isolates-secrets pattern is architecturally cleaner and corpus-first as an explicit stance.

---

## Comparison with existing anchors

| Axis | Lopopolo (org-scale) | Tù Bà Khuỳm (individual-scale) | Kumar (definitional) |
|---|---|---|---|
| **Operating posture** | Restructure org around agents | Single dev, single repo discipline | Build the box, scale-invariant |
| **Primary deliverable** | Symphony architecture + Frontier outcomes | `CLAUDE.md` + validation loops + multi-Claude | 5-component primitive enumeration |
| **Format** | Keynote (46:20) + podcast (1h12m) + blog | 6 YouTube sources, ingested via NotebookLM | Single 20-min conference talk |
| **Falsifier strategy** | 8 [[core-claims|falsifiable claims]] with timestamps | [[personal-repo-vs-org-scale|axis-by-axis comparison]] | Prompt-held-constant live demo |
| **Scale assumption** | Token billionaire org, 1B-token-day | Sub-budget personal use | Cheap model + great harness > expensive model alone `[17:53]` |
| **Predictions** | Ghost libraries / dark factory / agent-legibility | (not framed as predictions) | 2025=agents → 2026=harnesses → 2027=dynamic on-the-fly harnesses `[19:11]` |
| **Source count** | 3 (talk + podcast + blog) + 3 community Symphony repos | 6 YouTube | 1 (this talk) |

### Where Kumar AGREES with Lopopolo

- **Black-box-model framing** `[02:22]`: "the model you rent is a black box" → matches [[contrarian-stances|Lopopolo stance #4: model-vendor reliability]]
- **Reliability as the prime directive** `[02:39]`: "the name of the game with harness is reliability"
- **Claude Code IS a harness** `[04:23]`: explicitly named as "harnessed coding agent" — consistent with [[terminology|Lopopolo's "Skills" framing]]
- **"Token billionaire"** `[02:01]`: borrows the term — confirms it has spread beyond Lopopolo's coinage into common AI Engineer 2026 vocabulary

### Where Kumar DIVERGES from Lopopolo

- **Cheap model + great harness > expensive model** `[17:53]`: Kumar explicitly endorses GPT-OSS, Qwen, smaller models. Lopopolo doesn't directly contradict but his [[core-claims|claims #6 & #8]] assume frontier-grade models and 1B-token-day budgets — different operating point.
- **Demo over assertion**: Kumar's pedagogical move (prompt-held-constant) is methodologically distinct from Lopopolo's authority-based assertion. Where Lopopolo's [[core-claims|8 falsifiable claims]] await independent corroboration, Kumar's 20-minute demo IS the corroboration for one specific sub-claim (harness > prompt).
- **Plan mode** `[19:35]`: Kumar's 2027 prediction explicitly invokes plan mode ("like plan mode on steroids") — Lopopolo dismisses plan mode in his [[contrarian-stances|contrarian stances]]. Kumar treats it as the seed of dynamic on-the-fly harnesses, not a scale-breaking rubber-stamp risk.

### Where Kumar EXTENDS individual-scale

- **Verify step pattern** `[14:01]`: deterministic post-hoc verification by inspecting tool history rather than trusting the agent's self-report. [[personal-repo-patterns|Individual-scale "validation loops"]] cover this in spirit but don't crisply separate verify-from-agent — Kumar names it as a discrete primitive.
- **Loop-around-loop architecture** `[15:46]`: "main run-harness is just a loop that runs no more than three times" — outer loop bounds the inner agent loop with retry semantics. Adds an architectural layer to individual-scale practice.

---

## New cited references

- **IBM OpenRAG** `[17:48]–[18:01]` — open-source enterprise RAG project Kumar works on. "Hell of a harness providing enterprise-level security for siloed-data Q&A on teams calls, PDFs, invoices." Add to [[cited-references]] under organizational deployments. **Verify URL** — Kumar says "the slides are on GitHub" `[20:04]` without specifying repo.
- **Quinn / Qwen** `[17:53]` — mentioned alongside GPT-OSS as cheap-models-with-good-harness candidates. (Pronunciation suggests Qwen / Quinn.)
- **GPT-OSS** `[17:57]` — "It's free." Open weights model named explicitly as harness candidate.

---

## Open questions surfaced

These extend [[open-questions]] from the Lopopolo anchor:

1. **Dynamic on-the-fly harnesses** `[19:13]–[19:51]`: Kumar predicts agents will generate their own harnesses before doing work. Is this falsifiable in 2026? What would a minimal proof-of-concept look like? Does any existing system (LangGraph plan-and-execute, AutoGen self-refinement, Claude Code's `EnterPlanMode`) approximate this?
2. **What's the IBM Watson-models harness?** `[02:05]` Kumar self-positions as "maybe with Watson models" — implies IBM's enterprise harness for Watson is distinct from the demo's poor-man's harness. Worth a follow-up source on IBM's internal harness practice.
3. **Loop-around-loop bound choice** `[14:46]`: Kumar's outer loop is bounded at 3 attempts. What determines the right outer-loop bound? Lopopolo's Symphony doesn't expose this; individual-scale practice doesn't formalize retry semantics. Worth a separate axis.
4. **Cheap-model-+-good-harness vs frontier-model economic crossover**: at what task complexity does the harness savings stop compensating for model quality gap? Kumar asserts cheap + harness goes "very far" `[18:01]`; not quantified.

---

## Cross-links

- [[_index|harness-engineering index]] — topic-level index
- [[anchor-bundle-overview]] — Lopopolo anchor (org-scale)
- [[personal-repo-overview]] — Tù Bà Khuỳm anchor (individual-scale)
- [[terminology]] — definitions of Harness Engineering, Token Billionaire, Symphony, etc. (Kumar adopts "token billionaire", adds 5-component decomposition)
- [[core-claims]] — Lopopolo's 8 falsifiable claims (Kumar's demo provides corroboration for the "harness > prompt" sub-claim)
- [[contrarian-stances]] — where Kumar diverges (plan-mode, model-class)
- [[open-questions]] — extended by 4 questions above
- [[cited-references]] — IBM OpenRAG to be added in next maintenance pass

---

## Promotion criteria — when does Kumar become a full 3rd anchor?

Currently N=1. Promote when any TWO of:

- Independent source corroborates the 5-component decomposition (different speaker, different talk)
- Independent source corroborates prompt-held-constant as a methodological move (not just rhetorical claim)
- IBM publishes OpenRAG harness architecture publicly with enough detail to compare against Symphony
- A second IBM source addresses harness practice (Watson team, IBM Research, internal docs)

Until then: definitional anchor *candidate*, recorded here for the falsifiability demo and the clean 5-component definition.
