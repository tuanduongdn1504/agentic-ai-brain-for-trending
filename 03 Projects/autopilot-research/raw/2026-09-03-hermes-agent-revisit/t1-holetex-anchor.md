# Hermes Agent: Cài Trợ Lý AI Cá Nhân Từ Số 0 (holetex, EN auto-translation)


> Source: t1-holetex-anchor.en.vtt
> Converted: vtt-to-md.py
> Format: `[MM:SS] line` — verbatim auto-sub, deduplicated, word-timing tags stripped


**[00:00]** Imagine you’re a programmer with a personal assistant that summarizes the top tech news, automatically reads your work emails, and sorts your tasks every morning at nine. Or maybe you’re a salesperson, and it summarizes your orders and customer messages every evening. Or you’re an investor, and this assistant helps you... automatically monitor prices and proactively send you notifications about technical analysis. The special thing about this assistant is

**[00:25]** that it can work around the clock, even while you sleep. You can easily interact with it entirely through your phone, using messages or voice. And the more you use it, the smarter and more effective it becomes through its automatic learning mechanism. This assistant is called Hermes Agent. In today’s video, I’ll guide you through everything from scratch. We’ll start by looking at what Hermes Agent is, how its architecture works, and how to install it.

**[00:55]** Now, let’s get started. Back at Hotech—I’m Tùng! For those watching for the first time, I make videos about programming and technology. This is the GitHub page for Hermes Agent. As you can see, it’s described as an AI Agent that can learn by itself and continuously improve, built by Nous Research. It’s also the only Agent with a feature called the Learning Loop, or the learning loop.

**[01:24]** We’ll look at exactly how the Learning Loop works later, in the section where we explore Hermes Agent’s architecture. Basically, it automatically creates skills from its experience working with us. And besides the Learning Loop, it also has another very useful feature: it can understand many separate conversations over time while sharing one common memory. This is different from how we usually work with Claude Code, where each session or project has its own memory system, so we

**[01:52]** can’t know what we discussed in another session. But with Hermes Agent, there’s a system that can remember all of our conversations and sessions. It only launched this year, in 2026, but as you can see, Hermes Agent has already passed two hundred thousand stars on GitHub. And it’s available under the MIT License. So we can use it completely free of

**[02:21]** charge. We only pay for the LLM services, meaning we only pay for the tokens we use. The Agent itself is completely free. There are several ways to use Hermes Agent. We can run it on a personal laptop, on a PC, or on a VPS. But keep in mind that if we want an assistant that works twenty-four seven, even while we sleep, we should usually host it on a VPS. If we install it on our personal computer,

**[02:48]** the computer may go to sleep, and then any automatically running tasks may stop working. So in today’s video, I’ll show you how to install Hermes Agent on a VPS, giving us an assistant that can work for us twenty-four seven, even while we sleep. Simply put, a VPS is like having a computer running twenty-four seven in the cloud on a cloud system.

**[03:16]** To talk with Hermes Agent, we can easily use apps such as Telegram, Slack, Discord, and more. Next, let’s look at how Hermes Agent works. Here, we have a VPS, essentially a computer running in the cloud and operating twenty-four seven. Once we install Hermes Agent on this VPS, I’ll show you later in the video how to set it up there.

**[03:44]** Once it’s installed on a VPS, we can easily interact and talk with Hermes Agent through apps such as Telegram, WhatsApp, Discord, Slack, and more. We can use these apps on our phones or an iPad, and that’s all we need to start talking with Hermes Agent. Now I’ll walk you through the entire

**[04:11]** process, from sending a message in Telegram to seeing how Hermes Agent handles it. In our app, when we send a message through Telegram, Hermes Agent on the VPS has something called a gateway. It’s like a door that receives the message. Once it receives that message, it passes it to a component called the Agent Loop. The Agent Loop reads and records the

**[04:39]** memories, and it also manages a collection of tools so it can use them. It also has another important job: acting as the main point of contact with the LLMs, or with model providers such as OpenAI and Anthropic. These are the companies providing the AI models. All the parts like the gateway, Agent Loop, memory, and tools belong to Hermes Agent.

**[05:12]** The external LLM providers are where we actually use the AI models. So when the Agent Loop receives a request from the user through apps like these, it sends a request to the LLMs, to the external providers outside. When the model replies, if the LLM’s response says that a tool is also needed, the Agent Loop knows to call the appropriate tools—for example, to browse the web, open a terminal, or use tools for generating

**[05:40]** images. And this is what we call the Harness—the part that wraps around a model, which I introduced in an earlier video. If you'd like, you can go back and watch my video about Harness. Once it finishes running the tools, it remembers the relevant memories, and then sends its response. This is our Telegram message. So, this is the complete lifecycle of a

**[06:05]** message when we work with Hermes Agent. Now we'll go into more detail to see how it stores memory, and how it creates and updates skills. So now we'll describe how its self-learning loop works. Suppose it's working and notices that a certain task keeps recurring. At that point, it automatically recognizes the pattern and writes the necessary skills itself, so we don't have to create

**[06:33]** them manually. Of course, you can still create skills manually if you want. But because Hermes Agent comes with the ability to learn on its own, create skills, and update existing skills, it becomes smarter over time and works more efficiently. It's just like an employee: when someone is new to a job, they will naturally take longer than someone with five or ten years of experience. This agent

**[07:00]** now has that same ability to learn. Whenever it encounters a similar task again, it can use the skills it remembered from before. So it only needs to retrieve that skill and apply it in the same way. As a result, both its working time and the quality of its work improve compared with the first attempt. That's the self-learning loop in Hermes Agent. For example, the first time it creates a skill, but the second time, the time it takes to complete the task drops, and the

**[07:26]** number of tokens it consumes also drops significantly. This is one of the biggest strengths of Hermes Agent: its self-learning loop, also called its learning loop. If you're not yet clear on what this skill is, you can watch my video about agent skills. Through this learning loop, as it creates skills like these, it builds up a collection of skills. If you've watched my video about agent skills, you also know that a simple skill is just a Markdown file, or simply a piece of

**[07:57]** basic text. It has a section enclosed by three dashes, like this, and that section is called frontmatter. The reason this works better than using rules is that, by default, a rules file will usually be loaded in its entirety into the context window, regardless of its length, and it occupies a certain number of tokens there. Skills work differently.

**[08:25]** Even if we have a large collection of skills, we can think of each one as a work skill—for example, the skill used to export a PDF file, or the skill used to convert a piece of text into a speakable file, or text to speech, or to convert an audio file into text. Each of these is called a skill. It's just like us: we can have many skills, such as working with Excel, giving presentations, and so on.

**[08:52]** So now agents are equipped with skills as well. With Hermes Agent, there may be many skills, and it can automatically create many more, but it still works efficiently because, although there are lots of skills, the amount of text it places into the context window is actually very small. That's because it only sends in this frontmatter section, the part between these two sets of dashes.

**[09:20]** The specific content of the skill isn't placed into the context window when we first start a new session. So the number of tokens it occupies there is extremely small. Think of the left side here as a table of contents. The agent only reads these headings and their descriptions, then checks whether they match the user's request. If it finds a match, only then does it

**[09:45]** read the entire skill and load it into the context window. So even with many skills, these agents can still work very efficiently. Now let's look at the memory structure of Hermes Agent. During its operation, Hermes Agent as we chat with it, through messages, images, or files that we provide, automatically creates files for us, such as the user file, the memory file, and the file called sound.

**[10:16]** These contain information it has compiled and keeps very briefly: who we are and who uses the agent. In my own experience, it only takes up around 10 kilobytes. Every conversation is placed into that conversation's context window when we first start it. User contains user information, while memory contains some summarized details that it has automatically compiled using

**[10:46]** the LLM. Sound describes the user's personality. These three files are always loaded into every new conversation. That's the first layer. The second layer is where it stores all the conversations we have with Hermes Agent. It uses SQLite at this layer. Since the amount of data can become very large, it doesn't automatically put everything into the context window when we

**[11:11]** open a new session. Instead, it only looks things up when needed. Finally, the last layer can be expanded through additional For third-party memory, we have a range of tools such as memzero, Hisight, and Overviking. There are many external memory providers like these, and we can configure Hermes Agent to use them. In terms of memory, there are three layers. First—

**[11:42]** And that is the overall architecture I wanted to share with you. Now, we will move on to configuring and installing Hermes Agent on a VPS. The VPS service I will use today is Hostinger. Since I have a partnership with Hostinger, please visit the link in the video description to receive a 10% discount when you purchase a VPS from Hostinger. When you visit the link in the description, this website will open. We will go to the section where we can

**[12:10]** choose a plan. For our needs with Hermes Agent, the KVM2 plan here will be very It comes with 8 GB of RAM. Or if you want more... If you want a more powerful VPS, you can choose one of the options here. However, I will select the KVM2 plan. Here, we can choose to purchase the VPS for one month, 12 months, or 24 months. Please note that my discount code, Holtech

**[12:39]** Agent, can only be applied to plans lasting 12 months or longer. In other words, you can use it for either 12 or 24 months. For the one-month option, my discount code does not apply. Please keep that in mind. For example, I will select 12 months here. And I will enter the discount code here: Holtech Agents, with an S at the end. Then I will apply it.

**[13:06]** You will receive a 10% discount when using the Holtech Agent code. Next, we will move down to the section where we can choose the server that will host our VPS. Here, the nearest option for me will be Malaysia. Malaysia has the lowest latency here, at 43 milliseconds. You should choose the server closest to you, with the lowest latency available. I will select Malaysia. Since our goal is to configure Hermes Agent, you can first go to the Applications section

**[13:38]** here and choose from the available apps. In this case, I want to install Hermes Agent, and Hostinger already provides templates that make it easy to configure Hermes Agent. So, you can go to the Applications section and select it here. I will choose Hermes Agent and click the confirmation button here. Then after selecting Hermes Agent, we will see a few options. One option is to sign up for the AI router from Nexus. However, I will show you how to use the

**[14:04]** subscription included with the Plus or Pro plans you have already purchased so that you can use it with Hermes Agent. This means you will not need to spend extra money buying more tokens, and I will show you how to do that shortly. When you click Continue here, you will be taken to the page where you can sign in and complete the payment. Once the purchase is complete, click Start

**[14:29]** here. This is the page where we will configure Hermes Agent. This is the default username, so enter your own personal information here. You should not leave the default details as they are. Since this is only a demo, I will temporarily leave the name as Hermes Agent and use the default password shown here. Change your passwords. I will not use keys from Nexus or OCLabs.

**[14:57]** Instead, I will use my own ChatGPT Plus subscription. Now, I will click Deploy. We will wait for a moment while our VPS is installed and Hermes Agent is set up and made available for us. Then After a short wait, Hostinger has automatically installed Hermes Agent for us. Make sure you can see two services, two projects running: one called JFix, and

**[15:22]** the other called Hermes Agent, both showing a running status like this. That means the installation was successful. Each one must have its own container. Here, you will also see an option to open a terminal. The terminal is a workspace where you enter commands. Click the Terminal section here, and it will open in a new tab, where you can type commands. This is the simplest way to open the

**[15:47]** terminal. However, for a more proper setup, after registering a VPS, you will receive an IP address. Use the SSH command with your username and the VPS IP address so that we can connect and configure it using the username and the VPS IP address, connecting and configuring it with private and public keys. This makes the connection to the VPS more secure. In fact, I previously made a video

**[16:13]** explaining this part in my lesson on how to deploy a You can refer back to that video for the full process. So, for convenience, we can use the feature that opens a terminal directly on this VPS. Once you open it, you'll see an interface like this. This is the computer running on a cloud computing platform. Now, to install it, open this website so we can access the instruction file. I'll scroll down to this section.

**[16:43]** To begin the installation, we'll run the command “Hermes setup.” I'll select this part first, then return to the terminal window so we can enter the command there. Enter Hermes setup here. Here, we have a few options to choose from. First, there's quick setup, which uses a Node Portal with a free OAuth login and no API key.

**[17:08]** But as I mentioned, we'll be using our existing subscription plan for this setup rather than relying on a separate login or API key. So I'll choose the full setup option here. Then we'll select Space. Use the Space key and then Enter to make a selection. At this step, we can choose from several providers, as I explained in the architecture of a Hermes Agent. This is where we choose an LLM

**[17:35]** provider—the company providing the models we want to use. Models from Anthropic are known for very high quality, as are OpenAI's models. And as you can see, there are many providers listed here, practically all of the most popular providers in the world today. There are ROP, Anthropic, OpenAI, and so on. There are many models here, but now I'll choose I'll choose ChatGPT and Codex

**[18:03]** subscription. And this is also one of the advantages of using a ChatGPT subscription: it can be much more beneficial. That's because using Hermes Agent now consumes only from the subscription plans, so we don't have to pay separately for the API. On the other hand, if we use Anthropic here, we'd have to use the APIs. And as we know, Anthropic's models are

**[18:29]** extremely expensive and cost a lot. So I'll choose OpenAI here for this setup. I'll press Space, and here we'll have two choices: either use the ChatGPT and Codex subscription directly, or use the OpenAI API. So of course, we'll use the subscription. I'll select it now. The next thing I need to do is simply open the—uh, the instructions tell me to open this website, so I'll open it and

**[19:00]** enter this code. Right-click and copy it. Don't press Ctrl C to copy it. In the terminal window, Ctrl C means that the command will be canceled. Just remember that, use your mouse to select the code, right-click, and choose Copy instead of pressing Ctrl C, or it will exit now. And we'll open this website. Here, I'll log in to my account. Once I'm logged in, I'll click Continue. And now I'll paste the eight digits shown

**[19:30]** here—the “enter this code” section—to log in. I'll right-click, paste it, and click Continue. That's it, I've successfully logged in to Codex, and it immediately opens the interface where I can choose a model. So, there are many models here. At the time I'm recording this video, the 5.6 Son model is the most powerful, right? I'll choose a cheaper model instead, GPT

**[19:57]** 5.6 Luna. The more powerful the model you choose, the faster it will use up your tokens. So choose whichever model fits your needs here. To get started, as you get familiar with it, you'll certainly use it a lot while configuring everything at the beginning. So we'll choose a reasonably priced model here, since I mainly use Claude. But Claude, when used through Hermes with

**[20:26]** OAuth login, makes me purchase an additional package—basically, it requires using the API. It charges a very expensive API usage rate, so I bought a ChatGPT Plus plan too. So, to get started, I think I'll just choose 5.6 Luna. I'll press Space and select Luna, 5.6 Luna. Next, it asks me to choose a terminal backend. It selects Keep current by default, so

**[20:52]** I'll leave that as is and press Space. Then it asks me to choose one... the platform to configure. As I mentioned, we’ll be using Telegram as our messaging platform, right? So I can select Telegram here, and then press Space. If you want, you can select multiple services here, such as iMessage, Microsoft Teams, or WhatsApp, and so on. There are plenty of options, but here I'll choose Telegram. I can select several options at once, and

**[21:20]** then I'll press Enter. Here it asks whether I want to create a Telegram bot. Since I want to use Telegram to communicate with this Hermes Agent, I need to create a Telegram bot. So here I'll choose the option to create a Telegram bot automatically. I'll select option number one. and I'll just press Enter.

**[21:49]** Now it will show me a QR code. You can use your own phone, open the camera, and scan this QR code. That will open the Telegram interface for creating a new bot. Or you can click the link here. When I open the link, it automatically launches the desktop app and opens the interface for creating a new bot. I'll leave the default name as Hermes Agent. If you want, you can customize it and choose a different name. I'll keep Hermes Agent and click Create.

**[22:18]** Once I click Create, our bot is created It happens very quickly. Remember to press Start here to activate the bot. After activating it and sending the Start command, we'll return to Hostinger. As you can see, it has automatically detected the Telegram user. We need to send a message so the bot can identify the ID of our logged-in account and automatically send it over to the Hermes Agent.

**[22:48]** Here it asks whether this Telegram account is allowed to use the bot. By default, it selects Yes, shown as the letter Y. If you want to be explicit, type Y again to confirm Yes and allow access. For example, if you have multiple accounts and want to add them so they can use the bot to communicate with the Hermes Agent, you can add them here, separated by commas between the user IDs. But I'm only using one account, so I won't

**[23:13]** select anything else. It's asking whether I want to use my user ID as a home channel. The default is Yes, and it already has Yes selected, so I can just press Enter. That means I've successfully configured the platform for messaging. You can follow the same process for other messaging platforms such as WhatsApp or Discord. Just follow the instructions.

**[23:41]** Now it's asking whether I want to restart the gateway to apply these changes, so I'll keep the default Yes and press Enter. Basically, we've connected our personal Telegram account to this Hermes Agent. In a moment we'll try sending messages and communicating with it. Next are the tools. You can look back at the section where I described the Hermes Agent architecture and its tools.

**[24:07]** The Agent Loop has a collection of tools it can use, and here we have a whole list of them, with many enabled by default. This Hermes Agent automatically selects tools for us, such as Code Execution, which we'll leave at its default, and Image Generate, among many others. These tools expand the Agent's capabilities, giving it more ways to handle different tasks.

**[24:32]** Among those tasks, one is particularly important for running automation automatically on a schedule: the tool is Cron Jobs. Be sure to check Cron Jobs here. So now I'll basically just press Enter to install these tools for our Hermes Agent. Next, I'll choose the browser.

**[24:58]** It recommends using the local browser here, so I think we should go with the local browser recommended by Hermes rather than changing that recommendation for this setup. I'll press Space. Then we'll wait a moment while it installs all our tools. Next is the image creation section. Here, for image generation, because we’re using an OpenAI subscription, we’ll choose the option here to use Codex OAuth,

**[25:28]** specifically gpt-image-2 through ChatGPT and Codex OAuth. That way, it’s completely free, since it’s covered by the subscription we already have. If you use other models, you’ll have to pay their API fees separately. So a ChatGPT subscription is extremely convenient. All the money we paid for the bundle has already been spent upfront, and we only use the tokens included in the plan we

**[25:53]** purchased, rather than paying separately for every API request. That makes it very convenient. Also, as you may know, ChatGPT recently removed the five-hour limit. So with the Plus plan, we can use it quite comfortably, because ChatGPT now only has a weekly limit. That means we can use it quite comfortably. Another thing is that I’m using the Luna model, and its pricing was updated recently, so it’s extremely inexpensive.

**[26:21]** You can use it almost without restriction to generate images or chat with the Hermes Agent. This is especially convenient for this workflow, because you can keep using it freely within the subscription. So I’ll choose ChatGPT OAuth here for this setup. Next, I’ll... Next, choose the model for image generation. It depends on how you plan to use it: for the highest quality, choose gpt-image-2 with airforce set to two. It’s slower, but the quality is best.

**[26:49]** So here, I’ll go with the Medium plan. Next, I’ll choose the text-to-speech provider to convert the text into a voice track for the voice output in our application. Here, we have several options. If we use the available Microsoft S TTS, which is recommended, it’s free. And if something is free, go ahead and use it, because I’ve already tested Microsoft S TTS and it works very well. Recently, I also made an extension that can automatically provide voice-over when watching English content on Coursera,

**[27:19]** Netflix, or YouTube. I also use these Microsoft S TTS models myself, and they read extremely well and accurately. So, for this kind of tutorial, I’ll use Microsoft S here too, since the pronunciation is both natural and accurate. And next, I’ll... It asks which search provider I want to use. I’ll just choose a free one, since I’m not using a subscription. So here, I think I’ll use DuckDuckGo.

**[27:48]** As you can see, it’s free, requires no key, and is search-only. I’ll use this service. That means the basic installation is now complete and successful. Now I’ll open the chat window—uh, the Telegram window—so we can try talking, without needing any additional setup. with this Hermes Agent to see whether it’s working yet. If you want to change any of the providers later, you simply run the Hermes Setup command again.

**[28:15]** Or, once our Telegram is already connected to Hermes Agent through the bot and we can communicate with it, then we can use that connection to manage the setup. we can simply use the Telegram window to chat with this Hermes Agent, and have it automatically change these providers for us as well. Now I’ll open my Hermes Agent bot. I’ll try talking to it right now and say, “Are you running yet?” No response. So I’ll... Let me check again.

**[28:42]** I’ll open Hermes Agent once more. I’ll open—not the Terminal, but this section here. Notice that you need to sign in with the account you created when we bought the VPS earlier. That section contains a username and password, which you can use to log in and access Hermes Agent successfully. There, once you enter that information, you can log in, and you’ll see an interface like this. Here, Active Sessions is still showing zero, which means it hasn’t been configured yet.

**[29:11]** So let’s check the Channel section again. Ah, there you go. As you can see, our Telegram has been configured, but it says we need to restart to apply the configuration changes. Alright, now I’ll simply click Restart for this Gateway. Here, I’ll restart the Gateway. The Gateway is one part of the Hermes Agent architecture that I explained at the beginning of the video, right? You can go back and review all those

**[29:36]** components. It says Telegram is connecting now. As you can see, it has now switched to the connected state, so I think it should be working now. I’ll reopen Telegram and ask it again. Are you up and running yet? There, it’s typing now. Great, that worked. It says, “Codex GPT 5.6 Luna, the context is 900,000, and it will automatically compact the tokens when usage exceeds

**[30:06]** 85%.” So, we’ve connected successfully. It replies: “It’s running now. You can start working right away. Type help to see the commands.” So, we’ve successfully connected Telegram, and I can now send messages to this Hermes Agent. Basically, I’ve shown you how to buy a VPS, configure it to run Hermes Agent on that VPS, and set up a Telegram bot so we can use it as a channel for communicating with Hermes

**[30:37]** Agent. Since this is a completely new Hermes Agent and it doesn’t know anything about me yet, I’ve kept this demo fairly simple. Once you reach this setup stage, you can start talking and When you talk to Hermes Agent and ask what it can do, think of it as one of your employees—someone who has just joined the company, or simply a new friend you've just met.

**[31:05]** You definitely wouldn't want to share too much information with them, such as your Gmail accounts or other account details. related to your code, and so on. There are many things like that which you won’t want to share immediately with someone you don’t trust yet. So, talk to it as you would to an employee, and adjust your mindset accordingly. Instead of treating it as just a chatbot, think of it as an employee. You assign it a task and expect that task

**[31:33]** to be completed. For example, let’s say For example, I might give it a task: every day at around 8 a.m., please compile all the hottest tech news right now for me. Then, at 8 a.m., I'd say to it... Hermes Agent exactly that. Since I’m recording a demo for you, I’m using Telegram Desktop here. In practice, you can also use it on your phone. If you use the Telegram app, you can chat

**[32:00]** with Hermes Agent there as well. Let’s try it now. Now, create a job for me that runs at around eight every morning and gathers all the hottest technology news. It seems that because I spoke Vietnamese, it didn’t understand my message. So, I’ll just type it now. Here I go: create a job that runs every day at eight in the morning and summarizes the

**[32:30]** hottest technology news. There, I’ll send this to Hermes Agent. As you can see, when we send a job like this, it automatically knows which skill from the Hermes skill set to use. By default, Hermes already includes a collection of built-in skills. While working with us, Hermes can also automatically create additional skills, and update existing ones when

**[32:56]** necessary. Right, whenever it creates something or updates it, it lets us know, so we don't need to worry about this. It all happens automatically. The simplest way to think about it is as if we're working with a person. We need to change our mindset when working with Hermes Agent in exactly the same way: we assign a task to this employee and expect it to know automatically what to do.

**[33:21]** And now, let's try it. I'll choose Vietnam time here. It knows I'm in Vietnam, right? Vietnam time. But if we wait until, uh, eight tomorrow morning, it’ll be very hard to demo for you. So in a moment, I'll tell it to trigger this cronjob right now, so we can see exactly what content it returns to us. It says it created the Daily Tech News job

**[33:48]** for 8:00 a.m. Vietnam time, with up to seven top tech stories from the past 24 hours. Since we'd have to wait until tomorrow, I'll say, trigger Now. I can see it says it was sent to the background and will appear in this chat when it finishes. I'll wait a moment for Hermes Agent to run and respond to me. It also tells us that my web search

**[34:15]** tool—the one I registered earlier with DuckDuckGo, right?—is failing because it hasn't been installed yet. Let's see whether it can fix this problem automatically. And it says it doesn't have permission to write to Hermes. So now it has another route: using RSS instead. From what I can see, is it smart? When it tried searching with our search

**[34:42]** tool, such as DuckDuckGo, it wasn't successful. it immediately looked for other options, and we didn't have to intervene at all throughout the process. It found another route: using a script of its own to retrieve the RSS feeds. Now I'll tell it to run the script it just created and see whether it runs.

**[35:10]** See? It gives us, uh, seven tech news stories. August 21 tech news. See? I give it a task, and it knows how to find other options instead of using the approach we typically take with chatbots. We usually co-work with them, working together. But with Hermes Agent, we can think of it as an employee—an extremely intelligent employee. and it will figure out on its own how to

**[35:36]** meet the requirement we gave it. So, that was our first demo. To make this search tool properly reusable, you can run the Hermes Setup command again and choose a different web search provider, because DuckDuckGo no longer works. Now, this is the kind of task that requires web search. So I’ll tell Hermes Agent: create a daily

**[36:02]** reminder for me to take my medication at eight o’clock every evening. So, once I give it a request like this, every evening at eight o’clock, the Agent will automatically send me a message reminding me that it is time to take my medication. In the past, I would typically use N8N for tasks like this, but with N8N I still had to set up workflows, and that could be quite complicated. So now, as you can see, using Hermes Agent

**[36:30]** makes everything much simpler. We simply chat with it in natural language, as if we were talking to an ordinary employee, and it automatically runs in the background on our VPS, acting like a 24/7 personal assistant. You can also see this here. Here, can you see this? There is a message saying, “Self improvement review user profile updated.” That means it has automatically

**[36:55]** self-improved. This is an AI agent that improves itself, making itself smarter by automatically updating this user profile. We do not need to worry about what Hermes Agent does behind the scenes; whenever it does something, it lets us know. It does all of this automatically. We can view everything we just set up in this UI, including the Cron Job section. These are the jobs I requested. I have two, right?

**[37:22]** One reminds me to take my medicine in the evening, and it appears here. The second is the daily tech news briefing. In addition, you can also talk with Hermes Agent through Telegram, and it will handle things automatically for us. If you want to see more details in the UI, you can open the Hermes Agent UI. In addition, to expand an agent’s capabilities, once you trust this assistant tool, you can install and use MCPs with it.

**[37:50]** MCP stands for Model Context Protocol. This is a way for agents to expand the scope of what they can do and retrieve additional context from external applications. If you work in IT, you are probably familiar with Atlassian, right? It provides tools such as Jira and Bitbucket, which we can use to work and push code as well as create tasks there.

**[38:18]** By clicking the Install button here, we expand Hermes Agent’s capabilities even further. Similarly, this section includes many other MCPs, such as Figma, N8N, and Notion. We can install them directly through a UI like this. And besides that, there is another task I use quite often. When we deploy apps, many of them continue running while users are still using them, right?

**[38:47]** As a best practice, we usually need a page where we can monitor their status and health status, to check whether everything is currently online, or whether our service has encountered an error. We can also create a Cron Job to monitor these services automatically. For example, every two minutes or every minute, this job automatically calls the services through their health check URLs,

**[39:12]** and immediately sends a notification to Telegram for us. This is also one of the tasks I use very often. Basically, Hermes Agent is now very suitable for repetitive tasks. For more intensive coding tasks, I still use tools such as Codex or Claude Code for deeper coding when I work on a computer. Normally, I use Hermes Agent when I am

**[39:38]** out, taking a walk, or even just enjoying myself. If I suddenly have a good idea, I can tell this assistant to save it for me. Or, when working in a particular field, I might suddenly notice that a competitor, take a photo, and send it to Hermes Agent. The Agent can automatically save it so we know that we want to keep track of this competitor, and so on. In other words, any tasks we normally

**[40:03]** handle on our phones, while away from our computers, are a great fit for Hermes Agent, and it is especially powerful as we use it more and more, because Hermes Agent becomes increasingly intelligent through the Learning Loop system I described at the beginning of the video. Or, here is a very quick request: Create for me Let’s make a 4K image of a beautiful field, with a little boy herding buffaloes and happily making that cute “chiu chiu”

**[40:33]** sound. That’s basically it. I kept it simple because I’d already set up the image tool. I’m using my Codex subscription, and I’m asking the tool to make it. These are the typical tasks you can handle once you’ve granted Hermes Agent the necessary permissions. We can give it access to Google Drive so it can review our revenue figures and financial reports, right?

**[41:01]** Then we can have it create a job that summarizes everything quarterly, weekly, monthly, and so on. Or we can connect it to Gmail to automatically update our invoices at the end of every month. Instead of doing all that manually, once we grant Hermes Agent the right permissions, connections, and MCPs, it can handle those tasks completely automatically for us. automatically, saving us a lot of work and

**[41:28]** acting like a real assistant. And here, you can see the image it created for me. It looks pretty beautiful, right? GPT Image 2 is quite powerful, so it creates very nice images. So now I practically have an all-purpose assistant that can do almost anything for us, even create a website. Here, you can see that it automatically refreshed these skills and updated them for us.

**[41:57]** See that? Self improve review, skill schedule, news digest. We can view all the skills in the Skills tab right here. We can also see a whole list of skills here, including the ones that were already available. Hermes Agent comes with a large collection of built-in skills, and any skills it creates automatically are listed here too. You can look through this section and find everything. Now I’ll try searching for the Schedule news digest skill.

**[42:24]** I’ll search for it here. See? It found the skill it just updated for us, schedule news. We can even edit it directly on this page. But we only need to edit the things that matter; otherwise, we can let Hermes Agent handle all those tasks automatically. We don’t need to worry about that. Now, let me show you one more thing. I’ll tell Hermes Agent to create a website that tracks the Bitcoin price and automatically deploys it to Vercel for me.

**[42:54]** Let me say that now. You can simply tell it what you need in plain language, and the more specific you are, the better. For example, I’ll say: create a website that tracks the Bitcoin price deploy Vercel This task takes a little while, so I’ll wait for it to finish before we continue. See that? Even though I haven’t logged in to Vercel,

**[43:19]** it says it will create a temporary deployment. In other words, it will make a temporary deployment so the site can still be deployed to Vercel for us. As for the part where you want to set things up so you can log in to Vercel, you can simply tell this Agent to do that. Now I’ll open the website and see what the site created by this Agent looks like. See?

**[43:44]** In less than five minutes, it created a website for me and deployed it successfully. So, Bitcoin is really taking off today, up by as much as ten percent. See that? We have a very simple page like this, but this is only a basic demo. Still, you can see how powerful Hermes Agent is. We can use many different LLM providers. And if you use the ChatGPT ecosystem, it’s extremely convenient and extremely beneficial,

**[44:12]** because one subscription account gives you access to so many things. And while you’re working, Tibo resets quite often, right? So you get a lot of value from it. It resets around two or three times a week, which makes it very comfortable to use. Personally, I can use the Plus plan quite freely because I still handle the heavier tasks in Claude Code. The tasks I run through Hermes aren’t very demanding, so I also use the ChatGPT Plus plan, and that’s more than

**[44:41]** enough for me. Now let’s move on to checking security. Hermes also provides a tool that lets us check its security using a command called Hermes, Security. Now, if you have a question, or if you want to ask Hermes Agent itself to check—just say, in the ordinary way, “check security for us,” or “check security for me,” .

**[45:09]** But Hermes already has a command, right here, for checking the security level of Hermes Agent, so we can simply tell it, “um... Hermes, please run the Hermes Security check for me. It reports that it couldn't find a single vulnerability in any of the 152 components. Since I had only just installed everything

**[45:34]** from scratch, and this was also the latest version of Hermes at the time I recorded this video, around August 2016, the system had already received a number of important security updates and many security patches. So at this point, there are essentially no security issues. And that's all the demos I wanted to share with you. Now I'd like to leave you with one final, open-ended suggestion. Imagine that right now we have just one

**[46:02]** Agent, the Hermes Agent, right? And imagine that, when you want to expand it to the scale of a company, you might want to create additional Agents specialized in marketing, finance, operations—the day-to-day running of the business—or sales. Once we divide the work among separate Agents like this, and give each one a clear role, they will definitely operate more efficiently than That is certain.

**[46:28]** But we must balance whether creating another Agent is worthwhile. In practice, start by working with the first Agent, the Hermes Agent. Then, as you work with it, if you find that creating another Agent is necessary, you can simply chat with Hermes Agent, and it will guide you through automatically creating new Agents for us. Each Agent will have its own context, its own permissions, and its own tools. That makes it much easier to scale up and

**[46:54]** expand the system. This is just an open-ended suggestion from me, because in reality Hermes Agent has much more knowledge than I could possibly cover in a short video like this. Now you can start working with Hermes Agent and gradually build these Agents up over time. That's all I wanted to share today. I hope you learned something useful. If you find my videos useful, please leave

**[47:19]** a like and subscribe below. Thank you, goodbye!
