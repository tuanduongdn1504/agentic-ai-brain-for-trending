# (C) Codex-Dream-Skin — Deep Dive (v216)

> **Wiki ship v216 · 2026-07-18 · operator-requested** ("build LLM wiki for `https://github.com/Fei-Away/Codex-Dream-Skin`")
> **Verdict headline: ⚠️ OFF-GOAL (recorded as OFF-GOAL CAPTURE) — a cosmetic wallpaper/skin for OpenAI's Codex *Desktop* app. Off both goals. NO MINT. Counts 46/11 UNCHANGED.**
> Produced **inline + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` (no workflow / no subagent — the ~205K shim overflows subagent context → prompt-too-long, the v200→v215 self-throttle). Source hand-fetched (repo page + raw README.md + README.en.md + macos/README + landscape); identity + the OpenAI-Codex-not-Anthropic correction + the populated-genre landscape by WebSearch; collision by sanity-anchored hand-grep (0 subject hits).

---

## 1. What it is — in one blunt sentence

`Fei-Away/Codex-Dream-Skin` is a **cosmetic theming tool** that paints a **custom background wallpaper** onto the **OpenAI Codex *Desktop* app**'s window — via **local Chrome-DevTools-Protocol (CDP) injection** — while keeping the app's native controls interactive and without patching any official binary. Its own tagline: *"给 Codex 桌面端换一张会呼吸的脸"* — **"give the Codex desktop a breathing new face."**

It does **not** touch code, agents, prompts, models, API keys, or provider settings. It is a **skin**. The corpus is cataloging it because you asked; the honest verdict is that it is **off both of your goals** (master Claude & autonomous agents for software development; and hireui).

## 2. Identity — hand-verified

| Field | Value | Source / note |
|---|---|---|
| Repo | `Fei-Away/Codex-Dream-Skin` | operator URL |
| What it themes | **OpenAI Codex *Desktop* app** (the ChatGPT/Codex desktop client) | ✅ **corrected** — one summarizer conflated this with "Anthropic's Claude desktop." The repo name, the tagline (给 **Codex** 桌面端), the peer tool `heige-codex-skin-studio` ("OpenAI Codex/ChatGPT 桌面端"), and the press wire all say **OpenAI Codex Desktop**. The "Anthropic" phrasing was a small-model artifact from the README's boilerplate "not affiliated with OpenAI **or** Anthropic" disclaimer. |
| Author | **`Fei-Away`** — a **bare GitHub handle**, 1 contributor, Chinese-language primary README | §41: NOT Anthropic; no name/heritage/locale/notability rescue; the disclosed-individual (a)-axis answered NO. #19 19a data-point (first `Fei-Away` author). |
| Sponsor / credits | **Sponsored by passion8.cc**; Gothic design credited to **@seansong-ideogram** | README + press wire |
| License | **MIT** (`macos/LICENSE`) | ✅ |
| Languages | **JavaScript 40.6% / PowerShell 26.0% / Shell 22.7% / CSS 10.7%** | repo page |
| Stars / forks | **~4,808★/564 forks day-one (2026-07-16, press-wire-stated) → ~7.5k–8.9k★ / ~940 forks now (page-stated, sources conflict)** | §37.4 — GitHub API is **mocked** → page-stated only → **NOT a Pattern #52 (viral-velocity) claim**, despite the ~8k-in-3-days shape |
| Created | **2026-07-15** (≈3 days old as of this ship) | press wire (einpresswire, 2026-07-16) |
| Releases | **None published** | repo page |
| Trending | **Trendshift #84043** | page-stated |
| Extras | site `codex-dream-skin.org` + a press release + a knock-off SEO site `codexskins.org` | landscape |
| NOT source-cloned | Verdict rests on repo page + raw README(s) + landscape research | flagged per the v200→v215 self-throttle |

## 3. Mechanism — how the "skin" actually works

The load-bearing technique (the *one* mildly transferable idea in the whole repo):

1. **Codex Desktop is an Electron/Chromium app.** Electron apps expose a **Chrome DevTools Protocol (CDP)** endpoint on a local debug port.
2. The tool **launches / attaches to** the Codex renderer's CDP endpoint on **`127.0.0.1` only** (loopback), *after* Codex is running.
3. Over CDP it **injects CSS + a full-window background image (and DOM tweaks)** straight into the live renderer — swapping the visuals on the fly.
4. Because it injects into the *running renderer*, it **never modifies** `.app` / `app.asar` / `WindowsApps` / code signatures / official install dirs — so it is **reversible** (one-click restore to stock) and survives without repackaging the app.
5. The sidebar, suggestion cards, project picker, and composer stay **native, interactive controls** — "route-aware translucency" keeps home/task/plugin/scheduled-task/PR surfaces readable. It is a wallpaper *beneath* the real UI, not a fake overlay.

Delivery:
- **macOS:** double-click `macos/Install Codex Dream Skin.command`; theme store + switching via a **menu-bar** item.
- **Windows:** `scripts/install-dream-skin.ps1` then `start-dream-skin.ps1`; persistent local theme store + **system-tray** controls.

It ships **preset wallpapers** ("Gothic Void Crusade" = default macOS; "Arina Hashimoto"; "romantic-rose") + support for user-supplied 16:9 backgrounds (scaled to 2560×1440, auto focus/color adjust) + AI-prompt guides for generating your own backgrounds. ⚠️ The presets skew toward **anime / gravure-style waifu wallpapers** — a taste/appropriateness note if it's ever anywhere near a work machine or a shared screen.

Explicit non-goals (stated by the project): does **not** modify official binaries/signatures, does **not** rewrite API Key / Base URL / provider settings, CDP is loopback-only.

## 4. The decisive landscape fact — this is a *genre*, not a one-off

Codex-Dream-Skin is the **most-viral instance of a small, populated genre** of "skin the Codex Desktop via CDP injection" tools that all appeared around the same window:

- **CodeDrobe** — a peer toolkit, same CDP-attach-and-inject-CSS mechanism, macOS + Windows, "no files touched."
- **HeiGeAi/heige-codex-skin-studio** — "一键换肤 / One-click theme & skin switcher for OpenAI Codex Desktop," **9 presets** (Miku / 原神 / 鸣潮 / 火影 / 恋与深空), CDP-inject-zero-modification, custom-image color extraction.
- **mcpso/awesome-codex-themes** — an *awesome-list* cataloging the genre (the genre is big enough to have its own awesome-list).
- **Codex Desktop's own native appearance customization** — shipped **late March 2026** (base theme + accent/ink/surface colors + fonts + semantic diff colors), with themes traveling as portable `codex-theme-v1:{...}` JSON imported via Settings → Appearance.

→ Codex-Dream-Skin is **NOT world-first** and **NOT a novel capability**. It's the prettiest / most-starred wallpaper painter in a crowded lane. This is the load-bearing input to the NO-MINT decision.

## 5. Substance (c) — MODERATE, honestly

Real: a working, cross-platform, reversible, non-invasive CDP-injection tool with a genuine local theme store, menu-bar/tray UX, and ~8k stars in 3 days. But **shallow**: the "hard part" is CSS + image injection over a well-known protocol; there is no novel engineering, no agent, no model, no algorithm. Caveats: NOT source-cloned; star count page-stated + conflicting (4.8k/7.5k/8.9k) → not #52; the day-one "4,808★ in 27h" figure comes from a **self-published press wire** (einpresswire) → promotional, unverified; the aesthetic is niche/anime-gravure.

## 6. Why it's OFF-GOAL — the load-bearing (b) judgment

Your Goal #1 is *"master Claude and autonomous agents for software development."* Goal #2 is hireui. Codex-Dream-Skin:

- ❌ is **not Claude** (it themes OpenAI's Codex);
- ❌ is **not an agent, agent infrastructure, or a coding tool** (it changes zero about how you code — it paints the window);
- ❌ ships **no model, no skill, no methodology, no LLM/agent architecture** to learn from;
- ❌ has **nothing to pilot into hireui** (a recruitment SaaS doesn't want an anime wallpaper injector).

The corpus's **(b) MODERATE floor** has been held by subjects with a *real architectural/substrate hook* — GLM-5 v176 (a competitor frontier model = the engine agents run on), AIRI v210 (a provider-agnostic 30+-LLM seam), geti v213 (a first-party agent-skill suite), meetily v196 (a 7-provider vendor-seam). Codex-Dream-Skin has **none of those**. Its only two threads to the goal are thin:

1. **Ecosystem-adjacency** — it operates on the Codex Desktop app, a Claude-Code *competitor* the corpus tracks (grok-build v215 is Codex's vendor peer). But it's a *cosmetic accessory* to Codex, not Codex, not a capability.
2. **The CDP-injection technique** — attach to an Electron AI-tool's `127.0.0.1` CDP endpoint and inject CSS/DOM without patching binaries. Real and transferable (the same *class* of technique underlies instrumenting/augmenting an Electron AI client — the claude-tap v173 observability thread, the page-agent v199 in-page-agent thread), but here it is used purely for **wallpapers**, and CDP injection is well-known.

Neither lifts the **subject** above (b) FAIL. **The subject is a wallpaper skin. (b) FAILS. → OFF-GOAL.**

## 7. Pattern outcome — NO MINT

- **NOT a new top-level pattern** (max stays #85).
- **NO §C standalone.** "Cosmetic desktop-app theming/skinning via CDP injection" is **not a mintable agent-capability class** (§C vocab is agent-capability/tool-shaped — the meetily v196 / TimesFM v193 / geti v213 domain-not-capability discipline). It is also **NOT world-first** (CodeDrobe / heige-codex-skin-studio / awesome-codex-themes / Codex-native-themes). A "corpus-first cosmetic-theming" mint would be exactly the §28 phantom-count inflation the routine fights — on an off-goal, non-world-first, cosmetic subject → **DECLINED**. Recorded as a **corpus-knowledge data-point + a DEFERRED watch axis** ("cosmetic/wallpaper customization of AI-coding-tool desktop clients via CDP injection") only if a 2nd such subject ever warrants a subject-slot — honestly, this axis is off-goal enough that it barely merits a watch.
- **SECONDARY (NOT minted):** #19 19a first `Fei-Away` author · **CDP-injection technique cross-ref** (the one transferable idea — cousins: camofox v179 fingerprint-injection, opencode-antigravity-auth v67 credential-injection, page-agent v199 in-page DOM, claude-tap v173 renderer/traffic observation) · **Codex-ecosystem landscape** (grok-build v215 = Codex's vendor peer; DeepSeek-TUI v72; larksuite v143; Kilo Code v177) · **#66** (real: CDP on 127.0.0.1 = a local debug surface any co-resident process can also attach to, "avoid untrusted local processes while the theme runs"; `.command`/`.ps1` install scripts; + the anime/gravure preset content = a taste/appropriateness note, not a security one).
- **NON-claims:** NOT #52 (page-stated §37.4, conflicting stars, press-wire velocity) · NOT #57 (cites no corpus subject) · NOT #18 B1-MCP (no MCP server — the "CDP" in codegraph v70's Pattern-#18 taxonomy is a *code-data-plane protocol variant*, unrelated to Chrome DevTools Protocol) · NOT world-first · NOT corpus-first for a mintable class · NOT source-cloned (flagged).

## 8. ⚠️ Reviewable alternative (operator's call)

If you elect the two thin hooks (the CDP-injection technique + the Codex-ecosystem landscape) as **(b) MODERATE**, then **routine v2.7 §40** (operator-requested goal-adjacent → GA-per-direction) would flip this to **GOAL-ALIGNED**, the streak would continue **GA:75 → GA:76**, and OFF-GOAL would become the reviewable alternative. On the merits I record it the other way (OFF-GOAL primary), because §40 itself carves out *"truly off-everything subjects still use OFF-GOAL CAPTURE"* and a wallpaper skin is much closer to that than the geti/AIRI/meetily cohort was. **Say the word and I'll flip the tag** — but I'd recommend saving your build cycles for on-goal subjects.

## 9. Tier & counts

- **Tier T5 Application** (a cosmetic desktop-app customization utility — the off-goal-utility flavor).
- Counts UNCHANGED **46/11**; §C live standalones **44** unchanged; §C surface **≈51** unchanged.
- Streak: the 61-consecutive-GA run (v153→v215) **breaks** here → **GA:75 · OG:12 [7 ov]** (OFF-GOAL CAPTURE, operator-requested — *no override consumed*, this is the intake-channel capture track). ⚠️ Under the §40 GA-per-operator-direction reading → GA:76, streak continues.
- **§35 CLEAR** — window {v214 GA, v215 GA, **v216 OG**} = 1 OG ≤ 1 → clear (an OFF-GOAL here does **not** breach the soft off-goal-rate ceiling).
