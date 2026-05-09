# Research roadmap — sequencing the next ingests

> The anchor (see [[anchor-bundle-overview]]) defines the conceptual surface. This roadmap orders the next 10 ingestion candidates by leverage — which sources most expand or stress-test what we have.

## Ranking criteria

Each candidate scored on:
- **A. Falsification potential** — could it disprove a [[core-claims|core claim]]?
- **B. Gap closure** — does it address an [[open-questions|open question]]?
- **C. Disagreement amplification** — does it sharpen or counter a [[contrarian-stances|contrarian stance]]?
- **D. Foundation depth** — is it a cited source whose primary form differs materially from how Lopopolo framed it?

## Tier 1 — same-author corroboration (run before any external work)

### 1. OpenAI engineering blog "Harness Engineering"
- **URL:** https://openai.com/index/harness-engineering/
- **Status:** 403 during 2026-05-09 ingest; needs custom-scraper retry
- **Why:** canonical written form of the same content. Differences between speech and edited prose reveal which claims Lopopolo doubles down on vs softens. Highest-leverage same-author ingest.
- **Method:** Path 6 (custom scraper, Playwright headed) — pattern from [[external|telegram-remote-control-stack/setup-recipe-a]]. Then `notebooklm source add` to existing notebook `d772d58b`.

### 2. Bret Taylor public statements on agentic engineering
- **Why:** Lopopolo cites him as agreeing with claim #7 ("dependencies going away"). Independent corroboration if he's saying the same thing in his own words; medium-strength counter if he's saying something subtly different.
- **Method:** Path 5 (yt-search "Bret Taylor agents OpenAI") → if 5+ videos, escalate to Path 1 yt-pipeline.

## Tier 2 — falsifier + ceiling-bounder ingests

### 3. Datadog / Temporal "vendoring ceiling" investigation
- **Why:** Lopopolo names these explicitly as exceeding current agent vendoring capacity ([[open-questions#5]]). Concrete bounds on claim #7.
- **Method:** Path 4 multi-bundle (Datadog engineering blog + Temporal docs + any "we tried to replace X with vendored code" post-mortems on HN/Substack).

### 4. Anthropic response to MCP criticism
- **Why:** Lopopolo's strongest contrarian stance ([[contrarian-stances#8]]) directly challenges Anthropic's MCP. Anthropic's measurement or response is high-leverage — sharpens the disagreement axis.
- **Method:** Path 4 multi-bundle (Anthropic blog + MCP spec + community responses).

## Tier 3 — foundation deepening

### 5. Rich Sutton "The Bitter Lesson"
- **Why:** cited as foundational rationale ([[cited-references]]). Should have its own wiki article in the autopilot vault — it's a load-bearing reference for many AI engineering threads, not just harness engineering.
- **Method:** Path 3 single-URL ingest of the original 2019 essay + maybe 2 commentary pieces.

### 6. Elixir / Beam for agent orchestration
- **Why:** Symphony's architectural choice is treated as load-bearing. If true, this is a portable recommendation; if Lopopolo-specific bias, less so.
- **Method:** Path 1 yt-pipeline "Elixir Beam concurrency agent orchestration" + Path 3 (Alex Kotliarskyi posts if discoverable).

## Tier 4 — comparative + adjacent

### 7. Cursor / Aider / Claude Code harness comparison
- **Why:** Lopopolo's harness is OpenAI-centric. Comparative material from Cursor's or Anthropic's stack stress-tests claim #5 (hyper-modular architecture) and the MCP disagreement ([[contrarian-stances#8]]).
- **Method:** Path 1 yt-pipeline "Cursor Aider Claude Code harness internals".

### 8. Lovable / Bolt / Replit zero-to-one tooling
- **Why:** Lopopolo distinguishes harness engineering FROM zero-to-one scaffolding ([[open-questions#3]]). Understanding the distinction better refines the topic boundary.
- **Method:** Path 5 yt-search → triage → Path 1.

## Tier 5 — meta + governance

### 9. Symphony-class orchestrators (open source equivalents)
- **Why:** Symphony is internal at OpenAI. Open-source attempts (e.g., Inngest, Temporal-for-agents, LangGraph) are the comparison surface — even though Lopopolo dismisses scaffolds, the question is whether a non-OpenAI team can reproduce his throughput claim.
- **Method:** Path 1 yt-pipeline "agent orchestration framework Symphony".

### 10. "Frontier"-class enterprise governance for AI agents
- **Why:** Frontier wraps Symphony with safety + governance. Enterprise adoption of agentic workflows is the deployment ceiling — RBAC, audit, FinOps, compliance posture are the gating items.
- **Method:** Path 4 multi-bundle (enterprise AI governance reports + SOC2-for-agents discussions).

## Sequencing recommendation

If running the routine sequentially:
1. Tier 1 (#1, #2) — anchors author corroboration
2. Tier 2 (#3 OR #4 depending on which axis you want to develop first)
3. Tier 3 (#5) — foundational reading that benefits other threads too
4. Then Tier 4-5 as cycles permit

If running overnight cron with topics-queue:
- Add #1, #3, #5 to `topics-queue.md` together — they hit different axes (corroboration / falsification / foundation)
- Avoid running #2 + #4 in same cycle — too much OpenAI-OpenAI in one batch

## Maintenance

When an ingest from this roadmap completes, add a `### Completed YYYY-MM-DD` block under the candidate with the wiki link to the new article(s). Don't delete the candidate — it's the audit trail of what we ingested when.
