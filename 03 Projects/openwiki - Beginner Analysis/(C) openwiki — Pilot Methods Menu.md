# (C) openwiki — Pilot Methods Menu (24 methods)

> **Subject:** `langchain-ai/openwiki` — an agent that writes + maintains an agent-readable wiki inside your repo and wires it into `AGENTS.md`/`CLAUDE.md`, refreshed by a daily human-gated CI PR. Built on LangChain's DeepAgents + LangGraph. Default model **GLM 5.2** (cheap); Claude is one of 5 providers.
>
> **Why this one is special for you:** OpenWiki is a *productized, code-scoped version of this vault's own founding pattern* (an LLM that maintains a wiki). So the value splits two ways: **(1)** it doesn't maintain *this* vault (the vault is curated knowledge, not code) — but its **doc-agent system prompt + update-loop discipline are directly borrowable**; **(2)** it *can* run on **hireui** (your real Goal-#2 code monorepo), and better repo docs directly attack the "agents need too much exploration / GitNexus-first context" problem.
>
> **⭐ One-thing path: B5 → C11 → D17.** Lift the doc-agent prompt discipline into a vault skill (zero install) → run OpenWiki on a scratch hireui clone with the cheap GLM 5.2 default and read the output → if the docs are good, install the daily update-PR loop on an `agent-*` branch and let it feed the v189 PR-babysitter you already run.
>
> **Blunt framing:** the highest-ROU move is **B (borrow the prompt/loop patterns, zero install)** — that value is real regardless of whether OpenWiki itself earns a permanent slot. The **install** value (C/D) is real for hireui specifically, behind the fence below.

---

## Fence (read before any install)

- **`install-snapshot` first**, then `npm install -g openwiki` (install is benign — first-party LangChain deps, no postinstall — but snapshot so uninstall is clean). `npm-security-check` is optional here (mainstream deps) but fine to run.
- **Runtime is MODERATE-risk, not the install:** OpenWiki runs a DeepAgents `LocalShellBackend` that can **execute arbitrary shell** in the target repo. `virtualMode` sandboxes filesystem-tool *paths* but **NOT** the shell tool. → **Run on a SCRATCH CLONE first**, never point it at a repo with live secrets, and **review the git diff / PR** it produces (output is always a reviewable diff — that's the safety net).
- **Pin the model** (`OPENWIKI_MODEL_ID`) and start on the **cheap GLM 5.2 default**; only upgrade to `claude-sonnet-5` after you've seen output quality + cost.
- **Don't give it secrets** (the prompt already refuses `.env`, but scope it to a scratch repo anyway).
- **hireui = per its CONSTITUTION:** I-8 (operator installs skills/tools, not the agent), I-2 (`agent-*` branch only), **GitNexus-first**, BMAD harness. hireui has **no LLM spend yet** — this is build-it-right, not a retrofit.
- **Pin the version** `openwiki@0.0.1` (it's v0.0.1, ~3 days old — expect churn).

---

## A — Read & learn (zero install, ~1–3h, zero risk)

**A1 — Read the system prompt as a doc-authoring doctrine.** Open `src/agent/prompt.ts` (in the pinned clone). It's the single best artifact in the repo — a ~130-line "how to write agent-first codebase documentation" manual (grounding / discovery / subagent / planning / git / existing-docs / section-quality / mode-specific disciplines). Read it as a *teaching text*, not code.

**A2 — Read its own dogfooded `openwiki/` docs** (`openwiki/quickstart.md` + `architecture/overview.md`). This is what "good" output looks like: a navigable quickstart, an architecture page that explains **why** + "things to watch when editing," source maps with git-evidence hashes. Use it as a template for *your own* doc structure.

**A3 — Study DeepAgents as a "Claude Code alternative that works with any model."** Read the [DeepAgents overview](https://docs.langchain.com/oss/javascript/deepagents/overview). Understand the four primitives (detailed prompt + `write_todos` planning + virtual-filesystem backends + `task` subagents). This is directly relevant to your multi-agent-orchestration thread — it's a competitor harness to the Claude Agent SDK you use.

**A4 — Map OpenWiki against your own vault pattern.** Write a half-page: what OpenWiki does that the vault's hand-maintenance already does (incremental wiki, cross-links, update-on-change, anti-fabrication), and what's different (code vs curated knowledge; auto vs curated; prose-docs vs your entity/pattern pages). This sharpens *why* the vault stays hand-curated.

---

## B — Borrow patterns into the vault / hireui (zero install, highest ROI)

**B5 ⭐ — Lift the doc-agent system prompt into a vault `05 Skills/` doc-authoring skill.** Adapt `createSystemPrompt()` into a `(C)` skill for "generate agent-first documentation for a code repo" — you already have Claude Code; you don't need OpenWiki installed to *use its prompt*. This is the single highest-ROI, zero-install steal.

**B6 — Steal the content-snapshot no-op guard for your own loops.** OpenWiki hashes the whole `openwiki/` tree before + after a run and only writes metadata / opens a PR **if the hash changed** — the concrete answer to "how do I run an agent on a daily cron without daily noise." Port this into the vault's autopilot / scheduled tasks and into the v189 loop discipline (a "did anything actually change?" gate before a PR).

**B7 — Adopt the surgical-update "soft diff budget."** The `--update` mode rule — *"if fewer than ~5 source files changed, update at most 1–2 pages; no formatting-only edits; may be a no-op"* — is a reusable discipline for any maintenance agent (including the vault's own state-update passes). Add it to the loop-verifier's rubric.

**B8 — Adopt the `AGENTS.md`/`CLAUDE.md` section-template + dual-write rule.** OpenWiki writes a fixed, marker-able "OpenWiki" section into **both** files (because Claude Code reads `CLAUDE.md`, not `AGENTS.md`). Use its exact non-destructive pattern (preserve surrounding hand-written content; refresh only if stale) for any tool that touches your instruction files. (Relevant to your Antigravity/AGENTS.md-portability thread.)

**B9 — Adopt the "explain WHY + change-oriented guidance" doc goals** in your own wiki-writing and in hireui docs: "where to start, what to watch out for, which tests matter when changing this area." That single rule is what separates OpenWiki's output from a file inventory.

**B10 — Borrow the model-tiering-by-task idea.** OpenWiki defaults doc-writing to cheap GLM 5.2 and reserves frontier models for opt-in. Fold this into your `claude-api-cost-optimization` spec: *cheap model for the bulk/mechanical pass, Claude for the judgment pass* — a concrete tiering rule with a real-world example.

---

## C — Low-risk scratch trials (install; ~1–2h; scratch repo only)

**C11 ⭐ — `--init` a scratch clone with the cheap default.** `install-snapshot` → `npm i -g openwiki@0.0.1` → clone a throwaway repo (or a scratch clone of hireui) → `openwiki --init` with the GLM 5.2 default → read the generated `openwiki/`. Judge: is it grounded? navigable? does it explain *why*? **Cost is on you** — note the token spend.

**C12 — Test the surgical `--update`.** After C11, make a small code change + commit, then `openwiki --update`. Confirm it (a) edits only affected pages, (b) respects the soft diff budget, (c) is a **no-op** when nothing relevant changed (the content-snapshot guard). This is the behavior you'd rely on in CI.

**C13 — Provider/cost bake-off.** Run `--init` on the same scratch repo with `--modelId z-ai/glm-5.2` vs `--modelId claude-sonnet-5` (via OpenRouter or native Anthropic). Compare **output quality vs token cost** — a direct data point for your cost thread (is Claude worth the premium for docs, or is GLM 5.2 good enough?).

**C14 — Try the chat Q&A mode.** `openwiki "How does auth work in this repo?"` — the launch post's "Q&A over your docs and codebase." Judge whether it's better than just asking Claude Code directly (it has the maintained wiki as grounding).

**C15 — MEASURE the downstream token delta.** The real question isn't "is the wiki nice" — it's "does having it make my *coding agent* cheaper?" On a scratch hireui clone: run a representative Claude Code task **without** the openwiki docs, then **with** them (+ the `AGENTS.md` pointer), and compare tool-calls / tokens / exploration. Pair with the `ccusage`/OTel observability pilot. **This is the number that justifies (or kills) the install.**

**C16 — Inspect LangSmith tracing (optional).** Set a `LANGSMITH_API_KEY` and trace one run to the "openwiki" project. Useful to *see* how a DeepAgents run decomposes (planning → subagents → writes) — a learning artifact for your multi-agent-orchestration thread.

---

## D — hireui / Goal-#2 (the real payoff; per hireui's CONSTITUTION)

**D17 ⭐ — Generate hireui's agent docs on a scratch clone, operator-installed.** Per I-8 (operator installs) + I-2 (`agent-*` branch): run `openwiki --init` on a **scratch clone** of `/Users/Cvtot/monorepo/hireui` → review the generated `openwiki/` + the `AGENTS.md`/`CLAUDE.md` section → if good, land it on an `agent-*` branch. This directly attacks the "agents need too much repo exploration" problem and complements GitNexus-first.

**D18 — Pair OpenWiki (prose) WITH GitNexus (structure) — orthogonal, not a replacement.** GitNexus gives the agent the *code graph* (who-calls-what); OpenWiki gives it the *prose why* (what this area does, where to start, what to watch). hireui's CONSTITUTION is GitNexus-first; OpenWiki adds the narrative layer on top. Document them as complementary in hireui's `CLAUDE.md`.

**D19 — Install the daily update-PR loop, feeding your v189 PR-babysitter.** Copy `examples/openwiki-update.yml` into hireui's `.github/workflows/` (cheap GLM 5.2, `LANGSMITH` optional). It opens a `docs: update OpenWiki` PR daily — which the **v189 loop pilot you already run** (the D16 PR-babysitter on `pilot/v189-loop-a3-b5`) can triage. Two loops composing: one *writes* the docs, one *reviews* them. Start report-only; graduate per the v189 L1→L2 bar.

**D20 — Use the openwiki docs as the context layer for the Candidate-Detail spike.** The `CandidateDetailScreen.tsx` refactor (drifted tokens + half-migrated r1→r2) is exactly the kind of "future agent needs to understand this area before changing it" problem OpenWiki's change-oriented docs target. Generate docs for that subtree, then run the refactor agent *with* them, and see if it drifts less.

**D21 — Add a hireui `AGENTS.md`↔`CLAUDE.md` sync** using OpenWiki's dual-write pattern (Claude Code reads `CLAUDE.md`; BMAD/other harnesses read `AGENTS.md`). One source, both files, non-destructive — solves the harness-portability half of your Antigravity thread inside hireui.

---

## E — Off-goal / personal (optional)

**E22 — Run it on a personal side-project.** Any repo you own — a no-stakes way to build intuition + get real docs for free (cheap model).

**E23 — Contribute a provider/model PR.** The README explicitly invites PRs for new providers/models (`PROVIDER_CONFIGS` + a `createModel` branch — a ~1-file change). A low-effort way to get your name on an official LangChain repo + learn the DeepAgents provider seam.

---

## F — Vault-meta / pattern-library (follow-ups)

**F24 ⭐ — Write the "four ways to give an agent code context" synthesis.** The corpus now holds four distinct mechanisms for the same job — **graph** (§C#23 code-knowledge-graph: GitNexus/codegraph/codebase-memory-mcp), **vector** (claude-context v40), **lexical** (fff v194), and now **prose docs** (openwiki v195). Write the audit-grade synthesis: when to use which, whether they compose (they do — graph+lexical+prose is the strong stack), and what the vault/hireui should actually run. This is a genuine pattern-library artifact and the natural home for the v195 mint. **Also flag for the overdue ~v192 audit:** the new §C standalone (promotion-eligible at N=2) + a **DeepAgents-as-harness watch axis** (N=1 now; `openshell-deepagent` is a non-corpus sibling → watch for a corpus N=2).

---

### Method index
A1–A4 read+learn · B5–B10 borrow zero-install (⭐B5) · C11–C16 scratch trials (⭐C11) · D17–D21 hireui/Goal-#2 (⭐D17) · E22–E23 off-goal · F24 vault-meta.

**Recommended sequence:** ⭐ **B5 → C11 → C15 → D17 → D19**, with F24 as the pattern-library capstone. Everything in **B** is worth doing today regardless of whether OpenWiki earns a permanent install.
