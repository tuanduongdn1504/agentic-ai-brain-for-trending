# 06 — CSS, HTML & web fundamentals

Mostly from the very-junior React candidate (video 3), where Tuấn probed front-end basics. These are entry-level filters — get them crisp.

## Flexbox vs CSS Grid

- **Flexbox = 1D** layout — items along **one** axis (a row *or* a column), with flexible wrapping and item-driven sizing. Best for linear layouts (nav bars, toolbars, a row of cards).
- **Grid = 2D** layout — **rows *and* columns** together, with explicit grid lines and placement. Best for page/section layouts and complex 2D designs.
- ⚠️ Candidate said "Flexbox divides container space; Grid divides the page into equal parts" — the right instinct but missed the core **1D vs 2D** distinction, which is the answer interviewers want. (Captions: `Flashbox`=Flexbox, `GD`/`GCK`=Grid.)

## `flex: 1`

- Shorthand for **`flex-grow: 1; flex-shrink: 1; flex-basis: 0`**. It makes a flex item **grow to fill available space**, sharing leftover space equally with siblings that also have `flex: 1`.
- Candidate had the intuition ("fills the remaining space, grows proportionally") but not the shorthand breakdown — name the three sub-properties. (Captions: `Fet 1`/`Flash 1`=`flex: 1`.)

## CSS `position` values

- **`static`** (default, normal flow), **`relative`** (offset from its own normal position), **`absolute`** (offset from the nearest *positioned* ancestor), **`fixed`** (offset from the viewport), **`sticky`** (relative until a scroll threshold, then fixed).
- ⚠️ Candidate confusion worth avoiding: he listed `top`/`bottom`/`left`/`right` as the "values of `position`". Those are **separate offset properties**; they *position* an element *only when* `position` is `relative`/`absolute`/`fixed`/`sticky`. Keep **property values** (`static`/`relative`/…) separate from **offset properties** (`top`/`left`/…).

## HTML — the `<td>` tag

- `<td>` = **table data cell**, lives inside a `<tr>` (table row), inside `<table>`. Pairs with `<th>` (header cell). Holds the content of one cell in tabular data. (Captions: `TD tag/card`=`<td>`.)
- Broader signal: know semantic table structure `<table><thead><tbody><tr><th>/<td>` — Tuấn uses `<td>` as a quick "do you actually know HTML" check.

## Domain vs hosting

- **Domain** = the human-readable address (`example.com`), mapped to a server **IP via DNS**. You *lease* it (annual renewal).
- **Hosting** = the server/disk space where the site's files + database live. You *rent* it.
- Both are needed for a live site; a strong answer also mentions **DNS** resolving the name to the IP.

## Key Takeaways

- **Flexbox = 1D, Grid = 2D** — the one-line distinction that scores.
- **`flex: 1` = `flex-grow:1; flex-shrink:1; flex-basis:0`.**
- `position` **values** (`static/relative/absolute/fixed/sticky`) ≠ **offset properties** (`top/left/…`).
- `<td>` is a table cell inside `<tr>`; know the full `<table>` structure.

**Sources:** video 3 (0n8o), video 5 (Dzto). Related: [[03-react-and-hooks]] · [[01-javascript-core]].
