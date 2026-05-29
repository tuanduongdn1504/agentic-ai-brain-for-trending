# freellmapi — Beginner Analysis (v112)

**Subject:** `tashfeenahmed/freellmapi` — an OpenAI-compatible **proxy/gateway** that aggregates the **free tiers of 12 LLM providers** behind one `/v1/chat/completions` endpoint, with a priority router, automatic fallover, per-key rate-tracking, encrypted key storage, and a React admin dashboard. *"One OpenAI-compatible endpoint. Twelve free LLM providers. ~1B+ tokens per month."*

**Wiki version:** v112 (v111 hello-agents → **v112**; v110 audit cleared the cadence, so v111 + v112 = wikis OK; next natural audit ~v115).

**Fetched:** 2026-05-29 (GitHub API + README). Created 2026-04-21 (~38 days). **6,171★ / 938 forks** (fork_ratio **0.152** — strong active-deployment) → **~162 stars/day = Pattern #52 HIGH-NOT-EXTREME** (150–300/d), short 38-day window.

**Author:** **Tashfeen Ahmed** (@tashfeenahmed) — **Microsoft**, **Dublin**; bio "Making useful things with Design + Data ⚡️"; 12-yr GitHub account; tashfeen.me; @tashfene. Pakistani-heritage name (Karachi in README examples). ~12 community contributors (incl. @VinhPhamAI, a contributor — not the author). **NOT a VN/Asian-cluster cultural-peer.**

**License:** **MIT** (LICENSE file present **and** GitHub API agree — clean, no mismatch; unlike v111's CC-vs-NOASSERTION).

**Verdict:** **STRONG INCLUDE 3/4** — (a) **FAIL** (Microsoft-Dublin corporate engineer, Pakistani-heritage; no Asian-cluster membership, English-only no locale-inclusion) / (b) STRONG (LOW cost-to-try × INDIRECT-but-real dev-utility fit; explicitly NOT a Claude replacement) / (c) STRONG (rich reference architecture: adapter-pattern + priority-router + rate-ledger + fallover + sticky-sessions + key-encryption + tool-call translation) / (d) STRONG (high corpus connectivity: v73 sibling + v72 + v78 + Patterns #84/#18/#57/#66). See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md`.

**Phase 4b PRIMARY:** **Pattern #18 sub-archetype #8 "Multi-Provider/Runtime LLM Aggregator" N=2 STRENGTHENING** (v73 cc-switch config-switcher anchor + v112 freellmapi live-routing-proxy). Both aggregate ~12 LLM providers into one surface; distinct mechanisms (desktop switch-one-active vs server route-all-live) = genuine cross-instance spread. **Directly relieves the v2.4-deferred "multi-runtime-aggregator-as-distinct-sub-archetype (v73 N=1 only)" item.** Honest caveat: v73's label was "multi-**RUNTIME**-aggregator" and freellmapi is a "multi-**PROVIDER**-aggregator" → label-generalization flagged for the audit. See `01 Analysis/(C) Pattern-18-Multi-Provider-Aggregator-sub-archetype-N2-strengthening.md`.

**Streak:** **"42+1*"** (23rd consecutive clean Phase 0.9 PASS post-v84 OVERRIDE). ~97.7% INCLUDE rate (44-instance window, 43 PASS + 1 OVERRIDE).

**Honest non-claims:** NOT a Pattern #52 promotion (HIGH-NOT-EXTREME CONFIRMED v73); NOT a Claude Code skill / NOT in agentskills.io (57k) chain (it's a proxy — no SKILL.md/AGENTS.md/plugin); NO new top-level Pattern (sub-archetype N=2 strengthening only); NOT (a)-7 Foundational-Vendor-Direct-Source (author is *at* Microsoft but this is a **personal** repo `tashfeenahmed/*`, not `microsoft/*`); (a) FAILS honestly; (b) caveat = does NOT serve the core Claude-based wiki routine (no frontier models).

**Files:**
- `02 Wiki/index.md`
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md`
- `01 Analysis/(C) Pattern-18-Multi-Provider-Aggregator-sub-archetype-N2-strengthening.md`

**Phase status:** Phase 0/0.9 ✅ · Phase 1-4 wiki ✅ · Phase 4b PRIMARY ✅ · Phase 5-6 vault sync (chapter rename+append + root CLAUDE.md shim) — in progress.
