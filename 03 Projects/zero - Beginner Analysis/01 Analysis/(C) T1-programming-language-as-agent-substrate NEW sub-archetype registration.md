# (C) NEW T1 sub-archetype "programming-language-as-agent-substrate" — N=1 registration proposal

**Author:** v68 wiki ship (vercel-labs/zero, 2026-05-18)
**Status:** Phase 4b PRIMARY deliverable
**Audit target:** v69 Tier-Taxonomy Review T6 (already-scheduled; pre-registered at v66 audit; deferred from v66 Decision 14)
**Pattern Library reference:** [PATTERN_LIBRARY.md](../../../PATTERN_LIBRARY.md) — T1 Augmentation tier sub-archetype taxonomy
**Routine reference:** [llm-wiki-routine-v2.2.md](../../../05 Skills/llm-wiki-routine-v2.2.md) §"Phase 4b NEW Pattern candidate proposal-document discipline"
**Sibling proposal exemplars:** v64 Pattern #19 N=3 promotion proposal + v65 Pattern #78 N=2 promotion proposal + v67 Pattern #83 N=3 promotion proposal

---

## 1. Current state (pre-registration baseline)

**T1 Augmentation tier sub-archetypes (post-v67 baseline):**

| # | Sub-archetype | Corpus baseline | Mechanism |
|---|---------------|-----------------|-----------|
| 1 | general-purpose | v57 mattpocock-skills | 19 general-purpose skill collection |
| 2 | curated-meta | v50 awesome-claude-skills | Multi-skill aggregator with curation |
| 3 | corporate-curated | v51 agent-skills-of-vercel | Corporate-curated skill collection |
| 4 | single-artifact | v63 andrej-karpathy-skills | 7-skill viral-distillation single bundle |
| 5 | domain-vertical | v64 claude-seo | SEO-domain-vertical 25+18 collection |
| 6 | reverse-engineering-reference-archive | v65 claude-code-system-prompts | Continuous extraction of closed-vendor product internals |

**6 T1 sub-archetypes confirmed pre-v68. Zero v68 is candidate sub-archetype #7.**

### Tier T1 Augmentation definition (corpus baseline)

T1 Augmentation = framework augments AI assistant capability. Existing sub-archetypes all center on skill content augmenting an underlying agent runtime (Claude Code / Cursor / etc.).

---

## 2. NEW sub-archetype proposal: "programming-language-as-agent-substrate"

### Formal statement

> A framework whose primary artifact is a programming language (with compiler/runtime), explicitly designed with AI agents as the primary users from day one. Agents READ, WRITE, and DEBUG programs in this language; the language's syntax, standard library, tooling, and skill content are all optimized for agent consumption rather than human consumption. Skill content is bundled into the language runtime (compiler binary) rather than distributed as static files.

### Distinguishing properties (4)

A subject qualifies as "programming-language-as-agent-substrate" sub-archetype if ALL 4 properties hold:

1. **Primary artifact is a programming language** with its own compiler/runtime/interpreter (not a skill collection, not a service, not a plugin)
2. **Agents are PRIMARY users**, explicit in framework's design documentation (not augmentees of humans; not afterthought tooling-for-agents)
3. **Language-level commitments to agent-readability** (design axioms enforcing structural choices like regularity-over-syntax, standard-library-depth, structured-output)
4. **Skill content bundled with runtime** OR explicitly version-coupled with runtime artifact (not distributed as static skill files separable from runtime)

### v68 zero evaluation against 4 properties

| # | Property | Verdict | Evidence |
|---|----------|---------|----------|
| 1 | Primary artifact is a programming language | ✅ STRONG PASS | Zero is a programming language with its own native C compiler (`native/zero-c/`) + self-hosted compiler (`compiler-zero/`). File extension `.0`. Visible at zerolang.ai. |
| 2 | Agents are PRIMARY users (explicit) | ✅ STRONG PASS | README verbatim: *"The project is exploring what changes when agents are primary users from day one."* AGENTS.md: *"agent-first programming language"*. Explicit primary-user inversion vs traditional "language for humans + tooling for agents" framing. |
| 3 | Language-level commitments to agent-readability | ✅ STRONG PASS | 5 explicit design axioms (README §"What Zero Is Aiming For"): (1) agent-first learnability, (2) standard-library depth, (3) deterministic tooling, (4) direct DX, (5) regularity over syntax (verbose-but-regular over concise-but-irregular). |
| 4 | Skill content bundled with runtime | ✅ STRONG PASS | `skills/zero/SKILL.md` is thin discovery stub; actual skill content lives in `skill-data/` bundled into native compiler at build time; served via `zero skills get zero --full`. Version-coupled with compiler binary. |

→ **All 4 properties SATISFIED with STRONG PASS verdicts.**

---

## 3. Why this is a NEW sub-archetype (not absorption into existing)

### Distinguishing from existing T1 sub-archetypes

| Existing sub-archetype | How Zero v68 is structurally different |
|------------------------|----------------------------------------|
| general-purpose (mattpocock-skills) | mattpocock = 19 static skill files; Zero = programming language with runtime |
| curated-meta (awesome-claude-skills) | curated-meta = aggregator of others' skills; Zero = its own language with skill content as ONE bundled feature |
| corporate-curated (agent-skills-of-vercel) | corporate-curated = 28 static skill files curated by Vercel; Zero = runtime artifact, not skill curation |
| single-artifact (karpathy-skills) | single-artifact = 7 frontmatter-only SKILL.md bundle; Zero = language with compiler infrastructure |
| domain-vertical (claude-seo) | domain-vertical = 25+18 SEO-domain primitives; Zero = general-purpose programming language (not domain-vertical) |
| reverse-engineering-reference-archive (claude-code-system-prompts) | reverse-engineering = continuous extraction of closed vendor's product internals; Zero = original creation of a programming language |

**Zero v68 is structurally distinct from all 6 prior sub-archetypes.** The distinguishing trait is **primary artifact = programming language** (with compiler + ecosystem), not a skill collection or curation.

### Distinguishing from non-T1 tiers

| Tier | Why Zero v68 doesn't cleanly fit |
|------|----------------------------------|
| T2 Service | Zero is not a service; it's a language compiled offline + run locally |
| T3 Education | Zero is not educational content; it's a creation framework |
| T4 Bridge | Zero is not a bridge between two existing runtimes; it's an independent language |
| T5 Application | Zero is not an end-user application; it's developer-facing toolchain |

T1 Augmentation is the closest fit BECAUSE Zero augments agent capabilities (by giving them a language to WRITE programs in). But this is structurally weaker than other T1 sub-archetypes' augmentation claim — agents AUGMENT human users via T1 skill collections; agents USE Zero as their primary medium.

---

## 4. The alternative proposal: NEW Tier T6 Language/Runtime substrate

### Why this might be a NEW Tier rather than T1 sub-archetype #7

**Arguments for NEW Tier T6:**

1. **Foundational substrate vs augmentation:** A programming language is foundational substrate — agents DEPEND on it to perform tasks. T1 Augmentation enhances pre-existing agent capabilities; Zero PROVIDES a primary medium for agent expression.

2. **Different consumption pattern:** T1 sub-archetypes are consumed AT INVOCATION (agent invokes a skill). Zero is consumed AT WORKFLOW LEVEL (agent uses Zero as the language for entire projects).

3. **Compiler/runtime infrastructure:** All 6 prior T1 sub-archetypes are markdown/skill-content-only. Zero has substantial compiler infrastructure (`native/zero-c/`, `compiler-zero/`, `bin/zero` dispatcher, WASM playground, language server). Different artifact category.

4. **Future corpus subjects:** As agent-tooling matures, other languages/runtimes designed for agents may emerge (Anthropic AI-DSL? OpenAI agent language?). These would also need a tier home. T6 Language/Runtime substrate could accommodate this class.

**Arguments AGAINST NEW Tier T6 (for retaining T1 NEW sub-archetype #7):**

1. **Premature abstraction:** N=1 is too thin for a NEW tier. Wait until N=2+ Language/Runtime substrate subjects emerge before adding a tier.

2. **Skills protocol anchor:** Zero v68's Skill-As-Binary-Bootstrap mechanism uses the Anthropic skills protocol (T1 mechanism). Sharing protocol = sharing tier.

3. **Augmentation IS still present:** Agents using Zero ARE augmented by having a language designed for them. The augmentation axis hasn't been abandoned.

4. **Tier-taxonomy stability:** Adding tiers introduces complexity. T1-T5 has been stable for 67 wikis. Add sub-archetype first; promote to NEW Tier only if N=2+ evidence justifies it.

### Recommended audit decision

**For v69 audit:** **Adopt NEW T1 sub-archetype #7 "programming-language-as-agent-substrate"** with N=1 stale-risk-flag. Defer NEW Tier T6 decision to a future audit when N=2 evidence (a second programming-language-as-agent-substrate subject) emerges.

**Rationale:** Conservative classification. Maintains tier-taxonomy stability. Preserves the option to graduate to NEW Tier T6 later if the class proves to be more than a 1-subject anomaly.

---

## 5. Promotion criteria (3) for sub-archetype validity

For "programming-language-as-agent-substrate" to be considered structurally validated (not just one-off):

1. **All 4 distinguishing properties satisfied per subject** (per Section 2)
2. **At least 1 explicit "agent-first" or equivalent positioning statement** in framework's design documentation (axiom-level commitment, not afterthought)
3. **Skill content version-coupled with runtime** (binary-bundled, compiler-served, or equivalent runtime-coupling mechanism)

**Required for validation as sub-archetype (not just N=1 candidate):** 2+ subjects matching all 3 criteria.

**Re-evaluation:** v70 stale-check (N=2 emergence) / v75 retire-check (demote to observation if still N=1).

---

## 6. Structural diversity considerations (hypothetical N=2 candidates)

For sub-archetype #7 to reach validation, hypothetical un-stale candidates would include:

| Hypothetical candidate | Why it would qualify |
|------------------------|---------------------|
| Anthropic-published "agent DSL" | If Anthropic publishes a language explicitly designed for agent code-writing (analogous to Zero), with skill-content-bundled mechanism |
| OpenAI Codex-derived agent language | If OpenAI extracts a language sub-syntax from Codex training corpus for agent-first use |
| Independent solo programming language with agent-first framing | E.g., Karpathy-published "agent-tinygrad" or similar individual experimental language |
| Existing language adopting agent-first reframing | E.g., Python 4.0 or Rust 2.0 explicitly reframing as "agent-first" (probably won't happen, but observable) |
| Vercel Labs successor projects | If Vercel Labs publishes additional programming languages following the Zero pattern |

**Stale-risk:** Sub-archetype #7 may stay N=1 if "programming language with agent-first explicit framing" remains rare. The narrower trait (Skill-As-Binary-Bootstrap mechanism, see Section 7) may generalize faster than the full sub-archetype.

---

## 7. NEW observational candidate (sub-mechanism): Skill-As-Binary-Bootstrap

Separately from the NEW T1 sub-archetype registration, Zero v68 introduces a **sub-mechanism** that may generalize independently:

### Formal statement

> Framework or runtime ships skill content via a thin discovery-stub SKILL.md (or equivalent skill-protocol bootstrap artifact) that explicitly directs skill managers to invoke the framework's runtime/binary/compiler for the actual version-matched skill content. Skill manager registers ONE skill per framework; runtime serves N inner skills version-coupled with installed framework version. Solves skill-content-version-drift by binding content to the runtime artifact lifecycle.

### Promotion criteria (3)

1. Thin SKILL.md (or equivalent) explicitly identifies as a discovery stub
2. Stub directs agents/skill-managers to invoke runtime for actual content (e.g., `<framework> skills get <name>`)
3. Runtime serves N inner skills bundled at build time (version-coupled with framework version)

### v68 zero evaluation

✅ All 3 criteria PASS (per Cluster 3 + Entity 3 analysis).

### Re-evaluation

- v70 stale-check (N=2 emergence) / v73 retire-check.

### Cross-reference

- **Pattern #2 Distribution Evolution (CONFIRMED):** Skill-As-Binary-Bootstrap is candidate sub-variant of Pattern #2's packaging-channel evolution. Could register as Pattern #2 sub-variant rather than top-level pattern. Audit decides.
- **Pattern #57 corpus-citation chain:** Skill-As-Binary-Bootstrap uses the Anthropic skills protocol (corpus-confirmed). Strengthens Pattern #57 corpus-citation observations.

---

## 8. Recommended verdict at v69 audit

**Recommended action:** **REGISTER NEW T1 sub-archetype #7 "programming-language-as-agent-substrate"** as N=1 stale-risk-flagged at v69 Tier-Taxonomy Review T6.

**Plus secondary actions:**
- Register **NEW observational candidate Skill-As-Binary-Bootstrap** as candidate sub-mechanism (could be Pattern #2 sub-variant or top-level pattern; audit decides)
- Add v68 zero to **v69 Pattern #52 sustained-velocity test batch** (current batch: mattpocock + codex-plugin-cc + karpathy-skills + agentmemory + zero v68)
- Defer NEW Tier T6 decision to future audit (current N=1 too thin for NEW Tier)

**Confidence level:** **HIGH** for sub-archetype registration based on:
- All 4 distinguishing properties STRONG PASS for v68 zero
- Structurally distinct from all 6 prior T1 sub-archetypes
- Corpus-first observation in 67-wiki corpus history
- Pre-registered v66 deferral (Tier-Taxonomy Review T6 already on audit agenda)

**Conservative element:** N=1 stale-risk-flagged. The class needs N=2 to validate as durable sub-archetype rather than 1-subject anomaly.

---

## 9. Audit checklist (for next-audit operator deliberation)

When deliberating NEW T1 sub-archetype #7 registration at v69 audit, verify:

- [ ] All 4 distinguishing properties verified per v68 zero (Section 2)
- [ ] Structurally distinct from 6 prior T1 sub-archetypes (Section 3)
- [ ] No overlap >70% with existing tier (T1 Augmentation closest fit; Section 3)
- [ ] Promotion criteria specified (Section 5)
- [ ] Stale-risk-flag duration (v70 stale-check; v75 retire-check)
- [ ] Sub-mechanism (Skill-As-Binary-Bootstrap) registered separately (Section 7)
- [ ] Hypothetical N=2 candidates documented (Section 6)
- [ ] NEW Tier T6 vs T1 sub-archetype decision: ADOPT T1 sub-archetype #7 + DEFER T6 to future
- [ ] Auditor's independent verification: read v68 zero CLAUDE.md + Entity 1 + Entity 3 evidence

---

## 10. Evidence document cross-references

**Primary evidence sources (verifiable):**

| Source | Subject | Location |
|--------|---------|----------|
| README.md "Agent-first programming language" framing | v68 zero | [README.md](https://raw.githubusercontent.com/vercel-labs/zero/main/README.md) line 3 |
| 5 design axioms | v68 zero | README.md §"What Zero Is Aiming For" (lines 11-17) |
| AGENTS.md project direction (agent-first goals reaffirmed) | v68 zero | [AGENTS.md](https://raw.githubusercontent.com/vercel-labs/zero/main/AGENTS.md) line 5 + lines 7-22 |
| Skills protocol SKILL.md (thin discovery stub) | v68 zero | [skills/zero/SKILL.md](https://raw.githubusercontent.com/vercel-labs/zero/main/skills/zero/SKILL.md) |
| Compiler bootstrap architecture | v68 zero | AGENTS.md project layout (lines 61-68) |
| CHANGELOG v0.1.1 (skills protocol introduction) | v68 zero | [CHANGELOG.md](https://raw.githubusercontent.com/vercel-labs/zero/main/CHANGELOG.md) lines 26-34 |

**Wiki cross-references:**

- [v68 entity-3-skills-protocol-as-binary-bootstrap.md](../02 Wiki/entity-3-skills-protocol-as-binary-bootstrap.md) — Phase 4b PRIMARY entity with full NEW sub-archetype evidence catalog
- [v68 entity-1-zero-language-and-agent-first-design.md](../02 Wiki/entity-1-zero-language-and-agent-first-design.md) — agent-first framing + 5 design axioms detail
- [v68 entity-2-compiler-architecture-and-bootstrap.md](../02 Wiki/entity-2-compiler-architecture-and-bootstrap.md) — self-hosted compiler bootstrap detail
- [v68 cluster-1-readme-and-design-philosophy.md](../02 Wiki/cluster-1-readme-and-design-philosophy.md) — corpus-first observations
- [v68 cluster-3-skills-compiler-changelog.md](../02 Wiki/cluster-3-skills-compiler-changelog.md) — Skill-As-Binary-Bootstrap mechanism

**Cross-corpus references:**
- v51 agent-skills-of-vercel — corpus-baseline corporate-curated T1 sub-archetype #3
- v63 andrej-karpathy-skills — single-artifact T1 sub-archetype #4 + velocity-record
- v66 agentmemory — runtime-served skills via MCP (adjacent mechanism to v68's Skill-As-Binary-Bootstrap)

---

## 11. Post-registration follow-up (if accepted at v69)

After registration at v69 audit:

1. **Update `_patterns/03-active-candidates.md`** with NEW T1 sub-archetype #7 entry under Pattern #77 (T1 Augmentation tier sub-archetype tracking) OR as new entry
2. **Update PATTERN_LIBRARY.md** tier-taxonomy section to list 7 T1 sub-archetypes (currently lists 6)
3. **Cross-reference Pattern #2 Distribution Evolution** for Skill-As-Binary-Bootstrap sub-variant evaluation
4. **Cross-reference Pattern #57** for Anthropic skills protocol corpus-citation strengthening
5. **Set stale-check timeline:** v70 (N=2 emergence) / v75 (retire/demote-to-observation if still N=1)
6. **Track v68 zero in v69 Pattern #52 sustained-velocity test batch** alongside mattpocock + codex-plugin-cc + karpathy-skills + agentmemory
7. **Defer NEW Tier T6 decision** to future audit when N=2 emerges; meanwhile retain PROVISIONAL T1 sub-archetype #7 classification

---

## 12. Summary recommendation

**ADOPT NEW T1 sub-archetype #7 "programming-language-as-agent-substrate"** at v69 Tier-Taxonomy Review T6, registered as N=1 stale-risk-flagged with v70 stale-check + v75 retire-check.

- All 4 distinguishing properties STRONG PASS for v68 zero
- Structurally distinct from all 6 prior T1 sub-archetypes
- Corpus-first observation in 67-wiki corpus history
- Pre-registered for v66 Decision 14 deferral, now formalized
- HIGH confidence registration verdict
- Secondary: register **Skill-As-Binary-Bootstrap** as observational sub-mechanism (Pattern #2 sub-variant candidate)
- Secondary: add v68 zero to **v69 Pattern #52 sustained-velocity test batch**
- Defer NEW Tier T6 to future audit (N=1 too thin)
