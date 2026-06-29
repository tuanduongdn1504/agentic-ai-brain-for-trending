# Overview — Omnilogin AI Coding, and the three patterns worth keeping

## Source

[ySEOr1q-Ve4](https://www.youtube.com/watch?v=ySEOr1q-Ve4) (Omnilogin channel, 2026-04-23, Vietnamese, 10:26). Raw transcript: [2026-06-20-omnilogin-ai-coding.md](../../raw/2026-06-20-omnilogin-ai-coding.md). Verified against the originals via workflow `wf_1ac2a814-456` (6-facet research + adversarial verify).

## The 30-second version

**Omnilogin** is an *antidetect browser* (manages many isolated, fingerprint-spoofed browser profiles — used by affiliate marketers, multi-account e-commerce sellers, agencies). Its **new "AI Coding" feature** lets a non-coder type a task in natural language and get back a working browser-automation script. The clever part: the AI generates **three things at once** —

- **Script** — the automation code
- **UI code** — a little config form so a non-coder can paste their own data and re-run it
- **Output** — the run results

…and it's **bring-your-own-model**: you paste `provider type / provider name / Base URL / API key / model name` (+ a thinking toggle). The demo uses **Kimi (Moonshot AI)**. The presenter runs an **iterate-fix loop** (run → check for errors → ask the AI to fix), then scales the finished script across many profiles concurrently.

## Strip the product, keep the patterns

The video is a sales demo for an antidetect browser. Underneath it are **three genuinely useful engineering patterns** — and all three already connect to threads in this vault:

| Pattern | What it is | Already in your vault as |
|---|---|---|
| **BYO-model / OpenAI-compatible config** | `base URL + API key + model name` lets you swap any compatible provider — Kimi, OpenRouter, local Ollama | [[cowork-third-party-inference/_index]] (first-party version) + [[claude-api-cost-optimization/_index]] (the cost lever) |
| **NL → script + *self-config UI* + output** | The agent doesn't just write code, it writes a parameterized form so the artifact is re-runnable by a non-coder (= 2026 "generative UI" / A2UI) | The genuinely *new* idea — closest to [[multi-agent-orchestration/_index]]'s job-screener |
| **Iterate-fix verify loop + prompt discipline** | "Run, check, ask AI to fix" + a HAVE/NEED/STEPS/UI/SAMPLE-DATA prompt template | [[harness-engineering/_index]] validation loops + [[claude-md-12-rules/_index]] Rule 4/9 |

## The decision lens

- **The model (Kimi) is a commodity swap.** It's ~5–8× cheaper than Claude Opus on tokens and OpenAI-compatible, so it's a one-line `base_url` change. Worth a *measured* pilot against Claude on your own tasks — **not** a default switch (Kimi's coding benchmarks are vendor-only and unaudited; practitioners report weaker instruction-following).
- **The "generate the script *and* its config UI" idea is the keeper.** It's the shape of a hireui recruitment-automation feature (Goal #2) and a nice Claude Code skill for your own one-off scripts.
- **Don't adopt Omnilogin.** Adopt its *architecture* in your own Claude-native stack, where you control the keys, the routing, and (for hireui) the candidate data. Pasting your model key into a closed-source desktop app is the one anti-pattern here.

## What the verification corrected (don't repeat the video's claims verbatim)

- **"$39 plan required"** → the $39 is a *consumer* subscription tier (Allegretto). **API access is separate pay-as-you-go** from the platform console — you don't necessarily need the consumer plan. (kimi.com has 5 tiers: free Adagio + 4 paid.)
- **"Disable thinking to cut cost"** → real parameter (`thinking.type: "disabled"`) on K2.5/K2.6, but the **current K2.7-code (June 2026) always thinks and errors if you disable it.** The toggle worked at video time (K2.6 era); use K2.6 if you need that mode.
- **Kimi's coding scores** → no independent SWE-bench; only Moonshot's own benchmarks. Pilot on *your* eval set ([[prompt-evaluation/_index]]).
- **"AI writes the whole script, no code"** → real-world agentic task success is ~62%, not 100%; the video itself shows an iterate-fix loop. Keep the human-in-the-loop verify step.

## Suggested next action

Read [[omnilogin-ai-coding/kimi-moonshot-deep-dive]] for the model/API original, then the [pilot methods](../../output/(C)%202026-06-20-omnilogin-ai-coding-pilot-methods.md) — the top play is a **measured Kimi-vs-Claude codegen bake-off** using your existing `evals/` harness.
