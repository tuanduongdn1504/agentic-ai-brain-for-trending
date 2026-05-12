# Entity 2 — Karpathy-derivative-distillation mechanism

## 1. The mechanism in one sentence

**Solo-engineer extracts a public-figure's social-media observations on LLM coding pitfalls, distills them into 4 actionable principles with concrete worked examples, and packages the result as a multi-platform installable behavioral artifact — explicitly attributing the source individual.**

## 2. Why this is corpus-novel

Prior corpus subjects classifying as Pattern #19 archetype 2 (individual-influence-node) were either:

| Sub-pattern | Examples | Mechanism |
|-------------|----------|-----------|
| **author-original methodology** | mattpocock-skills v57 (own teaching) / Cole Medin (BMM v0) / etc. | Author teaches OWN methodology |
| **author-original tool** | shannon v45 / aidevops v47 / etc. | Author builds OWN tool |
| **corpus-cited-individual reference** | Karpathy in autoresearch v8 (passing reference) | Reference, not artifact |
| **derivative-distillation NEW at v63** | **andrej-karpathy-skills v63** | **Author distills another individual's public observations into installable artifact** |

**Sub-archetype proposed for Pattern #19:** *derivative-distillation-of-public-observations* (a4 sub-type alongside existing a1 own-methodology / a2 own-tool / a3 corpus-cited-reference).

## 3. The distillation lineage

**Source (Karpathy X tweet):**
- Models make wrong assumptions silently → **distilled to "Think Before Coding"**
- Models overcomplicate / bloat abstractions → **distilled to "Simplicity First"**
- Models change/remove orthogonal code as side-effect → **distilled to "Surgical Changes"**
- Karpathy positive: "LLMs loop until they meet specific goals" → **distilled to "Goal-Driven Execution"**

**1-to-1 mapping** — clean distillation, not synthesis. Each principle traces to a specific Karpathy quote.

## 4. What's added beyond the source

forrestchang's contribution beyond pure quote-extraction:

1. **EXAMPLES.md (522 lines)** — 8 ❌/✅ contrastive worked examples illustrating each principle in concrete code; this is **original pedagogy** not derivative
2. **3-platform packaging** — Claude Code plugin / per-project CLAUDE.md / Cursor rule; **original distribution choice** not derivative
3. **Tradeoff calibration** — explicit "judgment for trivial tasks" caveat; **original moderation** not derivative
4. **Senior-engineer-overcomplication test** — operationalizable heuristic ("Would a senior engineer say this is overcomplicated?"); **original framing** not derivative
5. **Success rubric** — 4 measurable behavioral outcomes; **original operationalization** not derivative

**Verdict:** forrestchang's value-add is **operationalization**, not novel methodology. Karpathy named the failure modes; forrestchang made them installable.

## 5. The 121K-star phenomenon — why this distillation went viral

Hypotheses (un-verified at v63 ship; observable signals only):

1. **Karpathy as 121K-star-magnet** — Karpathy posts have intrinsic viral velocity; any high-quality distillation inherits velocity
2. **"Single CLAUDE.md" simplicity sells** — install-cost ~2-min creates very low friction
3. **Anti-overengineering critique resonates with viral-coder demographic** — frustration with LLM bloat is widespread
4. **3-platform distribution maximizes reach** — Claude Code + Cursor + curl coverage spans most LLM-coder demographics
5. **Bilingual EN+ZH coverage** — Chinese developer market is ~30% of GitHub viral velocity historically
6. **Recency** — created 2026-01-27 = 102 days at observation; in early-burst window

**Pattern #52 implication:** mattpocock v57 hit ~370 stars/day; karpathy-skills hit ~1,186 stars/day. **3× velocity multiplier** despite finer granularity (1 skill vs 19 skills). Suggests Pattern #52 EXTREME-VIRAL is **driven by author-celebrity-or-source-celebrity** more than skill-count or content-density.

## 6. Comparison to mattpocock-skills v57 (Pattern #52 N=1 baseline)

| Dimension | mattpocock-skills v57 | andrej-karpathy-skills v63 |
|-----------|----------------------|----------------------------|
| **Author** | Matt Pocock (TypeScript educator, ~270K X followers) | forrestchang (Multica founder, modest X following) |
| **Source of authority** | Author's OWN expertise | DERIVATIVE — Karpathy's authority transferred |
| **Skills count** | 19 | 1 |
| **i18n** | EN-only | EN + ZH |
| **Platforms** | Claude Code (skills protocol) | Claude Code + Cursor |
| **Stars at observation** | ~12K → ~37K at v63 (~93 days) | 121K at 102 days |
| **Stars/day** | ~370 (at flag-time) | **~1,186** |
| **Pattern #52 status** | N=1 OBSERVATIONAL FLAG (stale) | **N=2 strengthening** |

**Key insight:** **derivative-distillation can outperform author-original** when the source individual's authority is transferable (Karpathy's authority > Pocock's authority in viral-coder demographic).

## 7. Pattern Library implications

**Pattern #19 archetype 2 individual-influence-node — NEW sub-type a4:**

> **a4 derivative-distillation-of-public-observations** — solo-engineer extracts public-figure observations on LLM/coding/methodology and packages them as installable behavioral artifact with explicit source attribution.
>
> **N=1 stale-flagged at v63 with karpathy-skills as baseline.** Un-stale criterion: 2nd corpus subject performing same mechanism (e.g., a future "andrew-ng-skills" or "fast.ai-skills" derivative-distillation) with similar attribution discipline.

**Pattern #57 Recursive Corpus Reference — 57c strengthening:**

> Karpathy is corpus-foundation-individual (LLM Wiki pattern → Storm Bear vault root CLAUDE.md). v63 subject is direct derivative of corpus-foundation-individual's public observations. **Recursive-citation-back-to-corpus-origin observation** — corpus-cited-individual's authority returns through derivative artifact.

## 8. The Multica connection (ecosystem-portfolio-builder)

forrestchang's README opens with cross-promotion to [Multica](https://github.com/multica-ai/multica) — *"open-source platform for running and managing coding agents with reusable skills."*

**Pattern #19 ecosystem-portfolio-builder sub-type N=2 (sister to gotalab v61):**

| Author | Portfolio products | Strategic shape |
|--------|-------------------|-----------------|
| gotalab v61 | cc-sdd + skillport + uxaudit + claude-code-marimo (4 products) | Solo-Japanese SDD/skills ecosystem |
| **forrestchang v63** | **karpathy-skills + Multica (2 products)** | **Viral-distillation + commercial-platform-play** |

**N=2 sub-type within Pattern #19 first-mover-authority-without-lineage ecosystem-portfolio-builder.** Strengthens v61 candidate registration.

## 9. Risks of derivative-distillation as model

Counter-considerations the artifact does NOT address:

1. **Source-individual-disagreement risk** — Karpathy could publicly reject the distillation (no evidence of this; speculative)
2. **Source-content-evolution risk** — Karpathy's views evolve; distillation freezes a snapshot
3. **Attribution drift** — third-party forks could remove Karpathy citation while keeping content
4. **Plagiarism perception** — though attribution is clean, distillation = repackaging another's labor for marketplace participation

**Operator-decision frame:** the artifact is functionally useful regardless of these risks; treating it as a behavioral overlay (not as Karpathy-endorsed) is the safe stance.

## 10. Strategic significance — why the mechanism matters

Derivative-distillation is **scalable**:
- For every public-figure observation thread, a parallel artifact could exist
- Karpathy / Andrew Ng / Yann LeCun / fast.ai team / etc. — each generates social-media observations on LLM/coding
- Each could be distilled by a different solo-engineer following the karpathy-skills template

**Implication for corpus:** if 2-3 more derivative-distillation artifacts appear in the next 5-10 wikis, Pattern #19 a4 sub-type promotes from N=1 to N=2-N=3 with structural confirmation. This is a **fast-emerging mechanism** worth tracking.

## 11. Counter-evidence to track

Pattern #52 EXTREME-VIRAL N=2 strengthening at v63 should NOT be over-celebrated until:
- 6mo+ velocity sustained (not burst-and-decay)
- 2+ subjects confirm sub-pattern (not Karpathy-celebrity-specific outlier)
- Engagement metrics beyond stars (forks 12K = ~10% star ratio = healthy; watchers 639 = ~0.5% = LOW signal of active interest)

The **639 watchers / 121K stars = 0.005 ratio** is notably low. mattpocock-skills similar ratio (need verification at v66 audit). Suggests stars = drive-by interest; sustained-engagement signal is forks not watchers.

## 12. Relationship to user's substitution question

User asked whether mattpocock + karpathy combo can replace cc-sdd. Both belong to **behavioral-overlay artifact category** (this entity); cc-sdd is **methodology-workflow-harness category**.

**Behavioral overlay** = modifies HOW (assumptions / simplicity / surgicalness / goal-orientation)
**Methodology harness** = adds NEW workflow phases (spec → plan → tasks → impl → adversarial review)

**Different categories. Combo cannot substitute. Can complement.** Full analysis in Phase 4b deliverable.

## 13. Pattern #19 promotion trajectory

Pattern #19 currently CONFIRMED at corpus level. v63 strengthens 2 sub-archetypes within already-confirmed pattern:
- a4 derivative-distillation NEW sub-type N=1 stale-flagged
- ecosystem-portfolio-builder existing sub-type N=2 (gotalab v61 + forrestchang v63)

**v66 audit deliberation:** does Pattern #19 sub-type a4 promote to confirmed-sub-type at N=2? Need 2nd derivative-distillation observation. Track for v64-v68 wikis.
