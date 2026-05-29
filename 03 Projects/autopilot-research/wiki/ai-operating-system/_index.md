# ai-operating-system

> The "Agentic OS" / "Second Brain" framing — building a personal AI workforce from structured Markdown + skills + MCP + sub-agents. Sister topic to [[../claude-cowork/_index]] (Anthropic's first-party desktop version of the same pattern) but framed at the **builder** layer rather than the **product** layer.

**Drained:** 2026-05-29 (autopilot loop)
**Raw source:** [`raw/2026-05-29-ai-operating-system-5-skills-framework.md`](../../raw/2026-05-29-ai-operating-system-5-skills-framework.md)
**NotebookLM notebook:** `1f5811fb-60c1-4857-a039-c784508b2ec4`
**Sources:** 6 YouTube videos (1 anchor + 5 yt-search), Feb–May 2026, total ~13 hours runtime

## Articles

- [[overview]] — what an "Agentic OS" is, key practitioners (Ben AI / Mani Kanasani / Ross Mike / Remy Gaskell / Simon Scrapes / Greg Isenberg / Nick Saraev / Fireship), tool landscape, the AIOS-vs-Cowork-vs-Claude-Code distinction
- [[instruction-layer-markdown-files]] — `claude.md` / `agents.md` / `soul.md` / `identity.md` / `user.md` hierarchy + Ross Mike's "95% don't need this" outlier
- [[skills-architecture-progressive-disclosure]] — modular skills + progressive disclosure (load-name-then-instructions) + build-via-failure + skill chaining
- [[memory-and-context-rot]] — 6 levels of memory + Open Viking + Ben AI's OS Optimizer + the corpus's most-cited technical hurdle
- [[builder-orchestrator-executor-pattern]] — Mani Kanasani's 3-role framework + Kanban orchestration + observe-think-act loops + autopilot loops
- [[security-philosophies-and-sandboxing]] — conservative-access (Ross Mike) vs infrastructure-led (NemoClaw via Mani) — strongest disagreement axis
- [[off-the-shelf-vs-handbuilt-skills]] — the corpus's sharpest divergence (Ross Mike's anti-distribution stance vs the rest) — high-relevance for vault studying skill-distribution
- [[production-readiness-gaps]] — 5 areas the YouTube corpus doesn't address + 6 follow-up topics
- [[takeaways]] — 10 actionable rules consolidated

## Cross-links to autopilot-research siblings

- [[../claude-cowork/_index]] — **sister topic**: same architectural pattern, different product (Cowork = Anthropic's first-party variant); see [[overview]] for the side-by-side
- [[../claude-md-12-rules/_index]] — the `.md` behavioral-contract pattern that the instruction layer descends from
- [[../harness-engineering/_index]] — org-scale variant of the same builder-orchestrator-executor decomposition
- [[../10x-claude-code/_index]] — productivity-multiplier framing overlap (especially the Nick Saraev 4-hour course inclusion in this drain)
- [[../autonomous-loops-human-in-the-loop/_index]] — the observe-think-act / Kanban-driven loop pattern this corpus advocates
- [[../claude-code-clones/_index]] — OpenClaw is a load-bearing tool in this corpus; Mani Kanasani's content overlaps with the clones topic

## Cross-links to Storm Bear curated vault

- [[external|Storm Bear: agent-skills-standard (v76)]] — codifies the portable-Skill format that the corpus's "skills" pattern relies on
- [[external|Storm Bear: AutoGPT (v59)]] — pre-Anthropic AI-employee framing
- [[external|Storm Bear: cc-sdd (v61)]] — SDD-discipline-as-skill-architecture pattern relevant to the build-via-failure tactic
- [[external|Storm Bear: ECC (v78)]] — affaan-m's 232-skill operator system is the maximal expression of this corpus's vision

## Key cross-source observations

- **Ross Mike is the corpus's central outlier** — pushes back on ~every consensus position (heavy `.md` files / off-the-shelf skills / off-the-shelf security). The most useful counter-balance to the otherwise pro-elaboration tilt of the corpus.
- **Mani Kanasani's Builder-Orchestrator-Executor framework** is the strongest organizing taxonomy in the corpus — adopt with confidence
- **Progressive disclosure for skills** (Simon Scrapes + Ross Mike) is the highest-leverage token-cost optimization — universally applicable
- **Memory architecture is the most-cited technical hurdle** (N=2+ explicit calls); Simon Scrapes's 6-level taxonomy is the most-actionable framework
- **OpenClaw is positioned as a load-bearing orchestrator** by Mani Kanasani — note the Storm Bear v60 free-claude-code and the wider clones-corpus relevance
- **NemoClaw (NVIDIA)** is mentioned only by Mani Kanasani — infrastructure-level sandboxing is corpus-rare but cited as production-grade
- **Fireship's Open Viking inclusion** is mostly tangential — short video, broader open-source-tools listicle; weakest single source in the bundle

## Status

- **Compiled:** 2026-05-29
- **Stub articles:** 0
- **Gaps:** (none — initial compile)
- **Promotion candidate?** Tentative — this is the 2nd drain on the broader "personal AI OS" pattern (1st was claude-cowork). One more corroborating drain + a 2-cycle audit would qualify for promotion-to-Storm-Bear consideration.
