# Corpus & hireui Relevance

Where a CS-fundamentals topic fits in a corpus otherwise about Claude Code, agents, and harness engineering — and what it means for hireui (the operator's recruitment SaaS, Goal #2).

## Corpus position

- The corpus' **first pure CS-fundamentals topic** and only its **2nd non-Claude/non-agent topic** (after [[self-hosted-devops-oss/_index]]).
- Slots under the corpus' **"software fundamentals matter more in the AI era"** thread — but the thread and this video argue at *different levels*, and this wiki is careful not to overstate the link (the corpus-xref pass flagged these as thematic, not content, links).

### Cross-links — honestly graded

**Content link (strong):**
- [[graphify-codebase-graph/_index]] — genuinely overlaps: it builds queryable **graphs** of codebases and runs the **Leiden** community-detection algorithm. The [[graph-and-traversal]] article is the fundamentals under that tool.

**Thematic links (fundamentals thread — NOT content overlap):**
- [[pocock-software-fundamentals/_index]] — argues fundamentals matter *more* now, but its "fundamentals" = **design discipline** (deep modules, TDD, naming), *not* knowing 16 structure names. This video supplies **knowledge**; Pocock demands **applied discipline**. Complementary, different layers.
- [[quanit-becoming-ai-engineer-2026/_index]] — "AI engineers need **fundamentals not internals**." Data structures are exactly the kind of fundamental he means (concepts you use), vs. transformer internals (you don't). Good thematic fit; not content overlap.
- [[system-thinking-ai-coding/_index]] — Naur "theory building"; a *design-philosophy* layer above data arrangement.

**Weak / implementation-detail only:** [[claude-code-memory-systems/_index]] (uses vectors / knowledge-graphs / SQLite as *means*, not subject).

**Dropped** (corpus-xref verdict FALSE — orthogonal): prompt-evaluation, claude-api-cost-optimization, self-hosted-devops-oss (the last is a *structural* sibling — same "non-agent topic" bucket — noted only in [[source-provenance]], not a content link).

## hireui relevance — which of the 16 actually show up

hireui's first planned AI feature is **candidate ↔ job matching** ([[quanit-becoming-ai-engineer-2026/_index]] pilot; RATIFIED candidate-LLM legibility ADR). Of the 16 structures, **~4–6 are directly load-bearing**; the rest are landscape or hidden in the database:

| Structure | Where it lands in hireui | Layer |
|---|---|---|
| **Hash table** ([[hashing]]) | O(1) candidate/job **ID lookup**; in-memory skill index | app |
| **Trie** ([[string-trie]]) | **Job-title / skill autocomplete** (type-ahead) | app |
| **Graph** ([[graph-and-traversal]]) | Model **candidate skills → job requirements** as edges; match strength = reachability/overlap | app |
| **Bloom filter** ([[probabilistic]]) | Cheap **dedup** of duplicate candidate records before expensive ranking | app |
| **B+-tree** ([[disk-scale]]) | **PostgreSQL indexes** underneath every query | DB (transparent) |
| the other ~10 | vocabulary / landscape — not in matching logic | — |

**Design lesson (not the "pick one" framing):** the matching feature will **compose** hash table + trie + graph + bloom filter over a B+-tree-indexed store — exactly the [[beyond-the-video|composition]] point. The video's "pick one structure" is pedagogy; hireui's feature stacks four.

## The reflexive hiring angle (hireui is a recruitment product)

hireui *screens engineers* — so the video's own limitation is a direct product insight: **it tests VOCABULARY, not COMPETENCE.** A candidate who can recite "skip list = O(log n)" is not the same as one who can implement a hash table with collision resolution or diagnose "our search is slow because we iterate a linked list." For hireui's screening design: a trivia round ("what is a trie?") is a cheap **pre-screen**, never a **competence assessment** — that needs implement / debug / reason-about-tradeoffs tasks. See [[critical-appraisal]].

## Pilot posture

**No tooling pilot** — this is a knowledge topic, not a tool. The actionable takeaways:
1. **Reference the composition map** (table above) when specifying hireui's matching feature — it names the 4–6 structures to reach for and why.
2. **Steal the pre-screen-vs-competence distinction** for any hireui candidate-evaluation logic.
3. **Fundamentals-as-verification:** per [[quanit-becoming-ai-engineer-2026/_index]] Pillar 3, this knowledge is what lets the operator *verify* AI-generated matching code is sound (right structure, right Big-O) rather than trust it blindly — aligned with the candidate-LLM legibility ADR.

## Key Takeaways

- **First pure CS-fundamentals topic; 2nd non-agent topic** in the corpus.
- Only **one true content cross-link** ([[graphify-codebase-graph/_index]], via graphs); the fundamentals-thread links (Pocock, Quân IT, system-thinking) are **thematic, not content** — graded honestly here.
- **~4–6 of 16 structures are load-bearing for hireui matching** (hash / trie / graph / bloom + B+-tree in Postgres); the feature **composes** them.
- Reflexive insight for a recruitment product: the video tests **vocabulary, not competence** — a pre-screen, not an assessment.
