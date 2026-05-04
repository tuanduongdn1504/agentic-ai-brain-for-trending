# (C) Cluster — luongnv89 ecosystem + VN-diaspora archetype

> **Cluster 3** of 3 — Author attribution: luongnv89 GitHub profile + 20 top companion repos + inferred ecosystem portfolio.
> **Source:** GitHub API `/users/luongnv89` + `/users/luongnv89/repos`, fetched 2026-04-22.

## 1. Author profile (verbatim)

GitHub API:
```json
{
  "login": "luongnv89",
  "name": "Luong NGUYEN",
  "company": "https://montimage.com",
  "blog": "https://luongnv.com",
  "location": "Paris, France",
  "email": null,
  "bio": "Software Engineer\r\n/ AI, Cybersecurity\r\n/ Learn, Build, Share and Connect",
  "twitter_username": "luongnv89",
  "public_repos": 116,
  "public_gists": 17,
  "followers": 642,
  "following": 20,
  "created_at": "2013-01-16T18:42:20Z"
}
```

**Key observations:**
- **Name:** "Luong NGUYEN" — Vietnamese naming (surname Nguyễn). Confirmed VN-authored.
- **Location:** Paris, France — **VN-DIASPORA** (distinct from codymaster/Tody Le's HCMC-in-VN).
- **Company:** Montimage (montimage.com) — French cybersecurity firm specializing in network monitoring + AI-driven traffic analysis. Luong is Software Engineer in AI + Cybersecurity domain.
- **Blog:** luongnv.com (personal site)
- **Twitter:** @luongnv89
- **Medium:** medium.com/@luongnv89 (per README "Additional Resources")
- **GitHub age:** Since Jan 2013 — 13+ years on platform, predates Claude Code era
- **Followers:** 642 — moderate individual-dev profile
- **Public repos:** 116 — ecosystem-layer individual signal (comparable to safishamsi at penpax.ai; lower than Anthropic-scale)
- **Bio tagline:** *"Learn, Build, Share and Connect"* — pedagogical value alignment visible

## 2. Companion repos inventory (15 repos with significant activity)

Sorted by star count, Jan 2026-Apr 2026 activity (most recent 20 repos):

| Repo | Stars | Lang | License | Created | Description |
|------|-------|------|---------|---------|-------------|
| `claude-howto` | 28,186 | Python | MIT | 2025-11-07 | The wiki subject |
| `asm` | 214 | TypeScript | MIT | 2026-03-11 | **Universal skill manager for AI coding agents** |
| `sleek-ui` | 111 | TypeScript | Other | 2026-03-26 | **Unsplash of design systems for AI agents** |
| `context-stats` | 92 | Python | MIT | 2025-12-28 | **Understand how you use Claude Code, spend less doing it** |
| `music-cli` | 61 | Python | MIT | 2025-12-29 | Command-line music player with AI-generated music |
| `skills` | 58 | Python | MIT | 2026-02-03 | **Supercharge AI agents with reusable skills** |
| `vscode-markdown-preview` | 15 | TypeScript | MIT | 2026-02-17 | Zed-inspired VS Code markdown preview |
| `ccl` | 11 | Python | MIT | 2026-04-09 | **Hit your limit? Swap the model** |
| `vibe-coding` | 6 | — | — | 2025-04-25 | **A living repository for vibe coders** |
| `yt-search-lib` | 5 | JS | MIT | 2026-01-12 | Client-side YouTube search without API key |
| `custats-feedback` | 2 | — | Other | 2026-01-04 | **Feedback repo for CUStats macOS menubar** |
| `unsloth-mlx` | 1 | — | Apache-2.0 | 2026-01-20 | **Bringing Unsloth to Mac via Apple MLX** |
| `luongnv89` (profile) | 1 | — | MIT | — | Personal special repo |
| `cv` | 1 | — | MIT | — | Personal CV |
| `better-shot` | 0 | TS | BSD-3 | 2026-01-13 | Screenshot editor (free, local, no account) |
| `App-Store-Connect-CLI` | 0 | Go | MIT | 2026-03-17 | CLI for App Store Connect API |
| `vscode-theme-neon-green` | 0 | JS | MIT | 2026-03-10 | VS Code theme |
| `textwiz-feedback` | 0 | — | Other | 2026-04-11 | **Feedback repo for TextWiz macOS menubar** |
| `asm-registry` | 0 | — | — | 2026-03-29 | **Skill registry for asm** |
| `luongnv89.github.io` | 0 | TS | — | 2015-04-02 | Personal website |

**Total tracked stars across portfolio:** ~28,775 (claude-howto dominant at 28,186).

## 3. Ecosystem clustering — 3 product families

**Family A: Claude Code / AI-agent tooling (6 repos, 28,561 stars combined):**
1. `claude-howto` (28,186) — pedagogical guide (wiki subject)
2. `asm` (214) — universal skill manager for AI coding agents
3. `skills` (58) — reusable skills library
4. `asm-registry` (0) — skill registry
5. `context-stats` (92) — Claude Code usage analytics
6. `ccl` (11) — model-swap helper

**Family A is the primary ecosystem** — Luong has built a coherent Claude-Code-adjacent toolkit: the tutorial (claude-howto) + the skill manager (asm + asm-registry) + the skill library (skills) + the usage analyzer (context-stats) + the model switcher (ccl). Directly analogous to:
- **Fiegel (awesome-mcp-servers v31 author)** — awesome-mcp-servers directory + awesome-mcp-clients companion + fastmcp framework + mcp-proxy + Glama commercial product
- **safishamsi (graphify v16 author)** — graphify + penpax.ai commercial product
- **Yeachan Heo (OMC v27 author)** — oh-my-claudecode + oh-my-codex sibling

Luong fits **Pattern #17 variant 1** (individual-led developer with ecosystem portfolio). Distinct from:
- Variant 2 (big-tech curator: Anthropic, Vercel)
- Variant 3 (commercial-startup: VoltAgent)
- Variant 4 (ecosystem-scale-commercial: HuggingFace, Microsoft)

**Family B: Design + UI tooling (2 repos, 111 stars):**
7. `sleek-ui` (111) — design systems for AI agents
8. `vscode-markdown-preview` (15) — markdown preview extension
9. `vscode-theme-neon-green` (0) — theme

**Family C: Developer utilities (7 repos, 69 stars):**
10. `music-cli` (61) — CLI music player with AI music
11. `ccl` (11) — model swap (dual-classified A + C)
12. `yt-search-lib` (5) — YouTube search library
13. `better-shot` (0) — screenshot editor
14. `App-Store-Connect-CLI` (0) — App Store automation
15. `unsloth-mlx` (1) — Unsloth on Mac MLX
16. `vibe-coding` (6) — vibe-coding repo

**Family D: Commercial products (indirectly, via feedback repos):**
- `custats-feedback` (2) — CUStats macOS menubar (monitors Claude AI usage) — commercial product inferred
- `textwiz-feedback` (0) — TextWiz macOS menubar AI assistant — commercial product inferred

**Commercial model:** Luong publishes free OSS (Family A/B/C) + commercial macOS menubar apps (CUStats, TextWiz — closed-source with public feedback repos). Similar to:
- **Fiegel (awesome-mcp-servers v31)** — OSS directory + Glama commercial platform
- **VoltAgent (awesome-design-md v25)** — OSS repo + getdesign.md commercial
- **NEW in corpus:** Luong's commercial model = **closed-source macOS apps + feedback-only public repos + OSS companion tools**

**Pattern #50 Commercial-Funnel Companion Platform** (CONFIRMED v31, N=2 VoltAgent + Glama):
- 3rd data point CANDIDATE — Luong's CUStats + TextWiz are structurally distinct (closed-source apps with feedback-only repos, vs VoltAgent/Glama web platforms that are open/public-facing). Arguably NOT same pattern. **Decision: Luong's model is adjacent-but-different; register as observation but NOT Pattern #50 strengthening.** Future wiki may establish new candidate for "closed-commercial-product + OSS-companion-tool" archetype if repeats.

## 4. Cross-corpus reference: `unsloth-mlx`

`luongnv89/unsloth-mlx` repo (Apache-2.0, 1 star, 2026-01-20):
> *"Bringing the Unsloth experience to Mac users via Apple's MLX framework"*

**CROSS-CORPUS connection:** Unsloth is Storm Bear corpus v23. Luong is consumer/porter of Unsloth v23's training infrastructure onto Apple Silicon. This is:
1. **Evidence of Luong as corpus-familiar individual** — he's aware of Unsloth (top training-infra framework)
2. **1-star repo** — early experimental port, not mature product, but signals technical breadth
3. **Apache-2.0 vs claude-howto's MIT** — Luong respects upstream license conventions (Unsloth dual-license Apache + AGPL per v23 wiki)

**Novel corpus observation:** This is the SECOND recursive corpus-adjacent linkage in Storm Bear history. First was OMC v27 citing v1 + v2 (recursive corpus reference — Pattern #57 N=1 at v27). However, v32 is structurally different: Luong hasn't CITED Unsloth in claude-howto README; he has CODED a derivative/port repo (`unsloth-mlx`). This is **corpus-latent** not **corpus-explicit** — he's working with Unsloth outside this wiki. Pattern #57 NOT un-staled by claude-howto (no citation).

## 5. Blog integration — Medium-pipeline

README §"Additional Resources" cites Medium blog pipeline:
- **Blog:** https://medium.com/@luongnv89
- **Learning References:** Individual Medium posts linked per module:
  - Slash Commands module → "Discovering Claude Code Slash Commands" Medium post (URL: cdc17f0dfb29)

**Corpus-first:** Medium-blog-integrated learning pipeline. No prior T1 framework in corpus explicitly links to external blog for each module. Demonstrates Luong's content strategy: GitHub repo = canonical + copy-paste templates; Medium = long-form narrative explanations; they reinforce.

**Pattern observation:** Multi-channel content distribution (GitHub + Medium + personal blog + Twitter + feedback repos) = novel at T1. Most T1 authors concentrate on GitHub. Luong's multi-channel approach may partly explain the 28K star acquisition in 5.5 months — he funnels Medium readership to GitHub.

## 6. Origin story + timing

- **claude-howto created 2025-11-07** — approximately 2 months after Claude Code's broader public rollout (September-October 2025)
- **`skills` repo created 2026-02-03** — followed claude-howto by ~3 months (cross-reference in claude-howto README)
- **`asm` repo created 2026-03-11** — followed by ~4 months
- **Monotonic ecosystem expansion** — Luong builds progressively:
  1. Tutorial (claude-howto, 2025-11-07) →
  2. Skill library (skills, 2026-02-03) →
  3. Skill manager (asm, 2026-03-11) →
  4. Skill registry (asm-registry, 2026-03-29) →
  5. Related companions (sleek-ui, ccl, context-stats)

**Observation:** Luong's ecosystem is SELF-REFERENTIAL — each new repo solves a problem exposed by the prior. Mature ecosystem-individual pattern at N=1 for this specific structure ("tutorial → library → manager → registry" cascade). May be generalizable but too early.

## 7. VN-diaspora vs VN-in-VN distinction

**codymaster v12 (Tody Le):**
- **Location:** Ho Chi Minh City (implied by VN-primary content + VN-first README)
- **Audience:** VN developers directly; VN-first pedagogy
- **Framework philosophy:** "Code Đi" (Go code!) — VN tagline
- **Product:** codymaster (vibe-coding framework with 79 skills)
- **Ecosystem:** codymaster + tody-agent organization
- **Pattern #17 fit:** individual-led-dev (variant 1) with organizational brand

**claude-howto v32 (Luong Nguyen):**
- **Location:** Paris, France (VN-diaspora)
- **Audience:** Global developers; EN-primary with VN+CN+Ukrainian ports
- **Framework philosophy:** "Master Claude Code in a Weekend" — global-English tagline
- **Product:** claude-howto (pedagogical guide with 45 templates)
- **Ecosystem:** claude-howto + asm + skills + asm-registry + context-stats + ccl (tool cluster)
- **Pattern #17 fit:** individual-led-dev (variant 1) with ecosystem portfolio

**Common VN-Regional-Archetype traits (N=2):**
- Solo authorship
- AI-agent/Claude-Code-specific framework
- T1 tier (Agent-as-assistant)
- MIT license
- Technical depth in AI/ML domain
- VN-language README (though claude-howto's VN README is thin)

**Distinctions (sub-variants of VN-Regional-Archetype):**
- **VN-in-VN sub-variant** (codymaster v12): VN-primary audience + VN-first README + VN tagline + local ecosystem
- **VN-diaspora sub-variant** (claude-howto v32): Global audience + EN-primary README + global tagline + multi-channel blog ecosystem

At N=2, VN-Regional-Archetype T1 pattern is **structurally unambiguous** (both satisfy N=2 promotion-candidate criteria) with 2 clear sub-variants. Proposed Pattern #70.

## 8. Sub-variant prediction

**If Pattern #70 VN-Regional-Archetype T1 promotes at v33+ audit:**
- N=2 structurally-unambiguous promotion path (per routine v2.1 criterion 2)
- Pattern cross-references Pattern #55 Korean Regional Archetype (still N=1 at v32)
- If 3rd Korean T1 appears: meta-pattern Regional-Archetype-Registry T1 consolidation candidate

**Prediction:** VN OSS community has growing AI-developer cohort (Tody Le + Luong + diaspora). 3rd VN T1 plausible within 5-10 wikis. Meta-pattern emergence at v35-v40 range.

## 9. Pattern #20 Solo-Scale Ceiling — dictionary row addition

Current dictionary (8 rows at v21 reformulation):
| Archetype | Observed ceiling | Evidence |
|-----------|------------------|----------|
| Solo narrow single-service | 100-1,000 | notebooklm-py v7 (~300) |
| Solo medium single-platform | 5-10K | ECC v1 (~5K), Superpowers v2 (~8K) |
| Solo broad multi-platform | ~30K | graphify v16 (30K) |
| Solo broad external regional | ~50K | TrendRadar v19 (52.1K CN) |
| Solo massive multi-platform viral | ~80K | agency-agents v18 (82.9K Reddit) |
| Solo aggregator + crypto + zeitgeist | ~135K+ | system-prompts-leaks v21 (135.5K) |
| Corporate multi-platform community | ~90K+ | spec-kit v17 (89.2K GitHub/Microsoft) |
| Outside-scope long-term aggregator | 491K | build-your-own-x v8 (10+ years) |

**Proposed v32 dictionary row:**

| Archetype | Observed ceiling | Evidence |
|-----------|------------------|----------|
| **Solo pedagogical-tutorial + ecosystem-portfolio** | **~28K (5.5 months)** | claude-howto v32 |

This sits BELOW solo-broad-multi-platform graphify v16 (30K) — similar ceiling, different domain. **NOT major revision — just new row.** Preserves pattern's v21 reformulation discipline.

## 10. Corpus-first observations from Cluster 3

1. **1st VN-diaspora-authored T1** (Luong Paris-France, distinct from codymaster VN-in-VN)
2. **VN-Regional-Archetype T1 N=2** candidate promotion-ready (proposed Pattern #70)
3. **Individual-led ecosystem-portfolio with closed-commercial-companion** model (CUStats + TextWiz macOS apps + feedback-only public repos)
4. **Corpus-latent cross-reference** — Luong's `unsloth-mlx` repo bridges to Unsloth v23 without citation in claude-howto (novel "corpus-latent" vs Pattern #57 "corpus-explicit")
5. **4-family ecosystem clustering** — Claude-tooling (6 repos) + design-UI (3 repos) + dev-utilities (7 repos) + commercial-feedback (2 repos)
6. **Self-referential ecosystem expansion cascade** — tutorial → library → manager → registry
7. **Multi-channel content distribution** — GitHub + Medium + personal blog + Twitter + 4-language README
8. **AI + Cybersecurity domain signature** (Montimage affiliation) — first corpus T1 author from cybersecurity firm
9. **13-year-GitHub-tenure** individual with 116 public repos — senior OSS profile
10. **~28K stars in 5.5 months at T1** = ~5,100 stars/month sustained Community-Viral Scale Path (Pattern #27 8th data point, VN-diaspora sub-variant)
11. **unsloth-mlx licensed Apache-2.0** (not MIT) — respects Unsloth v23's Apache-2.0 upstream license (license-awareness signal)
12. **`vibe-coding` repo** — Luong self-identifies with vibe-coding spectrum; Pattern #51 Vibe-Coding Spectrum implicit pro-pole data point (though claude-howto itself is pedagogical-structured, not pure vibe)
