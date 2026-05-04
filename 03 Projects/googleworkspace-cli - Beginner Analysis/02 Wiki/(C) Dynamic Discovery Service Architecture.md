# (C) Dynamic Discovery Service Architecture

> **Type:** Entity — novel architecture (most distinct primitive in v13)
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README summary]] §10, [[(C) CONTEXT + CLAUDE + AGENTS cluster summary]] §3 (AGENTS.md §1, §4)
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

googleworkspace/cli implements a **Dynamic Discovery Service** architecture — it does NOT ship pre-generated Rust crates for Google APIs. Instead, `gws` fetches Google's Discovery Document JSON at runtime, builds a `clap` CLI command tree dynamically from the schema, then re-parses arguments against the built tree. Registering a new service is a **1-line change in `services.rs`**; no per-API crate maintenance. This is the **only corpus project using runtime dynamic CLI generation**.

## 2. Key claims

1. **No generated crates** — zero `google-drive3`-style pre-generated Rust API bindings
2. **Runtime Discovery** — fetch JSON + build clap tree at launch
3. **Two-phase argument parsing** — service identification → tree build → re-parse
4. **Cache-backed** — Discovery Documents cached locally (TTL TBD)
5. **Single-line service registration** — `services.rs` adds entry; done
6. **Two-crate workspace** — library vs binary separation
7. **Schema introspection built-in** — `gws schema <method>` queries same cache

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| No generated crates | AGENTS.md §1 IMPORTANT block | High (explicit) |
| Runtime Discovery | AGENTS.md §1 + README §Architecture | High |
| Two-phase parsing | README §Architecture | High |
| Cache presence | AGENTS.md §Architecture "fetch cached Discovery" | High |
| Cache TTL | — | **Low — unknown (Q24)** |
| 1-line service registration | AGENTS.md §1 "only need to register it in services.rs" | High |
| Two-crate structure | AGENTS.md §Architecture | High |

## 4. How it works

### Two-phase argument parsing

```
$ gws drive files list --params '{"fields": "id, name"}'
         ↓
[Phase 1] Identify service = "drive" from argv[1]
         ↓
[Phase 2] Load Discovery Document for "drive" (from cache OR fetch)
         ↓
         Build clap Command tree:
           - drive
             ├─ files
             │  ├─ list  [params: q, pageSize, fields, ...]
             │  ├─ get   [params: fileId, fields, ...]
             │  ├─ create
             │  └─ ...
             ├─ permissions
             ├─ revisions
             └─ ...
         ↓
[Phase 3] Re-parse argv against built tree
         ↓
[Phase 4] Validate inputs (validate_safe_*, encode_path_segment)
         ↓
[Phase 5] Authenticate (multi-flow OAuth2)
         ↓
[Phase 6] HTTP call to Google API
         ↓
[Phase 7] Apply Model Armor sanitization (if enabled)
         ↓
[Phase 8] Emit structured JSON to stdout
```

### Service registration (1-line change)

From AGENTS.md §1:
> *"When adding a new service, you only need to register it in `crates/google-workspace/src/services.rs` and verify the Discovery URL pattern in `crates/google-workspace/src/discovery.rs`. Do NOT add new crates to `Cargo.toml` for standard Google APIs."*

**Implementation pattern (inferred):**
```rust
// crates/google-workspace/src/services.rs
static SERVICES: &[(&str, &str)] = &[
    ("drive", "https://www.googleapis.com/discovery/v1/apis/drive/v3/rest"),
    ("gmail", "https://www.googleapis.com/discovery/v1/apis/gmail/v1/rest"),
    ("calendar", "..."),
    // ... one line per service
];
```

### Cache layer

Discovery Documents cached locally. Benefits:
- **Fast cold start** — no network fetch for known services
- **Offline capable** — once cached, works offline
- **Deterministic** — same cache = same CLI tree

Cache TTL unknown (Q24). Likely eternity until manual clear or version bump.

### `clap` dynamic tree

`clap` is Rust's standard CLI parsing library. Typically, clap trees are defined declaratively at compile time. gws builds them at **runtime** from parsed JSON.

**Technical implementation (inferred):**
- `clap::Command::new()` + `.subcommand()` chains at runtime
- `clap::Arg::new()` + type inference from Discovery schema
- Required/optional flags derived from Discovery's `required` field
- Enum types translated to clap `value_parser` constraints

## 5. Worked example — user invokes Sheets operation

**Scenario:** User runs `gws sheets spreadsheets values append`

```
Phase 1: service = "sheets"
Phase 2: Load Discovery Document for sheets v4
         → Cache hit OR fetch https://sheets.googleapis.com/$discovery/rest?version=v4
         → Build clap tree:
           sheets
             └─ spreadsheets
                 ├─ values
                 │   ├─ append   (params: spreadsheetId, range, valueInputOption, ...)
                 │   ├─ batchGet
                 │   ├─ batchUpdate
                 │   ├─ clear
                 │   ├─ get
                 │   └─ update
                 ├─ ...
Phase 3: Re-parse argv → matches spreadsheets.values.append
Phase 4: Validate inputs (spreadsheetId format, range encoding)
Phase 5: Authenticate with OAuth2 token
Phase 6: POST https://sheets.googleapis.com/v4/spreadsheets/{id}/values/{range}:append
Phase 7: Apply Model Armor if configured
Phase 8: stdout: {"spreadsheetId":"...", "updates":{...}}
```

**Agent-facing benefit:** same pattern works for **every** Google API without new binary release. When Google ships a new Workspace API, `gws` supports it after services.rs registration + cache refresh.

## 6. Edges + failure modes

### Dynamic Discovery risks

- **Cache staleness** — if Google breaks backward compat in Discovery schema, cached copy produces wrong tree. Cache invalidation becomes correctness issue.
- **Network dependency on first run** — fresh install + first service invocation requires fetching Discovery. Offline install UX incomplete.
- **Schema drift** — Google may change Discovery format; gws parser must track.
- **Build overhead** — cold start includes CLI tree construction. Negligible for users but measurable for short-lived agent invocations.

### `clap` dynamic tree limitations

- **Error messages** — clap errors reference dynamic types, may be less friendly than hand-written CLIs
- **Autocomplete** — tab completion complicated by runtime-generated trees (shell integration TBD)
- **Testing** — contributor can't statically verify CLI surface; must run binary to see commands

### Discovery coverage gaps

Some Google APIs not in Discovery Service:
- **NotebookLM** — not in Workspace Discovery (hence v7 notebooklm-py unofficial exists)
- **Gemini APIs** — separate discovery (Google AI service, not Workspace)

gws covers Workspace Discovery surface; adjacent Google surfaces need separate tooling.

### Input adversarial assumption

Per AGENTS.md §6: all CLI args adversarial. Requires:
- validate_safe_output_dir/read before any file op
- validate_resource_name for any Google resource reference
- encode_path_segment before URL embedding
- Clap `value_parser` for enum allowlist

**Failure mode:** validator missed on new helper command → path traversal or URL injection. Mitigation: AGENTS.md §6 discipline + codecov/patch test coverage.

## 7. Related concepts

- [[(C) 110 Skills (44 gws-* + 10 personas + 56 recipes)]] — skills consume Discovery-generated methods
- [[(C) Multi-Flow OAuth2 + Model Armor + Validation Discipline]] — Phase 4-7 of execution flow
- [[(C) T4 Multi-Entrant Validation + Official-vs-Unofficial + Storm Bear Enterprise Angle]] — why official Google gets Dynamic Discovery vs unofficial reverse-engineering

## 8. Cross-project comparison

### vs notebooklm-py (T4 N=1)

| Aspect | notebooklm-py | gws |
|--------|---------------|-----|
| API access strategy | Reverse-engineered unofficial | Official Dynamic Discovery |
| Schema source | Inferred from web app | Published Discovery JSON |
| New API support | Manual wrapper code | 1-line services.rs entry |
| Breaking change risk | High (site changes) | Low (Discovery versioned) |
| Multi-service | ❌ | ✅ 11+ |
| Binary size | ~10MB Python wheel | Single Rust binary |

→ Dynamic Discovery is **only viable when the upstream provider publishes machine-readable schema**. Google does; NotebookLM's parent doesn't expose it. Hence different strategies.

### vs T1 peers (skill-based frameworks)

- BMAD/codymaster/GSD: skills are markdown with logic embedded
- gws: skills are **metadata layer** on top of Discovery-generated commands. Lighter skills, heavier runtime.

### vs T5 (agent-as-application)

- deer-flow: pre-defined SuperAgent harness
- autoresearch: program.md orchestration
- gws: **runtime-generated** command surface

**gws is unique in runtime CLI generation across all 13 wikis.**

## 9. Open questions

- Cache TTL specifics (Q24)
- Cache invalidation on Discovery schema change? (new — Q32)
- clap tree build cost on cold start? (new — Q33)
- Offline first-install UX? (new — Q34)
- New Google API support latency — how fast does gws add new Workspace API after Google ships? (new — Q35)
- Rust `clap` runtime API used — custom or standard? (new — Q36)

## 10. Decision log

- **Pre-gws design phase:** Google could have shipped generated crates (like google-api-rust) — chose dynamic
- **Rationale (AGENTS.md §1):** "Do NOT add new crates to Cargo.toml for standard Google APIs" — explicit policy
- **Two-crate split:** library (reusable across projects) + binary (auth + CLI-specific)
- **v0.22.5 current:** 44 iterations on architecture; no major reset visible

## 11. Storm Bear relevance

### Architectural lessons for Storm Bear vault

gws's Dynamic Discovery pattern suggests for vault:
1. **Schema-first** — treat wiki entity structure as discoverable schema, not hardcoded
2. **1-line registration** — adding new framework to corpus could be 1-line metadata entry (like services.rs)
3. **Cache-backed** — expensive operations (cross-project scans, comparison builds) cached with version-based invalidation
4. **Runtime composition** — generate 6-way comparison table dynamically from individual wiki data, not hand-rebuild

### Direct use for Storm Bear

- **Workspace automation** — Storm Bear uses Gmail/Drive/Calendar daily. gws + Claude Code = automation pipeline
- **Scrum workflows** — gws workflow +meeting-prep, +standup-report directly relevant
- **Bilingual docs** — gws docs +write could bulk-generate VN/EN reports

### Pilot candidate

High-priority Storm Bear pilot: install gws + use for 1-week Scrum coaching cycle. Workflow candidates:
- Monday: gws workflow +meeting-prep for week-ahead planning
- Daily: gws workflow +standup-report summarizing team status
- Friday: gws workflow +weekly-digest for leadership update

## 12. Migration / adoption notes

- **Fresh install:** works with cached Discovery after first fetch
- **Air-gapped environments:** pre-populate `~/.config/gws` with Discovery Documents from cached machine
- **OAuth setup:** `gws auth setup` is one-time per user (or `GOOGLE_APPLICATION_CREDENTIALS` for service accounts)
- **From notebooklm-py:** different scope; install both if using NotebookLM + Workspace

## 13. References

- README.md §Architecture
- AGENTS.md §1 Project Overview + §4 Architecture
- `crates/google-workspace/src/services.rs` (not fetched; cited by AGENTS.md)
- `crates/google-workspace/src/discovery.rs` (not fetched; cited by AGENTS.md)
- Parent: [[(C) index]]
- T4 sibling: `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) Python API Architecture.md` — contrast
