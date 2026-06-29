# Pilot methods — applying Graphify (codebase knowledge graphs) to your working flows

> **Source:** [[graphify-codebase-graph/_index]] — AI Stack Engineer "OpenCode + Graphify: Stop Wasting Tokens" ([-L_faOE-H5g](https://www.youtube.com/watch?v=-L_faOE-H5g)) + deep-dives of the originals (the [Graphify repo](https://github.com/safishamsi/graphify), [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [OpenCode](https://github.com/sst/opencode), [lucasrosati Obsidian+Graphify](https://github.com/lucasrosati/claude-code-memory-setup)). Adversarially verified (Workflow `wf_2f2a5052-7ac`). Verification log: [[graphify-codebase-graph/source-provenance]].
> **Date:** 2026-06-20.
> **Your working flows (from vault + memory):** (A) the **autopilot-research vault** — an Obsidian LLM Wiki (L5); (B) the **Storm Bear curated vault** (62-wiki corpus + Pattern Library); (C) **hireui** — TalentAxis recruitment SaaS monorepo, your **Goal #2** build target (no LLM yet; strict I-2/I-8 CONSTITUTION); (D) your **Claude Code / OpenCode harness**; (E) **cost / local-inference** discipline; (F) **Scrum coaching**.
> **16 methods, ranked.** Each is grounded in a verified finding, with a concrete first step + a success signal.
>
> **The headline:** Graphify is an **automated version of the exact LLM-Wiki pattern your whole vault runs on.** So its value to *you* splits by surface: on **code** (hireui, harness) it's a **token-cutter** (realistically 2-8×, not 71.5×); on your **knowledge vaults** it's a **structural-map + connection-discovery scout** that feeds your hand-curation. Don't apply the token pitch to the vault or the scout pitch to a code monorepo — match the value prop to the surface.

---

## ▶ Start here (recommended sequence)

1. **This week, lowest friction (~15 min, $0):** **A1** — run `graphify . --wiki` on a **copy** of the autopilot-research `wiki/` folder and just *look* at `graph.html` + `GRAPH_REPORT.md`. You'll see an automated structural map of your own 24-topic knowledge base — god nodes, communities, "surprising connections." This is the cheapest way to feel what the tool does, on content you know cold. (Code-free corpus → only Pass 3 costs anything; skip it or use a local model for $0.)
2. **The real test (the only way to know your multiplier):** **D9 → D10** — install Graphify into your Claude Code/OpenCode harness on **one real code project**, turn on `graphify hook install`, and **benchmark token usage over a week via the Anthropic dashboard** (the [[graphify-codebase-graph/token-savings-reality]] protocol). Expect 2-8×, not 71.5×.
3. **The compounding habit:** **A2** — use the graph's "surprising cross-community connections" as **candidate `[[wiki links]]`** your librarian verifies and adds. The graph scouts; you curate. This is the productive marriage of Graphify and your hand-built vault.

---

## Ranked table

| # | Method | Flow | Effort | Value | Why it ranks here |
|---|---|---|---|---|---|
| **A1** | Graph your own autopilot vault & inspect it | A vault | **Low** (~15m) | **High** | Cheapest way to see the tool work, on content you know; $0 |
| **D9** | Install + "always-on" in OpenCode/Claude Code on 1 real repo | D harness | Med | **High** | The end-to-end pilot; everything else is downstream of this |
| **D10** | Benchmark tokens before/after over a week (dashboard) | D harness | Med | **Very High** | The ONLY way to learn your real multiplier; kills the 71.5× myth |
| **A2** | Auto-graph as a *feeder* into curated `[[links]]` | A vault | Low–Med | **High** | The Graphify×LLM-Wiki marriage; graph scouts, you curate |
| **E13** | $0 + private Pass-3 via local Ollama | E cost | Low–Med | **High** | Makes the only paid pass free + data-sovereign; unlocks C |
| **C7** | Graph hireui as a dev-time *architecture map* | C hireui | Low | **High** | Value without cloud LLM or governance risk; helps you navigate the monorepo |
| **B4** | Graph the Storm Bear vault to lint structure | B vault | Med | Med–High | Surfaces orphans / missing cross-refs structurally (the "lint" directive) |
| **A3** | `graphify query` as a fast librarian assistant | A vault | Low | Med–High | Terminal answers w/ source refs, no full session |
| **D11** | `query`/`path`/`explain` in your terminal flow | D harness | Low | Med | Quick architecture answers; "load less, at the right time" |
| **C6** | hireui token-cut pilot — **sandbox-only**, governed | C hireui | Med | Med | Real Goal-#2 evidence, but only safely on a throwaway branch |
| **D12** | Verify the hook actually fires | D harness | Low | Med | Open issues report silent non-firing; don't assume "always-on" |
| **E14** | Slot Graphify into your cost-lever stack | E cost | Low | Med | Compare ROI vs caching / PTC / compaction |
| **B5** | Graph-driven Pattern-Library connection discovery | B vault | Med | Med | Auto-surface cross-wiki structural links as evidence candidates |
| **F15** | Graph as a shared team architecture map | F coaching | Low | Med | "God nodes" = high-coupling modules worth a refactor convo |
| **C8** | Keep the "dev-tool, not product-feature" distinction | C hireui | Low (framing) | Med | hireui has no LLM; Graphify here helps *you*, not the product |
| **F16** | "Build the wiki once" as a doc Definition-of-Done | F coaching | Low | Low–Med | Makes doc-debt visible (orphan / undocumented god nodes) |

---

## A — autopilot-research vault (your Obsidian LLM Wiki)

> Your vault **is** Level 5 (Karpathy LLM Wiki). Graphify is the **automated** version of that pattern — so here it's a **structural-map / connection-discovery scout**, *not* a token-cutter (a markdown vault isn't token-bound the way a code monorepo is). See [[graphify-codebase-graph/karpathy-llm-wiki-lineage]].

### A1 — Graph your own vault & inspect it ⭐
- **Grounding:** Graphify is multimodal — "point it at a folder of research papers, PDFs, meeting notes, screenshots" — your `wiki/` is exactly that kind of mixed-markdown corpus.
- **Apply:** build a graph of the autopilot-research wiki and look at what god-nodes/communities it auto-detects vs your hand-written `_master-index.md`.
- **First step:** `cp -r wiki /tmp/vault-graph-test && cd /tmp/vault-graph-test && uv tool install graphifyy && graphify . --wiki` → open `graphify-out/graph.html` + read `GRAPH_REPORT.md`. (Run on a **copy** so nothing touches the real vault.)
- **Success signal:** the report names ≥1 cross-topic connection you hadn't explicitly linked, or confirms your `_master-index` structure matches the auto-detected communities.

### A2 — Auto-graph as a *feeder* into curated links ⭐
- **Grounding:** the graph's "surprising cross-community connections" (in `GRAPH_REPORT.md`) are exactly the `[[wiki links]]` your librarian discipline asks you to maintain — found automatically.
- **Apply:** treat the report as a **candidate-link list**: the librarian reviews each, verifies it's real, and adds it as a curated `[[link]]`. Graph scouts; you curate (the marriage in [[graphify-codebase-graph/karpathy-llm-wiki-lineage]]).
- **First step:** from A1's report, pick the top 3 "surprising connections," verify them by hand, and add any genuine ones to the relevant `_index.md`.
- **Success signal:** ≥1 real cross-link enters the curated wiki that you'd otherwise have missed.

### A3 — `graphify query` as a fast librarian assistant
- **Grounding:** `graphify query "..."` traverses the graph and answers **with source-file references**, no agent session needed.
- **Apply:** a quick "what relates to X across my topics?" lookup — complements (doesn't replace) the routine's `query:` verb.
- **First step:** after A1, run `graphify query "what connects cost-optimization, memory systems, and harness engineering?"` and check the source refs.
- **Success signal:** you get a usable, cited answer faster than opening a session and reading `_master-index`.

---

## B — Storm Bear curated vault (62-wiki corpus + Pattern Library)

> Same scout framing, bigger corpus. ⚠️ **Scope clamp:** the autopilot routine may not write outside `03 Projects/autopilot-research/`. Run these as **interactive, operator-driven** experiments on a **copy** of the curated vault — never as an autopilot write.

### B4 — Graph the curated vault to lint structure
- **Grounding:** your prime directive includes "lint the wiki — check for orphan pages, missing cross-references, data gaps." A graph makes these **structurally visible** (isolated nodes = orphans; sparse god-node neighborhoods = under-linked hubs).
- **Apply:** graph a copy of the curated vault; use isolated/low-degree nodes as an orphan-page list and god nodes as "are these adequately cross-referenced?" candidates.
- **First step:** `graphify .` on a copy of the curated `wiki/` (or the `_patterns/` chapters); scan `graph.html` for disconnected nodes.
- **Success signal:** the graph flags ≥1 orphan/under-linked page your last manual audit missed.

### B5 — Graph-driven Pattern-Library connection discovery
- **Grounding:** Pattern Library = cross-wiki synthesis (finding the same structural pattern across N wikis). Graphify auto-detects cross-community edges — a candidate detector for "this pattern shows up in wikis X, Y, Z."
- **Apply:** use auto-detected cross-wiki connections as **N-counting evidence candidates** to bring to the next mini-audit (you decide if they're real patterns).
- **First step:** in B4's graph, look for nodes that bridge multiple communities; cross-check against existing Pattern Library entries.
- **Success signal:** the graph surfaces ≥1 cross-wiki structural link worth recording as candidate evidence.

---

## C — hireui (Goal #2) — with the security caveats up front

> ⚠️ **Do NOT install Graphify on hireui's main/production tree.** Verification verdict: typosquat → `.env.local` secret exposure, Pass-3 → candidate-data/GDPR exposure, auto-skill-injection → **I-8 governance violation**, git hooks → I-2/BMAD friction, and **no business urgency (hireui has no LLM)**. Full reasoning: [[graphify-codebase-graph/security-and-install-safety]]. The methods below are the *safe* ways to still get value.

### C7 — Graph hireui as a dev-time architecture map ⭐
- **Grounding:** Pass 1 (tree-sitter) is **local, free, and code-only** → no cloud, no Pass-3 data exfiltration, no API key needed.
- **Apply:** build a **code-only** graph of the hireui monorepo (5 services + 2 shared packages) as an **architecture map for *you*** navigating it — independent of any token-savings claim. `god nodes` name the high-coupling modules.
- **First step:** on a local clone, with a `.graphifyignore` excluding `.env*` + any candidate-data dirs, run `graphify . --mode deep --svg` and open the graph. **Code-only = $0, nothing leaves your machine.**
- **Success signal:** the graph gives you a faster mental model of hireui's service boundaries than reading the repo cold.

### C6 — hireui token-cut pilot — sandbox-only, governed
- **Grounding:** this would be real **Goal-#2 build-it-right evidence** (does a knowledge graph cut Claude Code's tokens when working in *your* monorepo?), but only safely sandboxed.
- **Apply:** clone hireui to a throwaway; `.graphifyignore` secrets + candidate data; run **Pass 3 against local Ollama** (E13) so nothing leaves the machine; benchmark Claude Code token usage on a real navigation task per [[graphify-codebase-graph/token-savings-reality]].
- **First step:** spin up the sandbox, build the graph (local model), and run D10's before/after on one representative task.
- **Success signal:** a measured multiplier on *your actual repo* (expect 2-8×) — a concrete data point for whether to ever propose it as a governed hireui skill.

### C8 — Keep the "dev-tool, not product-feature" distinction
- **Grounding:** hireui has **zero Claude API usage in product code** (verified 2026-06-15). Graphify here helps *you/Claude Code navigate the repo at dev time* — it is **not** a product memory feature.
- **Apply:** don't let the "memory system" framing (lucasrosati's Obsidian+Graphify) leak into a hireui product spec. If hireui *later* gets an LLM feature, that's the cost-optimization spec already written — separate concern.
- **First step:** none — just hold the line in any hireui planning doc.
- **Success signal:** no hireui runbook conflates Graphify-as-dev-tool with an LLM product feature.

---

## D — Claude Code / OpenCode harness

### D9 — Install + "always-on" on one real repo ⭐
- **Grounding:** `graphify install` (Claude Code default) or `graphify install --platform opencode` + `graphify opencode install` (AGENTS.md + `tool.execute.before` plugin) makes the graph load every session without you typing anything ([[graphify-codebase-graph/opencode-integration]]).
- **Apply:** pick one stable, mid-to-large repo; do the full ritual end-to-end.
- **First step:** `uv tool install graphifyy` → `graphify install --platform opencode` (or default for Claude Code) → `/graphify .` → `graphify hook install`.
- **Success signal:** a fresh session answers an architecture question by reading the graph report first (you see the injected reminder) instead of grepping files.

### D10 — Benchmark tokens before/after over a week ⭐
- **Grounding:** the 71.5× is a cherry-picked 52-file mixed-media best case; independent tests show 7.3× / ~7-8% ([[graphify-codebase-graph/token-savings-reality]]).
- **Apply:** run the real protocol — baseline a typical query (dashboard tokens), build the graph, re-run, repeat 10+ times over a week, compare totals **including build cost**.
- **First step:** note today's Anthropic dashboard token total; run your normal workflow on the D9 repo for a week with the graph on; compare.
- **Success signal:** you have a *measured* multiplier for your repo — and a fact-based keep/drop decision.

### D11 — `query`/`path`/`explain` in your terminal flow
- **Grounding:** these answer from the graph without a full session — pairs with your [[harness-engineering/_index]] "load less, at the right time" thesis.
- **Apply:** reach for `graphify path "A" "B"` / `graphify explain "X"` for quick orientation before opening a session.
- **First step:** add the three commands to your shell notes; use them once on the D9 repo.
- **Success signal:** you answer an orientation question without burning a session's context.

### D12 — Verify the hook actually fires
- **Grounding:** community issues report `tool.execute.before` **not firing** and Graphify plugins **not appearing** (#356, #755, rtk-ai #1706).
- **Apply:** don't trust "always-on" — confirm the injected reminder shows before relying on it.
- **First step:** after D9, start a session, trigger a bash call, and check the graph reminder appears; if not, re-run the platform install + inspect `.opencode/plugins/`.
- **Success signal:** confirmed reminder injection (or a logged "it didn't fire, here's the fallback").

---

## E — cost / local-inference

### E13 — $0 + private Pass-3 via local Ollama ⭐
- **Grounding:** Pass 3 sends content to *your* provider via *your* key; point it at a **local Ollama** model and the only paid pass becomes **free** *and* nothing leaves your machine — directly composing with [[cowork-third-party-inference/_index]].
- **Apply:** configure Graphify's backend to a local model for extraction + queries — the enabling move for C6 (hireui sandbox) and any sensitive corpus.
- **First step:** point Graphify's model config at your Ollama endpoint; rebuild a small graph; confirm no API spend on the dashboard.
- **Success signal:** a graph built with $0 cloud cost and zero data leaving the machine.

### E14 — Slot Graphify into your cost-lever stack
- **Grounding:** Graphify is a **context-engineering** lever (load a compact graph, not raw files) — same family as caching / programmatic tool calling / compaction ([[claude-api-cost-optimization/_index]]).
- **Apply:** compare its real ROI (from D10) against those levers; it's complementary, not a replacement (caching helps *every* call; Graphify helps *retrieval* on large repos).
- **First step:** add a row to your cost-optimization notes: "Graphify — context-eng lever, measured Nx on repo Y, payback ~Z days."
- **Success signal:** a clear-eyed place for Graphify in your cost toolkit, ranked by measured ROI.

---

## F — Scrum coaching / team practice

### F15 — Graph as a shared team architecture map
- **Grounding:** the `graph.html` star-map + `GRAPH_REPORT.md` is a living onboarding artifact; **god nodes** name the high-coupling modules everything touches.
- **Apply:** use it as a teaching frame — a new dev gets the graph instead of a stale wiki; "god nodes" become the agenda for a refactor/decoupling conversation.
- **First step:** in a working-agreements or onboarding session, show a graph of a shared repo and ask "is this coupling intentional?"
- **Success signal:** the team identifies one high-coupling module worth a deliberate decision.

### F16 — "Build the wiki once" as a documentation Definition-of-Done
- **Grounding:** Karpathy's "build the wiki once, maintenance cost near zero" + Graphify making doc-debt structurally visible (orphan modules, undocumented god nodes).
- **Apply:** a coaching lesson — documentation isn't prose nobody reads; it's a *queryable map* whose gaps are visible. Orphan/undocumented god nodes = doc-debt backlog items.
- **First step:** frame one retro around "what would our graph's orphans tell us about our docs?"
- **Success signal:** the team turns ≥1 structural gap into a concrete doc-debt backlog item.

---

## ⛔ Skip-list (don't do these)

- **Don't run it on tiny repos (<10 files)** — the video's own advice: "the graph value is structural for small stuff, not token savings."
- **Don't believe 71.5×** — it's a cherry-picked benchmark. Benchmark your own repo (D10). Plan for 2-8×.
- **Don't install on hireui's main/production branch** — typosquat + GDPR + I-8 governance + no LLM there. Sandbox only (C6/C7).
- **Don't type `pip install graphify` (single-y) from memory** — that's the unclaimed typosquat name. Use `uv tool install graphifyy` / `pipx install graphifyy`.
- **Don't expect it to replace curated synthesis** — it's a structural scout, not a cartographer. Your librarian still writes the prose.
- **Don't auto-graph *into* your curated `wiki/` folder** — keep generated graph/chat notes in a separate dir (`graphify/`) so they don't pollute curated content (the lucasrosati gotcha).

## 🔁 Critic reframe (the strongest skeptical take)

> *The token-savings pitch is aimed at code monorepos, and even there it's a measured 2-8×, not 71.5×, with a months-long payback. Your **vaults aren't token-bound** the way a churning code monorepo is — so on A/B the real value isn't tokens at all, it's **connection-discovery + structural linting** (a scout that feeds your hand-curation). On C/D it **is** a token-cutter, but a modest one you must measure. So the honest move is: **match the value prop to the surface** (scout for vaults, measured token-cutter for code), **prove it with D10 before adopting**, and **never let the 71.5× marketing set your expectations.*** The most defensible single pilot is **A1 + A2** (free, on content you own, immediate insight) followed by **D9 + D10** (the one real token benchmark).

## Cross-links

- [[graphify-codebase-graph/_index]] (source topic) · [[graphify-codebase-graph/token-savings-reality]] (the 71.5× truth) · [[graphify-codebase-graph/security-and-install-safety]] (the go/no-go) · [[graphify-codebase-graph/karpathy-llm-wiki-lineage]] (the vault connection) · [[graphify-codebase-graph/source-provenance]] (verified vs flagged).
- Sibling pilots this composes with: [[claude-code-memory-systems/_index]] (Graphify = automated L3/L5; your setup mapping) · [[claude-api-cost-optimization/_index]] (E14's cost stack) · [[cowork-third-party-inference/_index]] (E13's $0 local Pass-3) · [[claude-code-clones/_index]] (OpenCode) · [[harness-engineering/_index]] (load-less thesis) · [[claude-skills/_index]] (Graphify installs as a skill).

## Suggested next action

Do **A1 this week** (~15 min, $0): `graphify . --wiki` on a **copy** of the autopilot-research `wiki/` and read `GRAPH_REPORT.md` — you'll instantly see whether an automated map of your own knowledge base surfaces connections worth curating (A2). Then, when you want the one real token number, open the **D9 → D10** harness pilot on a single stable repo and measure it over a week. Tell me which and I'll scaffold it — the A1 copy-and-graph command sequence, or the D9/D10 install + benchmark checklist (with the local-Ollama E13 option wired in so Pass-3 is free and private).
