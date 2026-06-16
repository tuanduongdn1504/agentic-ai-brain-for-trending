# Prompt Caching

> Lever #1 in [[_index]]. The talk: *"If you remember one thing, remember prompt caching."*
> First-party docs: `https://platform.claude.com/docs/en/build-with-claude/prompt-caching` — **all claims below verified first-party.**

## Mechanism

Claude stores the processed **input-token prefix** server-side. On the next request with a byte-identical prefix, those tokens are served from cache instead of reprocessed. As a conversation grows, only the *new* tokens get processed; the rest are cache reads.

The cache is a **prefix match**: any byte change anywhere in the prefix invalidates everything after it. Render order is `tools` → `system` → `messages`, so put stable content first, volatile content last.

## Why it matters (three benefits, all first-party-confirmed)

1. **~90% cost cut on cached input.** Cache reads bill at ~0.1× the base input price. (Cache *writes* cost 1.25× for 5-min TTL, 2× for 1-hour TTL — break-even is ~2 requests at 5-min, ~3 at 1-hour.)
2. **Rate-limit multiplier.** Cached tokens don't count against rate limits. An 80% cache-hit rate ≈ **5× effective rate limit**.
3. **Lower latency.** Fewer tokens to process → faster time-to-first-token, especially on long conversations.

**Target:** >80% hit rate is the ideal for agentic apps. Top customers (talk names Replit, Cursor, Perplexity, Claude Code) reportedly hit 90%+ after deliberate effort. *(Customer figures are speaker anecdote — not independently published; see [[source-provenance]].)*

## The #1 mistake: timestamp in the system prompt

Putting "today's date" (or any per-request value: UUID, request ID, unsorted JSON) into the **system prompt** changes the prefix every request → cache always misses. Keep the system prompt frozen; inject dynamic context later in `messages` (or as a mid-conversation `role:"system"` message on supporting models). Other silent invalidators: changing/reordering tools, switching models, non-deterministic JSON serialization.

## How to apply

- **One-line auto-caching (easiest):** top-level `cache_control: {"type": "ephemeral"}` on `messages.create()` — caches the last cacheable block automatically. The talk's "change one line of code."
- **Manual breakpoints (fine control):** put `cache_control` on the last block of the stable prefix (max 4 breakpoints/request; min cacheable prefix ~4096 tokens on Opus, ~2048 on Sonnet).
- **Use the bundled Claude API skill.** The talk's "Claude API skill in Claude Code" = the `claude-api` skill shipped with Claude Code — it has a prompt-caching audit path (placement patterns + silent-invalidator checklist). Ask Claude Code to "optimize my cache hit rate" and it walks the assembly path.

## Measure it

- **Console:** `console.anthropic.com` → analytics tab (next to cost & usage) shows prompt-caching hit rate. A feature for **cache-miss reasons** (why a cache broke) was launched the day before the talk.
- **Per-response:** check `usage.cache_read_input_tokens` (served from cache, ~0.1×), `usage.cache_creation_input_tokens` (written, ~1.25×), `usage.input_tokens` (full price). If `cache_read_input_tokens` stays 0 across identical-prefix requests, a silent invalidator is at work.

## Key Takeaways

- Highest leverage / lowest effort lever — do this first, even before measuring anything else deeply.
- Freeze the prefix; volatile data goes last. Timestamp-in-system-prompt is the classic killer.
- Verify with `usage.cache_read_input_tokens` — don't assume it's working.

Related: [[context-engineering]] (tool search appends tool schemas to preserve cache; compaction interacts with cached prefixes), [[demo-cost-progression]] (caching halved HeroCorp's cost at ~58% hit rate).
