# The originals — "open source shoulders" (who originated what)

## Source

Open Design's README *"References & lineage"* table, each entry deep-dived against its primary GitHub repo via Workflow `wf_4a91a8b2-2bb` + operator `gh api` ground-checks (2026-07-01). Corrections flagged ⚠️. huashu-design gets its own article ([[open-design/huashu-design-deep-dive]]); the `DESIGN.md` schema gets [[open-design/design-md-as-source-of-truth]].

## Facts table (gh api, 2026-07-01)

| Repo | ★ | License | Lang | Created | Role in Open Design |
|---|---|---|---|---|---|
| [`nexu-io/open-design`](https://github.com/nexu-io/open-design) | 73,468 | Apache-2.0 | TS | 2026-04-28 | **the subject** (v0.12.0) |
| [Claude Design](https://www.anthropic.com/news/claude-design-anthropic-labs) | — | closed | — | 2026-04-17 | the product it's an alternative to |
| [`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design) | 20,457 | MIT | HTML | 2026-04-19 | design-philosophy compass |
| [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) | 19,554 | **AGPL-3.0** ⚠️ | HTML | 2026-04-23 | default deck skill (bundled) |
| [`lewislulu/html-ppt-skill`](https://github.com/lewislulu/html-ppt-skill) | 6,713 | MIT | HTML | 2026-04-15 | HTML PPT Studio deck family |
| [`OpenCoworkAI/open-codesign`](https://github.com/OpenCoworkAI/open-codesign) | 7,023 | MIT | TS | 2026-04-18 | the *first* OSS alternative; UX North Star |
| [`multica-ai/multica`](https://github.com/multica-ai/multica) | 38,621 | **NOASSERTION** ⚠️ | Go | 2026-01-13 | daemon + adapter architecture |
| [`VoltAgent/awesome-design-md`](https://github.com/VoltAgent/awesome-design-md) | 94,742 | MIT | — | 2026-03-31 | the `DESIGN.md` 9-section schema |
| [`bergside/awesome-design-skills`](https://github.com/bergside/awesome-design-skills) | 1,482 | MIT | — | 2026-03-09 | a batch of design skills |
| [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes) | 32,398 | Apache-2.0 | TS | 2026-03-10 | HTML→MP4 motion engine |

## `OpenCoworkAI/open-codesign` — the *actual* "first" (and the UX North Star)

- Created **2026-04-18 — 10 days *before* open-design** (v0.1.0 on 2026-04-20, 11 days before open-design's v0.1.0). This is why open-design's README calls it *"the first open-source Claude Design alternative,"* and why the "first" title belongs to it, **not** open-design.
- **MIT**, TypeScript, **7,023★**, latest **v0.2.1** (2026-05-23). Multi-model (Claude, GPT, Gemini, Kimi, GLM, Ollama) with one-click ChatGPT/Codex-subscription import; **added `DESIGN.md` support later (v0.2.0)**.
- Open Design borrows its **UX patterns**: the streaming-artifact loop, the sandboxed iframe, the live agent panel.
- **The lighter sibling:** open-design is **10.5× more starred** and far broader (video, HyperFrames, 15+ agents, 440+ plugins); open-codesign is the slim BYOK client. For a low-friction pilot, open-codesign is the smaller surface. → [[open-design/open-design-vs-claude-design]]

## `multica-ai/multica` — the daemon architecture (video's "Kami")

- **38,621★**, **Go**, created **2026-01-13** (6 weeks before open-design — the oldest upstream here). ⚠️ **License = NOASSERTION** — GitHub detects no recognized OSS license, so reuse terms are unclear; treat as *look, don't fork* until clarified.
- A **general** "managed agents platform — turn coding agents into real teammates," **not** design-specific. Open Design applies its pattern to the design vertical: **PATH-scan agent detection**, a **local daemon as the only privileged process**, workspace isolation, WebSocket streaming.
- ⚠️ The architectural "debt" is *credited*, not code-audited — open-design may reimplement rather than import multica. Cross-ref [[../multi-agent-orchestration/_index]].

## `op7418/guizang-ppt-skill` + `lewislulu/html-ppt-skill` — the deck skills

- **guizang-ppt-skill** (author 花园/@op7418): the **default deck skill**, bundled verbatim under `design-templates/guizang-ppt/`. Magazine-style (editorial) + Swiss-International layouts — the README cites "10 editorial layouts + 22 Swiss templates", social covers, a WebGL/low-power presentation runtime that "degrades gracefully." **19,554★.**
  - ⚠️ **License correction:** the upstream repo is **AGPL-3.0** (confirmed via `gh api` + its LICENSE file), but open-design's lineage table labels the *bundled copy* **"MIT, @op7418."** These conflict — **AGPL-3.0 is strong copyleft**, which matters for anyone redistributing. Verify the bundled `design-templates/guizang-ppt/LICENSE` before relying on the "MIT" claim. See [[open-design/caveats-and-safety]].
- **html-ppt-skill** (@lewislulu): the **"HTML PPT Studio"** family — **36 themes**, **31 page layouts**, **47 animations** (27 CSS + 20 canvas), **15 full-deck templates**, presenter mode (press **S**: draggable current/next cards, speaker notes, timer). Zero-build static HTML/CSS/JS, token-driven theming, iframe-isolated preview. **MIT**, **6,713★**.
- Both are **HTML-first `SKILL.md` skills** — you can use either **standalone** for Scrum decks without Open Design (pilot method D1).

## `VoltAgent/awesome-design-md` + `bergside/awesome-design-skills` — the design-system layer

- **awesome-design-md** (**94,742★**, MIT) — origin of the **9-section `DESIGN.md` schema** + ~70 product systems. Full treatment: [[open-design/design-md-as-source-of-truth]].
- **awesome-design-skills** (1,482★, MIT) — a catalog of design skills, each a folder pairing a `SKILL.md` (workflow) with a `DESIGN.md` (system). Open Design's README says it sourced **"57 design skills"** here; the repo now documents **~67** — a count drift, not a contradiction.

## `heygen-com/hyperframes` — the motion engine

- **32,398★**, **Apache-2.0**, TypeScript, created **2026-03-10**. ⚠️ Owner **is** a real organization (`heygen-com` = the HeyGen company) — verified, not a typo; "used in production at HeyGen," and cited by tldraw/TanStack.
- **HTML→MP4 deterministic motion graphics** ("same input, same frames, same output" — seeks each frame in headless Chrome, encodes with FFmpeg). Supports GSAP/CSS/Lottie/Three.js/Anime.js. Integrated into Open Design as the first-class **`hyperframes-html`**. ⚠️ Integration is README-described, **not code-audited** here.

## `Claude Code skills` (SKILL.md) — the convention adopted verbatim

Open Design adopts Anthropic's **[`SKILL.md`](https://docs.anthropic.com/en/docs/claude-code/skills)** format wholesale (a folder + YAML frontmatter + trigger phrasing), extended with its `od:` frontmatter. Zero migration cost for existing Claude Code skills. Cross-ref [[../claude-skills/_index]] · [[../claude-code-skills-stack/_index]].

## Key Takeaways

- Open Design is an **orchestrator standing on ~9 credited upstreams**, not a from-scratch build: philosophy (huashu-design), a predecessor (open-codesign), a daemon (multica), deck skills (guizang/html-ppt), the `DESIGN.md` schema (VoltAgent), and a motion engine (HeyGen's HyperFrames).
- **`open-codesign` is the real "first"** OSS Claude Design alternative (10 days earlier) — open-design credits it as its UX North Star and is the far larger, feature-rich sibling.
- Two **license landmines**: guizang-ppt is **AGPL-3.0** upstream (README says MIT for the bundled copy — a conflict), and multica is **NOASSERTION** (no recognized license). Both matter for redistribution.
- The **`SKILL.md` convention is Anthropic's**, adopted verbatim — the lineage runs straight back to Claude Code skills.
