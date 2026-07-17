# (C) AIRI — Verdict (LLM Wiki v210)

**Subject:** `moeru-ai/airi` (Project AIRI) — a self-hosted, real-time, embodied AI companion / AI VTuber ("digital life form") with a Live2D/VRM avatar, voice, memory, game-playing agents, and a 30+-provider LLM seam.
**Date:** 2026-07-17 · **Routine:** v2.7 · **Verdict produced INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — **no workflow / no subagent relied on** (the ~205K shim overflows every subagent >200K → prompt-too-long; the v200→v209 self-throttle precedent, 8 consecutive ships).

---

## Decision: GOAL-ALIGNED INCLUDE 3/4 — NO MINT — counts UNCHANGED 46/11

| Criterion | Score | Reasoning |
|---|---|---|
| **(a)** Author = Anthropic / cultural peer | **FAIL** | `moeru-ai` is a non-Anthropic OSS collective; founder Neko (`nekomeowww`) is a disclosed individual, not Anthropic. **§41**: no name/heritage/locale/notability rescue; the disclosed-individual axis is answered NO. First `moeru-ai`/`nekomeowww` author → #19 19a. Clean FAIL. |
| **(b)** Goal-relevance (**keys the tier**) | **MODERATE** | **Goal-adjacent, not on-domain.** The *domain* (AI companion / VTuber / entertainment) is off both goals — zero hireui/Scrum use, not software-development. But it touches **four live goal threads**: the provider-agnostic LLM seam (`xsAI`, the meetily-v196 vendor-seam blueprint), MCP-server tooling (`MCP Launcher`), memory systems (Memory Alaya / memory-pgvector / in-browser DuckDB-pglite), and perceive→reason→act game agents. **§40** (operator-requested + touches live goal threads + (b) MODERATE+) → **GOAL-ALIGNED per operator direction; no override consumed; no §35 pressure.** Held below STRONG because the domain is off-goal entertainment with no direct pilot into either goal. |
| **(c)** Substance / engineering | **STRONG** | Large, mature, production-grade monorepo: ~42.8k★, 79 releases (v0.11.0), 4,000+ commits, TypeScript/Vue, WebGPU/WASM/Workers, cross-platform (web/desktop/mobile), a real ecosystem (`xsAI`, `unspeech`, `MCP Launcher`, `memory-pgvector`, `drizzle-duckdb-wasm`), multi-provider LLM/TTS/STT, VRM+Live2D avatars, game integrations. **Caveats:** much is WIP (Memory Alaya/Factorio WIP, KSP/plugins planned); the hard AI is upstream models it orchestrates; **NOT source-cloned** (WebFetch-only, flagged). |
| **(d)** Corpus fit / cross-references | **STRONG** | Rich threads: meetily v196 (exact off-goal/architecture-is-prize precedent), fish-speech v20 (speech), Pattern #18 #8 aggregator + #84 84c (the `xsAI` seam), agentmemory v66 / supermemory v132 (memory), browser-use v41 / page-agent v199 / serve-sim v183 (perceive-act capability cluster), OpenMontage v188 / agency-agents v185 (the MINT-alternative precedent), the LLM-access-tooling family (cc-switch v73 / CLIProxyAPI v207 / OmniRoute v208). |

**⚠️ OFF-GOAL CAPTURE recorded as the reviewable alternative** (per §40, honesty preserved). AIRI has *zero* Goal-#2 use and an entertainment domain, so the OFF-GOAL reading ("an AI-waifu companion app, off both goals, captured only for its architecture") is defensible — arguably a touch more so than meetily v196's, which at least had a Scrum/recruitment notetaker angle. Under §40 the operator or a later audit can flip it; the ship counts GA.

---

## Pattern outcome: NO MINT

AIRI is **corpus-first for the AI-companion / VTuber / "digital life form" DOMAIN** (collision-clean: 0 hits across `_state/` + `_patterns/` for moeru/nekomeowww/vtuber/waifu/neuro-sama/live2d/vrm/tamagotchi/xsai/proj-airi/kokoro and whole-word `airi`; sanity anchors meetily=17, fish-speech=33 confirm grep works; the only `_patterns/06` "companion" hits are Pattern #50 "Commercial-Funnel **Companion**" + v124 "Companion-App Funnel" + v111 "Companion Framework" [RETIRED] — none an AI-companion §C standalone).

**But corpus-first-for-a-DOMAIN ≠ a mintable §C capability class** — the **meetily v196 / TimesFM v193 / mlsysbook v197 discipline**: §C vocab is capability/tool-shaped; a single off-domain product category enters the corpus as a **knowledge data-point + a DEFERRED watch axis**, not a mint. Recorded watch axis: **"self-hosted real-time embodied multimodal AI-companion / VTuber runtime."**

### ⚠️ MINT alternative recorded (operator/audit-reviewable — the serve-sim v183 / OfficeCLI v206 practice)

A §C standalone **"Self-Hosted Real-Time Embodied Multimodal AI-Companion / VTuber Runtime" (N=1)** is *defensible* on the **OpenMontage v188 / agency-agents v185 / Kilo-Code v177** precedent ("mint N=1 for the corpus-first world-class exemplar of a recurring-but-corpus-unrepresented class" — AIRI IS the ~42.8k★ OSS flagship of the self-hosted-AI-companion class, which recurs via Open-LLM-VTuber / Amica / ChatVRM, none in corpus). **It LOSES to NO-MINT on four grounds:**
1. the **meetily v196 domain-not-capability discipline** (directly on point + the most recent precedent);
2. **§28 anti-inflation** — minting on a domain/product-category, exactly the move declined at meetily v196 / TimesFM v193;
3. **§C vocab is capability/tool-shaped** — "AI-companion runtime" is a product category, not a capability primitive;
4. **NOT world-first** — Neuro-sama / Character.AI / ChatVRM / Amica / Open-LLM-VTuber precede; AIRI is the OSS flagship, not the inventor.

**Either reading → counts UNCHANGED 46/11.** (Unlike OpenMontage v188, which minted because its "agent-FIRST, the coding agent IS the runtime, deliverable = a rendered file" was a genuinely new *agent-capability class* — AIRI is a standalone consumer product with its own runtime, the meetily shape, not the agent-as-X shape.)

---

## SECONDARY (cross-refs, NOT minted)

- **`xsAI` provider-agnostic LLM seam** → **Pattern #18 #8 Multi-Source LLM Aggregator** instance-strengthening (recorded, not self-incremented) + **#84 84c** provider-agnostic-by-design (NO N-bump) + the meetily-v196 `generate_summary()` / mosh-ai A2 vendor-seam thread. `xsAI` is the **SDK-library** member of the LLM-access-tooling family (an app's own seam, distinct from the *gateway-service* members cc-switch v73 / CLIProxyAPI v207 / OmniRoute v208).
- **`MCP Launcher`** → #18 B1-MCP family cross-ref + DEFERRED watch axis "MCP-server builder/launcher" (NOT minted at N=1 as a companion-app sub-component).
- **Memory** (Memory Alaya + memory-pgvector + in-browser DuckDB-WASM/pglite) → CC-memory-systems thread; **in-browser vector memory** is a distinctive facet (agentmemory v66 / supermemory v132 cross-ref).
- **Game-playing agents** (Minecraft/Factorio) → perceive-act cluster (browser-use v41 / page-agent v199 / serve-sim v183) for **game environments**; the corpus's first game-agent facet; DEFERRED watch axis, NOT minted (Voyager/Mineflayer well-established externally; AIRI orchestrates).
- **Speech cluster** → 3rd speech-domain subject (fish-speech v20 / meetily v196 / AIRI v210); `unspeech` universal ASR/TTS proxy + Kokoro local TTS.
- **#19 19a** — first `moeru-ai`/`nekomeowww` (Neko / 絢香猫) author.
- **#66** — self-hosted MIT app holding your keys + mic + games/Discord TCP + local inference; runtime-trust + crypto-scam-impersonation (the project's own no-token warning), not a postinstall vector. Benign-to-moderate.

**NON-claims:** NOT #52 (~42.8k★ page-stated §37.4, velocity unestablishable) · NOT #57 (Neuro-sama/Character.AI/ChatVRM/pixiv/Reka-UI inspirations are non-corpus; mentions ≠ recursion) · NOT #18 B1-MCP *as a subject* (builds+consumes MCP, is not "one server, many clients") · NOT world-first · NOT a new top-level pattern (max #85) · NOT the first model-subject (fish-speech v20; AIRI *uses* models) · NOT a Domain-Vertical-Skill-Collection.

---

## Bookkeeping

- **Counts UNCHANGED: 46 confirmed top-level patterns / 11 CONFIRMED Library-vocab.**
- **§C surface** ≈49 unchanged (no new standalone).
- **Tier: T5 Application** (self-hosted real-time embodied AI-companion / VTuber runtime flavor — the meetily v196 / MoneyPrinterTurbo v123 / Echo Loop v128 tier, cleared on (b) MODERATE via goal-adjacent architecture per §40, NOT an (a)-rescue).
- **Streak: GA:69 → GA:70** (56 consecutive goal-aligned ships v153→v210).
- **§35 CLEAR** — window {v208 GA, v209 GA, **v210 GA**} = 0 OG (v203 = audit); even under the OFF-GOAL reading = 1 OG ≤ 1 → still clear.
- **inflation_check HELD** — 0 mints; the §C standalone DECLINED per §28 (domain-not-capability) + recorded as the reviewable alternative; counts 46/11 unchanged; max #85; no N-bumps self-incremented; NOT #57.

---

## Verification note

- **Source** hand-fetched: repo page + raw README + docs site + WebSearch (identity + landscape).
- **Identity** by WebSearch: Neko / `nekomeowww` / 絢香猫 / `@ayakaneko`; `moeru-ai` collective + `@proj-airi` sub-org; NOT Anthropic.
- **Landscape** by WebSearch: Open-LLM-VTuber (closest OSS peer), Amica, ChatVRM, Neuro-sama, Character.AI — all non-corpus → NOT world-first, NOT #57.
- **Collision** by sanity-anchored hand-grep of `_state/*.md` + `_patterns/*.md` + `03 Projects/` (see the Deep Dive §2 + this doc's Pattern-outcome section) — clean.
- **No workflow / no subagent relied on** (shim overflows subagent context; the v200→v209 precedent). Ultracode note: even under the standing "use a workflow" directive, subagents fail prompt-too-long here → the exhaustive-and-correct path is by hand.

---

## Bottom line

A genuinely impressive, large OSS agentic system — but an **AI-companion / VTuber entertainment product**, off both of your goals. **Include it for the architecture, not the product:** the `xsAI` provider-agnostic seam is the sharpest borrow (your future hireui vendor-seam), with MCP-Launcher, in-browser memory, and the game-agent loop as read-and-learn material. **NO MINT** — the meetily v196 shape exactly.

*Verdict by Claude (Opus 4.8) under LLM Wiki Routine v2.7 §40/§41. See `(C) AIRI — Pilot Methods Menu.md` for the 24-method application menu.*
