# (C) Verdict — `cathrynlavery/diagram-design` (v250)

**Date:** 2026-08-19 · **Routine:** LLM Wiki Routine v2.7 · **Tier:** T4 Plugin/Extension (with a T1 Skill/Methodology facet)

---

## Phase 0.9 — inclusion criteria

| Criterion | Verdict | Reasoning |
|---|---|---|
| **(a)** Anthropic affiliation / registered vendor-direct source | ❌ **FAIL** | **Cathryn Lavery** — founder of BestSelf Co, writes at littlemight.com, trained as an architect. A **disclosed individual, not Anthropic**, and not a registered (a)-7 vendor-direct source. Per **§41**, no name, notability, heritage or reputation inference may rescue (a) — and her notability is considerable, which is exactly why the rule exists. Answered **NO**. |
| **(b)** Goal relevance | ✅ **STRONG** | A **Claude Code plugin/agent skill** — the operator's primary tool, and the core of Goal #1 ("master Claude and autonomous agents for software development"). Not adjacent: it installs into Claude Code, ships a `SKILL.md` consumed by the model, and its central engineering problem (what a skill's frontmatter description does to invocation routing; what 37 KB of `SKILL.md` costs per request) sits directly on the vault's live tool-catalogue / token-cost thread. **No §40 operator-direction needed.** |
| **(c)** Quality / integrity | ✅ **STRONG** | MIT. **Source verified three times** across two transports (2 clones + tarball), 335 files, byte-identical. 20+ contributors, 114 commits, one git root. 26 CI gates wired across a 6-runner matrix with zero soft-fail. Six ADRs, one of which correctly amends itself. Honest limitation sections. ⚠️ Tempered by three real doc-drift instances and a 20-file lint baseline — all documented below, none concealed. |
| **(d)** Applicability | ✅ **STRONG** | The most directly pilotable subject in many ships: a one-line install into the operator's own Claude Code, no server, no credentials, no `postinstall`, writes confined to a profile directory and files you asked for. The vault ships an HTML artifact per wiki; diagrams are a live need. |

### → **GOAL-ALIGNED INCLUDE, 3/4**

**Streak:** v249 `GA:107` → **`GA:108 · OG:13 [7 ov]`** — **31 consecutive goal-aligned ships (v220→v250)**.
**§35:** CLEAR — window {v248 GA, v249 GA, v250 GA} = 0 OG.
**Override:** none required.

---

## Mint decision — **NO MINT**

**Counts UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab. §C live standalones 51 unchanged. Surface ≈58 unchanged.**

### Grounds

1. **It is a clean instance of a CONFIRMED pattern, not a new class.** **Pattern #88 "Anti-Slop-Curation"** (CONFIRMED, domain-general since the v110 audit) fits exactly, and at its strongest sub-typology **88c "machinery-with-enforcement"**. The tagline is literally anti-slop vocabulary — *"No shadows, no **Mermaid-slop**"* — and `README.md` states the aesthetic rationale in the pattern's own idiom: the 4px grid is *"non-negotiable, it's what keeps the diagrams from feeling AI-generated."* It joins the design-skill cluster **impeccable v75 / taste-skill v81 / huashu-design v82 / open-design v83 / ui-ux-pro-max v85 / hallmark v204 / ui-skills v218**. The **hallmark v204** handling is the direct precedent: a strong, well-built design skill by a notable org, rated a Pattern #88 88c instance with no mint.

2. **Decisive first-party prior art for the guidance half.** Anthropic ships diagramming guidance for agents itself: an **`artifact-diagramming`** skill is present in this very session's skill roster — *"Diagramming know-how for Artifacts — when a picture earns its place, how to draw one that shows the real mechanism, and the inline-SVG mechanics that keep it legible in both themes"* — and Artifacts **render Mermaid natively** (```` ```mermaid ```` fences in Markdown, `<pre class="mermaid">` in HTML). "An agent skill that teaches an agent to draw good inline SVG that works in light and dark" is a first-party feature. diagram-design is broader and far more opinionated, but the surface is occupied.

3. **Not world-first for the underlying idea.** "Declarative source → opinionated pretty diagram" is a mature category: Mermaid, D2, PlantUML, Graphviz, `mingrammer/diagrams`, Structurizr, draw.io, Excalidraw, Kroki, plus AI-era entrants (Eraser DiagramGPT, Napkin.ai, Whimsical AI, tldraw make-real). The **v222 lobehub** discipline applies — *world-canonical is not world-first, and fame is not a mint.*

4. **Form-factor-within-a-genre.** Delivering an established genre as an agent skill is a packaging choice, not a new capability class — the **v227 hermes-webui** and **v236 dsh-TUI** grounds.

5. **§28 anti-inflation** at 51 live standalones, and it is not the exemplar of a class it would open.

### ⚠️ Strongest NO-MINT alternative — RECORDED, reviewable, NOT self-executed

A §C standalone at **N=1**: *"Aesthetic/Editorial Design Ruleset with Machine-Verified Output Geometry"* — a design system whose rules are compiled into executable geometric assertions (label-mask paint-order checking; treemap area-fidelity checking with relative error) rather than expressed as a checklist addressed to the model.

**The case for it is genuinely strong on mechanism**: nothing in the seven-member design-skill cluster does this. Every prior instance is prose — a checklist, a forbidden-list, a critique rubric. This one numerically verifies that a chart's visual encoding does not lie about its own numbers, and tests its verifiers adversarially in both directions.

**The case against, which I judge to win**: the mechanism is a *technique*, not a capability class (the **v211 PixelRAG** discipline — corpus-first-for-a-technique is not mintable), and the verified-geometry machinery **does not ship to the user** (§9 of the Deep Dive), so it is not a capability the installed skill provides — it guards the vendor's own gallery. The **v242 D25 / v246** rule applies: *the machinery is not in the artifact you get.*

**Recorded, flagged to the overdue audit, not executed. A mint is an audit act (the v232 rule).**

### Secondary pattern activity — recorded, not self-incremented

- **Pattern #88 88c** — clean instance; N-tally is audit bookkeeping.
- **Pattern #84 84c** (cross-vendor ecosystem tolerance) — four harnesses from one canonical skill (Claude Code / Codex / Pi / Cowork org marketplace), reconciled by a CI gate comparing manifest descriptions rather than by symlink. Inherited shape → **no N-bump claimed**.
- **Pattern #57** — a genuine corpus-recursive dependency: ships a `prompts/` directory of **Pi** templates, and Pi is corpus subject **v36 / v228** (`earendil-works/pi`).
- **Pattern #83 honest-deficiency disclosure** — three instances: a *"When **not** to use this skill"* section that argues against its own use (*"Before drawing, ask: would a reader learn more from this than from a well-written paragraph? If no, don't draw."*); the checklist's explicit *"In this repository"* vs *"from an installed skill, manually check"* split; and a named, committed 20-file lint baseline.
- **v246's `grep -rni "silent"` detector — 5th consecutive replication**, with a new species (the silences hunted are the *checkers'* own blind spots). See Deep Dive §8.
- **v240 inventory rule** — its controlled experiment (two functions, one file). See Deep Dive §4.1.
- **v245 D32** — found independently in `docs/adr/0002` (*"see Amendments for the current figure"*).
- **v247 D34** — tested and **PASSED** (0 unwired gates, 0 soft-fail). The first clean pass on this rule in the run.
- **v247 D35** — confirmed by a within-repo controlled comparison (machine-maintained strings correct, hand-maintained strings stale).
- **NEW DEFERRED WATCH AXIS (N=1):** *"agent-skill engineering as an object of study — the frontmatter description as routing surface, and the byte budget that competes with it"* (ADR 0004). The corpus's first subject whose documented engineering problem is *how a skill gets invoked at all*.

---

## The three things worth remembering

1. **You can only compile the part of your aesthetic that becomes a *lie* when violated.** Of six rules `SKILL.md:261` calls "non-negotiable", one has a gate — the one whose violation is a determinate rendering defect. `verify-geometry.py:9-14` states the criterion: *"Paint order is what makes this a defect rather than a stylistic choice."* Sort your quality rules into decidable and not before automating any of them — and stop calling the second group non-negotiable.

2. **A gate's aim, not its quality, decides what rots.** Two scripts count this project's type count and an ADR calls it *"a stable, verifiable claim."* It is right in every gated surface and stale at 27 in three ungated ones — two shipped agent-facing command files and the repo description, the single most-read string it has. The same 236-line file contains one bidirectional inventory check and one unidirectional one; the README tree that the unidirectional check governs is missing **14 of 28** type files and **21 of 28** scripts, green.

3. **A skill's frontmatter description is infrastructure, not documentation.** ADR 0004 records a byte cap that forced deleting type names from the description and thereby **broke the skill's own invocation** — *"removing 'flowchart', 'Gantt', 'org chart' from it removes the lexical hooks that make 'make me a flowchart' invoke the skill at all."* They ranked description completeness above their own byte budget and mechanised it. The exact inverse of **v238**, which found that blanking tool injections *improved* reasoning — together the two bound the problem: strip the catalogue and the model reasons better; strip the description and the model never arrives.

---

## Security — **LOW** (cleanest since v249)

No server, no port, no CORS, no socket → **the broken-auth triad is structurally impossible**. No `postinstall`/`prepare`. No telemetry (README links carry `utm_source`; nothing else). Writes confined to `~/.diagram-design/profiles/`, the skill's `style-guide.md`, and diagrams you asked for, behind a real propose-diff-then-approve gate with a recoverable snapshot. Output safety is careful and specific: a font allowlist pinned to *hostname exactly `fonts.googleapis.com`, path exactly `/css2`, lookalikes fail*; `<iframe>`/`<object>`/`on*` rejected; the motion controller pinned byte-for-byte.

**🔴 The one gap:** brand onboarding fetches a live website into the agent's context and **nothing treats that page as untrusted text**. Every guard concerns what gets *written*, none what the page might *say*. Same for `.drawio`/`.mmd` labels: output-escaping is handled, agent-steering is not addressed anywhere. This is v247's gap. **Severity LOW** — the worst realistic outcome is an ugly diagram or a blocked remote font URL, and no credentials are in the path — but the sentence *"a fetched page is data, not instructions"* is missing and should not be.

---

## Pilot verdict — ⭐ **INSTALL, fenced** (a rare recommendation for this corpus)

This is the first subject in a long run where the install case is genuinely stronger than read-and-borrow, and the reason is specific: **the risk surface is almost empty and the need is live.** No server, no credentials, no lifecycle scripts, MIT, source-verified three times, 26 CI gates across 6 runners with nothing unwired. And the vault publishes an HTML artifact per wiki ship — diagrams are something it actually wants.

**The fence:**
- Install via the **Claude Code marketplace path**, not `npx skills add` (the README documents the migration off the standalone copy).
- **Pin the version you reviewed — 2.5.6** — and read the diff before accepting an auto-update. Note that enabling auto-update is an explicit opt-in step for third-party marketplaces; leaving it off is the more conservative default and costs you a manual `/plugin` refresh.
- **Do not point brand onboarding at a site you do not control** until you have satisfied yourself about the untrusted-page question. Onboarding the vault's own tokens by hand — editing `references/style-guide.md` directly, which the README documents — avoids the fetch entirely and is the recommended route.
- Prefer the **editable install** (`git clone` + symlink `skills/diagram-design` into `~/.claude/skills/`) so package updates cannot overwrite your customised style guide.
- Budget the token cost: **~11K tokens per diagram request** (`SKILL.md` 37.8 KB + one type reference ~5 KB).
- 🔴 **Never** run brand onboarding against a candidate's or client's site from a hireui-adjacent session; **never** put candidate data into a diagram.

**Zero-install first step if you would rather look before installing:** clone it and open the gallery — `open skills/diagram-design/assets/index.html` — and flip through all 28 types in light / dark / full-editorial. That answers the only question that actually matters (do you like the output?) in about ninety seconds, at zero risk.

---

## hireui relevance — honestly, thin, with two real exceptions

A diagram skill is not a recruitment component, and I will not manufacture relevance. Two genuine uses:

1. **Documenting hireui's architecture.** The Candidate-Detail refactor spike, the vendor-seam ADR and the RATIFIED candidate-LLM legibility ADR all describe structures that a diagram would carry better than prose — and the legibility ADR's whole demand is that an LLM path be *legible* to a human reviewer. An architecture diagram of that path is a direct artifact of that clause.
2. **The gate discipline, not the diagrams.** Three transferable rules: (i) sort quality rules into decidable and not, and only automate the first; (ii) make every inventory check bidirectional; (iii) a hardcoded expected value in a test is not a specification — put its authority somewhere a human must consciously amend.

**Not applicable:** anything touching candidate data.

---

## What is NOT established

Stated plainly, because the list protects the ship:

- **Reception and growth.** Star/fork/watcher figures are **page-stated only** (§37.4, the GitHub API is mocked here) → **no Pattern #52 velocity claim.** The originating share, the launch timeline, the substantive public criticisms, and whether the author has written about building it: **all unestablished.** The fleet's reception report did not survive its verification pass cleanly enough to publish specifics.
- Release/tag history and cadence; issue and PR counts and their contents; whether any open issue contradicts a README claim.
- The author's GitHub bio text and account history as any agent quoted it.
- `drawio_extract.py`'s numeric resource caps and XXE guard — **fleet-reported, structurally consistent with my reading, but the constants were not confirmed by me.**
- Whether the 28 types are *good* diagrams. Nothing in this analysis evaluates output quality; I read the machinery, not the pictures. The gallery is the test and it takes ninety seconds.
- Output-quality behaviour on a real request. No diagram was generated during this analysis.

---

## Blunt summary

A founder with no engineering training and a real design eye wanted diagrams that matched her website, got generic rounded boxes from Claude, and instead of complaining wrote a 28-type editorial design system as an agent skill — then wrote **11,305 lines of Python to check it**, which is **1.56× the size of the skill itself**, wired all 26 gates into a six-runner matrix with no soft-fail, and tested her own graders adversarially in both directions.

The interesting part is where she stopped. Of six connector rules her own `SKILL.md` calls "non-negotiable", exactly one has a gate — and the gate's docstring says why: *"paint order is what makes this a defect rather than a stylistic choice."* She gated the rules whose violation is a lie about the rendering and left the rules whose violation is merely ugly as prose addressed to the model. That is the correct line, drawn deliberately, and stated. Nobody else in this corpus's seven-member design-skill cluster has articulated it.

And then the ordinary thing happened. The type count is right in every surface a counter was aimed at — two scripts count it, an ADR calls it a stable verifiable claim, the amendment procedure was followed when treemap made it 28 — and it is still **27** in two shipped slash-command files and in the GitHub description, which is the single most-read string the project owns. The same 236-line file that gets the gallery inventory check right in both directions gets the README tree check right in only one, and the README tree is now missing half the type files and three-quarters of the scripts, green. The verification code is excellent, so the drift simply moved to where the verification is not.

Take three things and you can install the fourth. The decidability test, before you automate any quality rule. The rule that an inventory check must run both ways, because the one that does not cannot see what is missing. And the line from ADR 0002 that is worth more than the rest of the repository: *"the number in the test is just whatever the last contributor typed."*

**Suggested next action:** review + merge `wiki/v250-diagram-design`, then spend ninety seconds in the gallery deciding whether you like the output — and make **v251 the audit**, which is now **38 ships overdue.**
