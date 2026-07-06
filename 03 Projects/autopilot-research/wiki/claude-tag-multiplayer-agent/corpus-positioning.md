# Corpus Positioning — What Claude Tag Confirms, Extends, and Contradicts

## 1. The multi-user ToS tension (harness-engineering)

- [[external|Storm Bear: harness-engineering]] harness-economics-and-tos-timeline (as of 2026-07-04): *"Serving OTHER users through your subscription remains clearly prohibited (per-user credits, 'do not ship multi-user apps on plan auth')"*.
- Claude Tag **is Anthropic's own multi-user agent** — but it does **not** violate that line: it ships on **dedicated org billing** (org-funded usage balance, spend caps, launch credits), not on plan-auth reuse. Accurate framing: **Anthropic productized exactly the surface it prohibits customers from building on subscription auth**, and resolved the tension commercially (org metering) rather than by relaxing the ToS. The customer-side prohibition presumably still stands — third parties building Tag-like multi-user Slack agents still need API billing (per-user-credit economics the corpus has tracked). The corpus dive's stronger wording ("Anthropic violates its own ToS") is an **overreach — do not quote**; the critic flagged that current ToS was not re-fetched this pass. Watch-list: re-read the policy page at next harness-economics touch.

## 2. Cowork's app-must-be-open constraint, superseded (claude-cowork)

- [[external|Storm Bear: claude-cowork]] first-party anchor: the app-must-be-open scheduling constraint is *official Anthropic position* for Cowork.
- Claude Tag removes exactly that constraint — Anthropic-hosted ephemeral sandboxes + self-scheduling = the vendor's own answer to the Kenny-Liao-cron-workaround problem tracked there. **The reactive→proactive product axis is now first-party-complete:** Chat/Cowork/Claude Code (open-it-yourself, the video's own framing) → Tag (agent owns the trigger). Cowork wiki needs a cross-link caveat, not a correction: constraint still true *for Cowork*.

## 3. Memory (agent-memory-architecture, claude-code-memory-systems)

- Confirms the corpus headline that production vendor memory is **not vector-RAG**: Tag memory = accumulated explicit instructions in scoped stores (workspace + per-private-channel), admin-curated.
- **CMA link:** the docs place Tag on **Claude Managed Agents** — the same CMA whose Memory Stores + ZDR-ineligibility the memory topic pinned in its 2026-07-04 deepening. Tag's **ZDR-orgs-cannot-use-it** setup rule is independent confirmation of that pin.
- **New species for the taxonomy:** multi-author team memory (channel members co-write standing instructions; admin can restrict). Neither ChatGPT-dossier nor Claude-file-based patterns had *N humans + 1 agent sharing one store*.
- Extends [[external|Storm Bear: claude-code-memory-systems]]'s 6-level taxonomy with a server-side, org-governed L2 variant — no `git diff` auditability; admin UI instead.

## 4. The operator's Telegram stack is a self-built Claude Tag (telegram-remote-control-stack)

Pattern-by-pattern:

| Claude Tag pattern | Operator's stack today |
|---|---|
| Agent reachable in chat | ✅ Telegram channel → Claude Code (Recipe A, pilot-verified 2026-05-08) |
| Long-running async work | ✅ headless loops + background tasks (v189 loop, D16 PR-babysitter) |
| Self-scheduling follow-ups | ✅ CronCreate / ScheduleWakeup / nightly autopilot |
| Persistent instruction memory | ✅ MEMORY.md + memory files (file-based, git-auditable — *stronger* than Tag's admin-UI store) |
| Verification artifacts posted back | ✅/partial — text + files to Telegram; Tag posts videos/screenshots natively |
| Proactive jump-in judgment ("EQ") | ❌ operator's bot only responds when addressed; no ambient monitoring of a group chat |
| **True multiplayer steering** | ❌ single-operator by design (Telegram access policy = allowlist of 1) |

- Claude Tag is **first-party validation of the pattern the operator already runs** — and the two missing rows (ambient proactivity, multi-user steering) are precisely the two that carry the new security surface ([[security-and-governance]]). The corpus dive's "2-year-old stack" phrasing is wrong (piloted 2026-05-08) — corrected here.

## 5. The 65% figure joins the factory-empirics ladder (harness-engineering)

- Corpus ladder of "AI writes most of the code" datapoints: Cherny's Claude-Code-writes-itself (80-90%→100%, self-reported) → Stripe Minions 1,300 AI-PRs/wk (human-reviewed) → StrongDM zero-review factory → TNT's git-audited 100%-agent-commits → **now Tag's 65%-of-product-org PRs via a *chat surface*** (self-reported, three wordings — [[the-65-percent-claim]]). The new axis it adds: the *surface* where PR-shaped work originates moves from IDE/terminal to the conversation layer.

## 6. Convergences worth pattern-tracking (for the next Storm Bear mini-audit)

- **Credentials-never-in-model-context**: Tag's Agent Proxy + Elicit's gateway isolation ([[external|Storm Bear: elicit-verifiable-agent-dsl]]) = independent 2-vendor convergence; candidate observation-track.
- **Fresh-context ⇒ artifact-state**: ephemeral sandboxes + memory/schedule continuity = 4th independent instance (TNT + Archon + Pocock + now Anthropic first-party).
- **Multi-user steering of one agent session**: genuinely new axis at N=1 first-party; watch for OpenAI Workspace Agents / Gemini Spark equivalents to become N=2/N=3 ([[competitive-landscape]]).
- **Proactive-agent-in-chat category emergence**: 4 vendors in ~6 weeks (see [[competitive-landscape]]) — category-formation observation-track.

## Key Takeaways

- Tag **confirms** the corpus' memory + credential-isolation + artifact-state findings; **supersedes** Cowork's trigger constraint; **commercially resolves** (not violates) the multi-user ToS line; **validates** the operator's self-built stack while exposing its two missing capabilities.
- Quote-discipline items for future sessions: never repeat "78% of IT leaders" (corpus-agent confabulation, no source), never say Tag "violates" the ToS, never call the Telegram stack "2 years old."

Cross-links: [[overview]] · [[memory-model]] · [[the-65-percent-claim]] · [[architecture-and-execution-model]] · [[caveats-and-corrections]]
