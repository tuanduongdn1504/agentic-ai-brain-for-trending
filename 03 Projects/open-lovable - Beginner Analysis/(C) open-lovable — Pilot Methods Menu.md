# (C) open-lovable — Pilot Methods Menu (LLM Wiki v224)

> How to actually *apply* `firecrawl/open-lovable`. Honest menu (~20 methods, not a padded 24). **The subject is on-goal (Goal #1) as a reference architecture + a fast prototype/internal-tool builder; it is NOT a hireui product component.** ⭐ = highest-leverage. The **one-thing path is A1 → C11 → B5**.
>
> **Standing fence (applies to every hands-on method):** install-snapshot before installing · the **Firecrawl API egresses the scraped target site to Firecrawl's cloud** → **public, non-sensitive sites only**, never candidate/company/sensitive data · **BYO Claude/Firecrawl keys**, never a live account on first run · the **generated code runs in the Vercel/E2B sandbox** — do NOT run untrusted generated code on your machine · **NOT source-cloned** → treat the repo as untrusted-until-inspected · **MIT** = safe to fork/borrow (unlike firecrawl v214's AGPL core) · **hireui stays hand-built** per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first; no LLM spend yet → design/spec) — do NOT prompt-to-app the product · pin the commit you clone (no releases surfaced).

---

## A — Read & learn (zero install, highest safety)

- **⭐ A1 — Read the full loop.** Trace the pipeline end-to-end from the README + Firecrawl's tutorial: URL → Firecrawl scrape (clean/structured markdown) → LLM codegen (React/TS/Tailwind/shadcn) → Morph Fast-Apply edits → Vercel/E2B sandbox preview → download. Internalize **how a modern prompt-to-app agent is wired** and **where Firecrawl v214 slots in as the perception layer**.
- **A2 — The provider-agnostic seam.** Read how it routes across Claude / GPT / Gemini / Groq behind one seam (the `.env.local` provider config). This is the reusable architectural idea (→ B5).
- **A3 — The sandbox-isolation design.** Read why generated code runs in a Vercel/E2B sandbox ("preventing potentially harmful code from affecting your system") — the "run untrusted AI-generated code safely" pattern.
- **A4 — Category study.** Map open-lovable against Lovable.dev / v0 / Bolt.new / bolt.diy — where the "clone/recreate any *website*" (Firecrawl-scrape-then-regenerate) angle differs from prompt→app-from-scratch. Useful context for Goal #1's understanding of the 2026 AI-app-builder landscape.
- **A5 — Morph "Fast Apply."** Read what a fast-apply edit model does (fast incremental code edits vs full regeneration) — a codegen-editing technique worth knowing.

## B — Borrow patterns (zero/low install, into the vault or hireui spec)

- **⭐ B5 — The provider-agnostic LLM seam → hireui's first-LLM-feature / vendor-seam spec.** Lift the "N providers behind one seam, config-selected" shape (composes with meetily v196 `generate_summary()` + AIRI v210 `xsAI` + lobehub v222 + the **mosh-ai A2 seam**). Highest-ROI borrow; on an `agent-*` branch, design/spec only (no LLM spend yet).
- **B6 — The scrape→structured→LLM→structured-output loop → the hireui CV-parse / company-enrichment threads.** open-lovable's "scrape a site → clean structured content → LLM produces a structured artifact" ≈ the firecrawl v214 D16 public-web-enrichment + wardrobe v217 CV-parse + PixelRAG v211 threads. Borrow the discipline (structured surface in, structured artifact out), not the app-builder itself.
- **B7 — The sandbox-isolation rule into `CLAUDE.md` / hireui's LLM-integration ADR.** "Any AI-generated code that must run is executed in an isolated sandbox, never on the host / never in the product runtime." A clean safety invariant.
- **B8 — Write a one-pager: "what a prompt-to-app builder is + how it differs from a coding-agent CLI"** into `05 Skills/` — closes the corpus's understanding of the AI-app-builder cluster (sibling to the coding-agent-products cluster).

## C — Hands-on trials (fenced; scratch only)

- **⭐ C11 — Prove the loop.** install-snapshot → clone (pinned) → `pnpm install` → `.env.local` with **your** Firecrawl + Claude keys → `pnpm dev` → point it at a **public, non-sensitive** site → watch scrape → generate → sandbox-preview end-to-end. ~15 min; the fastest way to internalize the architecture.
- **C12 — Provider bake-off.** Run the same target through Claude vs GPT vs Gemini vs Groq; compare generated-code quality/cost. A cheap, real datapoint for the model-routing / cost thread.
- **C13 — Sandbox choice.** Try E2B (single key) vs Vercel Sandbox (default; OIDC) — note the tradeoffs for any future "run generated code" need.
- **C14 — Morph on/off.** Toggle Morph Fast-Apply; observe edit latency/quality on incremental changes.

## D — hireui / Goal #2 (design/spec only; behind the CONSTITUTION)

- **⭐ D15 — Vendor-seam ADR.** Turn B5 into a hireui vendor-seam ADR (the provider-agnostic seam as the template for hireui's first LLM feature — Match-Explain / candidate-summariser). On an `agent-*` branch; composes with the RATIFIED candidate-LLM legibility ADR + the Mosh A2 seam. **No LLM spend yet → build-it-right.**
- **D16 — Sandbox-invariant ADR.** If hireui ever needs to run user/candidate-supplied code or generated snippets, write the "isolated sandbox only" invariant (B7) into its LLM-integration ADR.
- **D17 — DO NOT productize.** Explicitly record: hireui is hand-built per its CONSTITUTION; open-lovable is a reference to study, not a builder to run against the product. (A guardrail note, not a task.)

## E — Off-goal-personal (fine, off the product core)

- **E18 — Rebuild a landing/marketing page fast.** Use open-lovable (MIT, code-you-own) to regenerate a hireui/TalentAxis **marketing** page or an internal tool from a reference site — off the product core, fully fenced (public sites, sandbox, own keys).
- **E19 — Personal prototype builder.** Keep open-lovable as a fast throwaway-prototype tool for non-product ideas.

## F — Vault-meta

- **F20 — File the §C mint + the NO-MINT alternative** for the overdue ~v221 audit (this ship did this in `_patterns/06`).
- **F21 — The AI-app-builder-cluster synthesis.** Write the note distinguishing the **prompt-to-app-builder cluster** (open-lovable now) from the **coding-agent-products cluster** (Kilo Code v177 / grok-build v215 / openinterpreter v223) — feed both to the audit.
- **F22 — The firecrawl v214 ↔ open-lovable v224 same-org-dependency data-point** (a v224 subject depending on the v214 subject, same org, openly credited — cleaner than cortex-hub v181's silent GitNexus v33 bundling; NOT #57).

---

**Bottom line:** the honest top-3 is **A1 (read the loop) → C11 (prove it on a public site, sandboxed, own keys) → B5 (borrow the provider-agnostic seam into hireui's vendor-seam spec)**. Everything past that is optional/off-goal. open-lovable is a genuinely on-goal, corpus-first capture of the AI-app-builder category and a clean provider-seam reference — but it is a demo/showcase, so borrow the architecture, don't adopt the product.
