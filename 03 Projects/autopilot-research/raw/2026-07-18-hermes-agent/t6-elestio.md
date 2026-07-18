> Source: t6-elestio.en-orig.vtt
> Converted: vtt-to-md.py
> Format: `[MM:SS] line` — verbatim auto-sub, deduplicated, word-timing tags stripped


**[00:02]** Are you looking for a free open-source platform [music] to run AI agents on autopilot? Let's discover Hermes Agent, a self-improving agent runtime that bundles persistent cross-session memory, autonomous skill creation, and isolated sub-agents for parallel work streams. It allows you to schedule automations, comes with tons of built-in tools, supports any LLM provider, and ship with native gateways for Telegram, Discord,

**[00:29]** Slack, WhatsApp, and [music] more. All from one process sharing the same memory. To start using it, you can self-deploy it on your device or server by running these two commands on the official website, or use a platform like ours, Elestio, to deploy it seamlessly on your server or the cloud provider of your choice. We handle the installation, backups, updates, and ongoing maintenance for you. To start using Hermes Agent on our platform, [music]

**[00:57]** head to ls.io and click on login. Then deploy my first service, search for Hermes, select, choose between the [music] different cloud providers, regions, and service plans based on your needs, and then click on next. Change the service name, adjust more advanced settings, and choose between different level of support. The first one is free and included by default. Once you're all good, hit the create service button. Once the installation is finished and

**[01:26]** your new Hermes instance is ready, you will receive this email with the link to access the UI, the agent monitoring dashboard, but also instruction on how to set up properly your instance. Because on some software, we can't configure everything right beforehand. So now, what we need to do is to look at these commands here. We want to run them on our Hermes instance. So go to Elestio on the dashboard of your instance, go to tools,

**[01:55]** and terminal. It will display the instruction to access the terminal. So, let's copy the password. Username will be root, and we can follow the link. Type root, paste the password, and sign in. Okay, we are connected to the terminal. Let's simply copy-paste these commands. Here it is. Run. And this command is to let us, as the user, to choose the LLM provider we want. So, you have many available, the

**[02:25]** most famous one, such as Anthropic, OpenAI, Google, Co-pilot, some less well-known, and you can even connect custom ones. What I will use for this video is GitHub Co-pilot. So, I will simply hit enter on that, and I have different way to connect to it. Either one, login with GitHub, or enter a token manually. I will choose one. I follow the URL and follow the steps. I authorize it. The

**[02:55]** connection between my Co-pilot account and Hermes is successful. It lists me the model available through my GitHub Co-pilot subscription, and you can choose the default model you want to use. Let's take Claude Opus. Then, you can choose the reasoning effort. So, be aware, the more you use it, uh the more tokens it might use. So, depending on what you are trying to achieve, you can put more or less. I

**[03:22]** will keep the default, and I'm all good. If we read correctly the instruction, then it tells us once we have finished this to also run this command. And also to not worry because we can still configure things later, but we will see it together. So, let's simply paste the command. It's restarting the Hermes agent and web UI, and we are good. Let's start exploring it. Let's go back to overview on our

**[03:51]** instance. We have two URL we can use. The first one is the admin UI that we will use in this video mainly, and the second one, which is more an agent monitoring. We will explore both. Let's start with the first one, copy the password, and follow the link. Paste it and sign in, and we arrive on a Hermes UI. So, let's quickly start to see if everything is set up correctly just by saying hello. And we are getting an

**[04:19]** error. So, it seems that Cloud Opus 4.7 isn't working with Copilot. So, we can try something else. Let's say 5.4 mini, try it, hello, and it seems with GPT-5 mini it's working. So, so far we will use this one. This is a classic chat interface where you have all your conversations, but with a few great things. First, you can create AI profile. So, here by default, we are on the default one that is created

**[04:46]** automatically. If we go to manage profiles, we can have multiple ones. So, if we click on the plus button, we are able to name it and choose another LLM for it. The profiles with Hermes is the equivalent of agents. So, you can see them as different persona, or to have one uh specialized in specific skills based on the LLM model you will use, the resources you will allow them, allowing you to create a real virtual team. Let's

**[05:14]** say for content creation, you use of these models, for marketing, you use that, for coding, something else. You'll find the perfect recipe for each use case. If we go back to the chat, you can also choose from which workspace you work from. Because uh the different agents work on your server, each agent will have its own workspace, but you can also use sub workspaces for specific tasks and projects. As you've seen

**[05:42]** earlier, you can define what model you want to use per message, and here we have only uh connected GitHub profile, but as you can connect multiple providers. And the list can be very long. So you can choose it by message, but also per profile. Here by default this is the one you configured earlier, but we will change it later. And more than that, you can adjust the intensity you want to use based on what you ask the AI. And you also have details about

**[06:09]** the context. By default each chat session appear in the all, but inside it you can create sub projects. A very useful feature not present in most of the public AI providers. Let's say content creation. And of course, inside a project you also have the liberty to choose between the different um profiles you created. Let's dive into what we can do. So you have

**[06:37]** the chat where you can talk to your agent, even if most of the time you will talk with your agent using a messaging gateway. So you can see most of the providers. Most of the typical one are available with Hermes. But what can make them really unique is to create skills to your agent. The skills can be defined per agent, per profile, and you have a lot that are available by default. For example, creative architecture diagram.

**[07:06]** You are able to see what it contains, edit it, delete it, and also add new ones. You can ask your AI to do things directly in the chat, but also to schedule tasks. So you would say every morning at this time you would do that. Every week you would do that procedure. And it's a very easy to set up, especially with this interface. So you can name create something. For the schedule, it's either a chronic expression or you can write every 1

**[07:33]** hour. Prompt, create a random art. And you can also attach a skill to it. I've seen earlier you have an ASCII art one, so let's select it. Save it. So, the job is created and we can try to run it. You can see the job is running, but I think it will fail. So, if we open it,

**[08:01]** we can see it failed and it's because the default LLM for this profile is the one that doesn't work. So, let's change it. If we go to settings, um default model here, I don't remember which one we were using GPT-5 mini. Let's keep this one, we know it works. Save settings. Another thing we can do to organize the workload we want to give to our agent is not with scheduled task,

**[08:29]** but with the Kanban, so real project management. Uh we won't use this UI because for any reason the plus button doesn't work here. So, it's the right moment to switch to other agent monitoring UI. So, copy the password and go to it. You arrive on this more modern user interface where you can change the theme with the different colors you like. I don't understand exactly why they have

**[08:58]** these two UI because some things work here and don't in the other and some don't work here that work in the other. For example, you can chat directly here. It's more for monitoring, but the Kanban plugin only works here. So, you can see you can add different tasks in the to-do, for example, new task title do X on Y project. You assign someone to bot. You choose the skill you want to

**[09:26]** use. You create it and once you're good with all the different things, you can run that dispatcher. And if you don't want scheduled job and you don't want to use a full project management software, you can use even more simple thing. And for this one, I need to go to the old UI, which is the task list. It looks a very similar to Cloud Co-work, where you can give

**[09:55]** instruction to your AI and it will run it in a specific workspace. So, let's keep home, but you can choose a different one. Let's say generate a random name generator. For this one, we'll use Grok code fast. Enter. The AI is working on it. We can see what it's doing in real time. So, it's writing a file, a Python script. As we didn't give any instruction about it, it finished. It shows us the full code that it generated and gave us also a

**[10:25]** sample run. So, here it's a very simple example, but know that it's running on a dedicated server and you can give it task and it will work on its own isolated. If we go back to the monitoring UI, you can have access to analytics to see the different models that you used and number of token used. So, I think the best screen is here, models. And you have clear details about the usage. You also have the other feature

**[10:53]** we saw together in the other UI that you can also set up here, but some are not available. For example, you can't create a skill unless I didn't find where from here and you can't have access to the detail. You can just enable disable them from here. But again, most of the time you won't use the UI unless for the initial setup and you will talk directly to your AI using your favorite platform, such as Telegram, Discord, Slack, anything else. As always, I highly

**[11:20]** recommend you to dive into the documentation for the different features I didn't cover in this video that could be useful for you to set up your AI agents. Thank you for watching. We hope you enjoyed discovering Hermes with us. Please hit the like button to help our channel be more visible [music] to other open source lovers. Don't forget to subscribe to not miss our next platform [music] overviews. If you want to continue your open source journey, watch
