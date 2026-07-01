# google-antigravity-skills

> **Topic index.** How **Google Antigravity** — Google's agent-first development platform — implements **Skills** and **Rules**, and (the load-bearing finding) why they're the **same open standards your Claude Code harness already uses**. Skills are **Anthropic's open `SKILL.md` format**; rules ride the **Linux-Foundation `AGENTS.md`** cross-tool standard. Net: your skills/rules are portable to Antigravity — a **free, multi-model** second surface — for roughly the cost of a directory rename.
>
> **Entry point:** [UFmV7YsVqlM](https://www.youtube.com/watch?v=UFmV7YsVqlM) — **"Google Antigravity 2.0: Cách tạo Skill AI, Rule Và Quản Lý Skill Từ A-Z"**, a **22:39 Vietnamese beginner tutorial** on **Dũng - Chia Sẻ Công Nghệ** (1,320 subs; uploaded **2026-06-27**, ~1.1K views). A *third-party* creator walkthrough teaching Skills + Rules via an Excel sales-report demo — **not** first-party. Full auto-caption transcript read (`raw/2026-07-01-google-antigravity-skills-rules-dung-chiasecongnghe.md`).
>
> **⚠️ "Antigravity 2.0" is real (and the video's title is accurate).** Antigravity launched in **public preview Nov 2025** with Gemini 3; **Antigravity 2.0** is an **official standalone desktop app** announced around **Google I/O 2026 (May 2026)** — alongside the IDE, CLI (Go) and SDK (Python). The operator's own first-read guessed "2.0 = informal label" and was **corrected** by the verification workflow. See [[google-antigravity-skills/source-provenance]].
>
> **Original resource (deep-dived against primary sources):** Google Antigravity itself — [antigravity.google/docs](https://antigravity.google/docs), the official [Skills codelab](https://codelabs.developers.google.com/getting-started-with-antigravity-skills), [Google I/O 2026 dev highlights](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/), the Cloud "[choosing your surface](https://cloud.google.com/blog/topics/developers-practitioners/choosing-your-surface-antigravity-20-antigravity-cli-antigravity-ide-or-antigravity-sdk)" page, Anthropic's [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) publication + [agentskills.io](https://agentskills.io/specification), and the [Linux Foundation Agentic AI Foundation](https://www.linuxfoundation.org) (`AGENTS.md`).
>
> **Verification:** Workflow `wf_1e5cf2f6-5ec` (**16 agents**: 7 dimension gatherers → 7 adversarial verifiers → synthesis → completeness critic; ~816K tokens, 355 tool calls) + operator WebFetch/WebSearch ground-checks. Corrections: **the video's skills path `.antigravity/skills` is wrong → `.agents/skills/`**; **Windsurf was a $2.4B *licensing + reverse-acquihire*, not an acquisition**; a WebFetch summarizer **over-flagged the real Cloud "2.0" page as "fictional"** (stale-cutoff misfire — overridden). Full ledger + don't-re-fabricate list: [[google-antigravity-skills/source-provenance]].

---

## Articles

- [[google-antigravity-skills/overview]] — what Antigravity *is* (agent-first platform; 4 surfaces: 2.0 desktop / IDE / CLI / SDK; multi-model incl. Claude; Nov-2025 launch + I/O-2026 2.0), and what the video teaches (the "teach once / clone yourself" framing).
- [[google-antigravity-skills/skills-system]] — **the mechanism.** Exact paths (`.agents/skills/` / `~/.gemini/config/skills/`), the `SKILL.md` format (`description` required, `name` optional), optional `scripts/`+`resources/`+`assets/`, **progressive-disclosure auto-discovery**, `/skill-name` invocation, manual creation.
- [[google-antigravity-skills/rules-and-customization]] — **`AGENTS.md` + `GEMINI.md` + `.agent/rules/`**, the System-Rules-immutable hierarchy, the **Customizations panel** / `/config`, global vs workspace, and the clean **Rule-vs-Skill** distinction.
- [[google-antigravity-skills/workspace-vs-global]] — the two scopes and the video's **"two houses"** analogy (vacuum-cleaner vs street-lamp), with exact on-disk locations.
- [[google-antigravity-skills/build-methods]] — the **two ways to build a skill** (hand-author vs harvest-from-a-session) + the **Excel sales-report worked example** (do-once → capture → guard with a rule → one-shot forever).
- [[google-antigravity-skills/anthropic-agent-skills-portability]] — **the headline.** Antigravity Skills = **Anthropic's open `SKILL.md`**; `AGENTS.md` = LF cross-tool rules standard; how to port skills/rules between Antigravity and Claude Code (copy folder + swap dir), with caveats.
- [[google-antigravity-skills/vs-claude-code-and-cursor]] — concept-by-concept map across **Antigravity vs Claude Code vs Cursor vs Windsurf/Kiro** (dirs, formats, invocation, orchestration).
- [[google-antigravity-skills/caveats-and-limitations]] — **the critic layer.** Public-preview immaturity, Chrome dependency, partial Linux, and the mid-2026 community reports (token overhead, weekly-quota lockouts, infinite-loop drain, 403 bans) — clearly labeled reported-vs-official.
- [[google-antigravity-skills/video-summary]] — a faithful, timestamped summary of Dũng's tutorial + the auto-caption garbles interpreted.
- [[google-antigravity-skills/source-provenance]] — the verified-vs-corrected ledger, the 11-video-claim confabulation guard, the WebFetch-"fictional" override, and the **don't-re-fabricate** list.

## Pilot methods (how to apply this to your flow)

A ranked menu of **methods + a skip-list + a critic's reframe** lives in **`output/(C) 2026-07-01-google-antigravity-skills-pilot-methods.md`**, across five angles: **standards-portability** (adopt `AGENTS.md` as a portable superset of your `CLAUDE.md`; recognize your existing skills are already Antigravity-compatible), **hireui Goal #2** (harvest the Candidate-Detail refactor workflow into a portable `SKILL.md` + an `AGENTS.md` guard rule; a free multi-model second-opinion surface), **the Skill-vs-Rule discipline** (as a lint for your vault + hireui harness), **Scrum coaching** (the "teach once" demo as an agent-adoption teaching aid), and the **vault** (make project-local skills tool-agnostic).

## Cross-topic links

- [[../claude-skills/_index]] · [[../claude-code-skills-stack/_index]] — the **`SKILL.md` convention** Antigravity adopts verbatim; "skills are files, not plugins."
- [[../open-design/_index]] — same open-standards posture: `SKILL.md` + `DESIGN.md`, bring-your-own-agent; an open re-use of Anthropic's format.
- [[../harness-engineering/_index]] · [[../pocock-agentic-workflow/_index]] · [[../workflow-ai-coding/_index]] — **harness > model** extends to **harness > tool**: portable skills/rules outlive any single IDE. (Harness-engineering also tracks the Kiro-methodology and `agents.md`-as-ecosystem-format threads.)
- [[../claude-md-12-rules/_index]] — `CLAUDE.md` / `AGENTS.md` project-rules lineage; the Rule-vs-Skill split is a governance idea.
- [[../claude-code-clones/_index]] · [[../codex/_index]] — the multi-tool agentic-IDE landscape Antigravity sits in.
- [[../multi-agent-orchestration/_index]] — Antigravity 2.0's parallel subagents / orchestration surface (persona names unverified — see caveats).
- [[../omnilogin-ai-coding/_index]] · [[../cowork-third-party-inference/_index]] — multi-model / BYO-model posture (Claude, Gemini, GPT-OSS in one IDE).
- [[../how-we-claude-code/_index]] — Antigravity ships a Stitch design-to-code MCP; HTML/artifact handoff lineage.
- [[../claude-api-cost-optimization/_index]] — the CLI's reported ~23–25k-token overhead + quota model.

## Key Takeaways

- **Antigravity = Google's agent-first dev platform** (IDE + CLI + SDK + the 2.0 desktop hub), **free public preview** since Nov 2025, **multi-model incl. Claude** — and **"Antigravity 2.0" is a real Google I/O 2026 product**, not a creator's label.
- **Its Skills ARE Anthropic's open `SKILL.md` format** and its rules ride the **`AGENTS.md`** Linux-Foundation standard — so **your Claude Code harness is portable here** for ~the cost of a directory rename. This is the finding to act on.
- The video's durable lesson is the **Skill (capability) vs Rule (constraint)** split and the **"do it once → capture as a skill → guard with a rule → one-shot forever"** loop — a clean discipline regardless of tool.
- **Correct the video where it's wrong:** the skills path is **`.agents/skills/`** (not `.antigravity/skills`), and "make a skill" is **the agent authoring the file**, not a product button.
- **Pilot it as a free sandbox / second surface, not a Claude Code replacement** — the public preview has real mid-2026 quota/stability/ban caveats; keep production data (hireui/PII) out.
