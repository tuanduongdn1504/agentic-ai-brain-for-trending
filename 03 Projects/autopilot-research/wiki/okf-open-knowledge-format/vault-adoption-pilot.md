# Vault Adoption Pilot: Should Storm Bear Adopt OKF?

The reflexive question this topic exists to answer. This vault (and this autopilot-research project) **is** a Karpathy LLM Wiki — so OKF is the first formal spec it could adopt or measure against. Synthesized from the workflow's pilot-design agent + the [[thesis-critique]].

## Verdict: **WATCH** — run one 40-minute experiment, don't adopt wholesale yet

**Why not adopt now:** the vault's bottleneck today is **compilation velocity + curation**, not **interoperability**. OKF's main unlock is *shareability*, and the operator has no stated external-sharing goal yet. Adopting a metadata standard across ~60 topics is real work with speculative payoff. **Why not reject:** the vault is already ~80% structurally OKF-shaped, the substrate is safe (markdown/YAML/folders — nothing to unwind), and a shareable-bundle capability could matter for hireui or public corpus publishing later.

## Where the vault stands vs OKF (grep-verified by corpus-xref)

| Aspect | Vault today | OKF | Alignment |
|---|---|---|---|
| Folder-per-topic + per-folder index | `wiki/<topic>/_index.md` + `_master-index.md` | `index.md` at any level | ~95% (filename differs) |
| Entity/concept pages, cross-links | Yes; `[[wiki links]]` | Yes; markdown links | ~80% |
| **YAML frontmatter with `type`** | **None on wiki articles** (rich frontmatter only on `raw/` files) | **Required** | **~0–10%** |
| `title`/`description`/`tags`/`timestamp` | Implicit in prose / source blockquotes | Recommended | ~5–10% |

**Summary:** ~**80% on structure**, ~**5–10% on metadata.** The entire gap is *machine-readable frontmatter*. Adopting OKF ≈ "add a YAML block with `type` to each article + rename indexes."

## A proposed `type` vocabulary for this vault

| `type` | Applies to | ~count |
|---|---|---|
| `topic` | autopilot-research topic `_index.md` | ~60 |
| `article` | ordinary wiki articles | ~300–600 |
| `video` | `raw/` source summaries | ~100+ |
| `pattern` | Pattern-Library entries | ~75 |
| `project` | Storm Bear vXX wiki ships | ~62 |
| `analysis` | reviews / audits / mini-audits | ~20 |
| `concept` | cross-cutting entities (OKF, Cynefin, BOLA, harness) | ~30 |
| `decision` | ADRs / pilot decisions / rules | ~15 |

(Multi-type docs: pick the primary `type`, put the rest in `tags`.)

## Honest migration cost (~60 topics, ~300–600 articles)

- **Design the type vocabulary + validate on 1 topic:** ~30–60 min (human).
- **Full refactor via sub-agents (Cole's parallel-refactor claim):** **testable, not proven.** If sub-agents agree on metadata → ~2–3h. If they disagree (inconsistent `type`/`tags` across agents) → serial, ~5–8h. **This is itself the thing the pilot should measure.**
- **Validation:** ~1–2h (feed a refactored bundle + SPEC to a fresh agent, confirm cross-links resolve).
- **Risk:** LOW — additive frontmatter breaks nothing; a single-topic pilot is trivially revertible.

## The <1-hour first experiment (the actual next action)

**OKF-ify ONE topic end-to-end and query it with a fresh agent.**

1. **Pick a small, recent, self-contained topic:** [[external|agent-memory-architecture/_index]] (few articles, already in a pilot thread) — or one Pattern-Library chapter.
2. **Add frontmatter** (`type`, `title`, `tags`, `related`) to each article; add an OKF-style `index.md`.
3. **Give a fresh agent** the [OKF SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) + the refactored folder; ask 5 questions.
4. **Measure vs the un-refactored topic:** time-to-first-correct-answer, accuracy of `type`/`tags` filtering, cross-link traversal.
5. **Decision gate:** <10% friction improvement → schedule full adoption. >20% friction (agents ignore metadata, prefer keyword search) → shelve, revisit in 6 months.

**Est. ~40 min** (20 refactor + 10 test + 10 write-up); ~1.5h if you also prototype the sub-agent refactor flow.

## hireui relevance — MEDIUM (conditional)

- hireui has **no LLM integration yet** ([[external|Storm Bear: hireui]] context), so OKF would sit *beneath* a future LLM layer as a knowledge base.
- Plausible use: a curated **recruitment domain-knowledge bundle** (bias-mitigation, EU AI Act high-risk employment context, NYC LL144, CV-parsing gotchas) that a future hireui agent queries by `type:concept` / `tag:bias-mitigation` to *explain* candidate-impacting decisions.
- This dovetails with the **RATIFIED hireui candidate-LLM legibility ADR** (any candidate-impacting LLM path must be fixed + legible + audited): a versioned, human-readable OKF knowledge bundle is exactly the kind of *legible, auditable* artifact that ADR wants — the opposite of an opaque vector store.
- **But** OKF doesn't *create* that knowledge; it only makes an already-curated bundle shareable. Separate, medium-term work.

## Pilot ranking: **MEDIUM-LOW**, escalation-gated

Against the standing backlog (cc-sdd #1, codex-plugin-cc #1.5, free-claude-code #2, pocock-writing-great-skills):
- Not Goal-#2 product-shipping; not operator-urgent (vault works today); **infrastructure/optionality value**, high confidence (spec is stable, pattern proven by Cole's bundle).
- **Escalates to MEDIUM if:** (a) hireui team wants knowledge-base access, (b) operator decides to publish topic bundles publicly, or (c) multi-agent cross-vault querying becomes a workflow.
- **Recommended sequencing:** run the 40-min single-topic experiment *after* cc-sdd ships; let the friction number decide full adoption.

## Key Takeaways

- **WATCH, don't adopt** — the vault is ~80% structurally OKF-aligned but ~0% on metadata; the delta is pure frontmatter.
- The **main unlock is shareability**, which the operator doesn't need yet → optionality, not urgency.
- **First step = one 40-min experiment** on [[external|agent-memory-architecture/_index]]: refactor → query with a fresh agent → gate on friction.
- **hireui angle (MEDIUM):** an OKF recruitment-knowledge bundle is a *legible, auditable* fit for the candidate-LLM legibility ADR — but needs the knowledge curated first.
- **Rank MEDIUM-LOW**, run after cc-sdd; escalate only if external sharing becomes a goal.
