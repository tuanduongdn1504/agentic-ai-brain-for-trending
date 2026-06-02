# (C) PILOT — fenced READ of obsidian-second-brain → borrow-by-hand into the LLM Wiki Routine

**Type:** Fenced study pilot (READ only — NO install, NO scheduled agents, NO auto-rewrite on the real vault).
**Subject read:** `eugeniughelbur/obsidian-second-brain` @ `main` — `README.md` + `references/ai-first-rules.md` + `commands/obsidian-reconcile.md` + `commands/obsidian-synthesize.md` (fetched live 2026-06-02).
**Goal:** borrow the **bi-temporal-fact** + **synthesize/reconcile-agent** disciplines into Storm Bear's routine **by hand**, keeping the vault's human-in-the-loop gate (which the source deliberately removes).
**Status:** This is the FIRST executed pilot after 5 goal-aligned ships (v126/v131/v132/v134/v135). It is a methodology borrow, not a corpus subject — **no Pattern Library state change.**

> ## For future Claude
> This note is a *pilot study* about borrowing obsidian-second-brain's fact-provenance + reconcile/synthesize disciplines into Storm Bear's LLM Wiki Routine, saved 2026-06-02. Its purpose: a concrete, human-gated routine delta + one honest correction to the v134 record. The proposed routine edits are NOT yet applied — they await operator approval (the vault's "ask before editing my notes" rule).
> *(This preamble is itself borrow #5 below — dogfooded.)*

---

## 0. The honest correction the READ surfaced (do this first)

**The v134 wiki + registry 06 §C said bi-temporal facts use "`timeline:` arrays preserving event-time + vault-learned-time."** The actual source does **not** implement a `timeline:` array. The real mechanism is:

- inline **recency markers** on each volatile external claim: `(as of YYYY-MM, source.com)` — verbatim example from `ai-first-rules.md`: `"Mem0 raised $24M Series A (as of 2026-04, mem0.ai/blog/series-a)"`;
- per-claim **confidence levels**: `stated` / `high` / `medium` / `speculation`;
- the **two-timestamp "audit trail"** ("you believed X Tuesday → after ingesting Y Wednesday, shifted to Z") is realized by the recency-marker (when-true) **plus** a `## History` section that `/obsidian-reconcile` *appends* when a belief changes (when-learned + why) — **not** a single structured array.

→ **The `timeline:` array was my v134 extrapolation, not a fact about the repo.** Proposed fix (needs your OK — it edits an existing `(C)` artifact): in `_patterns/06-library-vocab-registry.md` §C, change the "Bi-Temporal Fact Discipline" anchor description from "`timeline:` arrays" to "inline `(as of …, source)` recency markers + per-claim confidence + a `## History` section appended on belief-change." The N=1 entry itself stays valid; only the mechanism description was wrong.

---

## 1. What's genuinely worth borrowing (5 items), adapted to the vault's hand-curation gate

The source's engine is **auto-rewrite + scheduled headless agents**. The vault's constitution is the opposite: hand-curated, `(C)`-prefixed, "ask before editing my notes," never-fabricate. So for each borrow I keep the *discipline* and drop the *automation* — the borrow is the schema/checklist, the operator stays the gate.

### Borrow 1 — Recency markers + confidence on volatile facts *(highest value for THIS vault)*
**Source rule:** every volatile external claim carries `(as of YYYY-MM, source)` + a confidence tag.
**Why it fits the vault uniquely well:** this sandbox **mocks the GitHub API**, so star counts / `created_at` are routinely NOT verifiable — I've been bolting that caveat on ad hoc (v134 "~1,700★", v135 "≈4.4k★ NOT API-verified"). The source's format is the clean fix, and the confidence vocabulary **maps directly onto a discipline the vault already runs informally**: inferred-vs-declared. 
- `stated` ← "declared Taiwan" (v135), a number quoted from the repo page
- `medium` / `speculation` ← "Taiwan-inferred" (v89/v90), "inferred China-Mainland" (v117/v123)
**Adopt (per-fact, in project entries + wiki index):** `4.4k★ (as of 2026-06, github.com/1weiho/open-slide repo page — confidence: stated, NOT API-verified; sandbox mocks the API)`. No automation — just a writing convention for volatile facts.

### Borrow 2 — `## History` on belief-change, but APPEND not REWRITE
**Source rule:** when a fact changes, `/obsidian-reconcile` rewrites the page and adds a `## History` section (the shift + why + dated sources).
**Vault adaptation:** the vault already does belief-change tracking at the *meta* level (the `PRIOR:` chains in the shim, the audit docs, Pattern-state accumulation) — but NOT at the *per-fact* level inside a project entry, and the vault must **append, not rewrite** (its whole architecture is append-with-recency). 
**Adopt:** when a later wiki/audit revises a specific earlier fact (a star count, a verdict, a pattern N-count), add a one-line dated `History:` note to that entry rather than silently overwriting — e.g. `History: 2026-06-02 — v134 "timeline: array" mechanism corrected to recency-markers+History after the obsidian-second-brain READ pilot.` Keeps the audit trail the source is after, without its rewrite behavior.

### Borrow 3 — Reconcile's *classification taxonomy* + "flagged for user" as a first-class outcome *(folds into audits, NOT into ships)*
**Source procedure (`obsidian-reconcile.md`):** 4 parallel scan agents (Claims / Entity / Decisions / Source-freshness); **contradiction ≠ ideological evolution**; resolve by **source-authority rank** (peer-reviewed > blog > transcript > opinion); outcome taxonomy = **clear-winner** (rewrite + `## History`) / **ambiguous** (open a `Conflict — Topic` with `status: open`) / **evolution** (current state + history); log `X found, Y auto-resolved, Z flagged for user`.
**Vault adaptation — the audits already ARE the reconcile pass; borrow the structure, keep it human-gated:**
- Add the **outcome taxonomy** to the mini-audit checklist: classify each flagged contradiction as winner / ambiguous / evolution.
- Adopt **`status: open` Conflict tracking** — the vault currently resolves-or-defers contradictions in prose with no standing open-conflict list. A tiny `04 Reviews/OPEN-CONFLICTS.md` (or a registry section) would stop ambiguous contradictions from evaporating.
- Keep **"flagged for operator" as the DEFAULT** outcome for anything non-mechanical. The source auto-resolves (`Y auto-resolved`); the vault's "ask before editing my notes" rule means the vault's default is `Z flagged for user`. Same accounting verb, opposite default — and the vault's default is the correct one.
- The **contradiction-≠-evolution** rule is a clean import: a verdict that *changed across versions* (e.g. open-slide "not yet corpus-relevant" v91 → subject v135) is **evolution**, log it as history, don't flag it as a contradiction.

### Borrow 4 — Synthesize's *scan dimensions* as audit checklist items (the vault's §28 stays the mint-gate)
**Source procedure (`obsidian-synthesize.md`):** parallel scans — **cross-source** (a concept in 2+ unrelated subjects), **entity-convergence** (people/orgs appearing together with no connection page), **concept-evolution** (ideas with 3+ updates → timeline), **orphan-rescue** (unlinked notes with claimable ideas).
**Vault adaptation:** the Pattern Library + §28 clustering already IS the synthesize layer — but it's tuned anti-inflation (don't over-mint), whereas synthesize is pro-connection (find latent links). They're complementary; borrow the **scan dimensions as audit prompts**, keep §28 as the mint-gate:
- **entity-convergence** is the standout gap: the vault has *noticed* author/org convergence in prose ("rohitg00 = 2-subject author v66+v113", "nexu-io same-org v83+v91", the cited-to-subject elevation v91→v135) but has **no entity/author pages** tying them. Worth a lightweight `entities/` index of repeat authors/orgs.
- **orphan-rescue**: audits should explicitly look for project entries with no inbound cross-references.
- **CRITICAL guard the source LACKS:** it *auto-writes* synthesis pages → over-generation. The vault's **§28 ≤2-new-standalones cap + clustering-first + auto-retire** is exactly the antidote. So borrow the *scans*, route every candidate through §28, mint nothing automatically.

### Borrow 5 — `## For future Claude` preamble *(zero-clash, do it now)*
**Source rule:** every note opens with 2-3 sentences: "This note is a [type] about [topic] saved on [date]. It [purpose]." for ~10-second relevance triage.
**Vault adaptation:** project `CLAUDE.md` files already do an informal version (one-liner + why-here). Standardize the exact 2-3-sentence opener at the top of each project `CLAUDE.md` and wiki `index.md`. Pure win, no automation, no clash. *(Dogfooded at the top of this doc.)*

---

## 2. What I deliberately did NOT borrow (and why)

| Source mechanism | Why rejected for this vault |
|---|---|
| **Auto-rewrite 5–15 pages per source** | Head-on collision with "ask before editing my notes" + hand-curation. The vault's append-with-recency is a deliberate choice, not a scale bug. |
| **Scheduled headless agents** (morning/nightly/weekly/health + PostCompact background) | The vault is operator-driven and intermittent; autonomous agents rewriting state unsupervised is the exact opposite of the control the operator wants. The *health-audit cadence idea* is already covered by the routine's natural-cadence audits. |
| **Two-Output Rule** (every answer also mutates vault pages) | Would turn every Q&A into an un-gated write. The vault writes only on explicit ship/audit, on the operator's say-so. |
| **Auto-resolve contradictions** | Borrowed only as *flag-for-operator* (Borrow 3). Auto-resolution removes the human judgment that is the vault's whole value. |
| **`raw/` immutable source store** | Conceptually nice (verbatim sources) but the vault cites source URLs inline (Borrow 1) rather than mirroring content; mirroring is scope creep here. |

---

## 3. Concrete proposed routine delta (NOT yet applied — awaiting your OK)

If you approve, these are small, surgical, and human-gated:

1. **Wiki-ship checklist (routine v2.6):** volatile external facts in project entries + wiki index carry `(as of YYYY-MM, source — confidence: stated/high/medium/speculation)`; API-unverifiable metrics tagged `NOT API-verified`. *(Borrow 1; formalizes a caveat I already write ad hoc.)*
2. **Per-fact `History:` line** appended (not overwritten) when a later ship/audit revises a specific earlier fact. *(Borrow 2.)*
3. **Audit checklist additions:** classify each contradiction winner/ambiguous/evolution; open ambiguous ones in a standing `04 Reviews/OPEN-CONFLICTS.md` with `status: open`; report `X found / Y resolved / Z flagged-for-operator`; run the 4 synthesize scans (cross-source / entity-convergence / orphan-rescue / concept-evolution) as prompts, **routing every mint candidate through §28**. *(Borrows 3 + 4.)*
4. **`## For future Claude` 2-3-sentence opener** standardized on project `CLAUDE.md` + wiki `index.md`. *(Borrow 5.)*
5. **Correct the v134 registry §C** bi-temporal mechanism description (§0 above). *(Honesty fix.)*

**None of these add automation. Every one keeps the operator as the write-gate.** The single highest-value item is Borrow 1 (recency + confidence), because it formalizes the API-unverifiable-metric caveat the sandbox forces on every ship anyway.

---

## 4. Pilot verdict

- **Worth it.** A catalogue entry (v134) told me the subject *extends Karpathy's LLM-wiki*; the READ told me *exactly how* and let me lift 5 concrete disciplines — and caught a factual over-claim in my own v134 record. That's the difference between cataloguing and piloting.
- **The fence held:** zero install, zero scheduled agents, zero auto-rewrite touched the real vault. The borrow is a set of writing/audit conventions, not the tool.
- **No Pattern Library state change.** This is methodology, not a corpus subject. The bi-temporal item stays N=1 in registry 06 §C (with the §0 mechanism correction pending).
- **The real takeaway:** the vault was already doing rough versions of *reconcile* (audits) and *synthesize* (Pattern Library) — the source's value is the **fact-provenance layer** (recency + confidence + per-fact history), which the vault genuinely lacks and which maps perfectly onto its API-can't-verify constraint.
