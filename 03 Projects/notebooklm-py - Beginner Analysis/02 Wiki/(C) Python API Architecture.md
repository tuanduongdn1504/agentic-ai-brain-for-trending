# (C) Python API Architecture

> Entity page — Architecture concept
> Sources: README Python API + CLAUDE.md 4-layer design
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Python API Architecture** = async client library structured theo **4-layer pattern** (CLI → Client → Core → RPC). Layer separation isolate fragile RPC (undocumented Google APIs) from stable developer-facing Client.

**Main entry point:**
```python
async with await NotebookLMClient.from_storage() as client:
    # namespaced access: client.notebooks.*, client.sources.*, client.artifacts.*, client.chat.*, client.sharing.*
```

## 2. Why it matters / Sao quan trọng

**4-layer pattern = robustness strategy for unofficial API:**

- **Google changes RPC method IDs** → only `rpc/types.py` needs update
- **Users of Client layer** unaffected by RPC breakage
- **CLI users** invoke same Client → uniform behavior
- **Testability** — mock at Core layer for integration tests, at Client for unit tests

**Alternative (bad) architecture:** All RPC details leak into user code. When Google breaks API, every downstream user must rewrite.

**notebooklm-py chose sanity.** Solo maintainer (teng-lin) only needs to maintain 1 fragile file.

## 3. Architecture diagram

```
┌────────────────────────────────────────────────────┐
│ CLI Layer (cli/*.py)                               │
│   - Click commands per domain                      │
│   - --json flag for programmatic output            │
│   - Thin translation: CLI args → Client calls      │
└────────────────────┬───────────────────────────────┘
                     │
┌────────────────────▼───────────────────────────────┐
│ Client Layer (client.py + _notebooks.py etc.)      │
│   - NotebookLMClient (main entry)                  │
│   - Namespaced APIs:                               │
│     client.notebooks.*                             │
│     client.sources.*                               │
│     client.artifacts.*                             │
│     client.chat.*                                  │
│     client.sharing.*                               │
│   - Async context manager                          │
│   - Pythonic exceptions                            │
└────────────────────┬───────────────────────────────┘
                     │
┌────────────────────▼───────────────────────────────┐
│ Core Layer (_core.py)                              │
│   - HTTP client management                         │
│   - RPC abstraction                                │
│   - Credential loading (from_storage)              │
│   - Session management                             │
└────────────────────┬───────────────────────────────┘
                     │
┌────────────────────▼───────────────────────────────┐
│ RPC Layer (rpc/types.py)                           │
│   - Undocumented Google method IDs                 │
│   - Request encoding (nested lists, positional)    │
│   - Response parsing (variable nesting [[[[id]]]]) │
│   - ⚠️ FRAGILE — changes when Google ships updates │
└────────────────────────────────────────────────────┘
```

## 4. Namespaced Client API

| Namespace | Purpose | Example methods |
|-----------|---------|-----------------|
| `client.notebooks` | Notebook CRUD | `list()`, `create(name)`, `delete(id)`, `get(id)` |
| `client.sources` | Source management | `add_url(nb_id, url)`, `add_file(nb_id, path)`, `get_fulltext(nb_id, src_id)`, `list(nb_id)` |
| `client.artifacts` | Generation + retrieval | `generate_audio(nb_id, instructions)`, `wait_for_completion(nb_id, task_id)`, `download_audio(nb_id, path)` |
| `client.chat` | Q&A với notebook | `ask(nb_id, question)`, `continue_conversation(conv_id, question)` |
| `client.sharing` | Permissions | `set_sharing_state(nb_id, public=True)` |

**Pattern:** Every domain = namespace on client. No free functions.

## 5. Async-first design

```python
async with await NotebookLMClient.from_storage() as client:
    nb = await client.notebooks.create("name")
    await client.sources.add_url(nb.id, url, wait=True)
    result = await client.chat.ask(nb.id, "question")
```

**All I/O operations = async.** `await` required. Context manager ensures cleanup.

### Why async?

- **Generation tasks long-running** (audio 10-20 min, video 15-45 min)
- **Parallel operations** — multiple sources added concurrently
- **Integration with agent frameworks** — most agent loops use async

### Alternative: Sync wrapper?

Not provided. Users needing sync can wrap with `asyncio.run()` at boundaries.

## 6. Credential & State Management

### `from_storage()` pattern

```python
client = await NotebookLMClient.from_storage()
```

Loads credentials from standard location:
- Default: `~/.config/notebooklm-py/`
- Override: `NOTEBOOKLM_HOME=/custom/path`
- Profile: `NOTEBOOKLM_PROFILE=name`

### CI/CD pattern

```python
# Load from env var (CI-friendly)
os.environ["NOTEBOOKLM_AUTH_JSON"] = json.dumps(auth_state)
client = await NotebookLMClient.from_storage()
```

### Multi-agent isolation

```python
# Agent-specific home
os.environ["NOTEBOOKLM_HOME"] = f"/tmp/agent-{agent_id}"
# Or agent-specific profile
os.environ["NOTEBOOKLM_PROFILE"] = f"agent-{agent_id}"
```

→ **Every agent = own credential state.** Prevents cross-contamination.

## 7. Error handling

### Exception hierarchy (centralized in v0.3.0+)

```
NotebookLMError (base)
├── AuthError (session expired, login needed)
├── RateLimitError (Google throttled)
├── NotFoundError (invalid ID)
├── TimeoutError (wait exceeded)
├── RPCError (API failed, possibly broken)
└── ValidationError (bad parameters)
```

**Pattern:** Catch specific types for specific recovery:
```python
try:
    await client.artifacts.generate_audio(...)
except RateLimitError:
    await asyncio.sleep(300)
    # retry
except RPCError as e:
    # log + escalate; API may have changed
```

## 8. Trade-offs / Limitations

### Strengths
- **Layer separation** isolates fragility
- **Type enums** (v0.3.0+) replace stringly-typed APIs
- **Deprecation warnings** before removal
- **90%+ test coverage** enforced
- **mypy-checked** — strongly typed API

### Weaknesses
- **RPC fragility intrinsic** — Google can break anytime
- **Async-only** — sync users face overhead
- **Playwright dependency** for browser auth (heavy)
- **No explicit retry/circuit-breaker** — users implement
- **Bus factor = 1** — solo maintainer risk

## 9. Comparison to sibling architectures

| Sibling | Architecture style | Layer count |
|---------|-------------------|-------------|
| **ECC** | Plugin + skills + subagents | 3 (plugin + skill + agent) |
| **Superpowers** | 7-stage workflow pipeline | Pipeline (not layered) |
| **gstack** | Specialist roles + sprint pipeline | Role-layered |
| **GSD** | 14-harness + 33 agents + 83 commands | Command-oriented |
| **goclaw** | Multi-tenant platform + agent teams | **4-layer** (API + Core + Agent + Tenant) |
| **course** | N/A (teaches concepts) | — |
| **notebooklm-py** | **4-layer bridge (CLI/Client/Core/RPC)** | **4-layer** |

→ **Both goclaw (Tier 2) and notebooklm-py (Tier 4) use 4-layer architecture.** Pattern emerges for production-grade infrastructure.

## 10. Common pitfalls

1. **Forgetting `async with`** — credentials not cleaned up, session leaks
2. **Not `await`ing** — returns coroutine, not result
3. **Hardcoding notebook ID in parallel code** — fine if unique; collision if shared
4. **Catching generic Exception** — misses specific recovery paths (RateLimit vs Auth)
5. **Not handling deprecation warnings** — code breaks at v0.4.0
6. **Blocking on long-running in event loop** — use `--wait` CLI or `wait_for_completion()` properly
7. **Bypassing Client layer to touch RPC directly** — breaks on Google updates

## 11. When NOT to use Python API

- **Quick one-off task** — CLI faster
- **Shell script pipeline** — CLI composes better
- **Non-Python codebase** — use CLI via subprocess
- **Concerned about async complexity** — CLI simpler for linear workflows
- **Sync-only environment** — Python API async-only; wrapping adds overhead

## 12. Storm Bear vault relevance

**Python API use cases for Storm Bear:**

### Use case 1: Vault ingestion automation
```python
# After routine finishes building wiki:
async with await NotebookLMClient.from_storage() as client:
    nb = await client.notebooks.create(f"{wiki_name}-audio")
    for source_url in sources:
        await client.sources.add_url(nb.id, source_url, wait=True)
    status = await client.artifacts.generate_audio(
        nb.id, "Focus on 4-layer architecture lessons"
    )
    await client.artifacts.wait_for_completion(nb.id, status.task_id)
    await client.artifacts.download_audio(
        nb.id, f"./vault-audio/{wiki_name}.mp3"
    )
```

### Use case 2: Cross-wiki synthesis
```python
async with await NotebookLMClient.from_storage() as client:
    nb = await client.notebooks.create("cross-wiki-synthesis")
    # Add all 7 wiki beginner guides as sources
    for wiki_path in ["ECC", "Superpowers", "gstack", "GSD", "goclaw", "course", "notebooklm-py"]:
        await client.sources.add_file(nb.id, f".../03 Published/(C) {wiki_path} guide.md")
    result = await client.chat.ask(
        nb.id,
        "Which framework would you recommend for a Scrum coach starting from zero?"
    )
```

### Implementation status
- **Not adopted yet.** Storm Bear could add this as routine v2 optional phase.
- **Prerequisite:** NotebookLM paid plan.

## 13. References / Nguồn

- Source: [[(C) README summary]] (Python API section) + [[(C) Architecture + Release cluster summary]] (4-layer architecture)
- Related entities:
  - [[(C) CLI Surface]] (CLI = thin layer atop Python API)
  - [[(C) Skill Integration (Claude Code + Codex + OpenClaw)]]
- Sibling 4-layer architectures:
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) Multi-Tenant Architecture.md`
- External: [src/notebooklm/ GitHub source](https://github.com/teng-lin/notebooklm-py/tree/main/src/notebooklm)
