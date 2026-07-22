# (C) open-lovable — Verdict (LLM Wiki v224)

**Subject:** `firecrawl/open-lovable` — the Firecrawl team's MIT open-source **AI app-builder**: chat / a website URL → Firecrawl scrapes it → an LLM (Claude / GPT / Gemini / Groq) generates a React + TypeScript + Tailwind + shadcn/ui app → runs live in a Vercel / E2B sandbox → iterate + download. The open-source, code-you-own answer to **Lovable.dev**; the **"clone/recreate any website"** flavor of the prompt-to-app category.

**Author:** Firecrawl Inc. (the Firecrawl team, f.k.a. Mendable AI) — **NOT Anthropic**. **Same author as firecrawl v214** + uses Firecrawl as a core dependency.

---

## Decision: **INCLUDE — GOAL-ALIGNED 3/4** · **1 NEW §C standalone at N=1 (LEANING MINT)** · counts UNCHANGED **46/11**

| Criterion | Call | One-line why |
|---|---|---|
| (a) Anthropic / cultural-peer | **FAIL** | Firecrawl Inc., not Anthropic (§41). #19 19a returning author (2nd Firecrawl-org subject after v214). |
| (b) Goal relevance | **STRONG** (keys the tier; ⚠️ MODERATE-reviewable) | An autonomous LLM-driven software-*generation* system = Goal #1 core; Claude-capable; the canonical OSS AI-app-builder/website-cloner reference. STRONG-not-STRONGEST = a Firecrawl *example/demo* app + a website-cloning vertical + Claude 1-of-5 providers. Cleanly GA (no §40). |
| (c) Completeness | **STRONG** | Real ~28k★ MIT Next.js pipeline (scrape→LLM→sandbox), multi-provider, Vercel/E2B secure sandboxes, Morph Fast-Apply. Caveats: "example app," NOT source-cloned, hard parts upstream (Firecrawl/LLM/Vercel-E2B), page-stated stars → NOT #52. |
| (d) Connectedness | **STRONG** | firecrawl v214 (same-org dependency, NOT #57) + the AI-app-builder category + provider-agnostic seam (#84 84c) + Vercel/E2B code-sandbox + structured-surface thread + hireui (Goal #2). |

**Tier:** **T5 Agent-as-application** (AI app-builder flavor; the openinterpreter v223 / Kilo Code v177 / OpenHands v30 tier) — with a T2 self-hosted-web-app facet.

---

## Pattern outcome (LEANING MINT, reviewable)

**1 NEW §C live standalone at N=1 (CORPUS-FIRST for the AI-app-builder / prompt-to-app surface, NOT world-first):**
**"Open-Source AI App-Builder — Chat/Website-to-Running-App Generator with Live Sandbox Preview (the Lovable / v0 / Bolt.new / bolt.diy class)."**

- **Mint-favorable:** a genuinely-distinct, **corpus-unrepresented capability** (prompt/site → generated running app + live sandbox) — a **NEW adjacent cluster** (prompt-to-app builders), **sibling to, not a member of, the coding-agent-products cluster** (those help you code in your repo; open-lovable generates a whole app). A working **tool/capability** (mint-favorable side of the v201 line), not a collection. Mint at N=1 per grok-build v215 / openinterpreter v223 / fff v194.
- **⚠️ NO-MINT alternative recorded (reviewable):** "a Firecrawl example/demo app + a website-cloning vertical in a populated non-world-first category → a corpus-knowledge data-point on the firecrawl v214 showcase / instance-strengthening (the lobehub v222 domain-not-capability + awesome-llm-apps v201 fame-≠-mint discipline)."
- **Flagged to the OVERDUE ~v221 audit** (last audit v212): the coding-agent-products meta-cluster (openinterpreter v223's flag) + this NEW prompt-to-app-builder cluster.

**Either way counts UNCHANGED 46/11.** §C live standalones **46 → 47**; §C surface **≈53 → ≈54**.

**SECONDARY (NOT minted):** #19 19a (2nd Firecrawl-Inc. author) · firecrawl v214 same-org dependency (NOT #57) · #84 84c provider-agnostic (NO N-bump) · Vercel/E2B code-sandbox cross-ref · Morph "Fast Apply" cross-ref · #66 (generated code runs in a sandbox = safe; Firecrawl API egresses the scraped site; BYO keys; MIT = safe to borrow, unlike firecrawl's AGPL core; NOT source-cloned).

**NON-claims:** NOT world-first · NOT OSS-first (bolt.diy precedes) · NOT #52 · NOT #57 · NOT #18 B1-MCP · NOT a coding-agent-products cluster member · NOT a new top-level pattern (max #85) · NOT source-cloned.

---

## Streak / §35

**v223 GA:81 → `GA:82 · OG:13 [7 ov]`** (cleanly GA; 5 consecutive GA post the v219 OG break). **§35 CLEAR** (window {v222 GA, v223 GA, v224 GA} = 0 OG).

---

## Blunt take + PILOT

**Blunt:** open-lovable is a genuinely on-goal subject — an autonomous LLM-driven *software-generation* system (Goal #1) and the corpus's first prompt-to-app / AI-app-builder subject — **but it's the Firecrawl team's showcase/demo app in a specific website-cloning vertical, powered by upstream Firecrawl + upstream LLMs + upstream Vercel/E2B sandboxes.** The corpus value is (1) the **collision-clean corpus-first capture** of the AI-app-builder category, (2) the **leaning-mint §C standalone + the honest NO-MINT alternative**, and (3) two genuinely-transferable ideas: the **provider-agnostic LLM seam** and the **scrape→structured→LLM→structured-output loop**. It is **NOT a hireui component** — hireui is a hand-built recruitment SaaS, not a prompt-to-app'd one.

**PILOT — on-goal (Goal #1) as a reference architecture + a fast internal-tool/prototype builder; NOT a hireui product component:**

⭐ **One-thing path A1 → C11 → B5:**
- **A1** — read the scrape → LLM → codegen → sandbox loop + the multi-provider seam (zero install; internalize how a modern prompt-to-app agent is wired, and where Firecrawl v214 slots in as the perception layer).
- **C11** — install-snapshot + `pnpm dev` with **YOUR** Firecrawl + Claude keys against a **public, non-sensitive** site to prove the loop end-to-end (the generated code runs in the Vercel/E2B sandbox, not on your machine).
- **B5** — borrow the **provider-agnostic LLM seam** (Claude/GPT/Gemini/Groq behind one seam) into hireui's first-LLM-feature / vendor-seam spec (composes with meetily v196 `generate_summary()` + AIRI v210 `xsAI` + lobehub v222 + the mosh-ai A2 seam).

Off-goal-personal (fine): use open-lovable to rebuild a hireui **marketing/landing page** or an internal tool fast (off the product core, MIT-licensed, code-you-own).

**Fence:** install-snapshot before install + **the Firecrawl API egresses the scraped target site to Firecrawl's cloud** (public sites only; never candidate/sensitive data) + BYO Claude key, never a live account on first run + generated code runs in the **Vercel/E2B sandbox** (don't run untrusted generated code on your machine) + NOT source-cloned → treat as untrusted-until-inspected + MIT = safe to fork/borrow (unlike firecrawl v214's AGPL core) + **hireui stays hand-built per its CONSTITUTION** (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first; no LLM spend yet → design/spec) — do NOT prompt-to-app the product.

**Full method menu:** `(C) open-lovable — Pilot Methods Menu.md`.

---

*Verdict produced INLINE + hand-verified per `feedback_wiki_verify_independently_check_collisions` (no workflow/subagent — the ~205K shim overflows subagents, the v200→v223 self-throttle). Shipped on branch `wiki/v224-open-lovable` off the v223 tip (`a090d50`); not auto-merged — operator reviews + merges.*
