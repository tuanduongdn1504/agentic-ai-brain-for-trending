# Original Deep-Dive: Playwright CLI vs MCP for Claude Code QA

## Source

- **MCP:** [github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — npm `@playwright/mcp`.
- **CLI:** [github.com/microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) — npm `@playwright/cli`.
- **Eric's skill (public):** [github.com/EricTechPro/startup-claude-skills](https://github.com/EricTechPro/startup-claude-skills) → `playwright-qa-cli`.
- Verified (`gh api`, 2026-06-29): `playwright-mcp` **34,479★** Apache-2.0 TS (created 2025-03-21); `playwright-cli` **11,670★** Apache-2.0 JS (created 2020-06-19); `startup-claude-skills` **51★** MIT.

## What the video shows

Claude Code drives a real browser to QA the app: a multi-phase test pass (Eric shows ~16 phases), capturing **a screenshot + the console log at every step**, producing a **QA-report table** (per-step screenshots, pass/fail). Then it spins up Superpowers subagents to fix the console-log errors and pushes to main. Both Microsoft tools are official and safe.

## The real CLI-vs-MCP tradeoff (the point of his comparison)

| Dimension | Playwright **MCP** | Playwright **CLI** |
|---|---|---|
| Mechanism | Local MCP server; agent calls **49 tools**; full browser state (a11y tree, screenshots, console, network) streamed **into context every step** | Agent runs shell commands; state saved to **disk** (YAML snapshots w/ element refs, PNGs, console text); agent **reads only what it needs** |
| Schema overhead | High — tools loaded into context (benchmarks: schema injection in the **tens of thousands** of tokens at session start; a draft "~3,600" was a ~10× underestimate) | **~68 tokens** (reads `--help` once) |
| Per-run cost | A widely-cited benchmark: **~114K tokens** for a test flow | **~27K tokens** for the same — **~4× cheaper** |
| Best for | Short, exploratory, high-fidelity QA in isolation | Long test suites, large codebases, cost-sensitive runs |
| Determinism | Tool-call orchestration | Explicit, scriptable, replayable |

The CLI shipped for agent use around Playwright **v1.58 (Jan 2026)** specifically as the "token-efficient alternative". (Exact per-run numbers are third-party benchmarks — directionally solid, not first-party.)

## ⚠️ Correction

The video implies the actual Playwright skill files are **gated** behind Eric's Skool community. **REFUTED** — `EricTechPro/startup-claude-skills` is **public MIT** and ships `playwright-qa-cli` (plus `fix-ticket`, `develop-team`, `review-team`, `review-fix`). Only his broader community/templates are paid.

## Operator relevance (hireui Goal #2)

- **Default to the CLI** for hireui QA automation (cost-discipline; hireui has metered-spend concerns once it gets an LLM) and reserve **MCP** for high-fidelity detail testing (e.g., the Candidate-Detail screen's pixel/Figma-parity check).
- The screenshot-per-step + console-log capture is exactly the evidence trail the **Candidate-Detail refactor spike** needs (Figma-vs-rendered comparison).
- Composes with [[claude-code-observability/_index]] (console/network inspection feeds cost/error analysis) and [[telegram-remote-control-stack/_index]] (Eric runs the QA remotely via the Telegram skill while "stepping outside").

## Install safety

Both are official Microsoft Apache-2.0 packages — no concern. CLI needs Node 18+. Standard `npx`/`mcp add` install.

## Key Takeaways

- Two official Microsoft tools; the **CLI is ~4× more token-efficient** because it writes state to disk instead of streaming it into context.
- Eric's QA skill is **public**, not gated.
- For the operator: CLI-by-default for hireui QA, MCP for detail work; the per-step screenshot+console trail is reusable for Figma-parity verification.

## Related

[[claude-code-skills-stack/original-fix-ticket-marketing-telegram]] · [[claude-api-cost-optimization/_index]] · [[claude-code-observability/_index]] · [[telegram-remote-control-stack/_index]] · [[ai-web-design-workflow/_index]]
