# (C) AIRI — Pilot Methods Menu (LLM Wiki v210)

**Subject:** `moeru-ai/airi` — a self-hosted AI companion / VTuber. **Domain off both goals; the architecture is the prize.**
**Honest framing:** AIRI is NOT a product to adopt for software-dev or hireui. The value is **(A) read the architecture** and **(B) borrow patterns zero-install** — chiefly the `xsAI` provider-agnostic seam. Hands-on (C) and any hireui touch (D) borrow *architecture only*. (E) is off-goal-but-fun. (F) is vault-meta.

**⭐ One-thing path: A1 → B5 → D16** — read the `xsAI` seam (zero install) → distil a "provider-agnostic LLM seam" reference into the vault + hireui's first-LLM-feature spec (composes with meetily v196 `generate_summary()` + the mosh-ai A2 seam) → use it as the vendor-seam for hireui's first LLM feature (Match-Explain / candidate-summariser) on an `agent-*` branch, per the RATIFIED candidate-LLM legibility ADR + hireui's CONSTITUTION.

---

## A — Read & learn (zero risk, highest ROI, on-goal)

1. **⭐ Read the `xsAI` provider-agnostic seam** — how 30+ LLM providers hide behind one TS interface; where Claude's shape genuinely differs; how the app stays provider-agnostic while still using per-provider features. The vendor-seam masterclass. *(the meetily v196 / mosh-ai A2 thread.)*
2. **Read the Brain/Ears/Mouth/Body decomposition** — a clean mental model for an embodied real-time multimodal agent (reasoning / audio-in / audio-out / avatar). Note how each faculty is a swappable provider layer.
3. **Read the game-agent loop** (Minecraft/Factorio) as a perceive→reason→act exemplar — the same autonomy loop as browser-use v41 / page-agent v199, in a game world. What is the "observation" surface? How is the action space bounded?
4. **Read the memory design** — Memory Alaya + `memory-pgvector` + in-browser DuckDB-WASM/pglite. How does a persistent companion decide what to remember, and how does an *in-browser* vector store change the tradeoffs? *(CC-memory-systems thread.)*
5. **Read `unspeech`** — a universal ASR/TTS proxy = the *audio* analogue of the LLM seam. The same "one interface, N providers" pattern applied to speech.
6. **Read the web-first architecture choice** — why WebGPU/WASM/Workers from the start, and what desktop/mobile builds unlock (TCP-only features). A case study in "ship in the browser, escape to native only when forced."

## B — Borrow patterns (zero install, into the vault / hireui specs)

7. **⭐ Distil a "provider-agnostic LLM seam" reference** into `05 Skills/` (or hireui's LLM-feature spec) from `xsAI` + meetily v196 `generate_summary()`: one call shape, Claude's genuine deltas special-cased, no lock-in. *(highest-ROI borrow.)*
8. **Borrow the speech-proxy pattern** (`unspeech`) as a template if hireui ever adds voice (interview transcription): one ASR/TTS interface, swappable backends.
9. **Borrow the in-browser persistence idea** (DuckDB-WASM / pglite) as a candidate for client-side scratch/cache state — evaluate vs the token/latency cost.
10. **Borrow the MCP-Launcher approach** as a reference for building hireui's future MCP server (compose with the palmier-pro v192 `ToolExecutor` template + OfficeCLI v206 MCP context).
11. **Borrow the perceive→reason→act framing** into any hireui agentic feature's design doc — bounded action space + explicit observation surface (composes with browser-use v41 / page-agent v199).
12. **Borrow the anti-scam posture** — AIRI's explicit "no official crypto/token" notice is a good template for any viral OSS project's impersonation-defense README line (a #66 hygiene note).

## C — Hands-on, scratch only (low-risk trials)

13. **Run `stage-web` in the browser** (airi.moeru.ai) to *feel* the real-time voice + avatar loop — no install, understand the UX latency budget.
14. **Install-snapshot + build the monorepo on a scratch machine** — see the packaging (Electron `stage-tamagotchi`), measure the footprint, inspect what a companion app actually bundles. *(install-snapshot + npm-security-check first.)*
15. **BYO-keys, scratch account** — wire `xsAI` to Claude via your own key in a throwaway config; watch one request/response to see the seam in action. Never a live/primary account first-run.
16. **Read the actual `xsAI` source** (clone the standalone SDK) if you want to verify the seam claims code-level (this wiki was WebFetch-only — not source-cloned).

## D — hireui / Goal-#2 (architecture-only, behind the CONSTITUTION fence)

17. **⭐ Apply the provider-agnostic seam** as hireui's first-LLM-feature vendor-seam (Match-Explain / candidate-summariser) on an `agent-*` branch, per the RATIFIED candidate-LLM legibility ADR + the mosh-ai A2 thread. *(the genuine Goal-#2 payoff.)*
18. **Spec hireui's future MCP server** using MCP-Launcher + palmier-pro v192 `ToolExecutor` as templates (read-only tools first).
19. **Evaluate in-browser persistence** for a hireui client-side cache (DuckDB-WASM) vs the standard server path — a measured spike, not a commitment.
20. **Do NOT adopt the companion/avatar layer** into hireui — it's off-domain; note it as an anti-scope line in the ADR.
21. **Borrow the memory-decay/consolidation questions** (Memory Alaya) when designing hireui's candidate-context memory — what to keep, what to forget, residency of PII (compose with the data-residency ADR thread).

## E — Off-goal but fun / personal (both goals aside)

22. **Run AIRI as a personal AI companion** — MIT, self-hosted, BYO-keys; a low-stakes way to experience an embodied multimodal agent end-to-end (fence: scratch machine, verify the real `moeru-ai` org, keys in `.env`, heed the no-token warning).
23. **Try the game-playing agent** (Minecraft) as a hands-on demo of an LLM agent acting in a live environment — instructive for agent-autonomy intuition even though the domain is games.

## F — Vault-meta / audit

24. **File the DEFERRED watch axes** for the ~v212 audit: (a) "self-hosted real-time embodied multimodal AI-companion / VTuber runtime" (the MINT-alternative — re-review vs the meetily v196 domain-not-capability discipline); (b) "MCP-server builder/launcher"; (c) "LLM game-playing agent"; and note **AIRI = the corpus's 3rd speech-domain subject** (fish-speech v20 / meetily v196 / AIRI v210) + the `xsAI` SDK-library member of the LLM-access-tooling family.

---

## Fence (mandatory for any C/D/E touch)

- **install-snapshot** before building/installing; **npm-security-check** (the monorepo pulls many packages).
- **BYO-keys, scratch/disposable account** — never a live/primary account on first run; a companion app *holds your keys*.
- **Verify you cloned the real `moeru-ai`/`@proj-airi` org** (a fork `Ch1nChun/Moeru-ai-airi` exists; the "no official crypto/token" warning signals active impersonation risk).
- **hireui borrows ARCHITECTURE only** (the seam, memory questions, MCP approach) per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first); no companion/avatar scope; no LLM spend yet → build-it-right.
- **Scratch machine** for the desktop/WebGPU build (large Electron/native app).

---

*Pilot menu by Claude (Opus 4.8) under LLM Wiki Routine v2.7. AIRI is a knowledge/architecture subject: read the seam, borrow the patterns, don't adopt the product.*
