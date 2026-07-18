# (C) LLM Space — Pilot Methods Menu (v221)

**On-goal + directly pilotable.** LLM Space's *author → trace → replay → eval* loop is exactly the discipline the **RATIFIED candidate-LLM legibility ADR** demands (any hireui LLM path affecting a candidate MUST be fixed + legible + audited + human-in-loop + eval/bias-gated), and the vault itself builds agents constantly. So the payoff is **read the discipline + borrow it into your process + use it as the dev-environment when you build hireui's first LLM feature** — not "adopt a ByteDance product wholesale."

⚠️ **Fence (read first):** ⚠️ **NOT source-cloned** → treat the binary/setup as untrusted: `install-snapshot` + read what `mise run setup` does before running it. **Telemetry is opt-out-default-ON** → turn it off. **BytePlus/VolcEngine is the recommended default provider → that egresses your prompts/traces to ByteDance** → BYO your own keys (Claude via the Pi seam) and **never point it at candidate PII** with the default provider. Pin **v4.2.0**.

⭐ **One-thing path: A1 → B5 → D16.**

---

## A — Read & learn (zero install, zero risk)
- **A1 ⭐** Read the five-verb model (Build/Trace/Debug/Evaluate/Manage) and internalize the loop: *author the harness → trace every model-call + tool-run → replay from history → eval across runs*. This is the reference shape for "how to develop an LLM feature responsibly."
- **A2** Read it as a **landscape map** of the agent-dev-workbench category — then place the SaaS incumbents (Langfuse, Phoenix, MLflow, Opik, Braintrust) against it so you know the field before you pick a tool for hireui.
- **A3** Note the **Pi lineage** (built on Mario Zechner's Pi = corpus v36) — if you ever want a *minimal, hackable* agent loop under your own control, Pi is the substrate LLM Space wraps.

## B — Borrow patterns (zero install, highest ROI)
- **B5 ⭐** Lift the **"trace every model-call + tool-run → replay → eval across runs"** discipline into hireui's LLM-feature-development spec **and** the candidate-LLM legibility ADR — specifically the ADR's *eval/bias-gate-OUTSIDE-the-prompt* + *legible/audited* requirements. LLM Space is a working example of what "legible + eval-gated" looks like operationally.
- **B6** Steal the **prompt/tool/model-settings versioning** idea → a small `evals/` + versioned-prompt convention for hireui's first LLM feature (compose with the existing prompt-eval harness + the mosh-ai A2 vendor-seam).
- **B7** Borrow the **replay-from-history** idea for debugging agent runs into the vault's own multi-agent workflows + the loop-engineering v189 loops (a REJECT-first verifier + a replayable trace is the maker/checker pattern).

## C — Hands-on scratch (low-risk trial)
- **C11 ⭐** `install-snapshot` → `bun install` in a **scratch dir** → build a trivial **Pi agent** and drive it through LLM Space's Build→Trace→Replay→Eval loop to prove the workbench works end-to-end. **Telemetry off; BYO key (Claude via Pi); no real data.**
- **C12** Bake-off: run the same toy agent through LLM Space vs a quick Langfuse/Phoenix self-host — decide which trace+eval surface you'd actually want for hireui (desktop-single-user vs server-team).
- **C13** Verify the honest caveats yourself: confirm whether Claude is selectable (via Pi `pi-ai`), whether MCP is truly absent, and what TELEMETRY.md actually sends.

## D — hireui / Goal-#2 (behind the CONSTITUTION fence)
- **D16 ⭐** Use LLM Space (or its discipline) as the **dev-environment when you build hireui's FIRST LLM feature** (Match-Explain / candidate-summariser — the miai-cv-matching thread): author the prompt+tools, **trace + replay + eval it before it ever touches a candidate**, satisfying the candidate-LLM legibility ADR's audit + eval-gate requirements. On an `agent-*` branch, per hireui's CONSTITUTION (I-2 / I-8 / GitNexus-first); no LLM spend yet → design/spec + a scratch eval set.
- **D17** Wire the **eval-across-runs** step into hireui's CI as the bias/quality gate the ADR requires (the gate lives OUTSIDE the prompt). LLM Space is the interactive counterpart; the CI gate is the automated one.
- **D18** ⚠️ If you use LLM Space itself for hireui work: **telemetry off + BYO Claude key + never the BytePlus default + no candidate PII in a traced run** (ByteDance egress). Safer default = borrow the *discipline* (B5/D16), keep hireui's own tooling.

## E — Off-goal / personal
- **E20** Prototype any personal Pi agent (a research helper, a Telegram bot brain) in LLM Space to learn the author→trace→eval loop hands-on — low stakes, no candidate data.

## F — Vault-meta
- **F22** File the v221 §C standalone ("Local-First Desktop Agent-Development Workbench") + its NO-MINT reviewable alternative + the genuine **#57** (llm-space → pi-mono v36) + the **DeerFlow-v9 same-team cross-ref** + the **Electrobun form-factor** data-point for the **~v231 audit**.
- **F23** Add LLM Space to the "agent-dev-workbench vs coding-agent-session-monitor vs protocol-inspector" taxonomy note (llm-space / claude-tap v173 / the v158 observability sub-archetype) — three distinct "see-what-the-agent-does" surfaces.
