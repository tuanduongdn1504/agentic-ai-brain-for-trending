# Vision Agents (GetStream) — deep-dive of the original resource

## Source

- `gh api repos/GetStream/Vision-Agents` (2026-07-03, main-loop ground-check) + visionagents.ai + repo README + the shipped `vision-agent/` service in react-native-lingua; adversarially verified via workflow wf_5993da5f-31c.

## Verified repo facts (2026-07-03)

- **GetStream/Vision-Agents** — "Open Vision Agents by Stream. Build voice and vision agents quickly with any model or video provider. Uses Stream's edge network for ultra-low latency."
- **Apache-2.0**, Python (100%), **7,959★ / 662 forks**, created **2025-08-11**, actively maintained (pushed 2026-07-03), latest release **v0.6.6 (2026-07-01)**, homepage visionagents.ai.
- Python ≥3.10 (framework); install `uv add vision-agents` / pip; scaffold via `uvx vision-agents init`. Extras select providers: the video's service uses `vision-agents[getstream,openai]`.
- Integrations (README): **Realtime** = OpenAI Realtime, Gemini Live, AWS Nova Sonic, Qwen, Inworld; LLMs incl. OpenAI, Gemini, Anthropic, xAI, OpenRouter, HF, Kimi, MiniMax; STT/TTS (Deepgram, ElevenLabs…); video processors (YOLO, Roboflow); avatars; **MCP tool calling**; RAG (TurboPuffer, Qdrant, Gemini FileSearch); phone via Twilio/Telnyx; production guides (HTTP server, Prometheus, Kubernetes, Redis scaling). "35+ integrations" per site.
- ⚠️ **Claude has no realtime plugin** — anthropic plugin exists but no `realtime.py` (verified by plugin-tree inspection); Claude rides the standard message API path only.

## The three-layer architecture (as built in the video)

1. **Expo app** — the UI; joins calls with Stream's React Native Video SDK (`@stream-io/video-react-native-sdk`).
2. **Stream edge network** — commercial transport: calls, audio infra, tokens, custom call metadata. (Marketing latency figures — ~500ms join / <30ms — are vendor claims, not independent benchmarks.)
3. **`vision-agent/` Python service** — the AI participant that joins the call: ~200 lines, `Agent(edge=getstream.Edge(), llm=openai.Realtime(...), instructions=...)` + `AgentLauncher`. Lesson context arrives via **Stream call custom data** (call_id convention `lesson-{lang}-lesson-{n}-{userId}`).

**Verifier-conflict resolution (Rule 7):** one workflow verifier "CONFIRMED" Vision Agents is "available for React Native" from the README's SDK line — that line refers to **Stream's client SDKs**. The agent framework itself is Python-only; RN apps *participate in calls* the agent joins. The video's own architecture (and Adrian's "runs as its own Python service" explanation, 02:47–02:49) is correct; the "no Python needed — that's the beauty of agentic development" pitch means the AI writes it for you.

## Production prompt patterns worth stealing (from the shipped main.py)

- **Two-mode system prompt** — TEACHING MODE (say word + meaning + tip, end with ONE question, "your turn is OVER at that question mark") vs REACTING MODE (react only to actual student speech). ABSOLUTE RULES: *never praise unless the student actually spoke this turn; never continue past a question mark; never role-play the student's response; 1–2 short sentences; stay in-lesson.* — engineered against realtime-voice failure modes: self-conversation, imagined user responses, monologuing. (The video's "AI teacher improvements" lesson shows exactly these failures before the fix.)
- **Tuned server-VAD** — `server_vad(threshold=0.4, prefix_padding_ms=200, silence_duration_ms=400, interrupt_response=True)` with inline reasoning: energy-based VAD fires ~100ms after mic opens vs ~500ms+ for semantic detection, so the agent shuts up the instant the push-to-talk mic opens.
- **Transcription** — `gpt-4o-mini-transcribe` on input audio; agent+user transcription events power the app's live captions.
- **`_require_env` fail-fast** on missing env vars — the CodeRabbit-demanded fix, now shipped ([[verification-and-review]]).

## Open-source nuance

- Framework: genuinely Apache-2.0, no license trap. **But** every shipped example uses `getstream.Edge()` (commercial, credentialed); "works with any video edge network" has no shipped counter-example; self-host story unverified. Practical read: **open framework, commercial transport** — free tiers exist (Stream Maker plan; see [[stack-and-sponsors]]).
- Sponsor context: Stream sponsored the video; Vision Agents got the largest single share of runtime. The tech verified real regardless.

## Key Takeaways

- Vision Agents is a real, active, provider-agnostic Python framework for realtime voice/video agents — the "any model" claim holds (30+ providers), the "any edge" claim is unproven.
- The agent-as-call-participant model (agent joins the same WebRTC room as the user) is the load-bearing architecture idea — transferable to interview practice, support, coaching agents.
- The two-mode/hard-stop prompt + aggressive VAD tuning are the transferable hard-won details — they encode "don't talk over the student and don't imagine their answers" mechanically.
- Pass app→agent context through call custom data, not prompt-stuffing.
- Related: [[multi-agent-orchestration/_index|multi-agent-orchestration]] (agent architectures), [[ai-engineering/_index|ai-engineering]] (Ch.6 agents), [[cowork-third-party-inference]] (provider-agnostic BYO-model).
