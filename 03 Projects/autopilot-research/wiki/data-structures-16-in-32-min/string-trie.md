# String / Prefix — the trie

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~26:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

## The question it answers

Not "does this key exist?" but **"what words start with this prefix?"** — type-as-you-go autocomplete.

## Mechanism

- Still tree-shaped, but branches **by character**, not by value size.
- Each edge carries **one character**. Walk from the root down a path to a node marked "end of word," and the characters along the path spell a complete word.
- **Words sharing a prefix share that path** and only split where they differ.
- Example: `cat`, `car`, `care`, `cord`, `dog` — root branches to `c` and `d`; `c` → `a` splits to `t`(cat) and `r`(car→care), and `co` → `r` splits to `cord`/`core`; `core` can be a complete word even mid-path.
- **Autocomplete:** type `c`, `a` → the whole subtree beneath (`cat`, `car`, `care`) lights up as suggestions. Type `r` → suggestions narrow; `cat` drops off because it's no longer on the path.

## Complexity

- Lookup depends only on the **length of the string**, *not* on how large the dictionary is → effectively **O(L)** (L = string length).

## Origin

- First described by **René de la Briandais, 1959** (in a computing context). A year later, **Edward Fredkin, 1960**, independently described it and coined **"trie"** from the middle letters of **re*trie*val**.

## Key Takeaways

- **Trie** branches by **character**, not by value — built for **prefix / autocomplete** queries.
- Shared prefixes share a path; a node flagged "end of word" = a complete word.
- Lookup is **O(L)** (string length), independent of dictionary size.
- Origin: **de la Briandais 1959**; **Fredkin 1960** coined "trie" (from re**trie**val).
- Use it when you need **type-ahead / prefix matching** — see [[selection-framework]].
