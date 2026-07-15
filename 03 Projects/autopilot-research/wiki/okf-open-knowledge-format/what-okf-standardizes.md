# What OKF Actually Standardizes (from the SPEC)

**Primary source (read directly, not via the video):** [OKF SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (raw: `raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/SPEC.md`), verified 2026-07-15. OKF is spec **v0.1**.

OKF is deliberately tiny. It standardizes **two** things (Cole's summary is accurate) — and is loud about the many things it does **not** touch.

## 1. Structure / organization

- **A directory of markdown files, each with a YAML frontmatter block.** That's the whole substrate — "just markdown, readable in any editor, renderable on GitHub, indexable by any tool."
- **Reserved filenames** (the only filenames OKF gives special meaning):
  - **`index.md`** — progressive-disclosure entry point at *any* directory level (a folder's overview + what's inside). This is the OKF-formalized version of what Karpathy and this vault already do with index files.
  - **`log.md`** — an append-only history/changelog for the bundle or a subtree.
  - These filenames **MUST NOT** be used for ordinary concept documents (an explicit constraint).
- **Concept ID** = the file path minus `.md` (e.g., `tables/users.md` → `tables/users`). This is the stable identifier agents use to address a document.
- **Cross-links** = standard markdown links between concepts. OKF gives linking *semantics* but does not invent a new link syntax.
- **Folder hierarchy is NOT prescribed.** The SPEC explicitly says: *"The directory structure is independent of the domain — producers organize concepts however makes sense."* → This is an important correction to Cole's line that OKF specifies "exactly how you organize your different files." It specifies *reserved filenames + progressive disclosure*, **not a rigid tree.**

## 2. Metadata (YAML frontmatter)

| Field | Status | Purpose |
|---|---|---|
| **`type`** | **REQUIRED (the only one)** | A short string naming the *kind* of concept (e.g. `concept`, `video`, `BigQuery Table`). Drives categorization/filtering/traversal. |
| `title` | Recommended | Human-readable display name. |
| `description` | Recommended | One-sentence summary. |
| `resource` | Recommended | URI identifying the underlying asset (e.g. a BigQuery table URL, a video URL). |
| `tags` | Recommended | List of categorization strings. |
| `timestamp` | Recommended | ISO-8601 last-modified datetime. |

- **Exact required-field statement (SPEC):** *"Required: `type` — A short string identifying the kind of concept."* ✅ Cole is correct that `type` is the single required field.
- **Producers may add arbitrary extra keys.** **Consumers MUST tolerate/preserve unknown fields gracefully.** (This unknown-field-tolerance contract is a real addition over Karpathy's "choose whatever metadata is useful" — see [[caveats-and-corrections]].)
- Cole's `related` / `related_videos` frontmatter is a **content-level linking convention in his own bundle**, *not* an OKF-defined key. OKF does not prescribe a `related` field.

## 3. Producer **and** consumer roles

OKF explicitly defines expectations for both sides (this is why Cole calls it a standard for "both producing and consuming"):

- **Producer guidance:** favor structural markdown, use conventional section headings, give descriptive `type` values, keep `index.md` current.
- **Consumer guidance:** tolerate unknown `type` values, preserve unrecognized frontmatter keys, accept broken cross-links (don't crash on a dangling link).

## 4. A "bundle"

- **Bundle = "a self-contained, hierarchical collection of knowledge documents. The unit of distribution."** (SPEC term — not something Cole invented.)
- Distributed as: **git repositories (recommended)**, tarballs, or subdirectories within a larger repo.
- Cole's `coleam00/cole-medin-ai-coding` is a real, spec-conformant bundle (git repo, `index.md`, `concepts/`, `videos/`, `log.md`, `okf-cli.py`).

## 5. What OKF deliberately does NOT standardize

The SPEC is explicit that OKF **does not define**:

- **Storage, serving, or query infrastructure** — no database, no embeddings, no API, no vector store. (This is what makes Cole's "point your agent at a folder, zero integration" claim ✅ accurate.)
- **Taxonomies** — it won't tell you *which* `type` values or tags to use.
- **Domain-specific schemas** — the body of a document is free-form markdown.
- **Folder hierarchy** — see §1.

## Why the minimalism cuts both ways

- **Pro:** near-zero adoption cost; tool-agnostic; forward-compatible (unknown fields survive); trivially readable by any LLM. Cole's "minimally opinionated is the point" is a defensible design stance.
- **Con (the interop gap):** because `type` values, tag vocabularies, link fields, and folder layouts are **all unspecified**, two "OKF-valid" wikis can still be mutually illegible. A consumer agent will understand OKF *syntax* but not your *semantics*. → This is the crux of the [[thesis-critique]]: OKF guarantees a weaker interoperability than "your agent just understands mine" implies.

## Key Takeaways

- OKF standardizes exactly two things: **reserved-filename organization** + **frontmatter metadata**. Everything else is intentionally out of scope.
- **`type` is the one required field** — verified against SPEC. Recommended: `title`, `description`, `resource`, `tags`, `timestamp`.
- Real additions over Karpathy that Cole under-credits: **mandatory `type`, a recommended-field contract, reserved `index.md`/`log.md`, producer/consumer roles, unknown-field tolerance.**
- Folder hierarchy is **not** prescribed (correcting the video); OKF is a metadata + progressive-disclosure convention, not a directory schema.
- The minimalism is both the selling point and the source of the interop ceiling → [[thesis-critique]].
