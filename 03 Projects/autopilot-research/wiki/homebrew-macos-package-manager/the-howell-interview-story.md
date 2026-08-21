# The Howell interview story — and the correction the anchor exists to make

## The famous version

June 2015. Max Howell, who wrote Homebrew in 2009, interviews at Google and is rejected. He tweets:

> **"Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard so fuck off."**

Verified: [x.com/mxcl/status/608682016205344768](https://x.com/mxcl/status/608682016205344768). The anchor's paraphrase of it is accurate.

> *"Dòng tweet đó nổ tung, nó trở thành case study số 1 cho vô số cuộc tranh cãi kéo dài hàng chục năm: phỏng vấn kỹ thuật kiểu whiteboard có thật sự hiệu quả hay không."*
> ("That tweet exploded. It became case study number one for a decade of arguments about whether whiteboard technical interviews actually work.")

That much everyone knows. The anchor opens the video with it and returns to it at the end — the Homebrew explanation is the sandwich filling.

## The part the anchor made the video for

> *"Nhưng có một phần mà hầu như không ai kể lại, đó chính là lý do mình làm video này. Chính Max Howell sau đó đã lên tiếng bênh vực Google."*
> ("But there is a part almost nobody retells, and it is the reason I made this video. Max Howell himself later spoke up in Google's defence.")

Two specifics:

1. He said he genuinely could not invert a binary tree — *"anh còn chưa nắm rõ cây nhị phân là cái gì"*, he did not even really have a grip on what a binary tree was — **because he studied chemistry, not computer science.**
2. The post-interview feedback raised **several** weaknesses, not only that one problem.

**Both check out**, with a caveat on the first. Howell holds a **master's degree in chemistry**, left the profession after about a year, and came to software through open source, working at Last.fm and then TweetDeck before writing Homebrew. And he later clarified that his Google feedback mentioned multiple weaknesses, not just the binary-tree question. The specific "didn't know what a binary tree was" phrasing is graded **CBI** in [[claims-scorecard]] — the substance is corroborated, that exact self-description is not primary-sourced here.

The conclusion:

> *"Nói cách khác, một dòng Twitter viết lúc đang cay cú đã nén cả một buổi phỏng vấn phức tạp vào trong một câu cho sướng miệng. Rồi cái câu đó sống lâu hơn và đi xa hơn sự thật đằng sau nó cả trăm lần."*
> ("In other words, a tweet written while stung compressed a whole complex interview into one satisfying line. And that line outlived and travelled a hundred times further than the truth behind it.")

And the residue:

> *"Bài toán đảo cây nhị phân bây giờ chính là LeetCode số 226, nghĩa là hàng triệu người đang ngồi cày bài toán đó — một phần vì năm 2015 có một anh chàng bực mình trên Twitter."*
> ("Inverting a binary tree is now LeetCode #226 — meaning millions of people are grinding that problem, partly because in 2015 a guy was annoyed on Twitter.")

⚠️ **Problem #226 could not be verified directly** — `leetcode.com` returned HTTP 403 to this ingest. Secondary references consistently place *Invert Binary Tree* at #226. Graded CBI, not CONFIRMED.

The causal claim — that #226's prominence derives from the tweet — is **the anchor's interpretation, and unfalsifiable as stated.** The problem is a standard tree-traversal exercise that would plausibly exist regardless. What is defensible is the weaker version: the tweet made *this particular problem* a cultural shorthand for whiteboard interviewing. Keep the weak version.

## Why this belongs in a Homebrew wiki

Because it is **the same argument as the technical one, applied to a person.**

[[why-homebrew-won]] argues that the better-engineered tool lost, and that the record contradicts the folk story about merit. This section argues that the folk story about the interview contradicts its own protagonist's account. In both cases the anchor's move is: *go back to what the record actually says, and find that the memorable version is the distorted one.* That is a method, and it is the most portable thing in the video.

## The operator's own read, which is the last thing in the video

The anchor closes with his own position, and it is more interesting than the standard take:

> *"Mình thấy anh ấy trượt cũng có lý do. Lý do đến từ anh ấy và cả lý do đến từ Google. Howell sẽ phù hợp với vị trí như product owner hoặc là người phát triển product mới hơn. Anh ấy chính là owner … Anh ấy đã có một sản phẩm tuyệt vời, rất nhiều người dùng, mang lại value vô cùng to lớn cho cả thế giới. Anh ấy không cần phải thể hiện bản thân với bất cứ ai nữa. Nhưng vấn đề là vị trí anh phỏng vấn vào nó không phù hợp với những cái thứ mà anh ấy đã làm được."*

So: **not a hiring failure, a role-matching failure.** Howell's demonstrated evidence is product ownership and ecosystem stewardship. The role screened for something else. Both signals were real; they were about different jobs.

Then the structural point, on which the transcript cuts off mid-sentence at 13:56:

> *"Thêm một nguyên nhân nữa: hầu hết các công ty, để tối ưu quy trình tuyển dụng, họ không hề có hệ thống, có những bài test cho những ứng viên đặc [biệt]…"*
> ("One more cause: most companies, to optimise their hiring pipeline, simply have no system, no tests, for exceptional candidates…")

⚠️ Truncated — the available caption track ends here. Do not attribute a completed argument to him.

## The transferable claim, for recruitment work

Stripped of the story, the argument is:

> **A hiring pipeline optimised for throughput has no path for a candidate whose evidence does not fit its instrument. The instrument does not report "unmeasurable" — it reports "fail."**

That is a claim about **instrument validity**, and it is the same failure this corpus has already recorded twice from other directions:

- [[../nodejs-backend-interview/_index|nodejs-backend-interview]] — an interviewer's stated screening criterion that was **substantively inverted**, i.e. the instrument was measuring the wrong thing while reporting confidently.
- [[../mobile-engineer-interview/_index|mobile-engineer-interview]] — operator interviews on what senior signal actually looks like versus what gets asked.

Howell's case is the third instance and the cleanest, because the ground truth is unusually knowable: the candidate's work was, by the interviewer's own admission, running on 90% of the interviewer's engineers' machines. **When the artifact is that legible and the instrument still returns "fail", the instrument is the thing under test.**

For the recruitment product this corpus feeds, the operational form is a question, not a feature: *for a candidate whose evidence is an artifact rather than an exercise, what does the pipeline do?* If the answer is "scores them on the exercise anyway", the pipeline has a known blind spot with a famous name.

Note that this cuts **against** naive automation. The Howell case is not an argument for a better-scoring model; it is an argument that the scoring frame was wrong, which no amount of scoring accuracy fixes. That is consistent with the standing legibility policy for candidate-facing LLM paths — the requirement is that a decision be **explainable and contestable**, not merely accurate.

## Cross-links

[[why-homebrew-won]] · [[../nodejs-backend-interview/_index|nodejs-backend-interview]] · [[../mobile-engineer-interview/_index|mobile-engineer-interview]] · [[../data-structures-16-in-32-min/_index|data-structures-16-in-32-min]] — LeetCode #226 is a tree-traversal problem of exactly the class that topic covers · [[claims-scorecard]]
