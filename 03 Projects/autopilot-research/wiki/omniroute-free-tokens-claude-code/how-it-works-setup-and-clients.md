# How It Works — Setup & Client Integration

## Source
Anchor t1 (VPS install), t2/t4 (npm setup), t6 (Claude Desktop third-party inference), t7 (routing rules); OmniRoute docs (`ENVIRONMENT.md`, `.env.example`, `REMOTE-MODE.md`). Security posture: [[security-and-privacy]].

## Install (as shown in the videos)
```bash
# system prep: Node 22+ required (v18/19 will break)
npm install -g omniroute
omniroute            # starts the gateway + dashboard on http://localhost:20128
```
- The anchor installs on a **VPS** (for 24/7 availability), updates the system, installs Node 22, then runs the install commands. Setup completes in ~2–3 minutes.
- **Dashboard:** `localhost:20128` — first login uses default password **`change me` / `CHANGEME`** (you're prompted to change it). ⚠️ Videos frequently *don't*. See [[security-and-privacy]].
- **24/7 on a VPS:** a **systemd service file** keeps the gateway running after you close the terminal (the anchor walks through creating + enabling it).

## Configuring providers & combos
1. In the dashboard, open **Providers** → filter **free only** → add a provider (paste its API key, or OAuth for the subscription providers).
2. Create an **API key** in OmniRoute's key manager (this is what your client authenticates with — *not* the upstream keys).
3. Build **combos** — named model bundles with a routing strategy (priority / round-robin / cheapest-first…). The client selects a combo by name.
4. OmniRoute exposes one **OpenAI-compatible endpoint**; a "generate config" button emits a ready client config (e.g. for OpenCode).

## Connecting clients
- **Claude Code / OpenCode / Cursor / Cline / Codex CLI:** edit the client's settings to set the **base URL** to `http://<host>:20128/...` and the **API key** to your OmniRoute key. The anchor does exactly this in Claude Code's `settings.json` (and the model that answers is DeepSeek V4 — Path A).
- **Claude Desktop** (t6, t7): enable **Developer Mode** (Help → Troubleshooting → Enable Developer Mode), then **Developer → Configure Third-Party Interface**:
  - Connection type: **Gateway**
  - Credential kind: **Static API Key**
  - **Gateway Base URL:** the OmniRoute/Bifrost endpoint (Claude Desktop expects a specific `/anthropic` path)
  - Model discovery only surfaces models whose names contain **Opus / Sonnet / Haiku** — so free models are **aliased** to Claude-style names (or reached via a Claude-named combo) to appear.

## What actually happens on a request
1. Client sends a request for e.g. `claude-opus-4.8`.
2. Gateway's routing rule matches (`model contains "claude"`) and **redirects** to a free model (DeepSeek / Nemotron / Gemini free tier).
3. Response comes back; the client still displays "Anthropic Opus 4.8." (t7 confirms via logs it's really Nemotron.)
4. A ~7,000-token system prompt ("you are Claude Code, Anthropic's official CLI") + ~71–95 tools ride along — which is why the Cowork/agent features still work behind a swapped model.

## Reliability caveats
- **Auto-fallback** re-routes on rate-limit/outage — but quota-awareness had a real bug (GitHub #7387, 2026-07-16→17: combos still picked exhausted-quota accounts). See [[caveats-and-corrections]].
- Free-tier models are **slower** and **rate-limited**; expect quality swings and occasional first-call latency (repeatedly visible in the demos).

## Key Takeaways
- One command (`npm i -g omniroute`) + Node 22 → a local gateway on `:20128`; a **systemd** unit makes it 24/7 on a VPS.
- Clients connect by pointing their **base URL + key** at OmniRoute; Claude Desktop uses the official **third-party-inference** developer feature.
- Free models are **aliased to Claude names** to pass Claude Desktop's Opus/Sonnet/Haiku discovery filter — the UI says Claude, the engine isn't.
- The setup works, but **hardening is omitted** ([[security-and-privacy]]) and quota-aware fallback has been buggy.
- Related: [[what-omniroute-is]] · [[cliproxyapi-lineage-and-the-gateway-ecosystem]]
