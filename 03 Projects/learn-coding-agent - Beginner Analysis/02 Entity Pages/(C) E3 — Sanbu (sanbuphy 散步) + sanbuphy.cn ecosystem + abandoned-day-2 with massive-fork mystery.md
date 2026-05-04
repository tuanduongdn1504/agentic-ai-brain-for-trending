# E3 — Sanbu / sanbuphy / 散步 + aispacewalk.cn ecosystem + abandoned-day-2 with massive-fork mystery

> **Type:** Entity page (author + ecosystem profile)
> **Wiki #53**

---

## Identity

| Field | Value |
|-------|-------|
| GitHub handle | `sanbuphy` |
| Display name | Sanbu (散步) — Chinese: "stroll" / "walk" |
| Bio (verbatim) | *"Ask if you don't understand, Learn if you don't know."* |
| Location (claimed) | Mars (humorous; not actual) |
| Blog | https://www.aispacewalk.cn/ ("AI Space Walk" — CN AI blog) |
| Twitter | @sanbuphy |
| Email | Not publicly disclosed |
| GitHub created | 2021-12-15 (~4.4 years on GitHub) |
| Public repos | **279** |
| Followers | 752 |
| Affiliations | None disclosed (no company / lab / commercial entity) |

---

## Ecosystem signals

### High-volume publisher

279 public repos at 4.4 years on GitHub = **~63 repos/year** = **~1.2 repos/week**.

This is order-of-magnitude higher than typical OSS author archetypes:
- Typical solo OSS author: 5-30 repos
- Prolific OSS author: 30-100 repos
- **Sanbu: 279 repos = elite-prolific tier**

→ Inference: Sanbu treats GitHub as continuous-publish channel rather than focused-flagship channel. Consistent with frequent-publish-low-maintain CN-OSS culture (where many CN authors publish for portfolio + community + reputation + occasional viral hit).

### Active blog

aispacewalk.cn is a CN AI blog. Title interprets as "AI Space Walk" (空间漫步 / aerospace-walk). Blog likely hosts:
- Long-form CN AI commentary
- Tutorials / explainers
- Possibly translations of EN AI content into CN
- Companion content to GitHub repos

(Not directly probed; inferred from URL pattern + author profile.)

### Twitter @sanbuphy

Active Twitter (X) account. Cross-channel content distribution typical for CN AI educator/influencer profile.

### Mars-location humor + lighthearted bio

Self-presentation = enthusiast / playful / non-serious-corporate. Distinct from:
- Academic profile (would list institution + papers)
- Commercial founder (would list company + product)
- Anthropic-style corporate-anonymous (would list nothing)

→ Sanbu is **independent CN AI educator/blogger/publisher with playful brand**.

---

## Cross-corpus CN-author comparison

| Corpus wiki | CN author | Tier | Profile depth | Maintenance |
|-------------|-----------|------|---------------|-------------|
| TrendRadar v19 | sansan0 | outside-scope | Solo philosopher; "escape algorithmic control" | Active |
| dive-into-llms v39 | Lordog (Yuan Tongxin) + SJTU lab | T3 academic | Multi-institutional consortium | Active |
| MiroFish v49 | BaiFu+Shanda | commercial-startup | 2-founder commercial | Active |
| **learn-coding-agent v53** | **Sanbu / sanbuphy** | **outside-scope** | **Solo enthusiast + playful + Mars-humor + 279 repos + active blog** | **ABANDONED day-2** |

→ v53 is unique in corpus as **first abandoned-day-2 CN-author wiki**. Other CN authors maintain projects beyond initial publish.

---

## learn-coding-agent in Sanbu's portfolio

learn-coding-agent appears to be:
- Repo #N of 279 (specific position unknown)
- Created 2026-03-31, abandoned 2026-04-01
- One-shot publish-and-walk-away pattern
- May be 1-of-many similar research-archive style repos in Sanbu's portfolio

(Other Sanbu repos not probed at v53 build time; portfolio depth-analysis deferred.)

---

## Abandoned-day-2 mystery

### Timeline reconstruction

| Date | Event |
|------|-------|
| 2026-03-31 | Repo created |
| 2026-04-01 | **LAST PUSH** (abandoned) |
| 2026-04-25 | 24 days stale; 11.7K stars + 19.7K forks accumulated |

### Hypotheses for abandonment

1. **One-shot publish design** — Sanbu intended a single-publish research dump from the outset; abandonment is by design, not neglect
2. **Legal exposure awareness** — No LICENSE + Anthropic-internals disclosure → potential litigation risk; abandonment may be passive risk-management
3. **Anthropic outreach** — Anthropic may have privately requested takedown/abandonment (DMCA-style); README §"Copyright & Disclaimer" pre-anticipates this scenario
4. **CN-OSS culture norm** — Frequent-publish-low-maintain pattern; not pathological abandonment but cultural baseline
5. **Velocity exceeded planning capacity** — 11.7K stars + 19.7K forks + 59 issues in 25 days exceeded Sanbu's intended engagement bandwidth; passive abandonment as response
6. **Source-confidence concerns** — Sanbu may have realized claims need cross-reference/correction but lacked time/motivation to maintain accuracy

**Storm Bear cannot disambiguate** without direct contact with Sanbu (which is not in scope for vault wiki-building).

### What abandonment means for Storm Bear

- **Static reference**: Treat as point-in-time snapshot of Claude Code v2.1.88 internals (via Sanbu's interpretation of public sources)
- **Decay**: Future Claude Code versions diverge from v2.1.88; specific version-bound claims (codenames, feature flags, file paths) may already be stale
- **No update path**: 59 open issues unaddressed; no path to error-correction
- **Verification responsibility shifts to reader**: Storm Bear should sample-verify claims against actual Claude Code behavior before relying on them operationally

---

## CORPUS-RECORD 168.2% fork-to-star inversion mystery

### Numbers

- Stars: 11,735
- Forks: **19,741**
- Inversion ratio: 19,741 / 11,735 = **168.2%**
- Forks exceed stars by **8,006** (68% excess)

This is **CORPUS-RECORD** — exceeds prior corpus-first 138% inversion at bizos v37.

### Why this is structurally anomalous

Typical OSS repo: stars >> forks (by 5-50× for typical projects).

Repos with high fork ratios (typical):
- Templates (intended for cloning): forks may approach stars
- Course materials / tutorials (students fork for personal): forks may approach stars
- **Forks > stars is RARE**

learn-coding-agent has:
- ZERO code (markdown-only)
- ZERO template-deployable pattern
- ZERO course-assignment binding (no curriculum dependency)
- ZERO API to call
- Just READMEs + 5 deep-dive markdown reports

→ **Why are 19,741 people forking a markdown-only abandoned-archive?**

### Possible mechanisms (uncertain ranking)

1. **CN-class-assignment-fork**: CN academic culture sometimes uses GitHub forks for course assignments. If a Chinese CS course assigned "study Claude Code internals," students may fork as bookmark-with-modification-rights. **Plausible** given CN-author + CN-language docs.
2. **Mass-fork-bot**: CN GitHub ecosystem has documented fork-farm bot activity (sometimes for SEO / repo-promotion / proxy-distribution). 19,741 forks in 25 days could be partly bot-amplified. **Plausible**.
3. **Fork-as-bookmark CN-culture**: Some CN GitHub users prefer fork-instead-of-star for bookmarking (gives offline-mirror + persistence-against-deletion). **Plausible** given Anthropic-takedown-risk awareness.
4. **Self-host-mirror anticipation**: Users may fork in anticipation of original being taken down (DMCA-style). **Plausible** given research-only license + Anthropic-internals disclosure + DMCA clause in README.
5. **Fork-to-translate / fork-to-adapt**: 19 language groups beyond original 4 may have forked for translation work. Less plausible (would expect at least some translation forks visible publicly; not directly probed).

### Why this matters for Pattern #75

bizos v37 138% inversion = clear template-use mechanism (Next.js business OS template). v53 168% inversion = **mechanism unclear**. Pattern #75 cannot auto-promote to N=2 without operator overlap-resolution at mini-audit:
- (a) PROMOTE if mechanisms unifiable as "fork-amplified-cold-start"
- (b) SPLIT into 75a template-use + 75b CN-cultural-or-bot
- (c) STAY OBSERVATION-TRACK if mechanisms too divergent

(See E2 for detailed promotion analysis.)

---

## Cross-references

- E1 — Core archive (5-doc content)
- E2 — Pattern implications (#38 38b / #29 29-absent-4 / #75 N=2)
- E4 — 42nd consecutive Storm Bear meta-entity
- C3 — Author profile + abandoned status (cluster summary)
