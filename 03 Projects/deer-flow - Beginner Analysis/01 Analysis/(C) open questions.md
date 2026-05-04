# (C) Open Questions — deer-flow

> Placeholder. Append findings as wiki build progresses.

## Questions surfaced Phase 0

1. **ByteDance strategic intent** — Why does ByteDance invest in open SuperAgent harness? Related to Doubao LLM / internal agent needs?
2. **v1 vs v2 migration** — v2 rebuilt from scratch. Is v1 abandoned? Migration path for v1 users?
3. **LangGraph dependency** — deer-flow deeply uses LangGraph. Lock-in risk if LangGraph changes direction?
4. **Complementary vs competitive với Claude Code** — README positions complementary (via OAuth + `claude-to-deerflow` skill). But does deer-flow eat Claude Code's lunch for long-horizon tasks?
5. **Multi-channel integration security** — Telegram/Slack/Feishu/WeChat/WeCom = attack surface. Local-trusted-network recommendation acknowledges. Production-ready?
6. **Vietnamese support** — 5 READMEs (fr/ja/ru/zh/en), no Vietnamese. Submit VN translation PR = contribution opportunity.
7. **Vs Devin (Cognition AI)** — Devin commercial + closed; deer-flow open alternative. Feature parity vs Devin?
8. **Sub-agent cost** — parallel sub-agents = cost multiplier on LLM calls. How does deer-flow manage cost control?
9. **Memory persistence implementation** — cross-session memory = what storage? Vector DB? Filesystem? Pluggable?
10. **Skill marketplace emergence** — if Skills framework takes off, does ByteDance host skill marketplace? Community-run?
11. **Storm Bear integration potential** — deer-flow can invoke Claude Code via OAuth. Can Storm Bear vault's `llm-wiki-ingest` skill be ported to deer-flow?
12. **T5 multi-entrant validation** — only deer-flow in T5 currently. 2nd T5 needed to validate tier (candidates: OpenHands, AutoGPT, CrewAI, Agent Zero, Devin OSS alt).
