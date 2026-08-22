# (C) Verdict — v266 qiaomu-anything-to-notebooklm

> Companion to `(C) qiaomu-anything-to-notebooklm — Deep Dive.md`. Routine v2.8, Phase 0.9 STRICT.

## Subject

`joeseesun/qiaomu-anything-to-notebooklm` — a Claude Code **skill** that acquires content from many sources and pipes it into **Google NotebookLM** to produce podcasts, slide decks, mind maps, quizzes, flashcards and reports from natural-language requests in Chinese.

- **HEAD** `cea6ceee8cdcd01a573af5ae75c2d3cffc20650b`, 2026-04-28 09:38 +0800. Two clones, `diff -rq` clean both ways.
- **11 commits · 1 root · 1 author · 20 files · 4,680 lines · 2 tags (both 2026-01-25) · no CI ever.**
- MIT (`LICENSE:3` "Copyright (c) 2026 Joe"). Author discloses X `@vista8` and WeChat 「向阳乔木推荐看」 at `README.md:504`.

## Phase 0.9 STRICT — GOAL-ALIGNED INCLUDE 3/4

| Axis | Call | Ground |
|---|---|---|
| **(a) cultural-peer / vendor-direct** | **FAIL** | §41. No declared Anthropic affiliation anywhere in README, SKILL.md, LICENSE or any commit message. Not a registered (a)-7 vendor-direct source. A *disclosed individual* with a real public identity is not a registered (a) axis — the v171 / v174 / v183–v185 / v204–v205 / v212 discipline. No name, heritage or locale inference. |
| **(b) goal relevance** | **STRONG** | It *is* a Claude Code skill; the agent is the runtime and the entire artifact is agent-facing. Squarely on goal #1's substrate. |
| **(c) instructiveness** | **STRONG** | Instructive in both directions: a genuinely good progressive-questioning module and a clean intent-mapping table, alongside the corpus's most legible pull-request-shaped failure. |
| **(d) corpus connectivity** | **STRONG** | Three prior corpus subjects are its dependencies — v7, v28, v143. Sits in the skill / agent-capability cluster. |

**Cleanly GA. No §40 needed. No operator override. §35 CLEAR** (rolling window {v264 GA, v265 GA, v266 GA} = 0 OG).

**Streak: v265 `GA:122` → `GA:123 · OG:13 [7 ov]` — 46 consecutive goal-aligned ships, v220 → v266.**

## NO MINT

**Counts UNCHANGED: 46 top-level patterns / 12 CONFIRMED Library-vocab. §C-1 = 12. §C-2 = 38.**

Four independent grounds, in order of weight:

1. **Not world-first, and the prior art is in this vault.** Corpus **v7** (`teng-lin/notebooklm-py`, 2026-04-18) already ships a 26 KB `SKILL.md` for Claude Code / Codex / OpenClaw, an installer (`notebooklm skill install` → `~/.claude/skills/notebooklm`), **intent-based auto-activation on the same phrases** (*"Create a podcast about…"*, *"Turn this into an audio overview"*, *"Make flashcards…"*), the same artifact enumeration, five named workflow patterns — **and an explicit autonomy/trust boundary this subject does not have.** Three months earlier, first-party.
2. **Form factor within an established genre.** A front end for an existing capability is not a new capability class: **v222** lobehub (decisive), **v227** hermes-webui, **v236** dsh-TUI.
3. **Domain/locale coverage is not capability.** The new-for-the-corpus part is the *Chinese-platform acquisition stack* (WeChat public accounts · 小宇宙/喜马拉雅/B站 via Get笔记 · 飞书). Domain-not-capability — **v196** meetily / **v210** AIRI / **v213** geti.
4. **The novel parts are components, not the product** (**v242 D25**), and the most distinctive component — the paywall cascade — is **openly derived** from Bypass Paywalls Clean (`README.md:114`) and is **one third unreachable** (proved by execution).

`inflation_check` **HELD**. **Per §44 cl. 5, §28 does none of the work.**

## Recorded, NOT self-executed

**One §C-2 candidate**, for an audit to decide: *"Agent-Facing Paywall-Bypass Fetch Layer"* — a bypass cascade packaged as a capability an AI coding agent invokes rather than a browser extension a human clicks. Corpus-first for the *agent-facing* surface; **decisively not world-first**. I decline to mint: the strategies are borrowed and credited, a third of the cascade is dead code, and the corpus's web-acquisition family is already dense (crawl4ai v29 · browser-use v41 · CloakBrowser v69 · Agent-Reach v174 · camofox v179 · firecrawl v214 · CoreOfPotato v231 · gemini-web2api v232). **A mint is an audit act.**

## Instance-strengthening recorded, not self-incremented

- ⭐⭐ **Pattern #57 — corpus-recursive dependency at N=3 in a single subject.** `notebooklm-py` = **v7** (`install.sh:94`, credited `README.md:492`) · `markitdown` = **v28** (`requirements.txt:8`, credited `README.md:489`) · `lark-cli` = **v143** (`main.py:231`, **credited nowhere**). And **v7 is the subject that established the corpus's Tier 4 "Agent-as-bridge" category** — the category this subject sits on top of.
- ⭐ **The credit asymmetry, inside one repository.** Two of three corpus-subject dependencies are credited; the third is invisible to the installer, the environment checker, `requirements.txt` and the README alike. The corpus tracks this contrast **across** two repositories (v181 cortex-hub bundled GitNexus v33 silently; v265 credited codegraph v70). **Here one repository does both** — a cleaner instance than either.
- **Pattern #18** sub-archetype **B1-MCP** — bundles one MCP server (read-only, and unimportable) and registers a second, third-party one.
- **Pattern #19** 19a (individual, non-Anthropic).
- **Pattern #66** **MIXED→NEGATIVE** — two unpinned third-party fetches (`git clone` + `pip install git+`), no virtualenv, one of them becoming an executed agent tool.
- **Pattern #83** **SPLIT** — the legality FAQ and the BPC credit are honest-deficiency disclosure; "300+ sites" and "~50 sites" are not.
- **Pattern #12** MIXED.

## NON-CLAIMS

- **NOT Pattern #52.** Star/fork counts are page-stated only (§37.4); `README.md:10-13` embeds shields.io badges. **No velocity verified, none claimed.**
- **NOT a new top-level pattern** (max #85 unchanged).
- **NOT world-first on any axis.**
- **NOT** an instance of #68 (not a collection) or #88 (not an anti-slop ruleset).
- Nothing was installed, no credential created, and **no network request made to any subject-related service.** The only two executions were local: a network-stubbed `fetch_url.sh` reachability probe and a real `package.sh` run into a scratch directory.

## The five findings, one line each

1. ⭐⭐⭐⭐ **Every defect in the repository had a fix in an open pull request.** PR #1 (Hanson Mei, 2026-01-26 — *the day after the initial commit*) added a virtualenv, fixed `"command": "python"` → the venv interpreter, dropped `markitdown[all]`, restructured `SKILL.md`, and later added bilibili with a written graceful-degradation clause. PR #3 offered the project's **only 201 lines of tests**. PR #5 offered 6 lines to stop it crashing on Windows. **None merged.** The maintainer then rebuilt bilibili from scratch 82 days later on a worse foundation. PR #1 carries `Co-Authored-By: Claude Opus 4.5`.
2. ⭐⭐⭐ **Two of six documented cascade levels cannot execute** — `fetch_url.sh:351` is a top-level unconditional `exit 75`. **Proved by running it** with the network stubbed: three input classes, all exit 75, Level 5 / Level 6 markers never printed. And `agent-fetch`, the dead Level 6, is one of only three stages `SKILL.md:24` names for the X/Twitter path.
3. ⭐⭐⭐ **The share-this-skill script distributes no code.** `package.sh`'s `FILES` array was a complete manifest of the repository on 2026-01-25 and has never been amended. **Ran it**: 6 files out, 14 of 20 absent — including `LICENSE` (stale within 5 minutes of the licence being committed), `main.py`, and both `scripts/`.
4. ⭐⭐⭐ **The wrapper is more autonomous than the tool it wraps.** v7's bundled skill requires confirmation for expensive (`generate *`), filesystem (`download`) and destructive operations — a boundary the vault's own v7 page called *"mirror-able… for agent skill design generally."* Greps of all 742 lines of this `SKILL.md` for confirmation language return **one** hit, and it is a default, not a gate; for cost/quota language, **zero**.
5. ⭐⭐⭐ **A flag parsed and discarded in the exact command both manuals print.** `--to-feishu` is honoured only on the `url` path; the four `deep_analysis` call sites at `main.py:339/356/393/442` all omit it. Both `README.md:393` and `SKILL.md:290-291` give the **EPUB** form. The run prints `✅ 分析完成！` and creates nothing.

## Pilot

**⭐ READ-AND-BORROW — do not install.** The licence is permissive and the author transparent; the reason to decline is that the documented install path assembles a Playwright session of your real Google account, an unpinned third-party MCP server executed by Claude, a hand-extracted 90-day commercial JWT, and a Google-crawler-impersonating fetcher — behind a skill with no confirmation gate. **And the one capability worth having, corpus v7 already ships properly.**

Full ladder in the Deep Dive §15 and in `(C) Pilot Methods Menu.md`. Headline: **Rung 1 is about this vault** — `main` is at v226 and **45 commits / 41 ships (v227→v265) are unmerged**, while the standing next-action still says *"merge the chain v204 → …"* though v204–v226 are already in. Same defect as `package.sh`, different filename.

## The sentence

**The code here is better than its documentation, and its documentation is better than its process.** Five ships have now examined gates — the claim with no test, the gate that cannot fail, the test with no gate, the gate that skips and says so, the gate that is wired and never invoked. v265 concluded that a discipline stops wherever the safe choice would cost something. **v266 is the cheaper failure: the discipline was already written and reviewed-ready, sitting in a diff on the same remote, and the door was never opened** — ten minutes of review against three months of duplicated work, a repository with no tests, and a contributor who wrote four commits and got silence.
