# (C) open-lovable — Deep Dive (LLM Wiki v224)

> Claude-authored under operator direction ("build LLM wiki for https://github.com/firecrawl/open-lovable"). Verdict produced **INLINE + hand-verified** per `feedback_wiki_verify_independently_check_collisions` — **no workflow / no subagent** (the ~205K shim overflows every subagent > 200K → prompt-too-long; the v200→v223 self-throttle). Source hand-fetched (rendered repo page + raw README + Firecrawl's own tutorial); identity + rename + landscape by WebSearch; collision by sanity-anchored hand-grep of `_state/` + `_patterns/` + `03 Projects/`. ⚠️ **NOT source-cloned** — engineering internals below are README/tutorial/landscape-stated, not code-verified.

---

## 1. What it is (in one breath)

`firecrawl/open-lovable` — repo tagline **"🔥 Clone and recreate any website as a modern React app in seconds"**; About: **"Chat with AI to build React apps instantly. An example app made by the Firecrawl team."**

Open Lovable is an **open-source, self-hosted AI app-builder**: you give it a website URL (or chat a prompt), it uses **Firecrawl** to scrape the target into clean, LLM-ready structured content, an LLM (**your choice of Claude / GPT / Gemini / Groq**) **generates a modern React + TypeScript + Tailwind + shadcn/ui app** from that content, the generated code **runs + previews live in a secure cloud sandbox** (**Vercel Sandbox** default, or **E2B**), and you **chat to iterate** (with optional **Morph "Fast Apply"** for fast incremental edits) — then download the zip and run it locally. It is the **open-source, code-you-own answer to Lovable.dev** — the "clone/recreate any website → React app" flavor of the prompt-to-app / "vibe-coding app builder" category (Lovable / v0 / Bolt.new).

**Blunt framing:** this is Firecrawl's flagship **example/showcase app** — "an example app made by the Firecrawl team," born as "an internal tool to speed up their own development work," open-sourced to demonstrate what Firecrawl (the corpus's **v214** subject) makes possible. That it happens to be one of the most-starred open-source projects in the whole AI-app-builder category (~28k★) is what makes it a genuine, distinct wiki subject rather than a footnote to v214.

---

## 2. Identity, author, license, metrics (hand-verified)

| Field | Value | Source / caveat |
|---|---|---|
| Repo | `firecrawl/open-lovable` (was `mendableai/open-lovable`) | Rendered page + WebSearch (multiple sources reference `mendableai/open-lovable`) |
| Author | **Firecrawl Inc.** — "the Firecrawl team" (f.k.a. **Mendable AI**) | Same org-rename as firecrawl itself (`mendableai/firecrawl` → `firecrawl/firecrawl`). **Same author as v214.** |
| Tagline | "🔥 Clone and recreate any website as a modern React app in seconds" | Repo page |
| About | "Chat with AI to build React apps instantly. An example app made by the Firecrawl team." | Repo page |
| License | **MIT** | Repo page — ⚠️ **contrast firecrawl v214's AGPL-3.0 core**; MIT = no network-copyleft / productization blocker |
| Language | **TypeScript 94.9%** / CSS 3.7% / JS 1.4% | Repo page |
| Stars / forks | **~28k★ / ~5.3k forks** | Page-stated **§37.4** (mocked GitHub API) → **NOT a #52 velocity claim** |
| Releases / version | none surfaced | Repo page (no release/tag shown) |
| Released | early 2025; ~26,700★ "within months" → ~28k now | WebSearch (blog/tutorial) — velocity page/blog-stated, not verified |
| Related product | "For a complete cloud solution, check out **Lovable.dev** ❤️" | Repo page — Lovable.dev is the commercial reference (~$25/mo) |

**#19 19a — returning author.** open-lovable is the corpus's **second Firecrawl-Inc./Mendable-AI subject** (after **firecrawl v214**). Firecrawl Inc. = a YC-backed web-data-for-AI company (founders Peffer / Ciarla / Silberstein Camara; ~$16.2M funded per the v214 wiki). **NOT Anthropic** → **(a) FAIL** per §41 (no Anthropic affiliation; corporate author, not a cultural peer).

---

## 3. How it works — the end-to-end pipeline

From the repo README + Firecrawl's own tutorial (`firecrawl.dev/blog/open-lovable-tutorial`) + third-party guides:

```
[URL or chat prompt]
      │
      ▼
1. SCRAPE   — Firecrawl fetches + renders the target site (handles JS rendering,
              anti-bot), returns clean HTML / "structured, LLM-ready" markdown.
      │
      ▼
2. GENERATE — the chosen LLM (Claude / GPT / Gemini / Groq) writes a modern
              React 18+ / TypeScript / Tailwind CSS / shadcn/ui app from that
              structured content.
      │
      ▼
3. (EDIT)   — Morph "Fast Apply" (optional) applies incremental edits fast when
              you chat further changes ("make the header sticky", "add a pricing
              section") — a fast-apply edit model, not a full regeneration.
      │
      ▼
4. SANDBOX  — the generated code runs + previews live in a secure isolated cloud
              sandbox: Vercel Sandbox (default) OR E2B — "preventing potentially
              harmful [generated] code from affecting your system."
      │
      ▼
5. ITERATE / DOWNLOAD — chat to refine; download the zipped React project and run
              `npm install && npm run dev` locally (you own the code).
```

**The builder itself** is a **Next.js + React + Tailwind** web app you run at `localhost:3000`. **The generated app** is React + TypeScript + Tailwind + shadcn/ui.

**Setup (README):** clone → install (pnpm / npm / yarn) → configure `.env.local` with a **Firecrawl API key (required)** + **≥1 LLM provider key (required)** + optional Morph key + optional sandbox credentials → `pnpm dev`.

⚠️ **Doc-vs-code evolution caveat:** Firecrawl's tutorial (an earlier snapshot) describes **E2B + Vite** as the stack; the **current repo README** describes **Next.js + Vercel Sandbox (default) / E2B + Morph Fast-Apply**. The project has evolved (E2B-first → Vercel-Sandbox-default; Vite → Next.js builder). This wiki documents the **current repo state** and flags the tutorial as an earlier variant. Not source-verified.

---

## 4. Tech stack + integrations

- **Builder framework:** Next.js + React + Tailwind CSS.
- **Generated output:** React 18+ / TypeScript / Tailwind / shadcn/ui components.
- **Scraping:** **Firecrawl** (corpus **v214**) — required. The clean-markdown / structured-scrape layer.
- **LLM providers (BYO key, ≥1 required):** **Anthropic (Claude)**, OpenAI, Google Gemini, Groq. (Claude is a first-class supported provider; no default model surfaced in the README.)
- **Fast edits:** **Morph LLM "Fast Apply"** (optional) — a fast-apply edit model for incremental code changes.
- **Sandbox / live preview:** **Vercel Sandbox** (default; OIDC token recommended, or a PAT) **or E2B** (single API key, "designed for code execution") — secure isolated execution of the generated code.
- **AI SDK / routing library:** not explicitly named in the README/tutorial (multi-provider routing implied; likely the Vercel AI SDK family, **not source-confirmed**).

---

## 5. The category + landscape (world-first denial)

Open Lovable sits in the **AI app-builder / prompt-to-app / "vibe-coding app generator"** category — one of the most prominent AI-product categories of 2025–2026:

- **Lovable.dev** — the category leader; prompt → deployed React+Supabase app for non-devs (~$25/mo). open-lovable's namesake + explicit commercial reference.
- **Bolt.new** (StackBlitz WebContainers) — prompt → app, multi-framework (React/Vue/Svelte/Next/Astro).
- **v0** (Vercel) — started as a UI-component generator (Oct 2023); rebranded v0.dev → **v0.app** (Jan 2026); now full-stack.
- **Mocha**, **Dyad** (local), **Replit Agent**, **Create.xyz**, **Firebase Studio**, **a0.dev** — the broader field.
- **Open-source peers:** **bolt.diy** (the OSS Bolt fork — the closest OSS peer), **ai-app-builder-open**, **Reflex** (Python-first), **Appsmith / ToolJet** (open low-code).

**Verdict on priority:** open-lovable is **NOT world-first** (the category is huge and mature) and **NOT even OSS-first** (bolt.diy precedes as the OSS Bolt clone). What it *is*: the corpus's **first** subject in this category, **one of the most-starred (~28k★) OSS instances**, and the distinctive **"clone/recreate any *website*"** flavor (scrape-an-existing-site-with-Firecrawl → regenerate as clean React), as opposed to the peers' primarily prompt→app-from-scratch angle. So: **corpus-first for the surface, world-canonical-OSS-instance NOT world-first** (the lobehub v222 / awesome-llm-apps v201 "fame ≠ world-first" shape).

---

## 6. The Firecrawl relationship (load-bearing — read carefully)

open-lovable is **doubly tied to the corpus's v214 subject:**

1. **Same author** — Firecrawl Inc. built both `firecrawl/firecrawl` (v214) and `firecrawl/open-lovable`. → **#19 19a returning author.**
2. **Core runtime dependency** — open-lovable **requires a Firecrawl API key** and uses Firecrawl for its scrape stage. open-lovable exists partly **to showcase Firecrawl** ("an example app made by the Firecrawl team"; the v214 wiki already listed "**Lovable**" among Firecrawl's integrations — that's this relationship, one level up).

**This is a same-org self-reference + a corpus-recursive dependency — NOT a Pattern #57.** Per the **video-use v198 discipline** ("same org's own prior product = self-reference, logged NOT-#57"; browser-use v41 → video-use v198 was the precedent), and distinct from the **page-agent v199** genuine #57 (a *different* author, Alibaba, deriving from browser-use v41). open-lovable using firecrawl = the same shop's demo app using the same shop's product → a strong same-org companion cross-ref + a corpus-recursive-dependency data-point (a v224 subject depending on the v214 subject, same org, openly credited — cleaner than cortex-hub v181's silent bundling of GitNexus v33). **NOT #57.**

---

## 7. Four-criteria scoring (routine v2.7)

- **(a) FAIL** — Firecrawl Inc. / the Firecrawl team, **not Anthropic** (§41 — no name/heritage/locale/notability rescue; corporate author, not a cultural peer). Returning author (#19 19a; 2nd Firecrawl-org subject after v214).
- **(b) STRONG keys the tier (⚠️ MODERATE-reviewable)** — open-lovable **is an autonomous, LLM-driven software-*generation* system** = dead-center on Goal #1's core ("master … autonomous agents for **software development**"). It runs an agent loop (scrape → generate → edit-apply → sandbox → iterate), is **Claude-capable** (Anthropic a first-class provider), and is the **canonical OSS reference** for the prompt-to-app / website-cloner category — plus it lands on the vault's **provider-agnostic-vendor-seam** (5 providers behind one seam), **LLM-codegen**, and **structured-surface-not-raw-dump** threads. **STRONG-not-STRONGEST** because it's a **third-party *example/demo* app** whose raison d'être is showcasing Firecrawl v214, a **narrow website-cloning vertical**, and **Claude one of 4–5 providers** (not Claude-first). **Cleanly GOAL-ALIGNED via §31** — on-goal by (b), no §40 backstop needed. *(The MODERATE reading — "a demo/vertical showcase, not core agent infra" — is recorded as the reviewable alternative.)*
- **(c) STRONG** — a real, working, ~28k★ MIT Next.js app with a genuine end-to-end pipeline, multi-provider LLM support, Vercel/E2B secure sandboxes, and Morph Fast-Apply. **Caveats:** explicitly **"an example app"** (a reference/demo, not a hardened product); **NOT source-cloned** (README + tutorial + landscape only); the **hard parts are all upstream** — scraping = Firecrawl v214, codegen = the LLM, sandboxing = Vercel/E2B → open-lovable is an **orchestration/glue layer**; stars page-stated §37.4 → NOT #52; doc-vs-code evolution (§3 caveat).
- **(d) STRONG** — firecrawl v214 (same-org dependency, §6) · the AI-app-builder category (Lovable / v0 / Bolt.new / bolt.diy) · the autonomous-agents-for-software / LLM-codegen thread · **#84 84c** provider-agnostic (5 providers behind one seam — a hireui-vendor-seam data-point, the meetily v196 / AIRI v210 `xsAI` / lobehub v222 shape) · the **Vercel/E2B code-execution-sandbox** thread (a "run untrusted generated code safely" pattern) · the **structured-surface-not-raw-dump** thread (it consumes Firecrawl's clean markdown → regenerates; browser-use v41 / page-agent v199 / PixelRAG v211) · **Morph "Fast Apply"** (a fast-edit codegen technique) · self-hosted-app-platform family adjacency (lobehub v222) · **hireui** (Goal #2 — the scrape→LLM→structured-output loop ≈ the CV-parse / company-enrichment threads; the provider-agnostic seam ≈ the hireui vendor-seam blueprint).

**INCLUDE — GOAL-ALIGNED 3/4.**

---

## 8. Pattern outcome — 1 NEW §C standalone at N=1 (LEANING MINT)

**Minted (leaning):** a NEW §C live standalone —

> **"Open-Source AI App-Builder — Chat/Website-to-Running-App Generator with Live Sandbox Preview (the Lovable / v0 / Bolt.new / bolt.diy class)"** — **N=1**, anchor **v224 open-lovable**.

**Why mint (the mint-favorable case):**
- **Genuinely distinct + corpus-unrepresented capability.** The **coding-agent-products** cluster (Kilo Code v177 / grok-build v215 / openinterpreter v223 / CodePilot v161 / larksuite v143 / DeepSeek-TUI v72) are agents that **help you code in your existing repo** (edit files, run commands, TUI/IDE). open-lovable **generates a whole running app from a prompt/site + previews it in a live sandbox** — a different loop, output type, and user (non-dev/prosumer). **No corpus subject occupies this.** It opens a **NEW adjacent cluster** (prompt-to-app / AI app builders), sibling to — not a member of — the coding-agent-products cluster.
- It's a **tool/capability**, not a curated collection → on the mint-favorable side of the v201 awesome-llm-apps line ("§C standalones are reserved for tools/capabilities — fff / openwiki / page-agent / career-ops"; awesome-llm-apps was a collection → NO MINT).
- "Prompt-to-app builder" is a **capability class** (a distinct kind of agent), not a domain (recruitment / meeting-notes / forecasting) → passes the capability-shaped test.
- Mint at **N=1** per the **grok-build v215 / openinterpreter v223 / fff v194 / serve-sim v183 / llm-space v221** precedent (mint N=1 for a genuinely-distinct, corpus-first *capability* surface, scoped NOT-world-first).
- **Scope: corpus-first for the surface, NOT world-first** (Lovable / v0 / Bolt.new precede commercially; bolt.diy precedes as the OSS peer) — scoped conservatively.

**⚠️ NO-MINT alternative recorded (operator/audit-reviewable):**
> "open-lovable is a **Firecrawl example/demo app** (its explicit self-description) + a **website-cloning vertical** in a **populated, non-world-first category** → a **corpus-knowledge data-point on the firecrawl v214 showcase / instance-strengthening**, NOT a category-defining §C mint (the **lobehub v222** domain-not-capability + **awesome-llm-apps v201** fame-≠-mint discipline)."

**Leaned MINT** because the category is genuinely corpus-unrepresented, open-lovable is a working tool (not a collection), and it's the clearest + most-starred OSS instance — but the "it's a demo" reading is defensible and RECORDED (the exact openinterpreter v223 handling).

**⚠️ AUDIT FLAG (load-bearing):** the **~v221 audit is OVERDUE** (last audit v212, window v203–v212; v213–v224 all shipped since). openinterpreter v223 already flagged the **coding-agent-products meta-cluster** (Kilo Code v177 / grok-build v215 / larksuite v143 / CodePilot v161 / openinterpreter v223) as needing an audit cluster-vs-standalones decision. open-lovable adds a **second adjacent cluster** — **prompt-to-app / AI app builders** (open-lovable now; watch for bolt.diy-class peers). The overdue audit should decide how the coding-agent-products cluster AND the app-builder cluster relate + whether either should become a Library-vocab item. open-lovable's standalone is minted **provisionally** and flagged into that decision.

**Either way, counts UNCHANGED 46/11.** §C live standalones **46 → 47**; §C surface **≈53 → ≈54** (if the mint stands).

**SECONDARY (recorded, NOT minted):**
- **#19 19a** — first-instance-repeat: 2nd Firecrawl-Inc. author (after v214).
- **firecrawl v214 same-org dependency** — a corpus-recursive-dependency data-point; **NOT #57** (self-reference, §6).
- **#84 84c** provider-agnostic-by-design (Claude/GPT/Gemini/Groq behind one seam; **NO N-bump** — the mechanism is a multi-provider config, not the ponytail v168 native-rule-file generator).
- **Vercel/E2B code-execution-sandbox** cross-ref — a "run untrusted generated code in an isolated sandbox" pattern (a security-forward data-point; the corpus's clearest prominent sandbox-preview subject).
- **Morph "Fast Apply"** — a fast-edit codegen technique cross-ref (interesting, not corpus-central).
- **#66 supply-chain / runtime** — the **generated code runs in a Vercel/E2B sandbox** (mitigates the "run AI-generated code" risk — don't run it on your machine); the **Firecrawl API egresses the scraped target site to Firecrawl's cloud** (a data-egress consideration); BYO keys; MIT (safe to fork/borrow, unlike firecrawl's AGPL core); NOT source-cloned → treat as untrusted-until-inspected.

**NON-claims:** NOT world-first (a huge mature category) · NOT OSS-first (bolt.diy precedes) · NOT #52 (~28k★ page-stated §37.4 + likely brand-carried → velocity unestablishable) · NOT #57 (the firecrawl dependency is a same-org self-reference) · NOT #18 B1-MCP (ships no MCP server) · NOT a member of the coding-agent-products cluster (a sibling app-builder cluster) · NOT a new top-level pattern (max #85) · NOT source-cloned (flagged).

**Tier:** **T5 Agent-as-application** (an interactive AI app-builder that IS an LLM agent generating software — the openinterpreter v223 / Kilo Code v177 / OpenHands v30 tier), with a **T2 self-hosted-web-app facet** (`pnpm dev` → localhost:3000).

---

## 9. Streak / §35 / counts

- **Streak: v223 GA:81 → `GA:82 · OG:13 [7 ov]`** (cleanly GA on (b) STRONG; **5 consecutive GA post the v219 OG break** — v220 GA + v221 GA + v222 GA + v223 GA + v224 GA).
- **§35 CLEAR** — window {v222 GA, v223 GA, **v224 GA**} = 0 OG.
- **Counts UNCHANGED 46/11** (46 top-level patterns / 11 CONFIRMED Library-vocab). **§C live standalones 46 → 47** (leaning-mint); **§C surface ≈53 → ≈54**.

---

## 10. Verification trail (how this was confirmed, by hand)

- **Source** hand-fetched: rendered repo page (`github.com/firecrawl/open-lovable`) + raw README + Firecrawl's own tutorial (`firecrawl.dev/blog/open-lovable-tutorial`).
- **Identity + rename + landscape** by WebSearch: Mendable AI = the Firecrawl team; repo `mendableai/open-lovable` → `firecrawl/open-lovable` (same org-rename as firecrawl v214); released early 2025, ~26.7k→28k★; the Lovable/v0/Bolt.new/bolt.diy category (world-first denial).
- **Collision by sanity-anchored hand-grep** of `_state/` + `_patterns/` + `03 Projects/`: **CLEAN** — every "lovable" hit is incidental (v214 firecrawl's own entry lists "Lovable" as a Firecrawl *integration*; x1xhlol v21 lists "Lovable" among 31 archived AI-tool prompts; v1–29 a landscape mention). **No `open-lovable` subject; no `open-lovable - Beginner Analysis` folder** (only `firecrawl - Beginner Analysis` exists). The §C registry (rows 54–104) holds **no app-builder / prompt-to-app / website-cloner standalone** (the term-grep matches were all §F prose — e.g. v201 awesome-llm-apps' landscape E2B mention). Anchors (firecrawl=v214, PilotDeck, OpenHuman) confirm the grep works.
- **inflation_check HELD:** 1 mint ≤ 2; N=1 corpus-first-for-surface-NOT-world-first with the NO-MINT alternative + the not-a-coding-agent-products-cluster-member distinction recorded + flagged to the overdue audit; counts 46/11 unchanged; max #85; no double-count; no improper N-bumps (#84 84c NO N-bump; the firecrawl dependency NOT-#57).

*Docs: this Deep Dive + `(C) open-lovable — Verdict.md` + `(C) open-lovable — Pilot Methods Menu.md` + `wiki.html`. State: `_state/03c-projects-v61-v183.md` (v224 entry) + `_patterns/06-library-vocab-registry.md` (§C row + §F log). Shipped on branch `wiki/v224-open-lovable` off the v223 tip (`a090d50`); not auto-merged.*
