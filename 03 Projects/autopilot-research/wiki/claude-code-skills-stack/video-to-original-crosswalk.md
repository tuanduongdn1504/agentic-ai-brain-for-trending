# Video → Original Crosswalk

> Maps every Eric Tech skill → its canonical original → what Eric *adds* → what the video gets **wrong or omits**. Stars `gh`-verified 2026-06-29.

## Crosswalk table

| Video skill | Canonical original | Verified | What Eric adds | What's wrong / omitted |
|---|---|---|---|---|
| 1 Superpowers | `obra/superpowers` (Jesse Vincent) | 240.9K★ MIT Shell/JS | Uses it as the brainstorm/plan/execute spine of his merged skill | Says "tests *before* execute" — TDD actually runs *during* execution; calls it Markdown (it's Shell/JS) |
| 2 Skill Creator | `anthropics/skills`/skill-creator | first-party 156.4K★ | The **merge-3-frameworks** meta-move (build `build-feature`) | Doesn't show the eval/benchmark loop in depth; "Skill 2.0" = 2026-03-03 update |
| 3 UI UX Pro Max | `nextlevelbuilder/ui-ux-pro-max-skill` + `uipro-cli` | 97.6K★ MIT | Constraint-driven redesign ("keep my colors/order") | "Trained on hundreds of datasets" is **false** — it's bundled CSV + reasoning rules |
| 4 Awesome Design MD | `voltagent/awesome-design-md` + `google-labs-code/design.md` | 94.1K★ / 23K★ | Copy a brand (Apple/Stripe) `DESIGN.md` into the app | "Install via a command" — it's mostly **copy-based**; "Google Stitch introduced design.md" is right (garbled to "Stage") |
| 5 Playwright CLI | `microsoft/playwright-cli` vs `microsoft/playwright-mcp` | 11.7K★ / 34.5K★ | 16-phase QA run, screenshot+console per step → QA report | Implies skill files are **gated** — they're **public** (`EricTechPro/startup-claude-skills`) |
| 6 Obsidian | `kepano/obsidian-skills` (Steph Ango) | 38.8K★ MIT | Base files + per-project folder constraints + graph view | "Official Obsidian / a RAG" — it's his **personal** repo + **format skills**, not a RAG; the RAG is the **Karpathy pattern** it composes with |
| 7 "43 Marketing Skills" | `ericosiu/ai-marketing-skills` (**Eric Osiu**) | 2.7K★ MIT | Applied to BookZero growth | **Misattributed** — Eric Osiu's, not Eric Tech's; "0→1000 from these" unverifiable |
| 8 /fix-ticket | `EricTechPro/startup-claude-skills` (Eric's own) | 51★ MIT **public** | Full Sentry→Jira→fix→Vercel→handoff workflow | "Replaces ~90% of junior jobs" = hyperbole |
| + GSD | `gsd-build/get-shit-done` → `open-gsd/gsd-core` | 64.6K★ (**archived**) / 5.3K★ | AI-integration phase in merged skill | Original is **archived** — use open-gsd fork |
| + G-Stack | `garrytan/gstack` | 117.8K★ MIT TS | Persona review + `/qa` + `/ship` stages | No literal "devil's advocate" skill; "Garry Tan authored it" plausible-not-hard-verified |

## What the originals show that the video doesn't

- **Token economics** of plugin/skill loading (progressive disclosure) and CLI-vs-MCP (~4× difference) — only the CLI/MCP video touches it.
- **Eval rigor** behind Skill Creator (grader/comparator/analyzer; pass-rate/latency/token benchmarking) — the actual moat of the meta-move.
- **GSD governance** (archived original → community fork) and the **open vs official** distinction for the Obsidian skill.
- **When NOT to use** an SDD framework / persona panel (overhead on trivial tickets) — Eric's ticket-classifier *gestures* at this but the source frameworks debate it.

## Three classification axes

- **First-party Anthropic:** Skill Creator (#2), Telegram/Sentry-adjacent plugins, `frontend-design` (alt to #3/#4).
- **Real third-party, free, high-leverage:** Superpowers (#1), GSD, G-Stack, UI UX Pro Max (#3), Awesome Design MD (#4), Playwright CLI/MCP (#5), Obsidian skill (#6).
- **Creator's own / misattributed / gated-community:** /fix-ticket (#8, public), "43 marketing" (#7, Eric Osiu's), Skool templates (paid).

## Related

[[claude-code-skills-stack/_index]] · [[claude-code-skills-stack/the-eight-skills]] · [[claude-code-skills-stack/source-provenance]]
