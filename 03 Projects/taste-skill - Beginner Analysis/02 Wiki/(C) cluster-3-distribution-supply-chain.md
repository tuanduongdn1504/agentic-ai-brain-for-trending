# (C) Cluster 3 — Distribution + supply-chain + tasteskill.dev + GitHub Sponsors

**Source bundle**: GitHub API repo metadata + GitHub Sponsors panel + README "Installing" section + README "Support" section + `tasteskill.dev` custom domain + Leonxlnx user profile (104 repos / 819 followers / @lexnlin Twitter) + topics + license + push activity.

## Distribution mechanism: `npx skills add`

**Primary install vector** (README "Installing" section):

```
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

(Skill-name pattern inferred; exact `--skill` argument syntax not Phase 0 captured for all 12 skills.)

**Key properties**:
- Claude Code skills standard install command.
- Per-skill `--skill` flag granularity — user installs **only what they want** from the 12-skill catalog.
- Framework-agnostic at runtime (React / Vue / Svelte).
- Zero-API-key requirement (skill is design-intent rules + visual patterns, not external-service-dependent).
- Reversible (uninstall via Claude Code skill management surface).

## Multi-harness ecosystem coverage

**4-harness ecosystem citation** (Pattern #57 57c-product evidence):

| Harness | Citation in v81 | Corpus subject reference |
|---------|-----------------|--------------------------|
| **Claude Code** | Primary install target | v65 corpus subject |
| **Codex** | Variant skill `gpt-tasteskill` + repo description | v62 corpus subject |
| **Cursor** | Repo description multi-harness mention | v75 / v76 corpus subject |
| **ChatGPT Images** | Image-gen-skill targets ChatGPT image-gen | (corpus-adjacent; not yet anchor-subject) |

**Distribution layer mechanism**: repo-stored skill directories cloned via `npx skills add` from GitHub canonical source. **Pattern #84 84c.1 sub-sub-mechanism** ("repo-stored N-harness-replicas" — same pattern as v75 impeccable's 14-harness layout; **N+1 strengthening at repo-stored layer**).

## tasteskill.dev custom domain

**Custom domain investment**:
- Separate from `Leonxlnx.github.io/taste-skill` (default GitHub Pages).
- Suggests **product-brand positioning** beyond hobbyist-repo signaling.
- DNS + likely tailored landing page = marketing-surface investment.
- **Phase 0 not deep-fetched** for site content — landing page content + value-proposition statements + screenshots + CTAs unverified.

**Brand-investment signaling distinction**:
- v75 impeccable = no custom domain observed; GitHub-native presentation.
- v77 easy-vibe = `easy-vibe.netlify.app` deploy target (Netlify-hosted; non-custom).
- v78 ECC = `ecc.everythingclaude.ai` + `everythingclaude.ai` custom domain + Pro-SaaS at $19/seat/mo.
- v81 taste-skill = `tasteskill.dev` custom domain + GitHub Sponsors + **NO paid tier observed** = community-funded-indie-with-brand-investment hybrid.

## GitHub Sponsors panel

**8 named sponsors** at Phase 0 fetch time. **Modest community-funding base** consistent with:
- Indie-developer positioning.
- Pre-monetization-phase signal (no Pro tier observed).
- Personal-brand audience cultivation rather than corporate-funded indemnity.

**Distinct from v78 ECC's economic model**:
- ECC = MIT-OSS + 2 npm freemium packages + GitHub App freemium 150+ installs + Pro $19/seat/mo + Sponsors $5+/mo (5-tier dual-license-economic-model).
- v81 taste-skill = MIT-OSS + Sponsors only (1-tier community-funded model).
- **Library-vocabulary item #13 (OSS-with-hosted-Pro-SaaS-tier-on-MIT-base) NOT applicable** to v81 — economic-model is pure-OSS-with-donations distinct from ECC's hybrid.

## Supply-chain (Pattern #66) surface

**Install vector analysis**:

| Surface | Risk | Observed mitigation |
|---------|------|---------------------|
| `npx skills add` from GitHub | Trust-Leonxlnx-as-maintainer + Trust-GitHub-as-host | GitHub repo verifiable; commit history visible |
| 12-skill install granularity | 12 separate trust decisions per user | User explicit-choice per skill via `--skill` flag |
| `skills/` content | Markdown skill files (design rules + prompts); no executable code observed | Text-only content surface (lower supply-chain risk than binary distribution) |
| No `SECURITY.md` observed at Phase 0 | Disclosure-channel undeclared | None observed |
| No `CODEOWNERS` observed at Phase 0 | Maintainer-ownership-graph undeclared | Solo-maintainer-implicit-via-commit-history |
| Skill content can include prompt-injection vectors (instructions LLM consumes) | Skill content executes as part of agent's context | **NO Prompt Defense Baseline observed** (v78 ECC had explicit 6-axis baseline) |

**Pattern #66 within-pattern strengthening** — supply-chain-discipline-at-skill-bundle-scale partial; meta-supply-chain-awareness sub-category candidate evidence.

**v76 agent-skills-standard contrast** — 6-axis supply-chain integrity (text-only + zero-telemetry + local-first + injection-scanning + Zod-validation + evals.json per skill). v81 taste-skill = subset of v76 discipline (text-only confirmed; other 5 axes not observed).

## Push activity / sustenance signal

**Recent push** to main branch within Phase 0 fetch window (last push date not captured precisely; flag for Phase 2 git API fetch). **Open issues**: 14 / **Watchers (subscribers)**: 92 / **Forks**: 1,560.

**Velocity profile** (Pattern #52 N=4 HIGH-NOT-EXTREME):
- 18,264 stars / 90 days = 202.93 stars/day.
- Mid-range 150-300/d band.
- **Mid-life-cycle** (90 days = past launch-window-pulse; into sustenance-phase).
- **fork_ratio** 8.54% = modest active-deployment (below the >15% active-deployment threshold; consistent with design-rule-skill where users consume skill rather than fork-and-modify).
- **watchers_ratio** 0.50% = drive-by-stars-dominant.

**Pattern #52 N=4 evidence quality**:
- v69 CloakBrowser: 86 days (early-life-cycle)
- v72 DeepSeek-TUI: 120 days (early-mid-life-cycle)
- v73 cc-switch: 289 days (mid-life-cycle CORPUS-RECORD)
- **v81 taste-skill: 90 days (early-mid-life-cycle; mid-life-cycle equivalence band)**

v81 sits between v69 + v72 age-bracket = **age-distribution-coverage strengthening** for HIGH-NOT-EXTREME sub-class.

## Author profile distribution-implications

**Leon Lin (Leonxlnx)**:
- Munich location (per GitHub profile).
- @lexnlin Twitter handle.
- bio: *"i like to build stuff"*.
- 104 public repos = **ecosystem-portfolio-builder at scale** (Pattern #19 sub-mechanism candidate).
- 819 followers = moderate audience.
- GitHub Sponsors enabled.

**Pattern #19 NEW sub-mechanism 19l candidate "Munich-Solo-Founder-with-Multi-Skill-Design-Brand-Portfolio"** PROVISIONAL N=1 — distinct from existing 19a-19k sub-mechanisms (different geography + different methodology + different domain-vertical).

**AVOID inferences beyond observable** — profession / company affiliation / specific design-background not GitHub-public-verifiable; flag claims beyond observable.

## Pattern Library implications (Cluster 3 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **Pattern #52 N=4 HIGH-NOT-EXTREME age-distribution-coverage strengthening** | 202.93/d × 90d sits in mid-life-cycle band; complements existing 86d + 120d + 289d N=3 evidence | STRONG strengthening |
| **Pattern #57 sub-variant 57c-product** | 4-harness ecosystem citation (Claude Code + Codex + Cursor + ChatGPT Images) | STRONG within-pattern strengthening |
| **Pattern #66 supply-chain** | 12-skill install granularity + text-only content + no SECURITY.md + no Prompt Defense Baseline | Within-pattern STRENGTHENING with sub-typology contrast vs v76 6-axis discipline |
| **Pattern #84 84c.1 N+1 strengthening at repo-stored layer** | 4-harness repo-stored skill directories per harness × 12-skill = broader matrix than v75's 14-harness × 1-skill | Within-pattern strengthening (joins post-promotion arc) |
| **Pattern #19 NEW sub-mechanism 19l candidate** | Munich-solo-founder + multi-skill-design-brand-portfolio + 104-repo Leonxlnx + GitHub Sponsors | PROVISIONAL N=1 |
| **Pattern #82 quantitative-marketing** | "Anti-Slop" + "Portable Agent Skills" + "Framework-Agnostic" + dimensional spectrum + 4-harness claims | Within-pattern strengthening |
| **Library-vocabulary item #13 (OSS-with-Pro-SaaS-tier) CONTRAST evidence** | v81 = pure-OSS-with-donations = distinct from v78 ECC dual-license-economic-model | Negative-evidence sub-typology contrast |

## Cross-wiki siblings (Cluster 3)

- **v75 impeccable** — DIRECT SISTER; multi-harness distribution layer comparison; both 4+ harness Pattern #84 evidence.
- **v76 agent-skills-standard** — 6-axis supply-chain discipline CONTRAST vs v81 partial-discipline.
- **v78 ECC** — economic-model contrast (Pro-SaaS hybrid vs pure-OSS-with-donations).
- **v77 easy-vibe** — `llms.txt` artifact + brand investment + community-funded comparison.
- **v66 agentmemory** — solo-developer + skill-distribution comparison.

## Absences / open questions surfaced

- **tasteskill.dev landing page content** not fetched at Phase 0.
- **Recent push date precision** not pinned.
- **`SECURITY.md` / `CODEOWNERS` / `CONTRIBUTING.md` / `CHANGELOG.md`** observed absent at Phase 0 (negative confirmation via tree-fetch).
- **GitHub Sponsors tier-amounts** not fetched.
- **Per-skill harness-coverage matrix** unverified (does `minimalist-skill` work on Codex? does `gpt-tasteskill` work on Claude Code? assumed all-4-harnesses but unconfirmed).
- **Skill-install verification mechanism** (signature / checksum / integrity) unobserved.

These migrate to expanded `(C) open questions.md` Phase 4 pass.
