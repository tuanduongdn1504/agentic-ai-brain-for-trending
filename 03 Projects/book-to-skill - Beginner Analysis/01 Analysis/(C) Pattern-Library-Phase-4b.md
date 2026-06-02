# (C) Phase 4b — Pattern Library contribution — book-to-skill (v137)

**Subject:** `virgiliojr94/book-to-skill` · **Routine v2.6** · 2026-06-02
**PRIMARY:** methodology-embodiment of the Karpathy-LLM-wiki **construction step**, automated as a source→agent-skill generator — a **candidate** for the v118/v134 "generate-the-wiki" vector, with a load-bearing distinction → **DEFERRED** to the ~v139–v140 audit. + **1 NEW Library-vocab standalone FILED:** "Source-to-Agent-Skill Knowledge-Base Generator" N=1 CORPUS-FIRST.
**State change at ship:** NONE (46 confirmed / 8 Library-vocab CONFIRMED unchanged). No top-level pattern, no tier sub-archetype. §28 new-standalone count = **1** (≤2).

---

## PRIMARY — methodology-embodiment of the Karpathy-LLM-wiki construction step

### The event
book-to-skill **automates exactly the per-source ingestion step this vault performs by hand.** Its output structure is a one-to-one map of the LLM-wiki construction primitive:

| Vault's hand process (Karpathy LLM-wiki) | book-to-skill (automated) |
|---|---|
| read source, extract frameworks/mental models | Step 3 + 7: frameworks, principles, anti-patterns, "preserve exact naming" |
| write summary pages | `chapters/ch*.md` (on-demand, 800–1,200 tokens) |
| build an index | SKILL.md Chapter Index + **Topic Index** |
| glossary / cross-references | `glossary.md` + "Connects To" links |
| load on-demand, not all at once | progressive disclosure: SKILL.md <4k + chapters loaded per query |

This is the corpus's **own upstream foundation** showing up as a shipped tool — the same family the v134-v135 audit tracked as "methodology-embodiment of the Karpathy-LLM-wiki foundation" (RELABELED out of clean Pattern #57, which is corpus-*internal citation topology*).

### Relationship to the v118/v134 generate-vector — CANDIDATE, decision DEFERRED
The v134-v135 audit split the methodology-embodiment thread into a **generate-vector N=2 PROVISIONAL** (v118 OpenHuman + v134 obsidian-second-brain), promotion-eligible at N=3, + v94 Understand-Anything as adjacent *consume* N=1.

Is book-to-skill the genuine 3rd generate-vector instance? **The honest, load-bearing distinction (recorded, not laundered):**
- **v118 / v134 GENERATE + MAINTAIN a persistent, living, multi-source second-brain VAULT** (Obsidian/markdown; self-rewriting; contradiction-reconciling; synthesis-over-time).
- **book-to-skill is a one-shot CONVERTER:** one source → one static **agent skill**, and stops. No persistence, no living vault, no maintenance, no cross-source synthesis. Its output is a **Claude/Amp skill**, not a personal-knowledge vault.

So book-to-skill embodies the methodology at the **construction/ingestion layer** (closer to what the vault does *per wiki* — one subject → one structured page-set) rather than the **maintenance/second-brain layer** (v118/v134). Whether the generate-vector promotes broad-class to N=3 (counting book-to-skill) **or** splits into a "persistent-vault generation" sub-flavor (v118/v134) vs a "one-shot source→artifact construction" sub-flavor (v137) is precisely the **promote-broad-class-vs-split** question for the ~v139–v140 audit.

**I am NOT promoting it at ship.** This mirrors the v134-v135 audit's own discipline (it overturned v134's "N=3" headline). Recorded as a candidate that **feeds** the audit; the audit decides.

### NEW Library-vocab standalone (the concrete novelty) — FILED to registry 06 §C
**"Source-to-Agent-Skill Knowledge-Base Generator"** N=1 CORPUS-FIRST. Input = an arbitrary document (10+ formats); output = a **progressive-disclosure SKILL.md knowledge base** (frameworks + chapter index + glossary + patterns + cheatsheet + topic index, token-budgeted, on-demand). Distinct from:
- **v95 skill-creator** — a *general* skill scaffolder (you describe a skill); not source-driven, not document-ingesting.
- **v94 Understand-Anything** — source = a *codebase*, output = a *knowledge graph* (not a SKILL.md skill).
- **the agentskills.io 57k chain** — human-authored skill *collections*; book-to-skill *generates* one skill from one book.
Promotion-eligible at N=2 (a 2nd document→agent-skill generator); 5-wiki stale-watch ~v152. (Could become a tier sub-archetype at N=2 — held as a Library-vocab standalone for now, anti-inflation.)

## SECONDARY (observations — §28-disciplined; instance notes, not mints)

1. **Phase-0.9 (a)-8 "South-American-LOCATED" RE-REGISTERED → N=2** (v97 distill samuelfaj/Brazil + v137 book-to-skill/Brazil). Retired at v115 (N=1-only); §2/§28 permit re-registration on a genuine 2nd instance. **This is a Phase-0.9 (a)-axis ledger item, NOT a Library-vocab standalone** — it does not consume the §28 cap. Promotion-eligible to a formal (a) sub-axis at N=3. Recorded in the wiki/state + verdict; the (a) taxonomy lives in the routine, not registry 06.
2. **Pattern #84 84c "multi-harness / provider-agnostic" — N+1** (CONFIRMED). Targets Amp skill dirs (`.agents/skills`, `~/.config/agents/skills`, `~/.config/amp/skills`) + Claude Code (`~/.claude/skills`); `compatibility:` frontmatter names both. **Modest, Amp-first** — instance noted, not re-minted, not inflated.
3. **Library-vocab #20 Token-Economy-Quantification — N+1** (CONFIRMED). Step 2.5 pre-flight cost estimate (input/output tokens + USD at Sonnet/Haiku prices + time) shown **before** generation; the whole skill's design rationale is token-economy ("a 400-page book = ~200K tokens per conversation if injected; skills load on-demand"). A strong instance.
4. **Context-management corpus-recursive — OBSERVATION (NOT minted).** Step 2.6 cites the **Recursive Language Model (RLM)** paradigm and uses `grep`/`sed`/bounded `Read` to slice only relevant chapters from large books instead of full reads — *the vault's own "use awk for surgical extracts / never read >1 chapter" context-rot discipline*, arrived at independently. A genuine cross-arrival adjacency; narrow + product-specific → logged, no standalone filed (keeps §28 count at 1).
5. **Skill-generating-skill / meta-skill cluster — OBSERVATION (NOT minted).** v95 skill-creator + v131 harness (generates skills) + v137 book-to-skill (generates a skill from a book). **Heterogeneous** (general scaffolder vs team-factory vs book-converter) — minting a sub-archetype here is the anti-pattern the v125/v134-v135 discipline warns against. Logged as adjacency.
6. **Progressive-Disclosure Architecture per Skill — strengthening note.** The on-demand chapter loading + per-file token budgets echo the v98 "Progressive-Disclosure Architecture per Skill with Token-Cost Annotation" candidate; noted, not separately minted.

## Honest non-claims
- **NO Pattern Library state change at ship** (46 confirmed / 8 Library-vocab CONFIRMED unchanged; tracked PROVISIONAL surface +1 standalone).
- **The generate-vector N=3 question is DEFERRED, not decided.** No ship-promotion.
- **NOT an agentskills.io 57k `npx skills add` implementer** — installed by copying SKILL.md from a raw URL / curl; no `npx skills add` evidence. Amp `.agents/skills` is a directory convention, not the vercel-labs skills CLI.
- **NOT a Pattern #52 promotion** — ~113★/day is strong for a ~1-month repo, but the window is <90d (pulse, not Multi-Month-Sustained) AND the metrics are NOT API-verified (sandbox mock, §37.4). Recorded as a positive-but-unquantified signal.
- **(b) STRONG, not STRONGEST** — knowledge-management/study domain (see verdict doc; v134 calibration).
- **NO new tier sub-archetype, NO new top-level pattern.** §28 new-standalone count = 1 (≤2).

## What a future audit (~v139–v140) should carry from v137
1. **The generate-vector promote-vs-split decision** — does book-to-skill make it N=3 (promote broad class), or does it force a split into persistent-vault-generation (v118/v134) vs one-shot-source→artifact-construction (v137)? This is the explicit deferred call.
2. **"Source-to-Agent-Skill Knowledge-Base Generator" N=1** — watch for an N=2 (a 2nd document→skill generator) → promote, and decide Library-vocab-standalone vs tier-sub-archetype.
3. **(a)-8 South-American-LOCATED N=2** (v97+v137) — watch for an N=3 to formalize the (a) sub-axis.
