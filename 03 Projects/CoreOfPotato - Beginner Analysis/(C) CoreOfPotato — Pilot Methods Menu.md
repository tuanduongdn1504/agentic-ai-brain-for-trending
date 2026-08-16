# (C) CoreOfPotato — Pilot Methods Menu

> **v231** · `hwahao/CoreOfPotato` · 2026-08-16
> ⚠️ **Headline: pilot-AVOID.** This is an honest ~14-method menu, not a padded 24. Most rows are *read*, *borrow* or *don't* — because the product itself is a ToS-violating, account-ban-risking free-tier harvester with nothing safely installable. The real payoff is three read-only borrows.

**Why AVOID, in one line:** running it means logging your personal Grok/Gemini/ChatGPT accounts into an anti-detect browser built to evade those vendors' bot protection, behind a gateway that ships with authentication disabled — and the repo's own DISCLAIMER concedes the account-ban risk.

---

## A — Read + learn (zero install, zero risk) ⭐

| # | Method | Why | Effort |
|---|---|---|---|
| **A1** ⭐ | Read `core/server.py` + `core/browser_mgr.py` + `core/drivers/grok.py` on GitHub. Trace one request: `Bearer OCtest` → `validate_user()` → `nav_key = f"{caller}{modu}_{platform}"` → a specific browser tab → DOM scrape → SSE chunks. | The clearest small example in the corpus of **session multiplexing without server-side conversation state** — a 6-char key *is* the routing key *is* the auth token. | 30 min |
| A2 | Read the completion heuristic: poll every 0.25 s, done when `stable_count >= 8` (~2 s of unchanged text). | The cheapest possible argument for why an API contract is worth paying for. Hold it next to a real streaming API. | 10 min |
| A3 | Read `config.example.json` + `require_admin` in `core/routes.py` together. | A live, unusually clean specimen of broken authentication — see **D9**. | 10 min |
| A4 | Read the `caller_map` (`"OC": "OpenClaw"`, `"CD": "OpenCode"`) and note who this was built *for*. | Confirms the intended clients are coding agents, not chat users. Frames the whole design. | 5 min |

## B — Borrow patterns (zero install) ⭐

| # | Method | Why | Effort |
|---|---|---|---|
| **B5** ⭐ | Lift the **`BaseDriver` + driver-registry + per-platform worker-pool** shape into the vault's vendor-seam notes. | The 4th clean data-point on the seam thread: meetily v196 `generate_summary()` · AIRI v210 `xsAI` · lobehub v222 · **CoreOfPotato `BaseDriver`**. Abstract the shared 90 %, special-case the genuinely-different 10 %. | 45 min |
| B6 | Borrow the **three URL-cache strategies** (fixed / time-based / usage-based) as a general "long-lived session hygiene" pattern. | Directly transferable to any long-running agent conversation that degrades with context length. | 20 min |
| B7 | Borrow the **stable-text completion detector** as a *named anti-pattern* in the vault's notes: "heuristic completion detection = the tax you pay for having no contract." | Useful whenever someone proposes scraping instead of integrating. | 15 min |

## C — Hands-on (⚠️ heavily fenced, low value)

| # | Method | Why / why not | Effort |
|---|---|---|---|
| C8 | *If you must feel it:* a throwaway VM + a **burner** Google/xAI/OpenAI account, `setup.sh`, one `curl` to `/v1/chat/completions`. | The only defensible way to run it. Even so: a black-box Chromium binary from an anonymous vendor, and the burner account is the thing that gets banned. **Not recommended** — the architecture is fully legible from A1 without running anything. | 2 h + risk |

## D — hireui / Goal-#2 (the real payoff) ⭐

| # | Method | Why | Effort |
|---|---|---|---|
| **D9** ⭐ | Add to hireui's API-security work: **"a local service holding authenticated sessions MUST require auth by default; never ship wildcard CORS; never treat 'no token configured' as 'allow'."** Then red-team hireui's own local/dev surfaces against exactly that triad. | CoreOfPotato ships `require_auth: false` + `cors_origins: ["*"]` + `require_admin` allowing unconfigured access — the textbook broken-authentication finding, in a real shipped artifact. Composes with the standing **BOLA / api-security** thread (the #1 hireui risk). | 1–2 h, `agent-*` branch |
| **D10** ⭐ | Reinforce the standing ADR: **hireui uses official, paid API keys per vendor ToS — never web-UI scraping, never subscription re-exposure, never free-tier harvesting.** Record CoreOfPotato as the **third confirming anti-pattern instance** (after CLIProxyAPI v207 and OmniRoute v208), and the first that adds *evasion of bot protection* to the list. | Turns three catalogued gray-zone subjects into one durable, cited engineering rule. Zero install. | 30 min |
| D11 | Write the one-line fence into the candidate-LLM legibility ADR: **never route candidate data through a browser-automated consumer AI account.** | Candidate PII into a personal ChatGPT/Gemini session is a data-residency + GDPR + ToS breach stacked on the ban risk. Cheap to state, expensive to omit. | 15 min |
| D12 | Use the `BaseDriver` seam (B5) as a reference when specifying hireui's first LLM feature's provider abstraction. | Keeps the seam decision evidence-based across four independent implementations. | folded into B5 |

## E — Vault / corpus meta

| # | Method | Why |
|---|---|---|
| E13 | File for the overdue audit: the **DEFERRED watch axis** (web-UI-harvesting gateway), the **N=1 mint reviewable alternative**, and the **v207-row-generalization question** (does "re-exposes a non-API consumer entitlement" make this the non-port N=3 that fires the promotion?). |
| E14 | File the **#57** (CoreOfPotato → CloakBrowser **v69**, openly credited) and the **"AI-Generated-Repo Artifact Contamination"** cross-reference — the v69-era observational candidate that was never registered, of which this is a textbook instance. |

---

## ⭐ One-thing path: **A1 → D9 → D10**

Read the request path once (30 min), turn its shipped security defaults into a hireui red-team check on an `agent-*` branch, and bank the "official keys only" rule with its third citation. Zero install, zero risk, two durable artifacts.

## Fence (if anything here is ever run)
`install-snapshot` first · burner accounts only, never a real Google/OpenAI/xAI login · throwaway VM · **set `require_auth: true`, a real `admin_token`, and a non-wildcard `cors_origins` before the first request** · keep `host: 127.0.0.1` · treat the CloakHQ Chromium as an untrusted black-box binary · pin the commit (7 total, stale since 2026-06-09) · never point it at hireui or any candidate data · hireui stays on official paid keys per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first).
