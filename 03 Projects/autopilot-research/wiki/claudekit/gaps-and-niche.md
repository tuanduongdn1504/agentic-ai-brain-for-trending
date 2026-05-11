# Gaps + niche positioning

> What ClaudeKit explicitly does NOT solve, where it fits relative to alternatives. Source: synthesis section "What ClaudeKit does NOT cover".

## Explicitly out-of-scope

### 1. Model provisioning / subscriptions

ClaudeKit is a **productivity layer, not an AI model provider**. Users must maintain their own subscriptions:
- Claude Pro / Team / Enterprise (for Anthropic native)
- GPT subscription (for routing via CCS)
- GLM / Kimi credentials (for alternative providers)

CCS routing does NOT generate more quota — it just moves the work to a different pool.

### 2. Hard enforcement of rules

`CLAUDE.md` is treated as "guidance — a recipe book", NOT absolute enforcement. The AI may still miss instructions.

Docs explicitly recommend: for **guaranteed enforcement** (auto-formatting, blocking commands), use **Hooks** or **Permissions in `settings.json`**, not CLAUDE.md text.

This is the same point as Mnilax's "CLAUDE.md is advisory" framing — both systems acknowledge the soft-rule limit.

### 3. Absolute security safety

Auto Mode for permissions explicitly labeled **"Research Preview"**:
- Safer than full bypass
- NOT 100% secure against hallucinations or destructive commands (e.g., `rm -rf`)

For high-risk operations, docs recommend running in **container or isolated VM**.

### 4. Automated backups

Destructive commands like `ck init --fresh` (full reset) have **NO auto-backup**. Users warned to manually back up configs.

This is a notable gap — `--dry-run` exists for migration but not for `--fresh` reset.

### 5. Native IDE chat replacement

ClaudeKit configuration only applies to the **Claude Code extension** within VS Code / Cursor / Windsurf.

It does NOT affect:
- Native AI chat features built into those IDEs
- Standalone IDE AI assistants (e.g., Cursor's Tab autocomplete, Windsurf Cascade)

ClaudeKit + Cursor Tab = two separate AI experiences sharing the editor.

### 6. Infinite context management

Session recovery exists but does NOT solve context bloat:
- Sessions >100K tokens become "bloated"
- `/resume` won't help — manual `/export` and fresh restart required

This is the gap [[failure-modes-and-recovery#2-context-bloat]] discusses. Operationally Lopopolo's harness-engineering solves this with Symphony's per-task worktree isolation — ClaudeKit doesn't have that infrastructure layer.

### 7. Quota generation

Stated explicitly: CCS allows account rotation but cannot generate more quota. Shared upstream pools still hit limits.

## Niche positioning

### vs Raw Claude Code

| Raw Claude Code | ClaudeKit |
|---|---|
| Interactive terminal chatbot | **Professional automation system** |
| Manual "chatting" | Structured "commands" (`/ck:fix` vs "fix this bug") |
| One conversation thread per session | Workflows + state persistence + checkpoints |
| Bring-your-own-rules via CLAUDE.md | 50+ pre-built commands + curated agents |

**ClaudeKit's niche vs raw Claude Code:** the "Claude Code with batteries included" experience. Pre-built command surface saves user from building their own framework. Trade-off: less customization than building bespoke.

### vs Codex CLI (OpenAI)

| Codex CLI | ClaudeKit |
|---|---|
| Native runtime for OpenAI models | **Intelligence layer** (skills, agents, rules) |
| Provider-locked (OpenAI) | Multi-provider via CCS + migration via `ck migrate` |
| Lean runtime focus | Management features (quota tracking, dashboard) |

**ClaudeKit's niche vs Codex:** the management + abstraction layer. ClaudeKit can be installed INTO Codex CLI (via `ck migrate`) to add ClaudeKit's intelligence on top of Codex's runtime.

### vs IDE-locked tools (Cursor, Windsurf, etc.)

| IDE-locked tools | ClaudeKit |
|---|---|
| Locked to specific IDE | **CLI-first, modular, portable** |
| Intelligence tied to vendor's product | `ck migrate` exports intelligence to other tools |
| Single-provider runtime | Multi-provider via CCS |

**ClaudeKit's niche vs IDE tools:** portability. Users who fear vendor lock-in can develop their "intelligence layer" once and migrate it across Cursor / Windsurf / Codex / Droid.

## Gaps a personal harness must close

If you adopt ClaudeKit but want production-grade reliability, these gaps remain for the user to fill:

| Gap | What user must add |
|---|---|
| **State/config backups** | Pre-`--fresh` backup script (`tar czf .claude-backup-$(date +%s).tar.gz .claude/`) |
| **Hard enforcement of CLAUDE.md** | Git hooks (`pre-commit`) + CI gates to enforce coding standards ClaudeKit only "suggests" |
| **Cross-account session sync** | Manual `.jsonl` file copies between CCS profiles when needed |
| **Security sandboxing** | Container or isolated VM for `bypassPermissions` mode |
| **Token budget enforcement** | External monitoring on token spend; CCS provides usage data but no budget alerts |
| **Test intent verification** | External test-quality linting (mutation testing, snapshot review) — `/ck:test` runs tests but doesn't verify their semantics |

## Niche map: where each tool fits

```
                              ┌──── Org / Team Scale ────┐
                              │  Lopopolo's harness eng  │
                              │  (Symphony + Frontier)   │
                              │  - Dark Factory          │
                              │  - 1M LOC, 7-eng team    │
                              │  - $2-3K/day token spend │
                              └──────────────────────────┘
                                          ▲
                                          │ growing infrastructure
                                          │
                              ┌──── Multi-Provider Portable ────┐
                              │  ClaudeKit                      │
                              │  (CCS + ck migrate)             │
                              │  - Pre-built commands           │
                              │  - Agent/Skill/Workflow/Hook    │
                              │  - Individual + small team      │
                              └─────────────────────────────────┘
                                          ▲
                                          │ adding structure
                                          │
                              ┌──── Single-Tool Individual ────┐
                              │  Raw Claude Code + CLAUDE.md   │
                              │  (Mnilax 12-rule template)     │
                              │  - 12 behavioral rules         │
                              │  - 200-line CLAUDE.md ceiling  │
                              │  - Individual developer        │
                              └────────────────────────────────┘
                                          ▲
                                          │ getting started
                                          │
                              ┌──── No Structure ────┐
                              │  Bare Claude Code    │
                              │  (chat-style usage)  │
                              └──────────────────────┘
```

User progresses up the stack as their workflow complexity grows. Bare → Mnilax 12-rule template → ClaudeKit framework → harness-engineering-class infrastructure.

## Key Takeaways

- **ClaudeKit is "professional Claude Code with batteries included"** — saves framework-building work; trade-off is reduced customization
- **7 explicit out-of-scope areas** the user must cover externally — most consequential are hard enforcement, backup, security sandboxing
- **Niche superpowers:** CCS multi-provider routing + `ck migrate` portability — neither raw Claude Code nor harness-engineering has these
- **`/ck:*` 50+ command surface** is the user-facing value — but the same surface is also the highest cognitive load to learn
- **The 4-tool stack ladder** (Bare → Mnilax → ClaudeKit → Harness-engineering) is a useful mental map for "what to adopt when"
- ClaudeKit fits **individual + small team scale** — neither fully bare nor org-scale
