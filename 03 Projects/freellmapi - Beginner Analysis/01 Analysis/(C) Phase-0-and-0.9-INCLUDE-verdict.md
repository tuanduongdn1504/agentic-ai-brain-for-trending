# (C) freellmapi v112 — Phase 0 classification + Phase 0.9 STRICT verdict

**Subject:** `tashfeenahmed/freellmapi` — OpenAI-compatible proxy aggregating the free tiers of 12 LLM providers behind one endpoint, with router + fallover + per-key rate-tracking + encrypted key store + React dashboard.
**Fetched:** 2026-05-29 (GitHub API + README). **Routine:** v2.3.1.

---

## Phase 0 — classification

| Axis | Value |
|------|-------|
| Tier | **T2 Service** |
| Archetype | **Multi-provider LLM API aggregation proxy** (OpenAI-compatible gateway) |
| Sub-archetype | **Pattern #18 sub-archetype #8 "Multi-Provider/Runtime LLM Aggregator"** — STRENGTHENS the v73 cc-switch registration (PROVISIONAL N=1 → N=2). New sub-variant 8b "live-routing-proxy" vs v73's 8a "config-switcher". |
| Scale | mid-large (**6,171★ / 938 forks**) |
| Primary lang | **TypeScript** 359,909 B (~98%) + CSS 5,271 + JS 616 + HTML 384 |
| Packaging | **self-hosted Node 20+ server** (git clone + `npm install` + `npm run dev`/`npm run build`) + React/Vite dashboard. **No npm-published package; 0 git tags; 0 GitHub releases.** |
| Origin | solo author (**Tashfeen Ahmed**, Microsoft, Dublin) + ~12 community contributors |
| License | **MIT** (LICENSE file present **and** GitHub API report MIT — clean, no mismatch) |
| Default branch | `main`; homepage `tashfeenahmed.github.io/freellmapi`; topics none |
| Methodology | adapter-per-provider (`Provider` base class: `chatCompletion()` + `streamChatCompletion()`) → priority router (highest-priority healthy key under all rate caps) → AES-256-GCM-decrypt → call provider → on 429/5xx/timeout cooldown + retry next (up to 20 attempts); per-`(platform,model,key)` RPM/RPD/TPM/TPD ledger; sticky sessions (30-min model affinity to avoid mid-conversation hallucination spike); unified `freellmapi-…` bearer key (clients never see upstream keys); health probes (healthy/rate_limited/invalid/error); tool-call round-trip incl. Gemini `functionDeclarations` translation; `X-Routed-Via` + `X-Fallback-Attempts` response headers |
| Providers (12) | Google · Groq · Cerebras · SambaNova · Mistral · OpenRouter (21 free models) · GitHub Models · Cloudflare · Cohere · Z.ai (Zhipu) · NVIDIA (disabled by default) · HuggingFace (router → DeepSeek V4 · Kimi K2.6 · Qwen3) |
| Cross-vendor / LDS | **strongest cross-vendor-tolerance subject in the corpus** (12 vendor APIs behind one adapter layer). Provider catalog is the moving part — re-seed scripts in `server/src/scripts/` track free-tier drift (Pattern #78-adjacent). |

## Velocity-screen + engagement-signal

- Age: **38 days** (created 2026-04-21 → 2026-05-29).
- **6,171★ / 38 d = ~162.4 stars/day → Pattern #52 HIGH-NOT-EXTREME (150–300/d)**, short 38-day window (near the band floor; could decay — a *short-window* HIGH-NOT-EXTREME, not a sustained one like v73's 289d or v111's 264d).
  - HIGH-NOT-EXTREME is **CONFIRMED** (N=3 at v73). This is **post-CONFIRMED N+1 strengthening only** — NOT a promotion.
- fork_ratio = 938 / 6,171 = **0.152** → **strong active-deployment** (above the 0.15 high-bar; people self-host + customise — consistent with a clone-and-run proxy).
- subscriber/star = 28 / 6,171 = 0.0045 → low watch-rate (drive-by-stars-dominant).
- issue/star ≈ 34 / 6,171 ≈ 0.0055 → modest issue activity (healthy for a 38-day-old tool).

## Phase 4b PRIMARY pre-registration

**PRIMARY: Pattern #18 sub-archetype #8 "Multi-Provider/Runtime LLM Aggregator" N=2 STRENGTHENING** (Phase 4b vehicle #3 — within-pattern strengthening at the sub-archetype layer; Pattern #18 is already CONFIRMED top-level). Anchor = v73 cc-switch (PROVISIONAL N=1). Directly relieves the v2.4-deferred item "Multi-runtime-aggregator-as-distinct-sub-archetype (v73 N=1 only)". Proposal at `(C) Pattern-18-Multi-Provider-Aggregator-sub-archetype-N2-strengthening.md`.

**SECONDARY (OC layer, per §25 cascade-discipline — inventoried, not all formally registered):**
- **Pattern #18 sub-mechanism B protocol-variant B3 "OpenAI-compatible-API"** — one-service-many-clients via OpenAI HTTP (joins B1 MCP [v70] + B2 CDP). N=1 candidate.
- **Pattern #84 Cross-Vendor Ecosystem-Tolerance** — strongest cross-vendor subject in corpus (12 vendor APIs). Top-level N+1; the aggregation is *provider-side* (consumes many backends), the inverse of 84c's *consumer-side* provider-agnostic-distribution.
- **Pattern #52 HIGH-NOT-EXTREME N+1** (162/d × 38d short-window).
- **Pattern #57 57c framework/provider-citation density** — clients LangChain · LlamaIndex · Continue · **Hermes (v78 ECC corpus-recursive)**; providers incl. **DeepSeek V4 (v72 cross-link)** · Mistral · Z.ai/GLM · Qwen · Kimi.
- **Pattern #66 supply-chain/security discipline** — AES-256-GCM envelope encryption for keys at rest + unified-key abstraction (apps never see upstream keys) + `ENCRYPTION_KEY` required for startup + explicit dev-key-fallback warning.
- **Pattern #82 quantitative-marketing** — "~1.3 billion tokens/month", "up to 20 attempts", "30 minutes", "~40 MB RSS at idle".
- **Pattern #83 honest-deficiency-disclosure (STRONG)** — full "Limitations" ("No frontier models… For hard problems, pay for a real API"; "Intelligence degrades as the day progresses"; "No SLA, by definition") + "Not yet supported" + "Disclaimer" + "Terms of Service review" sections.
- **Library-vocab #19 Deliberately-Narrow Distribution Profile (CONFIRMED) N+1** — "The scope is deliberately narrow."
- **Library-vocab candidate "Free-Tier-Stacking-as-Capacity-Aggregation"** — economic framing: stack 12 free tiers → ~1.3B tokens/month usable capacity. N=1.
- **Library-vocab candidate "Sticky-Session Model-Affinity (anti-hallucination-on-switch)"** — 30-min per-session model stickiness. N=1.

## Phase 0.9 STRICT — Storm Bear meta-entity

**STRONG INCLUDE 3/4** ((a) FAIL + (b)(c)(d) STRONG):

- **(a) FAIL** — **Tashfeen Ahmed, Microsoft, Dublin** (Pakistani-heritage name; Karachi referenced in README examples). None of the 7 (a) sub-axes PASS: not (a)-1 VN-direct, not (a)-2 native-VN-language (README English-only), not (a)-3 product-locale-inclusion (no VN/Asian locale), not (a)-4 community-org, not (a)-5 multi-org-founder, not (a)-6 East/SE-Asian-cluster (the cluster is VN + China-Mainland + Taiwan + Japan; **South-Asian heritage located in Europe at a foundational vendor is a distinct profile**), not (a)-7 foundational-vendor-direct-source (author works *at* Microsoft, but this is a **personal** repo, not `microsoft/*`). **Per §25 cascade-discipline + the v98 precedent (Indian-diaspora-Berlin flagged but NOT registered to avoid (a)-axis dilution), no new (a) sub-axis is coined for this single South-Asian-Dublin instance.** (a) FAILS. Mirrors v97 Brazil + v98 Berlin + v108 SF.
- **(b) STRONG** — cost-of-trial **LOW** to *try* (git clone + `npm install` + generate `ENCRYPTION_KEY` + add **one** instant-free key like Groq + `npm run dev`; reversible via folder-delete; the vault already runs Node). Reaching the full ~1.3B-token capacity is MODERATE (provisioning 12 free-tier keys is real friction). Applicability is **INDIRECT-but-real**: Storm Bear "builds software" + the #1 goal is "master autonomous agents for software development" — a one-endpoint multi-provider gateway for *experimentation / side-projects / bulk-cheap tasks* is squarely a software-dev utility. Per §10 (LOW + indirect = STRONG (b)). **Honest caveat that scopes the use case (does not kill (b)):** it explicitly offers **no frontier models** ("you will not get GPT-5 or Claude Opus class reasoning through this") → it is **NOT a replacement for Claude Code** and does **not** serve the core wiki-building routine.
- **(c) STRONG** — a genuinely instructive **reference architecture** for multi-provider agent infrastructure: adapter-per-provider, priority router with health + multi-dimensional rate ledger + cooldown, automatic fallover chains, sticky sessions (a clever anti-hallucination detail), envelope key-encryption, and cross-provider tool-call translation. Directly relevant to "autonomous agents for software development". Strong cross-links (v73 / v72 / v78 / Patterns #84/#18/#57/#66).
- **(d) STRONG** — high corpus connectivity: direct sibling to **v73 cc-switch** (provider-aggregation), **v72 DeepSeek-TUI** (DeepSeek V4 is a routed provider), **v78 ECC** (Hermes cited as a compatible client = corpus-recursive); Patterns #84 cross-vendor + #18 one-service-many-clients + #57 citation-density + #66 key-encryption; many corpus-relevant providers (Mistral / Z.ai-GLM / Qwen / Kimi).

**Verdict: STRONG INCLUDE 3/4.** Clean INCLUDE on three STRONG criteria; (a) FAILs honestly. NOT STRONGEST (no STRONGEST criterion). Directly comparable to v97 distill / v98 Anthropic-Cybersecurity-Skills / v108 humanizer (all STRONG 3/4 with (a) FAIL).

### Finding-2 calibration note (per hello-agents Part 3, Ch 12)

The Part-3 read flagged the ~97.7% INCLUDE rate as a possible judge-leniency signal. **v112 is a healthy data point for that question: (a) genuinely FAILED here** (not laundered into a soft PASS), and the verdict is an honest 3/4, not an inflated 4/4. The rubric still discriminates on the (a) cultural-peer axis — a non-VN/non-Asian corporate-vendor engineer FAILs it cleanly, exactly as v97/v98/v108 did. INCLUDE here rests on (b)(c)(d), not on stretching (a).

## Streak + window update

- Prior (post-v111): **"41+1*"** (41 clean PASS + 1 OVERRIDE [v84]); 22nd consecutive clean PASS post-v84 OVERRIDE.
- v112 = clean PASS → **"42+1*"** = **23rd consecutive clean Phase 0.9 PASS post-v84 OVERRIDE**. NEW CORPUS-RECORD streak (first 23-consecutive milestone).
- INCLUDE-rate window: 44-instance window v65–v112 (v106 + v110 audits excluded per the established convention) = **43 PASS + 1 OVERRIDE = ~97.7% INCLUDE rate** (precise 43/44 = 97.73%; ~flat vs v111's 97.7%).
- Strength categorization v65–v112: STRONGEST × 17 + **STRONG × 19 (+1 from v112)** + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1 → STRONG leads STRONGEST by 2.
- Override-frequency: 1-in-44 — well below the 2-in-20 / 3-in-30 v2.3 redesign triggers (§7). Discipline holds.

## Honest non-claims

- No new top-level Pattern; the PRIMARY is sub-archetype N=2 STRENGTHENING, not a promotion to CONFIRMED.
- Not a Pattern #52 promotion (HIGH-NOT-EXTREME CONFIRMED at v73; this is short-window N+1).
- Not a Claude Code skill / not in the agentskills.io (57k) chain — it is a *proxy that OpenAI-clients consume*, with no SKILL.md/AGENTS.md/plugin manifest.
- Not (a)-7 Foundational-Vendor-Direct-Source: the author is a Microsoft employee, but `tashfeenahmed/freellmapi` is a **personal** repo, not at `microsoft/*` — criterion-4 (foundational-vendor primary GitHub org) FAILs.
- CORPUS-FIRST claims are deliberately modest and pressure-test-ready: freellmapi is the **first OpenAI-compatible live-routing aggregation *proxy*** in the corpus (vs v73 cc-switch's desktop config-*switcher*), and the **free-tier-stacking economic framing** appears corpus-novel — both held as cautious notes, not headline structural firsts.
