# cc-switch Contributor-Facing Cluster Summary

**Scope:** CONTRIBUTING + Architecture Overview + Development Guide + governance discipline
**Audience:** Contributors + maintainers + reviewers

---

## 1. Project type + workspace

**Tauri 2 application** with Rust backend + React+TypeScript frontend:
- `src/` — React + TypeScript frontend (TanStack Query for cache/sync)
- `src-tauri/` — Tauri Rust backend (Commands → Services → DAO → Database)
- `tests/` — Vitest frontend tests + cargo tests for Rust

Workspace dependencies declared in:
- `package.json` + `pnpm-workspace.yaml` (frontend)
- `Cargo.toml` (Rust workspace via `src-tauri/`)
- `rust-toolchain.toml` (pins Rust 1.85+)

## 2. Environment Requirements

```
Node.js 18+
pnpm 8+
Rust 1.85+
Tauri CLI 2.8+
```

## 3. Development Commands

```bash
pnpm install                          # Install dependencies
pnpm dev                              # Dev mode (hot reload)
pnpm typecheck                        # Type check
pnpm format                           # Format code
pnpm format:check                     # Check format
pnpm test                             # Run frontend unit tests
cargo test                            # Run Rust backend tests
cargo build                           # Build backend
pnpm tauri build                      # Production build
```

## 4. Layered Architecture (Pattern #21 SDD methodology evidence)

**Verbatim from README:** *"Layered Architecture: Clear separation (Commands → Services → DAO → Database)"*

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (React + TS)                    │
│  Components ─→ Hooks ─→ TanStack Query (Cache/Sync)         │
└────────────────────────┬────────────────────────────────────┘
                         │ Tauri IPC
┌────────────────────────▼────────────────────────────────────┐
│                  Backend (Tauri + Rust)                     │
│  Commands ─→ Services ─→ Models/Config (Data)               │
└─────────────────────────────────────────────────────────────┘
```

**Core Design Patterns (verbatim from README):**
- **SSOT** (Single Source of Truth): All data stored in `~/.cc-switch/cc-switch.db` (SQLite)
- **Dual-layer Storage**: SQLite for syncable data, JSON for device-level settings
- **Dual-way Sync**: Write to live files on switch, backfill from live when editing active provider
- **Atomic Writes**: Temp file + rename pattern prevents config corruption
- **Concurrency Safe**: Mutex-protected database connection avoids race conditions
- **Layered Architecture**: Clear separation (Commands → Services → DAO → Database)

## 5. Key Components (from Architecture Overview)

| Service | Responsibility |
|---------|----------------|
| **ProviderService** | Provider CRUD, switching, backfill, sorting |
| **McpService** | MCP server management, import/export, live file sync |
| **ProxyService** | Local proxy mode with hot-switching and format conversion |
| **SessionManager** | Conversation history browsing across all supported apps |
| **ConfigService** | Config import/export, backup rotation |
| **SpeedtestService** | API endpoint latency measurement |

**Pattern #21 sub-variant candidate:** Layered architecture with explicit Service separation = SDD methodology emergence at desktop-app layer. Sister to v66 agentmemory (Pattern #18 shared-backend-service sub-archetype) and v71 agents-best-practices (7-invariant execution-separation loop) — but at PRODUCT-architecture layer rather than agent-architecture layer.

## 6. CHANGELOG discipline (Pattern #83 within-pattern strengthening)

**CHANGELOG.md at 133KB** — corpus-record sustained release narrative in v60+ window.

Likely contains 100+ version entries documenting:
- Provider preset additions
- MCP/Skills/Prompts feature additions
- Tauri framework upgrades
- Bug fixes + security patches

**Inferred Pattern #83 evidence (CHANGELOG-as-disclosure-surface):** Sustained granular release narrative at 133KB suggests Pattern #83 83b methodology-disclosure within-pattern strengthening. Specific evidence verification pending CHANGELOG read.

## 7. Atomic-write config-protection (Pattern #66 architectural primitive)

**Mechanism:** Temp file + rename pattern. SQLite SSOT with mutex-protected concurrency.

**Critical insight:** Configuration corruption is a real failure mode for multi-runtime config aggregators. cc-switch's atomic-write discipline is the architectural response.

**Sub-mechanism candidate within Pattern #66:** "Configuration-integrity-via-atomic-writes-and-SSOT" — corpus-first formal architectural primitive at config-state-layer.

**Cross-reference:** Sister to v69 CloakBrowser's 3-tier signature verification (artifact-layer integrity). v73 cc-switch is config-state-layer integrity discipline.

## 8. Minimal-intrusion design principle (Pattern #66 + Pattern #21 strengthening)

**Verbatim (README FAQ):** *"CC Switch follows a 'minimal intrusion' design principle — even if you uninstall the app, your CLI tools will continue to work normally."*

**Implementation:**
- cc-switch never deletes the user's existing config
- Always keeps one active configuration (cannot delete the active provider — minimum-1-config guarantee)
- Cleanup on uninstall is opt-in, not automatic
- CLI tools' `~/.claude/`, `~/.codex/`, etc. config files persist independently

**Pattern Library implication:** Minimal-intrusion as architectural discipline = Pattern #66 supply-chain-isolation discipline applied to tool-substrate-coexistence-layer.

## 9. macOS code-signing + notarization

**Verbatim:** *"CC Switch for macOS is code-signed and notarized by Apple."*

Apple Developer ID + notarization process. Same level of OS-trust as commercial macOS apps. Distinguishes cc-switch from unsigned binaries (typical for solo-dev tools).

**Pattern #66 evidence:** Higher artifact-layer trust than typical solo-dev tool.

## 10. CONTRIBUTING discipline

`CONTRIBUTING.md` at 9.5KB. Likely contains:
- Issue templates
- PR guidelines
- Code formatting expectations (`pnpm format` + `cargo fmt`)
- Test requirements
- Commit message conventions

## 11. CODE_OF_CONDUCT.md at 9.9KB

Substantial code-of-conduct documentation. Suggests active community management at 75K-star scale.

## 12. SECURITY.md at 2.2KB + SUPPORT.md at 2.7KB

Explicit security disclosure policy + user support discipline.

## 13. Sponsor management (OC-Q candidate)

**20+ sponsor entries** dominate first ~140 lines of README. Each sponsor:
- Banner image in `assets/partners/banners/` or logo in `assets/partners/logos/`
- 2-3 paragraph value-proposition
- Affiliate-style registration link with promotion code

**Management overhead:** Active sponsor relationships at this scale require ongoing maintenance (sponsor onboarding, banner updates, deal-renewal cycles, sponsor-link health checks).

**Pattern Library implication:** Sponsor-density-as-corpus-signal (OC-Q candidate) — when subject domain attracts 10+ sponsors who are all domain-adjacent, this signals strong ecosystem-pull from subject's domain OR strong author-monetization-priority.

## 14. Issue + PR injection awareness (Pattern #66 66e sister)

**Inferred from sponsor density + scale:** With 923 open issues + 4.8K forks + 75K stars, cc-switch attracts substantial promotional/integration requests. Like v72 DeepSeek-TUI AGENTS.md, cc-switch likely has issue-triage discipline for prompt-injection-resistant review.

**v76+ verification:** Check if cc-switch has explicit "issue / PR injection" awareness section in CONTRIBUTING.md or AGENTS.md (not analyzed in v73 build window).

## 15. Cross-references

- **Pattern #21 SDD methodology** — layered architecture (Commands → Services → DAO → Database) at product-architecture layer
- **Pattern #66 atomic-writes-as-architectural-primitive** — sub-mechanism candidate
- **Pattern #78 12-layer LDS strengthening** — multi-runtime-multi-standard integration
- **Pattern #84 84c third-strengthening** — 6-runtime aggregator within sub-mechanism
- **Pattern #57 corpus-recursive STRONGEST** — 3+ corpus subjects cited

---

**Cross-reference:** Pattern Library implications → `entity-3-pattern-library.md`. Distribution architecture → `entity-2-distribution-multi-runtime.md`. Storm Bear methodology-influence → `entity-4-storm-bear.md`.
