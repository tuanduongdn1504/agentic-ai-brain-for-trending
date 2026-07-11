---
source: yt-dlp-only (path 5; operator-submitted single video; EN manual captions en-US -> dedupe -> full transcript below, read IN FULL in the main loop; NO NotebookLM)
topic: local-ai-coding-agents
generated: 2026-07-11T17:45:00+07:00
video_id: Zof2Oaj14rk
video_title: "Local AI Coding Agents Are Finally Good Enough"
channel: Code with Beto (Beto Moedano) — @codewithbeto
uploaded: 2026-07-09
duration: "16:55"
views_at_ingest: 6642
likes_at_ingest: 165
language: en
first_party_originals_double_dived: Qwen3.6-27B (Alibaba Qwen) + Apple MLX/MLX-LM + LM Studio + opencode (SST) + Locally AI/Apple Foundation Models
notebook_id: none
---

# Code with Beto — "Local AI Coding Agents Are Finally Good Enough" (full transcript)

> Ingested 2026-07-11. Central thesis: the 2026-04-22 release of **Qwen3.6-27B** (dense, Apache-2.0, multimodal, agentic-coding) run via **Apple MLX** inside **LM Studio** (OpenAI-compatible local server) and driven by the **opencode** terminal agent makes LOCAL, offline, zero-subscription AI coding "finally good enough" for real app work on a high-RAM Apple Silicon Mac. Presenter runs an M3 Ultra Mac Studio (96GB). Timestamps are ~30s anchors.

## Transcript

**[00:00]** if you've ever tried to run a local LLM on your computer you know that it's pretty trash it's a bad experience it doesn't really work but that actually just changed thanks to the latest release of Qwen 3.6 which is a 27 billion parameter model optimized for agentic coding improved multimodality capabilities and it uses lower VRAM which means you can run it on your computer decently and let me tell you right now it finally works it can code it can do agentic stuff it

**[00:30]** can recognize images it can create files read your code base contribute and it works offline and entirely on your computer on top of that with the new release of MLX which is the Apple framework to run LLMs locally on your computer running this model it's now more reliable than ever so in today's video i want to show you how you can download it and run it on your computer i'm going to show you some pretty cool examples let's get into it so Qwen3.6 was announced on April 21

**[01:00]** so it's pretty new and i just want to show you the benchmarks because this model is surprisingly very decent it's not going to replace the latest Opus model but definitely it's something cool to have it running on your computer being able to use it while you are on a flight when you don't have internet when you reach your limits you can actually get stuff done with this model now delivers agentic coding performance surpassing previous generations open source flagship Qwen

**[01:30]** 3.5 and of course it's fully open sourced let's take a look at the benchmarks here for agentic terminal you can compare this one to basically Opus 4.5 so it's not going to be the latest Opus but if you remember Claude 4.5 was pretty decent and this model it's basically the same for agentic coding it's literally the same value it's going to perform a bit worse than 4.5 but definitely it's amazing that you can

**[02:00]** run it on your own computer now by the way one thing to mention is that if you're not running this on a Mac you're going to need at least an RTX 4090 according to the specs you at least need 16 gigabytes of memory but i think that's going to be super tight so i would recommend at least 24 now that said what i like to do when i'm running local LLMs is that i like to go to the CanIRunAI website but this model is actually so new

**[02:30]** that they don't have it here the last one they have is 35 but if at the time that you're watching this video maybe it's on the list this website basically tells you the specs of your computer so right now i'm using an Apple M3 Ultra which is you know the best of the best at the moment with 96 gigabytes of VRAM and 80 cores so pretty decent machine that means that i can run this model decently fine but actually i tried to run it on my laptop it's a MacBook

**[03:01]** Pro with 18 gigabytes of VRAM and i wasn't able to run it unfortunately so that's the catch you have to have at least a decent machine but if you have the RAM you can absolutely run it so the way you can download it is by using LM Studio LM Studio is my favorite desktop application because it's super easy to use and it allows you to download any model so just go to LM Studio once you download LM Studio you're going to see something like this so make sure to

**[03:31]** enable developer mode otherwise you won't be able to see this tab if you didn't do that you can always go to the settings and enable developer mode here all right next thing that you want to do is just go to the model search tab and it's actually the first one right here this is the one that you want to download if you don't see it here just search for it and then download it it's going to be like 20 gigabytes and after that you will be able to go to the chat inside LM Studio and then just select the model and you can

**[04:02]** load it or eject it now the cool thing about Qwen3.6 is that it's actually a reasoning model that also supports vision and tool calling so you can ask things like let me start a new chat how's the weather today i don't think it knows my location but let's see you can see that it's actually thinking specifically for Bentonville, Arkansas and then hopefully it's going to use a tool to check the weather by the way you can always see the logs of

**[04:33]** this in real time in the developer tab here so you can see the tokens that we are generating the logs you can increase the context window that's why i really like LM Studio it's really good experience and on top of that they have this max concurrencies so you can set this to four for example like me that means that you can have four sessions at the same time you can even enable cache quantization this means that the output is going to be faster but you can hurt performance in the

**[05:03]** quality so that's why i haven't turned this on but if you need faster responses you can always turn this on so that's how you easily can start running and loading the model but most importantly i like to use it for coding tasks and if you want to do that you can just make sure that you have running the model and then turn this on which basically is going to enable this endpoint to make it reachable at this endpoint okay now this is actually compatible with OpenAI API and that means if you

**[05:33]** click here you can see that we have the endpoints that opencode is going to expect to connect to any local computer so if you have opencode already installed on your computer just go to your configuration but you can use the image recognition you need to pass the modalities here so this is important once you added this to your JSON you can go back to your terminal and open opencode and it's going to start working just great so here i have actually a couple of examples that i've been working on that i want to show you

**[06:03]** but just let's create a real example right now i'm going to go to my new tab i'm actually inside my AI Tattoo application project and let me actually bring the application here i actually asked the agent to create a new tab and it did work once you added the configuration the model is running locally you can just go to the models and connect directly you should be able to find it in the local models so right now i have it here already it's running locally from LM Studio

**[06:33]** i also have Gemma but Gemma it's pretty bad for real tasks so Qwen 3.6 27 billion is honestly mind blowing let's try to ask for something interesting like for example let's say that i want to know the SF Symbols names of these icons here so i can take a screenshot paste it in here and then tell me the name of the SF Symbols of these icons alright we can send that in you can again always

**[07:03]** go back to LM Studio and monitor how everything is coming here in the logs you can see that we are generating tokens handling the responses and it's building and at the same time i can go back to another chat that i was working on for example this is a chat where i asked the agent to create the new dev tab and display simple text right so now we can actually ask more complex things let me make this big okay so it's now telling me the SF Symbols used in the

**[07:34]** tab right that's pretty cool so let's go back to another chat this is the same conversation i just asked for a new screen and it actually recognized my code base i couldn't do this with any other local model this is amazing so in here maybe i can ask to display a card with the user info for devs only so include ID and useful information hit enter boom and then we can toggle between other conversations and

**[08:04]** what's cool about these guys is that of course this is going to work offline and it's running on my machine i'm recording my screen at the same time of course my machine has 96 gigabytes but it's working nicely and on top of that i actually went ahead and asked for a Minesweeper game and it created an HTML then i also asked for a snake game right so let me actually show you those games this is the Minesweeper you can see that the design is pretty good it did this

**[08:35]** all by itself and it works nicely and i asked for this game snake game and i can play it so how cool is that let's try to ask to change the emoji for example right it's an apple let's go back and this is the snake game chat change the emoji to be random between apple orange and other fruits and remember that it's actually working here

**[09:05]** so we have now two concurrencies in my machine i asked the SF Symbols question here this is this it worked really nicely this seems correct so i'm going to close this conversation just to keep things simple it recognizes images which is really nice we have two concurrent connections this is the snake game i also asked the agent to create a three page document explaining how LLMs work and it did it it created a Markdown file so i'm

**[09:35]** surprised about it now some things that i've realized is that you're going to notice that it's thinking for a while you don't get like the feedback that you get for example in LM Studio when you are chatting with it but in here you will get directly the response sometimes so after a while it will give you the response by the way you can also see the current concurrencies here so we have the gen one and gen two and it's generating tokens in both so that's pretty cool as well okay it's

**[10:05]** editing right now the snake game here we can see the fruits that it's going to use so i'm actually super surprised with these guys because this is actually useful and you can actually use this for fun things i'm not saying it's going to replace you know Opus 4.8 which is the latest model but definitely i can feel that it's very similar to the experience that i used to get with Opus 4.5 there we go okay it's done let's see let's refresh and now we get an orange i mean can you believe these guys

**[10:35]** and then from here you can keep iterating like each fruit will give you different points maybe we can add something that will kill you if you eat it game over i mean i don't know i don't know what to tell you i'm super excited about this now on the display card this is actually taking a while and actually my code base it's pretty big this is a real application this is my AI Tattoo app and i've noticed that you know local models are pretty decent at writing HTML as we saw right now but as soon as you put them into something

**[11:05]** more complex like a mobile application they start tripping they start importing things that don't make sense and it's not usable but Qwen3.6 27 billion it's in another level and the efficiency that it's running on my machine i mean other models that i tried in the same machine took longer to run and i think that has to do with the MLX support the new framework from Apple to run LLMs locally so definitely very excited about

**[11:35]** this and i think it's now actually worth investing in a good machine that can allow you to run this kind of models locally because you can integrate them to opencode expose them through an api and actually LM Studio has a pretty cool feature that allows you to connect to this model through the application so i actually have here my LM Link which is an app that you can download on your phone so let me actually show you right now oh and i can hear the vent of my machine i've never

**[12:05]** heard that from my Mac the vents are on definitely this task is a complex one because my Mac Studio is hot i can tell you that i'm still recording the screen and running a bunch of things but if you take a quick look it's actually running sub-agents so definitely this is a complex task and if it can do it i'm gonna be extra surprised look at this guys it did 31 tool calls and basically grabbed the information of my entire code base it knows that i'm using Better Auth the config

**[12:35]** between server client and all the useful information that is going to display so look at all these data boom and there we have it i mean it didn't put it on a scroll view but i can see it this is for developers only so i'm happy with the style it's giving me the name of the current authenticated user email it's verified when it was created the tier premium no entitlements none how cool is that let's actually see if i can subscribe to the

**[13:05]** weekly just for fun and see if it actually changes all right so i subscribed go to the dev yep tier premium yes it took almost 10 minutes to do that my machine was on fire the fans were loud but it's better now the temperature is lower i'm honestly super surprised because you could be able to do this on a laptop for example as long as you have good RAM i'm using a Mac Studio but super surprised by the results you can ask follow-up questions and it will

**[13:36]** just work so definitely i think this is useful i didn't pay for anything i cannot believe it to be honest last feature that i want to mention from LM Studio there's an app called Locally AI which is from LM Studio if you open it you can actually connect using the LM Link feature and it's awesome because it allows you to chat from your phone with your agents so in here i can use Apple Foundation or just select Qwen3.6 billion from my phone

**[14:06]** and i can start chatting like let's just select one of these prompts for now and this is going to be connected through my computer it's actually loading the model let's see there we have it it's working so right now i'm connected through my phone to the model locally my computer can actually be sleeping and i can be on my bed chatting with my model locally many other things you can run this as a cron job you can actually search the internet using the tool calling there we have it let's

**[14:36]** see if we can search the internet it's not searching not sure why but i'm going to ask what do you see in this picture and let's submit this is a beautiful scene image capturing a dramatic sunset by the way that was my view yesterday when i went for a walk so that's very cool okay so i think this is a good point to wrap up this video i'm extremely surprised for the possibilities because from here of course it's gonna get better and better and Apple is set to

**[15:07]** announce new Macs soon i think at least this year so they are optimizing for running LLMs locally and as more companies keep open sourcing models like this one i think this is going to get more useful and more useful and definitely it's good to know what's new out there what you can actually do with these local models right now and what are the specs that you currently need but of course i hope in the future getting a machine will get maybe cheaper with better memory and then you're going to be able to run models locally Apple

**[15:38]** already ships with Apple Intelligence and you can ask their model to do things but i think this one specifically for agentic coding i mean you saw that we were able to add a new screen and you know fetch scan the code base get data displayed on screen this is honestly the first time that i'm doing this my computer got hot but it did the job so i'm super surprised you can also pass images it supports tool calling you can pass skills even though it's not going to be like the best experience like you have with Opus 4.8

**[16:10]** but definitely i'm going to be using these more and more i've been using this for a couple days and sometimes i'm like okay i have a question of how do you write this right i'm always improving my english how can i write this and i'll just go ahead and ask my local agent for that and then i'm also thinking i should go ahead and cancel my ChatGPT subscription because i have both so i can maybe just keep the Claude subscription for work and more complex agentic tasks and for the simple things like refactoring copying things around maybe i can just use the local model that's pretty cool that's it for this video if you want to

**[16:40]** keep learning more about mobile development with agentic tools like Claude or now your local agents check out my book from idea to app store the link is in the description don't forget to like and subscribe thanks for watching and i'll see you in the next one
