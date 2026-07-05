# TNT vs the corpus — positioning, corpus-firsts, convergences, pattern evidence

> Cross-cutting positioning of the TNT/Trung Tran factory ([[tnt-cursor-cli-factory-anchor]]) against the topic's 3 layers (org-scale / individual-scale / platform) and the Storm Bear Pattern Library. Corpus-first claims below were checked against the wiki by the lineage verify agent (`wf_3740e2d5-2b4`); each is a *checked-absence*, phrased as "first corpus treatment", not absolute novelty.

## Where it sits

**Individual-scale, 10th sibling** — but structurally closer to the org-scale factory ideal than any prior sibling: prior siblings optimize *interactive* development (routing, multiplexing, review commands, memory); TNT runs an **unattended multi-gate pipeline that ships a whole app from specs**. It is the missing middle between Tù Bà Khuỳm's beginner harness and Lopopolo's Symphony — a one-person dark factory with brakes, on a $192/yr budget.

## Corpus-firsts (checked against wiki 2026-07-05)

1. **First non-Claude-Code full factory** in the individual-scale layer: Cursor CLI (`agent`) as the only AI runtime. Prior siblings: Claude Code (7×), Hermes+Codex+Claude, 9Router multi-vendor — all interactive-first. (Cursor appeared in corpus only as IDE mentions.)
2. **First separate TestGen loop**: requirement-tag-keyed, schema-validated JSON test-case artifacts with a 12-technique coverage taxonomy + mandatory coverage self-check — test *specification* generation decoupled from implementation, with its own loop, gate mode (optional/required), and enhance lane.
3. **First deterministic doc-fingerprint drift mechanism**: SHA256 of spec docs; drift → auto-reset of test-case currency AND slice `passes` → both loops re-converge. SDD's "specs are source of truth" enforced by hash, not discipline. (cc-sdd/OpenSpec/spec-kit encode spec *phases*; none in corpus auto-invalidate downstream work on spec edit.)
4. **First typed completion-signal protocol with dual grace timers** (`SLICE_DONE`/…, signalGraceMs + resultGraceMs, tail-scan detection) as loop-exit mechanism — deterministic sibling to Archon's `until_bash`, hand-rolled.
5. **First declarative forbidden-patterns gate** (regex + scoped paths + message in loop config; in-memory-repo/SQLite/mock-fixture/lorem-ipsum hard fails) — the corpus' anti-slop *advice* turned into config.
6. **First formalized validation-vs-evaluation two-stage gate vocabulary** (machine-decidable checks vs judgment review as named, ordered, separately-privileged stages).
7. **First in-the-wild adopt-vs-build A/B**: same product scaffolded twice — hand-rolled harness (`hesd`) vs BMAD-METHOD personas (`hesd_bmad`) — publicly, by one practitioner ([[tnt-factory-run-empirics]]).
8. **Zero-framework substrate**: bash + jq + 1 Node script + JSON + markdown. Prior corpus factories ride Claude Code, Archon, Hermes, or vendor plugins.

## Convergences (independent — repo cites nobody; verified zero mentions of Huntley/Lopopolo/Anthropic/Archon/BMAD-METHOD in we-event files)

| TNT mechanism | Corpus sibling | Note |
|---|---|---|
| Fresh agent context per iteration; state on disk+git | Archon fresh-context⇒artifact-driven; Pocock blank-slate | 3-way independent convergence — strongest design-consensus signal in topic |
| Prompt→context→harness narrative | [[archon-harness-builder-anchor]] evolution thesis; Tejas Kumar | now N≥3 independent tellings |
| Ralph loop (named) | Lopopolo terminology entry; Huntley technique provenance; Hermes `/goal`; Archon bounded-Ralph DAG | TNT = no-lineage vocabulary adoption; loop-exit is deterministic (signals+backlog), closer to Archon than to raw Ralph |
| Read-only reviewer w/ bundled evidence | Pattern #76 strata (cc-sdd role-separation; codex prompt-framing; archon-adversarial-dev state machine) | TNT = **4th mechanism stratum candidate: shell-pipeline role separation with CLI-mode-enforced read-only + evidence bundling** (gate pipeline, not adversarial panel) |
| Docs-first + acceptance tags + MVP scope guard | Pattern #21 SDD emergence (GSD/spec-kit/gsd-2/OpenSpec/cc-sdd) | independent SDD instance w/o SDD branding — supports Pattern #21's "structural inevitability" reading |
| Guardrails-as-lessons injected each run | progress.md/Ralph Signs ≈ Pocock `progress.md`, Archon guardrail nodes, memory-consolidation gates | TNT adds *failure-summary injection* from run JSONs — mechanical, not curated |
| Human-review checklist + `HUMAN_REVIEW_PASS` on mergeReady | dark-factory-with-brakes (Archon maintainer layer) | N=2 for explicit typed human sign-off signal |
| $192/yr Auto-lane economics | [[harness-economics-and-tos-timeline]] | Cursor's officially-sanctioned unlimited-Auto vs Anthropic's contested subscription-agent lane — cleanest verified cost floor in topic |
| Playwright-MCP browser gate w/ per-case IDs | helpline validator, Zen `/smell`-style catalogs, tester-gate patterns | 2nd independent full implementation; adds test-case-ID traceability |

## Divergences / contrasts worth keeping

- **Vs Archon**: same goals, opposite substrate philosophy — Archon = install a platform that builds harnesses (UI, DB, 18 tables); TNT = vibe-code a disposable harness per project, mutate, even generate-then-delete a scaffolder. Platform-vs-artisan axis now has both poles first-party documented.
- **Vs cc-sdd/BMAD**: TNT's own hesd_bmad experiment makes him the first corpus subject *running* the frameworks-vs-DIY question rather than arguing it. Outcome unknown as of 2026-07-05 (hesd_bmad is early) — watch-list item.
- **Vs John Kim anti-MCP stance**: TNT is MCP-minimal (exactly one: Playwright) — a middle position: MCP only where the capability (browser) is otherwise absent.
- **Vs Zen's anti-SDD prediction** ("won't survive 6 months", 2026-05-20): TNT is a counter-datum — an SDD-shaped pipeline whose *drift mechanics* remove the staleness objection Zen raises.

## Pattern Library evidence queued (for v66 mini-audit; ship-time registration only — do NOT bump counts)

- **Pattern #76** (adversarial/role-separated review): 4th mechanism stratum candidate — shell-pipeline gate with CLI-enforced read-only reviewer + evidence bundling (distinct from cc-sdd architectural, codex prompt-framing, archon workflow-state-machine strata).
- **Pattern #21** (SDD emergence): unbranded independent instance w/ novel enforcement (fingerprint drift) — strengthens structural-unambiguity reading; also counter-evidence log for Zen's anti-SDD position (Pattern #51-adjacent polarity data).
- **Pattern #55** (VN cohort): 2nd VN first-party voice in this topic (after Tù Bà Khuỳm), 3rd VN-language source incl. howznguyen; now VN has beginner-pedagogy + router-pattern + full-factory strata — deepest regional sub-cohort in the topic.
- **Pattern #57/#19**: solo-practitioner public-ledger factory as credibility mechanism (auditability-as-positioning) — observation only, N=1.
- **Cost-Discipline OT**: verified $192/yr unlimited-Auto datum.

## Key takeaways

- TNT closes the corpus gap between "individual harness = interactive productivity" and "factory = org-scale": the factory pattern is now demonstrated, audited, and affordable at N=1.
- The three strongest *portable* novelties: fingerprint-drift SDD enforcement, TestGen-as-separate-loop with technique taxonomy, declarative forbidden-patterns gate.
- Independent convergence count keeps rising on: fresh-context/artifact-state, docs-as-truth, staged gates, human sign-off brakes — these are becoming the topic's settled physics; the open frontier is authorship posture (platform vs artisan vs framework) and economics.

## Related

[[tnt-cursor-cli-factory-anchor]] · [[tnt-we-event-harness-mechanics]] · [[tnt-factory-run-empirics]] · [[archon-harness-builder-anchor]] · [[getting-started-consensus-and-divergences]] · [[personal-repo-vs-org-scale]]
