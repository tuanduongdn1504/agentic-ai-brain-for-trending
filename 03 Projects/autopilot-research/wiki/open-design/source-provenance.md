# Source provenance — the verified-vs-corrected ledger

## How this topic was built

- **Primary source:** YouTube `QOqWZzecjuY` (CodingMenace, "Open Design in 20 Minutes"), captured via `yt-dlp` English auto-subs → deduped **~4,200-word** transcript (`raw/2026-07-01-open-design.md`), **read in full** by the main loop. No NotebookLM. A **third-party first-impressions demo**, not a first-party source.
- **Originals deep-dive + adversarial verification:** Workflow **`wf_4a91a8b2-2bb`** — **13 agents** (8 original/main deep-dives → 3 adversarial skeptics + 1 hireui-application → 1 synthesis critic), ~633K subagent tokens, 219 tool calls, ~8.5 min. Each agent re-fetched primary sources (`gh api` + WebFetch) rather than trusting the video.
- **Operator ground-checks:** direct `gh api` on all 10 repos; **WebFetch of the Anthropic Claude Design announcement** + WebSearch (TechCrunch/VentureBeat/DataCamp) to settle the load-bearing premise; `yt-dlp --dump-json` + subtitle pull for the video.
- Honors autopilot-research constitutional rule #4 (never fabricate) and Storm Bear Rule 12 (fail loud).

## The load-bearing premise — settled

**Is "Claude Design" a real Anthropic product?** → **YES (HIGH confidence).** [anthropic.com/news/claude-design-anthropic-labs](https://www.anthropic.com/news/claude-design-anthropic-labs): Anthropic Labs, launched **2026-04-17**, research preview, **Opus 4.7**, cloud-only (claude.ai/design), **Pro/Max/Team/Enterprise** subscription-gated, reads codebase+Figma. Corroborated by TechCrunch + VentureBeat + DataCamp. Open Design (2026-04-28) is the **11-days-later** open alternative.

## Critic over-flag — overridden (independently check identity claims)

The workflow's **synthesis critic scored the dossier 5.5/10** and made **"Claude Design existence not verified against Anthropic sources"** its **CRITICAL #1** correction — even though the dedicated `claude-design-product` agent **had** verified it via the Anthropic URL. The critic was working from a truncated dossier slice and defaulted to skepticism. **Overridden** by the operator's own WebFetch + 3 independent outlets. This is the same failure mode logged elsewhere in the vault (a verifier calling Sand Castle "fabricated" because it couldn't reach GitHub; verifiers grepping the local FS instead of the repo). **Lesson reaffirmed:** when a verifier declares something unverifiable, check whether *it* just couldn't reach the source before believing the negative.

## Name corrections (auto-caption manglings)

The video's auto-captions mangle every non-English name:

| Video says | Actually |
|---|---|
| "Cloud Design" | **Claude Design** (auto-caption hears "Claude" as "Cloud" throughout) |
| "Huashu design" | **`alchaincyf/huashu-design`** (花叔 / huā-shū) |
| "Wizeng PPT" / "Guizhong PPT" | **`op7418/guizang-ppt-skill`** |
| "Kami" / "the daemon runtime … path-scan agent detection" | **`multica-ai/multica`** |
| "Open Cowork AI's open code design" / "opencode design" | **`OpenCoworkAI/open-codesign`** |
| "npm tools dev" | `npm run dev` (video) → now **`pnpm tools-dev run web`** (current docs) |

## Corrections vs the video / README (verified against primary sources)

| Claim | Status | Reality |
|---|---|---|
| guizang-ppt bundled copy is "MIT" (README lineage) | ⚠️ **conflict** | Upstream `op7418/guizang-ppt-skill` is **AGPL-3.0** (gh api + LICENSE). Verify the bundled `LICENSE` before trusting "MIT." |
| multica is open-source | ⚠️ **NOASSERTION** | No recognized license; no clear reuse grant. |
| "No telemetry, no cloud round-trip" | ⚠️ **imprecise** | Opt-in **PostHog**, no-op unless `POSTHOG_KEY` set + user setting; metadata-only if enabled. |
| "Per-target SSRF protection" | ⚠️ **unconfirmed in code** | A skeptic found no IP-filtering in the HTTP adapter; loopback-only default is the real mitigation. |
| "261 plugins / 100+ skills / 150 systems / 21 agents" | ⚠️ **moving / undercounted** | Dir enumeration ~440+ items / ~159 skills / ~152 systems; 15 named agents (21 in hero). Counts rise weekly. |
| Video "27K stars", "31 skills / 72" | **point-in-time (2026-05-05)** | Now **73,468★** (gh api 2026-07-01); numbers don't match. |
| open-design is "the first" OSS Claude Design alternative | ✅ **corrected in README itself** | `open-codesign` (2026-04-18) is first, 10 days earlier; open-design credits it. |
| DESIGN.md 9-section schema identical to VoltAgent's | ⚠️ **two different lists** | Open Design **adapted** VoltAgent's schema; the two 9-section enumerations differ. |
| HyperFrames integration | ⚠️ **README-described, not code-audited** | Real repo (heygen-com, Apache-2.0, 32K★); integration into open-design not diff-verified. |
| Claude Design `.zip` import | ⚠️ **video + landing page only** | Not found in repo QUICKSTART/docs — real-but-undocumented or evolved. |
| Creative-media providers (Suno/MJ/ElevenLabs/GPT-image/MiniMax) | ⚠️ **single-source (video + hero alt-text)** | BYOK proxy docs enumerate only OpenAI/Anthropic/Azure/Google/Ollama/senseaudio. |

## Verified-accurate (HIGH confidence, gh api 2026-07-01)

- `nexu-io/open-design`: **73,468★**, 8,348 forks, **Apache-2.0**, TypeScript, created **2026-04-28**, latest **v0.12.0** (2026-06-26); org `nexu-io` created 2026-02-24 (18 repos, 1,233 followers).
- Architecture: Node 24 · Express · SSE · `better-sqlite3` daemon; binds **127.0.0.1**; adapter contract `detect()/capabilities()/run()` in `apps/daemon/src/agents.ts`; BYOK proxy `/api/proxy/{anthropic,openai,azure,google,ollama,senseaudio}/stream`; `SKILL.md` + `od:` frontmatter; `DESIGN.md` (color/typography/spacing/layout/components/motion/voice/brand/anti-patterns); `execFile` (no shell); creds `config.toml` 0600.
- Originals (★/license/created): huashu-design 20,457 / MIT (→MIT 2026-05-14) / 2026-04-19 · open-codesign 7,023 / MIT / 2026-04-18 (v0.2.1) · multica 38,621 / NOASSERTION / 2026-01-13 · guizang-ppt 19,554 / **AGPL-3.0** / 2026-04-23 · html-ppt 6,713 / MIT / 2026-04-15 · awesome-design-md 94,742 / MIT / 2026-03-31 · awesome-design-skills 1,482 / MIT / 2026-03-09 · hyperframes 32,398 / Apache-2.0 / 2026-03-10.
- Star velocity **assessed organic** (smooth curve, 30 named contributors, <2% bots, healthy fork/issue ratios) + a disclosed **$1,000/MR "Fellows"** accelerant.

## Don't-re-fabricate quick list

1. **Claude Design is REAL** (Anthropic Labs, 2026-04-17, Opus 4.7, cloud, Pro/Max/Team/Enterprise). The critic's "unverified" flag was wrong — overridden.
2. **`open-codesign` is the real "first"** (10 days earlier); open-design is the bigger sibling that credits it.
3. **guizang-ppt = AGPL-3.0** upstream (README's "MIT" for the bundled copy conflicts — verify). **multica = NOASSERTION.**
4. **"No telemetry" = opt-in PostHog (off by default); "SSRF protection" = unconfirmed in code** — loopback is the real defense.
5. **Counts are marketing/moving** — cite live `gh api` stars with a date; the video's 27K/31-skills are stale.
6. **Names:** Claude (not "Cloud"); `alchaincyf/huashu-design`; `op7418/guizang-ppt-skill`; `multica-ai/multica`; `OpenCoworkAI/open-codesign`.
7. Install is **pnpm now** (`corepack enable && pnpm install && pnpm tools-dev run web`), not the video's npm.
8. Flag as **not-code-verified:** HyperFrames integration, `.zip` import, creative-media providers, multica architectural debt.
