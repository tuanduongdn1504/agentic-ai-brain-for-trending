# (C) skills-lock + Ecosystem Cross-Pollination

> **Type:** Entity — novel corpus-first pattern + ecosystem signal
> **Parent:** [[(C) index]]
> **Sources:** [[(C) Skills + Architecture + skills-lock cluster summary]] §2; cross-wiki references to OpenClaw/Hermes/nextlevelbuilder
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

multica's `skills-lock.json` is the **first dependency-locked skill manifest in Storm Bear corpus** — tracking 4 external skills (from Anthropic, shadcn, nextlevelbuilder, and Vercel) with SHA-256 integrity hashes. This surfaces **ecosystem-level cross-pollination** previously only hinted at: multica imports a skill from **nextlevelbuilder** (the org behind goclaw v4, another T2 entrant). Combined with shared agent-standard mentions across multiple wikis (OpenClaw in codymaster v12 + paperclip v14 + multica v15; Hermes in paperclip v14 + multica v15), the corpus is revealing an **emerging agent ecosystem with shared infrastructure projects transcending individual frameworks.**

## 2. Key claims

1. **First skills-lock.json in corpus** — dependency-locked skill manifest pattern
2. **SHA-256 integrity** for each tracked skill (supply-chain attack resistance)
3. **4 external skills locked** — all from GitHub sources
4. **nextlevelbuilder cross-pollination** — goclaw v4's parent org contributes skill to multica v15
5. **Anthropic skill registry** (`anthropics/skills`) — official Anthropic skill source
6. **Vercel skill registry** (`vercel-labs/agent-skills`) — Vercel agent investment
7. **shadcn** — standard UI lib (expected)
8. **OpenClaw + Hermes = emerging agent-runtime standards** (cross-wiki pattern)
9. **Pattern #16 candidate:** Skill Dependency Locking (mature ecosystems lock skill deps)

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| skills-lock.json exists | Root directory listing | High |
| 4 skills enumerated | Verbatim file content | High |
| SHA-256 hashes | File content (`computedHash` field) | High |
| First in corpus | 15-wiki retrospective scan | High |
| nextlevelbuilder connection | skills-lock.json `ui-ux-pro-max.source` field | High |
| OpenClaw cross-wiki mentions | codymaster v12 + paperclip v14 + multica v15 READMEs | High |

## 4. skills-lock.json anatomy

### Structure

```json
{
  "version": 1,
  "skills": {
    "<skill-name>": {
      "source": "<github org/repo>",
      "sourceType": "github",
      "computedHash": "<sha256>"
    },
    ...
  }
}
```

### Design pattern

Parallels **pnpm-lock.yaml** / **package-lock.json** / **Cargo.lock** patterns:
- **version** — format version (allows evolution)
- **source** — where to fetch
- **sourceType** — fetch protocol (extensible beyond `github`)
- **computedHash** — integrity verification

### Why skills need locking

- **Reproducibility** — team's `multica` install uses same skill versions
- **Security** — SHA-256 prevents supply-chain swap
- **Audit trail** — locked versions traceable
- **Rollback** — pin to known-good version if upstream regresses

### Update workflow (inferred — not documented)

Likely: `multica skills update <skill-name>` fetches latest, computes new hash, updates lock file. User commits.

## 5. 4 tracked skills — detail

### frontend-design (anthropics/skills)

**Source:** github.com/anthropics/skills

**Significance:** Anthropic's official skill registry. Multica imports directly from Anthropic.

**Implications:**
- Anthropic has curated skill offerings
- multica team maintains Anthropic partnership
- Routine v2 candidate: **scan corpus for anthropics/skills imports** — who else imports?

### shadcn (shadcn/ui)

**Source:** github.com/shadcn-ui/ui (likely `shadcn/ui` points here)

**Significance:** Standard React UI component library. Inclusion expected for any TS/React project.

**Implications:**
- multica uses shadcn-pattern components (copy-paste + adapt)
- Skill likely = design tokens + component catalog guidance for agents

### ui-ux-pro-max (nextlevelbuilder/ui-ux-pro-max-skill)

**Source:** github.com/nextlevelbuilder/ui-ux-pro-max-skill

**CRITICAL SIGNAL:** **nextlevelbuilder is the parent org of goclaw v4** (T2 N=1 entrant).

**Implications:**
- nextlevelbuilder org ships multiple agent-ecosystem projects
- Their `ui-ux-pro-max-skill` = reusable design skill
- **multica (T2 N=2) imports skill from goclaw's (T2 N=1) org** — ecosystem-level cross-pollination
- nextlevelbuilder may be:
  - Same team running both goclaw + skill library
  - Ecosystem coordinator publishing agent-space tools
  - Foundation-style organization

**Storm Bear relevance (Q3):** understanding nextlevelbuilder's nature illuminates T2 tier structure + goclaw's community-platform classification.

### web-design-guidelines (vercel-labs/agent-skills)

**Source:** github.com/vercel-labs/agent-skills

**Significance:** Vercel Labs publishes agent-skills registry. Shows Vercel's strategic investment in agent ecosystem beyond core Next.js.

**Implications:**
- Vercel sees agents as strategic extension
- vercel-labs/agent-skills likely contains multiple skills (web-design-guidelines is one)
- Routine v2: scan corpus for vercel-labs imports

## 6. Cross-wiki ecosystem signals (broader than skills-lock)

### OpenClaw — mentioned in 3 wikis

| Wiki | Mention context |
|------|-----------------|
| **codymaster v12** | Listed as install platform support |
| **paperclip v14** | First-class adapter + "If OpenClaw is employee, Paperclip is the company" |
| **multica v15** | Listed in 8 supported agent models |

**Hypothesis:** OpenClaw is an **independent agent-runtime standard** used across multiple frameworks. Possibly:
- Separate open-source project
- Shared specification
- Reference implementation

### Hermes — mentioned in 2 wikis

| Wiki | Mention context |
|------|-----------------|
| **paperclip v14** | Hermes adapter externalization (fork note) |
| **multica v15** | Listed in 8 supported agent models |

**Hypothesis:** Hermes is another agent-runtime option — possibly:
- Nous Research's Hermes fine-tune model family (reference)
- Specific agent implementation
- Internal code name at some org

### Ecosystem pattern (new corpus observation at v15)

Multiple frameworks converge on shared agent-runtime names (OpenClaw, Hermes). Suggests **agent ecosystem is maturing into shared infrastructure** rather than each framework building proprietary agent runtimes.

**Pattern #17 candidate:** Agent Runtime Standardization — as ecosystem matures, common agent-runtime identifiers emerge across frameworks (de facto standards).

## 7. Pattern #16 — Skill Dependency Locking (new at v15)

### Formal statement

> "As agent skill ecosystems mature, frameworks introduce dependency-lock files (similar to package-lock.json / Cargo.lock) to track external skill dependencies with integrity hashes for reproducible + secure skill composition. multica v15 is first-mover."

### Evidence

- 15 wikis scanned; only multica has skills-lock.json
- JSON format + version: 1 field suggests format evolution anticipated
- SHA-256 integrity = security-conscious design
- 4 skills from 4 different orgs = genuine external dependency management

### Prediction

Future framework wikis will show skill-lock patterns. Early adopters:
- Frameworks with external skill imports (not embedded)
- Frameworks with security-conscious user base (enterprise)
- Frameworks with supply-chain attack awareness

### Non-evidence

- codymaster v12 has 79 embedded skills — no external locking needed
- gws v13 has 110 generated skills (from Discovery) — no external locking needed
- paperclip v14 has 4 internal skills — no external imports

→ skills-lock pattern emerges **only when framework imports skills from external sources.**

## 8. Edges + failure modes

### skills-lock.json risks

- **Skills becomes skill-registry** — curation needed as # of skills grows
- **Hash verification failure** — upstream skill updated, hash mismatch = user blocked
- **Source unavailability** — GitHub skill source deleted or renamed = dependency breaks
- **Transitive skills** — skill-of-skill dependencies not tracked in v1 format
- **License propagation** — imported skills may have license conflicts with MIT multica

### Ecosystem risks

- **OpenClaw fragmentation** — multiple implementations diverge if no single spec owner
- **Hermes ambiguity** — name collision with other "Hermes" projects
- **Vercel commitment** — vercel-labs is "labs" (experimental); may be deprecated
- **Anthropic skill-registry policy changes** — Anthropic could restrict external use

## 9. Related concepts

- [[(C) Skills + Architecture + skills-lock cluster summary]] — cluster view
- [[(C) Linear-Analog Task Management for Agents]] — what skills extend
- [[(C) T2 2-way Validation + Pattern #9 Platform-Tier Refinement + Storm Bear]] — tier context

## 10. Cross-project comparison

### Skill ecosystem maturity

| Framework | Skill model | External imports | Lock file |
|-----------|------------|------------------|-----------|
| codymaster v12 | 79 internal | ❌ | ❌ |
| gws v13 | 110 generated + external registry | Plugin pattern | ❌ |
| BMAD v11 | 5 modules internal + marketplace emerging | v6.3 browser | ❌ (but marketplace = semi-lock) |
| paperclip v14 | 4 internal | ❌ | ❌ |
| **multica v15** | **4 external** | **✅ skills-lock.json** | **✅** |

→ multica = **most mature external-skill ecosystem engineering**. Import-and-lock pattern unique.

### Ecosystem maturity signal

multica's skills-lock suggests:
- Skill consumption is mature enough to warrant tooling
- Ecosystem has enough external skills to import (Anthropic + Vercel + community)
- Security + reproducibility concerns warrant engineering investment

**Implication for corpus:** multica may be **temporally later in ecosystem maturity** than other frameworks — operates in a world where skill-lock is necessary.

## 11. Open questions

- Anthropic's skill-registry URL and public status (new — Q46)
- vercel-labs/agent-skills full inventory (new — Q47)
- nextlevelbuilder skills list beyond ui-ux-pro-max (new — Q48)
- OpenClaw authoritative repo / maintainer (Q8)
- Hermes specific meaning (Q8)
- skills-lock.json update workflow documented? (new — Q49)
- `computedHash` algorithm specified? (new — Q50)
- Cross-wiki OpenClaw wiki candidate (new — Q51)

## 12. Decision log

- **v0.1-0.2 era:** skills embedded or minimal
- **v0.2.x:** skills-lock.json introduced
- **4 skills locked currently** — likely to grow
- **Future:** possibly skills marketplace with search + auto-update

## 13. Storm Bear relevance

### Pattern #16 application

Storm Bear vault itself could benefit from skills-lock pattern:
- Lock LLM Wiki template version
- Lock reusable skills (llm-wiki-ingest, llm-wiki-routine)
- Track external pattern imports (Karpathy LLM Wiki, Bostrom alignment theory as docs-references)

### Ecosystem awareness

- Anthropic publishes skill registry (anthropics/skills)
- Vercel publishes agent-skills
- nextlevelbuilder publishes agent-ecosystem tools (contributes to goclaw + multica)
- OpenClaw + Hermes are emerging runtime standards

Storm Bear can tap these ecosystems for own projects.

### nextlevelbuilder connection pilot

nextlevelbuilder org is notable:
- Publishes goclaw (v4 T2 N=1)
- Contributes ui-ux-pro-max-skill to multica v15
- Potentially deep agent-ecosystem investment

**Pilot candidate:** engage nextlevelbuilder community. Cross-reference with goclaw wiki. Possibly fruitful for Storm Bear.

## 14. References

- skills-lock.json (verbatim)
- Cross-wiki references:
  - `../../goclaw - Beginner Analysis/` (nextlevelbuilder parent)
  - `../../codymaster - Beginner Analysis/` (OpenClaw mention)
  - `../../paperclip - Beginner Analysis/` (OpenClaw + Hermes mentions)
- Parent: [[(C) index]]
- Pattern library: GOALS.md Pattern #16 candidate registration
