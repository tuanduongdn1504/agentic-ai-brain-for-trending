# Verification Framework — File-by-File Deep Dive

## Source

`anthropics/cwc-workshops/how-we-claude-code/phase-3-verify/` (read via `gh api`). This is the **double-deep-dive** into the workshop's original resource — the actual code, not the talk's description of it.

```
phase-3-verify/
├── src/features/todos/        TodoApp · TodoInput · TodoItem · TodoList · TodoStats · types · useTodos
├── src/verify/
│   ├── core/      contract.ts · registry.ts · runner.ts · types.ts
│   ├── verifiers/ schema.ts · invariants.ts · dom-contract.ts · a11y.ts · index.ts
│   ├── specs/     TodoStats.verify.ts · todos.feature.verify.ts · (+per-component) · index.ts
│   ├── harness/   Dashboard.tsx · Report.tsx · ReplayPage.tsx · UnitPage.tsx · Badge.tsx · handle.ts · recorder.ts · visibleAct.ts
│   └── matrix.test.ts          (vitest — the CI surface)
├── scripts/record.ts           (Playwright recorder)
└── package.json                ("verify" = vitest run · "record" = bun scripts/record.ts)
```

## 1. The DOM contract — `core/contract.ts`

- Components call a thin helper **`verifyAttrs(dict)`** which turns a record into `data-verify-<key>="<value>"` attributes on the root element. Pure TypeScript, zero dependencies (`Record[`data-verify-${key}`] = String(value)`).
- Constant `VERIFY_PREFIX = 'data-verify-'`.
- Readers: **`readContract(root)`** finds the first `[data-verify-unit]` descendant and extracts all `data-verify-*` attrs into a `Record<key,string>`; **`readAllContracts(root)`** returns the array.

Example (from `TodoStats.tsx` / `TodoApp.tsx`):
```html
<footer data-verify-unit="TodoStats" data-verify-total="3"
        data-verify-done="1" data-verify-active="2"
        data-verify-filter="all" data-verify-consistent="true">
```
The agent reads *that* — never the React fiber.

## 2. The unit declaration — `core/types.ts` + `specs/*.verify.ts`

- **`VerifiableUnit`** = `{ id, render, fixtures[], invariants[], propsSchema }`.
- **`Fixture`** = `{ id, description, props, probe?, act? }`. The optional **`act(ctx: ActContext)`** is an imperative hook with `click(selector)`, `type(selector, text)`, `wait(ms)` — so a fixture can express *"render, then type 'milk', then click the toggle, then verify."*
- **`Invariant`** = `{ id, description, check(ctx) => boolean|string, onlyFixtures? }`.
- Units register themselves via `registerUnit(...)` in a `*.verify.ts` spec file. The Todo app ships **2 units**: `TodoStats` (4 fixtures) and `todos.feature` (6 fixtures, the full add→toggle→clear flow).

## 3. The runner — `core/runner.ts`

`runFixture(unit, fixture)` does the whole loop:
1. Create a **fixed-position div at `left:-10000px`** (in the DOM for layout/a11y but invisible).
2. `flushSync` mount the unit for that fixture; `tick()` to let effects settle.
3. Run `fixture.act()` if present (drives the interactions).
4. `readContract()` the published DOM state.
5. Run **all registered verifiers**; collect their `Check[]`.
6. `verdictOf(checks)` → `PASS`/`FAIL`/`BLOCKED`/`SKIP`. Returns a `VerifyResult`.

Verifier exceptions are caught and converted to `fail` checks (the runner never silently swallows).

## 4. The agent API — `window.__verify` (`harness/handle.ts`)

Declared on `window.__verify` (a `VerifyHandle`):
- **`manifest()`** → all units, fixtures, verifiers (so an agent can *discover* what's testable).
- **`current()`** → the last `VerifyResult` for the mounted unit/fixture.
- **`runAll()`** → `Promise<VerifyResult[]>` — runs the whole matrix.
- `version`.

This is the seam a Playwright-MCP agent uses: navigate to a unit/fixture route, call `window.__verify.current()`, assert `verdict === 'PASS'`.

## 5. The three surfaces — one code path {#three-surfaces}

> *"The same `runFixture()` code path is called by: the dashboard, the agent, CI. One source of truth, three consumers."*

| Surface | Entry | How it runs |
|---|---|---|
| **Human dashboard** | `/verify` route (`harness/Dashboard.tsx`, `Report.tsx`, `UnitPage.tsx`) | React UI lists units; "Run all" button → `window.__verify.runAll()`; drill into each fixture's checks; `Badge.tsx` shows pass/fail/warn/probe |
| **Agent-driven** | browser console / Playwright MCP | `window.__verify.manifest()` then `.runAll()` / `.current()` |
| **Headless CI** | `bun run verify` → `matrix.test.ts` (vitest) | iterates `runUnit()` over the registry, asserts verdicts |

## 6. Proving it can fail — `matrix.test.ts`

Two assertions make the framework honest:
- **`EXPECTED_FAIL = new Set(['TodoStats::inconsistent-counts'])`** — a fixture deliberately built to violate the schema (`3 + 4 ≠ 10`). The matrix asserts it *fails*. If it ever passes, the framework is broken.
- **Every unit must have ≥1 `probe` fixture:** `expect(unit.fixtures.some(f => f.probe), '…has no probe fixtures').toBe(true)`.
  - Rationale: *"A unit with zero probe fixtures has only replayed the happy path."* / *"A surface with zero invariants is unverified."*

This is the same idea as vault Rule 9 (*tests verify intent, not just behavior*) and Rule 12 (*fail loud*) — see [[../claude-md-12-rules/_index]].

## 7. Recording as evidence — `scripts/record.ts` + `harness/recorder.ts`

- `bun run record` launches **Playwright headless Chromium with `recordVideo`**, navigates `/verify/replay?dwell=1500&key=60&auto=1`, polls `window.__verify_replay.done`, then `context.close()` finalizes a `.webm` saved to `recordings/replay-<timestamp>.webm`.
- The in-browser recorder (`harness/recorder.ts`) uses the Chrome **Region Capture** API (`CropTarget` + `track.cropTo()`): one `getDisplayMedia()` prompt → one shared tab stream cropped per fixture → **one `.webm` per unit×fixture** via separate `MediaRecorder`s.
- **No S3 in the repo.** Output is local `recordings/`. The talk *mentions* S3 ("you could put them in S3 or share with colleagues") as a downstream option only — see [[how-we-claude-code/source-provenance]].

## Key Takeaways

- The framework is **real, runnable, and ~complete in the repo** (every file above was read directly — see the provenance ledger; the adversarial verifiers that "refuted" it had searched the local filesystem by mistake).
- **One engine, three consumers, one verdict schema** — that's the whole trick; the DOM contract is the decoupling layer.
- **`probe` fixtures + `EXPECTED_FAIL`** are the part most people skip and the part that makes verification trustworthy.
- Adopting it is incremental: start with **one component + a11y verifier**, add schema/invariants/probes as confidence grows. Pilot mapping → `output/(C) 2026-06-29-how-we-claude-code-pilot-methods.md`.
- Caveat: `window.__verify_replay` (used by the recorder) lives in the `/verify/replay` route component, which wasn't in the fetched set; and Region Capture is Chrome-only.
