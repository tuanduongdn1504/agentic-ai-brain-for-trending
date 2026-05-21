# Anthropic large-codebases anchor — first-party authoritative 7-component harness

> **Primary source:** [How Claude Code Works in Large Codebases: Best Practices and Where to Start](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) — Anthropic, 2026-05-14
> **Walkthrough source:** [Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)](https://www.youtube.com/watch?v=efRIrLXoOVA) — Cole Medin, 2026-05-21 (28:10, ~2.1K views at fetch)
> **Worked-example source:** [coleam00/helpline](https://github.com/coleam00/helpline) — see sibling article [[helpline-worked-example]]
> **Raw:** `raw/2026-05-14-anthropic-large-codebases-blog.md` + `raw/2026-05-21-cole-medin-anthropic-masterclass-transcript.md` + `raw/2026-05-19-coleam00-helpline-readme.md`
> **Compiled:** 2026-05-21
> **Status:** **AUTHORITATIVE anchor** — first-party Anthropic guidance. Promotes existing community / practitioner anchors ([[anchor-bundle-overview|Lopopolo]], [[personal-repo-overview|Tù Bà Khuỳm]], [[tejas-kumar-anchor|Tejas Kumar]]) to derivative status; their definitions of harness now should be triangulated against Anthropic's official 7-component decomposition.

This anchor is **the corpus-first first-party authoritative source** on harness engineering. Until 2026-05-14, every harness-engineering source in the autopilot corpus was either community-practitioner (Tejas, Tù Bà Khuỳm, howznguyen) or vendor-competitor (Lopopolo at OpenAI, LangChain Deep Agents). Anthropic — who SHIPS Claude Code itself — has now published an official 7-component decomposition of the harness extension layer, with explicit configuration patterns for enterprise rollout.

Cole Medin's video (uploaded **2026-05-21**, ONE WEEK after the blog) walks through all 7 components against a companion codebase (`coleam00/helpline`) where every component is implemented and validated. The blog is concept-level; the video is walkthrough-level; the repo is implementation-level. Reading all three together is the cleanest possible path into harness engineering — and corpus-first as a complete vendor-published teaching set.

---

## The 7-component decomposition (authoritative)

Anthropic frames the harness as **the ecosystem around the model that determines performance more than the model alone**. Cole Medin's term — *"AI Layer"* `[03:24]` — is more descriptive than "harness" but refers to the same construct. The 7 components, in approximate session-use frequency (per the blog's visual indicator described by Cole at `[04:38]`):

| # | Component | Frequency | What it is | Helpline implementation |
|---|---|---|---|---|
| 1 | **CLAUDE.md hierarchy** | **continuous** — foundation | Context files Claude reads automatically. Root = big picture; subdirectory = local conventions. **Walks up directory tree loading every file** when initialized in a subdirectory. | lean root `CLAUDE.md` + one per service/package |
| 2 | **Hooks** | sporadic | Scripts at lifecycle events. **Most valuable use is continuous improvement**, not just defensive blocking: reflection hooks propose `CLAUDE.md` updates; start hooks load dynamic context. | `SessionStart` orientation hook + self-improving `Stop` hook that runs separate Claude in headless mode to review session diff and propose `CLAUDE.md` edits |
| 3 | **Skills** | sporadic / on-demand | Packaged instructions for specific task types, **loaded on-demand**, scoped via `paths:` glob to specific code paths to avoid universal-context bloat. | `billing-money-rules`, `api-add-route`, `scoped-tests` — all glob-scoped with progressive disclosure into `references/` |
| 4 | **Plugins** | install-time | Bundled skills+hooks+MCP distributed as installable packages. **Make AI Layer portable** to other repos via `/plugin marketplace add` + `/plugin install`. | `helpline-ai-layer` plugin at `tooling/helpline-ai-layer/` |
| 5 | **Language Server Protocol (LSP)** | sporadic | Symbol-level navigation. **Prevents pattern-matching errors on identically named functions.** Grep returns thousands; LSP returns relevant symbols only. | pyright + `pyright-langserver` for symbol-level Python navigation |
| 6 | **MCP servers** | sporadic | Connections to internal tools, data sources, APIs Claude cannot otherwise reach. Sophisticated teams expose structured search as a tool Claude calls directly. | `codebase-search` MCP — AST-based `where_is` / `find_references` / `outline` |
| 7 | **Subagents** | session-level | Isolated Claude instances with separate context windows. **Split exploration from editing** — read-only subagent maps subsystem while main agent edits with full context. | read-only `explorer` subagent (no write tools) |

### The visual frequency hierarchy (Anthropic blog, described in Cole at `[04:38]`)

The blog provides a visual showing each component's usage frequency across a session:

- **CLAUDE.md** = **continuous** (foundation; dictates behavior the entire time)
- **Hooks / Skills / LSP / MCP / Subagents** = **sporadic** (called when relevant)
- **Plugins** = **install-time** (one-shot setup distribution)

Cole's commentary on this hierarchy `[04:46]–[05:04]`:

> *"Most of them are sporadic like your hooks and skills and the LSP for navigation. But your global rules as your foundation, it is dictating the behavior of cloud code the entire time. So you better spend a good amount of time strategizing around your context curation here."*

This is corpus-first as an **explicit frequency-based hierarchy** of harness primitives. Tejas Kumar's [[tejas-kumar-anchor|5-component decomposition]] enumerated primitives at the same abstraction level but did not weight them by session frequency. Anthropic's framing makes the case that **investment in CLAUDE.md pays back more than any other component** — and is consistent with the empirical observations from individual-scale practice ([[personal-repo-patterns|CLAUDE.md is the central technique]]).

---

## The 3 configuration patterns

Anthropic enumerates exactly 3 patterns that "successful deployments" share. These are the load-bearing scale-out advice — applicable from mid-sized (helpline scale: ~5 services, ~10K LOC) to multi-million-line monorepos.

### Pattern 1 — Make the codebase navigable at scale

Six concrete sub-rules, each derived from a different scale-failure mode:

| Sub-rule | Failure mode prevented |
|---|---|
| **Keep CLAUDE.md files lean and layered** | Multi-thousand-line CLAUDE.md → context overwhelm → degraded model performance |
| **Initialize in subdirectories, not repo root** | Wrong working scope → Claude tries to edit across unrelated services |
| **Scope test and lint commands per subdirectory** | Full test suite per service change → timeouts |
| **Exclude generated files and build artifacts** | Noise in agentic-search results → wasted token budget reading generated code |
| **Build codebase maps for unconventional structures** | Non-standard directory layout → Claude cannot navigate by convention |
| **Run LSP servers for symbol-based searching** | Grep returns thousands → token-inefficient + ambiguous-symbol pattern-matching errors |

Cole's most-emphasized rule (around `[05:08]–[05:24]`): keep CLAUDE.md lean. He explicitly cites studies showing that thousand-line CLAUDE.md files **hurt** coding agent performance. The "lean" injunction is empirically grounded, not stylistic.

The **subdirectory-initialization rule** is corpus-first as an explicit anti-pattern correction. Cole demos `[07:14]–[07:53]`: VS Code right-click → copy path → `cd <path>` → `claude` — initializing Claude Code with that directory as the working scope. The walks-up-the-tree CLAUDE.md loading means **no context is lost** from the root, but the agent's natural working scope is bounded to the relevant subsystem.

### Pattern 2 — Actively maintain CLAUDE.md files

> *"As models evolve, instructions written for current models may constrain future ones. A rule telling Claude to break refactors into single-file changes might prevent newer models from making beneficial cross-file edits. Teams should review configurations every three to six months, especially after major model releases."*

This is **the first explicit corpus mention of harness-decay as a maintenance concern**. Tejas Kumar's anchor mentioned 2027 dynamic-on-the-fly harnesses but did not address mid-life maintenance of static harnesses. Anthropic's framing positions the harness as a **continuously-evolving asset** with model-version-coupled refresh cycle.

Cole's helpline implementation makes this **operationally tractable** via the Stop hook `[11:14]–[15:22]`. The Stop hook:
1. Runs at end of every session
2. Spawns separate Claude in **headless mode** to review the session's diff
3. Reads existing CLAUDE.md files (root + relevant subdirectories)
4. Proposes concrete edits if conventions drifted from current behavior
5. Outputs markdown review document for human to act on

Cole's demo at `[13:46]–[15:01]`: makes a small code change, Stop hook fires, separate Claude session reviews and outputs review markdown saying *"no changes needed — adding a trial enum value follows the existing model-only convention."* Then Cole makes a bigger change requiring CLAUDE.md update; Stop hook correctly recommends updating bullet 2 in billing service CLAUDE.md.

This converges with [[external|agent-development-lifecycle/langchain-interrupt-26-anchor|LangSmith Engine]]'s ambient-proactive meta-agent pattern — but at a much lighter weight (no SmithDB, no proprietary infrastructure, just a hook running Claude in headless mode).

### Pattern 3 — Assign ownership for Claude Code management

The blog's **strongest organizational claim**: technical configuration alone doesn't drive adoption; successful rollouts had dedicated infrastructure investment **before broad access**.

Three sub-recommendations:

| Recommendation | Implementation pattern |
|---|---|
| **Establish a dedicated role** | "Agent manager" — emerging hybrid PM/engineer function; OR developer experience / developer productivity team ownership; minimum viable = one DRI with authority on settings + plugin marketplace + CLAUDE.md conventions |
| **Prevent fragmentation** | Without centralization, knowledge stays tribal and adoption plateaus. Centralized owner assembles + evangelizes conventions, preventing thousands of engineers from independently rebuilding the same solutions. |
| **Address governance early** | Regulated industries: cross-functional working group (engineering + infosec + governance); define requirements together; start with approved skills + required code review + limited initial access; expand as confidence builds. |

Cole at `[25:55]–[27:36]` reinforces this from his consulting experience:

> *"Have a couple of people that build out the rules and skills and the LSP and the MCP servers, the whole AI Layer for the organization and then roll it out to people over time. The power of this is you get to create something that's really foundational for everyone to adopt together and then people can get more consistent results with Cloud Code or whatever coding agent faster so that they're not disappointed when they first use the tool."*

**Corpus-first observation:** this is the **first explicit prescription for an "agent manager" role**. Maps loosely to [[external|agent-development-lifecycle/langchain-interrupt-26-anchor|Managed Deep Agents]]' implicit role (someone owns the LangSmith deployment configuration) but Anthropic names it explicitly.

---

## The "quiet investment period" model

Cole's framing of the rollout pattern `[26:30]–[27:24]`:

1. **Quiet investment period** — a small team builds the AI Layer for the organization
2. **Foundation-first deployment** — roll out the AI Layer to people once it's substantively built
3. **Avoid disappointed-first-use** — operators should NOT encounter Claude Code without an AI Layer in place
4. **Avoid AI-Layer fragmentation** — prevent each engineer from independently evolving their own setup

This converges with multiple corpus findings:
- [[external|harness-engineering/anchor-bundle-overview|Lopopolo's Symphony architecture]] is the OpenAI in-house equivalent
- [[external|agent-development-lifecycle/langchain-interrupt-26-anchor|LangChain Managed Deep Agents]] is the platform-as-a-service equivalent
- [[personal-repo-router-multimodel|howznguyen's router+sub-agent pattern]] is the individual-scale "I am my own agent manager" version

All four are responses to the same root concern: **the harness needs a designated owner, or it decays**. The shape of the owner varies with scale — full team at enterprise, platform vendor at SaaS-customer scale, individual developer at personal scale — but the role is invariant.

---

## How this anchor relates to prior corpus anchors

| Prior anchor | Relationship to Anthropic anchor |
|---|---|
| [[anchor-bundle-overview\|Lopopolo (org-scale OpenAI Frontier+Symphony)]] | **Independent corroboration** of the harness-matters-as-much-as-model thesis from a competing vendor (OpenAI). Lopopolo's [[core-claims|8 falsifiable claims]] (1B-token-day economics, post-merge review, etc.) operate at a scale and product-stage Anthropic doesn't address in this blog. **Complementary, not contradicted.** |
| [[personal-repo-overview\|Tù Bà Khuỳm + 6 YouTube (individual-scale)]] | Individual-scale operating point of the same authoritative framework. The individual-scale anchor IDENTIFIED CLAUDE.md as load-bearing 2 months before Anthropic officially confirmed it. **Empirical-practice-precedes-vendor-doc**. |
| [[tejas-kumar-anchor\|Tejas Kumar (definitional, IBM)]] | Tejas's 5-component decomposition (tool registry / model / context / guardrails / loop / verify) operates at a **lower abstraction level** — the agent-runtime architecture. Anthropic's 7-component operates at the **extension-surface level** within Claude Code specifically. **Both correct, different abstraction layers.** Worth a future article explicitly mapping them. |
| [[personal-repo-router-multimodel\|howznguyen (router-multimodel)]] | Operates within Claude Code via `~/.claude/settings.json` + 3-slot config — orthogonal to the 7 components Anthropic enumerates here. Adds **cross-vendor delegation as an 8th-component-candidate** Anthropic blog doesn't mention. |
| [[external\|agent-development-lifecycle/langchain-interrupt-26-anchor\|LangChain Deep Agents]] | Competing platform's harness equivalent. Where Anthropic frames the harness as a **codebase concern** (settings.json, CLAUDE.md hierarchy at the repo level), LangChain Deep Agents frames it as a **platform concern** (LangSmith Deployments, Context Hub, Managed Deep Agents at the SaaS level). Two valid postures; same primitives at different abstraction. |

### Where Anthropic blog is SILENT (and might warrant future ingest)

- **No mention of cross-vendor delegation** (howznguyen pattern) — Anthropic naturally markets the Anthropic harness only
- **No mention of dynamic-on-the-fly harness generation** (Tejas's 2027 prediction) — Anthropic stays operational, not predictive
- **No mention of harness for OPEN-source models** behind Anthropic's API — Anthropic's "model" slot is implicitly Claude
- **No specific operating-point numbers** (lines of code threshold, team size threshold) for when each pattern starts paying back — left as judgment

---

## Open questions

1. **What's the lower-bound codebase size at which the AI Layer pays back?** Anthropic asserts the pattern works at multi-million-line scale but doesn't give a lower threshold. Helpline (~10K LOC, 5 services) demonstrates that smaller codebases work too; how small is too small for full 7-component investment?
2. **Will the "agent manager" role consolidate as an actual industry job title?** First-party Anthropic naming gives it weight; corpus tracking should watch for job postings, conference talks, or org-chart references over the next 6-12 months.
3. **How does helpline's `helpline-ai-layer` plugin compare to other plugin-based-harness-distribution patterns (e.g., [[external|claudekit/_index|ClaudeKit]], [[external|harness-engineering/personal-repo-router-multimodel|9Router-based setups]])?** All three are different routes to "make the harness portable" — direct comparison article candidate.
4. **What's the actual decay rate of CLAUDE.md without active maintenance?** Anthropic's 3-6 month review cadence is asserted without quantitative backing. A longitudinal study (e.g., diff `CLAUDE.md` across 6-month windows in active projects) would quantify.
5. **Does Anthropic plan first-party tooling for active CLAUDE.md maintenance** (the way LangSmith Engine does it for traces)? Cole's Stop hook implementation works but is operator-built. Anthropic could ship this as a built-in feature.
6. **What's the operational cost of running Stop hook on every session?** Each Stop fires a headless Claude session to review the diff — at scale (multi-dev, multi-session-per-day) this is non-trivial. Cost-benefit study warranted.

---

## Promotion-to-Storm-Bear-curated-wiki candidate

This anchor is a strong Storm Bear Pattern Library promotion candidate at next mini-audit (Storm Bear v66 cadence). Rationale:

- **First-party authoritative source** of the topic
- **Multi-piece teaching set** (blog + video + repo) — corpus-first format
- **7-component decomposition** is now the reference vocabulary; future autopilot ingests should cite this as baseline
- **Explicit "agent manager" role naming** is an industry-vocabulary contribution worth tracking

When 2-3 more vendor-published authoritative-anchor sources land (similar OpenAI/Google guidance), promotion to full Pattern Library is warranted. See [[external|harness-engineering/research-roadmap]] for tracking.

---

## Cross-links

- [[helpline-worked-example]] — sibling article: detailed walkthrough of how coleam00/helpline implements each of the 7 components
- [[_index|harness-engineering index]]
- [[anchor-bundle-overview]] — Lopopolo org-scale anchor (competing vendor's view)
- [[personal-repo-overview]] — Tù Bà Khuỳm individual-scale anchor (operator's view)
- [[tejas-kumar-anchor]] — Tejas Kumar definitional anchor (architectural view)
- [[personal-repo-router-multimodel]] — howznguyen router+multimodel pattern (orthogonal extension)
- [[terminology]] — where "harness", "AI Layer", "agent manager" definitions should consolidate
- [[research-roadmap]] — Storm Bear Pattern Library promotion candidate noted above
- [[external|agent-development-lifecycle/langchain-interrupt-26-anchor]] — LangChain's equivalent platform-level harness story
- [[external|claudekit/_index]] — ClaudeKit as plugin-based portable-harness alternative
- [[external|claude-md-12-rules/_index]] — Mnilax 12-rule template now operates within Anthropic's officially-blessed CLAUDE.md hierarchy framework
- [[external|claude-code-hooks/_index]] — Anthropic's "Hooks" component aligns with this topic's prior coverage
