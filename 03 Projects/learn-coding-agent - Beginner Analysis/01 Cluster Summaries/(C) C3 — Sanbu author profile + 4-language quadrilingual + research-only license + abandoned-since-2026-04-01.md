# C3 — Sanbu author profile + quadrilingual + research-only license + abandoned status

> Source cluster: GitHub author profile (`sanbuphy`) + repo metadata + README copyright section + commit history
> Wiki #53

---

## Author profile

**Handle:** `sanbuphy`
**Display name:** Sanbu / 散步 (Chinese: "stroll" / "walk")
**Bio (verbatim):** *"Ask if you don't understand, Learn if you don't know."*
**Location:** "Mars" (humorous; not actual)
**Blog:** https://www.aispacewalk.cn/ (Chinese AI blog — `aispacewalk` = "AI Space Walk")
**Twitter:** @sanbuphy
**GitHub created:** 2021-12-15 (~4.4 years on GitHub at probe time)
**Public repos:** **279** (very high portfolio count; suggests prolific publisher)
**Followers:** 752
**Email:** Not publicly disclosed beyond GitHub
**Affiliations:** None disclosed; no company / lab / commercial entity association

### Inference

Sanbu is a CN-based AI researcher / blogger / prolific OSS publisher with active blog at aispacewalk.cn. The "Mars" location + humorous bio + 279-repo portfolio suggests an enthusiast / educator profile rather than a commercial entity or formal academic affiliation.

learn-coding-agent appears to be one project in a large rotating portfolio — consistent with the **abandoned-after-day-2** repo lifecycle (created 2026-03-31, last push 2026-04-01, no further commits in 24 days at probe time despite 11.7K stars + 19.7K forks).

### Comparison with other CN-author wikis in corpus

| Wiki | CN author | Tier | Maintenance |
|------|-----------|------|-------------|
| TrendRadar v19 | sansan0 | outside-scope (CN news aggregator) | Active 228+ commits |
| dive-into-llms v39 | Lordog (Yuan Tongxin) + SJTU lab | T3 academic-curriculum | Active multi-institutional |
| MiroFish v49 | BaiFu+Shanda | commercial-startup | Active commercial |
| **learn-coding-agent v53** | **Sanbu / sanbuphy** | **outside-scope (single-tool internals research-archive)** | **ABANDONED day-2** |

→ v53 is the **first abandoned-day-2 CN-author wiki** in corpus. Distinct from prior CN authors who maintain projects.

---

## Quadrilingual structure

| Language | Code | README size | docs/ subdir |
|----------|------|-------------|--------------|
| English | en | 45 KB | `docs/en/` |
| Simplified Chinese | zh / cn | 43.9 KB | `docs/zh/` |
| Japanese | ja | 43.9 KB | `docs/ja/` |
| Korean | ko / kr | 40.5 KB | `docs/ko/` |

CN-author treats CN as authoritative (typical CN-author convention). EN positioned first in repo header for international reach.

### Comparison with corpus i18n leaders

| Wiki | i18n breadth | Tier |
|------|-------------|------|
| oh-my-claudecode v27 | 7-lang (en/ko/zh/ja/es/vi/pt) | T1 |
| fish-speech v20 | 7-lang | outside-scope foundation-model |
| awesome-mcp-servers v31 | 7-lang | outside-scope MCP-aggregator |
| LlamaFactory v22 | (multi-lang README) | outside-scope training-infra |
| oh-my-openagent v52 | 5-lang docs/ | T1 |
| **learn-coding-agent v53** | **4-lang EN+CN+JA+KO** | **outside-scope archive** |
| dive-into-llms v39 | CN-primary only | T3 |
| TrendRadar v19 | CN+EN | outside-scope |

v53 i18n is **strong-mid-tier for outside-scope**; absence of VN / ES / FR / RU / pt means CN-primary author prioritized CJK reach (CN + JA + KO) + EN for international.

---

## Governance state — MINIMUM CORPUS-LEVEL

| Governance file | Present? |
|----------------|----------|
| `LICENSE` | ❌ **MISSING** |
| `CONTRIBUTING.md` | ❌ |
| `AGENTS.md` | ❌ |
| `CLAUDE.md` | ❌ |
| `SECURITY.md` | ❌ |
| `CODE_OF_CONDUCT.md` | ❌ |
| `CHANGELOG.md` | ❌ |
| `.github/` workflows | ❌ |
| `CITATION.cff` | ❌ |
| Any other governance | ❌ |
| **Total governance files** | **0** (only 4 READMEs) |

This is **MINIMUM-CORPUS-LEVEL governance**. Comparable baselines:
- bizos v37: 2 files (AGENTS.md 327B + CLAUDE.md 11B alias) + NO LICENSE → had minimum-shim (Pattern #22 22b)
- system-prompts-leaks v21: 1-2 files + GPL-3.0 license-claim
- **learn-coding-agent v53: 0 files beyond READMEs + NO LICENSE FILE** → most-minimal in corpus to date

**Pattern #12 v42 refined-formulation perspective:** This baseline-fits the 3-factor refined model:
- Maintainer-philosophy: Solo CN researcher, prolific publisher, light-touch
- Maturity-ambition: Research archive, NOT product
- Scale-tier: Medium (11.7K stars, but functionally cold-start at 25 days)

→ Strengthens refined formulation; NOT counter-evidence.

---

## License analysis — informal research-only-non-commercial-restriction

### What's actually there

README §"Copyright & Disclaimer" (verbatim):

```
This repository is provided strictly for technical research and educational purposes.
Commercial use is strictly prohibited.

If you are the copyright owner and believe this repository content infringes your rights,
please contact the repository owner for immediate removal.
```

### Legal classification

- **No formal license** (NOT Apache / MIT / BSD / AGPL / GPL / SUL / PolyForm / MPL / etc.)
- **Default copyright applies** (international Berne Convention default = all rights reserved by author)
- **Informal "research-only + commercial-prohibited" declaration** in README only — has goodwill-signal weight, not legal-license weight
- **DMCA-style takedown clause** — author acknowledges potential third-party rights infringement (Anthropic claim could trigger removal)

### Pattern #29 absent-LICENSE 4-sub-context taxonomy (post-v52 state)

| Sub-context | Wikis | Description |
|-------------|-------|-------------|
| 29-absent-1 commercial-cold-start + README-proprietary-claim | bizos v37 | Commercial app, 2-day-old, README-only proprietary statement |
| 29-absent-2 academic-public-welfare + no-claim | dive-into-llms v39 | Academic curriculum, default-copyright, no commercial-restriction claim |
| 29-absent-3 README-OSI-license-claim-without-LICENSE-file | awesome-claude-skills v50 + vercel-labs v51 | README claims MIT/Apache but no LICENSE file |
| **29-absent-4 research-only-non-commercial-restriction-without-LICENSE-file + Copyright-disclaimer** **NEW v53** | **learn-coding-agent v53** | **Research archive, README-only "Commercial use strictly prohibited" + DMCA takedown clause, default copyright** |

→ Pattern #29 strengthens with NEW 29-absent-4 sub-context. Sub-context formalization-candidate at next mini-audit.

### Storm Bear commercial impact

learn-coding-agent's research-only license **blocks Storm Bear from**:
- Re-packaging this archive's content for client-facing Scrum coaching deliverables
- Using direct quotes/diagrams in commercial training materials
- Citing in pitch decks for monetary engagement

learn-coding-agent's research-only license **PERMITS Storm Bear to**:
- Read and learn from the archive personally
- Use insights for vault internal improvements
- Reference architectural concepts (which are facts not copyrightable)
- Cross-reference in this Storm Bear wiki under fair-use research framing

---

## Abandoned-since-2026-04-01 status

| Field | Value |
|-------|-------|
| Created | 2026-03-31 |
| First (initial) commit | 2026-03-31 (estimated) |
| Last push | **2026-04-01** |
| Days stale at probe | **~24 days** |
| Total commits (visible) | Few (low-commit-count repo per probe) |
| Open issues | 59 (unaddressed) |
| Open PRs | Unknown |

**Abandoned-archive pattern observation:** Repo gathered massive engagement (11.7K stars + 19.7K forks in 25 days) but author abandoned within day 2 → suggests:
1. Sanbu may have intended a one-shot publish-and-walk-away research dump
2. May be aware of legal exposure (no LICENSE + Anthropic-internals disclosure → litigation risk)
3. May be a CN-OSS-pattern of frequent-publish-low-maintain (consistent with 279 public repos)
4. Hypothesis: Sanbu compiled from upstream sources (anthropics' own bug reports? community Discord? LLM-assisted reverse-engineering?) and published once

**For Storm Bear**: treat as static reference; do not expect updates. Future Claude Code versions will diverge from v2.1.88 baseline.

---

## Cluster takeaway

Sanbu / 散步 = solo CN researcher, prolific publisher (279 repos), Mars-humor, blog-active at aispacewalk.cn. Quadrilingual EN+CN+JA+KO archive of Claude Code v2.1.88 internals. Zero-governance-files except 4 READMEs. Informal research-only-non-commercial-restriction without formal LICENSE → Pattern #29 NEW 29-absent-4 sub-context. Abandoned 24 days post-creation despite 11.7K stars + CORPUS-RECORD 168.2% fork-to-star inversion. Static reference for Storm Bear; commercial re-use blocked.
