# (C) Multi-Host Declarative Platform

> **Source:** README.md (install sections + host table), CHANGELOG v0.15.6.0 "Declarative Multi-Host Platform"
> **Ingested:** 2026-04-18
> **Type:** Entity page (distribution concept) — entity #4 cho gstack

---

## One-liner

**VI:** Multi-Host Declarative Platform là **cách gstack ship cùng 1 skill collection tới 10 harnesses khác nhau** (Claude Code, Codex CLI, OpenCode, Cursor, Factory, Slate, Kiro, Hermes, GBrain, OpenClaw) qua **pattern declarative** — mỗi host là 1 file TypeScript config trong `hosts/<name>.ts`. Adding new host = 1 config file, zero code changes.

**EN:** Multi-Host Declarative Platform is how gstack ships the same skill collection to 10 different harnesses via a declarative pattern — each host is one TypeScript config file. Adding new host = one config file, zero code changes.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu vì sao gstack chạy được trên 10 harnesses (most của 3 sibling frameworks)
- Designing cross-harness tool — xem gstack's pattern as template
- Compare với ECC's plugin model + Superpowers's per-harness manifest folder
- Adding support cho new harness trong fork riêng

**Không cần để dùng gstack cơ bản** — user chỉ cần `./setup` (auto-detects harnesses) hoặc `./setup --host <name>`.

---

## Comparison sibling: 3 distribution models

| Axis | gstack Multi-Host Declarative | Superpowers Per-Harness Manifest | ECC Plugin Model |
|------|-------------------------------|----------------------------------|------------------|
| Pattern | `hosts/<name>.ts` TypeScript config | `.<harness>/` folder per harness | Single plugin.json |
| Host count | **10** | 7 | 5 |
| Add new host | 1 TS config file | 1 folder + manifest + INSTALL.md | Plugin extension |
| Skills source | Shared root `skills/` (or role folders) | Shared root `skills/` | Plugin-bundled |
| Tool name mapping | Runtime (Claude names → host names) | Runtime (TodoWrite → todowrite) | Plugin-managed |
| Distribution channel | Git URL clone + symlink per host | Claude marketplace + git URL | Plugin install |
| Update mechanism | `./setup` re-runs + auto-upgrade hourly throttled | Marketplace refresh / git pull | Plugin manager |

→ **Distinctive:** gstack's declarative TypeScript pattern most elegant. Each host config is ~1 file, programmatically validated.

---

## Sub-types: 10 hosts supported

### Tier 1: Primary (well-tested)

| Host | Flag | Skills install path |
|------|------|---------------------|
| Claude Code | default | `~/.claude/skills/gstack` |
| OpenAI Codex CLI | `--host codex` | `~/.codex/skills/gstack-*/` |
| OpenCode | `--host opencode` | `~/.config/opencode/skills/gstack-*/` |
| Cursor | `--host cursor` | `~/.cursor/skills/gstack-*/` |

### Tier 2: Secondary (community)

| Host | Flag | Skills install path |
|------|------|---------------------|
| Factory Droid | `--host factory` | `~/.factory/skills/gstack-*/` |
| Slate | `--host slate` | `~/.slate/skills/gstack-*/` |
| Kiro | `--host kiro` | `~/.kiro/skills/gstack-*/` |
| Hermes | `--host hermes` | `~/.hermes/skills/gstack-*/` |
| GBrain (mod) | `--host gbrain` | `~/.gbrain/skills/gstack-*/` |

### Tier 3: Native (ClawHub)

| Host | Mechanism |
|------|-----------|
| OpenClaw | `clawhub install gstack-openclaw-*` — native methodology skills, no Claude Code session needed |

**4 native OpenClaw skills:**
- `gstack-openclaw-office-hours`
- `gstack-openclaw-ceo-review`
- `gstack-openclaw-investigate`
- `gstack-openclaw-retro`

---

## Anatomy: `hosts/<name>.ts`

Per CLAUDE.md project structure:

```
hosts/
├── claude.ts        # Primary host config
├── codex.ts         # OpenAI Codex CLI
├── factory.ts       # Factory Droid
├── kiro.ts          # Kiro
├── opencode.ts      # OpenCode
├── slate.ts         # Slate
├── cursor.ts        # Cursor IDE
├── openclaw.ts      # OpenClaw
├── hermes.ts        # Hermes agent runtime
├── gbrain.ts        # GBrain (mod)
└── index.ts         # Registry: exports all, derives Host type
```

**`index.ts` pattern:**
```typescript
// Pseudo-schema (inferred — not source-verified yet)
export const hosts = {
  claude: claudeConfig,
  codex: codexConfig,
  // ...
};
export type Host = keyof typeof hosts;
```

**Each host config declares (inferred từ `./setup --host <name>` behavior):**
- Install path pattern (`~/.codex/skills/gstack-*/`)
- Tool name mappings (TodoWrite → todowrite, etc.)
- Setup hooks (any post-install commands)
- Auth mechanisms (bearer token, session tokens, etc.)

→ **Pattern:** Type-safe host declaration. New host = 1 TypeScript file importing common schema.

---

## Cơ chế: Setup flow

### `./setup` auto-detection

```bash
cd ~/.claude/skills/gstack && ./setup
```

1. Detect installed harnesses by checking dirs (`~/.claude/`, `~/.codex/`, `~/.cursor/`, ...)
2. For each detected, run host-specific install (symlink skills, copy configs)
3. Report what was installed

### `./setup --host <name>` explicit

```bash
./setup --host codex
```

Runs single host install regardless of detection.

### `./setup --team` team mode (v0.15.13.0)

```bash
cd ~/.claude/skills/gstack && ./setup --team
```

Then bootstrap repo:
```bash
cd <your-repo>
~/.claude/skills/gstack/bin/gstack-team-init required  # or: optional
git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```

**Result:** Every developer installs globally. Updates auto (hourly throttled). No vendored files in repo.

### `./setup --no-prefix` / `--prefix` (naming)

- `--no-prefix` (default) → short names: `/qa`, `/review`
- `--prefix` → namespaced: `/gstack-qa`, `/gstack-review`

**Use `--prefix`** if running other skill packs alongside (avoid collision).

---

## Out-of-box behavior per host

**Claude Code (primary):**
- Skills at `~/.claude/skills/gstack/` symlink to each role folder
- Short names default (`/qa`)
- Hourly auto-upgrade check (silent, network-failure-safe)
- Browser daemon starts on first `$B` command

**Codex CLI:**
- Skills at `~/.codex/skills/gstack-*/`
- Namespaced: `gstack-qa`, `gstack-review`, etc.
- No browser daemon (Codex doesn't support)

**OpenClaw:**
- 4 conversational skills native
- Install via `clawhub`
- No Claude Code session spawn needed

**Cross-agent shared:**
- Same `/skill` names (after prefix config)
- Same SKILL.md prompts
- Different tool name resolution runtime

---

## Configuration knobs

| Knob | File | Effect |
|------|------|--------|
| `skill_prefix` | `~/.gstack/config.yaml` | Short vs namespaced names |
| `auto_upgrade` | `~/.gstack/config.yaml` | Throttled hourly vs manual |
| Host selection | CLI flag `--host <name>` | Explicit target |
| Team mode | `./setup --team` | Auto-update discipline for shared repos |
| Telemetry | `gstack-config set telemetry on/off` | Opt-in data sharing |

---

## Recipes

### Recipe 1: Fresh install, auto-detect

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup
```

Detects your harnesses (Claude/Codex/Cursor/etc.) and installs all.

### Recipe 2: Multi-harness dev machine

```bash
cd ~/.claude/skills/gstack
./setup --host claude
./setup --host codex
./setup --host cursor
```

Each harness gets own install. Skills update via single repo pull.

### Recipe 3: Contribute new host support

Per `docs/ADDING_A_HOST.md`:
1. Create `hosts/<name>.ts` with host config
2. Add to `hosts/index.ts` registry
3. Test `./setup --host <name>`

**Zero code changes elsewhere.** Declarative pattern.

### Recipe 4: OpenClaw native (no Claude Code)

```bash
clawhub login
clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

Conversational skills — no Claude Code spawn needed.

### Recipe 5: Dispatch-routing (OpenClaw → Claude Code)

**AGENTS.md in OpenClaw repo:**
```
When spawning Claude Code for coding work, tell session to use gstack.
Examples:
- Security audit: "Load gstack. Run /cso"
- Code review: "Load gstack. Run /review"
- QA test: "Load gstack. Run /qa https://..."
- Build feature: "Load gstack. Run /autoplan, implement, run /ship"
```

**User flow:**
```
You: "Run security audit on this repo"
OpenClaw: [spawns Claude Code with: Load gstack. Run /cso]
```

→ gstack functions as **shared standard vocabulary** across AI agents.

### Recipe 6: Team mode + CI enforcement

```bash
cd ~/.claude/skills/gstack && ./setup --team
cd <your-repo>
~/.claude/skills/gstack/bin/gstack-team-init required
git add .claude/ CLAUDE.md && git commit -m "require gstack"
```

- `required`: repo requires gstack for AI work (commit fails otherwise?)
- `optional`: repo recommends gstack but doesn't enforce

---

## Advanced patterns

### Pattern: Declarative host configuration

Type-safe `hosts/<name>.ts` với shared schema. Adding harness = 1 file. **Most elegant of 3 sibling distribution models.**

→ **Reusable** cho any cross-target tool (CLI, library, framework).

### Pattern: Auto-detect at install time

`./setup` without flags detects installed harnesses. User doesn't need to know which they have.

### Pattern: Team mode with silent auto-update

Throttled hourly, network-failure-safe, completely silent. User invisible discipline.

→ **Critical for team adoption:** nobody wants to "remember to update" a shared tool.

### Pattern: OpenClaw native vs Claude Code spawn

Same skill delivered 2 ways:
1. **Native OpenClaw:** conversational, no spawn
2. **Claude Code spawn:** full skill with tool access

→ **Flexibility:** simple skills conversational (OpenClaw), complex skills spawn Claude Code.

### Pattern: Prefix switch without data migration

`./setup --prefix` changes `/qa` → `/gstack-qa` across entire install. Persists in config.

→ **Namespace collision resolution** without reinstall.

---

## Combination với building blocks khác

### + Specialist Roles
Same 23 roles deploy to 10 hosts. Tool name mapping runtime handles differences.

### + Sprint Pipeline
Pipeline concept portable. `/office-hours` → `/plan-ceo-review` chain works trên Claude Code AND Codex AND Cursor.

### + Browser Daemon
Daemon is Claude Code-primary. Some hosts (Codex CLI) don't have browser support — those specialist roles degrade gracefully.

### Cross-project: + Superpowers Distribution Model
**Convergent:** both prioritize cross-harness portability.
**Divergent:** Superpowers uses `.<harness>/` folders (7 harnesses); gstack uses `hosts/<name>.ts` (10 harnesses). gstack more declarative, Superpowers more manifest-heavy.

### Cross-project: + ECC Plugin Model
ECC is Claude Code-first với plugin extensions. gstack is multi-host from day 1. Different philosophies about "primary host."

---

## Anti-patterns

❌ **Vendor gstack into project repo** — deprecated pattern. Use global install + `./setup --team` instead.

❌ **Manual maintain per-host installs** — `./setup` handles detection + install. Don't reimplement.

❌ **Hardcode host-specific paths trong skills** — skills must be host-agnostic. Config per host lives in `hosts/<name>.ts`.

❌ **Skip team mode for shared repos** — individual installs will drift. Team mode enforces version coherence.

❌ **Mix prefix modes across team** — some use `/qa`, others `/gstack-qa` = confusion. Team should pick one.

❌ **Install on unsupported host** — if no `hosts/<name>.ts` exists, skills don't map. Fork + add host first.

❌ **Expect all 23 roles work on all 10 hosts** — hosts without browser lose `/qa`, `/design-review`, `/browse`. Document per host.

---

## Cross-references

- [[(C) Sprint Pipeline]] — workflow portable cross-host
- [[(C) Specialist Roles]] — 23 roles deploy to 10 hosts
- [[(C) Browser Daemon Architecture]] — Claude Code primary
- [[(C) README summary]] — install matrix
- [[(C) CLAUDE.md summary]] — platform-agnostic design mandate
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Distribution Model.md` — per-harness manifest comparison
- Cross-project: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Plugins.md` — plugin model comparison

## Citations

- README.md lines 113-136 (10-host install matrix)
- README.md lines 74-113 (OpenClaw integration + native skills)
- CLAUDE.md lines 86-120 (hosts/ folder structure)
- CHANGELOG v0.15.6.0 "Declarative Multi-Host Platform"
- CHANGELOG v0.15.13.0 "Team Mode"

## TODO

- ⏸ Read `hosts/claude.ts` + `hosts/index.ts` source — verify config schema
- ⏸ Read `docs/ADDING_A_HOST.md` — exact contract cho adding new host
- ⏸ Verify `gstack-team-init required` enforces at git commit level (hook?)
- ⏸ Test cross-host behavior: run `/qa` on Cursor — does browser daemon work?
- ⏸ Compare OpenClaw native skills format với Claude Code skill format — same or different?
