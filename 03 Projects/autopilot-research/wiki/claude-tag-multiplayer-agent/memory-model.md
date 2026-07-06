# Memory Model

## What the memory is

- **Channel-scoped persistent memory** (workspace-shared across public channels, isolated per private channel — see scoping table) holding standing instructions, scope configuration, and preferences accumulated from **all users in that channel** over time ("remember all the instructions that all the users have given it" — launch video; docs security-and-data).
- Written conversationally: "monitor only for this type of issue" → remembered "for that channel forever after"; anyone in the channel can extend/adjust ("let me expand your scope") — **multi-author memory** is the novel bit vs every memory system previously in this corpus.
- Also stores **self-reminders** (the scheduling half of long-horizon behavior — see [[architecture-and-execution-model]]).

## Scoping & isolation (the part the video omits)

| Boundary | Behavior (first-party) |
|---|---|
| Public channels | **Workspace-shared memory**: public-channel learning is written to a workspace-level store all public channels share ([users/memory docs](https://claude.com/docs/claude-tag/users/memory)) |
| Private channels | **Asymmetric isolation** (verify-CONFIRMED): private channels *read* workspace memory while working, but what they save is written **only to that channel's own store** — private learning never reports out ([how-it-works docs](https://claude.com/docs/claude-tag/concepts/how-it-works)) |
| DMs | Run on the **sender's personal claude.ai account** — outside org admin controls entirely |
| Slack ↔ claude.ai | Conversations not visible across platforms in either direction |
| On disconnect | Conversations auto-delete within 30 days if the integration is disconnected; channel memory persists indefinitely until manually deleted |

## Context mechanics (docs, verify-corrected)

- Message-history window varies by invocation: **20 messages** on a channel mention, **50 messages** on a thread mention (bot replies filtered), **100 messages** when messages are forwarded to Claude — the launch materials never mention these bounds.
- **Standing instructions are channel-wide, not per-user**: editable by channel members by default, and admins can **restrict editing to admins** (Customize docs: "Owner for any scope; channel members for the channel scope") — the video's "all the users" framing is right about authorship, wrong about storage granularity.
- **ZDR incompatibility:** organizations with Zero Data Retention **cannot use Claude Tag at all** (setup docs) — memory + transcript retention is architecturally required. Direct confirmation of the CMA-not-ZDR-eligible pin in [[external|Storm Bear: agent-memory-architecture]].

## Controls

- **Admins** can view, edit, delete channel memory (support 15594475). **No individual-user deletion path** inside shared channels was found — flagged by the security dive as a privacy gap for sensitive discussions.
- Ambient mode (the always-reading behavior that *feeds* memory) is admin-toggleable per channel.

## Against the corpus' memory taxonomy

- On the [[external|Storm Bear: agent-memory-architecture]] map: Tag memory is **explicit-instruction accumulation + admin-curated store** — closest to the file-based `memory_20250818` / MEMORY.md lineage, *not* vector-RAG (consistent with that topic's headline finding that both vendors' production memory systems are non-vector). The distinctive delta is **write-access by multiple humans + one agent** into a shared store, with the org (not the user) as data controller.
- Versus [[external|Storm Bear: claude-code-memory-systems]] 6-level taxonomy: Tag is roughly L2 (curated durable memory) held **server-side per-channel**, with none of the operator-side auditability the vault's file-based approach gives — you inspect it through an admin UI, not `git diff`.
- The "memory took a long time to crack… we tried to get it right for Claude Code for years" line (Boris) is first-party confirmation of the multi-year memory-development arc the corpus tracked through Memory Stores + Dreaming (agent-memory-architecture 2026-07-04 deepening).

## Failure modes to watch (buyer questions, not incidents)

- **Memory poisoning via ambient input**: standing instructions can be written by anyone in the channel — a prompt-injected message that Tag interprets as an instruction persists beyond the message (the Zenity ambient-surface concern applied to the memory layer specifically).
- **Token bloat**: accumulated channel memory rides into every session's context (community concern; no first-party statement on memory-size limits found at ingest).
- **Retention ambiguity**: indefinite-until-deleted default inverts the vault's explicit-consolidation discipline ([[external|Storm Bear: agent-memory-architecture]] consolidation-gate design).

## Key Takeaways

- Claude Tag memory = **shared, multi-author, channel-scoped, admin-governed, server-side** — the first production system in this corpus where a *team* co-authors an agent's persistent memory.
- The isolation story (channel/private/DM boundaries) is strong on paper and entirely absent from the launch video — always read docs, not launches, for memory scoping.
- The open risks are write-path risks (who/what can become a standing instruction), not read-path — the exact inverse of most RAG-era memory worries.

Cross-links: [[architecture-and-execution-model]] · [[security-and-governance]] · [[external|Storm Bear: agent-memory-architecture]] · [[external|Storm Bear: claude-code-memory-systems]]
