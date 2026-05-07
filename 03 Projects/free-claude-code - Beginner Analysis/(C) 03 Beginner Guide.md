# free-claude-code — Hướng dẫn cho người mới (Beginner Guide, bilingual)

> **Wiki v60** / **60th LLM Wiki** Storm Bear corpus
> **Subject:** github.com/Alishahryar1/free-claude-code
> **Tagline:** "Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw"

## 1. Nó là gì? / What is it?

**VN:** free-claude-code là một proxy server cục bộ (chạy trên port 8082) đóng vai trò "trung gian" giữa Claude Code (CLI / VS Code / JetBrains / Discord-Telegram bot) và 6 nhà cung cấp model thay thế (NVIDIA NIM / OpenRouter / DeepSeek / LM Studio / llama.cpp / Ollama). Bạn không cần thay đổi cách dùng Claude Code — chỉ cần đặt biến môi trường `ANTHROPIC_BASE_URL=http://localhost:8082` và Claude Code sẽ gửi request qua proxy. Proxy dịch request sang định dạng API của upstream provider, gọi model rẻ hơn (hoặc local), rồi trả response về Claude Code dưới định dạng Anthropic gốc.

**EN:** free-claude-code is a local proxy server (port 8082) that sits between Claude Code clients and 6 alternative model backends. Set `ANTHROPIC_BASE_URL=http://localhost:8082` and Claude Code routes through the proxy, which translates requests to upstream-provider format and translates responses back. **Drop-in:** no Claude Code modification required.

## 2. Corpus-first signals

- **CORPUS-FIRST T4 archetype: api-protocol-translation-proxy.** 9th T4 entrant; distinct from prior 8 (all transform CONTENT; this transforms API PROTOCOL).
- **Pattern #57 57c forward-citation NEW polarity sub-variant: positive-comparison-parallel.** Tagline cites OpenClaw via positive parallel ("...like OpenClaw"). Sister to anti-pattern-foil polarity at v57+v58.
- **Pattern #51 anti-vibe pole streak break.** v60 NEUTRAL after v57+v58 anti-vibe + v59 NEUTRAL. Pattern #51 anti-vibe pole confirmed observational-only (commercial-educator T1 archetype-correlated, not universal).
- **Phase 0.9 STRICT 2-of-4 INCLUDE.** Restarts streak at 1 after v59 broke 41-streak.
- **Pattern #28 multi-provider per-Claude-tier routing sub-variant** — corpus-first per-tier-routing semantics at T4.

## 3. Tier placement

**T4 Agent-as-bridge.** 9th T4 entrant. Mechanism: api-protocol-translation-proxy. Distinct from content-transformation T4 peers (graphify / markitdown / GitNexus / claude-context).

## 4. Cài đặt / Installation

**VN — Yêu cầu:**
- Python 3.14 (cài qua `uv python install 3.14`)
- uv 0.x (cài qua `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Tài khoản tại ít nhất 1 provider (đề xuất: OpenRouter cho cloud + Ollama cho local)

**EN — Requirements:**
- Python 3.14 (install via `uv python install 3.14`)
- uv 0.x (install via curl one-liner)
- API key for at least one provider (recommended: OpenRouter cloud + Ollama local for free tier)

**Quick start:**
```bash
git clone https://github.com/Alishahryar1/free-claude-code
cd free-claude-code
cp .env.example .env  # populate with your provider keys
uv sync
uv run server.py
```

Then in a separate shell where you run Claude Code:
```bash
export ANTHROPIC_BASE_URL=http://localhost:8082
export ANTHROPIC_AUTH_TOKEN=any-string-here  # proxy doesn't validate
claude  # Claude Code CLI now routes through proxy
```

## 5. Core usage pattern

1. **Single-provider mode** — all Claude tiers map to one upstream provider/model
2. **Per-tier routing mode** — Opus → OpenRouter GLM-5; Sonnet → DeepSeek; Haiku → Ollama local
3. **All-local mode** — Opus + Sonnet + Haiku all map to LM Studio / llama.cpp / Ollama models running on your machine
4. **Chat-bot mode** — wrap proxy in Discord/Telegram bot for remote coding-via-chat with optional Whisper voice transcription

## 6. Novel concepts / kiến trúc

- **5 module domains** với encoded import boundaries: `api/` / `providers/` / `messaging/` / `cli/` / `config/` + `core.anthropic` neutral foundation
- **Facade pattern at `api/`** — only imports `providers.base / providers.exceptions / providers.registry` (decouples API layer from internal provider implementations)
- **5 mandatory CI checks** — ruff format / ruff check / ty check / pytest / smoke
- **AGENTS.md = CLAUDE.md sync-discipline** — explicit sync-comment header (corpus-first variant of Pattern #22)
- **architectural-discipline-via-encoded-prose** — PLAN.md enumerates import constraints as readable prose, not just code

## 7. So với các framework khác trong corpus / vs other corpus frameworks

| Subject | Tier | Bridge function | Position vs free-claude-code |
|---|---|---|---|
| graphify v16 | T4 | code → graph index | Content-transformation; orthogonal use case |
| markitdown v28 | T4 | doc → markdown | Content-transformation; orthogonal |
| GitNexus v33 | T4 | repo → graph (incremental) | Content-transformation; orthogonal |
| claude-context v40 | T4 | code → vector index | Content-transformation; STACK-COMPATIBLE (combine for Claude-Code-augmentation pilot) |
| OMC v27 | T1 | OpenClaw-fork harness | Korean fork; FULL agent runtime, not just proxy |
| oh-my-openagent v52 | T1 | OpenClaw-fork harness | Korean fork; FULL agent runtime |
| aidevops v47 | T2 | DevOps multi-provider | Service tier with multi-provider; different scope |

**free-claude-code = unique in being PURE protocol-translation at T4** with no content-transformation.

## 8. Ethical framing / supply-chain awareness

**EN:** Two supply-chain risk surfaces:
1. **Voice transcription** — Whisper API calls (cloud) or local Whisper models. If using cloud, audio data leaves your machine. If using local, ensure model integrity (download from official Whisper releases).
2. **Discord/Telegram bot integration** — bot wrappers route prompts/responses through chat platform infrastructure. Treat Discord-Telegram bot mode as untrusted-user-input surface (bot tokens are credentials).

**VN:** Hai bề mặt rủi ro chuỗi cung ứng (supply-chain):
1. **Phiên âm giọng nói (voice transcription)** — gọi API Whisper hoặc dùng model Whisper local. Nếu dùng cloud, dữ liệu âm thanh rời máy bạn.
2. **Tích hợp Discord/Telegram bot** — wrapper bot đi qua hạ tầng platform chat. Coi bot mode là untrusted-user-input surface; bảo vệ bot token như credential thật.

## 9. Storm Bear relevance — HIGH-OPERATIONAL pilot #3 NEW

**VN:** Đây là pilot tiềm năng số 1 trong tuần này cho vault Storm Bear. Lý do: vault đang chạy Claude Code mỗi ngày để build wiki, và free-claude-code có thể giảm chi phí đáng kể khi route các phase ít quan trọng (như source ingestion verbatim) qua DeepSeek hoặc local Ollama. Setup ~1h. Pilot 1 tuần: đo cost-delta + quality-delta + velocity-delta.

**EN:** Direct-operational pilot for vault. ~1h setup. 1-week pilot to measure cost / quality / velocity delta on wiki-build workflows.

## 10. 4-week learning roadmap

| Tuần / Week | Activity |
|---|---|
| 1 | Read README + AGENTS.md + PLAN.md verbatim. Run quick-start with single-provider OpenRouter. Run 1 wiki-source-ingestion phase through proxy. Compare output. |
| 2 | Configure per-tier routing: Opus → OpenRouter GLM-5 / Sonnet → DeepSeek / Haiku → Ollama. Run 1 full wiki build through proxy. Measure cost + quality. |
| 3 | If quality acceptable: roll out for routine wiki builds. Document quality-degradation thresholds. Build cost dashboard. |
| 4 | Decision: full adoption / partial (specific phases only) / revert. Document in vault `04 Reviews/`. |

## 11. Tradeoffs + limitations

- **Quality risk:** non-Anthropic models may produce lower-quality outputs for nuanced wiki synthesis (entity pages, Phase 5 iteration logs, cross-pattern observations)
- **Maintenance overhead:** solo-community repo with no releases — pin to commit SHA for reproducibility
- **Tool-use semantic-fidelity:** OpenAI-format tool-use ≠ Anthropic-format tool-use exactly; some Claude Code tool-call patterns may translate imperfectly
- **Streaming edge cases:** streaming Anthropic format ↔ streaming OpenAI format requires careful chunk-translation; partial messages may render strangely
- **Local backend hardware:** llama.cpp / Ollama require non-trivial GPU/RAM; local-only mode = capability-limited

## 12. Caveats + safety notes

- License is MIT (commercial-use OK, attribution required)
- 22.1K stars + 3.2K forks suggest mature community despite no formal releases
- 569 commits indicate active development; pin to known-good SHA
- 5 mandatory CI checks suggest engineering discipline; trust contributor reviews
- Voice + bot features = optional; minimal-attack-surface mode = proxy-only without messaging/voice

## 13. References + next action

**References (corpus-internal):**
- claude-howto v32 (T1 VN — Storm Bear pilot #1)
- claude-hud v35 (T1 — Storm Bear pilot #2)
- claude-context v40 (T4 vector search)
- mattpocock-skills v57 (T1 anti-vibe / 57c-anti-pattern-foil polarity)
- OpenSpec v58 (T1 anti-vibe / 57c-anti-pattern-foil polarity)
- AutoGPT v59 (T1+T5 corpus-historical-foundational)

**References (corpus-external):**
- github.com/Alishahryar1/free-claude-code
- AGENTS.md spec (cross-wiki standard, Pattern #22)
- OpenAI Chat Completions API (de facto upstream protocol)
- Anthropic Messages API (Claude Code native protocol)

**Next action / Hành động tiếp theo:**

**VN:** Quyết định pilot deployment trong tuần này. Nếu CÓ — thực hiện 1h setup + 1 tuần đo lường + viết review trong `04 Reviews/`. Nếu KHÔNG — flag để re-evaluate sau v60 mini-audit (sau khi audit xác nhận v60 evidence không có blocking concerns).

**EN:** Decide pilot deployment this week. If YES — 1h setup + 1-week measurement + review note in `04 Reviews/`. If NO — flag for re-evaluation post-v60 mini-audit.
