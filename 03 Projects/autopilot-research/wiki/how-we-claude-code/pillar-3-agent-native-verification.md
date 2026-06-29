# Pillar 3 — Agent-Native Verification (Architecture)

## Source

`anthropics/cwc-workshops/how-we-claude-code/phase-3-verify/` — a Vite + React **Todo app** built so an agent can verify it. README + `docs/verification.html` + `src/verify/*` fetched via `gh api` and read directly (see [[how-we-claude-code/source-provenance]]). This is the **load-bearing original** of the workshop.

## The core idea

> *"The DOM is the machine-readable surface. Verifiers and agents read the DOM contract, not React internals."*

Instead of scraping React state or writing brittle unit tests, **each component publishes its own state to the DOM as `data-verify-*` attributes.** That published surface is the **contract**. As long as the contract holds, you can rewrite a component's internals freely — and an agent (or CI, or a human dashboard) can read the *same* surface to decide pass/fail.

This is the "remixing of familiar primitives, made available to the agent first": Storybook-style fixtures + Zod schemas + DOM attributes + Playwright, rearranged so an **agent** is the primary driver.

## The four moving parts (per component)

A component is registered as a **`VerifiableUnit`** declaring:

1. **`fixtures`** — named render configurations (e.g. `empty`, `populated`, `inconsistent-counts`). Each may carry an optional `act()` hook and a `probe: true` flag.
2. **`invariants`** — predicates that must always hold (e.g. *"total = done + active"*). Return `true` or an error string.
3. **`propsSchema`** — a **Zod** schema validating the component's props (can `.refine()` for cross-field rules).
4. **`render`** — the function that mounts the component for a given fixture.

## The four pluggable verifiers

Each verifier is independent and registered globally; each returns a list of `Check` objects:

| Verifier | File | Checks |
|---|---|---|
| **schema** | `verifiers/schema.ts` | props validate against the Zod schema |
| **invariants** | `verifiers/invariants.ts` | every declared invariant holds for the fixture |
| **dom-contract** | `verifiers/dom-contract.ts` | the expected `data-verify-*` attributes are present/consistent |
| **a11y** | `verifiers/a11y.ts` | minimal accessibility (buttons/inputs/images have labels) — *not* a replacement for axe-core/Lighthouse |

## Check & Verdict taxonomy

- **Check status:** `ok` (confirmed) · `fail` (observed wrong) · `warn` (concerning) · `probe` (an off-happy-path case deliberately held).
- **Verdict** (folded from all checks): `PASS` (no fails) · `FAIL` (≥1 fail) · `BLOCKED` (couldn't even mount / no verifiers) · `SKIP` (zero fixtures).
- Deliberate design: *"BLOCKED (couldn't observe) is deliberately distinct from FAIL (observed and wrong). When in doubt, the runner fails."*

## Why this is "agent-native"

- The agent doesn't need to understand React — it reads `data-verify-*` and calls a tiny JS API (`window.__verify`).
- The **same code path** (`runFixture()` / `runUnit()`) serves all three consumers — see [[how-we-claude-code/verification-framework-deep-dive]] for the file-by-file mechanism and [[how-we-claude-code/verification-framework-deep-dive#three-surfaces]] for the surfaces.

## Key Takeaways

- **The contract is the surface, not the source.** Verification survives refactors because it observes rendered DOM, not implementation.
- **Four parts per unit:** fixtures, invariants, propsSchema, render. **Four verifiers:** schema, invariants, dom-contract, a11y.
- **Verdicts separate "couldn't observe" (BLOCKED) from "observed and wrong" (FAIL)** — a small but important honesty primitive.
- Cost of entry is low: *"1 VerifiableUnit per component ≈ 30–50 LoC; tooling cost zero."*
- *"A surface with zero invariants is unverified."* — declaring invariants is the actual work.
