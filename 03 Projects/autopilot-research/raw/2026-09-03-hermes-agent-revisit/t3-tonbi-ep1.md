# Hermes Agent Masterclass 1: Installation, Setup, Basic Commands (Tonbi's AI Garage)


> Source: t3-tonbi-ep1.en-orig.vtt
> Converted: vtt-to-md.py
> Format: `[MM:SS] line` — verbatim auto-sub, deduplicated, word-timing tags stripped


**[00:03]** Welcome everyone to the Hermes Agent Masterclass. I've dug into basically every document, every feature, every community skill and plugin and design this masterclass from start to finish. It's right now designed as 11 episodes, but obviously as Hermes Agent evolves, I'll be adding new episodes, new modules to keep up with the changes and evolution of the agent itself. So, this

**[00:30]** masterclass will have everything you want to know to get the most out of Hermes Agent. And we're starting literally from zero, completely new. This is going to be an introduction to the agent itself and full installation and then a tour of the CLI. So, by the end of this, we will have a Hermes Agent installed and configured and we're have going to have our first task actually completed. So, part one, what is Hermes?

**[00:59]** Hermes Agent is an open-source AI agent built by new research and it's a lab behind the Hermes model family. Most agents are built by tool companies. This one is built by the people who trained the models and that matters. And more on that in a second. It runs in your terminal as a CLI or as a gateway that can answer on your phone via Telegram, Discord, Slack, iMessage, WeChat. They have 16 platforms as of the latest version.

**[01:26]** It's provider agnostic, so you can use Claude, you can use GPT, Grok, Kimi, you can use a local model via Ollama, or anything else. Hermes doesn't care, you can pick exactly what you want. So, why does this exist? New research trains models. They built Hermes originally as a the harm harness that generates training data. So, when you use Hermes, you're using the same tool new research used to build the next generation of their models.

**[01:54]** And that's a credibility signal you don't often get. And this is obviously open-source, MIT licensed as of this recording around 7,000 stars on GitHub, nearly 300 contributors and it's moving fast. We literally just got the the most recent version 0.9.0 today. So, the key bet of Hermes Agent is compounding value. Most agents are stateless. So, every session starts from zero.

**[02:23]** Every ChatGPT session starts blank. Every new Claude conversation starts blank. Open Claude usually the same. Hermes was built differently. Every session feeds the next one. So, there's a four-step loop here. You give it a task. It could be anything. It records a trajectory. And this is the tools used, every decision made, every result. And then it can extract that as a reusable skill based

**[02:49]** on how it worked. So, the next time it's faster, more accurate and cost less tokens. And this is compounding value as a thesis and what makes Hermes really unique. A Hermes installed that you've had for 3 months is fundamentally better than what you set up yesterday. So, you're going to get to see this for yourself. I'm going to be installing this on a new device that has never had a Hermes Agent and through this masterclass, you're going to be able to see exactly how it develops, what skills

**[03:16]** it learns and how it becomes smarter. So, how do you know Hermes Agent is right for you? So, if you use agents enough that compounding benefit pays off, occasional users may not feel it. If you want model freedom, you might want to start on Claude, want to start on Grok, end up using local, Hermes can roll with that pretty easily. And if privacy or cost matters to you, the local model support is really first

**[03:44]** class. So, you may not want Hermes if you just want a chatbot, you could just use ChatGPT, you don't need a full agent. Or if you need max platform integration breadth, right now Open Claude has a bigger out-of-the-box integrations, but that is Hermes is catching up as we speak. So, by the time you see this, that may not even be true. Okay, enough of me yapping. Let's actually install this thing. So, will it run on my machine? If you have a Mac OS, it's native. Linux,

**[04:15]** native. Windows, it only works on WSL 2. And you need this these are the dependencies that it will install. Now, I am on a Windows PC. So, we need this WSL 2 and if you've done any Linux development on a Windows machine, you're familiar with it, but if you're not, I will show you what it means. So, this kind of gives you a a breakdown, but WSL stands for Windows Subsystem for Linux and the default one

**[04:43]** is usually Ubuntu, uh but there's others. I have Debian on this computer, so that's the one you'll see me use, but usually the default will be Ubuntu. It's basically the same thing. And this lets us develop with Linux applications and tools uh directly onto Windows. So, it's pretty nice and it's pretty easy. Uh you need to be running on a Windows 10 version or higher. Um and it's just this one thing, WSL install. You need to be in PowerShell in

**[05:12]** administrator mode and then just that one command and that'll install Ubuntu distribution of Linux uh as the default. And once you have that installed, you're ready. This is PowerShell. Uh so, just do WSL and it will launch your WSL. There we go. Base and Tony B at Corpus, you'll see

**[05:40]** something like this. That's the name of my my PC, but it doesn't matter where you install it, it's going to ignore whatever directory you're in and just install it to the Hermes, which is going to be home slash uh whatever your ID is and then Hermes.hermes. So, the quick install here is this is the uh you see on the top here. This is the new research slash Hermes Agent and this will give you the quick install mode here. And that'll open up the installer here.

**[06:19]** It'll install all the dependencies that you need. You see Python, And the configuration is pretty quick. You'll need to know your sudo password um for the build tools. See, all dependencies have been Okay, and once the installation is done,

**[06:52]** you're going to get a choice between full setup or just a quick setup. You do quick, it's very quick, but for this, we're going to do full setup so you can get to see everything here. So, first you can see the providers and these are your AI providers. New portal is new research's subscription service for AI models. Open router, um you can see Anthropic, which has the Claude models. You can use with an API

**[07:19]** key or through Claude code. Um you have OpenAI, Codex, you have Qwen, uh GitHub Copilot, Hugging Face inference models and there's more providers uh that you can use. For now, we're just going to use Open router uh since I have an API key for this one. Uh no open API key, so let's Here, I'll show you how to do that. So, if you just go to openrouter.com, you're going to have to

**[07:47]** put in a credit card at least, get a couple credits. Let's see. And you just get an API key, you can create it there and then just insert it. It'll be something like this, SK something. So, once you get your API key, just add It saved it. I'll show you how to use other models for now, but for now, we're going to use Open router. Um you can see all the different models that it has. It has Opus 4.6 as currently in use as

**[08:15]** the default, but let's try to do something a little bit cheaper. You can enter a custom model name. For now, let's do this one, the Mimo V2 Pro. So, then it it will offer a fallback and rotation. So, Hermes can keep multiple

**[08:43]** credentials for one provider and rotate between them when one of the credentials is exhausted or rate limited. And this preserves your primary provider while reducing interruptions. So, this is a pretty nice function. So, you just add a a second API key here and then you could have that whenever the first one runs out of credits or you hit some type of uh rate limit. And then we have the the max tool

**[09:08]** calling. So, that will determine how often your agent is allowed to uh call tools. Tool progress, we're just going to set that to all so you can see every single tool call for now, but you can change this to you just turn this off or only show the the new tools when they

**[09:33]** happen. You see here in Telegram, this is my uh existing Hermes Agent. You can see the tools that we have. Like these are all tool calls, listing, searching files, executing code. So, it'll list out all these so you can see them, which I kind of like, so we'll just do all for now, but you can set this for off or set this for only new tools, however you like. So, for this, the higher the threshold

**[10:06]** means the later you take to compress. Let's do 0. Split the difference 0.75. Depends on which model I'm going to be using. Cuz some models can handle longer context windows better and others need compression quickly. Uh session reset mode, inactivity and daily reset. Recommended reset, whichever comes first, inactivity only. Daily only, never auto reset.

**[10:34]** Um let's do inactivity and daily reset. Inactivity timeout. So, this is how long inactivity is. Each message adds to the conversation history, which means growing API costs. So, this is also about context management. If you have very long uh context, if you continue to do work there, you're going to have higher token costs. Higher IP API costs.

**[11:01]** Um yeah, we'll just skip that. Daily reset. Do midnight. Makes sense. Select plat- platforms to configure. So, we're going to do this in the next video when we get into the the um the gateway. We're going to set up a couple of these. So, I'll save those for Uh

**[11:30]** choose provider, local browser. Browser use Firecrawl. Uh we'll configure that later. Keep defaults. Flux 2 Pro. This is for in- image generation. Let me see. This is a paid thing. Okay, so I don't know if I'll use this FAL for image generation or something else, but

**[11:57]** we can add a key for now. You just sign in. There's no You sign in with your GitHub. And it'll create it for API, I guess. API, sure. Hermes agent. Okay, so I just paste that in. Uh wait. Microsoft Edge. Search provider. Firecrawl cloud. Uh Tavily is good as well. AI native search. You can also do this self-hosted, but

**[12:26]** you can do it locally. Uh let's keep the defaults and I can configure that later. Uh so, here we go. That was all the configuration you need to do. Some of the stuff we'll set up later, like the Telegram. That'll be in the next episode, but should we launch Hermes There we go. Hermes agent. I'm sure you all wanted to see that. So, this has all the available tools.

**[12:52]** You can see all the available skills and these come with it. None of these are custom. These just come with the You can see I'm using Mimo V2 Pro through OpenRouter right now. So, there you go. That was the installation and the setup. Now, we're going to go through a couple of the CLI commands that you'll use. So, here are some of the top ones you will use. So, it's important to go through these very quickly.

**[13:18]** Hermes just sharp starts this chat you up uh TUI terminal user interface. If you just do Hermes, you'll do this. Hermes. Hermes gateway starts the messaging gateway, which you'll need to connect to Telegram. Hermes doctor is to check for any issues So, I exited. Um it's just {slash} exit to get out. Cuz let's try a couple of these these

**[13:44]** CLI commands. So, Hermes model uh just shows what you're using. Okay, you have to reload your shell to use the Hermes command. So, let's do that. Excuse me, Hermes model will open up the configurer and you could select which provider to easily switch through them. So, we're going to stay with stay with two. Uh so, we'll just get out of that. So, that's for the model. Um and this shows you everything, the

**[14:17]** whole configuration that you have here. Where your project is. What model you're using, what provider you're using. Your API keys. Um you can see which ones are set and which ones are not set. So, this is very helpful. Hermes status. You could see the auth providers. Now, uh new portal, OpenAI Codex. Quen OAuth. And it shows everything that's configured and most stuff obviously is not configured cuz I just set this up.

**[14:43]** Um Hermes insights. This is probably not going to have much. But, let's see. Hermes insights. Since I just pulled it up. Yeah, no sessions found cuz I didn't I just loaded it. Um so, these are other things. You can see Hermes sessions browse. Uh the cursor pick uh curses picker to resume. So, you can browse which session you want to resume. Hermes skill browse. You can discover

**[15:12]** and install skills. Let's do that. Hermes skills browse. There we go. We got a lot of skills. Uh 50 skills loaded. Have all these different ones. Canvas. You could see DuckDuckGo search. Honcho. They're all official, so there's no no So, you can actually search for them

**[15:39]** specifically. Let's say Hermes skills search. Say you want something about with email. Uh these have all email related and you can see the trust. Some are official. This agent mail is official. Then you have a bunch of community. Some are trusted, which I guess are like this is Anthropic skills, which is obviously uh trusted provider. You can see they have all these skills. Cold emailing. React email, business email.

**[16:07]** So, that's a very useful skill. If you're looking for a specific skill with Hermes, Hermes skill search and then Hermes config show, which is going to show your configuration. Like I said, Hermes doctor and Hermes update, which pulls the latest. Let me see if we're actually updated yet. Hermes update. They may have had an It's updating some of the dependencies.

**[16:36]** Down new commits. Yeah, they just had a a new update actually while I was filming this. There you go. We're updated. Pretty easy. So, these are the top 10 {slash} commands and these are in-chat commands. So, let's go back to the chat and that's just Hermes chat, right? There we go. Back to the the terminal. Still with Mimo V2. So, new. If you've used like Claude

**[17:04]** code, you're familiar with this as well. You could put Think of this terminal interface as like a Claude code type of thing. Or Codex or whatever you're using. Um new starts a new fresh conversation, a new session. {slash} model. You can swap the model mid-session. So, that's a really nice feature. Um I'm going to switch to

**[17:32]** ZAI {slash} GLM 5 1. No, uh that's not the right one. ZAI {slash} GLM 5.1. There we go.

**[17:58]** So, there we go. We switched. Now, we're in GLM 51. And I don't have to restart the session. Um I can just continue. I don't have to re- reboot this configuration. There we go. Hello, I'm Her- Hermes, your CLI AI agent. I'm running on GLM 5.1 model. There we go. Fast, which is a a brand new one that actually came out in today's release, I believe. This is priority routing through OpenAI and

**[18:24]** Anthropic. I don't have those configured, but if you want like something quick going through those is going to be faster. Background prompt. So, you can do a background task and keep chatting. {slash} by the BTW and then you can ask you ask a question. So, that's a side question while Hermes is working. Uh {slash} Q with a prompt, which adds

**[18:51]** like a next term Q. This is also like when Hermes is working, you can do that. You can try some of these a little bit later when I once I give it a task. {slash} compress. So, this manually compacts the context. If you have a long context window and you want to compress everything, you can do that. Skills. You can browse or invoke a skill. Uh {slash} yolo. Toggle dangerous command approvals. Be careful with that. And of course, {slash} help with everything else. And that is probably the most helpful.

**[19:18]** You can see whoop. They have a lot of stuff. So, this has all the {slash} commands you could ever want. All the tools and skills. So, if you ever need some type of skill or some type of command, just the {slash} help will tell you. There are a lot. So, these are all skill commands as well. These are the ones that are installed. So, you can invoke them in this session if you need them. So, this is where stuff lives. And just

**[19:47]** quickly, everything is stored in this uh {slash}.hermes file. Or directory, I should say. Sorry, this is small, but if you go down, if you're in a Windows PC, you go down here to Linux and mine is says Deb- Debian, but yours might say Ubuntu. And you go to home and then whatever your username is. And then you could do this dot Hermes and this is where all the files live. The sole file um this has your history and this

**[20:17]** config.ya- yaml file is the main configuration and this is your settings and you can edit that. You can edit the dot env file cuz that's going to be your secrets. API keys, this one, this env file. API keys, any kind of passwords, stuff like that. It's going to be stored there. Sessions has every past conversation. Skills, you see sessions is over here. We've only had one, so

**[20:51]** It's all of these. These are the ones that come with the Hermes agent basically. Sorry this is small. Let me see. You can see a little bit better here. And you see here logs has your all of your agent logs and the error logs. Memory is here, so it's important at least to be aware of this dot Hermes directory in case you ever need to change anything here. And you can edit uh these top three config.yaml, dot env, and memories.

**[21:20]** You don't want to touch uh the sessions or crone by hand. Ask your agent to do it cuz you could break it. So, your first real task live demo. So, this was this video was teaching you how to install Hermes agent from scratch, how to set it up. We just did a basic setup. There's obviously a lot of settings we're going to be fooling with in the coming videos. Okay, so it's time for our first real task and it's going to be to do some competitor research. I

**[21:46]** have what I think's a really great idea for a business, but I need to my Hermes agent to research the competitors and see if there's any market gaps here. So, in order to do this, the one tool it's going to need is web searchability. So, what we're going to do is Tably. They have a really good free monthly credits. You can also they have DuckDuckGo available for free, but just to show you another option here is uh tably.com and then you just sign up. You don't

**[22:13]** need to put in a credit card or anything and you get 1,000 free credits, which is pretty good. But we'll look in more deep into web But here you get your API key here. Save that. Then back in your WSL you do Hermes config uh Hermes setup actually. Quick setup, configure missing items only. And these are all the items that are

**[23:03]** API key uh space to toggle that. Enter to confirm. And then you put in your API key. Just paste it there. Setup. Not going to do that right now. Okay, so that should be set up. And I checked here, I did Hermes status. You can see there we go. Tably is set up. So, we should be able to use web search now. So, let's get into Hermes then, Hermes chat. Uh using Memo V2 Pro still.

**[23:36]** So, this is my idea. Here we go. I had an idea to start a business that uses AI to make custom children's books. Instead of just the name, it can use AI to create custom illustrations in the style the customer requests as well as story themes, etc. Please do a thorough research into other companies and competitors who may provide this service and report back to me with their names and try to identify any market gaps that exist. So, you can see it's initializing the And it's preparing the web search to

**[24:05]** find got some good leads. You can see these are all the tool calls it's it has. I think this is a good business idea. It's a real one I had. Hopefully we can find some kind of Uh okay, and here we go. We got it our report back pretty quick as you just saw. Um here's a thorough breakdown of the

**[24:32]** competitive landscape. Competitive landscape market falls into three tier- tiers. Uh the traditional personalized book companies, which were pre-AI. So, let me see the AI-powered ones. Here we go. Direct competitors. These are the companies doing what you described using AI for both story and illustration generation. Uh now there's a lot. This might be a saturated market. Might not be workable.

**[25:03]** There's a lot doing this. And this first one, one of the earliest AI children books platform, template-based stories, AI illustrations. Mm. Okay, tier three general AI tools, indirect. Yeah, these are just visual ones. You can see here just that quick search it had found a lot of competitors. Market gaps and opportunities. There are some. Uh based on competitive analysis, here are the underserved areas. Custom art style selection.

**[25:29]** So, most competitors let you customize the character but lock you into one illustration style. Few let the customer choose or define the actual art style. Uh the user said in the style the customer requests, this is the real gap. That could be something, right? Older age groups. Almost everyone targets ages two to seven. Uh I really wanted children's like baby books. Those are the ones everyone's buying as like gifts.

**[25:56]** Bilingual. It found a lot of uh gaps here. But I don't know if any of these are workable for me. Audio first culturally specific author creator tools, that's more on the B2B side. Um so, here we go. Wonderbly. I See Me. So, there's actually a lot uh So, it

**[26:23]** gave it my my big take. The biggest white space is custom art style control combined with therapeutic niche story themes and older age groups. So, there we go. There's your kind of market report, competitor report. Just for this first video, we did something simple, but I think this is a a task that a lot of people have, right? We all have random business ideas. Maybe it's just me. And you can use your Hermes agent to uh

**[26:50]** check on them, check on the competition. See what kind of market gaps exist and try to plan when you want to start a business. And there you have it. That's going to be the end of this first video. Uh right now you should have Hermes installed and a provider configured. You know the top 10 CLI commands and top 10 slash commands. Got our real first artifact, com- the competitor report and the memory file that just started learning you. So, this has already started learning

**[27:18]** me just with this first task. You can see. So, we just started this blank right here and throughout this masterclass series, you're going to be seeing how this Hermes agent that just started brand new, how it develops over time as we continue to use it and work on it with different tasks and actually try to start some businesses. I'm not sure about this AI children's book one, but maybe other ones that has left less competition. That's going to be it for session one. I

**[27:46]** hope you enjoyed it. Next session we're going to talk about different deployment options and messaging. We're going to hook it up to Telegram. Maybe to some other apps so that you can see your options with that. And you don't have to just chat with it in the um Uh but thank you for watching. All of these videos will be available on my school community once it launches, which should be in June. But I'll be I'll be um presenting some of these on YouTube as well. So, you may

**[28:13]** be watching it there. If you So, if you want to watch the full series from day one in the school community, it'll be available all of the episodes. But I'll be posting some on YouTube. So, if you're interested in this content, please subscribe, please leave a like, leave a comment. Let me know if you have any questions about setting up Hermes like this.
