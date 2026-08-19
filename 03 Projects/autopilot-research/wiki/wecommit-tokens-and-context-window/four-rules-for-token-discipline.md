# Four Rules for Token Discipline

> **Source:** anchor [`yxQGugIwFaU`](https://www.youtube.com/watch?v=yxQGugIwFaU) [21:19]–[26:19] — the chapter he titles *"4 quy tắc dùng AI sau khi hiểu token"*. This is the actionable payload of the bundle.
> Read directly from the transcript in the main loop, not only via extraction.

## Rule 1 — Never let the model compute; make it write code

> *"Nếu để nó đoán trên token thì khả năng bị sai… Yêu cầu nó tạo ra code hoặc script để thực hiện tính toán."* — [21:47]

Because the model works on token ids and not numbers, any arithmetic, counting, reconciliation, code-checking or format-validation it performs is **guessing**. Have it emit a script and run that instead — then the result is deterministic. He stresses this holds **whatever tool you use** ("dùng Claude, dùng Codex, tool nào cũng thế").

**This is the strongest idea in the bundle**, and it independently re-derives **Rule 5 of this vault's own CLAUDE.md** — *"Use the model only for judgment calls… If code can answer, code answers."* He arrives at it from database engineering; the vault arrived at it from harness engineering. Same rule, two lineages. It is also the mechanism behind Anthropic's programmatic tool calling and code-execution features.

## Rule 2 — Demand terse output; consider answering in English

> *"Hãy yêu cầu nó cắt toàn bộ những cái gì mà thừa thãi… lấy đúng kết quả."* — [22:14]

Output bills at **~5× input** ([[claude-pricing-ladder]]), so padding is the most expensive text in the exchange. Two levers:

1. Instruct it to drop pleasantries and return only the result.
2. **Have it answer in English if you can accept that** ([20:49]) — because of [[vietnamese-token-inflation]], the same answer in Vietnamese costs materially more. *"Nếu chúng ta chấp nhận trả ra tiếng Anh thôi thì tiền nó khác hẳn luôn."*

Rule 2 is where the Vietnamese-specific economics turn into an actual decision, and it is advice you will not find in an English-language course.

## Rule 3 — Describe the problem before you send the data

> *"Đừng có đưa cho AI và yêu cầu nó làm ngay lập tức. Hãy chậm lại một bước."* — [22:41]

His worked example, for any dataset task ([23:08]–[24:57]) — **send none of the data at first**:

1. State the business problem ("this is my e-commerce sales data, I need to find winning products").
2. Give the **structure** — the columns and what each means.
3. Give a **few sample rows** so it can picture the shape.
4. Give the **total row count** — 1,000 vs 2,000 vs 1 million. *This is his data-engineering instinct:* volume changes the correct algorithm. He cites prior systems with hundreds of millions to billions of records in telecom.
5. Then ask: **"given this structure and goal, which columns do I need and which can I drop? How many sample rows do you need? Are any column names ambiguous?"**

The point of step 5 is explicit: *"tôi muốn loại bỏ tối đa những dữ liệu thừa thãi phải đưa vào cho AI… giảm được token đầu vào rồi, mà giảm cái sự [xao nhãng]"* — cut junk input to cut tokens **and** cut distraction.

> ⭐ **His conclusion is the important part:** *"Chính xác và đỡ tốn tiền nó đi liền với nhau"* — **accuracy and cost-saving go together.** They are not a trade-off.

That independently reproduces the "context engineering is intelligence-positive" thesis already in the corpus from an Anthropic Platform-team talk ([[claude-api-cost-optimization/context-engineering]]): removing junk context does not merely cut tokens, it improves output because the model sees only what is relevant. Two unrelated sources, same finding.

## Rule 4 — Partition by strength, and make it ask

> *"Hãy dùng đúng điểm mạnh của nó là phán đoán, diễn giải, tư duy, suy luận. Còn lại hãy dùng cái tool khác."* — [25:53]

Split the job explicitly:

- **Must be exact** — calculations, counting, cross-checking, code processing, format validation → **write code**, never let the model judge it. *"Không được tự tính."*
- **Judgment, interpretation, writing, reasoning** → let the model do it. That is its actual strength.
- **And always instruct it to ask:** *"nếu thiếu dữ kiện thì hãy liệt kê ra hỏi tôi"* — if facts are missing, list them and ask, rather than proceeding on assumptions.

The closing line is the whole method: *"Hãy làm việc với AI bằng cách chậm thôi thì AI sẽ rất là hiệu quả"* — work slowly and the AI becomes far more effective.

## Why these four rules are better than they look

They are derived, not collected. Each falls out of the tokenization mechanics in [[tokenization-mechanics]]:

| Mechanism | Rule it produces |
|---|---|
| The model manipulates token ids, not numbers | 1 — code for exactness |
| Output bills ~5× input; Vietnamese inflates volume | 2 — terse output, English when acceptable |
| Everything you send becomes billed input, and junk crowds the signal | 3 — schema first, data last |
| The model is good at inference, bad at determinism | 4 — partition by strength |

The "ask me when facts are missing" instruction also converges with the interview-first pattern the corpus documents elsewhere ([[pocock-real-feature-build/_index]]'s grill-me stage).

## Cross-links

- [[tokenization-mechanics]] — the mechanics each rule derives from
- [[vietnamese-token-inflation]] — why rule 2's English option matters here
- [[claude-api-cost-optimization/context-engineering]] — the independent confirmation of rule 3
- [[banking-principle-for-agent-correctness]] — video 4 extends rule 4 into explicit pass/fail criteria
- [[hireui-relevance]] — applying all four to a real product
