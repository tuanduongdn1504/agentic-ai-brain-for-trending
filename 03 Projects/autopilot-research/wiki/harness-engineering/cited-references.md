# Cited references — downstream research surface

> Every external reference Lopopolo makes in the anchor bundle. Each row is a **candidate next-ingest**: a tool, person, paper, or company whose deeper investigation would expand this thread. Marked priority based on (a) how load-bearing in the talk vs incidental, (b) availability of public material, (c) whether already covered elsewhere in the autopilot wiki.

## OpenAI products & internal tools

| Reference | Context | Priority |
|---|---|---|
| **OpenAI Frontier** | Enterprise platform for safe, governable agents at scale; Lopopolo's team | HIGH — central to thesis; needs separate research thread |
| **Symphony** | Elixir orchestration layer; coordinates hundreds of concurrent agents | HIGH — claim #4 depends on it |
| **Codex / Codex App** | Primary agent UI used by Lopopolo's team; 2M weekly active users cited | MED — separate Anthropic-comparison research |
| **GPT-5.2 / 5.4** | Cited as "isomorphic" inflection point | MED — model-capability axis |
| **Deep Research** | Cautionary anecdote (legal-issue rabbit hole) | LOW — anecdote only |

## Software tools & frameworks

| Reference | Context | Priority |
|---|---|---|
| **Elixir / Beam (BEAM VM)** | Why Symphony chose it: native process supervision + GenServers | HIGH — under-explored angle for agent infra |
| **Turbo (Turborepo) / NX** | Build systems for sub-1-min inner loop (claim #3) | HIGH — operational requirement |
| **GitHub CLI (gh)** | Token-efficient PR lifecycle without web UI | MED — overlaps [[external\|10x-claude-code/_index]] |
| **Linear** | Issue tracker that feeds milestones to agents | MED — agent-task ingestion surface |
| **Victoria Stack** | Go binaries for local observability | LOW — implementation detail |
| **Zod** | Schema validation as "load-bearing infrastructure" against typed slop | MED — adjacent to validation patterns |
| **Playwright** | UI smoke tests for Electron apps | LOW — already in autopilot stack |
| **Bazel** | Experimented with, transitioned away from | LOW — historical |
| **Grafana / Prometheus** | Dashboards agents author + monitor | MED — agentic observability angle |
| **Electron** | Testbed for Zero-Code experiment | LOW — incidental |
| **FFmpeg** | Cited as "Swiss Army Chainsaw" example of agent-usable CLI | LOW — illustrative |

## Companies & organizations

| Reference | Context | Priority |
|---|---|---|
| **Snowflake / Stripe / Brex / Citadel** | Lopopolo's prior employers; cited as Frontier target profile | LOW — biographical |
| **Datadog / Temporal** | "Too complex to vendor" — define current ceiling of claim #7 | HIGH — falsifies/bounds claim #7 |
| **Lovable / Bolt / Replit** | Zero-to-one scaffolding; explicitly distinguished from harness engineering | MED — comparative thread |
| **Applied Intuition / Shopify / Notion** | Other AI phase transitions (incidental in podcast) | LOW |

## Researchers, speakers & engineers

| Reference | Context | Priority |
|---|---|---|
| **Bret Taylor** (OpenAI Chairman) | "Software dependencies are going away" — corroborates claim #7 | HIGH — public talks/interviews to ingest |
| **Alex Kotliarskyi** | Built reference Elixir implementation that became Symphony | HIGH — authorial source for Symphony deeper-dive |
| **Andrej Karpathy** | "English is the hottest new programming language" | LOW — already represented in Storm Bear corpus |
| **Rich Sutton** (The Bitter Lesson) | Used to argue against over-engineering for current model limits | MED — foundational; ingest the original essay |
| **Linus Torvalds** | "Many eyes" theory of security, contrasted with vendoring | LOW — illustrative |
| **Jared Palmer** | Creator of Turbo build system | LOW — tool author |
| **swyx + Vibhu Sapra** (podcast hosts) | Co-investigators on this anchor | MED — their own AI-engineering content is companion-relevant |

## Papers, books & concepts

| Reference | Context | Priority |
|---|---|---|
| **ADRs (Architecture Decision Records)** | "Breadcrumbs" for agents to understand intent | HIGH — operational primitive |
| **Postel's Law** | Explains library bloat that vendoring (claim #7) sidesteps | MED — supporting concept |
| **MVC** | Classical architecture pattern justifying agent-legible re-sharding | LOW — illustrative |
| **LLVM / Cranelift** | LLMs as "fuzzy compilers" analogy | MED — conceptual bridge |
| **The Bitter Lesson** (Sutton 2019) | Cited indirectly in podcast | HIGH — foundational; should have its own wiki article |

## Companion content NOT ingested in anchor cycle

These were known but excluded from the 2026-05-09 ingest. Flag for the next research cycle:

| URL | Reason excluded | Re-attempt strategy |
|---|---|---|
| https://openai.com/index/harness-engineering/ | 403 bot block during WebFetch + (presumably) NotebookLM | Try custom scraper (Playwright + headed mode) per [[external\|telegram-remote-control-stack/_index]] pattern |
| Lopopolo's GitHub https://github.com/lopopolo | Out-of-scope for anchor | Mine for harness-engineering reference repos in next cycle |
| Latent Space "Recent Episodes" — Applied Intuition / Shopify / Notion AI transitions | Off-topic for this anchor but adjacent | Separate research threads |

## Top-5 next ingests (priority HIGH)

If running `/loop autopilot research` next, queue these in order — see [[research-roadmap]] for the full sequencing argument:

1. **OpenAI engineering blog "Harness Engineering"** (https://openai.com/index/harness-engineering/) — canonical written form of same content; resolve via custom scraper
2. **Bret Taylor public talks on agentic engineering** — corroborates/extends claim #7
3. **Symphony-adjacent material** — Elixir/Beam for agent orchestration, Alex Kotliarskyi posts if discoverable
4. **Datadog + Temporal "vendoring ceiling" investigation** — bounds claim #7
5. **Rich Sutton "The Bitter Lesson" essay** — foundational citation, should be its own wiki entry

---

## Speakers + frameworks from sibling drains (added 2026-05-30)

People, channels, and proprietary framework names surfaced via the 2026-05-30 harness-engineering-getting-started drain ([[getting-started-consensus-and-divergences]]). Each is a candidate next-ingest if their specific work warrants a focused drain.

### Individual practitioners

| Speaker | Channel | Context | Priority |
|---|---|---|---|
| **John Kim** | John Kim (YouTube) | Meta Staff Engineer position; anti-MCP stance ([[contrarian-stances#11]]); 300-line `claude.md` ceiling | MED — separate focused drain on his Meta tips video (435K views) |
| **AI with Avthar** | AI with Avthar (YouTube) | PSB system creator (Plan-Setup-Build); link-to-specialist-docs convention | MED — has companion course material worth surfacing |
| **Productive Dude** | Productive Dude (YouTube) | GCAO + DBS framework creator; 112-min full beginner course | LOW-MED — content is broadly covered elsewhere |
| **Maddy Zhang** | Maddy Zhang (YouTube) | Senior SWE 100-200-line `claude.md` ceiling (tightest in corpus); validation-hooks advocate | LOW — short video, content already absorbed |
| **Caleb Writes Code** | Caleb Writes Code (YouTube) | 8-min "Agent Harness explained" — meta-explainer | LOW — content already absorbed |
| **Tù Bà Khuỳm V2** | Tù Bà Khuỳm (YouTube) | V2 harness with SQLite-as-memory; same Vietnamese practitioner as V1 from 2026-05-13 bundle | HIGH — corpus-first SQLite contribution merits sustained tracking; [[personal-repo-tu-ba-khuym-getting-started]] is anchor |

### Proprietary framework acronyms

| Framework | Creator | Scope | Article reference |
|---|---|---|---|
| **GCAO** | Productive Dude | Goal · Context · Action · Output (prompts) | [[personal-repo-patterns#8]] |
| **DBS** | Productive Dude | Direction · Blueprints · Solutions (skills) | [[personal-repo-patterns#9]] |
| **PSB** | AI with Avthar | Plan · Setup · Build (project lifecycle) | [[personal-repo-patterns#10]] |
| **PRD-first** | Multiple (Caleb, Tù Bà Khuỳm, Avthar) | Production Requirement Document precedes any code | Standard methodology — not creator-branded but worth tracking adoption |

### Specific quantitative constraints worth tracking

| Constraint | Speaker | Quote |
|---|---|---|
| `claude.md` ≤ 200 lines | **Maddy Zhang** | "100 to 200 lines max" — tightest documented |
| `claude.md` ≤ 300 lines | **John Kim** | "around 300 lines is a decent target" |
| Session cycling every 30-45 min | Jack Roberts (Cowork sibling drain) | Prevents context-rot inflation |
| Plan mode duration ~15 min | **AI with Avthar** | "spends 15 minutes planning before any coding" |

These are testable thresholds — operator could measure context-bloat at each value to find the empirical sweet spot for their workflow.
