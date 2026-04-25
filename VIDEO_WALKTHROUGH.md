# Video Walkthrough — 100Hires Git Repo Presentation

[https://www.youtube.com/watch?v=NoNoduM7SP0]

## Full Transcript

[00:01
For any project that I built, when I built this repo, I used Gemini and Cloud in Browser to stress test if the idea that I was going for would appeal to the end user. All of my projects are designed with the end user experience in mind, which includes myself, and that's why they rate me, is a consolidation of everything that I wrote. That's why you also see this at the top, it takes you straight to the playbook.

00:23
I kept it pretty lean, mainly because I don't like to see stuff that has like a whole bunch of just folders and things to click through. So you mainly have like the cloud folder, you know, this was made with cloud code research, which pretty much contains like the LinkedIn post, YouTube transcripts, like these are actually kind of summarized pretty nicely. Like, for example, if we go to like Cori's, his videos are like pretty long, but basically, you know, I got these transcripts through one of the APIs that like I use for other projects that I do since it wasn't very many videos and you can kind of just like see the main idea here and this was really like decided for readability so and also you have the key entities or like the strategic category and you kind of see that same with Lily she's another one of my favorites and you'll see why later but you can see kind of like what she goes for and this is just highlighting the key points so going back here

01:09
Also, like, some of the LinkedIn posts, this is good to have for other creators that you might find more on the internet. Like, Denarty, for example, BofU content, same deal. And this is, like, direct text, like, from the LinkedIn articles because I know that some people, like, they can remove their content whenever. So, like, that's kind of, like, what I had in mind here. Then let's see. What else did I do? Okay. And also the source architecture. This is like kind of like one of the hidden things, but basically when I first started this project, like I kind of did it with the playbook in mind. So the pillars that I created like for the architecture, semantic layer, like audit proofing the logic, and risk mitigation. And by the way, something I want to point out about like these, mainly these three pillars, is these are all things that you have to do to be effective at prompting.

01:51
I know that I probably talk way too much, but I am going to try to keep this short. So yeah.

01:57
tech stack like with gemini and cloud so i'm going to show you like exactly what i mean so i kind of use gemini for like the meat and potatoes or like my architecture to like make sure it's technically sound because gemini tends to do better with those technical tasks it's not too good with like personalization and things like that but it is pretty nice and also i use it as a way to like stress test my logic and see how it looks before i just decide to commit it so you can like kind of see that here like with my prompts and you know this is where i also get to ask like some of my nerdy questions and they're mostly structural this is like just like how I work in general and Claude like you'll kind of see some of the same thing like this when I came up in Gemini what do you think I like Claude because Claude is a bit more user-friendly so like if I have complex ideas or I'm just literally talking like off the wall in ways that do not make sense Claude will definitely tell me in a way that aims to be digestible to the end user and also just some generally good ideas

02:45
And so now I'm going to pull up Codex. So here's Codex. Now, because quad code does use so many tokens, and I use quad in Gemini for a lot of things, but especially quad, I had to be pretty economical with my tokens and strategic. So the general logic for each push through quad code in Cursor is basically one commit per logic track. So I'm going to show you something here. You're going to only see commits in this track. And they were, surprisingly, just these very few commits ate up a lot of my limits. That's always something you have to be mindful of. But starting from the top, So you see that I first started with the research. That was the first commit. Then the structure was created, so you can see what I did, like the subdirectories. So this was from the very beginning, thinking with usability in mind. And also the little notes, so I can just anchor and remember what I did.

03:28
And you see those notes. And then this is what I did here with the sources, with the pillars. And also, this is cool. If you keep quadcode pretty clean and you keep the prompts clean, it'll tell you what you did. So if you walk away and go take a walk and come back, you're not totally lost. that was kind of the objective like with also the amount of commits as well because like i can actually go back here to like github and in my repo so like you can see like the number of commits and when i click here it's like a way for me to like also like track my logic in real time or like for a playbook application if something went wrong i can kind of troubleshoot like the errors in my reasoning so that just like kind of like keeps it clean all right now we're going to talk about some of the sources that influence my playbook so i'm going to give you three sources um But before I build anything, I will tell you that usually I am always risk aware, uh, when I build things and that doesn't mean I'm adversarial or like I'm overly cautious, but I just think that we have to know like what the constraints are.

04:25
So the first one that I'm going to pull up is Lily, um, with algorithmic risk.

04:33
There's like the video link for her. Um, but at the beginning she talks about like SEO follows a predictable cycle. Things work, they get shared, reverse engineered, targeted by updates, get devalued, rents repeat. We see this pattern a lot with various tech tools. So I think that is pretty important to keep in mind. And this has always been a thing that's not going to go away. And this is why I really like her content, also how she talks about the EEAT framework. like the experience, expertise, authoritativeness, and trustworthiness, because that's what's really going to target that Frankenstein buyer. But this is also what is going to stand out on the AI search results.

05:16
In some more of her content, you know, she does talk about some of the updates and just like also a general risk about LLM referral traffic, but also the AI overviews. And the gap between getting people to go from just looking at an overview to clicking is definitely important. But somebody who's already familiar with AI, you're not really convincing them.

05:41
So they are more likely to engage with the AI overview and probably click anyway. So that was part one. And then the second part was Corey's content. So he actually confirmed some of my suspicions.

06:00
that oh what was i gonna say about architecture okay that's where i was going with that um he confirmed some of that and i think like this is just like generally true like when you're working with ai tools however when i was reviewing his content um it definitely sounded like somebody who was already at like a pretty specific stage um and it just like reading this like you can definitely tell like this is not for somebody who's in those earlier stages or maybe they're doing something new uh and that's like kind of what led me to like the third point uh for inspiration of the playbook go back here and we have mike king uh he's a pretty popular one but he also warns about the risk of like aio reviews uh causing traffic loss you know

06:53
click reduction which is like basically your organic traffic and stuff and I also mentioned this like in my playbook as well and this is kind of what prompted me like at this point um I went and just like checked out your website and looking at like 100 hires I was like dude you know who would benefit from this the Frankenstein user I call them the Frankenstein user because like there are people you know even like myself who will string together like a hundred different tools um just to do something but then it gets to a point where you're like wow why do I have so many subscriptions like this is just not very efficient um however since these people are already engaged you know like I said before uh we're gonna have to Target them in like a really precise way but we also need to be mindful of the risk mitigation that Lily mentioned like with Google policies and stuff uh so we're not trading tomorrow's future for the games of today

08:20
All right. And because I am a pretty chatty person, I love talking about my work and making it digestible to people. I am going to show you exactly how I interact with AI in general, because like I know that's always like interesting to see. But what I do like with your questions is I basically like run them through like Google. This is output from Gemini because you can export directly.

08:48
And like kind of like a what to like talk about because I am so bad at like reading off a script. And I just have so much to say. And sometimes it can be hard for me to keep it concise. So this is like my anchor. And then wherever I feel like there were gaps or like it just sounds meh. It just sounds really chonky and just not like me. I end up just going through and writing. Like I actually love writing things like this.

09:14
So you can actually see my logic. So like this is all mine. And then what I do after that is I go make another chat.

09:22
And, you know, Claude, you know, this is an example of like how I use it as a thinking partner. So let me scroll up to the top because this is one of my short ones.

09:30
Also, I end up having extremely long chats with Claude or just any AI. You can probably tell, love to talk.

09:38
Not afraid of sharing my logic, but still continuing off the chat because, you know, I have previous contacts. Claude does a pretty good job at pulling that.

09:47
and let's see gave some tips but i was like okay um here's like the email and then like this is me like thinking through like some of my math like you know like i was like thinking like maybe a tick tock style section that was kind of like in the previous prompt and then we get down here and i was like okay so you know like i finished writing this like i actually put some thought into this you know um so like this is my sparkle and i like it when plot respects my sparkle of course um tells me like what's the weakest or like what i probably just didn't explain well or miss i try not to miss anything because you know i want to be respectful of your time and like i care about the user experience um and also of course so it's a good experience for me but as you can see here claude genuinely did not overwrite anything so

10:35
This is all my content and then make this nice and clear for you and to wrap this up. So explaining the piece where the experts contradicted. So I've got this on the screen here, like just for clarity, but this is like a glaring contradiction between the sources. Like Mike is telling you, yeah, you need to like put it out there.

10:58
You know, this is what converts. The goal is extractability, you know, get out there. And Lily's telling you, well, you know, here's some of the things that can happen. Here's like some general things to like keep in mind with Google and their content policies and things like that. But both of them ultimately talk about like different parts of the downstream. And I think that's really important when we talk about contradictions because when something contradicts, sometimes it's not necessarily a contradiction. It depends on like who they're speaking to at what stage. And that was kind of why I designed my playbook the way that I did And why I wanted to talk about targeting the Frankenstein buyer, because first, it doesn't really require you to go out of your niche to reach these people. They're already using tools that are very similar to what 100 hires is offering.

11:50
The other thing is like, you can also see my logic of how I used another AI tool like Gemini to actually index 100 hires, see what's out there, like kind of see what you do and validate or maybe bring to my attention some things that I could not immediately see from looking at your website. But something I do know about this buyer that we're talking about is they're not looking to be convinced. Like they want functionality.

12:13
They're not fumbling with an ATS. They are not trying to figure out how to write a prompt, you know, and they're probably already engaging with AI.

12:21
But reaching them is going to be difficult because, you know, when you are searching through an LLM, it's so not the same as searching in Google. Even within Gemini, like I think Gemini actually can go a bit deeper and um than just like regular google but it's not the same and you have to be extremely targeted like if i put something in gemini and gemini finds it for me like it's crazy oddly specific um so that's like a very like high signal low noise like um group to target and mainly what they're looking for if they're going to go on an ai they want a solution to a problem they need a tool and that's ultimately what 100 hires does and

13:00
Of the most skippable, so I generally tend to lean more pragmatic, like, in the way that I work.

13:07
I just wouldn't recommend following Ben Goody, even though he's a great guy to get you up to speed on everything. Most of his stuff is, like, really designed for a consumer or somebody who needs a prescriptive list. Like, if you're an operator, you know, you need high signal, low noise, and you need something that's, like, relatively actionable in his content that's not really going to be easy for you to do that with. and also within the playbook i do explain like when it should be used when it shouldn't be used and how it should be used but before i even open it i want to know the objective um and like what's the task pick a lane execute rinse and repeat also like since we're already using so many ai tools it's much easier for us to extract insights and the data and actually act on them and change in real time um and since we know that like the frankenstein buyer like has like a legit pain they

13:57
definitely need something a lot cleaner and i mean that's genuinely underserved like for a lot of things and i mean you could definitely expand like a bit in this like consolidated tool lane if you really wanted to um but yeah like i said before like we're not like reinventing or creating content outside of scope to get to these people We already know they're not gonna spend hours scrolling in Google and whatever else. They're already using AI search, LLM search.

14:28
And that's kind of why this is pretty good with my idea. And the existing SEO infrastructure and their behavior, it kind of points at the same place.

14:44
So in the next two weeks, I would identify where that buyer's actively searching make sure that 100 hires is like in those results and i could probably personally verify because i love a good ai search and make sure that we're actually targeting their pain my general framework for thinking is observe orient decide act rinse repeat all in like one you know sweep like there's no pauses in any of that um like i said if something's off We change plans, but we don't really need like a lot of time to like change plans. Like we can do this pretty rapidly and agile, like especially at an AI native company.]
