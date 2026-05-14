# Codex — Gaps & Follow-ups

> **Topic:** [[_index|codex]]
> **Source:** `../../raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md` § Gaps

What the 6-video bundle did NOT cover. The bundle is solid on **individual-developer** workflows but has significant blind spots at **team scale**, **enterprise production**, and **observability**. These are open questions for the next research cycle.

---

## Team-scale collaboration gaps

### Multi-developer agent orchestration

The sources extensively discuss **git worktrees and parallel threads for a single developer** [Source 1, Source 3], but **never address a team of 10-20 engineers running agents simultaneously** [Source 2, Source 6].

**Open questions:**
- How do you handle **merge conflicts between multiple agents** owned by different humans?
- What's the workflow when two devs' Codex sessions touch the same files?
- Is there a "lock" or "claim" primitive?

**Follow-up search:** "team workflow Codex Claude Code", "multi-developer agentic coding", "agent merge conflict resolution"

### Shared project memory

`agents.md` and `claude.md` are described as **local files** [Source 1, Source 4, Source 5]. **Open question:** how does a distributed team maintain a shared, evolving memory file?

- Version-controlled in git is the obvious answer, but the bundle never says this explicitly
- What about **per-developer overrides** vs **team-shared baseline**?
- How does Keith AI's automated `agents.md`-update loop [Source 1] interact with PR-based review of memory file changes?

**Follow-up search:** "claude.md team workflow", "agents.md shared memory git", "centralized agent memory knowledge base"

---

## Enterprise / production gaps

### Granular IAM (Identity and Access Management)

The bundle treats sandbox-vs-full-access as **binary** [Source 3]. Production needs:
- **Specific protocols for what an agent can access** in AWS/Azure environments
- **Secret management** — how does Codex/Claude handle credentials?
- **Prompt injection defense** — how do you prevent privilege escalation through prompt injection?

**Follow-up search:** "Codex enterprise IAM", "Claude Code agent permissions production", "agent prompt injection security"

### Data residency and compliance

The sources don't cover how to ensure tokens sent to Anthropic / OpenAI APIs comply with:
- **GDPR** — EU data residency
- **SOC2** — security/availability controls
- **HIPAA** — healthcare data
- Web-search tools introducing arbitrary outbound queries in regulated environments

**Follow-up search:** "Codex GDPR compliance", "Claude Code HIPAA", "agentic coding data residency", "PII redaction LLM tools"

### Automated quality gates (CI/CD)

Mosh emphasizes **human review of every line** [Source 5] and The AI Automators describe **adversarial evaluation** [Source 2]. **Gap:** in a high-velocity production environment, you need **automated, deterministic gates** — CI/CD triggers that block agent-generated code if it fails security scans or integration tests, without requiring a human to "approve" every step.

**Follow-up search:** "Stripe minion architecture", "deterministic CI gates AI code", "automated quality gates agentic"

---

## Observability gaps

### Structured logging and monitoring

The videos show **"spinny circles"** and visible todo lists [Source 2, Source 3]. **Gap:** for production systems you need:
- **Asynchronous logging** of every agent action
- **Performance monitoring** — success rates, latency, "context anxiety" behaviors
- **Cost-per-feature tracking** across thousands of sessions

**Follow-up search:** "LangSmith agentic coding", "Arize Phoenix Claude Code", "agent observability platforms"

### Multi-step decision auditing

When an agent "talks itself into" approving mediocre work [Source 2], you need to be able to **audit why** — what reasoning path led to the approval. The bundle does not address agent-decision traceability tools.

**Follow-up search:** "agent decision audit trace", "multi-step LLM reasoning audit", "agent reasoning explainability"

---

## Cost optimization gaps

### Token caching strategies

The sources advise **checking weekly usage** [Source 5] but don't go deeper. **Gap:**
- **Prompt caching** — Anthropic and OpenAI both support it; the bundle barely mentions it
- **Model routing** — cheap models for mechanical tasks (linting, formatting) and expensive models reserved for complex planning [Source 6 implies this via three-brain routing but doesn't quantify]
- **Distillation** — using cheaper models trained on outputs from more expensive ones

**Follow-up search:** "Claude prompt caching", "OpenAI Codex token caching", "agentic cost optimization", "model distillation coding tasks"

### Per-feature cost tracking

Useful for budgeting and ROI conversations. The bundle has no examples of teams tracking **cost per feature shipped** vs traditional dev time. This is the metric that wins enterprise approval, and it's absent.

**Follow-up search:** "AI coding cost per feature", "Claude Code ROI tracking", "agentic dev cost benchmarks"

---

## Codex-specific blind spots

### Codex hook equivalent

Claude Code has explicit **hooks** (see `[[../claude-code-hooks/_index]]`) — deterministic shell commands fired on lifecycle events. **Open question:** does Codex have an equivalent? The bundle never discusses Codex's lifecycle event model in this depth.

**Follow-up search:** "Codex CLI hooks", "Codex lifecycle events", "Codex pre-tool post-tool"

### Codex-vs-Claude head-to-head benchmark

The bundle is **all qualitative**. No source provides:
- Side-by-side **benchmark on the same task**
- **Latency comparison**
- **Cost per equivalent task**
- **Failure mode taxonomy**

This is the single largest evidence gap in the bundle.

**Follow-up search:** "Codex vs Claude Code benchmark 2026", "agentic coding tool comparison", "head-to-head AI coding agent"

### Codex plugin ecosystem

OpenAI publishing the `codex-plugin-cc` Apache-2.0 plugin FOR Claude Code (referenced in Storm Bear pattern library v62) is **not mentioned anywhere in the bundle**. Cross-vendor cooperation, plugin ecosystems, and the operator-side implications are not discussed.

**Follow-up search:** "codex-plugin-cc", "OpenAI Claude Code plugin", "cross-vendor agentic plugins"

---

## Recommended follow-up topics for the next autopilot loop

Topics ranked by promised information density (high → low):

1. **Codex vs Claude Code head-to-head benchmark** — biggest evidence gap, focused topic
2. **Team-scale agent collaboration** — shared memory files, merge-conflict workflows, per-developer overrides
3. **Enterprise IAM and prompt-injection defense for agentic coding** — production blocker
4. **Codex hooks / lifecycle events** — fills the Claude-Code-hooks parallel
5. **Agentic observability platforms (LangSmith, Arize Phoenix, etc.)** — covers logging and decision audit gaps
6. **Prompt caching and cost optimization for long-running agents** — directly affects scaling cost
7. **Cross-vendor plugin ecosystem (codex-plugin-cc and successors)** — emerging, complements operator-side work here

Add these to `raw/topics-queue.md` for the next `/loop` or cron run.

---

## Key Takeaways

- The bundle is **strong on individual-developer workflows** and **weak on team / enterprise / observability**
- The largest single evidence gap: **no head-to-head Codex-vs-Claude benchmark** — all comparisons are qualitative [Source 1, Source 3, Source 5, Source 6]
- **Team-scale agent collaboration** is essentially unaddressed [Source 1, Source 3] — git worktrees solve the one-developer case only
- **Enterprise compliance, IAM, and prompt injection defense** are critical for production but absent from the bundle
- **Codex's hook / lifecycle event model** is not characterized — Claude Code has explicit hooks ([[../claude-code-hooks/_index]]), Codex equivalent is unknown
- **Cross-vendor plugin ecosystem** (e.g. codex-plugin-cc) is a corpus-first development unmentioned in the bundle — worth a dedicated future topic
- 7 follow-up topics queued for the next autopilot run (see ranked list above)
