# (C) Verdict — v260 `mranex/Anime_Vault`

**2026-08-21** · **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46 / 12 UNCHANGED** · §C-1 **12** unchanged · §C-2 **38** unchanged

---

## Phase 0.9 gate

| Criterion | Call | Basis |
|---|---|---|
| **(a) cultural-peer / Anthropic signal** | **FAIL** | `mranex` — a pseudonymous individual; one email, no disclosed identity, no Anthropic affiliation, no registered (a)-7 vendor source. §41: no inference from name, heritage or locale. |
| **(b) goal-relevance** | **MODERATE via §40** ⚠️ **the thinnest (b) of the four — OFF-GOAL is genuinely defensible** | See below. |
| **(c) substance** | **STRONG** | 7,999 lines of Python + 3,172 of TSX over a 2,134-line data layer; three real front ends; a 14-parameter filtered randomiser with anti-repeat; per-drive UUID identity files; clean parameterised SQL. Source-verified by two clones. |
| **(d) legibility** | **STRONG** | Small, readable, conventionally organised. The core/ui/server split is obvious from the tree. An accurate architecture diagram. |

### ⚠️ (b) — stated bluntly, because it is the weak point

**Zero LLM. Zero agent surface. Zero CI.** The one hit from an eight-term AI/LLM grep across the whole tree was `ScrollMode` matching `llm`. There is no MCP server, no skill file, no `CLAUDE.md`, no model provider, nothing an agent can call. On its own domain — cataloguing a personal anime collection across external drives — **this subject does not clear (b), and the v219 Ghost-Downloader-3 precedent (a consumer download manager, rated OFF-GOAL CAPTURE) is the right comparison.**

The (b) MODERATE call rests entirely on two things, and I am not going to dress them up as more:

1. **It is the N=4 instance of the same-author control the operator ratified as §42 one ship earlier** — and it is the instance that found the method's confound. That is goal-relevant to the vault's own knowledge-building, which is Goal #1's substrate.
2. **Its architecture answers a live vault decision.** v258's *code moves forward, never backward* finding generalised to "only a shared library makes a fix travel back," and the v259 audit left open exactly that question about `05 Skills/` and the v2.1–v2.8 routine deltas. This repository is the same author solving it correctly — three front ends over one shared core, with the load-bearing function called and not copied.

⭐ **Under §40** (operator-requested goal-adjacent subject, (b) MODERATE+, no override required) this lands **GOAL-ALIGNED**. **OFF-GOAL CAPTURE is recorded as the strongest reviewable alternative of the four siblings** — thinner here than v256 (where the LLM was one stage of ten) and much thinner than v257 (13 versioned prompt templates). If the operator elects OFF-GOAL: **`GA:116 · OG:14 [7 ov]`**, and **§35 stays CLEAR either way** — window `{v257 GA, v258 GA, v260 OG}` = 1 OG in a rolling 3, which is at the ceiling, not over it. **The election costs nothing.** I would accept it without argument.

---

## NO MINT — five grounds

The declinable candidate is a §C-2 standalone at N=1: *"Multi-Front-End Desktop Application Over a Single Shared Core — a CLI, a native GUI and a web UI served by one data layer, with the superseded GUI shipped alongside its replacement."*

1. 🔴 **Domain-not-capability, decisive.** A personal media-library manager is a domain. The corpus has ruled this way repeatedly and recently — v197 (mlsysbook), v196 (meetily), v210 (AIRI), v220 (little-book-rl), v255 (HeadFirstAndroid). Corpus-first for a **domain** is a data-point, not a mint.
2. 🔴 **Not world-first, and not close.** Sharing a core across a CLI, a desktop GUI and an HTTP API is standard layered architecture — older than any subject in this corpus. There is nothing here a mint would be recording.
3. 🔴 **Form-factor within a genre.** "Desktop app with a web front end over a local API" is the v236/v227/v222 chain's exact shape, ruled on three times.
4. 🔴 **§28** — but per routine **v2.8 §44 clause 5** this is now a *supporting* ground only, measured against **§C-1 = 12**, not against the 38-row catalogue, and **must not be load-bearing alone.** It is not: grounds 1–3 each suffice.
5. 🔴 **A bus-factor-one anchor with no verification surface.** 3 commits, 87 minutes, one author, zero tests, zero CI, and a documented install path that cannot work. The v180/v234 discipline.

**`inflation_check` HELD** — 0 mints, 0 N-bumps, no promotions, no retires.

⭐ **RECORDED FOR THE AUDIT — the §42 amendment candidate** (§6 of the Deep Dive): *the same-author control must record, per repository, whether the repository was the **workspace** or a **destination**; habits that accumulate in a working directory are structurally unobservable in a bulk import, and reading their absence as discipline mistakes workflow for character.* Recorded, not self-executed — amending a routine section is an audit act.

⭐ **ALSO RECORDED — new method rule candidate D48:** *line numbers from a `cat` of a glob are not file line numbers; `grep -n` the file list, never the concatenation.* Plus the content-grep corollary to D42/D47: **a positive from an unanchored substring is not a positive** (`ScrollMode`→`llm`; `Plex`→`multiplexer`).

---

## Bookkeeping

- **Counts:** 46 top-level patterns · **12** CONFIRMED Library-vocab · §C-1 **12** · §C-2 **38** · max pattern #85. **All unchanged.**
- **Streak:** v258 `GA:116` → **`GA:117 · OG:13 [7 ov]`** — **40 consecutive goal-aligned ships, v220→v260** (v259 was an audit; audits are not ships).
- **§35:** **CLEAR.** Window `{v257 GA, v258 GA, v260 GA}` = 0 OG.
- **Override:** none. §40 applies; no override consumed.
- **Tier:** T5 Application. Reviewable — it has no agent facet at all, which makes it the plainest T5 in a long while.
- **Secondary, not minted:** #19 19a (fourth `mranex` data-point; the small-scale ecosystem-portfolio shape now at N=4) · LV-C7 Tauri-desktop cluster data-point · **#12 clean NEGATIVE, same-author N=4** (0 tests, 0 CI, 0 agent surface across all four repos) · **#66 MIXED** (bounded pins + clean SQL + no `shell=True` + a real licence, against a wildcard-CORS unauthenticated local API and an install path that cannot succeed) · **#83 NEGATIVE** — the README declares the migration but never discloses that the superseded generation is still shipped and still reachable.

---

## The one-line verdict

**A better-built program than any of its three siblings, documented so that following its own instructions cannot make it run — and the fourth data point that turned four of my six "dispositions" into artifacts of where the code was written.**
