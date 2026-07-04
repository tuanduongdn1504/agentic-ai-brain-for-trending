# Anthropic Memory Stores + Dreaming — the first-party deep treatment

> **Added 2026-07-04** (deepening pass): full workshop + docs + repo treatment of Anthropic memory surface #3 from [[how-claude-memory-works]]. This is the production consolidation agent both prior articles pointed at, now specified end-to-end.

## Sources

- **Video (VN dub, operator-submitted):** [Anthropic giới thiệu Dreaming: Tự động tổ chức và làm giàu bộ nhớ cho Agent AI](https://www.youtube.com/watch?v=b1qgIGwBUEI) (BizMate AI Official, 2026-06-30, 28:34, 1,467 views, 7,320 subs) — attributed dub, read in full
- **Video (EN original):** [Agents that remember](https://www.youtube.com/watch?v=geUv4CjPpxI) (official **Claude** channel, 472K subs, published 2026-05-23, 28:42, ~22K views) — speaker "Kevin, an engineer at Anthropic" (= **Kevin Chen, Member of Technical Staff**, per the London Extended session listing) — read in full
- **Docs (fetched in full 2026-07-04):** [managed-agents/memory](https://platform.claude.com/docs/en/managed-agents/memory) + [managed-agents/dreams](https://platform.claude.com/docs/en/managed-agents/dreams) + [managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)
- **Workshop repo:** [anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops) (Apache-2.0, created 2026-05-06, 1,280★/394 forks) — `agents-that-remember/` README + `bootstrap.sh` fetched in full
- **Official announcements:** claude.com/blog `new-in-claude-managed-agents` (2026-05-06, incl. the Harvey quote) + `code-w-claude-sf-2026-sf` recap (2026-05-12)
- Raw transcripts: `raw/2026-07-04-anthropic-dreaming-memory-stores.md`
- Verification: Workflow `wf_c3719baa-7f2` + main-loop ground-checks — see [[source-provenance]]

## The provenance chain

Code with Claude 2026 **SF, single day 2026-05-06** (+ "Extended" day May 7 added by demand) → Dreaming announced as one of **four new Managed Agents features** (Dreaming, Multiagent orchestration, Outcomes, Webhooks) alongside doubled Claude Code rate limits and raised Opus API limits → the 45-minute **"Agents that remember" workshop (W3)** delivered at the Extended events (SF-Ext May 7 "with Tina" per the repo's seed data; **London Ext 2026-05-20, Kevin Chen**; Tokyo Ext 2026-06-11, Sam Jiang) → recorded delivery published on the Claude channel 2026-05-23 (**venue CONFIRMED London 2026-07-04**: official session page `claude.com/code-with-claude/session/ldn-ext-agents-that-remember` lists Kevin Chen 12:00–12:45, and the `san-francisco-extended` page shows the SF-Ext May 7 instance was taught by **Tina Vachovsky** — resolving the repo seed data's "with Tina"; 2-lens verified during the [[../elicit-verifiable-agent-dsl/_index|elicit-verifiable-agent-dsl]] pass, which covers the *same London event* as James Brady's DSL talk) → BizMate VN dub 2026-06-30. Second VN licensed-dub-style chain in the corpus after [[../google-zero-open-web/_index]] — here attribution is explicit but authorization is unverified.

## Platform context (what this sits on)

**Claude Managed Agents (CMA)** = "pre-built, configurable agent harness that runs in managed infrastructure" — Anthropic's alternative to the raw Messages API for long-running/async work. Four concepts: **agent** (model + system prompt + tools + MCP + skills), **environment** (cloud or self-hosted sandbox), **session** (running instance), **events** (SSE-streamed messages). Status: **beta, enabled by default for all API accounts** (`managed-agents-2026-04-01` header); within it, **dreaming (+ MCP tunnels) is a gated research preview** — request access via claude.com/form/claude-managed-agents; dreams add the `dreaming-2026-04-21` beta header.

⚠️ **Production caveat:** CMA is stateful server-side by design → **not ZDR-eligible, no HIPAA BAA** (docs, fetched 2026-07-04). The client-side API memory tool (surface #2 in [[how-claude-memory-works]]) remains the ZDR-eligible option — a real fork in the hireui design decision.

## Memory stores — the hard numbers the video omits

| Parameter | Value (docs 2026-07-04) |
|---|---|
| Per-memory size | **100 KB (~25K tokens)** |
| Memories per store | **2,000** (writes fail beyond; reads still work) |
| Stores per session | **8** |
| Mount path | `/mnt/memory/<slugified-name>/` — read the authoritative `mount_path` field, don't construct |
| Attach time | **Session creation only** — no attach/detach on a running session |
| Access | `read_write` (default) / `read_only` — **enforced at filesystem level** |
| Per-attach `instructions` | ≤ 4,096 chars, injected into system prompt |
| Versioning | Every mutation → immutable `memver_…`; versions outlive deleted memories; **30-day retention** (recent versions kept longer); `redact` endpoint for compliance; `content_sha256` precondition for optimistic concurrency |

- The agent reads/writes the mount with the **standard file toolset** (`agent_toolset_20260401` in the workshop bootstrap) — bash, grep, file reads. A mount note (name, path, access, description, instructions) is auto-added to the system prompt. Writes outside the mount path land in container scratch and die with the session.
- **Store scoping is your product decision** — per user / per team / per project; docs recommend focused stores over one mega-store (each gets its own 2,000 cap).
- ⚠️ **Prompt-injection warning (docs, not in the video):** a `read_write` store + untrusted input = an injection can write malicious content that **later sessions read as trusted memory**. Use `read_only` for reference stores. This is the persistent-memory attack surface the jsm-practical-vibe-coding impersonation-vuln thread predicted.

## Dreaming — mechanics

**A dream is an explicit async job** (`POST /v1/dreams`): inputs = one memory store + **1–100 sessions**; optional `instructions` ≤ 4,096 chars; model ∈ {`claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-4-6`}. Output = a **separate** memory store (`outputs[]` once `running`). Lifecycle: `pending → running → completed | failed | canceled`; cancel + archive endpoints; list with pagination.

- **Non-destructive by contract:** "The input store is never modified." On `failed`/`canceled` the **output store persists with partial contents** — inspect, then clean up yourself (no auto-rollback). Deleting an input store/session mid-run fails the dream (`input_memory_store_unavailable` / `input_session_unavailable`); the output store can't be deleted while running (400).
- **Dogfooding = observability:** the dream's `session_id` points at the CMA session executing the pipeline — stream its events live, transcript archived (not deleted) after terminal state. The workshop demoed clicking into the dream session and reading its prompt + sub-agent activity.
- **`instructions` is a synthesis steerer, not an editor** (docs nuance beyond the video): focus areas, preservation rules, output conventions work; line-level imperatives ("change sentence X to Y") "generally produce no change" — for targeted edits use the Memory Stores API on the output store.
- **Billing:** standard API token rates for the chosen model; `usage` reports exact totals; "cost scales roughly linearly with the number and length of input sessions. Start with a small batch."
- **Duration:** docs "minutes to tens of minutes"; the workshop said "a couple minutes to hours" — see [[caveats-and-corrections]] (docs likely current; workshop upper bound stale or conservative).
- Model dates ground-truthed: Sonnet 4.6 **2026-02-17**, Opus 4.7 **2026-04-16**, Opus 4.8 **2026-05-28** — the video (pre-4.8) correctly offered only 4.7/4.6; docs added 4.8 later.

## What only the workshop teaches (not in docs)

- **Harness internals:** dreaming is a multi-agent pipeline — an **orchestrator spawns one sub-agent per input session transcript**, each with its own system prompt; "we actually kind of want Dreaming to be **exhaustive by design**… if you give it 100 chances, you want to make sure Claude is looking over all the information." (Workshop-spoken; not doc-specified — could change.)
- **Index-file generation (demo-observed, NOT doc-guaranteed):** the dream created an `index` file of slugs referencing memory files "so future agents… quickly grok what to look for **instead of a wider grep**" — plus an event-logistics file and reformatted originals (slug + description + metadata). This is exactly the MEMORY.md / `_master-index.md` pattern this vault runs.
- **The enrichment stance — write more, GC later:** "while an agent's working on a task, it's kind of hard to predict what it might need down the line… it's actually good to write additional details down… Dreaming can always go back and remove stuff that is no longer needed." Consolidation here **adds** detail (backfills dates, identifiers) as much as it compresses — a materially different philosophy from summarize-and-shrink.
- **Cost economics (workshop-spoken only, in ZERO written sources):** expected **~95% prompt-cache hit rate** on most dream sessions ("most of the processing is agentic… most of the tokens are actually cached"); Anthropic is "**exploring**" batch-API-style **~50% discounts** via off-peak scheduling + other levers (model switch, prompt steering, token budgets). The Batch API 50% discount itself is real and documented; a dreaming discount has NOT shipped as of 2026-07-04.
- **Review-then-retire ritual:** console shows a **snapshotted diff** of what the dream changed (repo README: "snapshotted comparison" + live store-vs-store comparison) → human-in-the-loop review → attach output store to new sessions → optionally `archive` the old store.
- **The three-layer mental model:** session (ephemeral, isolated) → memory store (connect information across sessions) → dreaming (organize/enrich/improve over time so memory "stays at a reasonable level… doesn't blow up," with staleness checks). Repo README's spectrum: "**cheap, live ◀▶ batch, distilled**."

## The workshop repo (the hands-on original)

[anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops) — Apache-2.0, created on event day, "sample code, not maintained." **Eight workshops**: agent-battle, agent-decomposition, **agents-that-remember**, eval-driven-agent-development, **how-we-claude-code** (companion to [[../how-we-claude-code/_index]] — cross-topic find), production-ready-agent, research-desk, rightmodel, ship-your-first-managed-agent.

`agents-that-remember/` = README (full CLI + Console ritual) + `bootstrap.sh` (downloads the **preview `ant` CLI** from a Stainless bundle; creates `cwc-agent` (opus-4-7) + `cwc-env` (cloud) + 3 seeded history sessions). Key commands, runnable today with research-preview access:

```bash
ant beta:memory-stores create --name "cwc-memory" --description "…"
ant beta:sessions create --agent $AGENT --environment-id $ENV \
  --resource '{"type":"memory_store","memory_store_id":"…","prompt":"…","access":"read_write"}'
ant beta:dreams create --model claude-opus-4-7 \
  --input '{"type":"memory_store","memory_store_id":"…"}' \
  --input '{"type":"sessions","session_ids":[…]}' \
  --instructions "I am attending CwC, and I want to remember what I've learned."
ant beta:memory-stores archive --memory-store-id $OLD   # retire after review
```

## Reception + framing split

- **Harvey (legal AI):** "Completion rates went up **~6x** in their tests" — verbatim from Anthropic's own blog (2026-05-06). **Vendor-reported, no independent audit**; treat like OpenAI's Dreaming-V3 9.4→75.1% ([[how-chatgpt-memory-works]]).
- **Press vs vendor framing:** press leaned hard on the **hippocampal / sleep-consolidation metaphor** (letsdatascience, mindstudio, buildfastwithai); Anthropic's own announcement used technical framing ("a scheduled process that reviews past agent sessions, surfaces patterns, and curates memory") — no sleep metaphor. The cog-sci lineage in [[memory-taxonomy-and-cogsci-lineage]] is the press's projection as much as the vendor's.
- **"Scheduled" vs explicit (Rule 7 conflict, surfaced not averaged):** even Anthropic's recap calls Dreaming "a scheduled process," and press describes automatic frequency controls — but the **documented API is explicit-invocation only** (create + poll; no scheduler endpoint in the dreams docs). CMA does have separate cron **scheduled deployments** for sessions. Read "scheduled" as the intended usage pattern (you cron the dream), not an API property. Docs win mechanically.

## Convergence significance (updates the topic thesis)

The 2026 two-vendor dream convergence in [[overview]] now has its full first-party half: OpenAI **Dreaming V3** (2026-06-04, consumer, continuous background, opaque) vs Anthropic **Dreaming** (2026-05-06, developer platform, explicit API, observable session, reviewable diff, non-destructive). Same verb, opposite control models — Anthropic productized the **auditable** version of the [[memgpt-letta-sleep-time]] sleep-time pattern, with Generative-Agents-style enrichment ([[generative-agents-reflection]]) rather than pure compression. And the output artifact (index file + focused files + supersession) is structurally the Karpathy LLM-Wiki pattern this vault runs — see [[consolidation-gate-design]] for where it slots in the trigger/model/operation design space.

## Key Takeaways

- **Memory stores are literally the vault pattern as a managed product**: files + grep + index + explicit consolidation + versioned audit trail. Zero vectors, again.
- **Dreams = consolidation with a paper trail**: non-destructive input→output stores, an observable pipeline session, a reviewable diff, and manual retirement — the productized version of this vault's `consolidate-memory` skill, with the same verbs (merge, supersede, surface) plus one this vault lacks: **enrich/backfill**.
- **The real design fork for builders (hireui):** CMA memory buys persistence + Dreams but costs server-side state (no ZDR); the client-side memory tool keeps data in your app (ZDR-eligible) but you build consolidation yourself. Decide on data-residency first, mechanics second.
- **Budget reality:** dreaming is exhaustive by design (1 sub-agent per transcript), billed at standard rates, cache-friendly (~95% claimed, unwritten); start with ~5–10 sessions per dream and review the diff before trusting output stores.
- **Version discipline:** 2,000-memory cap + 30-day version retention + read-only mounts for untrusted-input sessions are the three operational numbers that will bite first.
