# (C) Phase 0 + Phase 0.9 verdict — Sana (v116) — **OPERATOR OVERRIDE**

**Routine:** v2.4. **Fetched:** 2026-05-29. **Verdict:** STRICT **0/4 → SKIP**, force-built by **operator-elected OVERRIDE** (2nd in corpus history after v84 image-blaster).

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `NVlabs/Sana` |
| License present | ✅ **Apache-2.0** (code; GitHub API `apache-2.0`). Model weights licensed separately per HF collection. |
| Active / recently pushed | ✅ pushed 2026-05-28; created 2024-10-11 (~595 days) |
| Scale floor (≥1★) | ✅ **7,919★** |
| Tier classification | **Corpus-outlier** — not in the agent-centric T1–T5 taxonomy. Forced-nearest = T5 Application. **CORPUS-FIRST pure generative-vision research model.** |

**Phase 0 = technically PASS on the mechanical gates, but FLAGGED out-of-domain.** Every prior corpus subject sits in the Claude-Code / agent-skills / autonomous-coding / LLM-tooling ecosystem. Sana is a text-to-image/video diffusion research model. It clears the mechanical floors (license, activity, scale) but is a domain outlier.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **FAIL**

Owner = **NVIDIA Labs** (`owner.type: Organization`), the research division of NVIDIA Corp, a US mega-corporation. Algorithm credit shared with **MIT Han Lab (Song Han)** and **Tsinghua**. None of the corpus's (a) sub-axes apply:
- Not a VN/Asian indie cultural-peer (it's a US corporate + elite-academic lab).
- Not **(a)-7 Foundational-Vendor-Direct-Source** — the vault depends on Anthropic/Claude, *not* on an NVIDIA diffusion model. NVIDIA is not a substrate the wiki routine runs on.
- The MIT/Tsinghua academic affiliation is real but does not make a mega-lab research artifact a "cultural peer" in the sense the rubric means (solo/indie/VN-Asian builder aligned with Storm Bear's own scale and context).

**(a) FAIL — clean, no inference-tolerant rescue available.**

### (b) Goal-relevance / vault-utility — **FAIL**

Documented #1 goal: *"Master Claude and autonomous agents for software development."* A 4K text-to-image / text-to-video model has essentially zero bearing on that goal.
- Not a vault tool, not a Scrum tool, not an agent, not a coding assistant.
- Cost-of-trial is **HIGH** (needs a capable GPU; 8 GB is the floor *with* 4-bit quant) and directness is **~zero**.
- The single conceivable vault use — generating illustrative images — is negligible and not why one would study this repo.

**(b) FAIL.**

### (c) Instructive / exemplary — **WEAK (not a clean PASS)**

Sana is genuinely excellent engineering: the 32× DC-AE, linear-attention DiT, decoder-only LLM text encoder, and 8 GB-VRAM quantization are real, peer-reviewed contributions to *efficient generative vision*. **But that instruction lives in a different field.** For this corpus — whose Pattern Library tracks agent/skill/distribution/governance methodology — Sana teaches nothing transferable. Calling (c) a PASS would be laundering "this is impressive" into "this is relevant to us." It isn't.

**(c) WEAK** — instructive-but-orthogonal.

### (d) Corpus connectivity — **FAIL**

No agentskills.io chain (no SKILL.md / AGENTS.md / .claude/), no Karpathy LLM-wiki lineage, no Claude-Code adjacency. The only threads are tangential:
- decoder-only LLM (Gemma) used internally as a text encoder;
- SGLang serving exposes an **OpenAI-compatible API** (thin tie to Pattern #18 B3 / v112 freellmapi);
- MIT Han Lab's quantization toolchain (SVDQuant/Nunchaku) is efficient-inference-adjacent.

These are component-level coincidences, not corpus connectivity.

**(d) FAIL.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer / (a)-7 | **FAIL** |
| (b) goal-relevance / vault-utility | **FAIL** |
| (c) instructive | **WEAK** (orthogonal field) |
| (d) corpus connectivity | **FAIL** |

**STRICT = 0/4 clear PASS → SKIP.** This is a *more* out-of-scope subject than v84 image-blaster (which was at least a Claude-Code agent-skill bundle with `.claude/`). Sana isn't an agent skill at all.

**Operator decision (2026-05-29): OVERRIDE → INCLUDE.** Recorded honestly as the **2nd operator-elected Phase 0.9 OVERRIDE** in corpus history. Per the v84 Operator-Elected Override policy (routine v2.3 codification candidate), Option **B2 streak-with-override-asterisk** applies:

- Streak notation moves **"44+1\*" → "44+2\*"** (44 PASS + 2 overrides).
- The **25-consecutive-clean-PASS-post-v84** record (held at v114) is **BROKEN** — v116 is itself an override, so the post-override clean-PASS counter resets to **0**.
- **Override-frequency check:** v84 and v116 are **32 wikis apart** → does **NOT** trip the v2.3 redesign triggers (2-in-20 / 3-in-30). Lifetime override frequency = 2 overrides across the v65–v116 window. No Phase 0.9 redesign forced, but this is now a **2-data-point** override series worth watching at the next audit (~v119–v120).

**Honest framing carried to every artifact:** Sana is corpus-knowledge-of-an-outlier. It is NOT a pilot candidate, NOT goal-aligned, and contributes NO change to Pattern Library state.
