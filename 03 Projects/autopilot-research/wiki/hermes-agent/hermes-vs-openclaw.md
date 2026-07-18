# Hermes Agent vs OpenClaw

## Source
`raw/2026-07-18-hermes-agent/` (esp. t3 Tech With Tim, t1 Phan Dong Giang, t2 NetworkChuck, t8 AI LABS) + official README/docs. Verified via `wf_06a79485-687`.

## Why this comparison is the spine of the topic
- **OpenClaw is Hermes' explicit reference point.** Hermes ships **`hermes claw migrate`** (C15 = CONFIRMED) which imports an OpenClaw setup: **user profile, credentials, skills, and the "soul file"** (the agent's personality/instructions). A migration tool only exists because OpenClaw **predates** Hermes and has a user base to convert.
- ⚠️ **t8's claim that "Hermes was built before OpenClaw" is FALSE/unsupported** — Hermes' own repo is dated **2025-07-22** and it ships an OpenClaw→Hermes importer; the "we built ours first" framing is not evidenced. *(A specific OpenClaw creation date was asserted by a gatherer but is NOT independently verified here — so it is not stated as fact.)*

## The two positionings (surfaced, not blended — Rule 7)
- **"Replacement" camp** (NetworkChuck t2, anchor t1): Hermes is a straight upgrade — *"goodbye OpenClaw."* Migrate and move on.
- **"Complementary" camp** (Tech With Tim t3, the balanced source): they serve different jobs —
  - **Hermes** → single-user, personal, self-learning, longer to "warm up".
  - **OpenClaw** → more mature, feature-rich, better for **multi-channel / customer-facing / enterprise** orchestration, huge community skill library.
- Both camps agree Hermes' **self-learning + autonomous skill creation** is its genuine edge; they disagree on overall suitability. **The corpus takes no side** — pick per use-case.

## Feature-level contrasts drawn by the sources
| Dimension | Hermes (per sources) | OpenClaw (per sources) |
|---|---|---|
| Skills | Learns/creates its own over time; Skill Hub marketplace with **security-scanned** skills | Large **community** skill library ("50,000+" per t1 — UNVERIFIED); some community skills flagged unsafe |
| Memory | FTS5 + summarization under a **token cap** (prunes stale) | Persistent memory but **grows unbounded** (t8's critique) |
| Sandboxing | **Built-in** isolation by default | You **sandbox it yourself** (t8) |
| Setup | curl\|bash + `hermes setup`; migration importer | (mature, broader integrations) |
| Best for | Repetitive personal workflows, security-conscious users | Diverse work, need mature multi-channel now |

- ⚠️ Unverified stats to NOT assert: OpenClaw's **"50,000+ skills"** (t1), and any OpenClaw security-history specifics — these are source-claims, not primary-verified.

## The "learning loop is unique" claim — FALSE
- README says Hermes is *"the only agent with a built-in learning loop."* **This is FALSE** ([[claims-scorecard]] H4): the *same README* ships a tool to import **memories and skills from OpenClaw** — which only makes sense if OpenClaw already has memory + skills (i.e. a learning loop). Hermes' differentiation is the **autonomous skill *creation*** and the token-capped memory design, **not** having a loop at all.

## Key Takeaways
- Treat Hermes as an **OpenClaw successor/rival**, not a category unto itself — the `hermes claw migrate` command is the proof.
- **Don't repeat "goodbye OpenClaw" as settled** — the balanced review says OpenClaw stays better for mature multi-channel/enterprise work; Hermes wins on personal self-learning.
- The real, defensible Hermes advantages are **built-in sandboxing, token-capped pruning memory, security-scanned Skill Hub, and autonomous skill creation** — not "the only learning loop."
- Cross-links: [[vercel-eve|vercel-eve]] + [[herdr|herdr]] (agent-runtime siblings), [[claude-code-clones|claude-code-clones]].
