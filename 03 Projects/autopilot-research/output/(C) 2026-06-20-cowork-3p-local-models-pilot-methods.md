# Pilot methods — applying Cowork on 3P (local + cloud models) to your working flows

> **Source:** [[cowork-third-party-inference/_index]] — Bart Slodyczka's "Claude Cowork + Ollama = 100% FREE & PRIVATE" (video [ME4flXK_6tQ](https://www.youtube.com/watch?v=ME4flXK_6tQ), 2026-04-25, 18:41) + Anthropic's official [Cowork on 3P gateway docs](https://claude.com/docs/cowork/3p/). Verification log: [[cowork-third-party-inference/source-provenance]].
> **Date:** 2026-06-20.
> **Your working flows (from vault + memory):** (A) the **autopilot-research knowledge pipeline** (this vault — could run private research compiles on a local model, trading latency for zero-cost + zero-data-leakage); (B) **hireui** — TalentAxis recruitment SaaS, your **Goal #2** build target (recruitment PII = **data-sovereignty** killer app — candidate resumes must *never* leave a private model; local Ollama-via-gateway for dev/test + Cowork in the product); (C) your **Claude Code harness / personal dev flow** ($0 private Cowork for offline dev; harness-vs-model decoupling as a principle); (D) **Scrum coaching / team + client confidentiality** (MDM Export for team rollout; the "harness is the product, model is swappable" teaching frame).
> **18 methods, ranked.** Each is grounded in a specific video setup pattern (Ollama local, OpenRouter cloud, skills + MCP, Tailscale bridge) or a cross-pattern theme (data-sovereignty, cost, harness decoupling), with a concrete first step and a success signal.
>
> **The headline:** **hireui data-sovereignty via Cowork-on-3P gateway + Ollama local model** — candidate resumes never leave the machine; zero marginal cost; build-it-right from day one with a model-agnostic gateway layer.

---

## ▶ Start here (recommended sequence)

1. **This week, lowest friction:** **B2** — **gateway API sketch for hireui** in `hireui/_bmad-output/runbooks/` (~45 min). No Ollama yet. Just the shape: hireui agent talks to a gateway at some URL (could be local Ollama + Tailscale, or cloud, or a future self-hosted LLM), never Anthropic's API directly. You already have cost-optimization + eval specs there — this plugs the model-agnostic layer underneath. This turns Goal #2 from "Claude only" to "Claude + any model you swap in."
2. **Strategic Goal-#2 + data-sovereignty track:** **A1 → B2 → B4 → B5** — the local-Ollama pipeline for recruitment evaluation at zero cost, with candidate data staying on-machine. (A1 = set up Ollama + Gemma 3 locally; B2 = spec the gateway layer; B4 = write a test eval using the local model; B5 = measure cost + latency vs. Anthropic API — proves the business case.)
3. **Ongoing habit:** **C12 + C13** — before you reach for paid Cowork, ask "could this run on a local model?" (personal dev, private notes, client confidentials). A 30-second gate that compounds to 100% of small jobs running offline + free.

---

## Ranked table

| # | Method | Flow | Effort | Value | Why it ranks here |
|---|---|---|---|---|---|
| **B2** | Gateway API sketch for hireui | B hireui | Low–Med (design) | **Very High** | Unlocks model-swappability from day one; turns Goal #2 into a "bring-your-own-model" product |
| **A1** | Set up Ollama locally + Gemma 3/E2B model | A pipeline | Low (~30m) | High | The foundation; proves "free private" works; reusable baseline for B4/B5 |
| **B4** | Eval-first with local Gemma model | B hireui | Med | **Very High** | Same eval harness, different model; proves non-Claude can screen candidates fairly |
| **B5** | Cost + latency analysis: local Ollama vs. OpenRouter vs. Anthropic | B hireui | Med | High | The business case for data-sovereignty + cost: what do you give up? |
| **C12** | The 30-second "run this offline?" gate | C harness | Low (heuristic) | High | Catches every personal dev / private note / client-confidential job |
| **B1** | Data-sovereignty contract for hireui | B hireui | Design | **Very High** | Names the invariant: candidate data never leaves machine. Build the gateway to enforce it. |
| **B3** | Cowork-on-3P gateway setup in hireui's dev environment | B hireui | Med (infrastructure) | High | Proves the circuit: hireui agent → gateway URL → local Ollama |
| **A3** | Hybrid pipeline: cold-start on Opus, extend on local Gemma | A pipeline | Med | Med–High | The cost-speed tradeoff for autopilot research |
| **C14** | HTTPS bridge options: Tailscale Serve vs. alternatives | C harness | Low–Med | Med | Tailscale works; so do Caddy, ngrok, cloudflared — pick based on your setup |
| **A2** | Skills + MCP setup for local models (web search, files, etc.) | A pipeline | Med | Med–High | Local Gemma can't web-search natively; restore via MCP Brave Search or equivalent |
| **B6** | Run a real recruitment screener on local Gemma; observe quality delta vs. Opus | B hireui | High (measurement) | Med–High | The fairness + latency test; informs whether Gemma is production-ready for screening |
| **C13** | Offline mode for Claude Code: "dev without API" checkpoint | C harness | Low–Med | Med | Sketch a 1-week dev sprint with zero Anthropic API calls; measure friction |
| **A4** | Privacy audit: what data enters the pipeline? where does it go? | A pipeline | Med (design) | Med | Compliance for autopilot if it handles client content or sensitive URLs |
| **D15** | Teaching frame: "the harness is the product, the model is swappable" | D coaching | Low | Med | For teams; names the Anthropic design choice the video assumes |
| **A5** | Fallback logic: if Gemma fails, retry with OpenRouter cheaply | A pipeline | Med | Low | The hybrid strategy; adds complexity but reduces failure-to-expensive-model fallback |
| **C11** | Configure MCP Brave Search locally + wire into Claude Desktop | C harness | Med | Med | Restore web-search for non-Claude models in Cowork; reusable across local + cloud |
| **B7** | Security: "current-user" invariant for the hireui gateway | B hireui | Design | Med | Recruitment data = multi-tenant PII; the gateway must never escalate permissions |
| **D16** | Pilot Cowork-on-3P in a client engagement (confidentiality angle) | D coaching | High (real engagement) | Med | The actual test; does a client trust their data to a local model + your team? |

---

## A — Autopilot-research knowledge pipeline (this vault)

> This vault runs knowledge compilation at scale (overnight loops, multi-agent fan-outs). Cowork-on-3P opens two levers: **cost** (a free local model for test/dev compiles) and **privacy** (sensitive sources, client research, never touch Anthropic's API).

### A1 — Set up Ollama locally + Gemma model (foundation)
- **Video pattern:** the foundation — Ollama as a local inference server, two model tiers (a large model like Gemma 4 26B — 256K context, ~18GB, needs capable hardware — or a much smaller variant for modest machines), `ollama pull <model>` to download, `ollama list` to verify ([[cowork-third-party-inference/setup-local-ollama]]). ⚠️ The video's "Gemma E2B ~7.2GB" figure doesn't match Ollama's published model sizes — check the library before pulling.
- **Why it matters:** proves "free + private" works; becomes the baseline for testing (A3, A5) and hireui evals (B4).
- **First step:** 
  ```bash
  # Install Ollama (one-time, system-wide)
  brew install ollama
  
  # Pull a small Gemma for modest hardware (check the library for the exact tag + size)
  ollama pull gemma2:2b
  
  # Verify
  ollama list
  ```
  ([Ollama model library](https://ollama.com/library); sizes vary by quantization — verify the tag + VRAM fit before pulling.)
- **Success signal:** `ollama list` shows a model ready to use; local HTTP endpoint at `http://localhost:11434/v1/` (OpenAI-compatible API).

### A2 — Skills + MCP setup for local models (web search, files, etc.)
- **Video pattern:** local Gemma can't web-search natively (unlike Opus/Sonnet). Restore capability via MCP — configure Brave Search MCP by editing `~/.config/Claude/claude_desktop_config.json` ([[cowork-third-party-inference/skills-mcp-websearch-byom]]).
- **Why it matters:** web search is critical for autopilot drains; without it, local model compiles will be stale.
- **First step:**
  ```bash
  # 1. Create a Brave Search MCP server config in Claude Desktop's config file
  #    (the video shows the exact file location + JSON shape)
  # 2. Get a Brave API key: https://api.search.brave.com/ → create account → API keys
  # 3. Edit the config file to include:
  {
    "mcpServers": {
      "brave-search": {
        "command": "npx",
        "args": ["-y", "@brave/brave-search-mcp-server"],
        "env": {"BRAVE_API_KEY": "YOUR_KEY"}
      }
    }
  }
  # 4. Restart Claude Desktop
  # 5. In Cowork, go Settings > Developer > MCP > verify Brave Search is connected
  ```
- **Success signal:** a test query in Cowork like "latest Claude news" returns fresh results via Brave, not a failure.

### A3 — Hybrid pipeline: cold-start on Opus, extend on local Gemma
- **Video pattern:** recognize the tradeoff — a local model is materially slower than Opus/Sonnet (the speaker ranks local slowest, cloud-3P faster, paid Anthropic fastest), but free. Use the local model for **extend** operations (add 2–3 articles to a mature topic), not full cold-start drains ([[cowork-third-party-inference/tradeoffs-and-when-to-use]]).
- **Apply:** in `bin/autopilot-drain.py` (or Phase 2 of the routine), branch the source-count + model-choice on cold-start-vs-extend.
- **First step:**
  ```python
  # Pseudocode in autopilot-drain.py or the routine
  if job_type == "cold_start":
      model = "claude-opus-4-1"  # Full synthesis + multi-source
      sources = 8
  elif job_type == "extend":
      model = "gemma2:27b-instruct"  # Just fill gaps, use what's cached
      sources = 2
  ```
- **Success signal:** an "extend" run on the local model measurably completes cheaper than a cold-start on Opus (record your *own* wall-clock + cost baselines on the first run — don't trust a guessed number).

### A4 — Privacy audit: what data enters the pipeline? where does it go?
- **Video pattern:** the speaker assumes local Ollama = truly private (no data leaves); OpenRouter = "assume anything sent is collected" ([[cowork-third-party-inference/openrouter-deep-dive]]). But in a mixed setup, you need a map.
- **Apply:** draw the data flow — which sources are safe for local Gemma, which require Opus (and thus Anthropic's servers)?
- **First step:** audit `raw/topics-queue.md` and the last 10 compiles. For each topic, ask: "is this client content? industry secret? personal? or public knowledge?" Mark sensitivity on each. Local Gemma only for "public."
- **Success signal:** a one-page map: "local-Gemma topics" vs. "Opus-only topics" vs. "hybrid (cold-start Opus, extend Gemma)."

### A5 — Fallback logic: if Gemma fails, retry with OpenRouter cheaply
- **Video pattern:** non-Claude models struggle with some tasks (the video showed Gemma hanging on the "create Word doc" task); the workaround is "run the skill once, inspect the failure, ask the model to fix it" ([[cowork-third-party-inference/skills-mcp-websearch-byom]]). A fallback strategy: if local fails, escalate to OpenRouter (cheap) rather than Anthropic (expensive).
- **Apply:** in the routine's error-handling (Phase 5), add a retry-budget: Gemma × 2 attempts, then OpenRouter Gemma (~$0.06/$0.33 per million I/O tokens), then Opus.
- **First step:** in `skills/(C) autopilot-research-routine.md` Phase 5 (error handling), add:
  ```
  If compile fails:
    1. Retry on local Gemma (budget: 1 more)
    2. If still fails, retry on OpenRouter (Gemma model; cheaper than Opus)
    3. If still fails, escalate to Opus
    Log the model + attempt # in the loop-log
  ```
- **Success signal:** a compile that would have needed Opus falls back to OpenRouter + saves 10× on cost (Gemma via OpenRouter is ~$0.06 per million input tokens vs. Opus at ~$15).

---

## B — hireui (Goal #2: recruitment SaaS, data-sovereignty as the killer app)

> hireui has **no LLM integration yet** (verified 2026-06-15). So these are **build-it-right specs** — Cowork-on-3P as the foundational layer, not a retrofit. Candidate data (resumes, contact info, salary history) = PII that should never leave the machine. This suite spec the **gateway + local model** strategy for recruitment screening.

### B1 — Data-sovereignty contract for hireui ⭐
- **Why it matters:** recruitment = candidate PII. The Cowork-on-3P gateway is your leverage to keep that data private while keeping the harness (skills, Workflows, UI polish) that makes hireui work. This is not a nice-to-have; it's the product differentiation.
- **Apply:** write a 1-paragraph data contract in the hireui CONSTITUTION or a new `DATA_SOVEREIGNTY.md`:
  ```
  hireui agent queries never leave the network boundary.
  All inference happens on a private model (Ollama local or self-hosted cloud).
  No candidate resume, contact, or salary data is sent to Anthropic's API or any third party.
  The agent runs under the requesting user's permissions (row-level, no escalation).
  ```
- **First step:** create `hireui/DATA_SOVEREIGNTY.md` (or update the CONSTITUTION) with the contract above. Cite [[cowork-third-party-inference/overview]].
- **Success signal:** a stated, testable invariant before any code. In interviews, you can point to this and say "we process recruitment PII on-machine, not in the cloud."

### B2 — Gateway API sketch for hireui ⭐
- **Video pattern:** Anthropic's **gateway** protocol — hireui agent doesn't know whether it's talking to local Ollama, cloud OpenRouter, or a self-hosted model; it just POSTs `/v1/messages` to a gateway URL ([[cowork-third-party-inference/gateway-protocol-deep-dive]]).
- **Why it matters:** unlocks model-swappability from day one. You can eval on Gemma, productionize on a better model, switch later, all without touching the agent code.
- **Apply:** spec the hireui agent to use the Anthropic Messages API **through a gateway**, not direct.
- **First step:** create `hireui/_bmad-output/runbooks/gateway-api-spec-2026-06-20.md`:
  ```markdown
  # Gateway API Spec for hireui Agent
  
  ## Configuration
  - Base URL: configurable env var `INFERENCE_GATEWAY_URL` (e.g., `http://localhost:11434/v1/`)
  - Auth: Bearer token or X-API-Key, configurable by `INFERENCE_AUTH_TYPE`
  - Model: configurable env var `INFERENCE_MODEL` (e.g., `gemma2:27b-instruct`)
  
  ## Endpoints
  - POST `/v1/messages` — full Anthropic Messages API (streaming + tool use)
  - GET `/v1/models` — list available models (auto-discovery for UI)
  
  ## Invariants
  - Agent code NEVER hardcodes "anthropic" or "openrouter.ai"
  - Switchable at deploy time without code changes
  - Fallback: if gateway is down, queries fail gracefully (not escalate to expensive)
  
  ## Initial Model Targets
  - Dev/test: Gemma 3 local (free, zero latency for inner loop)
  - Staging: OpenRouter Gemma (cheap cloud, same model family as test)
  - Production: TBD (Opus, or a self-hosted larger model)
  ```
- **Success signal:** the spec is reviewed + signed off. Hireui's agent uses gateway config from day one (even if the agent itself hasn't been built yet).

### B3 — Cowork-on-3P gateway setup in hireui's dev environment
- **Video pattern:** the full walkthrough — configure Claude Desktop to use a gateway (Developer > Configure third-party inference > Gateway connection), plug in the URL + auth, relaunch, pick a model ([[cowork-third-party-inference/setup-local-ollama]]).
- **Apply:** in hireui's dev guide or BMAD harness, document the step-by-step for a team member to set up Cowork talking to a local Ollama instance (or OpenRouter for CI/CD).
- **First step:** create `hireui/docs/dev-setup-cowork-gateway.md` with:
  1. Install Ollama + pull Gemma model (copy the exact command from A1)
  2. Configure Claude Desktop: `Help > Troubleshooting > Enable Developer Mode > Developer > Configure third-party inference`
  3. Fill in: Base URL = `http://localhost:11434/v1/`, Auth = Bearer, Key = "Ollama"
  4. Test: run a simple message in Cowork; verify response comes from Gemma
  5. For CI/CD: use a containerized Ollama endpoint instead (point to a service URL)
- **Success signal:** a new team member can set up Cowork + local Ollama in <15 minutes without asking questions.

### B4 — Eval-first with local Gemma model ⭐
- **Video pattern:** non-Claude models struggle with some tasks (the video showed Gemma hanging on skill execution). Before you trust Gemma to screen real candidates, run it through your eval suite (from [[prompt-evaluation/_index]]).
- **Why it matters:** fairness. If Gemma scores candidates differently than Opus, you need to know *before* production.
- **Apply:** take the 20–50 candidate eval cases you (presumably) wrote for hireui evals, run them on local Gemma, compare results to Opus.
- **First step:** in `hireui/evals/`:
  ```python
  # Pseudocode
  for case in eval_cases:
      # Run the same candidate through both models
      opus_verdict = run_screening(case, model="claude-opus-4-1")
      gemma_verdict = run_screening(case, model="gemma2:27b-instruct")
      
      # Compare: do they agree? Do they rank candidates the same way?
      if opus_verdict != gemma_verdict:
          print(f"DELTA: case {case.id} — Opus={opus_verdict}, Gemma={gemma_verdict}")
  ```
- **Success signal:** you have a delta report: "Gemma agrees with Opus on 92% of cases; 8% delta is in interviews-vs-rejections boundary calls — acceptable for staging, flag for production review."

### B5 — Cost + latency analysis: local Ollama vs. OpenRouter vs. Anthropic ⭐
- **Video pattern:** OpenRouter pricing (Gemma 26B: ~$0.06 input, ~$0.33 output per million tokens) vs. Anthropic (Opus: ~$15 input, ~$45 output per million) ([[cowork-third-party-inference/openrouter-deep-dive]]). Local Ollama = $0 (your hardware cost, already sunk).
- **Apply:** run a realistic workload (screen 100 candidates, realistic resume+job-description length) on all three. Measure cost + latency.
- **First step:**
  ```python
  # Workload: 100 candidates, avg 2000 tokens/candidate
  # Metrics: cost, latency, verdict quality (vs. human ground truth)
  
  models = [
      ("gemma_local", "http://localhost:11434/v1/", "gemma2:27b-instruct", cost=0),
      ("gemma_openrouter", "https://openrouter.ai/api/v1", "google/gemma-4-26b-a4b-it", cost_per_mtok=0.06),
      ("opus", "https://api.anthropic.com/", "claude-opus-4-1", cost_per_mtok=15),
  ]
  
  for name, url, model, cost in models:
      start = time.time()
      verdicts = [screen_candidate(c, url, model) for c in candidates]
      elapsed = time.time() - start
      total_cost = ... # Calculate based on token usage
      print(f"{name}: {elapsed:.1f}s, ${total_cost:.2f}, quality={judge(verdicts)}")
  ```
- **Success signal:** a one-page table: "local Gemma = 30s, $0, 90% quality; OpenRouter = 8s, $0.12, 95% quality; Opus = 6s, $1.50, 99% quality." You can now make the production choice.

### B6 — Run a real recruitment screener on local Gemma; observe quality delta vs. Opus
- **Video pattern:** the speaker tested Gemma on a real task (create-document-from-web-search) and hit a failure (skill invocation hung). The response: "run it once, inspect the error, ask the model to fix the prompt" ([[cowork-third-party-inference/skills-mcp-websearch-byom]]). This is the fairness test.
- **Apply:** take your first real-world recruitment screening query (e.g., "screen these 5 candidates for the Senior Engineer role") and run it on Gemma in Cowork (via the local Ollama gateway). Observe where it succeeds vs. fails.
- **First step:** in hireui's Cowork dev setup (from B3), write a test query: "Screen candidate Resume_123 against job description JD_456. Output: hire/reject + reasoning." Run it on Gemma. Log any failures.
- **Success signal:** the query completes; results are sensible; if there's a failure, you can articulate why (model confusion, skill issue, context window) and a fix (better prompt, smaller context, simpler task).

### B7 — Security: "current-user" invariant for the hireui gateway ⭐
- **Principle (architectural best practice):** "run-as-current-user" — the agent only ever executes under the requesting user's permissions. In recruitment this means a screener agent never escalates privileges and never sees candidates outside the user's scope. (General security best practice — not a claim from the video.)
- **Apply:** write it as a non-functional requirement in B2's gateway spec.
- **First step:** in `gateway-api-spec-2026-06-20.md`, add:
  ```markdown
  ## Security Invariant: Current-User Execution
  
  The agent executes queries under the authenticated user's permissions:
  - Row-level security filters apply (user's team, user's open requisitions only)
  - No service account, no privilege escalation
  - Multi-tenant: agent in Tenant A cannot see Tenant B's candidates
  
  Testing: a user in Team A requests a screen → agent sees only Team A candidates (verified in query logs)
  ```
- **Success signal:** a testable rule before the agent is built.

---

## C — Claude Code harness / personal dev flow

> Cowork-on-3P enables **offline dev** (no API calls) + **free personal use** (local Gemma) + **confidentiality** (client notes, sensitive code, private scripts). Three small gates catch the high-value cases.

### C11 — Configure MCP Brave Search locally + wire into Claude Desktop
- **Video pattern:** step-by-step MCP setup (edit `claude_desktop_config.json`, add the Brave server) ([[cowork-third-party-inference/skills-mcp-websearch-byom]]).
- **Apply:** you already did this for A2 (autopilot pipeline). Do it once for your personal dev setup too.
- **First step:** follow A2's step-by-step, but this time for your personal Claude Desktop config.
- **Success signal:** `web search` works in a local-Gemma Cowork session without errors.

### C12 — The 30-second "run this offline?" gate
- **Video pattern:** the cost frame — local Gemma is free; if it can do the job, why use paid API? The gate: before reaching for paid Cowork, ask "**could this run on a local model?**" Personal dev, private notes, client confidentials, brainstorming — all of these probably can.
- **Apply:** habit, not code. Keep a one-liner in your dev notes: *"Local Gemma first. Paid Cowork only if Gemma can't do it."*
- **First step:** for your next 5 Cowork sessions, note which could have been local:
  - [ ] Dev debug session (local Gemma fits)
  - [ ] Client call notes (confidential → must be local)
  - [ ] Personal project brainstorm (local fits)
  - [ ] Proprietary code review (might fit locally)
  - [ ] Research on public knowledge (fits)
- **Success signal:** you identify ≥3 sessions from the last week that could have run locally + free.

### C13 — Offline dev on a local model: "dev without the API" checkpoint
- **Scope correction:** the Desktop **"Configure third-party inference" gateway is Cowork-only** — Claude Code (CLI) does *not* support that gateway UI (Anthropic issue [#52572](https://github.com/anthropics/claude-code/issues/52572) was closed *not-planned*). But Claude Code can still run offline: point it at a local model via the `ANTHROPIC_BASE_URL` env var → Ollama's **native Anthropic Messages API** (v0.14.0+). So "offline Cowork" uses the gateway; "offline Claude Code" uses `ANTHROPIC_BASE_URL` ([[cowork-third-party-inference/ollama-deep-dive]]).
- **Apply:** run a short sprint where development happens on the local model — Cowork via the gateway, Claude Code via `ANTHROPIC_BASE_URL`. Find the friction.
- **First step:** next week, (a) configure Cowork to local Ollama (from B3) for chat/knowledge work, and (b) `export ANTHROPIC_BASE_URL=http://localhost:11434` for a Claude Code session. Run 3–5 tasks. Note where the local model struggles.
- **Success signal:** a one-page "friction report" — what worked fine locally, what didn't, the minimal improvement needed (e.g., a bigger context window or a stronger local model).

### C14 — HTTPS bridge options: Tailscale Serve, alternatives, and when you need none
- **Video pattern + update:** the video bridges Ollama's HTTP (`localhost:11434`) to HTTPS with **Tailscale Serve**. **This may now be unnecessary:** since Ollama **v0.14.0** (Jan 2026) Ollama speaks the Anthropic Messages API natively, and for *local* use you can often point the gateway straight at `http://localhost:11434` — no bridge ([[cowork-third-party-inference/tailscale-https-bridge]], [[cowork-third-party-inference/ollama-deep-dive]]).
- **Why it matters:** the bridge is the fiddliest step; skipping it (or picking the right tool) decides how easy the setup is — and "100% private" only holds if the bridge keeps traffic local.
- **First step:** read [[cowork-third-party-inference/tailscale-https-bridge]] and pick, in order of preference for local-private use:
  - **No bridge** — point the gateway at local Ollama directly (v0.14.0+ native Anthropic API); confirm your Cowork build accepts a local HTTP URL.
  - **Tailscale Serve** (video method): MagicDNS + Let's Encrypt; keeps traffic on your tailnet/device (private). *Do not use Tailscale **Funnel** — it exposes the endpoint publicly.*
  - **Caddy reverse proxy**: local auto-TLS, full control.
  - **cloudflared / ngrok**: easy tunnels, but route through a third party — **not** "100% private."
- **Success signal:** you can state why you picked your bridge (or no bridge) — and confirm traffic stays local if privacy is the goal.

---

## D — Scrum coaching / team + client confidentiality

### D15 — Teaching frame: "the harness is the product, the model is swappable"
- **Video pattern:** the speaker interprets Anthropic's design: "they separated the harness (the desktop app) from their model because enterprise customers wanted the harness (amazing tool) but their own private models. That's why they released Cowork-on-3P relatively silently — we all benefit from it." ([[cowork-third-party-inference/overview]]).
- **Why it matters:** for teams, this is a powerful teaching moment. It reframes the question from "Claude vs. other models?" to "How do we architect so the model is swappable?"
- **Apply:** when onboarding a team to hireui or any LLM-powered feature, start with this frame.
- **First step:** in team kickoff or a working-agreements session, explain:
  ```
  Our approach to hireui + LLM:
  - The harness = the app, the skills, the Workflows (ours to build)
  - The model = swappable (Opus for accuracy, Gemma for cost, X for speed)
  - Day 1: we run on Gemma (free, fast iteration)
  - Day 30: we eval on Opus (fair comparison)
  - Production: we pick the model that wins the eval + budget tradeoff
  
  This isn't "we use Claude" — it's "we use Claude's harness, and we choose the best model for the job."
  ```
- **Success signal:** team members repeat back the frame: "wait, so we could swap models without rewriting?"

### D16 — Pilot Cowork-on-3P in a client engagement (confidentiality angle)
- **Video pattern:** the headline benefit — data never leaves the machine. For client work, this is a selling point.
- **Apply:** in your next Scrum coaching or training engagement, pitch it: "we can analyze your data in Cowork, with zero data leaving your machine — we run a private model locally."
- **First step:** pick a client or internal team project where confidentiality matters (e.g., salary band analysis, code review, strategy session notes). Set up Cowork-on-3P locally. Invite the client to try it.
- **Success signal:** client says "I feel more confident sharing sensitive data if it stays on-machine."

---

## Cross-links

- [[cowork-third-party-inference/_index]] (source topic) · [[cowork-third-party-inference/setup-local-ollama]] (Ollama walkthrough) · [[cowork-third-party-inference/openrouter-deep-dive]] (cloud alternative) · [[cowork-third-party-inference/gateway-protocol-deep-dive]] (the API spec) · [[cowork-third-party-inference/tailscale-https-bridge]] (HTTPS bridge options).
- Sibling pilots this composes with: [[prompt-evaluation/_index]] (B4's fairness eval) · [[claude-api-cost-optimization/_index]] (B5's cost analysis) · [[multi-agent-orchestration/_index]] (A3/A5's hybrid routing) · [[harness-engineering/_index]] (parent discipline) · [[claude-md-12-rules/_index]] (C13's offline ethos).

## Suggested next action

Do **B1 + B2 this week** (90 min, no code — just a data-sovereignty contract + a gateway API sketch in `hireui/_bmad-output/runbooks/`). These unlock the entire "private recruitment LLM" angle of Goal #2. Then run **A1 + B4 in parallel next week** — set up Ollama locally, eval on Gemma, get the fairness delta report. By week 3, you'll have **B5** (cost + latency) — the business case for why hireui should be built on a gateway from day one. Then **B3** (team onboarding) becomes a no-op: they follow the docs and it just works.

Tell me which, and I'll scaffold it: a `DATA_SOVEREIGNTY.md` + `gateway-api-spec-2026-06-20.md` ready for hireui review, or an Ollama + fairness-eval checklist for A1 + B4.
