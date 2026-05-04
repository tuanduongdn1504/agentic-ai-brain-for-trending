# Jarrod Watts — Australian solo-author + 144-repo portfolio

**Entity type:** Person / author archetype
**Subject:** Jarrod Watts (`jarrodwatts`), creator of claude-hud
**First documented:** 2026-04-23 (v35 wiki creation)

---

## 1. One-sentence definition

Jarrod Watts is a **Sydney, Australia**-based solo developer with an **8-year GitHub presence** (since 2018-01-21), **144 public repos**, and **1,075 followers**, who created claude-hud in January 2026 as a narrow-utility Claude Code plugin that reached 20K stars in ~3 months.

## 2. Public profile surface

| Field | Value |
|-------|-------|
| GitHub login | jarrodwatts |
| Real name | Jarrod Watts |
| Location | Sydney, Australia |
| Blog | jarrodwatts.com |
| Twitter | @jarrodwatts |
| Company | None listed on GitHub |
| Bio | Not provided on GitHub |
| Public repos | 144 |
| Followers | 1,075 |
| Following | 28 |
| Hireable | Not specified |
| GitHub since | 2018-01-21 (~8 years) |

**Observations:**
- No company affiliation disclosed publicly via GitHub.
- Homepage is personal blog (`jarrodwatts.com`), not a corporate landing page.
- 1,075 followers / 28 following = content-creator-shaped follower ratio (one-way broadcast-style).
- 144 repos is high-volume; claude-hud is the standout breakout.

## 3. Regional-archetype observation — 1st Australian T1

claude-hud is the **1st Australian-authored framework in the Storm Bear corpus** at any tier.

Prior T1 author regions (12 entrants):
- US (multiple): ECC v1 (affaan-m), Superpowers v2 (Jesse Vincent), gstack v3 (Garry Tan), GSD v5 (TÂCHES), BMAD v11 (BMad Code LLC), agency-agents v18 (msitarzewski)
- US corporate: spec-kit v17 (GitHub / Microsoft)
- VN-in-VN: codymaster v12 (Tody Le, HCMC)
- VN-diaspora: claude-howto v32 (Luong Nguyen, Paris)
- Korean: oh-my-claudecode v27 (Yeachan Heo, Seoul)
- Pakistani: claude-code-best-practice v34 (Shayan Rais, Karachi)
- **Australian: claude-hud v35 (Jarrod Watts, Sydney)** ← first Australian

### Registration discipline

Per v2.1 consolidation-forward discipline, Australian-Regional-Archetype is **NOT registered as standalone candidate** (which would be 4th regional-archetype-candidate fragment after #55 Korean STALE, #70 VN CONFIRMED, #73 meta-pattern v34-candidate). Instead, treated as **observational** — flag for potential #73 sub-variant 73d if 2nd Australian T1 emerges.

The v34 #73 meta-pattern wraps Korean + VN + Pakistani regional archetypes. Australian is a potential 4th region but at N=1 no structural evidence yet. Per v2.1 protocol:
- N=1 stale-risk-flag at registration — NOT registered
- Structural confirmation only at N=2 within Australian cluster

**Decision:** Pure observation in wiki narrative; no Pattern Library row.

## 4. 144-repo portfolio analysis

144 public repos is substantially larger than:
- Luong (claude-howto v32): 116 repos
- Yeachan (OMC v27): unspecified but visible siblings oh-my-codex + oh-my-opencode
- Shayan (claude-code-best-practice v34): 3 pinned
- Tody (codymaster v12): small portfolio

**claude-hud is the breakout standout** — per GitHub API metadata, claude-hud has 20K stars vs 1,075 follower count suggests prior repos were smaller-scale. **Solo-one-hit-flagship** pattern observation (author has broad portfolio, one repo becomes viral breakout).

### Solo-one-hit-flagship vs ecosystem-portfolio axis

Pattern #17 Ecosystem-Layer Organizations has tracked authors with **ecosystem portfolios** — Yeachan's sibling products (oh-my-codex, oh-my-opencode), Luong's 15+ companion repos, Shayan's 3 pinned ecosystem. These authors build **multiple interconnected products**.

Jarrod's profile is different:
- 144 repos spanning many years
- Only claude-hud reached 20K+ scale
- No observable "claude-hud ecosystem" (no sibling products like `claude-hud-notifier`, `claude-hud-for-cursor`, etc.)
- claude-hud stands alone as the viral breakout

**Hypothesis:** **Solo-one-hit-flagship** is a distinct Pattern #17 variant from ecosystem-portfolio. Author accumulates portfolio of exploration projects; one becomes the breakout; rest stay small. This is the **long-tail of individual open-source creator** economics.

**Registration decision:** N=1 at v35. NOT registered per consolidation-forward discipline. Flag in open questions. If 2nd similar case emerges (large portfolio + single breakout utility at 5K+ scale), consider Pattern #17 variant 6 registration.

## 5. Author voice from documentation

Characteristic phrases from README + CHANGELOG + CONTRIBUTING:

- *"ClaudeHUD never falls back to credential scraping or undocumented API calls"* — explicit security boundary statement
- *"Stop guessing auth mode from environment variables alone"* (CHANGELOG v0.0.12) — honest fix framing
- *"keep Bedrock/unknown pricing cases hidden rather than showing misleading estimates"* — prefer silence to imprecision
- *"closes attack vector where malicious code could be injected via compiled output in PRs"* — supply-chain-aware release notes
- *"We cannot guarantee response times, but we will triage issues as time allows"* (SUPPORT.md) — honest scope-limiting
- *"Only if they explicitly agree, run... Never run this automatically without user consent"* (CLAUDE.README.md star-ask step) — consent-gated LLM behavior

**Voice pattern:** Honest, security-conscious, approximation-aware, scope-limiting. Consistent with Anthropic-aligned community norms (trust signals, explicit boundaries, honest caveats).

## 6. Contribution acknowledgement habit

CHANGELOG explicitly credits contributors:

| Contributor | Contributions | Release |
|-------------|---------------|---------|
| @Tsopic | Config system, layouts, path levels, git toggle | v0.0.4 (#32) |
| @melon-hub | Usage API, configure skill, bug fixes | v0.0.4 (#34) |
| @r-firpo | Autocompact buffer ideas | v0.0.5 (#30) |
| @yansircc | Autocompact buffer ideas | v0.0.5 (#43) |
| @StephenJoshii | Autocompact buffer ideas | v0.0.5 (#49) |

Plus dozens of numbered PRs cited in subsequent releases.

**Observation:** Author credits prolifically. **Community-around-solo** pattern (similar to spec-kit v17 with numerous contributor acknowledgements).

## 7. Multi-channel presence

- **GitHub:** jarrodwatts (144 repos)
- **Blog:** jarrodwatts.com (listed as profile blog field)
- **Twitter:** @jarrodwatts
- **Sydney-based** (local presence)

Not observable from this wiki build (would require secondary source fetch):
- YouTube presence
- LinkedIn
- Medium / Substack
- Stack Overflow

**Multi-channel reach likely contributed to viral adoption** — Pattern #27 data points consistently show multi-channel authors scale faster than single-channel authors (Luong v32 had YouTube + Medium + LinkedIn + Stack Overflow; Shayan v34 had similar).

## 8. Technical signal inference

From repo structure + package.json + TypeScript + governance files:

- **Strong TypeScript engineering habits** — module-per-concern discipline, zero runtime dependencies, native test runner
- **Security-conscious release discipline** — preventive supply-chain hardening at v0.0.2
- **Documentation-first habit** — 3 parallel doc files (README + CLAUDE.md + CLAUDE.README.md), 7 governance files
- **Rapid iteration capability** — 12 releases in 3 months including 2 major default-layout redesigns
- **Willingness to break defaults for UX** — v0.0.6 / v0.0.7 migrations

**Professional software engineering signals present** — even though no company affiliation is disclosed on GitHub, technical practices match senior-engineer standards.

## 9. Relationship to Claude Code ecosystem

Jarrod is not an Anthropic employee (no company field, no evidence). He builds third-party tooling for Claude Code.

His relationship to the ecosystem is:
- **Consumer of Claude Code's extension-point API** (statusline primitive)
- **Contributor to Claude Code's plugin marketplace ecosystem** (claude-hud is the 2nd corpus-observed marketplace-native framework after OMC v27)
- **Not cited in Claude Code documentation as partner / ambassador / certified architect** (contrast Shayan Rais v34 who holds "Claude for OSS" + "Claude Community Ambassador" + "Claude Certified Architect" badges)

**Observation:** Jarrod is a **functional third-party contributor**, not a credentialed ecosystem insider. Distinct from Shayan's formal-affiliation profile.

## 10. Bus factor and sustainability

**Bus factor: 1.** Solo maintainer. MAINTAINERS.md explicitly single-person. SUPPORT.md explicitly "best-effort basis, no guarantee response times."

**Sustainability signals:**
- **Positive:** Zero runtime deps (low maintenance surface), MIT license (fork-friendly), documented extension procedure in CLAUDE.README.md (successor-friendly), triple-manifest version protocol (deterministic release), contributor-open maintainer succession path in MAINTAINERS.md
- **Neutral:** 3-month project age (not yet tested against multi-year maintenance fatigue)
- **Negative:** Heavy governance overhead (7 files) may signal over-engineering; rapid default-redesign cadence (v0.0.6 → v0.0.7) could fatigue long-term if continued

**If Jarrod goes dark:** Project is forkable, architecture is legible, scope is bounded. Low continuation cost for community takeover.

## 11. Storm Bear operator relevance

- **Regional archetype:** Australian (Sydney) is geographically/culturally distinct from VN operator, but cultural-content-overlap is high (English-primary, common Claude Code tooling, similar Slack/GitHub norms)
- **Communication channels:** Same English tooling stack as Storm Bear operator uses; no VN i18n friction
- **Author trust:** Voice patterns consistent with Anthropic-aligned community; low brand-risk for Storm Bear association
- **Pattern observation:** First Australian T1 = regional-archetype data point for potential future #73 meta-pattern expansion

## 12. Open questions specific to Jarrod Watts

- Does Jarrod have other Claude Code ecosystem contributions (non-claude-hud)? 144-repo scan might surface additional signals.
- What triggered claude-hud as the breakout? Early Reddit post? Twitter thread? Anthropic-internal mention? (unknown from README-only analysis)
- Will Jarrod expand into multi-plugin ecosystem-layer-individual variant (like Yeachan's oh-my-codex sibling), or remain single-plugin author?
- Is jarrodwatts.com blog an active content channel? Multi-channel contribution Pattern #27 data point would depend on this.

## 13. Provenance

- GitHub API user profile fetched 2026-04-23
- CHANGELOG contributor credits analyzed 2026-04-23
- README author voice pattern synthesized 2026-04-23
- Multi-channel reach inferred from profile blog + twitter fields only (not fetched directly)

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 3.*
