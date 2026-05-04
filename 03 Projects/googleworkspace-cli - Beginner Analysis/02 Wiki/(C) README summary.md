# (C) README summary — googleworkspace/cli (`gws`)

> **Source:** `README.md` — WebFetch 2026-04-19
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Positioning + tagline

**Tagline:** *"One CLI for all of Google Workspace — built for humans and AI agents. Drive, Gmail, Calendar, and every Workspace API."*

**Binary name:** `gws`

**Signals:**
- **Dual audience** — humans AND AI agents (explicit). No prior corpus project articulates dual-audience this clearly.
- **Unified scope** — "all of Google Workspace" positioning, not single-service bridge (contrast: notebooklm-py v7 is NotebookLM only)
- **API breadth** — "every Workspace API" is a bold claim, backed by Dynamic Discovery Service architecture

## 2. Supported services (11+ APIs)

From README §Prerequisites + Quick Start:

1. **Drive** — file storage + sharing
2. **Gmail** — email operations
3. **Calendar** — events + agenda
4. **Sheets** — spreadsheet operations
5. **Docs** — document creation/editing
6. **Chat** — Google Chat messaging
7. **Admin** — enterprise user/group management
8. **Script** — Apps Script push
9. **Workflow** — custom multi-step workflows (meeting-prep, standup-report, etc)
10. **Events** — event subscriptions (Drive changes, Gmail events)
11. **Model Armor** — Google's response sanitization layer

Plus: tool dynamically discovers ALL endpoints via Google Discovery Service. The 11 above are first-class; **any** Google Workspace API Discovery exposes becomes accessible.

**Contrast with notebooklm-py (T4 N=1):** single service (NotebookLM). googleworkspace/cli = 11+ services. **11× service scope.**

## 3. Installation — 5 channels

| Channel | Command | Use case |
|---------|---------|----------|
| Pre-built binaries | GitHub Releases download | Individual users, macOS/Linux/Windows |
| npm | `npm install -g @googleworkspace/cli` | JS/TS ecosystem users |
| Cargo | `cargo install --git https://github.com/googleworkspace/cli --locked` | Rust users, latest main |
| Nix | `nix run github:googleworkspace/cli` | Nix users (niche) |
| Homebrew | `brew install googleworkspace-cli` | macOS users |

**Also:**
- Gemini CLI extension: `gemini extensions install https://github.com/googleworkspace/cli`
- OpenClaw: symlink-based install via skills

**5 primary channels + extensions.** Second-broadest install matrix in corpus after codymaster's 8+ (v12).

## 4. Authentication — multi-flow OAuth2

**4 authentication modes:**

| Mode | Trigger | Credential storage |
|------|---------|--------------------|
| **Interactive local** | `gws auth setup`, browser flow | Encrypted (AES-256-GCM) in OS keyring |
| **Headless/CI** | `gws auth export` produces credentials file | File-based, user manages |
| **Service account** | `GOOGLE_APPLICATION_CREDENTIALS` env | File path to service account JSON |
| **Pre-obtained token** | `GOOGLE_WORKSPACE_CLI_TOKEN` env | Externally-minted token accepted |

**Priority resolution:** environment variables > credentials file > encrypted local > plaintext config

**OAuth scope presets:**
- **Testing mode:** ~25 scopes (Google's testing-mode OAuth apps have scope limit)
- **Recommended:** 85+ scopes (curated preset for production)

**Security discipline (from AGENTS.md §Input Validation):**
- Assume CLI args are adversarial
- Validators: `validate_safe_output_dir`, `validate_safe_dir_path`, `validate_resource_name`, `encode_path_segment`
- Environment variables = trusted inputs (exempt from traversal validation)

**Most enterprise-grade auth in corpus.** Prior T1/T4 auth models are either simple API-key (notebooklm-py unofficial) or service-specific (BMAD uses Claude's implicit auth).

## 5. Command structure

### Core syntax
```bash
gws <service> <resource> [sub-resource] <method> [flags]
```

### Discovery-generated methods
Auto-generated from Discovery Service per service:
- `gws drive files list`
- `gws gmail users messages list`
- `gws calendar events insert`

### Helper commands (prefix `+`)
Handwritten multi-step orchestration:
- `gws gmail +send`, `gws gmail +reply`, `gws gmail +triage`, `gws gmail +watch`
- `gws sheets +append`, `gws sheets +read`
- `gws calendar +agenda`, `gws calendar +insert`
- `gws docs +write`
- `gws chat +send`
- `gws workflow +standup-report`, `gws workflow +meeting-prep`
- `gws events +subscribe`, `gws events +renew`
- `gws drive +upload` (multipart upload)

### Schema introspection
- `gws schema <service>.<method>` — print JSON schema for agent to inspect before call

### Auth commands
- `gws auth setup` (initial)
- `gws auth login` (re-login)
- `gws auth export` (headless/CI credentials file)

### Key flags
- `--params '<JSON>'` — query/URL params
- `--json '<JSON>'` — request body
- `--page-all` — auto-paginate with NDJSON output
- `--page-delay` — pagination throttle (default 100ms)
- `--dry-run` — preview mutating operation without execution
- `--fields "<mask>"` — limit response fields (agent context window protection)

## 6. AI-agent design patterns

**README explicitly designs for agent use:**

1. **Structured JSON output** — every response is JSON, not human-formatted text
2. **NDJSON streaming** — `--page-all` emits one JSON object per line (consumable by agents)
3. **Schema introspection** — `gws schema` lets agent see expected input/output
4. **Dry-run preview** — mutating ops can preview JSON payload first
5. **Field masks** — `--params '{"fields": "id,name"}'` limits response size for context budget
6. **Auto-pagination with throttle** — agents don't loop-paginate manually

**From CONTEXT.md §Rules of Engagement for Agents:**
- "If you don't know the exact JSON payload structure, run `gws schema` first"
- "ALWAYS use field masks...to avoid overwhelming your context window"
- "Always use `--dry-run` flag for mutating operations"

**This is the most deliberate agent-user documentation in corpus.**

## 7. 110 Skills (detailed in cluster summary)

README mentions "100+ curated agent skills" — actual count from skills/ listing: **110 folders**:

- **44 gws-\* service skills** — one per service + sub-operation (gws-drive, gws-drive-upload, gws-gmail, gws-gmail-send, gws-gmail-triage, etc)
- **10 persona skills** — role-based bundles: team-lead, exec-assistant, content-creator, customer-support, event-coordinator, hr-coordinator, it-admin, project-manager, researcher, sales-ops
- **56 recipe skills** — workflow recipes: backup-sheet-as-csv, batch-invite-to-event, block-focus-time, meeting-prep, standup-report, weekly-digest, etc

**Install:** `npx skills add https://github.com/googleworkspace/cli`
**Select bundles:** `gws-drive`, `gws-gmail`, etc
**OpenClaw support:** symlink-based install

**Persona + recipe layer is NOVEL in corpus.** Prior skills taxonomies (ECC/Superpowers/codymaster) group by function, not by role/workflow-type.

## 8. Gemini CLI extension vs Claude Code integration

**Gemini:**
- First-class extension: `gemini extensions install https://github.com/googleworkspace/cli`
- Inherits authentication automatically
- `gemini-extension.json` manifest at repo root

**Claude Code:**
- CLAUDE.md at repo root is **1-liner:** "When contributing to this repository, you must strictly follow all guidelines outlined in the AGENTS.md file."
- No dedicated Claude Code plugin manifest
- Skills installable via standard `npx skills add`

**Asymmetry:** Gemini gets deeper integration (extension with auth inheritance); Claude Code gets standard skill install path. Expected given Google org.

## 9. Model Armor (response sanitization)

**First Google safety-layer in corpus.**

- Sanitizes API responses before agent sees them
- Prevents prompt injection attacks via response content
- Env vars: `GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE`, `GOOGLE_WORKSPACE_CLI_SANITIZE_MODE` (warn/block)
- Skills: gws-modelarmor, gws-modelarmor-sanitize-prompt, gws-modelarmor-sanitize-response, gws-modelarmor-create-template

**Agent safety layer built-in.** Contrast: notebooklm-py (T4 N=1) has no safety layer; codymaster's Self-Healing is about skill health, not content safety.

## 10. Architecture (two-phase parsing)

Per README §Architecture:

1. **Identify service** from `argv[1]` (e.g., `drive`)
2. **Fetch cached Discovery Document** for that service
3. **Build clap Command tree** from Discovery JSON schema
4. **Re-parse remaining args** against the dynamically-built tree
5. **Authenticate** and execute API call
6. **Output structured JSON**

**Cache:** Discovery Documents cached locally (TTL unknown — Q24)

**Dynamic over static rationale (from AGENTS.md):**
- Google APIs evolve; dynamic always-fresh
- No crate maintenance for each API
- Registration is 1-line: add service to `services.rs`
- Single binary supports ALL Google Workspace APIs

## 11. Environment variables (20+)

**Authentication:**
- `GOOGLE_WORKSPACE_CLI_TOKEN` — pre-obtained OAuth token (highest priority)
- `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` — JSON credentials file
- `GOOGLE_WORKSPACE_CLI_KEYRING_BACKEND` — `keyring` or `file`
- `GOOGLE_APPLICATION_CREDENTIALS` — standard ADC fallback

**Configuration:**
- `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` — override `~/.config/gws`

**OAuth Client:**
- `GOOGLE_WORKSPACE_CLI_CLIENT_ID`, `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET`

**Sanitization:**
- `GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE`, `GOOGLE_WORKSPACE_CLI_SANITIZE_MODE`

**Logging:**
- `GOOGLE_WORKSPACE_CLI_LOG` — stderr filter
- `GOOGLE_WORKSPACE_CLI_LOG_FILE` — JSON-line log dir with rotation

**Helpers:**
- `GOOGLE_WORKSPACE_PROJECT_ID` — GCP project

## 12. Version + release cadence

- **Current:** v0.22.5 (March 31, 2026 per GitHub API)
- **44 releases** over ~1 year → ~weekly cadence
- **Pre-1.0** — README notes: "Expect breaking changes as we march toward v1.0"
- **Changesets:** every PR has `.changeset/<name>.md` with patch/minor/major

**Release discipline parallel to BMAD v11** — structured changesets + weekly cadence. Google applies same professional release pattern.

## 13. Cross-references to T4 peer (notebooklm-py)

| Axis | notebooklm-py (v7) | googleworkspace/cli (v13) |
|------|--------------------|--------------------------|
| Service scope | NotebookLM (1) | 11+ Workspace services |
| Official status | Unofficial solo | **Official Google** |
| Language | Python | **Rust** |
| License | MIT | **Apache-2.0** |
| Stars | 11K | **25K** |
| Install channels | 1 (pip/npm single) | **5+** |
| Skill count | 1 mega-SKILL.md | **110 skills** |
| Architecture | Reverse-engineered API wrapper | **Dynamic Discovery API** |
| Auth | Unofficial session-based | **Official OAuth2 multi-flow** |
| Safety layer | ❌ | **✅ Model Armor** |
| Agent docs | Single SKILL.md | **Tri-file (CLAUDE+AGENTS+CONTEXT)** |

→ **Different T4 archetype:** notebooklm-py = unofficial-solo-specialist (single service, community-built); gws = official-corporate-generalist (multi-service, Google-shipped).

**Subcategorization hypothesis confirmed:** T4 splits along same axis as T5 (v10 deer-flow corporate-generalist vs autoresearch solo-specialist).

## 14. Exact section headers (from README TOC)

Prerequisites / Installation / Quick Start / Why gws? / Authentication / AI Agent Skills / Gemini CLI Extension / Advanced Usage / Multipart Uploads / Pagination / Google Sheets — Shell Escaping / Helper Commands / Model Armor (Response Sanitization) / Environment Variables / Exit Codes / Architecture / Troubleshooting / Development / License / Disclaimer

**Most complete section taxonomy in corpus.** Structured like a professional product document.

## Open questions surfaced

- Rust choice rationale (Q4)
- Discovery cache TTL (Q24)
- Model Armor availability model (Q6)
- OAuth "recommended" preset curation (Q13)
- Pagination 100ms default rationale (Q22)
