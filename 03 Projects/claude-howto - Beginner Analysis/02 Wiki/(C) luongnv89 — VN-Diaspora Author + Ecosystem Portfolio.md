# (C) luongnv89 — VN-Diaspora Author + Ecosystem Portfolio

> **Entity type:** Distribution/ecosystem entity (author attribution + companion-repo ecosystem)
> **Wiki:** v32 claude-howto
> **Status:** ✅ entity page v1

## 1. Who is luongnv89?

**Full name:** Luong NGUYEN (Nguyễn Văn Lường — Vietnamese surname order would be Nguyễn first)
**GitHub:** `luongnv89` (github.com/luongnv89), since 2013-01-16
**Location:** Paris, France — **VN-DIASPORA**
**Company:** Montimage (montimage.com) — French cybersecurity firm
**Blog:** luongnv.com
**Medium:** medium.com/@luongnv89
**Twitter:** @luongnv89
**Bio:** *"Software Engineer / AI, Cybersecurity / Learn, Build, Share and Connect"*
**Public repos:** 116
**Followers:** 642
**Following:** 20

## 2. VN-Diaspora distinction

| Dimension | Tody Le (codymaster v12) | Luong Nguyen (claude-howto v32) |
|-----------|--------------------------|--------------------------------|
| **Location** | Ho Chi Minh City, Vietnam | Paris, France |
| **Diaspora?** | No (VN-in-VN) | Yes (VN-diaspora) |
| **Audience framing** | VN-first | Global-first |
| **Primary README** | VN-first | EN-first |
| **VN README presence** | Native (primary) | Port (73 lines, 8% of EN) |
| **Tagline** | "Code Đi" (VN) | "Master Claude Code in a Weekend" (EN) |
| **Employer** | Head of Product (VN company implied) | Montimage (French cybersecurity) |
| **Domain signature** | Product-led, AI-coding-framework, no-code background | AI + Cybersecurity engineer |
| **Ecosystem approach** | codymaster + tody-agent org brand | luongnv89 individual with 116 repos |
| **T1 scale** | 38 stars | 28,186 stars |
| **Scale philosophy** | Small + deep (79 skills) | Moderate + broad (10 modules + 45 templates) |

**VN-Regional-Archetype T1 pattern (proposed #70):**
- **VN-in-VN sub-variant** — Tody Le (codymaster) writing for VN audience directly; local ecosystem; VN tagline
- **VN-diaspora sub-variant** — Luong Nguyen (claude-howto) writing for global audience; VN as courtesy port; EN primary

Both satisfy: VN-authored + T1 Agent-as-assistant + MIT + AI-agent-domain + solo-author. Structural N=2 validates pattern promotion via structurally-unambiguous-at-N=2 criterion (routine v2.1 criterion 2).

## 3. Luong's ecosystem portfolio (Pattern #17 variant 1 strengthening)

15 significant repos clustered into 4 families:

**Family A: Claude Code / AI-agent tooling (6 repos, 28,561 stars total)**
- `claude-howto` (28,186) — pedagogical guide
- `asm` (214) — universal skill manager for AI coding agents
- `skills` (58) — reusable skills library (referenced in claude-howto README "Additional Resources")
- `asm-registry` (0) — skill registry for asm
- `context-stats` (92) — Claude Code usage analytics
- `ccl` (11) — model-swap helper ("Hit your limit? Need privacy? Swap the model")

**Family B: Design + UI tooling (3 repos)**
- `sleek-ui` (111) — design systems for AI agents
- `vscode-markdown-preview` (15) — Zed-inspired preview
- `vscode-theme-neon-green` (0) — theme

**Family C: Dev utilities (7 repos)**
- `music-cli` (61) — CLI music player with AI music
- `yt-search-lib` (5) — YouTube search without API key
- `better-shot` — screenshot editor
- `App-Store-Connect-CLI` — App Store automation (Go)
- `unsloth-mlx` (1) — Apache-2.0, **cross-corpus bridge to Unsloth v23 via Apple MLX**
- `vibe-coding` (6) — self-identifies with vibe-coding spectrum

**Family D: Commercial products (feedback-only public repos)**
- `custats-feedback` (2) — CUStats macOS menubar (closed-source; monitors Claude AI usage)
- `textwiz-feedback` (0) — TextWiz macOS menubar AI assistant (closed-source)

## 4. Ecosystem cascade — self-referential expansion

Luong's repos form a cascade where each solves a problem exposed by the previous:

```
claude-howto (tutorial)      → teaches features
    ↓ exposes: need for reusable skills
skills (skill library)       → provides templates
    ↓ exposes: need for management
asm (skill manager)          → installs + manages skills
    ↓ exposes: need for discovery
asm-registry (skill registry) → discovers available skills

context-stats                → measures Claude Code usage
    ↓ exposes: when you hit limits
ccl (model swap)             → handles limits
```

Both cascades = **self-referential ecosystem** where each repo completes a user-pain-point exposed by a prior repo. This is coherent ecosystem-individual pattern — matches:
- **Fiegel (awesome-mcp-servers v31)** — awesome-mcp-servers → awesome-mcp-clients → fastmcp → mcp-proxy → Glama
- **Yeachan Heo (OMC v27)** — oh-my-claudecode → oh-my-codex → (claude-hud → Superpowers citation lineage)
- **safishamsi (graphify v16)** — graphify → penpax.ai

**Pattern #17 variant 1 (individual-led-dev) 8th data point strengthening.**

## 5. Pattern #50 Commercial-Funnel — tangential data point

Pattern #50 Commercial-Funnel Companion Platform (CONFIRMED v31 at N=2: VoltAgent getdesign.md + Glama glama.ai/mcp/servers) requires:
- OSS product has commercial companion PLATFORM
- Platform is web/SaaS-based with revenue mechanism
- OSS and commercial are structurally linked (directory/content-funnel)

**Luong's model is structurally distinct:**
- OSS tutorials (claude-howto) → free forever, no commercial upsell
- Commercial products (CUStats, TextWiz macOS apps) are CLOSED-SOURCE menubar apps
- Feedback-only public repos (`custats-feedback`, `textwiz-feedback`) have no product code
- No cross-linking from claude-howto README to commercial products

**Verdict:** Luong's commercial model = **closed-commercial-macOS-app + separate-OSS-tooling**, NOT commercial-funnel-companion-platform. NOT Pattern #50 3rd data point. Could emerge as novel pattern if 2nd example (closed-commercial-product + OSS-companion-tools decoupled from funnel) appears.

## 6. Cross-corpus observation — `unsloth-mlx` latent linkage

`luongnv89/unsloth-mlx` (Apache-2.0, 1 star, created 2026-01-20):
> *"Bringing the Unsloth experience to Mac users via Apple's MLX framework"*

**Significance:**
- **Unsloth = Storm Bear wiki v23** (training-infrastructure, 62K stars)
- Luong is **consumer/porter** of Unsloth v23 onto Apple Silicon
- **Corpus-latent cross-reference** — Luong hasn't CITED Unsloth in claude-howto; he has DERIVED/PORTED Unsloth
- Distinct from Pattern #57 Recursive Corpus Reference (OMC v27 CITED ECC v1 + Superpowers v2 in README)
- claude-howto itself doesn't reference Unsloth — only Luong's other repo does

**New corpus observation (not new pattern yet):** Corpus-latent cross-reference = authors linked via derivative works, not via citation. Pattern #57 stays at N=1 (corpus-explicit); corpus-latent may become distinct pattern if another author publishes derivative of a corpus wiki's subject.

## 7. Boris Cherny lineage (corpus-first)

README §"Additional Resources":
> *"Boris Cherny's Claude Code Workflow — The creator of Claude Code shares his systematized workflow: parallel agents, shared CLAUDE.md, Plan mode, slash commands, subagents, and verification hooks for autonomous long-running sessions."*

Link: https://x.com/bcherny/status/2007179832300581177

**Boris Cherny** = Anthropic engineer widely credited as creator of Claude Code CLI. First Storm Bear corpus citation of Boris Cherny.

**Pattern #19 Intellectual Lineage Archetypes — archetype 1 (individual-author lineage) data point strengthening:**

Prior individual-lineage touchpoints (5 touchpoints across 2 individuals):
- Karpathy: vault foundation + autoresearch v10 + graphify v16 (3 touchpoints)
- John Lam: spec-kit v17 (2 touchpoints; direct author + jflam GitHub handle)

Now adding:
- **Boris Cherny: claude-howto v32 (1 touchpoint — workflow-post citation)**

**Total at v32:** 6 touchpoints across 3 individuals. Strengthens Pattern #19 archetype 1.

## 8. Multi-channel content distribution

Luong distributes claude-howto content across multiple channels:
1. **GitHub repo** — canonical source-of-truth + copy-paste templates
2. **Medium blog** — long-form narrative explanations per module (e.g., "Discovering Claude Code Slash Commands" linked from 01-slash-commands)
3. **Personal blog** (luongnv.com) — general content
4. **Twitter/X** (@luongnv89) — announcements
5. **4-language README** (EN + VN + CN + Ukrainian) — reach
6. **EPUB** — offline/Kindle distribution
7. **Feedback repos** (custats-feedback, textwiz-feedback) — commercial product feedback channel

**Corpus observation:** No prior T1 author has documented multi-channel distribution so explicitly. Contrast:
- codymaster v12 — GitHub + npm + VN-focused
- ECC v1 — GitHub only
- gstack v3 — GitHub + twitter (Garry Tan as YC president, separate channel)
- spec-kit v17 — GitHub + Anthropic/Microsoft official docs

Luong's multi-channel may partly explain 28K stars in 5.5 months (funneling Medium readership + French network + Eastern European reach via Ukrainian README).

## 9. Time-based scale analysis

**Linear month-over-month:**
- 2025-11 (created): 0 stars
- 2026-04-16 (pushed): 28,186 stars (per README "21,800+ GitHub stars" text — slightly behind actual API count of 28,186 at fetch time; README text lags reality)
- Duration: ~5.5 months
- Average: ~5,100 stars/month

**Comparison with Pattern #27 Community-Viral Scale Path data points:**
| Wiki | Scale | Duration | Rate |
|------|-------|----------|------|
| agency-agents v18 | 82.9K | ~6 months (Reddit-viral) | ~14K/month |
| TrendRadar v19 | 52.1K | — (CN community) | — |
| system-prompts-leaks v21 | 135.5K | 13 months | ~10.4K/month (fastest sustained) |
| awesome-design-md v25 | 60K | 20 days (extreme) | ~3K/day |
| OMC v27 | 30K | 3.5 months | ~300/day |
| crawl4ai v29 | 64K | 24 months | ~90/day |
| awesome-mcp-servers v31 | 85K | 17 months (sustained) | ~5K/month |
| **claude-howto v32** | **28K** | **5.5 months** | **~5K/month** |

**Sub-path classification:** claude-howto = **solo-pedagogical + multi-channel sustained-community** sub-path. Distinct from:
- Reddit-single-viral (agency-agents)
- CN-regional (TrendRadar)
- Extreme-velocity (awesome-design-md)
- Korean-community (OMC)
- Sustained-organic (crawl4ai, awesome-mcp-servers)

**Pattern #27 8th data point** with NEW sub-path (VN-diaspora-pedagogical-multi-channel).

## 10. Storm Bear operator relevance

**Direct applicability HIGH for VN-based operator:**
- Author is VN-diaspora with VN language support (though thin)
- Pedagogical framing matches Storm Bear's Scrum-coach-training-others mission
- Interactive self-assessment concept maps to Storm Bear wiki-quality diagnostic potential
- Ecosystem approach (tutorial → library → manager → registry) may inspire Storm Bear vault expansion

**Comparison to codymaster v12 for VN operator:**
- codymaster: VN-first, product-authored, solo enterprise application framework
- claude-howto: EN-first with VN port, pedagogical, multi-module tutorial

**Potential operator actions:**
1. Walk through all 10 modules as self-onboarding (~11-13h weekend)
2. Adopt 3-scope CLAUDE.md variant pattern for Storm Bear vault (project / directory / personal)
3. Reference Luong's `skills` sibling repo for skill library patterns
4. Consider Medium-blog-pipeline for Storm Bear content distribution

## 11. Risk profile

**Low risk overall:**
- MIT licensed + real named author + public identity + company affiliation
- Active maintenance (synced with every Claude Code release)
- Production-grade CI (pytest + Ruff + Bandit + mypy + Codecov)
- Explicit security policy with private-disclosure channel
- No perverse-incentive monetization (free forever + separate commercial macOS apps)

**Minor caveats:**
- Subagent + skill + hook templates are copy-paste to user's `.claude/` — users should review (standard tutorial caveat)
- Pre-commit hook VN README thinness — VN users get EN-primary experience
- Solo author bus factor (though 642 followers + active issue responses mitigate)

## 12. Cross-wiki references

| Sibling | Relationship |
|---------|-------------|
| codymaster v12 | **Primary VN-authored peer** — VN-in-VN vs VN-diaspora sub-variants |
| Unsloth v23 | Luong's `unsloth-mlx` repo is latent cross-corpus bridge |
| OMC v27 | Pattern #55 Korean Regional Archetype analog; #70 VN-Regional-Archetype inspiration |
| awesome-mcp-servers v31 | Pattern #17 variant 1 peer (Fiegel ecosystem portfolio) + Pattern #50 distinction |
| graphify v16 | Pattern #17 variant 1 solo-brand peer |
| spec-kit v17 | John Lam intellectual lineage (Pattern #19 archetype 1 peer) |

## 13. Pattern implications summary

- **Pattern #17 variant 1** (individual-led-dev): 8th data point (strengthens)
- **Pattern #19 archetype 1** (individual-author lineage): Boris Cherny as 3rd influence node; 6th touchpoint across 3 individuals (strengthens)
- **Pattern #20 Solo-Scale Ceiling dictionary**: new row "solo pedagogical-tutorial + ecosystem-portfolio" at ~28K/5.5mo (add row, no revision)
- **Pattern #24 SECURITY.md at T1**: 4th data point (strengthens)
- **Pattern #27 Community-Viral Scale Path**: 8th data point with new sub-path "VN-diaspora-pedagogical-multi-channel"
- **Pattern #55 Korean Regional Archetype**: stays N=1 at v32; claude-howto creates structural analog but different region
- **Pattern #50 Commercial-Funnel**: NOT strengthened (Luong's model is closed-commercial-app, not commercial-platform-funnel)
- **Proposed Pattern #70 VN-Regional-Archetype T1**: NEW at N=2 (structurally-unambiguous promotion-candidate); cross-refs Pattern #55
- **Proposed Pattern #71 Interactive Self-Assessment Mechanism**: NEW at N=1 (stale-risk-flagged)
