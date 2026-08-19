# (C) Unsloth v245 — Pilot Methods Menu

**Standing constraint:** ⚠️ **READ-AND-BORROW.** `pip install unsloth` ships `unsloth_cli` (36/36 files `SPDX-License-Identifier: AGPL-3.0-only`) and `studio.backend` inside a wheel whose metadata declares `license = "Apache-2.0"` (`pyproject.toml:11` vs `:79-81`). Until that is resolved upstream, Unsloth is **not a hireui component** — the v214 firecrawl / v188 OpenMontage / v243 ToolJet precedent. **Every method below except M6 requires installing nothing.**

Ordered by value-per-unit-risk, best first.

---

## M1 — Strip the frontier credential before pointing an agent anywhere else ⭐ ZERO INSTALL · ZERO RISK

**What Unsloth does** (`unsloth_cli/commands/start.py:146`):

```python
_CLAUDE_ENV_UNSET = ("ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN")
_CODEX_ENV_UNSET  = ("OPENAI_API_KEY", "CODEX_API_KEY", "CODEX_ACCESS_TOKEN")
```

Before launching Claude Code against a non-Anthropic endpoint, it **removes** the real Anthropic credential from the child environment.

**Why it matters here.** Every other gateway-class subject in this corpus went the other way — v207 CLIProxyAPI re-exposed CLI-tool OAuth subscriptions, v208 ported it, v231/v232 drove logged-in consumer sessions. This is the first subject that treats your vendor credential as blast radius to shrink.

**Do it:** any wrapper script or alias that sets `ANTHROPIC_BASE_URL` must also `unset ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN`. Two lines. It closes (a) silent fall-through billing to Anthropic and (b) handing your real key to a third-party endpoint.

**Cost:** one edit. **Risk:** none. **Do this first.**

---

## M2 — Measure the vault's own prompt, then use the flag that actually shrinks it ⭐ ZERO INSTALL · ZERO RISK

**The finding** (`.github/scripts/agent-guides-drive.sh:~186-204`), measured by people paying CPU prefill for every token:

> measured via `claude -p /context`, the **default prompt is ~28k tokens of which ~18k is "System tools" alone**. `--allowedTools`/`--disallowedTools` only gate PERMISSION … **`--tools` is the flag that restricts which schemas are sent.** (The ~8k "Memory files" chunk is auto-loaded `CLAUDE.md`.)

**Verified against Anthropic's docs (2026-08-19):** `--allowedTools` is documented as *"Tools that execute without prompting… To restrict which tools are available, use `--tools` instead."* Their central claim holds. ⚠️ One clause of theirs is now inaccurate: a **bare** name in `--disallowedTools` *does* remove the tool from context per current docs.

**Why this is the vault's own open question.** The standing note says the **~54K tool catalog is the subagent-context floor**, and v238's entire thesis is that the first request's tool schema conditions the model's reasoning — with the recommendation to *"trial `defer_loading` and MEASURE it."* This supplies the instrument.

**Do it:**
1. `claude -p /context` in the vault root — record the split (system / tools / memory files). The `~8k` memory-files figure is *this vault's* `CLAUDE.md`, which is the number the shim-size discipline has been guessing at for 80 ships.
2. Re-run with `--tools "Bash,Read,Edit,Write,Grep"` and diff.
3. Compare against trimming connected MCP servers — the two levers are additive.

**Cost:** two commands. **Risk:** none (read-only measurement). **Payoff:** the first real measurement of the vault's own prompt budget.

---

## M3 — Apply D32 to `_state/03c-projects-v61-v183.md` ⭐ ZERO INSTALL · ONE EDIT

**The mechanism** (`.github/scripts/kaggle_t4_ci/BUDGET.md`, ¶2):

> **The workflow header is the source of truth.** … **If the two ever disagree, the workflow is right and this file is stale; fix this file.**

**⇒ D32: when two documents must carry the same fact and mechanisation is impractical, declare which copy wins — inside the copy that loses.**

**The vault's instance.** `_state/03c-projects-v61-v183.md` has held entries through v245 for **sixty-two versions**. v239, v240, v242 and v243 each diagnosed exactly this defect. The prescribed fix (rename + reference sweep) has never been run, because it is a multi-file change and every ship has had something more urgent.

**D32 says the cheap fix is not a compromise.** Add one line at the top of the file:

```markdown
> **Source of truth:** the entries below are authoritative. The version range in this
> file's NAME is stale (it reads `-v183`; entries run through v245). The chapter index
> in `CLAUDE.md` is correct. If the filename and this notice disagree, this notice wins.
> Rename still pending — see the v239/v240/v242/v243 doc-integrity findings.
```

**Cost:** one edit. **Risk:** none. **Effect:** a reader who trips over the filename is instructed rather than misled — today, without waiting for the rename.

---

## M4 — Steal `studio/frontend/.npmrc`, and steal the habit more than the file ⭐ ZERO INSTALL

Contents worth copying: `min-release-age=7` (pi v228 had 2 → **N=2** on this technique), `save-exact=true`, `registry=` pinned, `audit-level=high`, and *"use `npm ci` (never `npm install`)"*. **Zero npm lifecycle scripts** across all three `package.json` files.

**But the transferable thing is the commenting discipline.** The file documents:
- the **threat** it defends against — *"Mini Shai-Hulud / Axios-style … closing the typical 4-72h attack window between malicious publish and upstream removal"*
- a **parsing footgun** — *"npm interprets the bare integer as DAYS; do not append `d`, npm 11.x will parse `7d` as a Date string and abort"*
- **the defeat condition of its own control** — *"this does NOT block an ambient `NPM_CONFIG_REGISTRY` env var … **That is exactly why Unsloth does not read `NPM_CONFIG_REGISTRY`** and instead exposes one deliberate, explicit opt-in"*

⭐ **The best security comment states what its control does not cover.** Adopt that as a rule for the vault's own skill and hook files: every guard documents its bypass.

**Cost:** one file copied into hireui's frontend + a `CLAUDE.md` line. **Risk:** none (`min-release-age` can delay an urgent upgrade — that is the intended trade).

---

## M5 — Make `verify-vault-docs` a generator, not a linter ⭐ THE STRUCTURAL ONE

**The mechanism** (`.github/scripts/agent-guides-drive.sh` header):

> **Self-updating:** for all six agents … we obtain the exact env + command from **`unsloth start <agent> --no-launch`** and run **THAT**, so a recipe change is exercised automatically.

Eleven ships have handed this vault a piece of `verify-vault-docs`: v239 the linter, v240 prose-vs-code + the inventory rule, v241 D22, v242 D23, v243 the symlink, v244 the third symlink + D29, **v245 this**. Every prior piece either *prevents* duplication (symlink, generator) or *detects* it (linter). This one **removes the prose from the loop**: the documented recipe is a command's output, so there is nothing to lint.

**The vault version.** Wherever a routine or skill documents a command sequence, invert it: have the code print the sequence (`--dry-run` / `--no-launch`), put *that output* in the doc, and add a check that runs it. Concretely — `bin/autopilot-drain.py` already has the A1 anchor-validation gate shipped; extend the same shape to the ship procedure rather than writing prose about it.

**⚠️ And take the limit with the mechanism.** Unsloth's docs live off-repo at `unsloth.ai/docs`; only 27 `.md` files are in tree. Their CI validates the *command* the website documents without ever reading the website. **A doc check reaches only the docs in the repository.** For this vault that is good news — the docs *are* the repository — but it is the reason their answer is a generator rather than a linter, and the reason ours can be either.

**Cost:** a design session, then real work. **Risk:** none. **This is the one that compounds.**

---

## M6 — A fenced local-model spike (the only method that installs anything) ⚠️ OPTIONAL · MEDIUM FOOTPRINT

**Only if** there is a concrete reason to want a local model in the loop. There currently isn't one for hireui — the RATIFIED candidate-LLM-legibility ADR requires a fixed, legible, audited, human-in-the-loop, eval-gated path, and a locally-fine-tuned GGUF is the *opposite* of legible.

**If run anyway, the fence:**
- ⭐ Run `/install-snapshot` **before** anything (the installers are ~40,901 lines across 12 files; `install.sh` alone is 5,732; `studio/setup.ps1` 6,867 — they download prebuilt llama.cpp/node/whisper/sd-cpp binaries and write outside their install dir).
- Pin a tag. All 79 tags are `v0.1.NNN-beta`; **there has never been a non-beta release.** Latest `v0.1.800-beta`.
- **Scratch machine or scratch user account.** Not the vault host, not anywhere near candidate data.
- Keep the default bind `127.0.0.1` (`unsloth_cli/commands/studio.py:1709`). If remote access is needed, use `--secure` — it *forces* loopback and publishes only the authenticated Cloudflare tunnel (`studio/backend/run.py:2258-2266`). **Never** `-H 0.0.0.0` without it: the CORS default is `["*"]` (`utils/host_policy.py:50-56`).
- MCP stays off unless wanted: it needs `UNSLOTH_STUDIO_ENABLE_MCP=1` **and** a `UNSLOTH_STUDIO_MCP_TOKEN`. Remember what it grants — `start_training`, `stop_training`, `load_checkpoint`, **`export_gguf`**.
- 🔴 **Do not meter it with `cache_read_input_tokens`.** On the Anthropic `/v1/messages` path Studio never sets that field (`assert-prompt-cache.sh:15-28` documents this against `inference.py:8787-8790`), so it reads **0 on every request regardless of the truth**. The OpenAI `/v1/chat/completions` path does forward it. The vault's ccusage→OTel cost thread depends on that field.
- Apply **M1** — the credential unset — which `unsloth start` does for you, but verify it.

**Highest-value single experiment if you do run it:** `unsloth start claude --as-subagent` and delegate *read-only reconnaissance* (plan-mode variant, `unsloth_plan_agent`) to a local model while Opus does the reasoning. That is the §3 inversion tested at its cheapest and most defensible point: cheap local grep-and-summarise, expensive remote judgement.

**Cost:** hours + disk + a GPU or patience. **Risk:** medium (large installer footprint, beta-only releases). **Not recommended now.**

---

## Explicitly do NOT

- 🔴 Install into any hireui environment (§6 licence ambiguity).
- 🔴 Point Studio, or any local model served by it, at candidate data — the RATIFIED candidate-LLM-legibility ADR.
- 🔴 Repeat *"~90% slower"* as an Anthropic-API figure, or tell anyone `CLAUDE_CODE_ATTRIBUTION_HEADER=0` will cut their Anthropic bill. The documented scope is `ANTHROPIC_BASE_URL` — third-party, proxied and local endpoints. First-party effect is **NOT VERIFIED**.
- 🔴 Report AI-tool usage in this repo from a commit-body grep: `codex` 390 / `gemini` 546 / `openai` 829 are **file paths and feature names**. Real non-Claude trailers: `Made-with: Cursor` = **1**.

---

## ⭐ Recommended route: **M1 → M2 → M3** in one sitting (≈30 minutes, three edits, zero installs), then **M5** as the next real piece of work.

M1 hardens every future agent-routing experiment. M2 finally measures the prompt budget the vault has been reasoning about since v167. M3 closes a defect four ships have diagnosed and none has fixed. M5 is the structural payoff.

---

*Prepared by Claude Opus 5 for Storm Bear, 2026-08-19, from a twice-cloned source tree at `cabed07f`. Companion to `(C) Unsloth v245 — Deep Dive.md` and `(C) Unsloth v245 — Verdict.md`.*
