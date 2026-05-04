# (C) 14-Harness npm Distribution

> **Source:** README.md lines 107-200, package.json (inferred)
> **Ingested:** 2026-04-18
> **Type:** Entity page (distribution concept) — entity #4 cho GSD

---

## One-liner

**VI:** GSD's distribution model là **npm-first single-command install** (`npx get-shit-done-cc@latest`) với **interactive harness + location selector**. Supports **14 AI coding harnesses** — most của any framework (ECC 5, Superpowers 7, gstack 10, GSD 14). Bonus: `@gsd-build/sdk` npm package (gsd-sdk CLI) auto-installed. Match npm ecosystem conventions vs git-clone approach của siblings.

**EN:** npm-first distribution with `npx get-shit-done-cc@latest`, interactive harness/location picker, 14 AI coding harnesses supported. Plus auto-install of `@gsd-build/sdk` npm package.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Cài GSD lần đầu (npm command)
- Compare distribution models across 5 projects
- Add GSD support cho new harness (contribution opportunity)
- Troubleshoot install failures

---

## Comparison sibling distribution

| Axis | ECC | Superpowers | gstack | goclaw | **GSD** |
|------|-----|-------------|--------|--------|---------|
| Primary install | Plugin + manual | Claude marketplace + git URL | `./setup` script + git clone | Docker + binary + desktop | **`npx` one-liner** |
| Package manager | N/A | N/A | N/A | N/A | **npm (`get-shit-done-cc`)** |
| Interactive picker | ❌ | ❌ | Minimal | Onboarding wizard | **✅ Runtime + location picker** |
| Harness count | 5 | 7 | 10 | Self-hosted | **14** |
| Update mechanism | Plugin refresh | `gstack-upgrade` | marketplace refresh / git pull | Docker pull | **`npx get-shit-done-cc@latest` again** |
| Non-interactive install | N/A | git+harness manual | `--host <name>` flag | Env vars | **`--claude --global` flags (15+ flags)** |
| SDK package | None | None | None | internal | **`@gsd-build/sdk` npm auto-installed** |
| Community ports | N/A | N/A | N/A | N/A | **README mentions "Community Ports"** |

→ **GSD leverages npm ecosystem most elegantly.** Others require git familiarity.

---

## Sub-types: 14 supported harnesses

### Detailed install matrix

| Harness | Flag | Global path | Local path |
|---------|------|-------------|------------|
| **Claude Code** | `--claude` | `~/.claude/` | `./.claude/` |
| **OpenCode** | `--opencode` | `~/.config/opencode/` | (implicit) |
| **Gemini CLI** | `--gemini` | `~/.gemini/` | (implicit) |
| **Kilo** | `--kilo` | `~/.config/kilo/` | `./.kilo/` |
| **Codex** | `--codex` | `~/.codex/` | `./.codex/` |
| **Copilot** | `--copilot` | `~/.github/` | `./.github/` |
| **Cursor CLI** | `--cursor` | `~/.cursor/` | `./.cursor/` |
| **Windsurf** | `--windsurf` | `~/.codeium/windsurf/` | `./.windsurf/` |
| **Antigravity** | `--antigravity` | `~/.gemini/antigravity/` | `./.agent/` |
| **Augment** | `--augment` | `~/.augment/` | `./.augment/` |
| **Trae** | `--trae` | `~/.trae/` | `./.trae/` |
| **Qwen Code** | `--qwen` | `~/.qwen/` | `./.qwen/` |
| **CodeBuddy** | `--codebuddy` | `~/.codebuddy/` | `./.codebuddy/` |
| **Cline** | `--cline` | `~/.cline/` | `./.clinerules` |

**Plus:** `--all` → all at once.

### Harness tiers (inferred)

**Tier 1 Primary** (documented thoroughly):
- Claude Code, OpenCode, Gemini CLI, Codex, Copilot, Cursor

**Tier 2 Secondary**:
- Kilo, Windsurf, Antigravity, Augment, Trae, Qwen Code, CodeBuddy, Cline

**Tier 3 Community ports** (README mentions section "Community Ports" — line 892):
- Not deep-read; likely user-maintained adapters for other harnesses

→ **Ecosystem inclusivity.** More harnesses supported = broader reach.

---

## Anatomy: Install flow

### Interactive mode (default)

```bash
npx get-shit-done-cc@latest
  ↓
Installer prompts:
  1. Choose runtime: [Claude Code, OpenCode, ... or all]
     (interactive multi-select — pick multiple in single session)
  2. Choose location: [Global (all projects) | Local (current project only)]
  ↓
Install to chosen paths
  ↓
Auto-install @gsd-build/sdk (gsd-sdk CLI)
  ↓
Run /gsd-help to verify
```

### Non-interactive mode (CI, Docker, scripts)

```bash
# Claude Code global
npx get-shit-done-cc --claude --global

# Codex local
npx get-shit-done-cc --codex --local

# All harnesses global
npx get-shit-done-cc --all --global

# Skip SDK install
npx get-shit-done-cc --claude --global --no-sdk
```

→ **Scriptable.** Good cho CI, Docker image bakes.

---

## Cơ chế

### Mechanism 1: npm package `get-shit-done-cc`

Published to npmjs.com. Each `npx ... @latest` pulls newest version. **Auto-versioned.**

### Mechanism 2: `@gsd-build/sdk` auto-install

Per CHANGELOG Unreleased:
> "Installer now installs `@gsd-build/sdk` automatically so `gsd-sdk` lands on PATH. Resolves `command not found: gsd-sdk` errors..."

SDK = required by `/gsd-*` commands. Without SDK, commands fail at runtime.

**Flags:**
- `--no-sdk` opt out
- `--sdk` force reinstall

### Mechanism 3: Interactive multi-select

Installer uses Node.js prompts library (inferred). User picks 1+ runtimes với space-bar multi-select.

→ **Supports multi-harness user** (dev who uses both Claude Code AND Codex).

### Mechanism 4: Skill format auto-detection per harness

Per README note:
> "Claude Code 2.1.88+, Qwen Code, and Codex install as skills (`.claude/skills/`, `./.codex/skills/`, or the matching global `~/.claude/skills/` / `~/.codex/skills/` roots). Older Claude Code versions use `commands/gsd/`."

Installer detects harness version, chooses correct install path automatically.

**Canonical contract:** `docs/skills/discovery-contract.md`

### Mechanism 5: Verification per harness

Post-install, different verification per harness:
- Claude Code / Gemini / Copilot / Antigravity / Qwen Code: `/gsd-help`
- OpenCode / Kilo / Augment / Trae / CodeBuddy: `/gsd-help`
- Codex: `$gsd-help` (different invocation)
- Cline: check `.clinerules` exists (no `/help` command)

→ **Handles harness conventions.**

### Mechanism 6: Development install (contributor mode)

```bash
git clone https://github.com/gsd-build/get-shit-done.git
cd get-shit-done
npm run build:hooks
node bin/install.js --claude --local
```

**`build:hooks` step required** — compiles hook sources into `hooks/dist/` before install. Normal npm release handles this via `prepublishOnly`.

→ **Build step separates source từ installable artifact.**

### Mechanism 7: Update = re-run

```bash
npx get-shit-done-cc@latest
```

Same command re-runs installer với latest version. Overwrites installed files.

→ **Simple mental model.** No separate `update` subcommand needed (though `/gsd-update` exists cho in-Claude-Code invocation).

---

## Out-of-box behavior

**After install:**
- All 33 agents + 83 commands + 11 hooks installed to chosen harness path
- `gsd-sdk` CLI available on PATH (via `@gsd-build/sdk` npm package)
- `/gsd-help` verifies (Claude Code)
- No `.planning/` yet (created on first `/gsd-new-project`)

**First usage:**
```
/gsd-new-project
```

Triggers interactive onboarding, creates `.planning/` in current repo.

---

## Configuration knobs

| Knob | Default | Effect |
|------|---------|--------|
| Install location | interactive | Global (all projects) vs Local (current) |
| Runtime | interactive multi-select | One or more of 14 |
| `--no-sdk` flag | false | Skip gsd-sdk CLI install |
| `--sdk` flag | false | Force reinstall SDK |
| `--all` flag | false | Install to all 14 harnesses |
| Skill format (Claude) | auto-detect | `.claude/skills/` (2.1.88+) vs `commands/gsd/` (older) |

---

## Recipes

### Recipe 1: Fresh install for Claude Code (most common)

```bash
npx get-shit-done-cc@latest
# Pick: Claude Code
# Pick: Global (recommended)
```

Or non-interactive:
```bash
npx get-shit-done-cc --claude --global
```

### Recipe 2: Multi-harness setup (team with mixed tooling)

```bash
npx get-shit-done-cc --all --global
```

All 14 harnesses installed. Every team member's tool works.

### Recipe 3: Update to latest

```bash
npx get-shit-done-cc@latest
# Overwrites current install với newest version
```

Or in-session:
```
/gsd-update
```

### Recipe 4: Clean install after failed update

```bash
# Remove old
rm -rf ~/.claude/skills/gsd   # or wherever

# Fresh install
npx get-shit-done-cc --claude --global --sdk
```

### Recipe 5: Docker/CI install

```dockerfile
RUN npx get-shit-done-cc --claude --global --no-sdk
```

`--no-sdk` if SDK not needed in container (e.g., just running agents, not GSD CLI).

### Recipe 6: Contributor development install

```bash
git clone https://github.com/gsd-build/get-shit-done.git ~/gsd-dev
cd ~/gsd-dev
npm install
npm run build:hooks
node bin/install.js --claude --local   # installs to ./.claude/
```

Test modifications before PR.

### Recipe 7: Non-Claude-Code harness (e.g., Codex)

```bash
npx get-shit-done-cc --codex --global
# Verify: $gsd-help (note: $ prefix, not /)
```

---

## Advanced patterns

### Pattern 1: npm as distribution backbone

Leverages existing infrastructure:
- npm registry reliability
- `npx` caching (no global install pollution)
- Version management via semver
- Community tooling (depfu, renovate)

→ **Match OpenAI's `openai` npm package distribution.** Proven pattern.

### Pattern 2: Multi-runtime single-binary

`get-shit-done-cc` binary handles 14 harnesses. Shared code + harness-specific adapters.

→ **Smaller maintenance** vs separate packages per harness.

### Pattern 3: Community ports section

README line 892 has "Community Ports" section. Indicates:
- Canonical 14 harnesses supported by core team
- Community maintains adapters for others
- Distributed maintenance model

### Pattern 4: SDK as separate package

`@gsd-build/sdk` separate từ `get-shit-done-cc`:
- Core CLI runtime (SDK) can version independently
- Bug fixes to SDK don't require full CLI reinstall
- Multiple CLIs could share SDK (future-proofing)

### Pattern 5: Auto-install dependencies

`@gsd-build/sdk` auto-installed with `get-shit-done-cc`. User doesn't need to know about SDK.

→ **Transparent UX.** User installs 1 thing, gets working system.

### Pattern 6: Harness version detection

Claude Code 2.1.88+ → skills format. Older → commands/gsd/. **Handle version drift transparently.**

### Pattern 7: Flag explosion handled via `--all`

14 flags = a lot to remember. `--all` aggregates.

→ **Escape hatch for complexity.**

---

## Combination với building blocks khác

### + Context Rot Solution
Install once per harness. Rot prevention uniform.

### + 5-Step Workflow
Workflow commands installed to harness's command path. `/gsd-next` works same cross-harness.

### + 33 Specialized Agents + Commands
All agents/commands install atomically. No pick-and-choose (vs ECC plugin model).

### + Hooks
Hooks install to each harness's hook directory. 11 .js/.sh files per install.

### Cross-project: + ECC Plugin model
Different mechanism:
- ECC: plugin install via Claude Code's plugin system
- GSD: npm package install to harness's skills/commands directory

Trade-off:
- ECC: Claude Code-native but less portable
- GSD: npm-portable but requires Node.js

### Cross-project: + Superpowers marketplace + git URL
Different mechanism:
- Superpowers: 2 channels (Claude marketplace + git URL)
- GSD: npm (single channel)

Trade-off:
- Superpowers: multiple paths, flexibility
- GSD: single command, simplicity

### Cross-project: + gstack `./setup` script
Different mechanism:
- gstack: clone + run script
- GSD: npm oneliner

Trade-off:
- gstack: no npm dependency
- GSD: no git knowledge needed

### Cross-project: + goclaw Docker/binary
Different TIER (Tier 2 platform vs Tier 1 assistant). Not directly comparable.

---

## Anti-patterns

❌ **Manual file copy** — bypasses npm, update path breaks. Use `npx`.

❌ **Edit installed files directly** — overwritten on next update. Fork repo if customization needed.

❌ **Mix install mechanisms** — use `npx` OR git clone + build, not both. Conflict possible.

❌ **Skip `--sdk`** — some commands fail without SDK. Default auto-installs, don't disable unless CI.

❌ **Use `--no-sdk` in dev** — debug pain later when commands fail cryptically.

❌ **Install to wrong location** — local install vs global matters. Local = `./.claude/`, global = `~/.claude/`. Team members installing locally = repo clutter.

❌ **Run without harness running** — install succeeds silently if harness not installed. Verify harness exists first.

❌ **Assume 14 harnesses work identically** — Claude Code most tested. Others may have edge cases. Check `docs/skills/discovery-contract.md`.

---

## Cross-references

- [[(C) Context Rot Solution]]
- [[(C) 5-Step Workflow]]
- [[(C) 33 Specialized Agents + Commands]]
- [[(C) README summary]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Distribution Model.md`
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) Multi-Host Declarative Platform.md`
- Cross-project: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Plugins.md`

## Citations

- README.md lines 100-200 (install matrix + flags)
- README.md line 117 (Claude Code 2.1.88+ skills note)
- README.md line 119 (canonical discovery contract reference)
- README.md line 196 (SDK flags `--no-sdk` / `--sdk`)
- README.md line 892 (Community Ports section)
- CHANGELOG Unreleased (SDK auto-install fix #2385)

## TODO

- ⏸ Read `docs/skills/discovery-contract.md` — canonical contract
- ⏸ Verify 14 harness list against latest package.json + installer code
- ⏸ Document "Community Ports" section content (line 892-905)
- ⏸ Test: install GSD on Claude Code, verify all 83 commands callable
- ⏸ Benchmark install time vs siblings (ECC plugin, gstack setup, Superpowers marketplace)
