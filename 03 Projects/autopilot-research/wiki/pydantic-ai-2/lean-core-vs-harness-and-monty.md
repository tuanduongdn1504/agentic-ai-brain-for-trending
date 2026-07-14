# Lean core vs. harness, and the Monty sandbox

## The two-layer split (CORRECT_BUT_INCOMPLETE)

Cole describes two lanes of capability: a **"lean core"** — capabilities Pydantic AI considers fundamental to nearly every agent (he names thinking, web search, tool search) — and a **"harness"** — capabilities Pydantic wants to support but doesn't consider critical for most agents (his example: code mode / sandboxed execution).

The launch article confirms this split in its own words:
- Core: *"the loop, the providers, the capability and hooks API, and only the capabilities that need deep provider support or are fundamental to every agent."*
- Harness: *"memory, guardrails, context management, file system access, code mode, and more"* — where the framework "can move fast."

What the article does **not** do is enumerate "thinking, web search, tool search" by name as the core set — it states the *selection principle* rather than a fixed list, and the separate capabilities reference docs don't use "core" vs "harness" as an organizing heading at all. The split is real; the specific three-item core list is Cole's own reading of it, not a quoted taxonomy.

## Monty — real, but shipped as a separate package (resolved contradiction)

Cole's claim: Pydantic (the company) is building its own lightweight open-source sandbox, "Monty," for the harness's code-mode capability.

**This checked out, with one wrinkle worth recording precisely** because the workflow's own completeness critic flagged a contradiction in the first pass, and it was worth resolving before publishing rather than leaving two verifier notes in tension (project discipline: fail loud, don't paper over a contradiction).

- **Monty is real:** [github.com/pydantic/monty](https://github.com/pydantic/monty), MIT license (copyright Pydantic Services Inc.), a minimal Python interpreter written in Rust "for use by AI" — full host isolation (filesystem/env/network blocked), resource limits, sub-microsecond startup, snapshottable state. Confirmed the *only* project called Monty in the Pydantic ecosystem (i.e., not confused with an unrelated same-named project).
- **The wrinkle:** Monty's own README still reads "will (soon) be used to implement codemode in Pydantic AI" — future tense — and code-mode is not in core `pydantic-ai` v2.0.0's dependency list. A first pass read this as "not actually shipped yet," in tension with a second finding that a separate package already markets it as shipped.
- **Resolution (main-loop follow-up, 2026-07-14):** Code mode ships via a **separate package**, [`pydantic-ai-harness`](https://github.com/pydantic/pydantic-ai-harness) — "the official capability library for Pydantic AI" — at version **0.6.0, released 2026-07-09** (one day before this video went up). Its capability matrix marks Code Mode ✅ shipped and documented: *"Sandboxed Python execution via Monty — one `run_code` call replaces N tool calls."* Monty's own README is simply stale relative to the harness package's release, not evidence the feature is vaporware.

This actually **fits Cole's own model perfectly**, even though he doesn't say it explicitly: code mode is a harness capability by his own two-layer framing, and it ships in a package literally named `pydantic-ai-harness` rather than bundled into core `pydantic-ai`. The "harness" is architecturally a separate, faster-moving package — not just a conceptual category.

## Takeaway

Verdict stands at CORRECT_BUT_INCOMPLETE rather than escalating to MISLEADING: Monty is real, open source, Pydantic-owned, and does power code mode — the video just doesn't mention that "harness" capabilities literally live in a separately-versioned pip package, which is the more precise (and more interesting) fact underneath the two-layer story he tells.
