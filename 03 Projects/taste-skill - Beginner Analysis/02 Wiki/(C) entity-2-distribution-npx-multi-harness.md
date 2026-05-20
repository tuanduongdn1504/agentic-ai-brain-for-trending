# (C) Entity 2 — Distribution: `npx skills add` multi-harness + tasteskill.dev brand-surface

**Entity scope**: How the product reaches users + brand-investment surface + supply-chain posture + economic model.

## Primary install vector

```
npx skills add https://github.com/Leonxlnx/taste-skill --skill "<skill-name>"
```

**Properties**:
- Claude Code skills standard install command.
- Per-skill `--skill` flag = user chooses among 12 skills.
- GitHub repo as canonical source.
- Zero-API-key (skill content is design-rules + prompts, not external-service-dependent).
- Reversible (uninstall via Claude Code skill management).

**Distribution layer mechanism**: **Pattern #84 84c.1** ("repo-stored N-harness-replicas") — same sub-sub-mechanism as v75 impeccable (14-harness layout) + v76 agent-skills-standard (CLI-generated alt). v81 contributes **N+1 strengthening at repo-stored layer** with broader skill-count × harness matrix.

## 4-harness ecosystem coverage

| Harness | v81 evidence | Storm Bear corpus reference |
|---------|-------------|------------------------------|
| **Claude Code** | Primary install target (`npx skills add` is Claude Code native) | v65 corpus subject |
| **Codex** | Variant skill `gpt-tasteskill` + repo description multi-harness mention | v62 corpus subject |
| **Cursor** | Repo description multi-harness mention | v75 / v76 corpus subject |
| **ChatGPT Images** | Image-gen skill targets ChatGPT image-gen workflow | corpus-adjacent (not anchor-subject) |

**Pattern #57 sub-variant 57c-product** STRONG within-pattern strengthening: 4-corpus-subject ecosystem citation in single-subject product surface.

## Custom domain `tasteskill.dev`

**Investment signaling**:
- Separate from default GitHub Pages.
- DNS purchase + maintenance = ongoing brand-investment.
- Marketing-surface beyond GitHub README likely exists at site (Phase 0 not deep-fetched for content).

**Brand-investment vs revenue**:
- No paid tier observed.
- No SaaS observed.
- GitHub Sponsors = donation-based community-funding.
- Custom domain + no monetization = **community-funded-indie-with-brand-investment hybrid economic model**.

**Distinct from v78 ECC dual-tier model**:
- v78 ECC = MIT-OSS + npm freemium + GitHub App freemium + Pro $19/seat/mo + Sponsors ($5+/mo) = 5-tier dual-license-economic-model.
- v81 taste-skill = MIT-OSS + Sponsors = 2-tier pure-OSS-with-donations.
- Library-vocabulary item #13 (OSS-with-hosted-Pro-SaaS-tier-on-MIT-base) **NOT applicable** to v81 = CONTRAST evidence; PROVISIONAL #13 status unchanged.

## GitHub Sponsors panel

- **8 named sponsors** at Phase 0 fetch.
- Modest community-funding base.
- Tier-amount distribution unfetched at Phase 0.
- Consistent with indie-developer + pre-monetization signaling.

## Supply-chain (Pattern #66) posture

| Surface | v81 posture | v76 contrast (6-axis discipline) |
|---------|-------------|----------------------------------|
| Text-only skill content | ✅ Observed | ✅ |
| Zero-telemetry | ✅ Inferred (no telemetry observed) | ✅ explicit |
| Local-first | ✅ Skills install locally | ✅ explicit |
| Injection-scanning | ❌ Not observed | ✅ explicit |
| Schema validation (e.g., Zod) | ❌ Not observed | ✅ explicit |
| Per-skill evals.json | ❌ Not observed | ✅ explicit |

**v81 = 3-of-6 axes evident** (subset of v76's 6-axis discipline). **Partial supply-chain discipline** at 12-skill install-vector scale.

**Observed absences** (Phase 0 tree-fetch):
- No `SECURITY.md`.
- No `CODEOWNERS`.
- No `CONTRIBUTING.md`.
- No `CHANGELOG.md`.
- No Prompt Defense Baseline (v78 ECC had explicit 6-axis baseline).

**Pattern #66 within-pattern strengthening** — meta-supply-chain-awareness sub-category candidate evidence (the absences themselves are observable; flag as known gap).

## tasteskill.dev landing-page content (UNVERIFIED — flag for Phase 2 deeper fetch)

Phase 0 did not deep-fetch the custom domain. Likely landing-page content (inferred): tagline + visual examples + install command + sponsor link + maybe skill catalog browser. **Phase 5 iteration log SHOULD flag** this gap if Phase 4 hasn't closed it.

## Trust topology

Trust required for `npx skills add` flow:
1. **Trust GitHub** as canonical host.
2. **Trust Leonxlnx as maintainer** of `Leonxlnx/taste-skill` repo.
3. **Trust 12 skill content authors** (single-maintainer Leonxlnx implicit per commit history).
4. **Trust skill-content prompts** as part of agent's execution context (prompt-injection vector if skill author becomes adversarial).

**Solo-maintainer trust model** = single point of failure / compromise; consistent with indie-developer scale. **Higher trust burden** for users than community-maintained alternatives (e.g., v76 agent-skills-standard's contributor model).

## Pattern Library implications (Entity 2 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **Pattern #66 supply-chain partial-discipline** | 3-of-6 axes from v76's baseline + 12-skill install granularity + solo-maintainer trust model | Within-pattern STRENGTHENING with sub-typology contrast |
| **Pattern #84 84c.1 repo-stored N+1 strengthening** | Repo-stored 12-skill × 4-harness matrix | Within-pattern strengthening |
| **Pattern #57 sub-variant 57c-product STRONG** | 4-harness corpus-subject ecosystem citation | STRONG within-pattern |
| **Library-vocabulary item #13 CONTRAST evidence** | v81 = pure-OSS-with-donations DISTINCT from v78 ECC Pro-SaaS hybrid | Negative-evidence sub-typology contrast |
| **Pattern #19 NEW sub-mechanism 19l candidate** | Munich-solo-founder + multi-skill-portfolio + brand-investment-without-monetization | PROVISIONAL N=1 |
| **Pattern #82 quantitative-marketing** | "Anti-Slop" + "Portable Agent Skills" + "Framework-Agnostic" + 4-harness claims + dimensional spectrum | Within-pattern strengthening |

## Open questions migrated from Cluster 3

- tasteskill.dev landing page content
- Recent push date precision
- GitHub Sponsors tier amounts
- Per-skill harness-coverage matrix (do all skills cover all 4 harnesses?)
- Skill-install integrity (signature / checksum verification?)
