---
source: manual yt-dlp transcript capture (interactive session, not yt-pipeline)
topic: prompt-evaluation
generated: 2026-06-16
videos_count: 2
notebook_id: (none — direct transcript, no NotebookLM)
deliverable: report
---

# Grading with AI — Anthropic "Building with Claude" Lesson 17 (source capture)

## Sources

- **Video 1 (entry point — Vietnamese localization):** `( Việt Hóa ) CHẤM ĐIỂM BẰNG AI | Khóa Học Claude API - Building with Claude - Bài 17` — channel **BizMate AI Official**, 601s, uploaded 2026-06-16. https://www.youtube.com/watch?v=nYMcPrnRzhI
- **Video 2 (the "original resource" — original English lesson):** re-upload (placeholder title), channel **Stoic Manhood Guide**, 601s, `en-orig` captions. https://www.youtube.com/watch?v=GjakSOir2dE
- **True canonical original:** Anthropic **"Building with the Claude API"** course → **"Prompt Evaluations"** module → the grading lesson (`grade_by_model`, `run_test_case`, test-case dataset). Repo: https://github.com/anthropics/courses

> Both videos are the identical 601-second lesson. Video 1 is BizMate's VN dub; Video 2 is the original English audio. Captured via `yt-dlp --write-auto-subs` (en-orig), parsed from srv1.

## Verbatim transcript (original English, cleaned)

The next thing we're going to implement inside of our prompt evaluation workflow is a grading system. A grader takes in some output coming from our model, and our hope is that the grader gives us some kind of objective signal — a number, or a true/false value. Very frequently you'll see a number output between 1 and 10, where 10 means a very high quality output and 1 means a very low quality output. That's not a requirement, but it's a very common practice.

There are three different kinds of graders: **code, model, and human.**

**Code-based grader:** take the output from our model and feed it into a snippet of code that you author. Inside this code you can do any programmatic check — verify the output was not too long or too short, make sure it does/doesn't have certain words, do JSON/code syntax validation, even more complex checks like a readability score (make sure generated text is at an appropriate reading level). The only requirement is that running the code returns some actual signal (usually a number 1–10, not a hard requirement).

**Model-based grader:** take the output from our original model call and feed it into an additional model — another API request. This gives a tremendous amount of flexibility: evaluate a response on general quality, how well it followed prompt instructions, completeness, just about anything. The only real requirement is the model gives back a hard objective signal, usually a number 1–10.

**Human-based grading:** put all the model outputs in front of an actual person who evaluates them. Humans are very flexible — evaluate for any metric imaginable. The big downside: it takes a lot of time and is tedious work.

No matter the style, **you decide upfront what your evaluation criteria are** — exactly which aspects of the responses you focus on. For this use case the criteria are three:
1. Only get back Python, JSON, or regex with no additional explanation from Claude.
2. The Python/JSON/regex has valid syntax (no typos).
3. General task-following — the model clearly addressed the user's task with generally accurate code, no major errors or logic mistakes.

Criteria 1 and 2 → **code grader** (validate format; validate syntax). Criterion 3 (flexible, judgment) → **model grader**.

**Implementing the model grader** (`grade_by_model`): pass in the test-case dictionary (each dataset value is a test case) and the output from the original model call. Inside, call a model and ask it to grade the output. The prompt is fairly long — it sets a role, asks clearly for the model to evaluate an AI-generated solution, prints the task, lists the generated solution, and gives directions on exactly how to respond. Here we ask the model for a list of **strengths and weaknesses** of the solution, the **reasoning** behind it, and an **actual score**.

> **Key insight:** if you ask for a score by itself, you very often get scores of just 6 — middling scores, because the model assumes "could be better, could be worse, give it a 6." By asking the model to provide reasoning, strengths and weaknesses, you make it hone in and decide on a more concrete score.

Call the grading model: build a messages list, add a user message; because we get back JSON, extract it cleanly using a **prefilled assistant message** (```` ```json ````) and a **stop sequence** (closing ```` ``` ````). Then `json.loads` the eval text and return it.

Wire it in: in `run_test_case`, replace the placeholder `score` with `model_grade = grade_by_model(test_case, output)`; extract `score` and `reasoning` from the returned dict (it also contains strengths/weaknesses lists). Put score + reasoning into the final output dict.

**Aggregate:** average all the scores — comprehension over `result["score"] for result in results`, wrapped with `statistics.mean` — and print the average. The run produced individual scores of 8, 7, 6 and an **average score of 7.33**. This gives a final objective metric: it may be a bit capricious and could use better guidance, but now there's a score to focus on and try to increase.

## Compile note

Compiled into `wiki/prompt-evaluation/` on 2026-06-16. See `_master-index.md`.
