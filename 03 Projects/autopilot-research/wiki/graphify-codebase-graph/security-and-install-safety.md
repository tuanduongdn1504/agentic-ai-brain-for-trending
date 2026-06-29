# Graphify — Security & install safety (go/no-go)

> **Source:** [[graphify-codebase-graph/_index]]. Adversarially assessed (Workflow `wf_2f2a5052-7ac`). **Verdict: safe-with-caveats for your knowledge vault; risky for the hireui production monorepo.** This matters because you run npm-security-check discipline before unfamiliar installs.

## The tool itself: legitimate

- **MIT license**, **YC S26-backed**, single maintainer (Safi Shamsi, MSc Data Science — thesis on knowledge-graph RAG).
- **~69.6K stars, ~1.8M PyPI downloads** (954K in 30 days), 139 releases, v0.8.44 (2026-06-19). High adoption for a ~2.5-month-old project.
- **No postinstall scripts.** Entry points only: `graphify` → `graphifyy.__main__:main`, `graphify-mcp` → `graphifyy.serve:_main`.
- **No telemetry, no analytics.** AST + Whisper passes are **fully offline**.
- Ships a **`SECURITY.md`** (private reporting, 48h ack / 7-day critical fix), plus defensive controls: URL validation (blocks private/loopback/link-local IPs + cloud-metadata endpoints), prompt-injection defanging with tamper-evident delimiters, HTML escaping, YAML-injection escaping.
- Known/acknowledged issues (not CVEs): Cypher injection in `export.py` (DB exports), SSRF bypass in `_fetch_tweet`, possible XSS in HTML templates. All documented.

## 🚩 The real red flag: typosquatting (Issue #280)

- **The official package is `graphifyy` (two y's).** The single-y **`graphify` was unclaimed on PyPI.**
- An attacker could register `graphify` with a malicious `setup.py`; anyone who **drops one y** silently installs arbitrary code — with whatever filesystem/env access the install has.
- The maintainer recommends defensively registering `graphify`; **it was not confirmed done** at research time.
- **Mitigation:** never type the name from memory. Use **`uv tool install graphifyy`** or **`pipx install graphifyy`** (copy-paste the exact name). This is exactly the `npm-security-check` reflex, applied to pip.

## The Pass-3 data-flow question

- Pass 3 sends **your markdown/PDFs/images/transcripts to your configured LLM provider** (Anthropic/OpenAI/Gemini/Ollama/…) using **your own API key**. **Graphify has no relay server and never sees the content.**
- So privacy = *whatever your provider's terms are*. For non-sensitive corpora this is a non-issue. For regulated data, the content **is** visible in your provider's API logs.
- **$0 + fully private option:** point Pass 3 + queries at a **local Ollama model** — nothing leaves your machine. See [[cowork-third-party-inference/_index]].

## Go / No-Go

### ✅ Your knowledge vault (autopilot-research + Storm Bear) — SAFE with discipline
- No PII, no secrets, no GDPR data — you own all of it.
- Install with **`uv tool install graphifyy`** (exact name), **skip git hooks** at first, **disable query logging** (`GRAPHIFY_QUERY_LOG_DISABLE=1`), and **review the injected skill file** before committing.
- Genuine fit: a natural automated L3/graph layer on top of your existing L1+L2 memory.

### 🚫 hireui (recruitment SaaS monorepo) — DO NOT install (yet)
The combination is the problem, not the tool:
1. **Typosquat → secret exposure.** One typo and arbitrary code runs with access to `.env.local` (DB creds, OAuth, payment keys, Anthropic key).
2. **Data sensitivity / GDPR.** Pass 3 would send recruitment workflows + candidate-evaluation content to your provider; that may breach a data-processing agreement.
3. **Governance conflict.** It auto-writes a skill into `.claude/skills/graphify/` + injects settings — **violates hireui's I-8 operator-only skill registry** (and the git hooks rub against the **I-2 agent-branch policy** + BMAD/CI).
4. **No business urgency.** hireui has **zero Claude API integration** (verified 2026-06-15) — a knowledge graph is nice-to-have, not load-bearing.

**If you ever do want it on hireui:** sandbox it on a throwaway branch/clone, with hooks off, query-log off, an explicit `.graphifyignore` excluding `.env*` and any candidate-data dirs, run Pass 3 against a **local Ollama** model (no cloud exfiltration), and only after the maintainer has defensively registered `graphify`. Treat it as a governed, operator-approved skill addition, not a casual install.

## Key Takeaways

- The tool is **legitimate, popular, transparent, no postinstall scripts** — but it's a single-maintainer, fast-moving 2.5-month-old project (bus-factor 1).
- **The #1 risk is the `graphifyy`-vs-`graphify` typosquat** — install via `uv`/`pipx` with the exact name, never from memory.
- **Pass 3 = your data → your provider via your key.** Use a local model for sovereignty.
- **Safe for the vault, risky for hireui** — context, not code quality, is the deciding factor.
