# open-design

> **Topic index.** **Open Design** ([`nexu-io/open-design`](https://github.com/nexu-io/open-design)) — a **local-first, open-source alternative to Anthropic's Claude Design**. Its one load-bearing idea: **it ships no LLM.** Instead it *drives whatever coding-agent CLI is already on your PATH* (Claude Code, Codex, Cursor, Gemini, Copilot, OpenCode, …) as the design engine — **"we don't ship an agent, yours is good enough."** Design intent lives in portable **`DESIGN.md`** systems + composable **`SKILL.md`** skills, and everything runs on a local `127.0.0.1` daemon. Generates web/desktop/mobile prototypes, dashboards, decks, images, video (HyperFrames) → HTML/PDF/PPTX/MP4.
>
> **Entry point:** [QOqWZzecjuY](https://www.youtube.com/watch?v=QOqWZzecjuY) — **"Open Design in 20 Minutes (Full Setup + Demo)"**, a **22:04 first-impressions install+demo** on the **CodingMenace** channel (Dennis; uploaded **2026-05-05**, ~19.4K views). A *third-party* creator walkthrough, **not** a first-party source. Full auto-caption transcript read (`raw/2026-07-01-open-design.md`).
>
> **⚠️ Claude Design is real (and load-bearing).** The whole "alternative to" framing rests on [**Claude Design**](https://www.anthropic.com/news/claude-design-anthropic-labs) being a genuine product — **verified**: an **Anthropic Labs** product launched **2026-04-17** (research preview, **Opus 4.7**, cloud-only at claude.ai/design, **Pro/Max/Team/Enterprise** subscription-gated). Open Design was created **2026-04-28** — **11 days later.** See [[open-design/open-design-vs-claude-design]].
>
> **Originals (deep-dived against primary sources, gh-api-verified):** [`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design) (design-philosophy compass, 20.5K★) · [`OpenCoworkAI/open-codesign`](https://github.com/OpenCoworkAI/open-codesign) (the *actual* "first" OSS alternative, 7K★) · [`multica-ai/multica`](https://github.com/multica-ai/multica) (the daemon+adapter architecture, 38.6K★) · [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) + [`lewislulu/html-ppt-skill`](https://github.com/lewislulu/html-ppt-skill) (deck skills) · [`VoltAgent/awesome-design-md`](https://github.com/VoltAgent/awesome-design-md) (the `DESIGN.md` schema, 94.7K★) · [`bergside/awesome-design-skills`](https://github.com/bergside/awesome-design-skills) · [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes) (HTML→MP4). Full lineage: [[open-design/the-originals]].
>
> **Verification:** Workflow `wf_4a91a8b2-2bb` (**13 agents**: 8 original/main deep-dives + 3 adversarial skeptics + 1 hireui-application + synthesis critic; ~633K tokens, 219 tool calls) + operator `gh api` / `yt-dlp` / WebFetch ground-checks. **The synthesis critic over-flagged** "Claude Design existence unverified" as its #1 concern — **overridden** by a direct WebFetch of the Anthropic announcement (+ TechCrunch/VentureBeat). Corrections (AGPL guizang-ppt, NOASSERTION multica, opt-in-PostHog-vs-"no telemetry", unconfirmed SSRF, plugin-count inflation) captured in [[open-design/source-provenance]].

---

## Articles

- [[open-design/overview]] — who's who (CodingMenace demo), what Open Design *is*, the "we don't ship an agent" thesis, the six "load-bearing ideas," and where it sits vs the closed Claude Design it clones.
- [[open-design/architecture-and-byoa]] — **the mechanism.** The local Node-24/Express/SQLite **daemon**, **PATH-scan agent detection** + the `detect()/capabilities()/run()` **adapter contract**, the **BYOK proxy**, the **three-layer model** (plugins = workflows · skills = taste · design-systems = tokens), the `SKILL.md` `od:` frontmatter, and the security posture (loopback-default, credentials `0600`).
- [[open-design/design-md-as-source-of-truth]] — **the load-bearing pattern for *your* work.** `DESIGN.md` as a portable, version-controlled brand contract (the 9-section schema), why "design systems are portable markdown," and the direct fix for hireui's drifted tokens — *stealable without adopting the tool*.
- [[open-design/features-and-workflow]] — the feature surface (wireframe vs hi-fi prototypes, decks, images, video, HyperFrames, export formats) and the **exact demo workflow** from the video (import a Claude Design `.zip` → prompt → clarifying questions → to-do list → `.html`/JSX artifacts → iterate v2/v3).
- [[open-design/install-and-setup]] — native desktop app vs from-source (**pnpm**, not the video's npm), `od mcp install <agent>`, first-run PATH-scan + media providers, and the **safety precautions** before you `install`.
- [[open-design/huashu-design-deep-dive]] — **the design-philosophy original**, deep-dived: the **Brand Asset Protocol** (logo > product > UI > color), the **anti-AI-slop checklist**, the 40-style library, the **Design Direction Advisor**, and the **Junior-Designer workflow** — the piece that composes with your Taste Skill.
- [[open-design/the-originals]] — provenance of every credited upstream ("open source shoulders"), who originated what, with the license + name corrections.
- [[open-design/open-design-vs-claude-design]] — open vs closed, **bring-your-own-agent** vs cloud-locked-to-Opus, feature/parity comparison, and the honest "when to use which."
- [[open-design/caveats-and-safety]] — **the critic layer.** License landmines (**AGPL-3.0** guizang-ppt, **NOASSERTION** multica), the **"no telemetry" vs opt-in-PostHog** nuance, the **unconfirmed SSRF** claim, plugin-count inflation, star-velocity assessment (**organic**, with a paid-Fellows accelerant), and maturity/pilot risk.
- [[open-design/source-provenance]] — the verified-vs-corrected ledger, the critic-over-flag override, and the **don't-re-fabricate** list.

## Pilot methods (how to apply this to your flow)

A ranked menu of **24 methods + a skip-list + a critic's reframe** lives in **`output/(C) 2026-07-01-open-design-pilot-methods.md`**, across five angles: **hireui Goal #2** (pilot Open Design on the Candidate Detail screen driven by your own Claude Code CLI; the `DESIGN.md`-fixes-token-drift play; a comparison pilot vs your Figma+Taste flow), **steal-the-pattern-not-the-tool** (`DESIGN.md` single-source-of-truth + huashu's anti-slop checklist without installing anything), **decks for Scrum coaching** (guizang/html-ppt standalone), the **vault** (portable-skill lessons), and **personal Claude Code** (BYOA/harness lessons).

## Cross-topic links

- [[../ai-web-design-workflow/_index]] — **the closest sibling.** Your **Taste Skill** (leonxlnx, anti-slop gate) lives there; huashu-design's anti-AI-slop philosophy *composes* with it, and Open Design is the tool-level counterpart to that topic's redesign workflow.
- [[../claude-code-clones/_index]] — Open Design is to **Claude Design** what those clones are to **Claude Code**: an open-source re-implementation of a closed Anthropic product.
- [[../claude-skills/_index]] · [[../claude-code-skills-stack/_index]] — the `SKILL.md` convention Open Design adopts verbatim; "skills are files, not plugins."
- [[../pocock-agentic-workflow/_index]] · [[../harness-engineering/_index]] — **harness-over-model** in a design tool: "we don't ship an agent, yours is good enough" is BYOA = bring-your-own-harness.
- [[../cowork-third-party-inference/_index]] — same **BYOK / model-agnostic** posture (drive any provider via an OpenAI-compatible proxy).
- [[../multi-agent-orchestration/_index]] — multica (Open Design's architectural upstream) is a general agent-orchestration daemon.
- [[../how-we-claude-code/_index]] — HTML-artifacts-as-design-handoff; Claude Design itself reads codebase+Figma and hands off to Claude Code.
- [[../claude-api-cost-optimization/_index]] — BYOK means *your* token spend; model choice per task.

## Key Takeaways

- **"We don't ship an agent — yours is good enough."** Open Design's whole thesis is **bring-your-own-agent (BYOA)**: a local daemon PATH-scans for the coding-agent CLIs you already have and drives them as the design engine. No vendor model lock-in; swap Claude Code for Codex/Cursor without changing your design system.
- **Design becomes files, not a canvas.** Brand intent = a portable **`DESIGN.md`** (9-section markdown contract); workflows = **`SKILL.md`** skills; both are version-controllable and agent-readable. This is the part most worth stealing even if you never install the app.
- **It's a genuine open clone of a genuine closed product.** Claude Design (Anthropic Labs, 2026-04-17, Opus 4.7, cloud+subscription) is real; Open Design (2026-04-28, Apache-2.0) is the local-first, model-agnostic answer — **73.5K★ in ~9 weeks** (assessed organic, with a paid-`$1,000/MR`-Fellows accelerant).
- **The originals are a whole ecosystem**, not one repo: a design-philosophy compass (huashu-design), a predecessor (open-codesign), a daemon architecture (multica), deck skills (guizang/html-ppt), and the `DESIGN.md` schema (VoltAgent). Open Design is the *orchestrator* that composes them.
- **Handle with the usual caution:** an AGPL-3.0 bundled skill, an unlicensed (NOASSERTION) architectural upstream, a "no telemetry" claim that's really opt-in-PostHog, and an SSRF claim not confirmed in the code one skeptic read. Sandbox-pilot it; don't point it at production data on day one.
