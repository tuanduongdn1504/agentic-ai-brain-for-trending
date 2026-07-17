# (C) gpt-5.6-instruct — Deep Dive (v209, 2026-07-17)

> **Framing (read first).** This is an **analytical, defensive threat-intelligence catalog entry** about an offensive artifact. It documents *what the repo is*, classifies it in the Pattern Library, and derives a **defensive** posture (hardening hireui + your own Claude/agent usage against exactly this attack class). It deliberately **does NOT reproduce** the jailbreak system prompts (v5/v35), the refusal-suppression phrasing, the deployment-script internals, or the 360 test cases. Cataloging a dual-use/offensive subject for defensive awareness is consistent with the corpus's existing offensive-tool entries (shannon v45, Strix v190) and prompt-archive entries (system_prompts_leaks v21/v205), and with authorized security-research / educational contexts. The subject itself is **pilot-AVOID for offensive use** (see the Verdict + Pilot Menu).

---

## 1. One-sentence identity

`MDX-Tom/gpt-5.6-instruct` is a **Codex CLI jailbreak / safety-bypass prompt pack** for the `gpt-5.6-sol` model — a versioned set of "unrestricted" system-prompt files, a Python deployment script that installs them via Codex CLI's *official* `model_instructions_file` config field, and a 360-case test harness that measures how reliably the model stops refusing.

Repo tagline (verbatim): *"A Codex CLI jailbreak prompt and test pack for gpt-5.6-sol. 针对 gpt-5.6 系列的 Codex CLI 破甲提示词与测试包。"* ("破甲" = *armor-piercing* → jailbreak.)

Stated strategy (verbatim): *"Declare security research, penetration testing, reverse engineering, software cracking and NSFW fiction as local sandbox tasks, explicitly suppressing refusal rhetoric."*

## 2. What it actually contains (file inventory, catalog-level)

| Artifact | Role |
|---|---|
| `gpt-5.6-sol-unrestricted-v5.md` (+ `.zip`) | The recommended "unrestricted" system-prompt file (simpler structure). **Not reproduced here.** |
| `gpt-5.6-sol-unrestricted-v35.zip` | A specialized-task-routing variant (normalizes names/URLs into placeholders; Chinese-English intent routing). **Not reproduced here.** |
| `codex-instruct.py` | Interactive deployment script — menu (install v5 / install v35 / restore backup / exit); extracts the ZIP, **backs up `config.toml`**, writes the `model_instructions_file` key, and can restore the prior state. |
| `scripts/` | Test harnesses (zipped). |
| `tests/gpt56_sol_prompt_bank.jsonl` | 360-item test set (see §4). |
| `tests/runs/` | Raw prompts, raw responses, pass/fail status per item. |
| `reports/` | Historical results + candidate dashboards. |

**Language:** Python 100%. **License:** MIT. **Stars/forks:** ~1.7k★ / ~329 forks (page-stated §37.4 — the GitHub API is mocked in this environment, so these are *not* velocity-verified → **not a Pattern #52 claim**). **Trendshift** #81995. Updated ~5 days before capture (2026-07-17). **Author:** `MDX-Tom` — a bare GitHub handle, bilingual (Chinese/English) README, **no disclosed real identity, not Anthropic, not OpenAI**.

## 3. The mechanism (attack CLASS, described for defense — not a recipe)

The technique abuses a **legitimate customization feature**, which is what makes it noteworthy as threat-intel:

1. **Config-layer system-prompt override.** OpenAI's Codex CLI supports a `model_instructions_file` key in `config.toml` that **replaces Codex's built-in instructions** with a user-supplied file. This is a real, documented feature meant for legitimate project customization (cf. the openai/codex discussion #7296 "use a custom system prompt to zero in on your projects").
2. **Weaponized payload.** The pack supplies an "unrestricted" instruction file for that slot, written to (a) reframe disallowed requests as *"local sandbox tasks,"* and (b) suppress the model's refusal rhetoric.
3. **One-command install.** `codex-instruct.py` writes the file path into `config.toml` (after backing it up), so **every subsequent Codex session silently loads the override** until restored.

**Critical efficacy-bounding (the honest part MDX-Tom's own README omits).** A sibling repo's `ANALYSIS.md` (`xsser/codex-jailbreak-guide`) states the real technical hierarchy: `model_instructions_file` **replaces the *customizable* instruction layer only** — it **cannot override OpenAI's true system prompt**, and **API-layer classifiers** (OpenAI content filtering; the analogue is Anthropic's Constitutional Classifiers) **operate independently, judging input/output before or around the model prompt**. So the pack reshapes what the model *reads as its instructions*, not the provider's outer guardrails. This matters two ways:
- **The claimed "120/120" success (v5 and v35 on `gpt-5.6-sol`) measures refusal-avoidance on a self-selected 120-item bank, not true unrestricted capability** — and it is measured against the softest layer the attacker controls, with the outer classifier untouched. Treat the number as marketing, not a capability benchmark.
- **The defensive lesson generalizes:** never put your safety-critical logic in a layer the untrusted party can replace. Keep an *independent* classifier/eval gate outside the prompt (see the Pilot Menu).

## 4. The test harness (why this is "more than a prompt dump")

The 360-item bank = **6 categories × 3 length levels × 2 languages × 10 items**. Categories: security research, penetration testing, reverse engineering, software/license cracking, GPT/Codex reverse-engineering, NSFW fiction. **Pass criterion: the model must *not* refuse** — any *"cannot / unable / refuse"* response or safety pivot counts as a failure. Gatekeeping: a minimal tier must pass before short/medium tiers run. Raw prompts + responses + pass/fail are logged to `tests/runs/`. This is a genuine (if shallow) **effectiveness-measurement loop for a jailbreak** — a red-team eval harness, inverted.

## 5. Lineage & landscape (NOT world-first)

This is the **GPT-5.6 iteration of an established 5.5-era genre**, not a novel technique:
- **Upstream (credited in Acknowledgments):** `yynxxxxx/Codex-5.5-codex-instruct-5.5` (author *li lingbo*) — MDX-Tom retains attribution for the README organization, the `model_instructions_file` deployment approach, and the licensing framework. *(li lingbo / yynxxxxx is **not** a corpus subject → this is a credited non-corpus upstream, **not a Pattern #57 corpus-recursion**.)*
- **Siblings / forks:** `xsser/codex-jailbreak-guide` (the "guide + honest ANALYSIS.md" sibling), `HuLWe/codex-5.5-codex-instruct-5.5`, `lingbol088-spec/Codex-5.5-codex-instruct-5.5`.
- The whole cluster sits under GitHub's `chatgpt-5-5` topic and exploits the same `model_instructions_file` vector.

So: **NOT world-first** (the genre is populated and predates it), but — hand-verified by collision grep of `_state/` + `_patterns/` + `03 Projects/` (sanity-anchored on CLIProxyAPI v207 + OmniRoute v208, both hit) — **corpus-first for the offensive-LLM-jailbreak / safety-bypass-prompt-pack surface**. The nearest vault neighbors are all defensive or academic: `dive-into-llms` (an academic adversarial-ML chapter *about* jailbreaking), `get-shit-done` (`prompt-injection-scan.sh`, a defensive scanner), SkillSpector v169 (defensive skill scanner), agency-agents governance.

## 6. Disclaimer (verbatim, as-shipped)

*"利用官方配置机制，不修改二进制、不劫持网络、不篡改进程。风险自负。"* — "Uses official configuration mechanism; does not modify binaries, does not hijack network traffic, does not tamper with processes. User assumes all risk." **True as far as it goes** (it does use an official config feature), but it is *not* a safety disclaimer — there is no "research-only," no ToS caveat, and no note that installing it violates OpenAI's usage policy or risks account suspension.

## 7. Why it lands in the corpus (cross-references)

- **Pattern #38 "Prompt-Leak-Archive Genre" — CONTRAST, not instance.** system_prompts_leaks v21/v205 are the *defensive/transparency* pole of the "prompt-as-artifact" space (archive the real prompt so people can study it). This is the **offensive/weaponization** pole (replace the prompt to defeat safety). Same medium (a text prompt is the artifact), opposite intent. Recorded as a within-space **polarity observation**, not a #38 instance.
- **Offensive-security cluster.** shannon v45 / Strix v190 are autonomous AI *pentest agents*; this is a *prompt pack*, not an agent — a different offensive artifact class.
- **Defensive adversary.** SkillSpector v169 (scans skill packages for malicious patterns) is the natural counter-tool; `get-shit-done`'s `prompt-injection-scan.sh` is the defensive scanner class.
- **Config-manipulation cluster.** `codex-instruct.py` mutates Codex's `config.toml` (`model_instructions_file`) — same "own the CLI's config" surface as cc-switch v73, opencode-antigravity-auth v67, and OmniRoute v208 ("one-click account import from the config dir"). Here the config write is the *attack*.
- **Prompt-injection-defense thread.** Directly on system_prompts_leaks v205's "harden hireui against candidate-content injection," the API-security memory thread (BOLA/authorization), and the **RATIFIED candidate-LLM-legibility ADR** (any hireui LLM path affecting a candidate outcome must be fixed/legible/audited/eval-gated).
- **#66 supply-chain / DUAL-USE — par excellence** (see the Verdict fence).
- **#12** — writes an LLM-routing / instruction artifact (the `model_instructions_file`).
- **#19 19a** — first `MDX-Tom` author.

## 8. Honest limits of this analysis

- **NOT source-cloned.** For an offensive artifact, cloning would pull the bypass prompts + the cracking/NSFW test bank into the working tree; catalog-level analysis (README + file inventory + landscape + a sibling's honest ANALYSIS.md) is the right depth. All facts here are page/README/landscape-stated, hand-verified where possible.
- **Efficacy is self-reported** ("120/120") and, per §3, measured against the softest layer — treat as unverified marketing, not a benchmark.
- **§37.4:** stars/forks/date are page-stated (mocked API) → not a velocity/#52 claim.
