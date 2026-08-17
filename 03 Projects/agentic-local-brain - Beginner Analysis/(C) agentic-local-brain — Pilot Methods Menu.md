# (C) agentic-local-brain — Pilot Methods Menu

> **v234 · honest menu, not a padded 24.** This is a **read-and-borrow** subject with a **hard install fence**. Most rows below are "read", "borrow", or "don't". Fourteen methods, ranked.

**⭐ The one-thing path: A1 → B5 → D9.**

---

## A · Read & learn (zero install, zero risk)

**⭐ A1 — Read the CLI-as-agent-protocol argument.**
The author's design gist (*"Building a Local-First Knowledge Brain System — Based on Agent + IM + Skill + CLI"*) argues that a CLI, not MCP, is the right agent interface: self-describing (`--help` *is* the prompt), self-contained (one command = one action), no auth/SDK/JSON. ~30 min. Pairs with **pi v228**'s MCP-exclusion pole. This is the sharpest artifact in the whole subject and it costs nothing.

**A2 — Read the graceful-degradation table.**
Four rows, one sentence: *"Documents are always saved… regardless of service availability."* A clean statement of fail-soft ingestion.

**A3 — Read the wiki-compile design.**
Topic clusters → LLM-synthesised article (≤3000 words) + entity cards (≥3 mentions) + wiki-links + staleness + recompile. Read it as a design reference for what an automated version of *this vault* would look like.

**A4 — Read the skill's intent-recognition tree.**
`skills/localbrain-collect/SKILL.md` — a compact worked example of "given arbitrary user phrasing, pick the right tool", including the auth-walled-URL workaround (agent fetches with its own browser → temp file → collect as FILE) and the restraint rule *"DO NOT pass `--tags`/`--summary` by default."*

**A5 — Read the landscape, not the repo.**
Khoj (~34k★), AnythingLLM (~63k★), Quivr, Onyx, PrivateGPT, SurfSense, Reor, LocalRecall. 20 minutes here tells you more about the category than this repo does — and tells you which tool to actually use if you ever want one.

---

## B · Borrow into the vault (zero install, highest ROI)

**⭐⭐ B5 — Steal staleness tracking + auto-recompilation. *The single best idea here.***
Derived artifacts in this vault — the §C registry rows, the `CLAUDE.md` head, Pattern Library entries, the Weekly Update — are compiled from sources that keep changing, and nothing flags them when the sources move. `CLAUDE.md` already lists "check for stale claims" as a maintainer duty, and the registry carries a **stale-flagged C22–C27 backlog with a retire pass deferred for months**. Borrow the mechanism: **give derived artifacts a source fingerprint; flag them stale when the fingerprint changes; recompile on demand.** Zero install — this is a discipline change, not a dependency.

**B6 — Borrow the 3-tier extraction ladder** as a general pattern for any enrichment step: *explicit user input > model > deterministic fallback*, never *nothing*.

**B7 — Borrow the entity-card threshold idea** (promote an entity to its own page once it is mentioned ≥ N times). A cheap, mechanical answer to "when does a thing deserve its own wiki page?" — a question this vault currently answers by taste.

**B8 — Borrow the "one command = one complete action" CLI discipline** for the vault's own scripts, so an agent can drive them from `--help` alone.

---

## C · Hands-on (⚠️ fenced — only if genuinely curious)

**C9 — Source-clone read, no execution.** `git clone` at a pinned commit and read `wiki compile` + the staleness logic. Never run the installer. This is the only "hands-on" step worth taking.

**C10 — Scratch-machine trial (⚠️ discouraged).** If tried at all: source clone at a **pinned commit** → `pip install -e .` in a throwaway venv on a scratch machine → **no email ingestion**, **no DashScope key** (point LiteLLM at a local or OpenAI endpoint) → feed it a handful of public PDFs → run `wiki compile` once to see the output shape → delete. Budget: an hour and nothing you care about.

**🚫 C11 — DO NOT run the published installers.**
```
curl -fsSL http://…/install.sh | sh      ← plaintext HTTP
irm  http://…/install.ps1 | iex          ← plaintext HTTP
```
Unauthenticated RCE by design. And **do not** paste the README's agent-install line (*"Please install or update this knowledge collection skill: http://…/SKILL.md"*) into Claude Code or any agent — that is instructing an autonomous agent to adopt instructions fetched over plaintext HTTP.

---

## D · hireui / Goal #2

**⭐ D9 — The ingestion-vs-evaluation defaults, into the CV-parsing ADR.**
Adopt the 3-tier ladder as the **ingestion-side** default for CV/résumé parsing (user-supplied field > LLM extraction > deterministic parse; **never drop the document**) — and pair it explicitly with **ClawWork v233's fail-closed evaluation gate**. One line in the ADR:

> *Ingestion fails soft — a candidate document is always stored, even if enrichment is unavailable. Evaluation fails closed — no score is produced without a file-backed rubric and a measured threshold.*

Two consecutive corpus subjects, opposite defaults, both correct. On an `agent-*` branch per hireui's CONSTITUTION (I-2 / I-8 / GitNexus-first).

**D10 — The staleness idea for candidate records.** A derived candidate summary should know which source documents produced it and flag itself stale when a new CV arrives. Design note only.

**🚫 D11 — Hard fence: never point this at candidate data.** It ingests email, and by default ships embeddings and RAG calls to DashScope (Alibaba, China). Candidate PII through an unpinned, plaintext-installed, third-party tool is not a defensible path under any reading of hireui's constitution or the EU AI Act posture.

---

## F · Vault-meta

**⭐ F22 — File the deferred broad-class question.** The **v137** entry deferred *"promote-broad-class-vs-split"* on the Pattern #57 Karpathy-productization vector to the "~v139–v140 audit", which never resolved it. v234 is a **4th generate-instance and a structurally new one** (application-with-its-own-store, vs harness-memory v118 / vault-skill v134 / one-shot converter v137). Hand this to the badly-overdue audit.

**F23 — File the CLI-as-agent-protocol watch axis** (v228 + v234, cross-reference only, no N-bump).

---

## Ranking, blunt

1. **A1** — read the gist. Half an hour, best value in the subject.
2. **B5** — steal staleness tracking. The only idea here that changes how the vault works.
3. **D9** — the fail-soft/fail-closed pairing into the hireui ADR.
4. Everything else is optional.
5. **Installing it is not on the list.**
