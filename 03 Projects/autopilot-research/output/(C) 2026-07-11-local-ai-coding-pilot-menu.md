# (C) Pilot menu — applying `local-ai-coding-agents` to your working flow

> **From:** wiki topic [[local-ai-coding-agents]] (video: Code with Beto, *"Local AI Coding Agents Are Finally Good Enough"*, 2026-07-09).
> **For:** Storm Bear — vault autopilot work + the **hireui** recruitment SaaS (Goal #2: ship software with these tools).
> **Date:** 2026-07-11.
> **How to read:** 13 methods in 4 tiers, each with *what / why / effort / risk / success signal*. The two standing threads this feeds — **cost-optimization** and **data-residency/privacy** — are tagged 💰 and 🔒. Ranked recommendation at the bottom.

**The one big idea to carry across every method:** local inference turns candidate PII from a *compliance liability* (3rd-party processing) into an *internal, auditable control* (data never leaves the box) — while giving you a **$0-marginal-cost tier** for cheap/bulk work. The trap to avoid is the video's "it's free" framing: it's **high-capex, zero-marginal-cost**, worth it for **volume or privacy**, not for small-scale savings.

---

## Tier A — Try-it-this-week (your own Mac, zero hireui risk)

### A1 · Stand up the local stack + baseline it 💰
- **What:** Install LM Studio → download Qwen3.6-27B (MLX build) → toggle the OpenAI server on → point `opencode` at `http://localhost:1234/v1` via one `baseURL` (see [[local-ai-coding-agents/opencode-local-provider]]). Run it on a throwaway repo.
- **Why:** You can't reason about local-vs-cloud for hireui until you know (a) whether your machine even has the RAM (need **≥24 GB** unified memory; check first), and (b) real tok/s + latency on your hardware.
- **Effort:** ~1 hour. **Risk:** none (sandbox).
- **Success signal:** the SF-Symbols-from-screenshot demo works locally + you have a measured tok/s number. If your Mac has <24 GB, stop here and note "local-on-my-machine not viable; revisit with cloud-GPU or a bigger box."

### A2 · Route vault/autopilot grunt-work to the local model 💰
- **What:** Use Qwen3.6-local as the **cheap tier** for mechanical autopilot chores that currently burn Claude tokens: VTT dedupe, transcript cleanup, filename normalization, bulk summary first-drafts. (opencode local, or Claude Code via LM Studio's endpoint + a thin proxy.)
- **Why:** Direct sibling of the **free-claude-code v60** cost-reduction pilot — proves the "cheap model for cheap tasks" discipline on *your own* workflow before betting it on hireui. Feeds [[local-ai-coding-agents/hardware-economics-and-tco]] break-even math.
- **Effort:** ~1–2 hours wiring. **Risk:** low (quality dips on hard tasks — keep those on Claude).
- **Success signal:** a week of autopilot runs where ≥1 mechanical step ran local with acceptable output; log the token/$ displaced.

### A3 · Local PII-redaction spike (the data-residency proof) 🔒 ⭐
- **What:** Take a **synthetic** CV (never a real candidate's — see fence below) → run it through Qwen3.6 **locally** for (a) PII field extraction and (b) redaction, and prove via network monitoring that **nothing egressed**.
- **Why:** This is the single cleanest demonstration of the topic's killer app for hireui: candidate PII processed with **zero data egress** ([[local-ai-coding-agents/privacy-data-residency]]). It's the concrete artifact you show in a compliance conversation.
- **Effort:** ~2–3 hours. **Risk:** low. **Fence:** synthetic/consented data only; this is a spike, not a candidate-data pipeline.
- **Success signal:** a redacted-CV output + a packet-capture screenshot showing no outbound calls during inference. File as evidence toward the EU-AI-Act/PDPL data-governance leg.

---

## Tier B — hireui first-LLM-feature architecture (the Goal-#2 core)

> All of these run **in the hireui repo under ITS rules** (I-2 `agent-*` branches, I-8 operator-only skills, GitNexus-first, follow the CONSTITUTION). hireui has **no LLM yet** — this is greenfield, so bake it right.

### B1 · Add a LOCAL provider behind the Match-Explain vendor seam 🔒💰 ⭐
- **What:** The planned Match-Explain feature already sits behind a **vendor-abstraction seam** ([[mosh-ai-powered-apps/_index|Mosh A2 pattern]]). Add "**LM Studio localhost (OpenAI-compatible)**" as one concrete provider implementation of that seam — no new abstraction, just a second implementation.
- **Why:** Because LM Studio speaks the OpenAI API, this is a **one-`baseURL`** change behind an interface you're already building. It makes "run this locally" a config flag, not a rewrite — and it's the structural enabler for B2.
- **Effort:** ~half a day (the seam is the pre-req). **Risk:** low — it's additive.
- **Success signal:** the same Match-Explain call runs against either Claude-cloud or Qwen-local by flipping one config value, with a test proving both paths return the seam's contract shape.

### B2 · Tiered routing: "redact local, reason cloud" 🔒💰 ⭐
- **What:** Split the pipeline by **data-sensitivity × difficulty**: **bulk CV parsing / PII detection / redaction → local (Qwen3.6)**; **final nuanced Match-Explain → cloud frontier**, fed only redacted/derived inputs. Route **deterministically in code** (Rule 5 — code routes, model judges).
- **Why:** Best of both worlds — strongest residency on the *raw* PII, best quality on the *hard* reasoning. This is the honest version of Beto's tiering insight, adapted to a regulated domain.
- **Effort:** ~2–3 days (depends on B1). **Risk:** medium — needs the eval set (B3) to prove local quality is good enough for the parse/redact stage.
- **Success signal:** an end-to-end run where a raw CV is parsed+redacted locally and only sanitized text reaches the cloud model; a data-flow diagram you can hand to legal.

### B3 · Recruitment-domain eval set (the gate that keeps you honest) ⭐
- **What:** 50–100 **recruiter-labeled** CV↔job pairs with ground-truth match scores + explanation-quality ratings. Run Qwen3.6-local vs cloud on it.
- **Why:** Every benchmark in the video is **coding-domain (SWE-bench)** — it says *nothing* about CV-matching quality. Local's real quality gap on *your* domain is unknown until you measure it. This is the sibling of the **B1 recruiter-labeled eval set** from [[miai-cv-matching-agent/_index|miai-cv-matching-agent]].
- **Effort:** ~1–2 days to build; reusable forever. **Risk:** low; it's the de-risker.
- **Success signal:** a table: local vs cloud accuracy + explanation quality on the recruitment set. **This gates B1/B2** — if local is close on parse/redact, ship the hybrid; if it's bad even at parsing, keep cloud + redaction-only-local.

### B4 · Local multimodal CV/document parsing 🔒
- **What:** Qwen3.6 **vision**, locally, on resume PDFs→images: extract logos, detect signatures, flag formatting anomalies (light fraud signal). The local sibling of the **A1 CV-parsing / receipt-parsing spike** from [[jasonlee-claude-mobile-app/_index|jasonlee-claude-mobile-app]].
- **Why:** Confirmed that local vision works ([[local-ai-coding-agents/qwen3.6-27b]] C10). Running it locally means **candidate images never hit a cloud vision API** — a strong residency + cost win for a high-volume step.
- **Effort:** ~2–3 days. **Risk:** medium (accuracy vs cloud vision unmeasured — fold into B3's eval).
- **Success signal:** local vision extracts the target fields from a sample corpus at accuracy within an agreed margin of a cloud baseline.

---

## Tier C — Harness & methodology

### C1 · opencode-as-harness bake-off (vs Claude Code + cc-sdd)
- **What:** Evaluate **opencode** — model-agnostic, BYO-provider, subagents, AGENTS.md — as a portable harness for hireui work, against your current Claude Code + cc-sdd setup. Use one real hireui ticket as the shared task.
- **Why:** opencode's `baseURL`-swap makes hybrid local/cloud trivial at the *harness* level, not just the app level. If it holds up, it's a vendor-agnostic option; if not, you've learned the seam is better kept in-app (B1).
- **Effort:** ~1 day. **Risk:** low (evaluation only). **Note:** confirm you're on upstream `sst/opencode`, not a custom fork, before generalizing results.
- **Success signal:** a short write-up: which harness produced a cleaner PR on the same ticket, and whether opencode's local path is production-viable.

### C2 · "Local-first / keys-never-client" ADR into hireui's CLAUDE.md
- **What:** Write a decision record: *when* hireui runs inference local vs cloud (by data-sensitivity × difficulty), plus the standing rule that **keys/PII never reach the client**. Extends the **A5 keys-never-client ADR** from [[jasonlee-claude-mobile-app/_index|jasonlee-claude-mobile-app]] and the **data-residency ADR** from [[agent-memory-architecture/_index|agent-memory-architecture]].
- **Why:** Encodes the tiering decision so future work doesn't re-litigate it or accidentally send raw PII to a cloud API.
- **Effort:** ~2 hours. **Risk:** none.
- **Success signal:** an ADR merged into hireui docs that B1/B2 can cite.

---

## Tier D — Cost & compliance instrumentation

### D1 · hireui TCO / break-even model 💰
- **What:** Compute hireui's real break-even: projected cloud API spend for Match-Explain at scale vs a local box (capex + electricity + ops). Use verified anchors: Q4 ~16.8 GB, break-even ≈ **$80–100/mo** cloud spend, **7–24-mo** hardware payback ([[local-ai-coding-agents/hardware-economics-and-tco]]).
- **Why:** Turns "local feels cheaper" into a number. Feeds the same cost thread as **ccusage → OTEL** ([[claude-code-observability/_index|claude-code-observability]]) and the free-claude-code proxy.
- **Effort:** ~half a day. **Risk:** none.
- **Success signal:** a one-pager: "local pays off above N candidates/month; below that, cloud + redaction is cheaper." A real decision input.

### D2 · EU-AI-Act / PDPL compliance memo (local inference as a data-governance control) 🔒
- **What:** Short memo positioning local (or redact-local-reason-cloud) inference as a concrete **data-governance control** for high-risk-employment AI: no third-party processor on raw PII, no cross-border transfer, internal audit trail. Note the moving deadline (**2026-08-02**, possibly **2027-12-02** via Digital Omnibus) and VN PDPL (in force 2026-01-01).
- **Why:** The regulatory clock is the strongest *business* reason to do this now; the memo makes the compliance value legible to non-engineers.
- **Effort:** ~half a day. **Risk:** none (not legal advice — a technical-control memo for counsel to build on).
- **Success signal:** a memo counsel can react to; a decision on whether compliance urgency justifies pulling B1/B2 forward.

---

## ⚠️ Fences (carry these into any pilot)

- **Real candidate data:** only in the **local, no-egress** path, and only after the B3 eval + D2 memo. Spikes (A3, B4) use **synthetic/consented** data. hireui's CONSTITUTION + I-8 govern.
- **"Free" is capex-deferred, not free** — always pair a local pitch with the D1 number.
- **Don't design around the "sleeping computer" LM Link behavior** ([[local-ai-coding-agents/locally-ai-lm-link]] C9) until verified empirically. The "overnight batch while the Mac sleeps" idea is tempting but **HIGH-RISK / unverified** — parked, not recommended.
- **Local quality is below the benchmark** (4-bit quant vs full model vs 3-gen-old Opus). Gate every "use local here" decision on the B3 eval, not on the video's benchmark chart.

---

## Ranked recommendation

**Do first (this week):** **A3** (local PII-redaction spike) → it's the cheapest, lowest-risk proof of the one thing that actually matters for hireui (data-residency), and it produces a compliance artifact.

**Then (the real Goal-#2 move):** **B1 → B3 → B2**, in that order — add the local provider behind the Match-Explain seam, build the recruitment eval set to *prove* local is good enough for the parse/redact stage, then wire the **"redact local, reason cloud"** hybrid. B3 is the honesty gate; don't ship B2 without it.

**In parallel, cheap:** **D1** (TCO number) + **C2** (ADR) — a half-day each, and they make every other decision legible.

**Watch, don't build yet:** Apple Foundation Models on-device (could remove the hardware capex entirely for recruiter Macs) and LM Link sleep-mode batch (unverified). Revisit at the next `local-ai-coding-agents` refresh.

> **Suggested next action:** run **A1** (30-min viability check on your Mac — do you have ≥24 GB?). If yes, do **A3** this week and open an `agent-*` branch in hireui for **B1**. If your Mac is under 24 GB, jump straight to **D1 + D2** (decide *whether* local is worth a box) before spending on hardware.
