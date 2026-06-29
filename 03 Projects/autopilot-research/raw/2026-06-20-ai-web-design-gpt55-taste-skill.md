---
source: yt-dlp (path 5, operator-submitted single video)
topic: ai-web-design-workflow (GPT-5.5 / Codex + Taste Skill + Images 2.0 + Seedance 2.0)
video_id: PFO01z7Qe38
video_url: https://www.youtube.com/watch?v=PFO01z7Qe38
title: Redesigning Websites with GPT-5.5 & Images 2.0
channel: Lukas Margerie (@lukas-margerie)
upload_date: 2026-04-24
duration: 7:18
views: 31231
generated: 2026-06-20
captions: en (auto), deduped via bin/vtt-to-md.py — 216 unique cue lines, 16 timestamped paragraphs
deliverable: report
note: operator ask = "build knowledge + DOUBLE deep-dive into the original resource + pilot methods"
---

# Redesigning Websites with GPT-5.5 & Images 2.0 — raw ingest

## Video description (verbatim — resource links)

> 👉 Chat with me: https://discord.com/invite/vZxn6wZrDD
> 👉 Join the next live build: https://www.skool.com/builderzgym
>
> GPT 5.5 is here — and it's not just hype. I put it to the test using OpenAI's Codex to build a full landing page from scratch, and the results genuinely surprised me.
>
> In this video, I compare Claude (Opus) vs GPT 5.5 side by side, use the Taste Skill to redesign the site, generate custom images with ChatGPT Images 2.0, and animate them with Seedance 2.0. This is the future of web design — and it's happening right now.
>
> ⏱ Timestamps
> 0:00 GPT 5.5 potential + use cases
> 1:19 Project setup + goal
> 2:01 Claude vs GPT 5.5 comparison
> 2:53 Installing Taste skill + redesigning the site
> 4:34 Using AI images (Images 2.0) to upgrade sections
> 5:54 Adding animation (Seedance 2.0) + refining final design
>
> What you'll learn:
> How to use OpenAI Codex with GPT-5.5 for web design
> How to install and use the Taste Skill (Redesign command)
> How to generate and replace section images using ChatGPT Images 2.0
> How to animate static images with Seedance 2.0 for a dynamic Hero section
> Claude vs Codex — which one actually builds better landing pages?
>
> Tools used in this video:
> - OpenAI GPT-5.5: https://openai.com/index/introducing-gpt-5-5/
> - ChatGPT Images 2.0: https://openai.com/index/introducing-chatgpt-images-2-0/
> - Seedance 2.0: https://higgsfield.ai/seedance/2.0
> - Taste Skill (GitHub): https://github.com/leonxlnx/taste-skill
>
> Follow me on socials:
> X: https://x.com/lukas_margerie
> LinkedIn: https://www.linkedin.com/in/lukas-margerie-99196118a/

## ORIGINAL RESOURCES to double deep-dive (extracted)

1. **Taste Skill** — https://github.com/leonxlnx/taste-skill — THE load-bearing original (a real, fetchable skill repo; `gpt-taste` + `redesign` commands). Centerpiece deep-dive.
2. **OpenAI GPT-5.5** (run inside OpenAI Codex) — https://openai.com/index/introducing-gpt-5-5/
3. **ChatGPT Images 2.0** — https://openai.com/index/introducing-chatgpt-images-2-0/
4. **Seedance 2.0** (image→video animation, on Higgsfield) — https://higgsfield.ai/seedance/2.0
5. Context examples named in-video (not deep-divable resources, just attribution): Pietro Schirano / Magic Path "time machine"; Jake Soft Servo robot-arm configurator; Anton Guilds landing-page prompt (community, not public); Pinterest as image-inspiration source.

## Full transcript (deduped, [MM:SS] verbatim auto-sub)

**[00:03]** Hey guys, now GPT 5.5 is finally here. And with this great leap forward from OpenAI, this insane next step towards the inception of AGI, I really don't feel limited by what this model can do. I actually feel limited by what I can imagine. And just to show you quick little example of what you can build with this. This is an example built by Pietro Schirano, who's the founder of Magic Path. He built this time machine where you can prompt out the moment in time where you want to go, and Codex using GPT 5.5 and the new image model

**[00:33]** will basically create this panoramic view trapped in time in the specific moment. Not only that, I've seen posts by other people like Jake Soft Servo creating a robot arm with GPT 5.5. So, as you can see, you have like these different configurators on the right. It's 100% generated in Codex. And he says a similar result would have taken me weeks stitching half a dozen tools together. But something that really got me interested and what really inspired me to create this video was using GPT 5.5 to build a landing page for product

**[01:03]** and creating the images with ChatGPT images 2.0, which is their new model, and animating these specific images with C dance. And it's not just this example that caught my attention. I've seen a couple of other ones as well. I just want to use this time in today's video to explore what we can do with GPT 5.5 and web design in general. So guys, without further ado, let's go ahead and get started. So first thing I like to do here is I always want to create a new folder, and we're going to name this one. We're going to call it GPT 5.5

**[01:30]** designer. And we're going to open up Codex and choose our project using existing folder. To get started, I'm going to be using this prompt that you know, shout outs to Anton Guilds for making this. Anton is a really great designer in my community. And if you guys want to join my community, my Discord community, feel free to join that link down below. We get together every single weekday to talk about different tools and topics. So, you know, if you guys are interested, you're free to join. So I'm going to get this prompt, copy this. So over here on the

**[01:58]** left we have Claude running on Opus 4.7 with an extra high effort setting. And over here we have on the right side we have Codex using the same exact prompt, but running on GPT 5.5 also with an extra high intelligence setting. So we can go ahead and submit both of these. And so on the left we get what Claude gave us. And on the right is what Codex gave us. And you can see if I scroll through this really quickly, it gives us a nice design. I don't know if it's better than the one for from

**[02:26]** Claude code and you know, to start off with, but you can see that this is a really nice over here. Um everything else looks pretty solid. And the Claude one, let's see. Let's open it up. Actually, this one is a little bit worse than the other one, than the Codex one. All in all, I actually like the Codex design much more, but there are different ways to improve your design here. And so there's this skill called the taste skill. And we can go down here and you can copy this command

**[02:51]** to install the CLI in Codex. I can say install the taste skill. And so this skill comes with different commands. So the taste skill GPT taste, taste skill, we have redesign skill, and you can kind of read through the description of each one. I, for example, will try try this out with the redesign skill. All right, so let's install that GPT taste skill from GitHub. So all we have to do is restart Codex to pick up the new skills.

**[03:19]** And then I can go ahead and type taste and use that GPT taste skill and say let's redesign this site. And just like that we get our site redesigned like this. Um very very nice interesting background that it chooses an image. The recorded transcript and post editor sit in one continuous workflow. And now we have this kind of weird transition with the Bento, but it's interesting. I'm just going to see what else we got.

**[03:46]** This nice little sticky scroll over here. The text kind of fades in like so. That looks interesting. We have these like nice little hover interactions for this section. Clear cast made our customer calls useful twice. First for research, then for distribution. The post still sound human because the source is clean. And we have this section down here. Looks pretty cool. You have the text. We have this image. Kind of reminds me of like some type of framer template. And I mean, if you compare it to the old site,

**[04:14]** which is this one, again, I'm just going to show you how that looks. I really like the redesign that they that I did over here. I like the the new Bento grid more. It looks less AI generated, I would say with the skill. There are still a few things like I don't like this screw There are little details that that I don't really like. For example, this. And let's try to fix that now. And now Costel Matrescu, who is in my community, gave me this image. Very very nice section with these gradients in the

**[04:41]** background. And what I would try to do is I would use a new image two model from GPT to redesign this based on the context of my landing page and then get that result, feed it into Codex and try to see what happens. So I can say something like this is an image of a section in a website. Can you redesign it as an image based on the following prompt? And this is the prompt that I used in the beginning to generate this site. And we get this output, which looks pretty interesting. And then I would want to replace that over here.

**[05:08]** All right, so now this isn't even done yet, but it's looking much much better and something I really want to get rid of is this over here. So what I'm going to do is I'm just going to go over here and click on annotate. And then we can click on this and we can say delete this and just click on enter and submit. And after maybe less than a minute, it gets deleted. And going back into Pinderes, we can look at more types of image

**[05:37]** examples like maybe something like this. And then again, paste that into ChatGPT. Then you can say something like replace the background image of the truck in the desert with this image. You just attach that image that you got generated from ChatGPT. And we get our nice image in the background. I still think it's kind of like it's too static. So in this case we can use something like C dance to animate this image. I'll create like an 8-second animation 16 by 9. Use model C

**[06:04]** dance 2.0. I can say something like slowly animate the sound waves. Let's see what we get. And while that loads, in the meantime I found this little Bento grid over here. And again, using ChatGPT, basically asking it to redesign this Bento grid with the context of my site. And then saying redesign this Bento grid based on the attached image. Back here we get this animated gradient. It has sound, so I'll probably ask it to take the sound away. All right, so here we get our nice little Bento grid or like new grid I would say

**[06:32]** that we generated from ChatGPT. And I can say something like replace the attached video with a background image of the hero section. All right, cool. Now we're getting that little video in the background of the hero section. And then finally we get a new site with a nice video background, clean hero section. We can scroll down here. We get this new section over here. Get this nice text fade in. We get this nice section that kind of describes what this app does. And then we get a very simple footer at the end. So that's it, guys. That's pretty much the whole video testing out GPT 5.5 with web design. Let

**[07:01]** me know what you guys think. If you have any comments or questions, also please let me know down in the comments below. And if you guys have been experimenting with Codex and GPT 5.5, please feel free to share what you're building. Again, I have that Discord community down below and you can join that and share your work. And like always, thanks so much for joining. Hope to see you next time. Goodbye.
