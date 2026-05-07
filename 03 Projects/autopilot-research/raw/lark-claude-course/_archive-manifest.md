---
source: lark-wiki-archive
topic: Claude AI Vietnamese course
discovered: 2026-05-07
crawled_via: Browser MCP (partial — full enumeration deferred to Phase 2 scraper)
---

# Lark Wiki Archive — Khoá học Claude toàn diện tiếng Việt

## Source-of-truth URLs

- **Lark root wiki page:** https://transform.sg.larksuite.com/wiki/EY8kwGVvcirJTBkCFzalp71igQb
  - **Public**: yes (guest access, no Google or Lark login required)
  - **Title:** "Khoá học Claude toàn diện tiếng Việt" (Comprehensive Vietnamese Claude course)
  - **Stats (as of 2026-05-07):** 54,292 readers · 81,435 views · modified 2026-05-03
  - **Author:** Nguyễn Ngọc Tuấn, Founder Transform Group, Lark Platinum Partner
  - **Description:** "Claude & AI Fluency — 245 bài học · 15 khoá học · ~60+ giờ học · Nguồn: Anthropic Academy + tinh chế cho knowledge worker Việt Nam"

- **Derivative NotebookLM (the user's original question):** https://notebooklm.google.com/notebook/2a42eeff-a797-44cd-86d5-f8b8a4ee491b
  - 319 sources (uploaded `.md` files)
  - "Claude Couse 2026" — same content packaged as a NotebookLM

## Top-level wiki page IDs (8 confirmed via Browser MCP — partial)

These are the only sub-pages with anchor tags rendered on the root page. The full sidebar tree contains ~150+ more nested pages but Lark uses click-handler navigation (not `<a>` tags), so harvest cost via Browser MCP is high.

| Lark page ID | Title |
|---|---|
| `EY8kwGVvcirJTBkCFzalp71igQb` | Khoá học Claude toàn diện tiếng Việt (ROOT) |
| `TZMBwKoCPiSHj7kelzilsN9MgBf` | Tâm thế, mindset, skillset, toolset dùng Claude AI |
| `IORWw7lFDi6nMfkuugLlUJGYgYe` | 🔥Recap 5 buổi học Claude AI online |
| `A9yLwQECVirge8kbrVClGcuEgHb` | 18 - Xây dựng bộ Skills cho Claude |
| `RYUDwqHaeiNawikWsOLlgG1Dgre` | 19 - Mastering Claude Cowork |
| `RKyVwPgQgiCXMtkh0R8liR5Og9b` | 20 - Claude Design cho Designer UI/UX |
| `HXJ8wIoNniiMIckgSL2lvAVOgef` | 25 tập khám phá Claude AI |
| `So1awg7D6izCIpkjozJlx4zVg1g` | Lộ trình tự học 5 buổi × 2 tiếng |

URL pattern: `https://transform.sg.larksuite.com/wiki/<ID>`

## Sidebar inventory (49 titles partially harvested — IDs not extracted)

These titles are visible in the expanded sidebar tree. Full URLs require either clicking each (expensive) or hitting Lark's internal tree API.

```
Khoá học Claude toàn diện tiếng Việt   (root)
🔥Recap 5 buổi học Claude AI online
  ✅Buổi 1, Ngày 18/4
    Recap buổi 1
    Q&A buổi 1
  ✅Buổi 2, Ngày 20/4
    Recap buổi 2
      From Tony
      From Hai Le
  ✅Buổi 3, Ngày 22/4 @7.30 PM
    Recap buổi 3
      Example
      skill_creator_project.zip
      bitis-offer-onboarding.zip
      bitis-interview-kit.zip
      bitis-cv-screening.zip
      bitis-job-posting.zip
      tiktok-content-producer.zip
  ✅Buổi 4, Ngày 24/4 @7.30 PM
  ✅Buổi 5, Ngày 28/4 @7.30 PM
    Recap buổi 5
      guide.md
      Mastering_Agentic_AI.pdf
Anthropic courses
  01 - Claude 101
  02 - Claude Code 101
  03 - Claude Cowork
  Slide: Claud... [TRUNCATED at 4000 chars]
```

(The full inventory should be ~245 lessons across 15 paths/courses per the description.)

## Phase 2 — Full archive plan (deferred)

To get all 245+ pages locally, build a dedicated Lark scraper that:

1. Hits Lark's space-tree API endpoint directly (network inspection of any logged-in browser session reveals the URL pattern; usually `/space/api/wiki/v2/space/<spaceId>/node/...`)
2. Walks the tree breadth-first, collecting all `obj_token` values
3. For each page, requests the rendered markdown / HTML representation
4. Saves each as `<slug>.md` in this folder
5. Optionally also feeds each URL to `notebooklm source add` for queryability

Approximate effort: 30-90 min of engineering depending on Lark API friendliness. Output: ~245 markdown files + index.

## Phase 1 (now) — what we're doing

1. Save this manifest (you're reading it)
2. Add the 8 known Lark URLs to a new owned NotebookLM via `notebooklm source add` once CLI auth is refreshed
3. Test whether NotebookLM auto-follows internal Lark links when fed the root URL — if yes, this gets us a substantial clone in one call

## Risk profile

| Threat | Mitigation today | Phase 2 mitigation |
|---|---|---|
| NotebookLM owner deletes notebook | Lark wiki is public, accessible via root URL | Local .md archive of all 245 lessons |
| Lark wiki gets unshared/deleted | NotebookLM clone (with whatever sources we ingested) | Local .md archive |
| Both deleted | Lose anything not yet ingested | Local .md archive (the only true safe state) |
