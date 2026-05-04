# (C) VN Localization + Storm Bear Direct Relevance

> **Type:** Entity — Storm Bear-specific meta-concept
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + VN summary]] §8, [[(C) CHANGELOG skim summary]] §7
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

BMAD-METHOD v6.3 (April 9, 2026) added **Vietnamese (vi-VN) documentation translation alongside Czech (cs-CZ)** — making BMAD the **first T1 entrant in the Storm Bear corpus with any Vietnamese localization**. Translation quality is **professional machine-translation with minimal human polish**, not native-quality. Still, its existence signals intent to serve VN users and provides a concrete adoption pathway for Storm Bear's Vietnamese operator context.

## 2. Key claims

1. **BMAD = first T1 entrant with VN translation** — ECC/Superpowers/gstack/GSD have zero
2. **Added v6.3 (2026-04-09)** — very recent, ~10 days old at wiki ingestion
3. **Bundled with Czech** — suggests batched translation effort, not VN-community-driven
4. **Translation quality = machine-translated** (honest assessment, downgrade from Phase 0 log)
5. **URL structure:** `docs.bmad-method.org/vi-vn/` — language-suffix routing
6. **Agents/workflows NOT translated** — only README + docs translated to VN
7. **No VN community signals** in repo (no VN Discord channel mentioned, no VN issues/PRs seen)

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| VN translation added v6.3 | CHANGELOG 2026-04-09 entry | High |
| Translated files: README_VN.md | Repo root directory listing | High |
| Czech also added same release | CHANGELOG | High |
| Translation quality = machine | WebFetch re-read 2026-04-19 | High |
| Agents not translated | Inferred: no VN `.md` in `bmad/bmm/agents/` visible | Medium (not post-install verified) |
| No VN community signals | Absence in README/CHANGELOG mentions | Medium |

## 4. How it works

### Translation delivery

- File: `README_VN.md` at repo root (7.5 KB)
- Structure: parallel to `README.md` (same sections, same order)
- URL routing: `docs.bmad-method.org/vi-vn/<path>` — presumed full docs translation, not just README
- Installed product: **EN agents/workflows** still ship; VN is docs-layer only

### What a VN user experiences

1. Lands on GitHub repo → sees README in EN + links to README_VN + README_CN
2. Reads README_VN in VN (machine-translation quality)
3. Installs via `npx bmad-method install` (EN CLI prompts)
4. Gets EN agent personas, EN workflow prompts, EN error messages
5. Can prompt agents in VN → agents respond in VN (LLM-level, not BMAD-level)

**Key insight:** VN support is **superficial docs layer**, not deep product localization.

## 5. Worked example — Storm Bear pilot

**Scenario:** Storm Bear onboards a VN-speaking junior engineer to BMAD

- ✅ VN engineer reads `README_VN.md` — understands framework concept
- ✅ VN engineer installs via `npx bmad-method install` — works same as EN user
- ⚠️ VN engineer sees EN agent names (Amelia, PM, Architect) — cognitive friction
- ⚠️ VN engineer reads workflow templates in EN — friction
- ✅ VN engineer prompts Amelia in VN — Claude/Amelia responds in VN (via underlying LLM)
- ❌ VN engineer reads `bmad-help` output — EN only
- ⚠️ Overall: **BMAD is accessible to VN engineers but not native-feeling**

## 6. Edges + failure modes

### Translation quality issues

- Stiff corporate tone, awkward phrasing in places (`"một mô-đun khung phát triển hướng AI"`)
- "Build More Architect Dreams" rendered literally, not idiomatically
- "Skills" untranslated while "process" localized — inconsistent
- Good-enough for docs; insufficient for marketing/community-building

### Depth of localization

- Only docs, not product — agents respond in EN by default
- No VN-specific examples (uses same EN examples)
- No regional payment/billing/community integrations (Discord = global)
- No mention of VN community size or presence

### Maintenance risk

- Translations may drift from EN as EN evolves
- No stated translation maintenance cadence (who updates VN when README changes?)
- Q3 (open): community-maintained or paid?

### Phase 0 log correction

Phase 0 log overstated VN quality as "professional-quality, full fidelity, VN-specific URL paths, contextual examples in VN". Honest downgrade:
- Quality ≠ professional-quality human; is **machine-translation with light polish**
- URL paths = language-suffixed, not VN-specific routing logic
- No contextual examples in VN

Correction logged here for future reference integrity.

## 7. Related concepts

- [[(C) 12+ Specialized Agents (Amelia Dev + PM + Architect + UX)]] — agents not translated
- [[(C) 34+ Workflows + 5 Module Ecosystem]] — workflows not translated (VN community module = potential contribution)
- [[(C) README + VN summary]] — full translation quality assessment

## 8. Cross-project (VN coverage in corpus)

| Project | Tier | VN support | Notes |
|---------|------|-----------|-------|
| **BMAD** | **T1** | ✅ README_VN v6.3 (2026-04) | **First T1 with VN** |
| ECC | T1 | ❌ | |
| Superpowers | T1 | ❌ | |
| gstack | T1 | ❌ | YC-backed but EN-only |
| GSD | T1 | ❌ | |
| goclaw | T2 | ❌ | |
| course (ai-agents-for-beginners) | T3 | ✅ | Microsoft education, multi-lang |
| notebooklm-py | T4 | ❌ | |
| deer-flow | T5 | ❌ | Chinese-primary (ByteDance) |
| autoresearch | T5 | ❌ | Karpathy EN-only |
| build-your-own-x | Outside | ✅ | Multi-lang aggregator |

**Observation:** VN support is rare in agent-tool corpus. T3 Microsoft course + T1 BMAD + outside-scope build-your-own-x are the only projects with any VN. **BMAD is the first framework-tier VN option.**

## 9. Open questions

- Who translated VN? Paid? Contracted? Claude-based? → Q3 existing
- Will translation be maintained? Cadence? → Q3 existing
- Will VN get a dedicated community channel (Discord thread? Zalo?) → Q13 existing
- Will agents/workflows themselves ever translate to VN? → Q32
- Would a native-VN polish PR be accepted? → Q23 existing
- How many VN users actually use BMAD today? → Q13 existing

## 10. Decision log

- **2026-04-09 (v6.3):** VN translation released alongside Czech
- **Unknown pre-date:** Translation work happened; no commit-level detail fetched
- **Future unknowns:** Maintenance model, potential deeper localization

## 11. Storm Bear relevance (PRIMARY FOCUS)

### Why this entity matters more than others for Storm Bear

Storm Bear operator = VN-based Scrum coach + developer. Every wiki in corpus asks: "does this framework serve VN teams?" For 9 of 11 corpus projects, answer is **no** (EN-only). BMAD's v6.3 release **changes the answer to "partially yes"** — first framework-tier option.

### Concrete Storm Bear use cases

1. **VN team onboarding:** Share `README_VN.md` link with VN junior engineers. They read framework intro in VN, lower barrier-to-entry
2. **VN team adoption pilot:** Try BMAD on a VN Scrum team. Expected friction = agent names/workflows in EN; expected benefit = structured methodology
3. **Contribution pathway:** Storm Bear could contribute native-VN polish to translation. Low-barrier OSS contribution + direct impact on other VN users
4. **Localized module:** Storm Bear could fork BMM, translate workflow prompts to VN, publish as community module (v6.3 marketplace enables this). **High-leverage contribution**

### Risks

- Machine-translation quality signals project *intent* without *depth* — Storm Bear should not over-rely on VN support
- No VN community visible — adoption = pioneering (no VN peer support)
- v6.3 is recent — translation may atrophy if no maintainer steps up

### Pilot recommendation

**Short-term (1-2 weeks):** Read README_VN yourself, assess quality first-hand, compare to your VN phrasing intuitions.

**Medium-term (1 month):** Run one Scrum ceremony using BMM + Amelia with VN team. Track friction points.

**Long-term:** If BMAD stays viable for your context, contribute VN polish PR + consider a VN community module.

## 12. Migration / adoption notes

- No migration from "no VN" — greenfield adoption
- Check `docs.bmad-method.org/vi-vn/` for evolving translation depth
- Watch CHANGELOG for VN-specific features (community channel? VN module?)

## 13. References

- `README_VN.md` — primary artifact
- `CHANGELOG.md` v6.3.0 (2026-04-09) — release note
- `README.md` §Documentation — points to translations
- Parent: [[(C) index]]
- Open questions: [[../01 Analysis/(C) open questions]] Q3, Q13, Q23, Q32
- Root vault context: `/Users/Cvtot/KJ OS Template/CLAUDE.md` — VN operator profile
