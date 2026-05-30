# Anthropic first-party positioning — official taxonomy + constraints + Skill/Plugin definitions

**THE CANONICAL ANCHOR for the claude-cowork topic.** Other articles in this topic should cite this article when they need first-party Anthropic confirmation of a claim previously sourced from creator-economy content.

## Source

- Raw: [`raw/2026-05-30-anthropic-cowork-first-party-docs-path4.md`](../../raw/2026-05-30-anthropic-cowork-first-party-docs-path4.md)
- NotebookLM: `def7ce93-5ef6-4af6-94af-504f2b288ca6`
- Ingest path: **Path 4** — `notebooklm notebook create + source add ×2` (manual, NOT yt-pipeline)
- 2 first-party Anthropic-domain URLs:
  - https://claude.com/docs/cowork/overview (canonical docs)
  - https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork (Help Center getting-started)

## Why this article exists

The original 2026-05-29 claude-cowork drain compiled 6 creator-economy YouTube videos into 9 articles. The 2026-05-30 follow-up drain (b05d3444 notebook) targeted "Anthropic Cowork official documentation" via yt-pipeline but yt-search rubric **does NOT surface first-party Anthropic content** — it returned 4 more creator videos. The first-party-docs gap remained until this Path 4 manual ingest of 2 actual Anthropic.com URLs.

This article closes **claude-cowork wiki surviving gap #1** as of 2026-05-30.

## Anthropic's official Cowork summary (verbatim core)

> "Claude Cowork is an agentic workspace integrated into the Claude Desktop app that enables the AI to perform complex, multi-step tasks autonomously."

Confirmed feature surface from first-party docs:
- **Direct local file access** without manual uploads
- **Code execution in a secure environment**
- **Parallel workstreams** to produce professional deliverables (spreadsheets, presentations)
- **Paid subscribers only**, macOS and Windows
- **Scheduled recurring jobs**
- **Mobile remote-task assignment** (Pro/Max users only; requires desktop active)
- **Projects + Plugins** for customization
- **Safety protocols** — explicit permissions for file deletions, different levels of oversight

## Cowork-vs-Code-vs-Chat — OFFICIAL TAXONOMY (closes prior 3-way speaker disagreement)

The original 2026-05-29 corpus had **3 conflicting speaker taxonomies** ([[overview]] §"three-mode taxonomy"). Anthropic's first-party position:

| Feature | Regular Claude Chat | Claude Cowork | Claude Code |
|---|---|---|---|
| Primary Use | Simpler tasks | Knowledge work beyond coding | Coding |
| Interaction | Sequential prompts | Agentic, multi-step tasks | Agentic |
| Interface | Web/Desktop/Mobile | Claude Desktop app | Terminal (implied) |
| File Access | Manual uploads only | Direct local file access | Not explicitly detailed |
| Scheduling | Not supported | Supports recurring tasks | Not explicitly detailed |

**Anthropic's framing:** Cowork "brings Claude Code's agentic capabilities to Claude Desktop for **knowledge work beyond coding**." Cowork and Code share the same agentic architecture; Cowork removes the terminal-CLI requirement.

This validates **Jack Roberts's "rebrand of earlier Claude Code packaging"** framing (from [[overview]]) and **Bart Slodyczka's professional-role distinction** (Code = developer, Cowork = "employee"). Tech With Tim's "user skill level" framing is consistent but less load-bearing.

**Cowork explicitly costs more usage allocation than chat** — Anthropic states this directly. Composes with [[token-and-cost-management]] guidance.

## Scheduling: app-must-be-open is OFFICIAL ANTHROPIC POSITION (not workaround)

[[scheduling-and-the-app-open-constraint]] was correct. Anthropic's docs state explicitly:

> **"Scheduled tasks only run while your computer is awake and the Claude Desktop app is open."**

Plus four corroborating first-party statements:

> "The Claude Desktop app must remain open and your computer must be awake for Claude to work on tasks. If you close the app or your computer goes to sleep, active tasks will stop."

> "The Claude Desktop app must remain open while Claude is working. If you close the app, your session will end."

> "Ensure the Claude Desktop app was open throughout the entire task. If the app was closed or your computer went to sleep, the session may have ended." [troubleshooting]

> Pro and Max users can message Claude from a mobile device "while your desktop stays active."

**Implication:** The N=4-of-6 creator consensus (Tech With Tim + Bart Slodyczka + Stefan Wirth + Kenny Liao) was correct. Kenny Liao's cron-plugin and Jack Roberts's Railway are **real workarounds for an officially-documented Anthropic limitation**, not fixes for an undocumented bug.

This permanently settles the constraint question. Future operators reading [[scheduling-and-the-app-open-constraint]] should treat it as gospel, not heuristic.

## Skills + Plugins — OFFICIAL ANTHROPIC TWO-TIER HIERARCHY

This is the most-load-bearing first-party clarification. The [[skills-vs-plugins-hierarchy]] article documented the corpus-first Prince+Wilson N=2 articulation. **Anthropic's first-party docs confirm at N=3 (with Anthropic as the canonical authority).**

### Anthropic's definitions

- **Skills:** "Teach Claude reusable workflows with custom instructions."
- **Plugins:** "Shareable packages" that "bundle skills, connectors, and more" — used to "customize how Claude works for your role, team, and company in Cowork."

### Anthropic's distinction

| Tier | Composition | Distribution intent |
|---|---|---|
| Skills | Single workflow | Operator-scope; not characterized as "shareable" |
| Plugins | **Bundle of Skills + Connectors + Sub-agents** | "Shareable packages" — designed for distribution across teams/org |

### What this adds vs prior corpus

**Plugins can bundle sub-agents** — this is a NEW architectural detail not in any prior corpus. Prince+Wilson described Plugins as bundling Skills + Connectors; Anthropic explicitly adds **sub-agents** to the bundle. This makes Plugins materially more powerful than what creator content described.

**Reconciliation of the Camp A vs Camp B distribution debate** (from sister [[../ai-operating-system/off-the-shelf-vs-handbuilt-skills]]) is now first-party-confirmed:
- **Skills should be operator-authored** (Anthropic doesn't characterize them as shareable; Ross Mike's build-your-own posture aligns)
- **Plugins are explicitly shareable** (Anthropic says so directly; Camp A's marketplace posture aligns at the Plugin level)

## What this article does NOT cover (carry-forward gaps)

1. **API/SDK programmatic access** — Cowork API docs aren't in this 2-URL bundle. Separate Path 3 ingest needed on `platform.claude.com/docs/...`.
2. **`setup-cowork` Anthropic-skill content** — that's a vault skill registry surface, not claude.com docs. Path 6 custom scraper required.
3. **Specific connector inventory** — Anthropic publishes a separate connectors page worth its own ingest.
4. **Pricing tiers + usage allocation specifics** — mentioned in the docs but not enumerated. Anthropic pricing page would close this.

These are NEW carry-forward gaps surfaced BY closing the first-party-docs gap. Net the topic is healthier: original gap closed, finer-grained gaps identified.

## Implications for prior wiki articles in this topic

The following articles now have first-party confirmation for their main claims:

| Article | What this anchor confirms |
|---|---|
| [[overview]] | Cowork = agentic workspace in Claude Desktop; "knowledge work beyond coding" framing is Anthropic's own |
| [[scheduling-and-the-app-open-constraint]] | The constraint is officially documented, not a workaround for a bug |
| [[skills-to-plugins-pipeline]] | Skill-vs-Plugin scoping is confirmed two-tier; codify-after-success workflow produces Skills that may then bundle into Plugins |
| [[skills-vs-plugins-hierarchy]] | Two-tier hierarchy is officially Anthropic's taxonomy at N=3 with first-party verification |
| [[mcp-connectors-landscape]] | Connectors are confirmed as a primitive bundlable inside Plugins |

[[contextual-engineering]] / [[sandboxing-and-workspace-structure]] / [[token-and-cost-management]] / [[production-readiness-gaps]] / [[takeaways]] don't directly conflict with first-party positioning — they're operator-tactical content where creators contribute legitimate IP.

## Key Takeaways

- **The first-party-docs gap is CLOSED.** Anthropic has canonical Cowork docs at `claude.com/docs/cowork/overview` + Help Center `get-started` article.
- **App-must-be-open is OFFICIAL** — not a workaround for a bug. Operator must plan accordingly (or use Kenny Liao's cron-plugin / Jack Roberts's Railway / vault `/schedule`).
- **Skills vs Plugins two-tier hierarchy is OFFICIAL** — confirmed at N=3 with Anthropic as authoritative source. Plugins include sub-agents (new detail).
- **Cowork explicitly costs more usage** than chat — first-party confirmation of [[token-and-cost-management]] guidance.
- **Cowork = "knowledge work beyond coding"** is Anthropic's own framing — settles the corpus's 3-way taxonomy debate.

## Related

- [[_index]] — topic entry; status updated post this ingest
- [[overview]] — taxonomy now first-party-confirmed
- [[scheduling-and-the-app-open-constraint]] — constraint now first-party-confirmed
- [[skills-vs-plugins-hierarchy]] — two-tier hierarchy now first-party-confirmed at N=3
- [[skills-to-plugins-pipeline]] — codify-after-success workflow consistent with Anthropic framing
- [[../ai-operating-system/off-the-shelf-vs-handbuilt-skills]] — Camp A vs Camp B debate now reconciled at first-party level
