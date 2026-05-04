# Vault License Decision — 2026-04-28 session 68

> **Status:** ✅ DECIDED — **MIT License** chosen for Storm Bear vault
> **v27 HIGH bundle item #5: COMPLETE**
> **Decision basis:** Operator interview answers (Q1: A / Q2: C / Q3: B / Q4: A / Q5: C) mapped to corpus Pattern #29 6-sub-context taxonomy

---

## Operator interview answers

| Q | Answer | Meaning |
|---|---|---|
| Q1 Public-release intent | **A** | YES, soon — within next 1-3 months (Phase 2-3 timeline) |
| Q2 Commercial protection | **C** | PURE PERMISSIVE — anyone can use including commercial repackaging |
| Q3 Copyleft preference | **B** | NO — derivatives can be re-licensed |
| Q4 AI-attribution | **A** | `(C)` PREFIX IS SUFFICIENT — no additional attribution required |
| Q5 Dual-license posture | **C** | NO — single license forever; no commercial tier |

**Profile cluster:** Pure-permissive minimal-friction publishing path.

## License options evaluated

| Option | Pros for Storm Bear | Cons | Verdict |
|---|---|---|---|
| **MIT** ✅ | Shortest license (~170 words) / minimal attribution / OSI-recognized / corpus-most-common / future re-license OK | None significant for knowledge-base content | **CHOSEN** |
| Apache 2.0 | Patent grant / explicit derivative-work guidance / OSI-recognized | 11.5KB verbose / NOTICE file requirements / patent grant unnecessary for non-software-patent vault content | Not chosen — adds friction without benefit |
| AGPL-3.0 | Strong copyleft / network-use clause / OSI-recognized | Conflicts with Q2=C (pure permissive) + Q3=B (no copyleft) | Rejected by Q2 + Q3 |
| SUL family | Commercial protection / corpus N=3 sub-context | Conflicts with Q2=C (pure permissive); non-OSI | Rejected by Q2 |
| PolyForm Noncommercial | Commercial restriction | Conflicts with Q2=C; non-OSI; Pattern #72 stale | Rejected by Q2 |
| No-license / informal | Zero friction | Conflicts with Q1=A (publish soon); creates legal ambiguity | Rejected by Q1 |

## Why MIT specifically (over Apache 2.0)

Both MIT and Apache 2.0 satisfy operator's Q2=C (pure permissive) + Q3=B (no copyleft) + Q5=C (no dual-license). Discriminator factors:

1. **Q4 = `(C)` prefix sufficient** → MIT's minimal attribution requirements align (just preserve copyright notice). Apache 2.0 adds NOTICE file requirements that introduce friction for solo operators.

2. **Vault content is knowledge-base, not software-with-algorithms** → Apache 2.0's explicit patent grant clauses are unnecessary. Storm Bear vault contains:
   - LLM Wiki analyses (text/markdown content)
   - Skill definitions (procedural instructions)
   - Pattern Library (structured observations)
   - No novel patentable algorithms requiring patent-grant protection

3. **Corpus precedent** → MIT is most-common license in 56-wiki Storm Bear corpus:
   - vercel-labs v51 (MIT-claim per README)
   - spec-kit v17 (MIT)
   - multica v15 (Apache 2.0; one of few Apache instances)
   - Anthropic-imported skills in awesome-claude-skills v50 (MIT)
   - Many T5/T4 entrants use MIT

4. **Future re-license posture** → MIT permits sole-copyright-holder re-licensing to any other license later (Q5=C "no dual-license now" doesn't preclude future re-license if market signal emerges; this is the n8n-could-have-started-MIT counterfactual).

5. **Solo-operator pragmatism** → Storm Bear is solo-VN-Scrum-coach without legal-counsel support for complex license enforcement. MIT's brevity + ubiquity makes it easiest to defend / explain / link / cite.

## Pattern Library impact

**Pattern #29 License-Category Diversity** — Storm Bear vault enters corpus as MIT-permissive + AI-attribution-minimal + non-software-patentable knowledge-base. This is a NEW data point but does NOT register as new candidate (consolidation-forward: routes to existing MIT-permissive observation cluster within Pattern #29).

**Pattern #57 Recursive Corpus Reference** — Storm Bear vault becomes self-referential corpus subject (vault publishes content ABOUT 56-wiki corpus). This is new structural form: vault-as-meta-corpus-subject-citing-its-own-corpus. Could be candidate for Pattern #57 sub-variant 57e at v57+ if Storm Bear vault is published AND becomes wiki subject in some future corpus iteration.

**Pattern #45 Dual-Licensing** — STAYS STALE. Q5=C confirms no dual-license posture; Storm Bear does not un-stale Pattern #45.

**No new candidates registered.** **20-streak ZERO-NEW-ACTIVE-CANDIDATES preserved at session 68 mid-execution** (license decision is internal vault-state action, not wiki-build action; doesn't count toward wiki-streak).

## Storm Bear meta implications

This decision unlocks:
- **v27 HIGH item #4** (public-release decision) — license is now defined; release granularity/timing/platform decisions can proceed
- **v27 HIGH item #2** (publishing strategy) — MIT compatibility with vercel-labs SKILL.md format + composio marketplace.json + Anthropic skills marketplace verified (all support MIT)
- **v27 HIGH item #3** (skill-lock) — MIT licensing applies uniformly to skill definitions; no per-skill license fragmentation needed

## Files created/updated at this decision

- ✅ `LICENSE.md` (vault root) — MIT license text + AI-attribution notes + cited-corpus-subject notes
- ✅ `_state/license-decision-2026-04-28.md` (this file) — decision rationale chapter
- (deferred) Root `CLAUDE.md` Vault State Architecture section — add chapter pointer to license-decision file (next phase)

## Storm Bear-specific notes

**Subject of MIT license = vault content ONLY.** Each external open-source project analyzed in `03 Projects/<subject> - Beginner Analysis/` retains its own license:

- The wiki ABOUT n8n is MIT (Storm Bear's analysis content)
- n8n itself is n8n SUL (n8n-io/n8n's source code)
- Storm Bear's analysis does NOT include n8n source; only describes it — no license conflict

This is the standard "review-of-X-is-CC-BY-SA-but-X-is-still-MIT" pattern in tech-content-publishing.

## Decision freeze

This decision is COMMITTED at session 68 (2026-04-28). License will not be changed without:
1. Operator-explicit approval
2. New decision rationale chapter at `_state/license-decision-YYYY-MM-DD-revision-N.md`
3. Updated weekly review entry in GOALS.md

Next phase (item #4 public-release decision) builds on this MIT foundation.
