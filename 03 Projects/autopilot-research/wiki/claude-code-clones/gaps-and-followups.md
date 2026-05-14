# Claude Code Clones — Gaps & Follow-ups

> **Topic:** [[_index|claude-code-clones]]
> **Source:** `../../raw/2026-05-13-open-source-claude-design-clones-alternative-agent.md` § Gaps

What the 6-video bundle did NOT cover. The bundle has the structural weakness that **most of its videos are workflow-focused, not clone-focused** — so the clone-specific gap surface is unusually large.

---

## Naming and inventory gaps

### Only four clones named

The bundle names **OpenClaw, Hermes, OpenCode, Aider** [Source 1, Source 2, Source 3, Source 6] and discusses none of them in technical depth. The Storm Bear Pattern Library tracks at least three other relevant T4-archetype projects (**free-claude-code v60, cc-sdd v61, codex-plugin-cc v62**) that the bundle does not mention. There are almost certainly more.

**Follow-up search:** "Claude Code fork", "Claude Code clone open source", GitHub topic search for `claude-code-clone`, awesome-claude-code lists.

### No feature comparison matrix

The bundle has zero **what-does-each-clone-actually-support** detail — no comparison of MCP support, slash commands, hooks, plugin systems, memory layers, model routing.

**Follow-up search:** project-by-project README dive; build a comparison matrix; ask each project's docs whether it ships hooks, MCP, plugins.

### Aider barely discussed despite being foundational

Caleb mentions Aider as one of the precursors that introduced terminal-as-IDE [Source 3], but the bundle goes no deeper. Aider has its own architecture, license, and design choices worth their own wiki topic.

**Follow-up search:** Aider-specific topic — its own NotebookLM bundle if signal warrants it.

---

## Legal and business-model gaps

### No license analysis

The bundle does not discuss the **licenses** of any of the named clones. Is OpenClaw GPL? MIT? Apache 2.0? Proprietary-with-source-available? This is decision-critical for any commercial use.

**Follow-up search:** project-by-project license inspection; especially OpenClaw given its leak-derived origin.

### Copyright / IP risk of leak-derived forks

Fireship's discussion of the leak [Source 2] mentions "**barely legal** forks" without expanding on the actual legal status. Is OpenClaw legally distributable? Has Anthropic taken any DMCA action? What does the bundle's "barely legal" phrasing actually mean in practice?

**Follow-up search:** "OpenClaw legal status", "Anthropic source leak takedown", trademark / copyright filings.

### Business-model risk

The bundle hints repeatedly at Anthropic crackdowns on subscription smuggling [Source 1, Source 3] but **does not quantify** how much of the clone ecosystem depends on this trick. If 80% of clone users use a clone for subscription cost arbitrage, the crackdown destroys most of the value. If 20% do, it barely matters.

**Follow-up search:** surveys / GitHub issues / community discussion on clone-adoption motivations.

---

## Technical and operational gaps

### Model-routing implications

The bundle mentions OpenRouter [Source 5] and free-model substitution but **doesn't explore how clones differ in model-routing flexibility**. Can OpenClaw route to non-Anthropic models the way official Claude Code via OpenRouter can? Does Hermes lock you to one provider?

**Follow-up search:** project docs on supported providers; Storm Bear v60 free-claude-code is directly relevant here.

### MCP support across clones

MCP (Model Context Protocol) is a critical Claude Code primitive. The bundle does not discuss whether **any of the clones implement MCP** or how compatible their MCP implementations are with the official one.

**Follow-up search:** "OpenClaw MCP", "OpenCode MCP support", project-by-project.

### Hook system replication

The Claude Code hook system is documented at [[../claude-code-hooks/_index]]. The bundle does not discuss whether clones replicate hooks, replicate them faithfully, or skip them entirely.

**Follow-up search:** project docs for "hook" / "lifecycle event" support.

### Multi-tenant / team scaling

The bundle is heavily **solo-developer focused** (local Mac Mini, personal Telegram bot, "war room"). It does not discuss how any clone — or the Agent SDK bridge — scales to a 10-50 person dev team [explicit bundle gap, § Gaps]. No SSO, RBAC, audit logs, FinOps story for clones.

**Follow-up search:** "Claude Code team", "Claude Code enterprise", clone-specific multi-user docs.

### Sandboxing the bash tool

The bash tool is the load-bearing primitive [Source 2]. The bundle's § Gaps section explicitly calls out that **none of the sources discuss sandboxing** the bash tool to prevent `rm -rf /` accidents or prompt-injection escalation [bundle § Gaps].

**Follow-up search:** "Claude Code bash sandbox", "agent CLI container isolation", Docker / Firecracker / gVisor patterns for agent CLIs.

---

## Update-lag and maintenance gaps

### How do forks track upstream?

OpenClaw is leak-derived [Source 2]. The bundle does not discuss **how OpenClaw stays current** as Anthropic ships new versions of Claude Code. Manual diffing? Re-leaks? Independent feature work that diverges from upstream?

**Follow-up search:** OpenClaw release notes / changelog / contributor activity.

### Decay timeline

If a clone stops tracking upstream, how fast does it become functionally obsolete? The bundle gives no estimate — but Mark Kashef's pivot [Source 1, Source 4] is implicitly a signal that the decay is real.

**Follow-up search:** OpenClaw last-commit-date trends, GitHub star velocity, community-activity signals.

---

## Storm Bear vault-specific gaps

These are gaps in **bundle vs vault state**, not in the bundle on its own terms.

- Bundle does not discuss the **api-protocol-translation-proxy archetype** (Storm Bear v60 free-claude-code) even though it's clone-adjacent
- Bundle does not discuss the **SDD methodology framework archetype** (Storm Bear v61 cc-sdd) which is augmentation-not-clone but adjacent
- Bundle does not discuss the **cross-vendor cooperation pattern** (Storm Bear v62 codex-plugin-cc) where OpenAI publishes a Claude Code plugin — directly relevant to "is the answer to fork or extend?"

**Implication:** the bundle's view of the clone landscape is **narrower than the Pattern Library tracks**. A future autopilot run should cross-walk this bundle against Pattern Library entries v60, v61, v62.

---

## Recommended follow-up topics for the next autopilot loop

Topics ranked by promised information density (high → low):

1. **OpenClaw deep-dive** — license, architecture, upstream-tracking, current status. The single highest-value follow-up.
2. **Aider architecture wiki** — Aider is foundational and the bundle treats it as a footnote
3. **MCP compatibility across clones** — concrete feature-matrix question
4. **Bash tool sandboxing patterns** — security gap; relevant to clones and official tool alike
5. **Claude Code enterprise / team scaling** — explicit bundle gap; affects clone evaluation
6. **Comparison: Claude Code vs Codex vs OpenClaw vs OpenCode** — feature matrix the bundle does not provide

Add these to `raw/topics-queue.md` for the next `/loop` or cron run.

---

## Key Takeaways

- The bundle is **structurally thin on clones** — most videos are workflow content with passing clone mentions
- **Only four clones named**, none discussed in technical depth — see [[overview]]
- **No license analysis**, **no copyright / IP discussion**, **no business-model risk quantification** — significant decision-critical gaps
- **Update-lag** is the implicit risk no source quantifies, but Mark Kashef's pivot is the strongest signal it exists [Source 1, Source 4]
- **Bash tool sandboxing** is an explicit bundle gap with security implications [bundle § Gaps]
- The bundle's clone-landscape view is **narrower than the Storm Bear Pattern Library** tracks (v60 free-claude-code, v61 cc-sdd, v62 codex-plugin-cc all relevant and uncovered)
- **6 follow-up topics queued** for the next autopilot run; OpenClaw deep-dive is the single highest-value next step
