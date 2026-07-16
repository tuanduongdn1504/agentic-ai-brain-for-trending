# (C) CLIProxyAPI — Pilot Methods Menu

> **Wiki v207** · 2026-07-16 · `router-for-me/CLIProxyAPI`.
> 24 methods across 6 ladders. **⚠️ Standing fence:** the flagship Claude-via-subscription path is **ToS-violating, Anthropic-blocked (April 4 2026), and account-ban-risk** — so this is a **pilot-AVOID-for-Claude** subject. The high-value methods are **read/learn (zero risk)** and **borrow-the-architecture (zero install, official-keys-only)**. Hands-on methods are scratch/disposable-only and never touch your primary Claude/paid accounts.
>
> ⭐ **One-thing path: A1 → A3 → B7** — read the landscape + the ToS boundary → map it against the cortex-hub v181 dependency + hireui's future vendor-seam → write the "use official API keys, never subscription-OAuth reverse-engineering" rule into hireui's LLM-integration ADR (zero install, zero risk).

---

## A — Read & learn (zero risk, highest ROI here)

1. **⭐ A1 — Read the landscape.** Read the README + help.router-for.me + the Deep Dive §6: internalize the "CLI-subscription→unified-API gateway" class (CLIProxyAPI flagship + claude-proxy / CliRelay / ai-cli-proxy-api). This is the grey-market LLM-access layer — knowing it exists + how it works is Goal-#1 landscape fluency.
2. **A2 — Map the multi-protocol front.** Study how one server speaks OpenAI Chat Completions / OpenAI Responses / Gemini `/v1beta` / Claude `/v1/messages` / Codex simultaneously. This is the protocol-translation pattern hireui's eventual vendor-seam will need (minus the subscription-OAuth).
3. **⭐ A3 — Read the ToS boundary as a case study.** The Jan-2026 enforcement + April-2026 Claude-Max block (Deep Dive §7) is the single most useful lesson: it draws the line between *official API keys* (allowed) and *subscription-OAuth reverse-engineering* (blocked, ban-risk). Write this line down — it governs every future hireui LLM decision.
4. **A4 — Study the "model name ≠ backend" footgun.** The docs' own caveat about alias collisions is a real reliability lesson for any provider-routing layer.

## B — Borrow patterns (zero install, into vault / hireui)

5. **B5 — Steal the protocol-translation architecture** as a reference sketch for hireui's vendor-seam (the mosh-ai A2 thread) — one internal interface, N provider adapters, protocol-normalized front. Use **official API keys**.
6. **B6 — Borrow the multi-account round-robin idea** for hireui's *own* keys (rotate across legitimate API keys / rate-limit tiers), never for subscription-OAuth arbitrage.
7. **⭐ B7 — Write the guardrail ADR.** Add to hireui's LLM-integration ADR + `CLAUDE.md`: *"LLM access uses official, paid API keys per vendor ToS — never subscription-OAuth reverse-engineering / CLI-token extraction (see CLIProxyAPI v207: Anthropic-blocked + ban-risk)."* Zero install, protects Goal #2.
8. **B8 — Borrow the path-based provider-routing convention** (`/api/provider/{provider}/...`) as a clean design for hireui if it ever fronts multiple LLM vendors.
9. **B9 — Note the credential-storage gap** (format/encryption undocumented) as an anti-pattern: any hireui secret-holding layer must document + encrypt at rest.

## C — Hands-on (scratch/disposable ONLY, never primary Claude/paid accounts)

10. **C10 — install-snapshot first.** Before any `docker run`/compose, run the install-snapshot skill so you have an uninstall checklist for what it writes.
11. **C11 — Inspect the Docker image** (`eceasy/cli-proxy-api`) in a scratch context — layers, entrypoint, what it persists — before running anything.
12. **C12 — Stand it up empty** (no credentials) in a throwaway container and read the Management API (`/v0/management`) + config surface, to understand the shape without exposing any account.
13. **C13 — If (and only if) evaluating a permitted provider** (a free-tier Gemini/OpenRouter API key you own — NOT subscription-OAuth), point one scratch client at it to see the protocol translation work. Never Claude, never a paid subscription-OAuth login.
14. **C14 — Read the EasyCLI GUI + Management-Center WebUI** source structure (Tauri v2 / WebUI) as examples of managing a proxy — an LV#22 adjacency study.

## D — hireui / Goal-#2 (architecture reference, official-keys-only)

15. **D15 — Vendor-seam reference.** When hireui builds its first LLM feature (the Match-Explain / candidate-summariser thread), use CLIProxyAPI's protocol-normalized front as a *shape* reference for the seam — implemented with the Anthropic SDK + official keys, behind Mosh A2.
16. **D16 — Multi-vendor fallback design.** If hireui ever needs a fallback provider, borrow the aggregator *routing* idea (official keys per vendor), gated by the B7 guardrail.
17. **D17 — Cost-optimization thread linkage.** File CLIProxyAPI as the "grey-market baseline" in the claude-api-cost-optimization notes: the *legitimate* levers (prompt-caching / Batch API / model-tier routing) achieve cost goals without the ToS/ban exposure.
18. **D18 — Candidate-PII boundary.** A self-hosted gateway can be a PII-residency win (traffic stays local) — record this as a *legitimate* reason to run an official-key gateway later, distinct from the subscription-arbitrage the tool is famous for.
19. **D19 — Never in the candidate-outcome path.** Per the ratified hireui candidate-LLM legibility ADR, any candidate-affecting LLM path must be fixed/legible/audited — a grey-market subscription gateway is disqualified there by construction.

## E — Personal / off-goal (fenced)

20. **E20 — Understand the "free models" temptation honestly.** It's real that people run this to stretch subscriptions — but the Jan/April-2026 enforcement means the Claude path is a dead end + a ban risk. Note it, don't do it.
21. **E21 — Watch the cat-and-mouse.** 761 releases in a high-velocity arms race with the vendors whose auth it wraps — a useful signal of how fast the grey-market layer churns.

## F — Vault-meta

22. **F22 — Record the corpus-recursive dependency.** File the hand-verified finding that cortex-hub v181 bundled `eceasy/cli-proxy-api` (= this subject) as its LLM gateway → v181 bundled TWO now-corpus subjects (GitNexus v33 + CLIProxyAPI v207). A DEPENDENCY data-point, NOT #57.
23. **F23 — Flag the mint boundary for the ~v212 audit.** The N=1-for-the-gateway-surface vs N=2-crediting-opencode-antigravity-auth-v67 question + the NO-MINT-Pattern-#18-#8-aggregator alternative.
24. **F24 — LLM-access-tooling surface synthesis.** For the audit: cc-switch v73 (config-switch) / freellmapi v112 (free-tier stack) / CodexPlusPlus v117 (reseller relay) / ai-switcher v153 (multi-account rotate) / opencode-antigravity-auth v67 (OAuth bridge) / CLIProxyAPI v207 (subscription→API gateway) = a coherent LLM-access-tooling cluster worth a taxonomy pass.

---

### Fence (mandatory)
- **DO NOT run against your Claude/Anthropic account** — ToS violation + ban risk + blocked since April 2026.
- If evaluating other providers: scratch/disposable account only + `install-snapshot` + inspect the Docker image + treat stored OAuth tokens as high-value secrets + pin **v7.2.80**.
- hireui uses **official, paid API keys** per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first) — never subscription-OAuth reverse-engineering.
