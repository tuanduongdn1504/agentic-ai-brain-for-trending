# Pi (earendil-works/pi) — v228 Pilot Methods Menu

**Wiki:** v228 REVISIT of v36 · **Date:** 2026-08-08 · Pin `earendil-works/pi@e47b8e3`, npm `@earendil-works/pi-coding-agent@0.84.1`.

**Blunt framing.** Pi is on-goal and directly pilotable, but it is a **competitor coding harness** you'd run *instead of / alongside* Claude Code — so "adopt the product" is the low-value read. The **high-ROI payoff is borrowing four engineering playbooks** (supply-chain hardening, agent containerization, an evals discipline, vendor-neutral telemetry) into the vault + hireui, plus keeping Pi as the operator's **multi-provider escape-hatch**. Most of the value needs **zero install**.

**⭐ One-thing path: B1 → C11 → D16** — lift Pi's supply-chain-hardening playbook into a hireui dependency-security ADR (zero install) → install Pi with `--ignore-scripts` + BYO Claude key + run one real vault task to feel the Claude-Code delta → use Pi's evals discipline + containerization as the dev-environment when you build hireui's first LLM feature (the candidate-LLM legibility ADR's eval-gate), run in a Gondolin/Docker sandbox on an `agent-*` branch.

---

## A — Read + learn (zero risk)
- **A1** Read `docs/usage.md` §"Design Principles" + Mario's *"what if you don't need MCP?"* essay — the minimalism thesis (no MCP / no sub-agents / no plan-mode; "ask pi to build it or install a package"). A design lens for hireui's first LLM feature: **CLI-tools-with-READMEs vs MCP**, **skills vs sub-agents**.
- **A2** Read `SECURITY.md` — the honest "trust boundary = the user, prompt-injection is out-of-scope, containment is your job" model. The clearest agent threat-model statement in the corpus.
- **A3** Read `README.md` §"Permissions & Containerization" + `docs/containerization.md` — Gondolin micro-VM / Docker / OpenShell as three ways to sandbox any coding agent.
- **A4** Skim the client/server spine (`pi-protocol` CBOR + `pi-client` + `pi-server` + `session-backends`) — how a local CLI becomes a remotely-drivable, embeddable runtime (interactive / print-JSON / RPC / SDK).

## B — Borrow, zero-install (HIGHEST ROI)
- **⭐ B1** **Supply-chain-hardening ADR for hireui + the vault.** Port Pi's playbook: pin direct deps exact + `.npmrc save-exact=true` + **`min-release-age=2`** + shrinkwrap the shipped package + `--ignore-scripts` on all installs/CI + a **scheduled `npm audit --omit=dev`** workflow + a **lifecycle-script allowlist**. hireui is a real Node/TS monorepo and this lands squarely on your **api-security thread**. Single highest-value steal.
- **B2** **Containerization pattern → "run an agent against hireui safely" ADR.** Gondolin/Docker/OpenShell as the sandbox for any agent (Pi *or* Claude Code) touching a repo you don't fully trust; composes with the Strix v190 authorized-testing fence.
- **B3** **Evals discipline** (`pi-evals`) → wire an author→run→measure eval gate into hireui's first-LLM-feature spec; satisfies the RATIFIED **candidate-LLM legibility ADR**'s eval/bias-gate-outside-the-prompt requirement (pairs with llm-space v221 + the prompt-eval thread).
- **B4** **Vendor-neutral telemetry contracts** (`pi-telemetry`, typed schemas + conformance tests) → the shape for hireui LLM-feature observability on the CC-observability/OTel thread.
- **B5** **The "no MCP" lens** — before adding an MCP server to hireui/the vault, ask Pi's question: would a CLI-tool-with-a-README + a skill be simpler? (Counter-pole to the vault's MCP-heavy habits; a healthy design check, not a mandate.)

## C — Hands-on, scratch (low risk)
- **⭐ C11** `install-snapshot` → `npm install -g --ignore-scripts @earendil-works/pi-coding-agent` (Pi's own recommended install; prefer this over the `curl | sh` installer) → `export ANTHROPIC_API_KEY=…` → run one real vault/scratch task → compare output + ergonomics with Claude Code. Feel the delta.
- **C12** Multi-provider escape-hatch: `/login` a second provider (or a **local llama.cpp / Ollama** model) → `/model` switch mid-session → confirm you're not vendor-locked. This is the v36 pilot's headline personal value, now broader (~30+ providers).
- **C13** Session ergonomics: `/tree` / `/fork` / `/compact` / `/export` HTML + `/share` (private gist) on a real session — steal the branching/compaction workflow patterns even if you stay on Claude Code.
- **C14** Run Pi **inside Docker/Gondolin** for one task (A3/B2) to see the containerized-agent workflow first-hand.

## D — hireui / Goal-#2 (behind the fence)
- **⭐ D16** Build hireui's **first LLM feature** (Match-Explain / candidate-summariser — the miai-cv-matching thread) with an **eval gate first** (B3) and, if using Pi as the dev-agent, in a **container** (B2), on an `agent-*` branch per hireui's CONSTITUTION (I-2 / I-8 / GitNexus-first). hireui has no LLM spend yet → this is design/spec + a traced+eval'd prototype, not a retrofit.
- **D17** Apply the **B1 supply-chain ADR** to hireui's actual `package.json`/lockfile as a real security PR (pinned deps + `min-release-age` + audit workflow) — a concrete Goal-#2 artifact requiring no LLM spend.
- **D18** Evaluate Pi's **SDK/RPC embedding** only *if* hireui ever needs an embedded, provider-agnostic coding agent (vs vendor lock) — a watch item, not near-term.

## E — Personal / off-goal
- **E21** Donate OSS sessions via `badlogic/pi-share-hf` (HuggingFace) if you do open-source work with Pi — aligns with the vault's "compounding public knowledge" ethos.
- **E22** Local-only coding on `llama.cpp`/Ollama through Pi for data-residency-sensitive work (the "redact local, reason cloud" thread).

## F — Vault-meta
- **⭐ F24** File the v228 revisit record + the **DEFERRED watch axis** ("remotely-drivable open coding-agent runtime + CBOR wire protocol") + the **solo→open-core-company trajectory** observation + the tier reconciliation, all **flagged to the OVERDUE ~v221 audit** (which already owns the coding-agent-products cluster — Pi is its OG member). Note llm-space v221's #57 dependency on `pi-agent-core`.

---

## Fence (mandatory)
`install-snapshot` before any install · **`npm install -g --ignore-scripts`** (Pi's own recommendation; prefer npm over `curl | sh`) · `npm-security-check` the `@earendil-works/*` packages · **BYO Claude key** (never a shared/committed key) · **Pi has NO built-in sandbox** → run it in **Gondolin/Docker** before pointing it at anything sensitive or at hireui · scratch repo before real hireui · it's a **competitor harness** — evaluate vs Claude Code, don't wholesale-switch · pin **v0.84.1** / `e47b8e3` · hireui per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first; no LLM spend yet → build-it-right, not a retrofit).

---

*(C) Claude-generated 2026-08-08 — v228 REVISIT pilot menu. The payoff is the playbooks (B1 supply-chain, B2 containerization, B3 evals, B4 telemetry) + the multi-provider escape-hatch, not adopting the product.*
