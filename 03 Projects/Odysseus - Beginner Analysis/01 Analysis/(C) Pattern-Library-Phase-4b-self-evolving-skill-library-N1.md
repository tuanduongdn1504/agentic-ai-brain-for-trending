# (C) Pattern Library — Phase 4b — Odysseus (v132)

**Routine:** v2.6 (CURRENT). **Ship:** 2026-06-01 (renumbered v131 → v132 — a concurrent v131 `harness` ship took v131 on a parallel branch). **Net Pattern Library state change:** **+1 PROVISIONAL Library-vocab standalone** (≤ the §28 2-per-wiki cap) + **1 strengthening (N=2)**. **NO new top-level Pattern; NO confirmed-count change** (46 confirmed / ~25 active / 8 Library-vocab CONFIRMED unchanged; PROVISIONAL +1). **No promotions at ship.**

> **§28 compliance:** the new standalone + the strengthening below are *actually written into* `_patterns/06-library-vocab-registry.md` this session (rule 5 — "filing is an act, not a claim"). 1 standalone ≤ the 2-per-wiki cap.

---

## PRIMARY — NEW Library-vocab: "Agent-Authored Self-Extracting Skill Library" PROVISIONAL N=1 (CORPUS-FIRST)

**The observation.** Odysseus's skills are not human-authored and not merely imported — the agent **writes its own**. After any run that took **≥2 rounds or ≥2 tool calls**, a background extractor (`services/memory/skill_extractor.py`) asks an LLM to *conservatively* distill the session into a reusable skill (returns the bare word `null` unless it is a genuine repeatable *computer* procedure; `MIN_CONFIDENCE=0.6`, `CONTEXT_WINDOW=12`). The result is persisted as a **`SKILL.md`** (`services/memory/skill_format.py`) with provenance frontmatter — `source: learned | taught | imported`, `teacher_model`, `confidence`, `uses`/`last_used` (sidecar `_usage.json`) — and is **evicted by confidence** when stale.

**Why CORPUS-FIRST.** The corpus has extensive *human-authored* skill collections (the agentskills.io 57k chain: v76/v93/v98/v99/v100/v113/v114/v124/v126…) and one *productized memory tree* (v118 OpenHuman). It has **not** had an **agent that auto-authors its own skill library from its own runs, with provenance + confidence-gated eviction.** That mechanism — *self-extraction + provenance + eviction* — is the novel unit.

**Why it is genuinely PRIMARY (and minted, unlike v119/v124/v126).** The recent calibration was "strengthen, don't mint" — correct for subjects whose only novelty was a count. Here there is a real new mechanism, CORPUS-FIRST, so a single PROVISIONAL N=1 standalone is the honest call (not manufactured novelty). Promotion-eligible at N=2 if a 2nd agent-self-authoring-skill subject appears; 5-wiki stale-watch ~v137. Filed to registry as a new standalone.

**Vault relevance (load-bearing).** This is a *productized, automated cousin of the vault's own discipline* — the Pattern-Library "don't repeat the same mistake twice" loop + confidence/promotion machinery, but run by the agent on itself. Genuine prior art worth studying when evolving the vault's skill/audit process.

---

## SECONDARY — strengthening + administrative (no further mint)

- **Parallel-skill-standard observation → N=2.** v121 CodexKit registered "Codex-Native Skill Collection — a parallel skill-authoring standard to agentskills.io." Odysseus's **Hermes-lineage SKILL.md** (the parser docstring states it is *"Inspired by Hermes' skills format,"* NousResearch) is a 2nd non-agentskills.io skill standard → the skill ecosystem is bifurcating into **≥3 standards** (agentskills.io / Codex-native v121 / Hermes-lineage v132). *Filed to registry (strengthening).* **Deliberately NOT counted as a 57k-chain implementer** (Hermes-lineage ≠ agentskills.io — the same exclusion v121 applied to Codex-native).
- **Pattern #18 Multi-Source LLM Aggregator (CONFIRMED N=3) N+1.** Odysseus aggregates **multi-provider** (OpenAI/OpenRouter + roadmap Anthropic/Gemini/Groq/xAI/DeepSeek) **and multi-runtime** (vLLM/llama.cpp/Ollama) behind one workspace — an aggregator at the *application* layer. Administrative N+1, not a promotion.
- **Pattern #84 cross-vendor ecosystem-tolerance** — local + remote, many providers/runtimes; **MCP host** + 4 built-in MCP servers (email/image/memory/rag) + npx Playwright browser MCP.
- **Pattern #57 corpus-composition (honest attribution).** `ACKNOWLEDGMENTS.md` credits **opencode** (agent loop; v67/v99) + **llmfit** (Cookbook) + **Alibaba Tongyi DeepResearch** (Deep Research; Apache-2.0 vendored) — 3 corpus-adjacent/known sources composed with preserved licenses. Strong attribution discipline.
- **Pattern #83 Honest-Deficiency-Disclosure (strong specimen).** `ROADMAP.md`: *"It works great for me (lol)... I dont know what I'm doing hlep"*; *"Skill audit, how does your model respond to skill injection?"* (skill-injection security awareness).
- **Pattern #45 multi-license composition** — MIT core + Apache-2.0 (Tongyi/ChromaDB) + AGPL-3.0 (SearXNG, Docker-composed unmodified) coexisting.
- **Pattern #52 EXTREME-VIRAL pulse — with a caveat.** ~11,771★ in ~1 day is record-shattering by rate, but **audience-driven** (PewDiePie's ~110M audience), NOT organic developer adoption — a #52/#82 caveat specimen, **NOT** a velocity promotion.
- **agentmemory v66 / Pattern #85** (ChromaDB + fastembed memory + a `memory` MCP server). **v118 OpenHuman sibling** — same genus (productized Karpathy-LLM-wiki: persistent memory + skills workspace); **v131 harness** concurrent sibling (agent-harness subject). **Pattern #82** quantitative-marketing ("trillion $Dollar"; 270+ models; the rig's 256 GB VRAM / Qwen-235B).

---

## Honest non-claims (load-bearing)

1. **(a) FAILS** — PewDiePie is a Swedish mega-creator, not a cultural-peer and not (a)-7. Not laundered.
2. **It is a composition of OSS, not novel primitives** — opencode + llmfit + Tongyi + ChromaDB + SearXNG + MCP SDK. HN's "Python UI over OSS" is literally true; the value is integration breadth + the self-extracting skills loop, not new primitives.
3. **SKILL.md is Hermes-lineage, NOT agentskills.io** → NOT counted as a 57k-chain implementer (I corrected my own iteration-2 research note on this).
4. **★-velocity is audience-driven** — recorded as a Pattern #52/#82 caveat specimen, NOT a velocity promotion.
5. **1 new PROVISIONAL standalone only** (≤ §28 2-cap) + 1 strengthening — both filed to the registry this session. NO new top-level Pattern; NO confirmed-count change; NO promotions.
6. **Renumbered v131 → v132** — a concurrent v131 `harness` ship (GOAL-ALIGNED, parallel branch, commit `8aa25e8`) was the actual first v2.6 ship + §35 breach-remedy. Odysseus-v132 is the 2nd consecutive GOAL-ALIGNED ship, clearing the §35 rolling-3 window. Not laundered into a "first ship" claim.

**Storm Bear's blunt take.** This is the cleanest possible answer once the §35 ceiling had been remedied by the concurrent v131 harness: a genuinely GOAL-ALIGNED subject (an autonomous-agent workspace — goal #1's core), shipped without an override or an (a)-rescue, and the 2nd straight goal-aligned ship that actually clears the rolling off-goal window. The one mint is honest — the agent-self-authoring-skills mechanism is really CORPUS-FIRST, and pretending it were "just a strengthening" would under-claim a real novelty as badly as inflating an off-goal app would over-claim. Everything else is strengthening (the bifurcating-skill-standard story finally hits N=2 with Hermes-lineage) or administrative. And the thing actually worth doing with this wiki isn't filing it — it's reading `services/memory/skill_*.py` as prior art for automating the vault's own "don't repeat the same mistake twice" loop, and (if you want) self-hosting it once behind auth.
