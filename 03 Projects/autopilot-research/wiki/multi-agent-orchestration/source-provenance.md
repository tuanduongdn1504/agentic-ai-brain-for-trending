# Source provenance & verification

> **Why this article exists:** per autopilot constitutional rule #4 (NEVER fabricate) and Storm Bear Rule 12 (fail loud), every load-bearing claim in this topic is tiered here so a reader knows exactly what's first-party-confirmed vs. third-party framing vs. single-source. Mirrors [[claude-api-cost-optimization/source-provenance]] and [[prompt-evaluation/source-provenance]].
> **Build:** compiled 2026-06-20 from the video transcript (path 5, `yt-dlp`) + a deep-dive/adversarial-verify Workflow **`wf_d77d2e85-2dc`** (24 agents: 5 source-research → 9 draft→verify article pipelines → 1 pilot draft; 1.29M subagent tokens).

## The caption advantage (this one has a transcript)

Unlike [[agentic-analytics-harness/_index]] (which was uncaptioned and built by triangulation), **this video has full auto-captions.** They were pulled with `yt-dlp 2026.06.09` (`--write-auto-subs`, en), deduped to a ~105K-char transcript, and **read in full by the main loop.** So the *video* claims in this topic are transcript-grounded, not recap. The video metadata (title, channel "ExamPro", **2026-04-29**, **2h9m**, ~57K views at capture, 970 likes) came directly from `yt-dlp --print`, so date/duration are T1-confirmed (view count is volatile — treated as "at capture").

## Source tiers

| ID | Source | Tier | What it backs |
|---|---|---|---|
| S1 | Video transcript (`yt-dlp` auto-captions, vRYBG_R8JAI) | **T1 — primary, verbatim** | Every video-pattern claim: hub-and-spoke, coordinator jobs, the EV-market narrow-decomposition example, dynamic selection, partitioning, planner-vs-coordinator split, refinement loop (incl. score-going-down), observability audit, refactoring moves, the SDK-port narration + the "tool-use got easier… MCP server… Anthropic priority" quote |
| S2 | Video metadata (`yt-dlp --print`) | **T1** | Title, channel, 2026-04-29, 2h9m, view/like counts |
| S3 | [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | **T1 — first-party Anthropic** | The 5 workflow patterns (prompt chaining / routing / parallelization-sectioning+voting / orchestrator-workers / evaluator-optimizer); workflows-vs-agents; when-not-to-use-agents; simplicity/transparency/ACI principles |
| S4 | [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | **T1 — first-party Anthropic** | Orchestrator-worker (Opus lead + Sonnet subagents, isolated contexts); **90.2%** eval gain; token economics (~4× agent, ~15× multi-agent vs chat; ~80% variance from token usage); delegation discipline; parallel-tool-call speedup; LLM-as-judge + human eval; rainbow deployments; stateful/durable execution |
| S5 | Claude Agent SDK docs (`docs.claude.com`/`code.claude.com` agent-sdk) | **T1 — first-party** (fetched by research agent) | `@tool`, `create_sdk_mcp_server` (in-process MCP), `query()`/`ClaudeAgentOptions`/`ClaudeSDKClient`, hooks, sessions, built-in tools, Python+TS (no Ruby) |
| S6 | Claude Code sub-agents docs | **T1 — first-party** (fetched) | Subagent = own context window + custom prompt + restricted tools; communication via delegation + result return (no direct spoke↔spoke) |
| S7 | dev.to article + WebSearch on "CCA-F" / "Claude Certified Architect" | **T2 — third-party, unverified** | Surfaced an alleged Anthropic certification with exam logistics — **deliberately excluded** (see below) |

## What is first-party-confirmed (high confidence)

- The **5 workflow patterns** and their exact names + definitions [S3]; the video's terms map onto them (routing↔dynamic-selection, parallelization-sectioning↔partitioning, orchestrator-workers↔hub-and-spoke, evaluator-optimizer↔refinement-loop, prompt-chaining↔sequential-delegation) — see [[multi-agent-orchestration/video-to-original-crosswalk]].
- The research system's **90.2% gain** (multi-agent Opus+Sonnet vs single Opus) and token economics (~4×/~15× vs chat; ~80% of variance from token usage; model-tier > token-budget) [S4]. These are **Anthropic's numbers, not the video's** — the video does not cite them.
- The Agent SDK **does** replace manual JSON tool schemas + a hand-rolled dispatch loop with `@tool` + `create_sdk_mcp_server` (an in-process MCP server) [S5] — confirms the video's headline port claim.
- Claude Code subagents are **context-isolated and communicate via delegation + result return, not peer-to-peer** [S6] — confirms the video's "spokes never talk directly."
- All video-pattern claims [S1] — transcript-grounded.

## What was STRIPPED during verification (fail-loud)

The adversarial verify pass (and main-loop review) caught and **removed** two fabrication/contamination classes the draft agents introduced:

1. **A "CCA-F official Anthropic certification" framing with exam logistics.** Draft agents pulled "Claude Certified Architect — Foundations, Domain 1 = 27% of exam, 60 questions, 120 minutes, passing 720, $99 fee, launched March 12 2026" from a **third-party dev.to article + WebSearch** [S7] — *not* from the video. The video is merely *titled* "Claude Architect" and links a course at `exampro.co/cca-f`; **whether that maps to any official Anthropic certification is unconfirmed.** All exam-logistics specifics were removed from every article; ExamPro is now described only as a third-party paid course. (Direct analog to the [[prompt-evaluation/source-provenance|"Promptfoo acquired by OpenAI"]] fabrication stripped last ship.)
2. **A cross-topic "Blobotomy" leak.** The crosswalk draft attributed "Blobotomy" / "don't fragment knowledge across agents" to *this* video. That term is from **Omni's talk in [[agentic-analytics-harness/_index]]**, not here — the video never says it. Corrected to point at the real source.

Also fixed: invented in-topic wiki links (`orchestrator-workers.md`, `evaluator-optimizer.md`, `dynamic-routing.md`, `partitioning.md`, `observability.md`) and broken `00 Notes/(C) 2026-06-20-*.md` links in `overview.md` → repointed to the real article files + external URLs; a wrong import (`anthropic_sdk` → `claude_agent_sdk`); a "rainbow deployments" mis-attribution (it's S4, not S3); and a backwards statement of the screener lesson (the video collapses the **three** hard-coded screening spokes into **one agent contextualized N ways** — not the reverse).

## What is single-source / flag before reuse

- **Decorator-evaluation timing** ("runs at call time" vs "definition time"). The closure-via-factory *mechanism* is real; the exact timing is **not documented** [S5] — the video author's "call time" is his framing. Hedged in [[multi-agent-orchestration/agent-sdk-deep-dive]] + [[multi-agent-orchestration/refactoring-and-agent-sdk-port]].
- **Claude Code subagent specifics** — exact frontmatter field list, nested-subagent depth limit, and version numbers (e.g. "v2.1.172", "5 levels") came from a single doc fetch and were **softened**; re-verify against current docs.
- **"Three factors explain 95% of variance"** [S4] — the source states the figure but our digest didn't enumerate the three factors; the article flags it.
- **`evaluate_coverage` / `submit_final` / MAX-STEPS** are the video author's pattern choices, not SDK primitives — labeled as such.

## The one reconciliation (Rule 7 — surfaced, not blended)

**"Claude Architect" (video title) vs "Claude Certified Architect" (alleged cert)** — these are **not asserted to be the same thing.** ExamPro brands the course "Claude Architect"; a third-party article claims a separate Anthropic "Claude Certified Architect" exam. With no first-party confirmation of either the cert or a link between them, this topic treats the video purely as **a third-party teaching artifact** and makes no certification claim.

## Open verification items

- **First-party confirmation of any "Claude Certified Architect" Anthropic certification** — not established; the dev.to/WebSearch material is T2 and was excluded.
- **Current Agent-SDK + Claude-Code-subagent API specifics** — fetched once during the build; the docs move fast. Treat exact field/version/depth claims as point-in-time.
- **The video's final code** — not published by ExamPro; the code shapes here are reconstructed from the narration + S5/S6 docs.

## Key Takeaways

- **Video patterns = transcript-grounded (T1); the deep-dive stats = first-party Anthropic blogs (T1).** This is one of the better-sourced topics in the wiki.
- **The headline risk was the *opposite* of last ship's:** not a missing transcript, but draft agents *adding* unverified scaffolding (a CCA-F exam framing + a Blobotomy leak). The verify pass + main-loop review caught both — the choke point worked.
- **When reusing a claim, check the tier:** Anthropic-blog numbers are solid; SDK/Claude-Code *specifics* and the decorator-timing detail are point-in-time / author-framing — hedge them.
