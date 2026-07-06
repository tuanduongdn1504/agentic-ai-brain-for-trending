---
source: yt-dlp-only (operator-submitted VN dub → resolved to Anthropic first-party original)
topic: claude-tag-multiplayer-agent
generated: 2026-07-06
videos_count: 2 (1 original + 1 full VN dub of the same content)
notebook_id: — (no NotebookLM; yt-dlp captions read directly in main loop)
deliverable: report
---

# Claude Tag — "The future of work with @Claude" (Anthropic first-party launch interview)

## Source chain

1. **Operator-submitted:** `6kU_TpceoJ4` — BizMate AI Official (VN), "(New Update) Anthropic ra mắt Claude Tag: Giải pháp AI đa người dùng cho doanh nghiệp", 2026-07-05, 11:26, ~292 views at ingest. **Full Vietnamese dub** of the Anthropic original (same 11:26 runtime, full lồng tiếng + Vietsub; description credits the original + links Skool community `bizmate-ai-community-9131` + `anthropic.skilljar.com`). VN VTT read in full in main loop.
2. **Original (double-dive target):** `MhfnicQVkgY` — official **Claude** channel, **"The future of work with @Claude"**, published 2026-07-02, 11:26, ~87,069 views at ingest. Speakers per description: **Boris Cherny (Head of Claude Code)** + **Cat Wu (Head of Product, Claude Code)**. EN VTT (official captions) read in full in main loop.
3. **Product:** Claude Tag — claude.com/tag ("Claude Tag is available now in Slack (beta)"), docs claude.com/docs/claude-tag/overview, announcement anthropic.com/news/introducing-claude-tag.

## Official video description (verbatim)

> "In the past, you had to open Claude and ask. With Claude Tag, Claude jumps in." In this conversation, Boris Cherny (Head of Claude Code) and Cat Wu (Head of Product, Claude Code) walk through how they got there: the long-horizon and alignment research that lets Claude stay on track for days at a time, the memory system that finally feels right, and how usage spread inside Anthropic. Today, 65% of the product team's code is created by Claude.
>
> Claude Tag is available now in Slack (beta). Learn more: claude.com/tag

## Full English transcript (official captions; speaker attribution NOT in captions — labels below are inferred and pending verification)

[00:00] What do you do if there's no Claude in the channel? — I don't know, I can't remember a world without Claude in the channel.

[00:15] (Interviewer?) Walk me back. Three years ago, we were just starting to adopt AI into our day-to-day workflows. What was it like back then? And take me all the way to where we are today.

[00:26] (Boris?) I remember two years ago, I was still using typeahead. That was what AI could do as an engineer. And you know, we built Claude Code, we brought agents, and kind of the next generation of ways to do your coding. And it's just changed so much since. With typeahead, I was still deciding, I want to write this line of code, and the agent was helping a little bit. It was just writing the line. And then we got to the point where it was writing whole functions, whole files, whole features. And I feel like now with Tag, it just does the whole thing. It can write the feature, it can do an entire experiment end-to-end, it does my data analyses. It's been like two leaps in 2 years.

[01:09] (Cat?) When I think back to the last couple of years, it's almost like this transition. We went from a person always in the loop, it's one person sitting there, and they're just typing a line at a time. We got to one person sitting there with like 10 Claudes, you know, typing a bunch of features at a time. Now we're at the point where Claude is actually driving a little bit more. And it's not just one person anymore, it's an entire team that's interacting with it.

[01:37] So, what is Claude Tag? — In the past, you had to open Claude, and you had to ask it something, and then Claude would do the work. It'll use your tools, it'll use your computer, and it'll get the task done. That's the way that it used to be. With Claude Tag, Claude jumps in, it's proactive, it knows when to jump in. It'll do the work, even if it takes days or weeks, and it'll follow up. And I think the coolest thing is, it'll remember what I told it for next time. Before, I would have to prompt Claude every time, and I would have to say, "Claude, now do this, or now do this." I would have to remember to do that. Now we just add Claude to a channel, it will proactively jump in and do the work. Everyone gets to see it, everyone gets to participate, because it's multi-player, and it'll remember for next time.

[02:28] Okay, so what on the research side actually enabled this? How is it that Tag is so good?

[02:34] For many years, we've been working on making our models more long-running and autonomous. So if you look at the latest METR evals, our latest models can work for 16 hours at a time, and are now in the zone where we can't even accurately detect how long it's able to work for. In something like Claude Tag, Claude is able to self-schedule work for itself. And so you can take this one 16-hour task, and it actually increases over time because Claude can schedule a follow-up after days, or weeks, or months.

[03:08] I feel like the task that we couldn't trust it to do before, now it can get almost every single time. I have a bunch of these Claude Tag sessions, personally, that are running for days, weeks. I think I might have one that's a month. It's essentially this long-running experiment, and it's just checking in every day, checks the data, once in a while, it sends a bug fix if there's a bug that needs to get fixed. I just see the pull requests coming in, and I get these data readouts every day.

[03:32] The other big innovation is just being able to have memory in the model. The model can not only set reminders for itself, but it can also remember just all the instructions that all the users have given it over time. Memory took a long time to crack. I think we tried to get it right for Claude Code for years, and it feels like we finally got it right. It feels really good to use.

[03:56] If you're working with Claude Tag in a channel, and you tell it, "Hey, I want you to monitor only for this type of issue, but not these other categories," it will do that. It will remember that for that channel forever after. And then, if someone else says, "Hey actually, let me expand your scope to this new thing," it will adjust.

[04:15] Another big thing that people love is Claude's personality and EQ. Sometimes when I talk with people about adding Claude Tag into a channel, they say, "Oh, how do I know it won't jump in on every thread and be annoying?" Well, Claude is trained to have a good sense for when it's needed, and it can take the back seat. If it ever goes too much in the wrong direction, you can just tell it to do something different, to jump in less, or jump in more, and it'll just remember it for the future.

[04:45] (Interviewer?) So when you look at the internal usage, and when you talk with our customers who are getting started on Claude Tag, what are the patterns that you see?

[04:53] The coolest thing to me has been how customers are figuring it out. It can write your pull requests, it can debug production issues, it can do data analysis. All you have to do is hook it up to your tools. I think that's only possible because the memory is just so good. And I've seen people do this emergent stuff where, you know, for example, this is a channel for Q&A, anytime a question is answered, you must check it off. You tell Claude Tag this, and it'll just do that. It'll answer the questions, and it'll react with a check every time, and it'll just do this for you.

[05:24] We have a channel for data questions, and now Tag just answers all the questions. Or we have the channel for Claude Code feedback, and Tag just fixes everything now. The most common way that I ask a data question is, I post in our data channel, but then I tag Claude Tag, and then it takes the first pass, and normally it's pretty good. I kept doing this in a bunch of channels, and then I just got tired of tagging it, so I just told it, "Please respond every time." I think it goes to show how powerful the memory is, that you're able to do something like this. You can just tell it, "Hey, remember to always do this thing," and it just has your back. It's been a huge shift in how we all do work.

[05:58] I think this also is a way for more people to understand how to work with AI. Because Claude Tag is working in public channels, everyone is able to observe how the expert users leverage it. And then they take those patterns, and they bring it to new projects that they're working in. And so both internally and in the customers that we've been working with, we've been seeing this diffusion of Claude Tag best practices that is, I think, very novel to AI tools.

[06:28] It was surprising how fast it took over. I feel like now I see Tag in every channel that we have; every feedback channel, every data channel. It started with a few people using it, but I think as other people saw those people using it, they quickly picked it up. It's been very empowering to be able to have Claude Tag have my back.

[06:46] So for a lot of our existing tools, like Chat, Cowork, and Claude Code, you typically have to remember to open it. And so it's a more reactive experience. And one thing that's great about Claude Tag is you give it this higher-level objective, like put up PRs for every bug in this channel, and it just has your back and puts up a PR for every single one without you needing to remind it.

[07:10] The second thing that's really cool is that it's multi-player. So almost all of the AI tools that people use right now are just you and Claude working together, and then copy and pasting this output to your team. And I think the big shift that Claude Tag allows is, it brings Claude right into the middle of your work so that multiple people can guide the session to a better output.

[07:33] There's so many, like, dynamics here. Like one, we're all learning about how to use Claude Tag better by observing other people. Claude Tag is learning how to better work with us by hearing the guidance that we're giving it. At the end of the day, the customer gets a better result, because it's not just my opinion of how we should solve it, it's our whole team is able to jump in to nudge this PR to the best possible state.

[07:57] I mean, I love this idea. I keep telling everyone, I want everyone to contribute to the code base, and so many people are afraid because they have to, like, open a terminal, even the desktop app, because you have to deal with a Git and code checkouts and stuff. And with Tag, they can just do it. It's really cool.

[08:14] The other thing that I think is really important is making sure that your collaboration platform has public channels. That way, Claude Tag can monitor different projects that you're tracking. So as a PM, I'm often working on maybe five to 10 features, and I have Claude Tag look at the status for every single one, and then give me a daily report.

[08:33] The other big unlock we've been seeing is that, people can now self-serve their questions. When people onboard to our company, instead of asking Legal about whether they can say this, or instead of asking our HR team what our benefits are, they can just tag Claude Tag. And because Claude Tag is connected with our source-of-truth files, it can give them a really fast answer, no matter what time they're looking for it.

[08:58] I think the single biggest thing is just how much more productive it's made everyone. And, you know, this is driven by our internal version of Claude Tag. And if you look at just the product org, so, the part of the company that we sit in, the number of PRs that are written by Tag, I think it's like 65% now, and it's just climbing like this. I thought that Claude Code was the thing that makes engineers go faster. This is a product that makes engineers go way faster.

[09:25] I think actually, a lot of the reason is, because the way you're interacting with it, you ask Tag to do something, and it'll respond, and you move on to the next task. So you actually want to set it up in a way where Tag can do the work, and you don't have to check in all the time.

[09:42] (Interviewer?) You have hundreds of these Claude Tags running, but you're still a power user of Claude Code. How do you decide when to reach for each of them?

[09:50] (Boris?) Yeah, so I used to use Claude Code for everything, and then I started using Tag for more and more things. First, it was really simple fixes. Someone has a bug, the button's off by a few pixels or something. I'll just ask Claude, "Please fix it." Or someone has a simple data question, I'll ask them to fix it. And I think what's been happening more and more over the last few weeks as I've been getting more comfortable with the product, is I've been using Tag for just more and more things. And even more complicated work, it's actually able to do. Because it can verify its work, because it's running in the same remote sandbox that we use for mobile and for the desktop app, and it's using the same agent SDK. So it's just as intelligent.

[10:31] When you add memory to this, in different channels, I have specific preferences about how I want it to verify. It might be a little bit different for every channel. Often what it does is it'll fix some bug, then it'll post back a video in Slack, and I don't even have to leave it.

[10:45] (Interviewer?) What's next for Claude Tag?

[10:48] So we launched Claude Tag in Slack, and we're excited to bring it to more platforms where people collaborate, like Microsoft Teams. We want to make sure that every knowledge worker is within arm's length of Claude, no matter where they're getting their work done. And I think one of the coolest parts of Claude Tag is, it's not just changing how individuals work, it's putting Claude in the center of teams and transforming entire orgs. We've built Claude Tag to be incredibly customizable, just like Claude Code. And I'm so excited to see how orgs customize Claude Tag and make it their own. I can't wait.

## Key claims extracted (for verification)

1. Claude Tag = proactive, multi-player Claude in Slack channels; beta on Enterprise + Team plans (product page).
2. METR evals: "our latest models can work for 16 hours at a time… we can't even accurately detect how long" (Boris).
3. Self-scheduling: Claude schedules its own follow-ups days/weeks/months out; sessions running for a month.
4. Memory in the model: remembers all users' instructions over time, per-channel standing config, adjustable conversationally.
5. Trained "EQ": knows when to jump in vs stay back; tunable by telling it.
6. 65% of product-org PRs written by Tag (Cat); description restates as "65% of the product team's code is created by Claude" — wording drift PR-vs-code.
7. Runs in the same remote sandbox as Claude mobile/desktop; same Agent SDK; "just as intelligent" (Boris).
8. Positioning vs Chat/Cowork/Claude Code: those are reactive open-it-yourself tools; Tag is proactive with higher-level objectives.
9. Public channels prerequisite: best-practice diffusion by observation; PM daily status reports across 5-10 features.
10. Self-serve Legal/HR answers via source-of-truth file connections.
11. Roadmap: Microsoft Teams + more collaboration platforms; "incredibly customizable, just like Claude Code".
12. VN dub (BizMate) is a faithful full-length re-voicing with no added analysis; wraps Anthropic content for VN audience with Skool community + Skilljar cert links.

## VN dub notes (from full VN VTT read)

- Dub renders "@Claude"/"Claude Tag" variously as "Claude Tag / Clawd Tag / Quad Tag / QuadTag / Cotag / CodTag / ClawTag" — caption-garble of the same name; no content divergence found vs EN captions.
- Description adds BizMate framing: "Video gốc của Anthropic được thực hiện hoàn toàn bằng tiếng Anh. BizMate Việt hóa toàn bộ… hoàn toàn miễn phí."
- No indication of authorization from Anthropic for the re-dub; monetization angle = Skool community funnel.
