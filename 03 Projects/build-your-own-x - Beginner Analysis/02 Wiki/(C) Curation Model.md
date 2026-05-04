# (C) Curation Model

> Entity page — Community concept
> Sources: Contribution guidelines + CodeCrafters maintenance + CC0 license + PR/issue flow
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Curation Model** = how build-your-own-x maintains 491K-star quality across ~400-600 entries submitted by thousands of contributors across 10 years. Not code gatekeeping — **taste + format + community consensus**. Curated by Daniel Stefanovic initially, now CodeCrafters, Inc. team.

## 2. Why it matters / Sao quan trọng

**Aggregators fail without curation.** Unfiltered aggregators → spam, SEO farms, dead links, low-quality content. Curation = what makes build-your-own-x useful after 10 years.

### Curator's 3 jobs
1. **Format consistency** — reject PRs not matching `[**Language**: _Title_](URL)`
2. **Quality gate** — accept tutorials that teach building, reject using-tutorials
3. **Category stewardship** — promote Uncategorized → own category when ready; prevent category bloat

### Why not automate?

- Format checks = automatable
- Quality assessment = human judgment (needs read tutorial + evaluate)
- Category decisions = require community pulse

→ **Human curator irreplaceable** at current scale.

## 3. Curation responsibilities breakdown

### Curator (Daniel → CodeCrafters)
- Final merge decisions
- Category restructuring
- Quality bar enforcement
- Community moderation (rare)

### Community (contributors + reviewers)
- Submit PRs
- Review + react to pending PRs
- Flag broken links via issues
- Suggest new categories

### Infrastructure (GitHub)
- Hosts content + history
- Renders Markdown
- Provides PR/issue mechanics
- Free for public repos

## 4. PR flow detailed

```
Contributor forks repo
  ↓
Contributor edits README.md (single file)
  ↓
Contributor submits PR với:
  - Tutorial URL
  - Standardized format
  - Brief description
  ↓
Community comments + reactions (👍 / 👎)
  ↓
Curator reviews:
  - Format correct? 
  - Content teaches building?
  - Not duplicate?
  - Link works?
  ↓
Accept → merge
  OR
Reject → close với explanation
  OR
Request changes → contributor updates PR
```

### Review bottleneck
- 491K stars × small curator team = review backlog expected
- Pending PRs may sit weeks/months
- Community reactions = voting (higher-voted PRs prioritized)

### Spam defenses
- Curator manual review catches most spam
- No automated URL checking
- SEO link farm PRs get rejected on content quality
- Some spam slips through; community flags via issues

## 5. Implicit quality criteria

From observing accepted vs rejected PRs (inferred):

### Accepted
✅ Tutorial teaches building from scratch
✅ Has working URL (not paywall-only)
✅ Correct language tag
✅ Unique (not duplicate of existing)
✅ Tutorial has substance (not 3-paragraph hello-world)

### Rejected / ignored
❌ Using-tutorial (not building)
❌ Blog spam
❌ Paywall-only (unless exceptionally valuable)
❌ Dead link
❌ Self-promo without teaching value
❌ Malformed Markdown

### Gray area
⚠️ Book (paid): accepted if classic/foundational
⚠️ Video-only: accepted if `[video]` tag
⚠️ Large commercial course: case-by-case
⚠️ AI-generated tutorial: increasingly controversial

## 6. Evolution of curation over 10 years

### Phase 1: Solo Daniel (2016-~2022)
- Personal project
- Slow careful curation
- Taste-defining decisions
- Initial 28 categories established

### Phase 2: CodeCrafters takeover (~2022-present)
- Company-sponsored maintenance
- Larger team reviews
- Business interests may subtly shape decisions
- Banner + codecrafters.io link added

### Phase 3: Future (speculative)
- **AI-generated tutorials flood?** — AI can author "build your own X" content at scale; curator needs new filters
- **LLM coding copilots change learning?** — does Feynman framing weaken when AI writes code for you?
- **Category expansion pressure?** — AI agents, Web3, etc., want categories

## 7. Comparison to sibling curation approaches

### Solo-curator Storm Bear vault
- **Curator:** Cvtot (+ Claude)
- **Scale:** 8 wikis
- **Governance:** implicit (Cvtot's taste)
- **Feedback loop:** Cvtot + occasional team feedback

### Community-curator build-your-own-x
- **Curator:** Daniel → CodeCrafters
- **Scale:** ~500 entries, thousands PRs
- **Governance:** implicit criteria + community consensus
- **Feedback loop:** PR comments + reactions + issues

### Vendor-curator ai-agents-for-beginners (Microsoft course)
- **Curator:** Microsoft Learn team
- **Scale:** 14 lessons
- **Governance:** Corporate standards + peer review
- **Feedback loop:** Employee review + customer feedback

### Solo-maintainer notebooklm-py
- **Curator/maintainer:** teng-lin
- **Scale:** 1 library
- **Governance:** solo decisions
- **Feedback loop:** GitHub issues + PRs

**Pattern:** Curation style correlates với project scale + resource availability.

## 8. Trade-offs / Limitations

### Strengths của build-your-own-x model
- **Sustainable** — company-funded curation
- **High bar** — 491K stars = trust signal
- **Scalable** — flat structure + single-file edits work
- **Community-driven** — wisdom of crowds via reactions

### Weaknesses
- **Review bottleneck** — PRs sit forever
- **Business bias risk** — CodeCrafters may favor topics aligning với paid courses
- **No quality criteria documentation** — new contributors must infer
- **Language bias** — JS/Python over-represented
- **English-only** — VN contributors excluded

## 9. Governance patterns observed

### Pattern 1: Small team, high bar, slow pace
build-your-own-x follows this. Stable; doesn't explode with low-quality content.

### Pattern 2: Large team, medium bar, fast pace
awesome-* lists often follow. More entries but quality variance.

### Pattern 3: Solo maintainer, high variance
Many single-topic awesome lists. Quality tied to maintainer's time + interest.

### Pattern 4: Vendor-funded, corporate bar, controlled pace
Microsoft Learn, AWS docs. High quality but constrained by corporate agenda.

**build-your-own-x = Pattern 1** (sustainable version).

## 10. Common pitfalls for curator / contributor

### Curator pitfalls
1. **Neglect** — PR backlog kills community energy
2. **Inconsistent criteria** — accept X one week, reject similar Y next week
3. **Business capture** — favor company's paid product competitors
4. **Over-expansion** — accept marginal categories → dilution
5. **Under-expansion** — reject genuinely new topics → stagnation

### Contributor pitfalls
1. **Drive-by PR** — submit without checking for duplicates
2. **Self-promotion** — submit own tutorial without reciprocal community engagement
3. **Format sloppiness** — get rejected purely on format
4. **Scope creep** — suggest unrelated restructures via PR

### Community reviewer pitfalls
1. **Silent review** — miss opportunity to guide contributors
2. **Emoji spam** — 👍 on low-quality PRs inflates false signals
3. **Gatekeeping** — reject newcomer PRs without constructive feedback

## 11. When curation models matter

### High-stakes cases
- **Public aggregator** (build-your-own-x) — bad curation → reputation loss
- **Enterprise knowledge base** — bad curation → wrong decisions downstream
- **Scientific wiki** (Wikipedia) — bad curation → misinformation harm

### Lower-stakes cases
- **Personal notes** — curator = you; errors only affect you
- **Team internal wiki** — small audience, self-correcting

Storm Bear vault = **currently lower-stakes** (personal) but could transition higher-stakes if published publicly.

## 12. Storm Bear vault relevance

### Current Storm Bear curation
- **Curator:** Cvtot + Claude
- **Criteria:** Implicit (wiki = 13-section format, published guide = bilingual, etc.)
- **Governance:** Solo decisions
- **Review:** Routine self-regulates (Phase 4b taxonomy decisions)

### Lessons for scaling Storm Bear governance

If Storm Bear goes public:

1. **Document criteria explicitly** — format spec, quality bar, scope
2. **Choose license** — CC0 for wiki content (build-your-own-x model), MIT for skills
3. **Accept community contributions** — PR flow for team-extensions
4. **Review bottleneck plan** — rotate curators, batch reviews weekly
5. **Quality vs volume trade-off** — prefer build-your-own-x quality model

### Short-term actions
- [ ] Document 13-section entity page format explicitly
- [ ] Codify routine v2 với formal Phase 4b decision rules
- [ ] Write CONTRIBUTING.md if Storm Bear opens to community
- [ ] License decision when publishing

## 13. References / Nguồn

- Source: [[(C) Governance + Curation cluster summary]] (CodeCrafters + CC0 + contribution flow)
- Related entities:
  - [[(C) 29 Categories Taxonomy]] (what gets curated)
  - [[(C) Feynman Philosophy Applied to Learning]] (why curate toward building tutorials)
  - [[(C) Storm Bear Vault — Knowledge Architecture Lessons]] (curation lessons synthesis)
- Sibling governance patterns:
  - `../../ai-agents-for-beginners - Beginner Analysis/02 Wiki/*` (vendor corporate curation — Microsoft)
  - `../../notebooklm-py - Beginner Analysis/02 Wiki/*` (solo maintainer curation)
  - `../../goclaw - Beginner Analysis/02 Wiki/*` (solo maintainer platform)
- External: CC0 spec, GitHub PR flow, awesome-lists pattern reference
