# (C) Pilot methods — Anthropic Memory Stores + Dreaming (2026-07-04 deepening)

> **Source:** [[../wiki/agent-memory-architecture/anthropic-memory-stores-and-dreaming]] (BizMate VN dub → Anthropic "Agents that remember" workshop + docs + repo, adversarially verified).
> **Relationship to the 2026-07-03 menu:** the earlier 24-method menu (`(C) 2026-07-03-agent-memory-architecture-pilot-methods.md`) stands; this menu is the *deepening delta* — methods that only became available/concrete once the first-party mechanics were ground-truthed. Composes with, does not replace.
> **20 methods, 5 angles.** Effort = setup time, not calendar. ⭐ = headline picks.

---

## A — hireui Goal #2 (first LLM feature; no LLM in product yet)

- **A1 ⭐ Data-residency ADR before any memory code** (~30 min, zero install). The deep-dive surfaced a hard fork Anthropic now documents: **CMA memory stores = managed persistence + Dreams, but stateful server-side → NOT ZDR-eligible, no HIPAA BAA**; the **client-side memory tool** (`memory_20250818`) keeps candidate data in your app and stays ZDR-eligible — but you build consolidation yourself. Recruitment SaaS holds PII; write the one-page ADR (per the lazy-ADR pattern) picking the client-side path unless/until CMA exits preview with ZDR. This decision gates every other memory method.
- **A2. Candidate-memory spec, memory-store-shaped** (~1–2h, design only). Steal the *shape* without the platform: per-candidate directory of small focused files (docs: "many small focused files, not a few large ones"; 100KB/2,000-memory discipline), an index file, a store-level description telling the agent what lives there, and per-session usage instructions (the `prompt`/`instructions` lever the workshop called "the lever you'll iterate on"). This extends the 07-03 menu's files-first spec with the four concrete parameters Anthropic actually exposes.
- **A3. Copy the dream-job lifecycle as hireui's consolidation design** (design now, build with the feature). The productized pattern is directly compliance-friendly for recruitment: **explicit trigger → non-destructive output → reviewable diff → human approves → swap → retire old**. A candidate-profile consolidation that a recruiter reviews as a diff before it becomes canonical is a *feature*, not just plumbing. Use a strong model for curation (Letta logic) and cap inputs like dreams do (start 5–10 "sessions" per consolidation).
- **A4 ⭐ `read_only`-by-default constraint line** (~15 min, zero install). The docs' prompt-injection warning is the sharpest new security fact: *untrusted input + writable memory = poisoned trusted memory in later sessions*. Candidate-submitted content is untrusted by definition. Add one line to the hireui agent-harness constraints (beside the existing I-2/I-8 rules): "Agent memory over candidate-supplied content is read-only; writes only from operator-reviewed paths." Sibling of the jsm impersonation-vuln sweep.
- **A5. Hands-on CMA sandbox hour** (~1h + API spend; gated). Submit the research-preview request (claude.com/form/claude-managed-agents), then run `anthropics/cwc-workshops/agents-that-remember` verbatim (`bootstrap.sh` → `ant` CLI → write/recall tests → one dream over ~5 sessions). Cheapest way to evaluate whether managed memory beats build-your-own for hireui's eventual recruitment agent — evidence for the ADR in A1, not a production commitment.
- **A6. Version-trail pattern for candidate memory** (design note, ~30 min). Memory versions (`memver_`, versions outlive deletions, `redact` for compliance, `content_sha256` optimistic concurrency) are a ready-made blueprint for candidate-data audit trails and right-to-erasure workflows. Even client-side, implement: append-only versions + redact-not-delete + hash preconditions on concurrent edits.

## B — this vault + autopilot pipeline

- **B1 ⭐ Teach the vault's consolidation gate the "enrich" verb** (~30 min). The vault's `/consolidate-memory` skill currently compresses/merges/prunes. Dreaming's demonstrated stance is the missing fourth verb: **backfill** — convert relative dates to absolute, add identifiers, add cross-references a *future* session will need ("hard to predict what it might need — write it down; GC later"). Add an enrich pass to the skill prompt. (The 07-03 menu's C1 "name and tune the gate" — this is the concrete tuning.)
- **B2 ⭐ Non-destructive consolidation with diff review** (~30 min). Mirror input→output stores: consolidation writes to a staging copy, `git diff` is the console diff, operator approves, old state retired by the commit. Git makes Anthropic's whole review-then-retire ritual free in this vault — it just needs to become the skill's explicit procedure instead of in-place edits.
- **B3. Dream over the loop-logs** (~1h, quarterly cadence). Dreams take *transcripts* as input, not just the store. Vault equivalent: run a consolidation pass over `loop-log/` (episodic) into a distilled `output/` operations-memory article — merge repeated lessons (the misfire classes!), supersede stale procedures, index the rest. The misfire log in [[../wiki/agent-memory-architecture/source-provenance]] is exactly what a dream would extract.
- **B4. Codify the pin-as-tripwire win** (~15 min). This session, a memory pin (ExamPro/CCA-F) caught a dive agent's confabulation before it entered the wiki — the first observed instance of corpus memory functioning as a fact-check layer. Add one line to the project CLAUDE.md verify discipline: "When a dive claim collides with a memory pin or prior wiki verdict, mandatory main-loop primary fetch before incorporation."
- **B5. Storm Bear queue line** (~5 min). Queue for the v66+ mini-audit: the two-vendor dreaming convergence now has N=2 *mechanism-divergent* instances (OpenAI opaque/continuous vs Anthropic explicit/auditable) + a first-party enrichment-not-compression stance — evidence for the consolidation observation-track, sibling to the files-not-vectors thread.

## C — personal Claude Code harness

- **C1. AutoDream posture check** (~10 min). Multi-third-party reports (still zero official docs) describe feature-flagged auto-consolidation in Claude Code. Don't build on it. Do check whether `/dream` exists in your CLI; either way, keep the manual `/consolidate-memory` cadence as the *reliable* gate — explicit beats undocumented-automatic (the same conclusion the docs' Dreams design embodies).
- **C2. Review-then-retire ritual for auto-memory** (~20 min, then habitual). Before each memory consolidation: snapshot `~/.claude/.../memory/`, consolidate, diff, keep-or-rollback. Same B2 mechanics applied to the personal memory dir (which is not in the vault git).
- **C3. Session-attach instructions as a steering habit** (zero install). The workshop's "lever you'll iterate on" — a per-session memory-usage prompt ("track X, ignore Y, organize as Z") — is portable to CLAUDE.md phrasing for what Claude should write to auto-memory in this project. One sentence per project beats generic memory accumulation.

## D — Scrum coaching / team practice

- **D1. Retro-as-dream-job framing** (next retro, zero prep). The three composable layers map cleanly: sprint = session (ephemeral), team wiki/working-agreements = memory store (persistent, shared, *writable by the team*), retrospective = dream job (reads the sprint's "transcripts", merges duplicates, supersedes stale agreements, backfills missing context, produces a *new* working-agreements version the team reviews as a diff — never edits history in place). The non-destructive + review-the-diff discipline is the part most retros lack; Harvey's ~6x (vendor-reported) is the stakes-anecdote.
- **D2. Memory hygiene as a team norm** (workshop material). "Focused stores per owner/lifecycle, read-only for reference, prune before the cap, index-first retrieval" translates verbatim to team-documentation norms — usable as a 15-minute teaching segment with the workshop video (VN dub available for VN teams via BizMate; pairs with the hoidanit VN junior-onboarding thread).
- **D3. VN community resource line** (~5 min). BizMate localizes the whole CWC course free (Skool, 648 members) — add to the VN onboarding resource list with the attribution-verified/authorization-unverified caveat.

## E — evals / measurement (composes with `evals/` + prompt-evaluation topic)

- **E1 ⭐ The write-test/recall-test eval pattern** (~1h). The workshop's demo IS an eval: session A writes fact F; session B (fresh context, same memory) must recall F. Port to the vault: N seeded facts across sessions → consolidation → recall quiz → score. Run before/after B1+B2 changes to *measure* whether enrich+diff consolidation improves recall — the first quantitative test of the vault's own memory layer.
- **E2. Cache-rate ground-truthing** (if A5 runs). The 95% cache-hit claim is workshop-spoken only. If the CMA sandbox pilot runs, read `usage.cache_read_input_tokens / input_tokens` off the dream resource and publish the measured number in the wiki — converting an unverified vendor number into corpus ground truth for the cost-optimization topic.
- **E3. Consolidation-cost budget line** (~10 min). Dreams bill standard token rates, linear in session count — the same math prices the vault's B3 loop-log consolidation and hireui's A3 job. Add a per-consolidation token budget (Rule 6 discipline) informed by cache-read ≈0.1× pricing.

## Skip-list (deliberate non-actions)

- **Don't adopt CMA for hireui production now** — research preview, gated access, no ZDR/BAA; sandbox only (A5).
- **Don't build on Claude Code AutoDream** — multi-source but unofficial, feature-flagged, could vanish.
- **Don't quote 95% cache / 50% dream-discount as facts** — workshop-spoken/exploratory only (caveats D2/D3).
- **Don't add a vector DB to any of this** — the deepening *strengthened* files-first: Anthropic's flagship memory product is files + grep + index.
- **Index-first retrieval for the vault** — already implemented (`_master-index.md`, MEMORY.md); no action needed, the vendor just validated the design.

## Critic reframe (what would falsify the plan)

The gap between the vault's memory system and Anthropic's productized version is exactly two mechanics — **enrichment** (B1) and **non-destructive diff review** (B2) — plus one measurement (E1). If E1's before/after shows no recall improvement, the vault's current compress-only gate was already sufficient and B1/B2 stay as safety features, not quality features. For hireui, everything routes through A1: if the ADR lands client-side (likely), A3/A6 are design patterns to *implement*, and A5 is optional tourism; if CMA exits preview ZDR-eligible, the build-vs-buy flips.

## Suggested next action

Execute the zero-install headliners this week: **A1** (ADR, 30 min) + **A4** (constraint line, 15 min) + **B1+B2** (consolidation skill retune, ~1h) + **B4** (tripwire line, 15 min), then schedule **E1** as the measurement gate before touching anything else. Submit the **A5** research-preview request today — access latency is the long pole and it costs nothing to queue.
