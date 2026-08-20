# Claims scorecard

> Every substantive claim in the 6-video bundle, graded. Grades: **CONFIRMED** (independently verified) · **CBI** (confirmed-by-internal-consistency — multiple independent sources agree, no external check available) · **PLAUSIBLE-NOT-PRIMARY** (widely reported, no primary source) · **MISLEADING** (true-ish, framed wrongly) · **FALSE** · **UNRESOLVED** (sources disagree or evidence insufficient) · **UNVERIFIABLE**.
>
> Verification date: **2026-08-20**. Direct fetches: `github.com/deepseek-ai/deepseek-harness`, `github.com/cordiverse/paper`, `github.com/topics/dsh-plugin`.

## Totals

**47 claims graded: 24 CONFIRMED · 10 CBI · 4 PLAUSIBLE-NOT-PRIMARY · 4 MISLEADING · 1 FALSE · 3 UNRESOLVED · 1 UNVERIFIABLE. 0 FABRICATED.**

_Totals verified by tallying the table itself, not by hand-count._

---

## Identity, license, scale

| # | Claim | Source | Grade | Note |
|---|---|---|---|---|
| 1 | DSH is open source under **MIT** | Turing Post, Better Stack | **CONFIRMED** | Verified on repo |
| 2 | "About" string is *"DeepSeek Harness: Everything is a Plugin"* | multiple | **CONFIRMED** | Verified verbatim |
| 3 | It is a **developer preview** | Chase AI, Firecrawl | **CONFIRMED** | README: *"THERE WILL BE COMPATIBILITY-BREAKING CHANGES"* |
| 4 | **167,000 stars** (2026-08-20) | Chase AI | **CONFIRMED** | 169.1k measured same day; ~1% |
| 5 | **147,000 stars / 15,000 forks** (08-17) | Turing Post | **CONFIRMED** | Official counter that day: 141,532 / 14,350 — same-day drift |
| 6 | **135,000 stars** (08-17) | Cef | **MISLEADING** | Low against 141,532; same-day, likely recorded earlier |
| 7 | **150,000 stars** (08-19) | Better Stack | **MISLEADING** | Stale-low; 8/18 readings already exceeded it |
| 8 | **"over 150,000 in just a few days"** (08-18) | Firecrawl | **CONFIRMED** | Consistent with vault's 159.0k same day |
| 9 | **158,000 stars** (08-18) | VN | **CONFIRMED** | Vault v242 independently read 159.0k that day |
| 10 | **"fastest growing repo ever"** | Chase AI | **PLAUSIBLE-NOT-PRIMARY** | ~20k in ~1h, ~100k in <48h reported; **but GitHub publishes no velocity record and no primary source claims it** |
| 11 | Growth **faster than OpenClaw** | VN | **PLAUSIBLE-NOT-PRIMARY** | Multiple reports name OpenClaw as prior holder; independently reached by VN |
| 12 | Prior speed reference was **Grok-1 (~1.2 days)** | external | **PLAUSIBLE-NOT-PRIMARY** | Secondary reporting only |
| 13 | **TypeScript 97.1%** | VN | **UNRESOLVED** | Page-stated language bar; v242's D23 (language-basis) applies — bilingual `.md`/`.zh.md` pairs distort doc counts, unclear whether code % is affected |
| 14 | Repo went public **~3–4 days** before 08-17/08-18 | Cef, VN | **CBI** | Both independently; paper draft dated **2026-08-13** corroborates a ~08-12/13 launch |
| 15 | Desktop app has **11,000 stars** | Better Stack | **UNVERIFIABLE** | Not re-measured this ship; vault v241 covers the artifact |

## Architecture

| # | Claim | Source | Grade | Note |
|---|---|---|---|---|
| 16 | Model adapter, tool registry, agent loop, session log, sandbox policy, web UI are all plugins | all 5 EN + VN | **CBI** | Six independent enumerations, near-identical |
| 17 | Built on **Cordis** | all 6 | **CONFIRMED** | README: *"is powered by Cordis"* |
| 18 | Cordis is **not** a DeepSeek invention — by **shigma**, from the **Koishi** ecosystem | Turing Post, Better Stack | **CONFIRMED** | Verified; also matches v242's `README.md:7` credit to `cordiverse` |
| 19 | Cordis ran **4 years / 4,000+ community plugins** in Koishi | Turing Post | **CONFIRMED** | Verified externally |
| 20 | Cordis *"sat on GitHub since 2022"* | Better Stack | **UNRESOLVED** | v242 read copyright as *"2021-present Shigma"*; external reporting says "four years" (→ ~2022). Both recorded |
| 21 | **"Everything"** excludes the kernel/node/OS/hardware | Turing Post | **CONFIRMED** | Only source to check the word; correct |
| 22 | You can edit the **agent loop** itself — not possible via Claude Code skills/hooks | Chase AI, VN | **CBI** | Two independent; plugin config exposes loop parallelism |
| 23 | Turning off core plugins can **lobotomize** the app | Better Stack | **CBI** | Direct consequence of #16; nobody demonstrates it |
| 24 | Model-agnostic: DeepSeek / OpenRouter / OpenAI / Anthropic / Bedrock / Ollama / any OpenAI-compatible | all | **CBI** | Demonstrated live by 4 of 6 |
| 25 | Modes: **standard / PTC / minimal / creator** | Chase AI, Firecrawl, Cef, Better Stack | **CBI** | Consistent across four |
| 26 | "PTC" batches tool calls into one script to cut context bloat | Chase AI | **UNRESOLVED** | Behaviour described consistently; **no source expands the acronym** — vault does not assert an expansion |

## The paper

| # | Claim | Source | Grade | Note |
|---|---|---|---|---|
| 27 | A paper exists: *"A Programming Paradigm for Spatiotemporal Composability"* | Turing Post, Cef, VN | **CONFIRMED** | `cordiverse/paper`, 2.4k stars |
| 28 | Abstract as read aloud | Cef | **CONFIRMED** | Verbatim match on fetch |
| 29 | Authors from **Peking University + DeepSeek** | Turing Post | **CONFIRMED** | Yifan Shi (PKU+DeepSeek), Wei Zhang (PKU), Tianyi Cui (DeepSeek) |
| 30 | Paper repo at **~2,000 stars** | Turing Post | **CONFIRMED** | 2.4k now; accurate at recording |
| 31 | Paper is **~70–80+ pages** | VN, external | **PLAUSIBLE-NOT-PRIMARY** | Not confirmed on repo page |
| 32 | **Confluence**: path-independent final state | Turing Post | **MISLEADING** | Accurately described, **but presented as a result — it is a preprint "under active revision," dated 2026-08-13, not peer-reviewed** |
| 33 | Confluence's stated limits (correct inverses; successful execution; independent effects; no cycles) | Turing Post | **CONFIRMED** | Only source to state limits; strongest source in bundle |
| 34 | *"Cordis can remove the plugin that sent an email. It cannot remove the email"* | Turing Post | **CONFIRMED** | Correct characterization of the boundary |
| 35 | Math basis is effect systems | Turing Post | **CONFIRMED** | Verified as **effects and coeffects** from type theory |

## Creator mode

| # | Claim | Source | Grade | Note |
|---|---|---|---|---|
| 36 | Agent authors plugins for its own harness mid-session, human approves | all 5 EN | **CBI** | Four independent live demos |
| 37 | Creator packages **cannot self-promote** to permanent | Turing Post | **CONFIRMED** | The precise formulation |
| 38 | Plugins persist **only** if you tell the model to write them to config | Chase AI, Firecrawl | **CBI** | Compatible with #37; the human-initiated path |
| 39 | **Hot reload works without restart** (unqualified) | Cef | **FALSE** | Applies to *dynamic* plugins only; installed presets are frozen at session start (Firecrawl) and Cef himself never tests a preset |
| 40 | Hot reload *"depends on the plugin"* | Chase AI, Firecrawl | **CONFIRMED** | The correct version; VN's screen confirms by breaking |
| 41 | A self-improving harness is **not** today's reality | Chase AI, Turing Post | **CBI** | Both explicitly deflate; zero non-cosmetic demos in bundle |

## Security

| # | Claim | Source | Grade | Note |
|---|---|---|---|---|
| 42 | **Every plugin gets full shell + filesystem access** | Chase AI, Firecrawl, VN | **CONFIRMED** | DSH's own docs: sandbox is *"containment for honest code, not a security boundary"* |
| 43 | Creator sandbox is **not a security boundary** | Turing Post | **CONFIRMED** | Primary-sourced; strongest safety finding in bundle |
| 44 | A rogue plugin could read your API keys | Chase AI, Firecrawl, VN | **CBI** | Follows from #42; nobody demonstrates it |
| 45 | *"the job of a harness is to prevent prompt injection, not make it easy"* | Firecrawl | **CONFIRMED** | Editorial, and correct as stated |

## Ecosystem

| # | Claim | Source | Grade | Note |
|---|---|---|---|---|
| 46 | Catalogue at **~1,400 entries**, growing daily; repo **8,400 stars in 4 days** | VN | **CONFIRMED** | Independently corroborates vault v240's 1,390 |
| 47 | The plugin ecosystem is **~1,400 plugins** | implied by all | **MISLEADING** | The `dsh-plugin` **topic holds 8,874 repos**; the catalogue is a **~16% sample**. See [[deepseek-harness/ecosystem-and-the-catalogue-gap]] |

---

## Zero fabrications

**No source in this bundle invented a fact.** Every error found was a same-day star drift, an unqualified generalization (#39), an over-read of a preprint (#32), or a scope error (#47). For a bundle whose titles include *"Changed AI Forever,"* *"The End Of Coding Agents,"* and *"Fastest Growing Repo EVER,"* the body content is markedly more disciplined than the packaging — see [[deepseek-harness/caveats-and-corrections]].

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/caveats-and-corrections]] · [[deepseek-harness/hype-vs-source-scorecard]] · [[deepseek-harness/source-provenance]]
