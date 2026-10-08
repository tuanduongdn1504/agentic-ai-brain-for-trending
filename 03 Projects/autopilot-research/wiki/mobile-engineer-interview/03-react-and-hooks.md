# 03 — React & hooks

The React front-end layer (shared with React Native — same mental model). Mostly from the strongest candidate (video 5), who answered this domain well; the very-junior candidate (video 3) hadn't reached React yet (it was named the gating requirement).

## Virtual DOM vs Real DOM

- **Virtual DOM** = an in-memory JS representation of the UI. On state change React builds a new VDOM tree, **diffs** it against the previous one, and **patches only the changed nodes** in the Real DOM.
- The Real DOM is the browser's actual document; touching it is expensive. Selective patching (vs re-rendering everything) is why this is faster. Clean model answer from the candidate.

## JSX

- HTML-like syntax inside JavaScript; **syntactic sugar** that transpiles to `React.createElement(...)` calls. It's not HTML and not a string — it's expressions.

## Hooks (function components)

- **Introduced in React 16.8 (Feb 2019).** Before hooks, **class components** were required for state and lifecycle. Now function components + hooks cover all cases. (Candidate got the sequence; blanked on the exact version — fine.)
- Common hooks: **`useState`** (local state), **`useEffect`** (side effects), **`useMemo`** (memoise a computed value), **`useCallback`** (memoise a function), `useReducer` (complex state), `useContext`, `useRef`.

### `useEffect` and its dependency array (asked explicitly)

`useEffect(setupFn, deps)` — `setupFn` runs after render; an optional `return` is the **cleanup** function; `deps` controls *when* it re-runs:

- **No array** → runs after **every** render.
- **Empty `[]`** → runs **once** on mount (≈ `componentDidMount`); cleanup on unmount.
- **`[a, b]`** → runs on mount **and** whenever `a` or `b` changes. (Most common: data fetch keyed on an id.)

The candidate correctly enumerated all three — a strong answer.

### `useMemo` vs `useCallback`

- `useMemo(fn, deps)` memoises the **returned value** of `fn` (skip expensive recomputation).
- `useCallback(fn, deps)` memoises the **function itself** (stable identity to pass to memoised children / effect deps).
- Both limit unnecessary re-renders/recomputes. Rule of thumb: `useMemo` for values, `useCallback` for functions passed down.

## Component lifecycle (function-component mental model)

Three phases: **mount** (initial render) → **update** (props/state change → re-render) → **unmount** (cleanup). With hooks these map onto `useEffect` (mount = `[]`, update = deps, unmount = cleanup return).

## SPA vs multi-page

- **SPA:** one HTML shell; JS handles routing + rendering client-side (React Router). Only the first load fetches a full page; subsequent navigation is JS-driven → fast, app-like (Gmail, Maps).
- **Multi-page:** server renders each page; every navigation is a full reload → slower, traditional.

## CSR vs SSR

- **CSR (client-side rendering):** browser downloads JS, renders, and calls APIs for data (JSON). Fast subsequent navigation; slower first paint; weaker SEO by default.
- **SSR (server-side rendering):** server renders HTML and sends it ready-to-display. Faster first load + better SEO; more server work. (⚠️ the candidate conflated SSR with the **MVC** pattern — they're different axes: MVC is a code-organisation pattern, SSR/CSR is a *rendering* strategy.)

## Practical React knowledge Tuấn probes

- **Project folder structure:** a mature answer — `src/` split into `pages`, `components`, `hooks`, `services` (API), `store` (state), `utils`, `assets`, `layouts` (incl. permission-gated), plus root config (`eslint`, `tsconfig`). Consistency matters more than the exact taxonomy.
- **UI libraries:** **Ant Design** (Alibaba; leaner API, good defaults, quick to use) vs **Material UI** (Google's system; comprehensive, more verbose). Pick by design fit + team familiarity.
- **Vue vs React:** Vue uses **single-file components** (template/script/style in one `.vue` file), gentler curve; React uses **JSX** (JS-centric), more flexible, dominant in enterprise.
- **File upload:** `<input type="file">` → `FormData` → `fetch`/axios `POST`; Excel parsing via a library (e.g. `xlsx`). Know `FormData` + binary handling, not just "I used a library".

## Key Takeaways

- **Virtual DOM = diff + patch only changes.** JSX = sugar for `createElement`.
- Hooks arrived in **16.8**; know **`useEffect`'s three dependency-array cases** cold.
- `useMemo` = value, `useCallback` = function.
- Keep **CSR/SSR** (rendering) separate from **MVC** (code organisation).

**Sources:** video 5 (Dzto), video 3 (0n8o). Related: [[01-javascript-core]] · [[02-async-and-event-loop]] · [[05-react-native-and-mobile-deployment]] · [[06-css-html-and-web-fundamentals]].
