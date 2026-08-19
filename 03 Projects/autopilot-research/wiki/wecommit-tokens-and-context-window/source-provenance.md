# Source Provenance

## The bundle

Four videos, **one creator**, ingested 2026-08-19 via **Path 1 `/loop` yt-dlp-only** (no NotebookLM, no yt-search).

| # | Video | Role | Published | Duration | Views at ingest | Transcript |
|---|---|---|---|---|---|---|
| 1 | [`yxQGugIwFaU`](https://www.youtube.com/watch?v=yxQGugIwFaU) "Mỗi lần chat, AI phải đọc toàn bộ lịch sử & cách tối ưu Token (Claude, ChatGPT, Gemini)" | **ANCHOR** — operator-submitted | 2026-08-15 | 26:58 | 5,887 | 747 cues → 59 ¶ / 6,948 words |
| 2 | [`4PKT7vFo334`](https://www.youtube.com/watch?v=4PKT7vFo334) "Claude: Cách Tôi Cho AI Vận Hành Cả Kênh YouTube (Demo thực tế và kỹ thuật tối ưu chi phí Token)" | sibling — longest | 2026-08-02 | 59:26 | 4,267 | 1,678 cues → 129 ¶ / 15,291 words |
| 3 | [`MshYeoy8g2o`](https://www.youtube.com/watch?v=MshYeoy8g2o) "Điểm yếu chí tử \"hay quên\" của AI Agent & chiến lược của các tập đoàn công nghệ" | sibling — oldest | 2026-04-22 | 33:11 | 5,189 | 916 cues → 72 ¶ / 8,411 words |
| 4 | [`QgDsHhy9Cpo`](https://www.youtube.com/watch?v=QgDsHhy9Cpo) "15 năm kinh nghiệm các dự án ngân hàng dạy tôi 1 nguyên tắc giúp AI Agent làm đúng \| Demo thực tế" | sibling | 2026-08-13 | 21:52 | 2,607 | 625 cues → 47 ¶ / 5,723 words |

**Total: 2h21m27s / 36,373 words.**

## The creator

**Trần Quốc Huy** — channel **"Learning Database with Tran Quoc Huy"**, handle [`@tranquochuywecommit`](https://www.youtube.com/@tranquochuywecommit), channel id `UCtsYzL7iN7rBCPnkjYp4XYw`, **189,000 subscribers** at ingest (`yt-dlp --print %(channel_follower_count)s`).

- Brand hashtags on every video: `#wecommit #tranquochuywecommit`. He sells a **"Coaching Agentic AI (no-code)"** program and links his own website for text versions of this material — **a commercial educator; the close of the anchor video is a soft pitch.** The method stands apart from the pitch, but the incentive is on the record.
- Self-described background, used as the authority claim in video 4: **~15 years on banking projects** and large-scale data work — he cites telecom systems of "a few billion records" and datasets of "a few hundred million records" (`QgDsHhy9Cpo`, and again at `yxQGugIwFaU` [24:01]). Unverified externally; treated as self-reported.

**Corpus-first on channel size — grep-verified.** At 189K subs this is the **largest Vietnamese-language source in the corpus**, roughly 2.5× the previous largest ([@hoidanit](https://www.youtube.com/@hoidanit), 74.6K, in [[hoidanit-fullstack-vibe-coding/_index]]). Other VN sources for comparison: Mì AI ~52K, LetDiv 9.2K, BizMate AI Official 7.4K, Thầy Hoàng JS/CodeFarm 1,920, Dũng - Chia Sẻ Công Nghệ 1,320.

> ⚠️ **Grep trap for future sessions:** the string `189K subs` already appears in `_master-index.md` for **Jason Lee (@jasonleefinance)**, an English-language channel in [[jasonlee-claude-mobile-app/_index]]. The identical figure is pure coincidence — two different channels. Do not conflate them.

## How the bundle was selected

The three siblings were **not** chosen by the yt-search rank rubric. They are the three "related videos" the **anchor's own description links**, i.e. **creator-declared siblings**. This gives higher precision than search rank (which has dropped operator anchors before — see the anchor-injection note in `raw/topics-queue.md`) and makes the bundle a coherent single-author series rather than a topic sweep.

## Capture method

```
yt-dlp --skip-download --write-auto-subs --sub-langs vi-orig --sub-format vtt
python bin/vtt-to-md.py <id>.vi-orig.vtt <id>.md
```

- **Auto-captions only.** `--list-subs` reports *no* manually-authored subtitle track on any of the four — only automatic captions, in `vi-orig` (Vietnamese original) plus ~100 machine-translated languages. **ASR garble is therefore expected throughout** and is catalogued in [[caveats-and-corrections]].
- `bin/vtt-to-md.py` strips YouTube's rolling-caption duplicates and `<c>` word-timing tags, emitting `[MM:SS]` paragraphs. All four transcripts were read by per-video extraction subagents; the **anchor was additionally read directly in the main loop** as a faithfulness check on the extraction.
- No cookies needed — all four are public.

## Provenance findings (things the sources get wrong about themselves)

1. **Video 4 was retitled.** The anchor's description links it as *"Vì sao AI Agent của anh em làm sai hoài? Bản chất ở đây & Demo thực tế"*. Its current title is *"15 năm kinh nghiệm các dự án ngân hàng dạy tôi 1 nguyên tắc giúp AI Agent làm đúng | Demo thực tế"*. Same video id, retitled after the anchor published — the link text no longer matches the target.

2. **⭐ The "exact Claude encoder" claim is description-only.** The anchor's description asserts: *"Mọi con số trong video tôi đều cho chạy đếm thật trên đúng bộ mã hóa mà Claude đang dùng"* — every number was counted on the *exact* encoder Claude uses. **A grep across all four transcripts (36,373 words) returns ZERO hits** for `mã hóa`, `tokenizer`, `encoder`, `tiktoken`, `cl100k`, `BPE`, or any named library. He **never names a tokenizer on camera in any of the four videos.** The strong claim lives in the marketing copy, not in the content; on camera he speaks generically of "bộ từ điển" (the vocabulary/dictionary). See [[claims-scorecard]] for the verdict this drives — it is a materially fairer finding than "he claims to use Claude's tokenizer," and it is the single most important provenance distinction in this topic.

3. **The on-screen tool is unverifiable from captions.** The description promises a live demo of a Vietnamese sentence being tokenized, and he narrates one ("tôi cho anh em xem tận mắt một câu tiếng Việt bị băm ra"). **Which tokenizer UI he has open cannot be determined from an audio transcript** — no frames were analysed. Any claim about *which* tokenizer produced his numbers is therefore out of reach of this ingest. Stated as a boundary, not filled in.

## What this ingest does NOT cover

- **No video frames were examined.** All on-screen numbers, UIs, dashboards, and code are known only through his narration.
- **The text versions on his website were not fetched** — he references written versions of this material; only the videos were ingested.
- **His paid coaching program's content is out of scope** — only the free public videos.

## Cross-links

- [[claims-scorecard]] — every load-bearing claim with its verdict
- [[caveats-and-corrections]] — ASR garble map + what to un-learn
- [[overview]] — what the bundle teaches
