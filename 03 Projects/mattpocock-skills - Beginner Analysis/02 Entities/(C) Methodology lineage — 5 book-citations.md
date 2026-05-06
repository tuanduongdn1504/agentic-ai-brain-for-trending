# Entity 3 — Methodology lineage: 5 book-citations + corpus-internal-anti-pattern foils

## 1. Identity

mattpocock/skills README contains **5 explicitly-cited intellectual sources** — 4 named-author software-engineering books + 1 grouping of 3 prior corpus subjects framed as anti-pattern foils. This is the **most book-citation-dense methodology lineage** in the Storm Bear corpus to date.

## 2. The 5 cited sources

### Citation 1 — Pragmatic Programmer (Hunt + Thomas)
- **Cited 2× in README** (problem-#1 misalignment + problem-#3 code doesn't work)
- Quotes used:
  - "No-one knows exactly what they want" (frames grilling-session need)
  - "Always take small, deliberate steps. The rate of feedback is your speed limit." (frames feedback-loop philosophy in `/diagnose` + `/tdd`)
- **Skill alignment**: `/grill-me` + `/grill-with-docs` + `/diagnose` + `/tdd`

### Citation 2 — Domain-Driven Design (Eric Evans)
- **Cited 1× in README** (problem-#2 verbosity)
- Quote used: "With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model."
- **Skill alignment**: `/grill-with-docs` (CONTEXT.md domain-glossary) + `/improve-codebase-architecture` (deepening-via-shared-language)

### Citation 3 — Extreme Programming Explained (Kent Beck)
- **Cited 1× in README** (problem-#4 ball-of-mud)
- Quote used: "Invest in the design of the system every day."
- **Skill alignment**: `/improve-codebase-architecture` (continuous-investment) + `/tdd` (red-green-refactor implicit Beck-lineage)

### Citation 4 — A Philosophy Of Software Design (Ousterhout)
- **Cited 1× in README** (problem-#4 ball-of-mud)
- Quote used: "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
- **Skill alignment**: `/improve-codebase-architecture` + `/tdd` deep-modules sister-doc + `/zoom-out` (system-context perspective)

### Citation 5 — Anti-pattern foils (3 prior corpus subjects)
- **Cited 1× in README** (introduction paragraph 3)
- "Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control..."
- **Negative citation**: positions mattpocock/skills as anti-corpus-internal-class

## 3. Lineage type: book-citation vs individual-name

### Storm Bear corpus prior individual-name lineage observations

| Wiki | Cited individual | Wiki tier |
|---|---|---|
| v10 autoresearch | Karpathy | T1 |
| v17 spec-kit | (Karpathy / vibe-coding spectrum implicit) | T1 |
| v18 agency-agents | John Lam (no-lineage explicit) | T1 |
| v20 fish-speech | Research-paper-chain (academic) | outside-scope |
| Multiple | Boris Cherny / Lance Martin / Anthropic-team | various |

These are **individual-name lineage** — single named human as influence-node.

### v57 mattpocock/skills lineage type: NAMED-BOOK lineage

5 cited sources use book-as-citation-unit (4 books + 1 corpus-subject-grouping). Individual authors named **only in book attribution context** (Hunt + Thomas + Evans + Beck + Ousterhout). This is structurally distinct from individual-name lineage:

- Individual-name lineage: cites person directly (e.g., "as Karpathy advocates")
- Book-citation lineage: cites text directly (e.g., "Pragmatic Programmer states...")

**Pattern #19 archetype 4 sub-variant emerging:** book-citation lineage as 1st N=1 stale-flagged sub-variant within archetype 4. Promotion path: N=2 by v62 → formalize as Pattern #19 archetype 4 sub-variant within already-confirmed pattern.

## 4. Sources curated as "decades of engineering experience" claim

README opener: "These skills are designed to be small, easy to adapt, and composable. They work with any model. **They're based on decades of engineering experience.**"

The 4 cited books span:
- Pragmatic Programmer (1999/2019 anniversary)
- Domain-Driven Design (2003)
- Extreme Programming Explained (1999/2004 2nd ed)
- Philosophy Of Software Design (2018/2021 2nd ed)

Mean publication year: ~2008. Cumulative books span: ~22 years. "Decades of engineering experience" claim is **citation-supported** (not personal-authority claim, unlike v55 automate-faceless-content "OG AI Wizard" which had no citation backing).

**Counter to v55 cautionary contrast:** mattpocock/skills uses authority-via-citation (proper) vs v55 used personal-authority-claim ("OG AI Wizard" with no backing). v57 inverts the v55 cautionary pattern — both subjects are commercial-educator-archetype but with opposite authority-construction mechanisms.

## 5. Methodology-cluster cross-pattern observations

### Cluster: Anti-process-owning + pro-fundamentals + small-composable

Mattpocock/skills positions in this cluster:
- **Anti-process-owning**: rejects GSD/BMAD/spec-kit "owning the process" framing
- **Pro-fundamentals**: 4 books all = software-engineering-classics
- **Small-composable**: 13 active skills, none monolithic; explicit "composable" claim
- **Anti-vibe**: most-explicit anti-vibe positioning in corpus to date

### Pattern #51 Vibe-Coding Spectrum positioning

| Pole | Wiki examples |
|---|---|
| **Anti-vibe (max)** | spec-kit v17 (9-article constitution) + **mattpocock/skills v57 (most-explicit "real engineering, not vibe coding")** |
| Anti-vibe-leaning | tdd v? / Pragmatic-Programmer-cited subjects |
| Center | Most agent skills bundles |
| Pro-vibe-leaning | awesome-design-md v25 (vibe-coded design templates) |
| **Pro-vibe (max)** | automate-faceless-content v55 ("$1K/mo passive autopilot") |

mattpocock/skills v57 strengthens anti-vibe pole at maximum-explicit position. Cross-corpus observation: anti-vibe-pole subjects cite each other (Pragmatic-Programmer + Beck + Ousterhout = anti-vibe canon); pro-vibe-pole subjects cite social-media (Facebook + YouTube + affiliate-funnel mechanics).

## 6. Notable absences from methodology lineage

mattpocock/skills cites NO:
- AI-research (no Karpathy / Bengio / Hinton / OpenAI-team / Anthropic-team)
- LLM-architecture lineage
- Agentic-engineering canonical figures (Boris Cherny / Lance Martin)
- Academic AI papers
- Industry blog posts or Twitter threads
- Other agent-tooling authors

Author's lineage is **strictly software-engineering-classical-books + anti-corpus-process-owning**. AI-aware but AI-research-agnostic.

This is a **distinct lineage stance**: skills work through software-engineering fundamentals applied to AI-tooling, NOT through AI-specific theory. Implicit claim: AI-tooling failure modes are **engineering misalignment problems**, not novel AI problems.

## 7. Pattern #19 archetype 4 implications

**Observations strengthening archetype 4 (no-explicit-individual-lineage):**

| Wiki | Lineage style |
|---|---|
| v18 agency-agents | "no-lineage explicit" |
| v55 automate-faceless-content | "OG AI Wizard" personal-authority claim (NO citation) |
| **v57 mattpocock/skills** | **Book-citation lineage (NEW sub-variant: cited-via-classical-books)** |

v57 introduces book-citation as 1st named-citation sub-variant within archetype 4 (which was previously defined as "no individual-name-lineage"). Refinement candidate: archetype 4 sub-variant for citation-supported authority vs personal-authority-claim vs no-claim.

## 8. Cross-wiki references (within entity)

- v10 autoresearch (Karpathy lineage — individual-name)
- v17 spec-kit (vibe-coding-spectrum anti-pole; cited by mattpocock/skills)
- v18 agency-agents (no-lineage explicit precedent)
- v20 fish-speech (research-paper-chain academic precedent)
- v25 awesome-design-md (pro-vibe pole opposite)
- v55 automate-faceless-content (personal-authority-claim contrast)
- v51 Pattern #51 Vibe-Coding Spectrum

## 9. Recommendation for next mini-audit

| Action | Status |
|---|---|
| Register Pattern #19 archetype 4 sub-variant **book-citation-lineage** N=1 stale-flagged v62/v67 | NEW candidate |
| Strengthen Pattern #51 anti-vibe pole at "most-explicit-positioning" axis | Within-pattern strengthening |
| Pattern #19 archetype 4 14th+ data point | Strengthen existing |
| Defer process-owning-meta-frameworks meta-category | Until 2nd external author convergence |
