# How ChatGPT memory actually works (vs the video's account)

## Sources (tiered)

- **T1 vendor**: OpenAI memory announcement/FAQ ([openai.com/index/memory-and-new-controls-for-chatgpt](https://openai.com/index/memory-and-new-controls-for-chatgpt/), help.openai.com Memory FAQ) + the Dreaming pages (openai.com/index/chatgpt-memory-dreaming — fetched by workflow agents; one agent got a 403 and used secondary mirrors).
- **T2 credible teardowns**: Simon Willison, ["I really don't like ChatGPT's new memory dossier"](https://simonwillison.net/2025/May/21/chatgpt-new-memory/) (2025-05-21; **main-loop fetched directly** — section names quoted below are ground truth); Manthan Gupta, [manthanguptaa.in/posts/chatgpt_memory](https://manthanguptaa.in/posts/chatgpt_memory/) (reverse-engineering, 2025–26).
- **T2/T3 press** for Dreaming V3 metrics (TechTimes, opentools.ai, cryptonomist) — vendor-reported numbers relayed by press; flagged as such.

## The verified timeline

- **2024-04**: Memory launches — explicit **Saved memories** (user-visible, editable; stored deliberately: "you either request it or confirm it" — Gupta found 33 facts, all user-confirmed).
- **2024-09-05**: expanded to Free/Plus/Team/Enterprise.
- **2025-04**: **reference chat history** added — the implicit layer (ChatGPT draws on all past chats).
- **2026-06-04**: **"Dreaming V3"** — a rewrite: "a single asynchronous background process now synthesizes memory from many conversations simultaneously, automatically captures context that arises naturally in conversation, and updates existing memories as circumstances change" (e.g. "You're going to Singapore in July" → "You went to Singapore in July 2026"). Vendor-reported metrics via press: time-sensitive accuracy 9.4% → 75.1%; factual recall 41.5% (2024) → 82.8%; preference adherence → 71.3%; ~5× compute efficiency. **Not independently audited.**

## The mechanism (the load-bearing correction)

- Willison (fetched directly): "it looks like this is yet another **system prompt hack**. ChatGPT effectively maintains a detailed summary of your previous conversations, updating it frequently with new details. **The summary then gets injected into the context every time you start a new chat.**"
- The injected dossier's four sections (Willison, exact names): **Assistant Response Preferences**, **Notable Past Conversation Topic Highlights**, **Helpful User Insights**, **User Interaction Metadata**.
- Gupta's four-layer architecture (independent teardown, consistent): Session Metadata (device/subscription/usage, injected once per session) + User Memory (explicit facts) + Recent Conversations Summary (timestamped digests) + Current Session Messages. His flat statement: **"No vector databases. No RAG over conversation history."** — "ChatGPT trades detailed context for speed and efficiency by **pre-computing summaries** instead of running similarity searches on past messages."

## Grading the video

| Video claim | Verdict |
|---|---|
| Memories are short, editable, constantly updated | ✅ CONFIRMED (Saved memories UI + periodic dossier regeneration) |
| A consolidation process distills chats into durable facts | ✅ CONFIRMED in spirit — Dreaming V3 IS background consolidation |
| Trigger = after N conversations | ❌ Dreaming V3 is **continuous/async**, no disclosed count threshold |
| A *cheaper* summarizer model does it | ❓ UNVERIFIABLE — OpenAI discloses no model assignment |
| Storage = vector store, retrieval = RAG top-k | ❌ REFUTED by both teardowns — pre-computed summaries injected wholesale |

- Caveat on the teardowns themselves: the four-layer/dossier structure is **inferred from behavior + prompt extraction**, not OpenAI documentation — high-quality but still reverse-engineering; and it describes the pre-V3 system, with Dreaming V3's internals undisclosed.

## Key Takeaways

- ChatGPT memory is **summary-injection, not retrieval**: the whole dossier rides into every new chat. That's why it's fast, why it's short, and why Willison's complaint is loss of *context control* — everything comes along whether relevant or not.
- The video gets the *product behavior* right and the *mechanism* wrong — the exact gap between using a system and building one.
- Design lesson for [[consolidation-gate-design]]: OpenAI chose deterministic injection over probabilistic retrieval for assistant memory — when your consolidated state is small enough to always include, **skip retrieval entirely**.
