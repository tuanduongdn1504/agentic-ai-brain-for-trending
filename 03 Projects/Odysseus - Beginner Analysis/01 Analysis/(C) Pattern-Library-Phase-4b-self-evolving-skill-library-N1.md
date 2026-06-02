# (C) Pattern Library — Phase 4b — Odysseus (v136)

**Routine:** v2.6 (CURRENT). **Shipped:** v136, 2026-06-02 (researched 2026-06-01; renumbered v131→v132→v136 across two concurrent-ship windows). **Net Pattern Library state change:** **+1 PROVISIONAL Library-vocab standalone** (≤ §28 2-cap) + **1 strengthening (N=2)**. **NO new top-level Pattern; NO confirmed-count change** (46 confirmed / ~25 active / **8 Library-vocab CONFIRMED** unchanged). **No promotions at ship.**

> **§28 compliance:** the new standalone + the strengthening below are *actually written into* `_patterns/06-library-vocab-registry.md` this session (rule 5 — "filing is an act, not a claim"). 1 standalone ≤ the 2-per-wiki cap. Registry was at 9 standalones (post-v135); this makes 10.

---

## PRIMARY — NEW Library-vocab: "Agent-Authored Self-Extracting Skill Library" PROVISIONAL N=1 (CORPUS-FIRST)

**The observation.** Odysseus's skills are not human-authored and not merely imported — the agent **writes its own**. After any run that took **≥2 rounds or ≥2 tool calls**, a background extractor (`services/memory/skill_extractor.py`) asks an LLM to *conservatively* distill the session into a reusable skill (returns the bare word `null` unless it is a genuine repeatable *computer* procedure; `MIN_CONFIDENCE=0.6`, `CONTEXT_WINDOW=12`). The result persists as a **`SKILL.md`** (`services/memory/skill_format.py`) with provenance frontmatter — `source: learned | taught | imported`, `teacher_model`, `confidence`, `uses`/`last_used` (sidecar `_usage.json`) — and is **evicted by confidence** when stale.

**Why CORPUS-FIRST.** The corpus has extensive *human-authored* skill collections (the agentskills.io 57k chain) and productized memory systems (v66 agentmemory, v118 OpenHuman, **v132 supermemory**). It has **not** had an **agent that auto-authors its own skill library from its own runs, with provenance + confidence-gated eviction.** That mechanism — *self-extraction + provenance + eviction* — is the novel unit. Explicitly distinct from **v132 supermemory** (a memory *retrieval/benchmark* engine, not a self-authoring-skills mechanism) and from v118's memory-tree (memory, not skills).

**Why genuinely PRIMARY (and minted).** Calibration since v119/v124/v126 favored "strengthen, don't mint" for count-only novelty. Here there's a real CORPUS-FIRST mechanism, so a single PROVISIONAL N=1 standalone is the honest call — not manufactured novelty. Promotion-eligible at N=2 (a 2nd agent-self-authoring-skill subject); 5-wiki stale-watch ~v141. Filed to registry section C as the 10th standalone.

**Vault relevance (load-bearing).** A *productized, automated cousin of the vault's own discipline* — the Pattern-Library "don't repeat the same mistake twice" loop + confidence/promotion machinery, run by the agent on itself. Genuine prior art for evolving the vault's skill/audit process (and a sibling to the new §37 fact-provenance discipline the vault just adopted at v134).

---

## SECONDARY — strengthening + administrative (no further mint)

- **Parallel-skill-standard observation → N=2.** v121 CodexKit registered "Codex-Native Skill Collection — a parallel skill-authoring standard to agentskills.io." Odysseus's **Hermes-lineage SKILL.md** (parser docstring: *"Inspired by Hermes' skills format,"* NousResearch) is a 2nd non-agentskills.io skill standard → the ecosystem is bifurcating into **≥3 standards** (agentskills.io / Codex-native v121 / Hermes-lineage v136). *Filed to registry (strengthening on the v121 Codex-native row).* **Deliberately NOT a 57k-chain implementer** (Hermes-lineage ≠ agentskills.io — same exclusion v121 applied).
- **Pattern #18 Multi-Source LLM Aggregator (CONFIRMED N=3) N+1** — multi-provider (OpenAI/OpenRouter + roadmap Anthropic/Gemini/Groq/xAI/DeepSeek) + multi-runtime (vLLM/llama.cpp/Ollama) at the *application* layer. Administrative.
- **Pattern #84 cross-vendor** — MCP host + 4 built-in MCP servers (email/image/memory/rag) + npx Playwright browser MCP.
- **Pattern #57 corpus-composition (honest attribution)** — `ACKNOWLEDGMENTS.md` credits opencode (v67/v99) + llmfit + Alibaba Tongyi DeepResearch (Apache-2.0, vendored). Strong attribution discipline. *(Not the "corpus-recursive-at-methodology-influence" thread — that was RELABELED+SPLIT at the v134–v135 audit; Odysseus is plain honest-composition, not claimed as that thread.)*
- **Pattern #83 Honest-Deficiency-Disclosure (strong)** — `ROADMAP.md` "It works great for me (lol)... I dont know what I'm doing hlep"; "Skill audit — skill injection?".
- **Pattern #45 multi-license** — MIT core + Apache-2.0 (Tongyi/ChromaDB) + AGPL-3.0 (SearXNG, Docker-composed unmodified).
- **Pattern #52 EXTREME-VIRAL pulse — caveat** — ~11,771★ in ~1 day (NOT API-verified) is record-rate but **audience-driven**, NOT organic dev adoption. A #52/#82 caveat specimen, NOT a velocity promotion.
- **Corpus-memory cluster connectivity** — agentmemory v66 / Pattern #85 + **v132 supermemory** + **v134 obsidian-second-brain** + v118 OpenHuman: Odysseus sits in the corpus's growing agent-memory/knowledge-workspace neighborhood (observation, not a mint).

---

## Honest non-claims (load-bearing)

1. **(a) FAILS** — PewDiePie, Swedish mega-creator, not a cultural-peer and not (a)-7. Not laundered.
2. **Composition of OSS, not novel primitives** — opencode + llmfit + Tongyi + ChromaDB + SearXNG + MCP SDK. HN's "Python UI over OSS" is literally true; the value is integration breadth + the self-extracting skills loop.
3. **SKILL.md is Hermes-lineage, NOT agentskills.io** → NOT a 57k-chain implementer.
4. **★-velocity is audience-driven + NOT API-verified** (§37) — a Pattern #52/#82 caveat, not a velocity promotion.
5. **1 new PROVISIONAL standalone** (≤ §28 cap) + 1 strengthening, both filed. NO new top-level Pattern; NO confirmed-count change; NO promotions.
6. **Renumbered v131→v132→v136** — concurrent ships (v131 harness; then main's v132 supermemory + v133–v135) took the lower numbers. Not laundered into any "first ship" claim.

**Storm Bear's blunt take.** Stripped of the concurrent-ship renumber drama, this is a clean GOAL-ALIGNED ship: an autonomous-agent workspace (goal #1's core), included on (b)(c)(d) with (a) the honest single fail. The one mint is real — agent-self-authoring-skills is genuinely CORPUS-FIRST, and it's the most vault-relevant thing here (prior art for automating "don't repeat the same mistake twice," now next to the corpus's other memory subjects supermemory/obsidian/agentmemory). Everything else is strengthening (Hermes-lineage takes the parallel-skill-standard line to N=2) or administrative. The thing worth doing isn't filing it — it's reading `services/memory/skill_*.py`, and (if you want) self-hosting it once behind auth.
