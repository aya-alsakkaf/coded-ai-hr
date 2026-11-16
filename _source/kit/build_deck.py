# -*- coding: utf-8 -*-
"""The slides of AI Fundamentals for HR, day by day: the kit's slide source. The engine's deck.py renders every call.
One helper call is one slide. Every note is written as N(...) parts and never repeats the slide text.
The engine adds the close slide of each day from CLOSE."""
from deck import *
import content as C
import content_demos as CD
from content_demos import DEMOS
import data as D

SECTIONS = {
 1: [("Opening", "g-mark", ["open"]), ("How AI works", "g-code", ["b1"]), ("Prompting", "g-frame", ["b2"]), ("Word", "g-impact", ["b3"]), ("Word and Outlook", "g-code", ["b4"]), ("Close", "g-progress", ["b5", "close"])],
 2: [("Opening", "g-mark", ["open", "c0"]), ("Safe data", "g-code", ["c1"]), ("Meetings", "g-frame", ["c2", "c3"]), ("Excel", "g-impact", ["c4"]), ("Word", "g-code", ["c5"]), ("PowerPoint", "g-frame", ["c6"]), ("Close", "g-progress", ["c8", "close"])],
 3: [("Opening", "g-mark", ["open", "e0"]), ("Agents", "g-code", ["e1", "e2"]), ("Power Automate", "g-frame", ["e3"]), ("Workflows", "g-impact", ["e4"]), ("Close", "g-progress", ["e5", "e6", "e7", "close"])],
}
FLOW = {
 1: (["AI", "Prompt", "Word", "Outlook", "Save"], {"b1": 0, "b2": 1, "b3": 2, "b4": 3, "b5": 4}),
 2: (["Data", "Meetings", "Outlook", "Excel", "Word", "PowerPoint"], {"c1": 0, "c2": 1, "c3": 2, "c4": 3, "c5": 4, "c6": 5}),
 3: (["Agent", "Test", "Flow", "Map", "Compare"], {"e1": 0, "e2": 1, "e3": 2, "e4": 3, "e5": 4}),
}
COVER_NOTES = {
 1: N(time="09:00-09:10", do="(Before 09:00: helpers walk the room and check that every laptop is signed in to Copilot Chat with a work account.)",
      more=["Housekeeping: breaks at 10:30 and 13:20, lunch and Dhuhr at 11:35. Prayer room and toilets."],
      say="Good morning, everyone. Please open your laptop and sign in to Copilot Chat with your work account while I set up. "
          "If anything does not work, raise your hand and one of us will come to you. We start in two minutes."),
 2: N(time="09:00", do="(Before 09:00: check that every laptop has Copilot Chat open, and that people downloaded today's files from the Day 2 page.)",
      more=["Housekeeping: breaks at 10:45 and 13:35, lunch and Dhuhr at 11:35."],
      say="Good morning, and welcome back. Yesterday you learned to ask clearly and check everything. Today we protect people's data, run meetings, check numbers, and finish with Word and PowerPoint. Please open Copilot Chat while I start."),
 3: N(time="09:00", do="(Before 09:00: open Agent Builder on the presenting laptop, and check that the Power Automate demo video plays with sound.)",
      more=["Remind the room: post-MAP and survey at 14:20, certificates at 14:40.", "Ask everyone to download today's files from the Day 3 page."],
      say="Good morning, and welcome to the last day. Today your best requests become tools that other people can use, and after lunch we look at a whole HR process."),
}
OUTCOMES_NOTES = {d: N(expect="Most people pick the checking outcome.", silent="pick the one you use most yourself and say why.",
                       say="These are the four things you will be able to do by the end of today, on fictional Mutla files. "
                           "Which one matters most for your own job? Tell your neighbor in one sentence.") for d in (1, 2, 3)}
ROAD = {d: {"title": "One company. <span class=\"hl\">Five HR units.</span>",
            "n": N(do="(Point to each block, then to the breaks.)", say="This is our day. Mutla Oil Company has five HR units, the same as many real HR departments. "
                   "Pick the unit closest to your own job: you will use it in the tasks. When I press the cup button, the break clock starts.")} for d in (1, 2, 3)}
CLOSE = {
 1: {"big": "Ask clearly. <span class=\"hl\">Check everything.</span>", "next": "Tomorrow: safe data first, then meetings, Outlook, Excel, Word and PowerPoint.",
     "n": N(say="Thank you for a great first day. Please bring the same laptop tomorrow. See you at 9:00.")},
 2: {"big": "Safe data. <span class=\"hl\">Checked figures.</span>", "next": "Tomorrow: two HR agents, a Power Automate demo, and a whole HR workflow.",
     "n": N(say="Thank you for a full day. Tomorrow you build your own agents. See you at 9:00.")},
 3: {"big": "Copilot drafts. <span class=\"hl\">People decide.</span>", "next": "Thank you. Copilot drafts. You check. Authorized HR staff decide.",
     "n": N(do="(Hand out the certificates.)", more=["Point to the take-home guide and the safe-use card on the workshop site."], say="Thank you for three great days. Start with one green task at work this week.")},
}

R = D.ROLES["cmp"]

def live(sid, topic, did, title, show, watch, n=None):
    """A live demo slide: what the trainer shows, what to watch for, the files. The notes keep the click steps and the backup."""
    d = DEMOS[did]
    files = ", ".join(d["files"]) if d["files"] else "none: the request is on the prompt sheet"
    items = [f"<b>What I will show:</b> {show}", f"<b>Watch for:</b> {watch}", f"<b>Files:</b> {files}"]
    steps = [x.replace("[T] ", "") for x in d["setup"]]
    base = N(time="5 min, live", more=["Click steps: " + " ".join(f"({i}) {x}" for i, x in enumerate(steps, 1))] + list((n or {}).get("more") or []),
             expect=d["expected"], fallback=d["fallback"] + f" The backup is on the Day {d['day']} backup results page, {d['card']}.")
    if n:
        for k in ("say", "do", "silent", "time"):
            if n.get(k): base[k] = n[k]
    return listslide(sid, topic, f"{d['card']} · live in {d['tool']}", title, items, d["point"], n=base)

# ------------------------------------------------------------------ Day 1 · Copilot Foundations for HR Documents and Communication
def day1():
    welcome = listslide("b0welcome", "open", "Welcome to CODED", "CODED Professionals: <span class=\"hl\">learn it by doing it.</span>",
        ["<b>CODED</b> is a Kuwaiti tech education company. CODED Professionals trains teams from companies across Kuwait.",
         "<b>This workshop</b> is about 70% hands-on. You practice every idea on your own laptop.",
         "<b>Your trainer</b> teaches CODED's AI workshops for company teams. Ask a question at any time.",
         f"<b>{D.COMPANY}</b> is our practice company. It is made up, so you can make mistakes safely."],
        "Copilot drafts. You check. Authorized HR staff decide.",
        n=N(time="2 min", do="(Stand at the front. Smile. Wait for the room to settle.)",
            say="Good morning, and welcome to CODED. My name is [your name], and I am [your role] at CODED. For the next three days we are going to work, not just listen: "
                "you will spend most of the time on your own laptop. Everything we use belongs to a company that does not exist, so nothing you type can hurt anyone. "
                "(Point to the last line.) Remember this sentence. You will hear it every day."))
    s = opening(1, opener=[welcome])
    # Opener · one job description, live
    s.append(story("b0story", "open", "Opener · one job description", "Sunday 1 November, 09:20",
        f"Yousef, the HR Section Head, needs a job description for the new <b>{R['title']}</b> before the evaluation round. Abdulaziz opens Copilot and types one short line.",
        "One role, two requests. <span class=\"hl\">Watch what changes.</span>", "See why the request decides the quality of the draft.",
        n=N(time="09:20-09:30", say="Here is our first story. (Read the story aloud.) Before I show you anything: what would you type? Call it out. "
              "(Wait for two or three answers.) Most of us type one short line. Let us see what that gives us.",
            expect="Short answers like “write a JD for a compensation analyst”.")))
    s.append(live("b0live", "open", "d10", "One role, <span class=\"hl\">two requests.</span>",
        "One short line in the first tab. The full request, with two files, in the second tab.", "The duties, the team size and the grade line in each answer.",
        n=N(say="(Run the one-line request in tab 1.) Look at this. It sounds professional. Now read it slowly: a team to manage, a senior grade, duties nobody approved. "
                "(Run the full request in tab 2.) Same tool, same role. This one follows our template, uses only the six approved duties, and leaves the grade for the committee. "
                "The only thing that changed is what we gave Copilot, and that is what we practice today.")))
    # Block 1 · How generative AI and Copilot work
    s.append(story("b1story", "b1", "Block 1 · How generative AI and Copilot work", "This week",
        "Hands up: <b>how many of you used an AI tool this week?</b> At work or at home. What did you use it for, and which tool was it?",
        "AI is already <span class=\"hl\">in your week.</span>", "Say what AI is, where Copilot fits, and why it can write a confident sentence that is wrong.",
        n=N(time="09:30-10:30", do="(Count the hands. Ask three people: what for, and which tool?)",
            say="Block 1. Before we write a single request, I want to know where you are. (Read the question.) Keep your hand up if you used it for work. "
                "Now tell me, in a few words: what did you use it for?",
            expect="Most hands go up. ChatGPT, Copilot, translation, a photo app, maybe Google search.", silent="Write the tools they name on a sticky note. You come back to them on the next slides.")))
    s.append(term("b1ai", "b1", "Block 1 · the word", "First: <span class=\"hl\">what is AI?</span>", "Artificial intelligence (AI)",
        "Computer systems that do tasks which usually need a person's judgment: they <b>recognize</b>, <b>predict</b>, <b>sort</b> or <b>create</b>.",
        "Normal software follows rules a person wrote…", "…AI <b>learns patterns from examples</b>.", "AI is a big family of tools, and Copilot is one member of it.",
        n=N(time="3 min", say="Here is a simple definition. Normal software follows rules that a programmer wrote, step by step. "
                "AI learns from many examples. Show it thousands of junk emails, and it learns what junk looks like. Nobody writes the rule by hand.")))
    s.append(listslide("b1ex", "b1", "Block 1 · AI you already use", "AI you used <span class=\"hl\">before Copilot.</span>",
        ["<b>Email:</b> the spam filter decides which messages are junk.", "<b>Phone:</b> face unlock recognizes your face.",
         "<b>Maps:</b> the app predicts traffic and your arrival time.", "<b>Bank:</b> an alert flags an unusual card payment as possible fraud."],
        "These tools sort, recognize and predict. None of them writes you a letter.",
        n=N(time="3 min", say="None of these is new. Your spam filter learned from millions of junk emails. Face unlock learned your face. "
                "Maps learned from traffic data. (Ask:) What else on your phone learns from you?", expect="Photo search, keyboard suggestions, streaming recommendations.")))
    s.append(cards3("b1fam", "b1", "Block 1 · where LLMs fit", "So where do ChatGPT, Claude <span class=\"hl\">and Copilot fit?</span>",
        [("Artificial intelligence", "The whole family", "Spam filters, face unlock, maps, fraud alerts, and everything below.", ""),
         ("Machine learning", "AI that learns from data", "Most AI today: it finds patterns in examples.", ""),
         ("Large language models", "Machine learning on text", "It learned from huge amounts of text, so it can write. ChatGPT, Claude, Gemini, and the models inside Copilot.", "")],
        "Every LLM is AI. Not every AI is an LLM.",
        n=N(time="3 min", say="Picture three circles, one inside the other. AI is the biggest. Inside it, machine learning: AI that learns from data. "
                "Inside that, the newest circle: large language models. ChatGPT, Claude, Gemini and the models behind Copilot all live in this small circle.",
            silent="Point back to the tools from the first slide and ask which circle each one sits in.")))
    s.append(term("b1llmdef", "b1", "Block 1 · the name", "LLM: <span class=\"hl\">Large Language Model.</span>", "LLM",
        "<b>Large:</b> it learned from a huge amount of text. <b>Language:</b> it works with words. <b>Model:</b> a program that learned patterns from examples.",
        "A spam filter sorts the email you have…", "…an LLM <b>writes new text</b>, one word at a time.", "Each kind of AI makes its own kind of mistake, so each needs its own check.",
        n=N(time="3 min", say="LLM stands for large language model. The difference matters because each kind of AI goes wrong in its own way. When someone says the AI did it, ask which AI. "
                "A fraud filter can block your card by mistake. An LLM can write a wrong rule that sounds right, and you catch that only by reading the source. "
                "For Copilot, the check is always the source document.")))
    s.append(rule("b1fatma", "b1", "Block 1 · a story", "Fast, confident <span class=\"hl\">and wrong.</span>",
        f"Monday 2 November, 08:40. Fatma in Personnel asks Copilot how many days of leave staff can carry over. The answer comes at once: 30 days. Mutla's policy says {D.LEAVE['carry']}.",
        n=N(time="2 min", say="Now a real-looking story from HR. (Read it.) Has an AI tool ever given you a wrong number at work? One sentence each, two people.",
            expect="Two short stories.", silent="Share one of your own wrong-number stories if the room is quiet.")))
    s.append(rule("b1an", "b1", "Block 1 · the picture", "Your phone keyboard guesses <span class=\"hl\">your next word.</span>",
        "Copilot does the same thing with a much bigger memory. Its guesses sound right because it learned from a huge amount of text.",
        n=N(do="(Ask two people to type “I will be there in” on their phone and read the suggestions.)",
            say="Your keyboard does not know where you are. It only knows what people usually type after those words. Hold on to that idea.",
            expect="“5 minutes”, “a bit”, “10”.")))
    s.append(term("b1t1", "b1", "Block 1 · the idea", "What Copilot <span class=\"hl\">really does.</span>", "Next-word prediction",
        "Copilot writes by <b>predicting the next word</b>, one word at a time, from patterns in the text it learned from.",
        "Like your phone keyboard…", "…it picks a <b>likely</b> next word. Numbers and dates are words too.", "It predicts. Without the source, it guesses or searches the web, and nothing checks it against Mutla's policy.",
        n=N(say="So the official name is next-word prediction. Copilot is not looking anything up in our policy unless we give it the policy. "
                "It writes what usually comes next. People often forget that, to Copilot, a number is just another word, so it predicts numbers the same way.",
            silent="Ask: is the most common number always Mutla's number?")))
    s.append(llmslide("b1llm", "b1", "Block 1 · live widget", "It writes by guessing <span class=\"hl\">the next word.</span>",
        "At each step, every possible next word gets a score. The model picks one and repeats.", f"It predicts <b>likely</b> words. Mutla's policy says {D.LEAVE['carry']}, but 30 is more common.",
        n=N(time="7 min", do="(Read the start of the sentence. Ask the room for the next word, then click it.)",
            more=["Click Pick the top word: 30 wins, because it is common in policies everywhere.", "Start again and pick 15: Mutla's real number is only the second guess.", "Pick camel (1%). The sentence still sounds confident.", "The percentages are illustrative."],
            say="Watch what wins. (Click the top word.) Thirty, because thirty follows these words most often in policies around the world. Our rule says fifteen. "
                "(Start again, pick camel.) And even nonsense comes out sounding confident. The tone tells you nothing about the truth.")))
    s.append(term("b1t2", "b1", "Block 1 · the risk", "Fluent <span class=\"hl\">and wrong.</span>", "Hallucination",
        "When Copilot writes something that <b>sounds right but is not true</b>: a wrong number, date, rule or name.",
        "A likely next word…", "…is not always a <b>true</b> one. Nothing checks it for you.", "Check every number, date and rule against the approved source.",
        n=N(say="This has a name: hallucination. Many people think it means Copilot is broken. In fact Copilot did what it always does: it predicted a likely word, and the likely word was wrong. "
                "Fatma's thirty days was a likely answer and a wrong one.", silent="Ask: what would have caught Fatma's 30 days?")))
    s.append(check("b1chk1", "b1", "An employee forwards you Copilot's answer: <b>Hajj leave is 30 days.</b> <b>What do you check before you reply?</b>",
        [("How sure Copilot sounded in its answer", 0, "Sounding sure is not evidence. Check the source."),
         ("A second answer from a new Copilot chat", 0, "A second prediction is not a check. Read the policy."),
         ("The Hajj section of the leave policy", 1, f"Right. The policy says {D.LEAVE['hajj']} days. The approved policy decides.")],
        n=N(say="Quick check. Hands up for A. For B. For C. (Tap the most popular.) A second chat is just a second guess. Only the policy can answer this.")))
    s.append(rule("b1key", "b1", "Block 1 · a second picture", "A colleague with <span class=\"hl\">your keycard.</span>",
        "They can open every door you can open, and no other door. That is how Copilot reaches your work files.",
        n=N(do="(Hold up your own badge or keycard.)",
            say="Second question: what can Copilot see? Imagine a colleague borrows this card. Which rooms can they enter? Only the rooms I can enter. Keep this card in mind for the next slide.",
            expect="Only the rooms I can enter.")))
    s.append(term("b1t3", "b1", "Block 1 · the idea", "What Copilot <span class=\"hl\">can see.</span>", "Permissions",
        "With a Microsoft 365 Copilot license (the M365 Copilot (Premium) label), Copilot uses <b>only what you can already open</b>. On Copilot Chat (Basic), it uses <b>the web and the files you upload</b>, and you also get Copilot in Outlook. M365 Copilot (Basic) adds Copilot in Word, Excel and PowerPoint.",
        "Like the borrowed keycard…", "…it opens <b>your</b> doors, never more.", "Your access is the limit. The decision about what to share is still yours.",
        n=N(do="(Open the Microsoft 365 home page on the screen and show the label under your name, at the bottom.)",
            say="Copilot works with your permissions. If a folder is closed to you, it is closed to Copilot. Now look at the label under your own name, please. We will read it together on the next slide.",
            expect="A mix of Basic and Premium in most rooms.", fallback="Anyone unsure: open m365.cloud.microsoft and read the label under your name, at the bottom.")))
    s.append(tslide("b1lic", "b1", "Block 1 · your label", "Read the label <span class=\"hl\">under your name.</span>", ["Label", "What Copilot can use", "In this workshop"],
        [["Copilot Chat (Basic)", "The web, files you upload, and Copilot in Outlook", "Every task works with uploaded files"],
         ["M365 Copilot (Basic)", "The web and files you upload, plus standard Copilot in Word, Excel and PowerPoint", "Every task, and most in-app steps"],
         ["M365 Copilot (Premium)", "Your files, emails, chats and meetings (the Microsoft 365 Copilot license)", "Full Copilot in the apps"]],
        "Every task works in Copilot Chat with a file attached.",
        n=N(say="Hands up if your label says Copilot Chat. (Count.) M365 Copilot Basic? Premium? Good news for everyone: every task this week works in Copilot Chat with the file attached. "
                "If you have an M365 label, you can also try the steps inside Word and Outlook.", more=["Source: Microsoft Support, What Copilot license do I have (cheat sheet, Part 4)."])))
    s.append(check("b1chk2", "b1", "Khaled has an M365 Copilot (Premium) label. A folder of salary files is closed to him. <b>Can Copilot use those files for him?</b>",
        [("Yes, if his manager has access to the folder", 0, "No. Copilot never opens a door that is closed to him."),
         ("Yes, if he names the folder in his prompt to Copilot", 0, "Asking does not change his permissions."),
         ("No. It uses only what he can already open", 1, "Right. His permissions are the limit.")],
        n=N(say="Think of the keycard. (Wait for hands.) Asking nicely does not open a locked door, for Khaled or for Copilot.")))
    s.append(live("b1live", "b1", "d11", "The same question, <span class=\"hl\">with and without the policy.</span>",
        "The carry-over question asked twice: once with no file, once with the leave policy attached.", "The number, the deadline, and whether the answer names its section.",
        n=N(say="Now let us test what we just learned. (Ask with no file.) A number, said with full confidence. (Ask with the policy attached.) "
                "Fifteen days, the deadline, and a section number I can open in ten seconds. Which of the two would you send to an employee?")))
    s.append(check("b1chk3", "b1", "The second answer was right. <b>What made it easy to check?</b>",
        [("It named its source: the policy section", 1, "Right. You open section 4 and confirm in seconds."),
         ("It was longer and more detailed", 0, "Length proves nothing."),
         ("It used formal HR words", 0, "Formal words sound right. They prove nothing.")],
        n=N(say="One more quick check before you try it yourself. (Tap the answer.) A section number turns a guess into something you can check.")))
    s.append(task("b1task", "b1", "t11", n=N(say="Your turn, in pairs. This answer was written by Copilot and it reads very well. Your job is to find what is wrong, by hand, with the policy open. "
                                                "No AI until you have checked. Twelve minutes. (Start the timer.)")))
    s.append(rule("b1deb", "b1", "Block 1 · debrief", "Fluent is <span class=\"hl\">not the same as correct.</span>",
        "Every statement in that answer sounded certain. Only the policy could tell the right ones from the wrong ones.",
        n=N(do="(Ask two pairs for one mistake each and the section that fixes it.)", expect="Carry-over, emergency leave and notice.",
            say="The answer had three wrong numbers in perfect English. An employee who got it would plan their leave on the wrong rules, and nobody would notice until too late. A confident tone tells you nothing about whether a number is right.")))
    s.append(cards3("b1groups", "b1", "Block 1 · three groups", "Sort the task <span class=\"hl\">before you type.</span>",
        [(a, b, c, "") for a, b, c in C.GROUPS], "Grades, pay, ratings, discipline and selection stay with authorized HR staff.",
        n=N(say="Last idea of this block: where Copilot's role stops. Every HR task falls into one of these three groups. "
                "Give me one task from your own unit for each group. (Take one example per group.)",
            expect="Job descriptions and recaps go to drafts; grades stay with people.", silent="Give your own example for each group.")))
    s.append(term("b1t4", "b1", "Block 1 · the idea", "Some decisions <span class=\"hl\">stay with people.</span>", "Human decision",
        "A decision that changes a person's pay, grade, rating, record or job is made by <b>authorized HR staff</b>. Copilot may prepare the file. It never decides.",
        "Copilot prepares…", "…a person with authority <b>decides</b>.", "Drafts, yes. Decisions about people, no.",
        n=N(say="However good the draft is, the decision about a person belongs to a person with the authority to make it. "
                "Which decisions in your unit change someone's pay or record?", expect="Grades, allowances, warnings, promotions.")))
    s.append(sortslide("b1sort", "b1", "Demo 1.1b · card sort", 'Which group? <span class="hl">Tap a card.</span>', CD.GROUP_SORT, CD.GROUP_LABELS, did="d11b",
        n=N(say="Let us sort eight real HR tasks. I read the card, you call the group, then I tap it. Ready? (Read the first card.)")))
    s.append(check("b1chk4", "b1", "Noura works on next quarter's training. <b>Which step stays with authorized HR staff?</b>",
        [("Approving which employees join a course", 1, "Right. A choice about a person stays with people."),
         ("Booking the training room for the course", 0, "A booking is not a decision about a person."),
         ("Checking course dates against the training calendar", 0, "Copilot can help. A person checks it.")],
        n=N(say="One for the L&D people in the room. (Wait for hands, then tap.) Choosing people is a decision about people.")))
    s.append(rule("b1files", "b1", "Block 1 · today's rule", "Today: <span class=\"hl\">practice files only.</span>",
        "Tomorrow morning we learn exactly what may go into a prompt. Until then, use only the Mutla files and your own drafting. No names, salaries or cases from work.",
        n=N(time="10:26-10:30", say="One rule for today, before we start writing. We learn how to protect employee data first thing tomorrow. "
              "Until then, please practice on the fictional company's files and on your own writing. Nothing from a real employee. Break now: fifteen minutes. (Press the cup button.)")))
    # Block 2 · Writing a clear prompt
    s.append(story("b2story", "b2", "Block 2 · Writing a clear prompt", "Monday 9 November, 10:45",
        "Fatma types one line: <b>“Remind staff about carrying over leave.”</b> The email says staff can carry over <b>30 days</b>, gives no deadline, and promises extensions.",
        "One line in. <span class=\"hl\">Three problems out.</span>", "Write a request with the prompt checklist.",
        n=N(time="10:45-11:35", say="Welcome back. You now know why Copilot guesses. This block is about how to stop it guessing. (Read the story.) "
              "Three problems from one line. Who has sent a one-line request like this?", expect="Most hands go up.")))
    s.append(rule("b2an", "b2", "Block 2 · the picture", "Brief Copilot like <span class=\"hl\">a new colleague.</span>",
        "On their first day, a new colleague needs the background, the job, the facts, the limits, and what the result should look like.",
        n=N(say="Think about a new colleague on their first morning. You would never say only “write a reminder” and walk away. "
                "You would brief them. What would you tell them? (Collect answers.) Everything you just said has a place in a request.",
            expect="What to do, who it is for, which file, how it should look.")))
    s.append(tslide("b2check", "b2", "Block 2 · the prompt checklist", "Five parts <span class=\"hl\">before you press Send.</span>", ["Part", "It tells Copilot", "Example"],
        [[f"<b>{a}</b>", b, c] for a, b, c in D.CHECKLIST], D.PARTS_LINE + ".",
        n=N(time="12 min", say="Here is the whole checklist: five parts. Each one answers a question Copilot would otherwise guess: who is asking and why, what to do, with which facts, within which limits, and what the result looks like. "
                "(Go row by row and ask the room for a second example of each.) Any order works, as long as nothing is missing.",
            expect="Constraints and Format are the parts people leave out.")))
    s.append(term("b2t1", "b2", "Block 2 · the part people forget", "Constraints: <span class=\"hl\">the limits.</span>", "Constraints",
        "The <b>limits</b> Copilot must keep: use only these files, add no grade, change no date, stay under one page.",
        "Without constraints…", "…Copilot <b>fills the gaps</b> with likely words.", "Write what it must not add, change or guess.",
        n=N(say="If you remember one part from this block, make it this one. Constraints are the fence. Without a fence, Copilot fills every gap with the most likely words, "
                "and in HR the most likely words are often someone else's policy.")))
    s.append(live("b2live", "b2", "d12", "Five short parts, <span class=\"hl\">typed live.</span>",
        "A reminder to all staff about carrying over leave, built one part at a time.", "The number and the date in the email. Do they match section 4?",
        n=N(say="Now I will fix Fatma's request, live, one part at a time. Tell me what to type for each part. (Type each part as the room suggests it, then send.) "
                "Read the email with me. It has fifteen days and the deadline, and nothing is invented. Fatma used the same tool with a one-line brief.")))
    s.append(check("b2chk", "b2", "Copilot's email adds a rule from section 3 that you did not ask for. <b>Which part of the checklist would stop it?</b>",
        [("Format: friendly and clear", 0, "Format sets how it looks and sounds. It does not limit what goes in."),
         ("Constraints: use only section 4", 1, "Right. Constraints set the limits."),
         ("Context: you are a Personnel officer", 0, "Context gives the background. It sets no limits.")],
        n=N(say="Quick check on the fence. (Wait for hands, then tap.) Exactly: constraints.")))
    s.append(task("b2task", "b2", "t12", n=N(say="Your turn. Here are five weak requests, one from each HR unit. Choose two: one from your own unit, plus any other. "
                                                 "Give each of them all five parts. Then swap: can your neighbor tell what Copilot will produce? Fourteen minutes. "
                                                 "If you are stuck, the Day 1 lab page has hints. (Start the timer.)")))
    s.append(rule("b2deb", "b2", "Block 2 · debrief", "A full brief works better <span class=\"hl\">than one clever sentence.</span>",
        "The best rewrites in the room were plain. Each line answered a question Copilot would otherwise guess.",
        n=N(do="(Ask two people to read a rewrite aloud. Ask the room which part is strongest and which is missing.)",
            say="The strongest rewrites used plain words, and every part had a job. Lunch now, and Dhuhr. We start again at 12:15 sharp.",
            expect="Most rewrites miss constraints or the output format at first.")))
    # Block 3 · Draft, fix and check in Word
    s.append(story("b3story", "b3", "Block 3 · Draft, fix and check in Word", "Wednesday 11 November, 12:15",
        "Hessa's checklist draft looks perfect. Then she reads it twice: <b>“Manages a team of six analysts.”</b> and <b>“Grade 8.”</b> Neither is in the role information. And it is two pages.",
        "A good draft <span class=\"hl\">still needs fixing.</span>", "Fix a draft with follow-up instructions, and ask for the source of every line.",
        n=N(time="12:15-13:20", say="Welcome back. Even a good request gives you a draft, not a final document. (Read the story.) "
              "What would most people do now? (Pause.) They delete everything and start again. Today we learn a faster way.",
            expect="Start again, or fix it by hand.")))
    s.append(term("b3t1", "b3", "Block 3 · the idea", "Fix it. <span class=\"hl\">Do not start again.</span>", "Follow-up instruction",
        "A short message in the <b>same chat</b> that names one problem, says how to fix it, and says what must not change.",
        "“Make it better.”", "“Add the missing duty, word for word. Change nothing else.”", "Name the problem. Name what to keep.",
        n=N(say="A follow-up is a short message in the same chat. Compare the two on the slide. The first one gives Copilot nothing. "
                "The second names the problem, says how to fix it, and protects everything that was already right.")))
    s.append(cards3("b3fu", "b3", "Block 3 · three follow-ups", "Three follow-ups <span class=\"hl\">you will use every week.</span>",
        [("Fix what is missing", "Add or correct one thing", "Add the missing duty, word for word.", ""), ("Fix the shape", "Length, order, format", "One page. Keep every duty.", ""),
         ("Show the guesses", "Ask what it assumed", "List every assumption that is not in the files.", "")],
        "One problem per follow-up.",
        n=N(say="These three cover most of what goes wrong. The third one is my favorite: you ask Copilot to confess its guesses. "
                "Anything it assumed is something you check or delete.", silent="Ask: which of the three would fix Hessa's two pages?")))
    s.append(live("b3live1", "b3", "d13", "One draft, <span class=\"hl\">three follow-ups.</span>",
        f"The job description for the {R['title']}, then three short follow-ups in the same chat.", "What changes after each follow-up, and what stays the same.",
        n=N(say="(Run the request, then read the draft aloud.) Now I name one problem at a time. (Send each follow-up.) "
                "Look: the duty is added, the length is right, and everything else stayed where it was. That took three short messages, and I did not start again.")))
    s.append(rule("b3an", "b3", "Block 3 · the picture", "An auditor ticks <span class=\"hl\">every line against a receipt.</span>",
        "A line with no receipt is not paid. A line in a draft with no source is not sent.",
        n=N(say="Follow-ups fix what you can see. But how do you find a problem you cannot see? Think of an auditor with a pile of expense claims. "
                "What happens to a claim with no receipt?", expect="Rejected, or the auditor asks for proof.")))
    s.append(term("b3t2", "b3", "Block 3 · the idea", "Ask Copilot <span class=\"hl\">to show its receipts.</span>", "Source trace",
        "A table where <b>every line of the draft</b> shows the line of the source it came from, or says <b>NOT IN SOURCE</b>.",
        "Like the auditor's receipts…", "…every line has its source, or it goes.", "No source, no line.",
        n=N(say="We ask Copilot to do the auditor's job for us: next to each line of the draft, the matching line from the role sheet. "
                "When there is no source, it must say so in capital letters. Then you decide.")))
    s.append(cards3("b3fail", "b3", "Block 3 · three ways a draft fails", "Three failures <span class=\"hl\">to look for.</span>",
        [("Unsupported claim", "A line with no source", "“Manages a team of six.”", ""), ("Missing information", "A source line left out", "A duty from the role sheet is gone.", ""),
         ("Confident mistake", "A source line changed", "15 days became 30.", "")],
        "The source trace catches the first. Reading the source catches the other two.",
        n=N(say="Three failures to hunt for. The source trace finds the first one for you. For the other two, you open the source and read it yourself, so the last step is always yours.")))
    s.append(live("b3live2", "b3", "d13b", "Every line, <span class=\"hl\">with its source.</span>",
        "A finished-looking draft, checked line by line against the role sheet.", "The NOT IN SOURCE lines. Then the role sheet, to prove they are not there.",
        n=N(say="(Run the source trace.) Two lines come back with no source: the team of six and the grade. (Open the role sheet.) "
                "I do not trust Copilot on this either: I check the role sheet myself. They are not there, so I delete them.")))
    s.append(check("b3chk", "b3", "The source trace marks one duty <b>NOT IN SOURCE</b>. What now?",
        [("Delete it, or check it with the owner", 1, "Right. No source, no line."),
         ("Keep it, because it sounds right for the role", 0, "Sounding right is how hallucinations look."),
         ("Ask Copilot if it is sure", 0, "It may say yes again. The role sheet decides.")],
        n=N(say="Quick check. (Tap after hands.) Sounding right is exactly what a hallucination looks like.")))
    s.append(task("b3task", "b3", "t13", n=N(say="Your turn, with your own unit's role. Write your own request: all five parts, both files attached. Fix the draft with two follow-ups. "
                                                 "Then run the source trace and check by hand. Twenty-two minutes. Hints are on the Day 1 lab page. (Start the timer.)")))
    s.append(check("b3chk2", "b3", "Your draft still ends with <b>“Grade 7”</b>. What do you do?",
        [("Keep it, since Copilot used the template", 0, "The template says the grade stays blank."),
         ("Change it to the grade you think is right", 0, "That is still a decision for the committee."),
         ("Delete it; the grade is the committee's", 1, "Right. The committee sets grades.")],
        n=N(say="Before the next task, one check. (Tap after hands.) Even your own best guess is still a guess about a grade.")))
    s.append(task("b3task2", "b3", "t14", n=N(say="Same method, a different document. Three employees asked for experience letters. Do Ali's. "
                                                  "Write your request, then ask Copilot to flag, not fix, anything that breaks the rules. You decide what goes in the letter. Fifteen minutes. (Start the timer.)")))
    s.append(rule("b3deb", "b3", "Block 3 · debrief", "The record decides the dates. <span class=\"hl\">You decide the letter.</span>",
        "Copilot found the problems in Ali's request in seconds. Deciding what goes into the letter was still your job.",
        n=N(do="(Ask one person what Copilot flagged in Ali's request, and what they did about it.)", expect="The 2014 start date and the “best technician” line.",
            say="Two documents, one method: draft with the checklist, fix with follow-ups, check every line. Break now. (Press the cup button.)")))
    # Block 4 · From policy to people: Word, then Outlook
    s.append(story("b4story", "b4", "Block 4 · From policy to people", "Thursday 12 November, 13:35",
        "The Allowances Policy version 4 is approved. By lunch, Abdulaziz has <b>14 emails</b> from staff asking what it means for them. Yousef wants a one-page summary for staff today, and an announcement after that.",
        "One policy. <span class=\"hl\">Hundreds of readers.</span>", "Summarize a policy you can check, then write one message for three readers.",
        n=N(time="13:35-14:40", say="Last block of the day: from a policy to the people who live with it. (Read the story.) "
              "Fourteen emails by lunch. Who in this room answers the same policy question again and again?", expect="Several hands.")))
    s.append(term("b4t1", "b4", "Block 4 · the idea", "A summary <span class=\"hl\">you can check.</span>", "Summary with sections",
        "Every point names <b>the section it came from</b>, keeps every number as written, and says from when the rule applies.",
        "A summary with no sections…", "…is <b>a rumor</b> nobody can check.", "Section, number, date. Then check two numbers yourself.",
        n=N(say="A summary goes to people who will never open the policy. So it must carry its own proof: the section for every point. "
                "And one thing people forget: the date from which the rule applies.")))
    s.append(live("b4live1", "b4", "d15", "The leave policy, <span class=\"hl\">for new joiners.</span>",
        "Eight bullets for new joiners, each with its section.", "Two numbers I check by hand, live, against the policy.",
        n=N(say="(Run the request.) Every bullet has its section. Now watch me do the part Copilot cannot do for me. (Open the policy, check two numbers aloud.) "
                "A person has checked two numbers, so now the summary can go out.")))
    s.append(task("b4task1", "b4", "t15", n=N(say="Your turn. Write your own request for a one-page summary of the allowances policy, for staff. "
                                                  "Then check three numbers by hand, and find the date this version starts. Fifteen minutes. (Start the timer.)")))
    s.append(check("b4chk", "b4", f"Your summary says the housing maximum is <b>KWD {D.ALLOW['housing_v4']}</b>. Version 4 starts on {D.ALLOW_V4_DATE}. <b>What else must it say?</b>",
        [("That version 3 applies until then", 1, "Right. Staff need today's rule and the date of the change."),
         (f"Nothing: KWD {D.ALLOW['housing_v4']} is in the policy", 0, f"It is, from a future date. Today the maximum is KWD {D.ALLOW['housing_v3']}."),
         ("That the amount may change again", 0, "That is a guess, not a fact from the policy.")],
        n=N(say="Who found the date? (Tap after hands.) A summary with the right number and no date can still mislead every reader.")))
    s.append(term("b4t2", "b4", "Block 4 · tone", "Turn the tone dial. <span class=\"hl\">Keep the facts.</span>", "Tone dial",
        "The same facts written for <b>employees, line managers or senior leadership</b>. You name the facts that must not change.",
        "“Make it friendlier.”", "“Rewrite it for managers; keep every date and rule.”", "The reader changes the order and the voice, never the facts.",
        n=N(time="14:03", say="Now Outlook. The same facts often go to three different readers: staff, their managers, and senior leadership. "
              "Each needs a different order and a different voice. Nobody gets different facts.")))
    s.append(live("b4live2", "b4", "d16", "One reminder, <span class=\"hl\">three readers.</span>",
        "The carry-over reminder from Demo 1.2, rewritten for line managers and for senior leadership.", "The number and the date. They must be the same in every version.",
        n=N(say="(Go back to the chat from Demo 1.2 and send the tone request.) Read the version for managers: it tells them what to do. The one for leadership is three lines. "
                "(Point to the number and the date in each.) The number and the date did not move.")))
    s.append(task("b4task2", "b4", "t16", n=N(say="Your turn. A real thread: thirty messages about new attendance rules. First find the decisions. "
                                                  "Then write the announcement for staff, a version for managers and three lines for leadership, and a reply to Mubarak. Seventeen minutes. (Start the timer.)")))
    s.append(check("b4chk2", "b4", f"Message 3 proposes {D.ATT['old_start']}. Message 24 approves {D.ATT['start']}. <b>Which date goes in the announcement?</b>",
        [(D.ATT["start"], 1, "Right. The later, approved decision stands."),
         (D.ATT["old_start"], 0, "That was a proposal. A later message replaced it."),
         ("Both, so staff can choose", 0, "Two dates confuse everyone. Use the approved one.")],
        n=N(say="Which date did you use? (Tap after hands.) A thread holds old decisions too. The approved one wins.")))
    s.append(check("b4chk3", "b4", "Fatma rewrites the staff announcement <b>for line managers</b>. What changes?",
        [("The start date, because managers need more notice", 0, "The facts stay the same for every reader."),
         ("What managers must do, such as approving permissions", 1, "Right. The reader changes the focus, not the facts."),
         ("The number of permissions, so managers can plan", 0, "A rule does not change with the reader.")],
        n=N(say="And for managers, what changed in your version? (Tap after hands.) The focus moves to what they must do. The rules stay.")))
    s.append(rule("b4deb", "b4", "Block 4 · debrief", "Change the tone, <span class=\"hl\">keep the rules.</span>",
        "Read each version once for tone, and once for every date, time and rule. Two readings, two different checks.",
        n=N(do="(Ask two people to read their reply to Mubarak.)", expect="One reply promises an exception: discuss why it should not.",
            say="Did anyone promise Mubarak an exception? It is easy to do when you are trying to be kind, but HR cannot promise what the rules do not allow.")))
    # Prompt Bank and wrap
    s.append(listslide("b5bank", "b5", "Prompt Bank", "A request you checked <span class=\"hl\">is worth saving.</span>",
        ["<b>Task:</b> what it is for, in one line.", "<b>Request:</b> the five parts, with [brackets] for what changes each time.", "<b>Files:</b> which approved files it needs.", "<b>Check:</b> how you check the result."],
        "Tomorrow you start from your bank, not from a blank page.",
        n=N(time="14:40-15:00", say="You wrote some excellent requests today. Do not lose them. Your Prompt Bank is a Word file with four columns. "
              "Put brackets where the details change, so next month you only fill in the brackets.")))
    s.append(timer_slide("b5go", "b5", "Prompt Bank · 8 minutes", "Save two entries, <span class=\"hl\">then read one to a neighbor.</span>",
        f"Fill two entries in {CD.F['bank']}: your job description request and your announcement request. Then read one to the person next to you.", 8,
        n=N(say="Eight minutes. Save your two best requests from today. Then read one aloud to your neighbor: could they use it without asking you anything? (Start the timer.)",
            expect="Most entries miss the Check column at first.")))
    s.append(listslide("b5seats", "b5", "Where Copilot sits", "One checklist, <span class=\"hl\">many seats.</span>",
        ["<b>Copilot Chat:</b> ask, upload a file, draft. Works on every label.", "<b>Copilot in Word and Outlook:</b> the same engine, inside the app you already use. Excel and PowerPoint tomorrow.",
         "<b>Agent Builder:</b> an agent with your instructions and approved files (Day 3).", "<b>Power Automate:</b> a flow that runs on its own when something happens (a Day 3 demo)."],
        "The request matters more than the seat.",
        n=N(say="Now that you have used it, here is the map of where Copilot lives. Today: Chat, Word and Outlook. Tomorrow: Excel and PowerPoint. "
                "On Thursday you build an agent, and I show you Power Automate. The checklist works in all of them.")))
    s.append(tslide("b5gcse", "b5", "Microsoft's words", "The same idea, <span class=\"hl\">in Microsoft's words.</span>", ["Microsoft says", "Our checklist"],
        [[a, b] for a, b in D.GCSE], "Use whichever words you remember. Give Copilot all of it.",
        n=N(say="If you read Microsoft's own guidance, you will see four words: goal, context, source, expectations. Same idea, grouped differently. Use whichever you remember.")))
    s.append(wrap("w1", "close", "Ask clearly, check everything: <span class=\"hl\">the habit for every HR draft.</span>",
        [(1, "You built", "A checked job description, an experience letter, a policy summary and one announcement for three readers."), (2, "You found", "Three wrong numbers, two lines with no source, and a date that changed."), (3, "The habit", "Copilot drafts. You check. Authorized HR staff decide.")],
        "Tomorrow: safe data first, then meetings, Outlook follow-ups, Excel, Word and PowerPoint.",
        n=N(say="Look at what you made today. (Read the three cards.) Tomorrow starts with what you may and may not put into Copilot. Then you use it on meetings, figures and slides.")))
    return s

# ------------------------------------------------------------------ Day 2 · Meetings, Reporting and Mapping Your HR Workflow
def day2():
    s = opening(2)
    s.append(rule("c0rule", "c0", "Callback · Day 1", "A full brief in, <span class=\"hl\">a source for every line out.</span>",
        "Yesterday you wrote with the checklist, fixed drafts with follow-ups and traced lines to their source. Three quick questions, then today.",
        n=N(time="09:00-09:10", do="(Ask for hands.) Who used Copilot at work after yesterday's session?",
            say="Good morning. Before anything new, three questions on yesterday. Answer with your hands, and do not look at your notes.", expect="One or two hands.")))
    s.append(check("c0chk1", "c0", "Copilot's job description adds <b>a team of six</b> that is not in the role information. <b>Which part of the checklist was weak?</b>",
        [("Format: it should sound more formal", 0, "Format changes how it sounds. It does not stop additions."),
         ("Constraints: add no duty or team size", 1, "Right. Constraints say what it must not add."),
         ("Context: you are an HR officer", 0, "Context gives the background. It sets no limits.")],
        n=N(say="First one. (Wait for hands, then tap.) The fence again: constraints.")))
    s.append(check("c0chk2", "c0", "The draft is good but runs to two pages. <b>What do you send next?</b>",
        [("The same request again, in a new chat", 0, "Starting again throws away what was right."),
         ("“One page. Keep every duty. Change nothing else.”", 1, "Right. Name the problem and what to keep."),
         ("“Make it better and shorter.”", 0, "Copilot cannot tell what “better” means here.")],
        n=N(say="Second one. (Tap after hands.) A follow-up names one problem and protects the rest.")))
    s.append(check("c0chk3", "c0", "A source trace marks a line <b>NOT IN SOURCE</b>. <b>What do you do?</b>",
        [("Keep it if it fits the template", 0, "Fitting the template does not make it true."),
         ("Ask Copilot whether it is sure", 0, "The source decides, not Copilot."),
         ("Delete it, or check it with the owner", 1, "Right. No source, no line.")],
        n=N(say="Last one. (Tap after hands.) Good. Today starts with the question we left open yesterday: what may go into a prompt at all?")))
    s.append(tslide("c0old", "c0", "Callback · the old way and the AI way", "The same HR work, <span class=\"hl\">done the AI way.</span>", ["HR job", "Today", "With Copilot", "When"],
        [["Job descriptions", "Copy last year's and edit by hand", "Draft from the template and role sheet, then trace every line", "Day 1"],
         ["Policy questions", "Staff email HR; HR answers each one", "An agent answers with the section; HR handles the cases", "Days 1 and 3"],
         ["Meetings", "Notes that nobody sends", "A recap with owners and dates, sent the same day", "Day 2"],
         ["Payroll checks", "Compare two months by eye", "Copilot lists each change; a person confirms why", "Day 2"],
         ["Onboarding", "New joiners email the same questions", "An onboarding agent answers from the checklist", "Day 3"],
         ["Training requests", "Printed, signed, scanned, typed twice", "Mapped, then improved step by step", "Day 3"]],
        "Copilot takes the drafting and checking steps. Decisions stay with HR.",
        n=N(time="3 min", say="Before we start, one slide that connects the three days. Each row is HR work you already do. The middle column is how most teams do it today. "
              "(Point to two rows.) Which row is closest to your own job? (Take two answers.)", expect="Policy questions and meetings, most often.")))
    # Block 1 · Protecting employee data
    s.append(story("c1story", "c1", "Block 1 · Protecting employee data", "Tuesday 10 November, 09:10",
        "A line manager emails HR a case note about a technician. Fatma wants a neat summary for the file. She is about to paste the whole note into Copilot: <b>two names, a civil ID, a mobile number, a salary and a medical reason.</b>",
        "The summary would be fine. <span class=\"hl\">The prompt is not.</span>", "Sort every task as green, amber or red, and redact a note before Copilot sees it.",
        n=N(time="09:10-09:45", say="Yesterday I asked you to use practice files only. Today you learn why, and what to do with real work. (Read the story.) "
              "Stop Fatma. What should she do before she presses Send? Call it out.", expect="Remove the names. Do not use Copilot. Ask IT.")))
    s.append(rule("c1an", "c1", "Block 1 · the picture", "A traffic light <span class=\"hl\">before every prompt.</span>",
        "Green: go ahead. Amber: only in your company's approved account, with names removed. Red: stop. It never goes into a prompt.",
        n=N(say="Think of a traffic light at a junction. You do not decide at the last second; you look at the light first. "
                "We do the same with every task, before we type a single word. Let us see what makes a task green, amber or red.")))
    s.append(cards3("c1safe", "c1", "Block 1 · green, amber, red", "Look at the light <span class=\"hl\">before you type.</span>",
        [(t, d, "; ".join(x), "") for _k, t, d, x in C.SAFE], "When you are not sure, treat it as red and ask.",
        n=N(time="5 min", say="Here are the three lights. (Read one example from each card.) Notice amber: it depends on your company. "
                "If your company has not approved a Copilot account for HR work, every amber task becomes red. Your company's policy always comes first.",
            silent="Ask: which light is a salary list with names?")))
    s.append(sortslide("c1sort", "c1", "Demo 2.1 · card sort", 'Green, amber or red? <span class="hl">Tap a card.</span>', C.SORT, C.SORT_LABELS, did="d21",
        n=N(say="Eight tasks from real HR work. I read each card, you call the color, then I tap it. If the room disagrees, we stop and talk about it. (Read the first card.)")))
    s.append(term("c1t1", "c1", "Block 1 · the idea", "Redact first. <span class=\"hl\">Then ask.</span>", "Redaction",
        "Replacing names with roles, and removing IDs, phone numbers, salaries and medical details, <b>before</b> a document goes anywhere near a prompt.",
        "A note about Bader and Sara…", "…becomes a note about <b>Employee A and Colleague B</b>.", "Redaction happens before the prompt, not inside it.",
        n=N(say="Redaction is the skill that turns many red tasks into amber ones. You remove who the person is, and you keep what happened. "
                "One warning: asking Copilot to keep a secret does not protect anything. The protection is what you never typed.")))
    s.append(check("c1chk1", "c1", "Your company has an approved Copilot account. A manager asks you to summarize a grievance letter that names two employees. <b>What first?</b>",
        [("Paste it as it is: the account is approved", 0, "An approved account still gets the minimum data."),
         ("Replace the names and IDs, then use the approved account", 1, "Right. Redact first, then the approved account."),
         ("Use your personal Copilot at home tonight", 0, "Never. Work data stays in the approved account.")],
        n=N(say="Quick check. (Wait for hands, then tap.) Approved account and redaction: you need both.")))
    s.append(live("c1live", "c1", "d21b", "Redact first. <span class=\"hl\">Then ask.</span>",
        "A case note redacted on the trainer screen, then a summary request that holds only the redacted text.", "Whether the summary guesses anything that was removed.",
        n=N(say="(Show the original note on your own screen only.) I am not pasting this anywhere. (Redact it aloud: names, ID, phone, salary, medical reason.) "
                "Now Copilot sees only roles and facts. (Run the request.) Read the summary with me. Did it invent a reason for the absence? It should not, and if it does, we delete it.")))
    s.append(task("c1task", "c1", "t21", n=N(say="Your turn. The same kind of note, on your own laptop, in Word. You redact by hand: no Copilot until nothing sensitive is left. "
                                                "Eleven minutes. (Start the timer.)")))
    s.append(rule("c1deb", "c1", "Block 1 · debrief", "Six details out. <span class=\"hl\">The case is still clear.</span>",
        "Redaction removed who the people are, not what happened. A summary of the redacted note is just as useful to the file.",
        n=N(do="(Ask one person which item was hardest to spot.)", expect="The salary or the medical reason, because they sit inside a sentence.",
            say="The easy ones are the names. The dangerous ones hide inside a sentence, like a salary in brackets. Read every sentence, not only the headings.")))
    # Block 2 · Before and after the meeting
    s.append(story("c2story", "c2", "Block 2 · Before and after the meeting", "Tuesday 3 November, 11:30",
        "The orientation planning meeting ends. Personnel, IT and L&D agreed on a lot. A week later, IT asks: <b>who said 18 laptops, and by when?</b> Nobody wrote it down.",
        "A good meeting. <span class=\"hl\">No actions.</span>", "Prepare a meeting with Copilot, then turn notes into actions with owners and deadlines.",
        n=N(time="09:45-10:45", say="Block 2 is about meetings: the page before, and the page after. (Read the story.) "
              "Be honest: how many of your meetings last month ended with a written list of who does what by when?", expect="A few hands, some laughter.")))
    s.append(tslide("c2when", "c2", "Block 2 · before, during, after", "Copilot drafts <span class=\"hl\">the page around the meeting.</span>", ["When", "Copilot drafts", "You check"],
        [["Before", "An agenda, a background brief, discussion points", "Every fact comes from an approved file"],
         ["During", "Answers about the meeting so far (Teams, Premium, transcribed)", "Ask before you record; follow your policy"],
         ["After", "Decisions, actions with owner and deadline, open questions", "Nothing is added that nobody agreed"]],
        "The meeting is still yours. Copilot writes the pages around it.",
        n=N(time="6 min", say="Three moments. Before the meeting, Copilot can prepare the paper. After it, Copilot can turn notes or a transcript into actions. "
                "During the meeting, Copilot in Teams needs a Premium label and a transcript, so most of us will paste the notes or the exported transcript into Copilot Chat instead. "
                "The result is the same: you check it.", more=["Copilot in Teams meetings needs the M365 Copilot (Premium) label and transcription switched on. Everyone else: Copilot Chat with the transcript or notes."])))
    s.append(live("c2live1", "c2", "d22", "Agenda, brief <span class=\"hl\">and discussion points.</span>",
        "A 30-minute planning meeting for new joiners, prepared from five approved facts.", "Whether the minutes add up, and where the open question went.",
        n=N(say="(Paste and run the request.) Three pieces in under a minute. Now my job. (Add the minutes aloud.) Thirty: good. "
                "(Point to the discussion points.) The open question about Medical Services became something to discuss, not a decision. That is what we asked for.")))
    s.append(task("c2task1", "c2", "t22", n=N(say="Your turn. Your unit track's case file has a meeting coming up. Prepare it: agenda, brief, three discussion points. "
                                                  "Write your own request with the checklist. Fifteen minutes. Hints are on the Day 2 lab page. (Start the timer.)")))
    s.append(term("c2t1", "c2", "Block 2 · the idea", "What, who, <span class=\"hl\">by when.</span>", "Action item",
        "An action has three parts: <b>what</b> will be done, <b>who</b> does it, and <b>by when</b>. An idea that nobody agreed to is not an action.",
        "“Someone will look into the laptops.”", "“Hamad sets up 18 laptop accounts by Wednesday 2 December.”", "Missing an owner or a date? It is not an action yet.",
        n=N(say="After the meeting, everything depends on this. Read the left side: who will look into it? Nobody. Read the right side: one person, one task, one date. "
                "When you check a recap, look for those three parts in every line.")))
    s.append(live("c2live2", "c2", "d23", "Notes into <span class=\"hl\">decisions and actions.</span>",
        "Rough meeting notes turned into decisions, an action table and open questions.", "The idea nobody agreed to. Does it sneak into the action table?",
        n=N(say="(Run the request.) Read the table with me. Four actions, and one of them honestly says: no deadline set. "
                "Now look for the CEO. Somebody had an idea, nobody agreed to it, and it is not in the table. If it were, I would delete it.")))
    s.append(check("c2chk", "c2", "The notes say: <b>“Someone said we could invite the CEO.”</b> Nobody agreed. <b>Where does it go in the recap?</b>",
        [("An action for the chair, due next week", 0, "Nobody agreed to it, so nobody owns it."),
         ("A decision: the CEO is invited", 0, "Nothing was decided."),
         ("Not in the actions or the decisions", 1, "Right. An idea nobody agreed is neither.")],
        n=N(say="Quick check before your turn. (Tap after hands.) A recap records the meeting that happened, not the one we wish had happened.")))
    s.append(task("c2task2", "c2", "t23", n=N(say="Your turn. A real-length transcript: the staffing meeting for a new section. Write your own recap request, then check every owner and deadline against the transcript. "
                                                  "Fifteen minutes. (Start the timer.)")))
    s.append(rule("c2deb", "c2", "Block 2 · debrief", "The open question <span class=\"hl\">stays open.</span>",
        "Two positions could be contract or permanent. Nobody decided. A recap that decides it for the meeting is wrong, however tidy it looks.",
        n=N(do="(Ask two people to read their open questions.)", expect="Some recaps turned the open question into a decision.",
            say="Did anyone's recap say the two positions are contract? Copilot likes to finish things. Your job is to keep what is unfinished, unfinished. Break now. (Press the cup button.)")))
    # Block 3 · Follow-ups and reminders in Outlook
    s.append(story("c3story", "c3", "Block 3 · Follow-ups and reminders", "Thursday 29 October, 13:00",
        "Finance asks where last month's cost estimate is. Abdulaziz thought Khaled was preparing it. The recap was clear, but <b>nobody sent it</b>, and nobody sent a reminder.",
        "A clear recap <span class=\"hl\">that nobody sent.</span>", "Write a follow-up and a polite reminder that keep every owner and date.",
        n=N(time="11:00-11:35", say="Welcome back. (Read the story.) A recap in a folder helps nobody. Today it goes out, and then we remind people before the deadline, not after.")))
    s.append(live("c3live", "c3", "d24", "A follow-up <span class=\"hl\">and a reminder.</span>",
        "The action table from Demo 2.3, turned into a follow-up for everyone and a reminder for one person.", "Every owner and date. Did any of them change?",
        n=N(say="(Go back to the chat from Demo 2.3 and run the request.) Two emails. Read the reminder to Noura: it names the task, gives the date, and says thank you. "
                "No blame, no new task. (Point to each owner and date.) All the same as the table.")))
    s.append(task("c3task1", "c3", "t24", n=N(say="Your turn. Use your recap from the staffing meeting. A follow-up to everyone, then a reminder to Khaled. Twelve minutes. (Start the timer.)")))
    s.append(task("c3task2", "c3", "t25", n=N(say="Second exercise. Back to your unit track's case: someone needs a message from you. Find who, and why, then write it. Ten minutes. (Start the timer.)")))
    s.append(check("c3chk", "c3", "Khaled's deadline was yesterday and the request is still missing. <b>Which line belongs in the reminder?</b>",
        [("“You missed the deadline again. Please hurry.”", 0, "Blame makes people defend, not act."),
         ("“Please send the request today; Finance is waiting.”", 1, "Right. Polite, specific, and the reason."),
         ("“No rush. Send it when you can.”", 0, "It removes the deadline that matters.")],
        n=N(say="One for real life. (Tap after hands.) Polite does not mean vague. Give the task, the day and the reason.")))
    s.append(rule("c3deb", "c3", "Block 3 · debrief", "Polite, specific <span class=\"hl\">and on time.</span>",
        "The best reminders in the room named the task and the date, asked once, and blamed nobody.",
        n=N(do="(Ask one person to read their reminder to Khaled.)", say="Notice what the strong ones have in common: you could not misread them. Lunch and Dhuhr now. We start again at 12:15.")))
    # Block 4 · Excel: figures you can check
    s.append(story("c4story", "c4", "Block 4 · Excel: figures you can check", "Sunday 4 October, 12:15",
        f"Noura sends the Q3 report: <b>{D.TRAIN_ROWS_EXPORT} training requests.</b> The HR system says <b>{D.TRAIN_TRUE}</b>. The Head of L&D asks which number is right, and why.",
        f"{D.TRAIN_ROWS_EXPORT} or {D.TRAIN_TRUE}? <span class=\"hl\">Only a check can tell.</span>", "Ask Copilot about a tracker, see the rows, and check the total against a control figure.",
        n=N(time="12:15-13:00", say="Welcome back. Numbers now. (Read the story.) Hands up if you have ever sent a report and then found the total was wrong. (Pause.) Keep your hand up if you found out from your manager.",
            expect="Several hands, then laughter.")))
    s.append(cards3("c4three", "c4", "Block 4 · three steps", "Ask. See the rows. <span class=\"hl\">Check.</span>",
        [("Ask", "One clear question", "One sheet, one measure, one period.", ""), ("See the rows", "The formula or the rows", "Show the formula, or list what you counted.", ""),
         ("Check", "Against a control total", "Compare with the checked figure from the HR system.", "")],
        "Always check against a reference: a control total, or the list of approved changes.",
        n=N(time="6 min", say="Three steps for any figure. The middle one is the one people skip: ask Copilot to show its work, so you can see the rows behind the number. "
                "Then the last step: a control total, a figure you already trust, from the HR system.",
            more=["Copilot in Excel needs a saved .xlsx workbook in OneDrive or SharePoint and an M365 label. Everyone else: attach the file to Copilot Chat.",
                  "Data > Clean Data (Copilot in Excel) suggests fixes for text written two ways, numbers stored as text and extra spaces. It works best on an Excel table. Source: Microsoft Support, Clean data in Excel."])))
    s.append(live("c4live", "c4", "d26", "Ask the tracker, <span class=\"hl\">then see the rows.</span>",
        "The Q3 training count by unit, the Control totals next to it, then a chart of both.", "The difference between the totals, and where it shows on the chart.",
        n=N(say="(Run the request.) Copilot counts every row, correctly. (Open the Control totals sheet.) And the system says something else. "
                "Copilot did not make a mistake here. The rows did. (Run the chart request.) Look: every unit is a little too high, not one unit. Which kind of problem does that? (Point to the axis: it starts at zero, so the bars do not exaggerate.)", expect="Duplicates.")))
    s.append(task("c4task1", "c4", "t26", n=N(say="Your turn, in pairs. Find the rows behind the difference with Copilot, then prove it yourself in Excel. Twelve minutes. (Start the timer.)")))
    s.append(task("c4task2", "c4", "t27", n=N(say="Second exercise, same pairs, and you choose. A: payroll for October and November, checked against the list of approved changes, employee codes only. "
                "B: an overtime export nobody has cleaned. You clean it, chart it and check it against the approved hours. Twelve minutes. (Start the timer.)",
                                                  more=["A: comparing the months finds only one problem. The leaver and the missing joiner show up only against the Movements sheet.",
                                                        "B: a chart with more than five bars means a unit is still written two ways. Two units stay above the approved hours after cleaning."])))
    s.append(check("c4chk", "c4", "Copilot finds that one employee's basic salary rose by KWD 200, and <b>no approved change explains it</b>. <b>What do you do?</b>",
        [("Set it back to last month's salary", 0, "You do not know the reason yet. There may be a late approval."),
         ("Ask Compensation to confirm the reason before the bank file goes", 1, "Right. Copilot finds it; a person confirms it."),
         ("Accept it, because the total adds up", 0, "A total can add up and still pay the wrong person.")],
        n=N(say="(Tap after hands.) Copilot is good at finding the question. A person answers it.")))
    s.append(rule("c4deb", "c4", "Block 4 · debrief", "Copilot finds the change. <span class=\"hl\">A person confirms the reason.</span>",
        "Every check needed a reference: a control total, the approved changes, or the approved hours. Without one, a correct count of wrong rows looks perfect, and a missing joiner looks like nothing at all.",
        n=N(do="(Ask each pair for one sentence: what was wrong, and how they found it.)",
            say="Two points from this block. First, the payroll system calculates salaries; Copilot should never recalculate them. It is a second pair of eyes before the file goes to the bank. "
                "Second, a fixed rule, like flag any change above a set amount, catches big numbers. Copilot can also say which change has no approved reason behind it, and ask why.")))
    # Block 5 · Word summaries
    s.append(term("c5t1", "c5", "Block 5 · the idea", "Three lines <span class=\"hl\">a manager reads.</span>", "Management summary",
        "A short note that puts <b>the finding, its limits and the next step</b> first, with every number as written in the source.",
        "Every detail you found…", "…cut to what a manager must <b>know or decide</b>.", "Finding, limits, next step.",
        n=N(time="13:00-13:35", say="You found two wrong figures. That is only useful if someone reads it. Managers read the first three lines and stop. "
                "So we put the finding, what it does not show, and the next step right at the top.")))
    s.append(live("c5live1", "c5", "d28", "A finding into <span class=\"hl\">a note for management.</span>",
        "The attendance pilot result as a title and three bullets for the Head of HR. Then one bullet, rewritten in Word.", "The line that says what the pilot does not show, and whether Rewrite changed a number.",
        n=N(say="(Run the request.) Three bullets. The second one is the one I like: one division, eight weeks. A result with its limits is a result people can trust. "
                "(Check the percentage in the brief.) Same as the source. (In Word, select the second bullet, then Copilot, Rewrite.) Three versions. I keep one only if the numbers did not move.")))
    s.append(task("c5task1", "c5", "t28", n=N(say="Your turn. What you found before lunch now goes to the person who signs the report. Write it short. Twelve minutes. (Start the timer.)")))
    s.append(task("c5task2", "c5", "t29", n=N(say="Second exercise, and you choose. A: your summary as three lines for the team channel. "
                "B: a supervisor's long memo, rewritten for staff. C: a three-page report, summarized for the HR Director. Ten minutes. (Start the timer.)",
                more=["B: two numbers in the memo do not match the approved rules in the annex.", "C: a summary with only good news has left out section 8."])))
    s.append(check("c5chk", "c5", "Your three-line update for the HR team channel still names <b>EMP-3346</b>. <b>What do you do?</b>",
        [("Keep it: the channel is inside HR", 0, "A channel is wider than the people who need the code."),
         ("Take the code out; Compensation already has it", 1, "Right. The wider the audience, the less personal detail."),
         ("Add the name too, so it is clearer", 0, "That makes it more personal, not clearer.")],
        n=N(say="(Tap after hands.) The rule from this morning again: the wider the audience, the less personal detail. Break now. (Press the cup button.)")))
    # Block 6 · PowerPoint
    s.append(story("c6story", "c6", "Block 6 · PowerPoint: from document to deck", "Thursday 5 November, 13:50",
        "The Head of HR asks for the attendance update as slides for Sunday's managers' meeting. Noura has the brief in Word. <b>Building ten slides by hand takes her the whole afternoon.</b>",
        "The facts are ready. <span class=\"hl\">The slides are not.</span>", "Build slides from a prompt and from a document, fix a messy deck, and check every number on every slide.",
        n=N(time="13:50-14:50", say="Last block of today, and a tool many of you asked about: PowerPoint. (Read the story.) How long does a ten-slide deck take you today?",
              expect="Two hours, half a day.")))
    s.append(listslide("c6can", "c6", "Block 6 · Copilot in PowerPoint", "What Copilot <span class=\"hl\">can do in PowerPoint.</span>",
        ["<b>Create</b> a deck from a Word file or a request.", "<b>Edit:</b> add a slide, rewrite a slide for a different reader, add speaker notes.",
         "<b>Summarize</b> a long deck someone sent you, slide by slide.", "<b>Without it:</b> ask Copilot Chat for the outline, then paste it into PowerPoint and use Designer for the layout."],
        "Copilot builds the slides. You check every number on every slide.",
        n=N(time="5 min", say="Four things to know. It can build a first deck from a request or from a document, edit it in rounds, and summarize a deck you received. "
                "If your label does not include Copilot in PowerPoint, Copilot Chat writes the outline and you paste it in. The result is the same: a first draft you check.",
            more=["Copilot in PowerPoint needs the M365 Copilot (Basic) or (Premium) label. Everyone else: Copilot Chat for the outline, then Designer in PowerPoint."])))
    s.append(live("c6live1", "c6", "d210", "From a prompt, then <span class=\"hl\">from a document.</span>",
        "Five slides from one line and no file. Then five slides from the policy brief.", "Which deck has times and numbers that are not in the brief.",
        n=N(time="6 min, live", say="(Run the one-line request, no file.) Tidy slides in a minute. Read the start times with me. Where did they come from? Nowhere: Copilot guessed. "
                "(Create the deck from the brief.) Now every time comes from the brief. (Check each time and number against the brief.) A prompt gives you a structure. A document gives you the facts.")))
    s.append(task("c6task1", "c6", "t210", n=N(say="Your turn, the same two ways. First a deck from one line, and you circle what it made up. "
                "Then the deck from your Task 2.8 summary. Check every number on every slide. Fourteen minutes. (Start the timer.)")))
    s.append(live("c6live2", "c6", "d211", "Edit the deck <span class=\"hl\">in rounds.</span>",
        "One request that adds a slide for managers, rewrites a slide in plainer words and adds speaker notes.", "Whether any time or number changed while Copilot edited.",
        n=N(time="6 min, live", say="(Run the edit request on the deck from Demo 2.10.) A new slide, a plainer slide, notes everywhere. "
                "After every round of edits, I check the numbers again, because each round is a new draft.")))
    s.append(task("c6task2", "c6", "t211", n=N(say="Second exercise, and you choose. A: a deck someone made in a hurry, with nine problems in nine slides. Fix it in rounds. "
                "B: your own meeting, from this morning's agenda and brief. Eighteen minutes. (Start the timer.)",
                more=["A: the deck repeats the training slide with two numbers, shows names and salaries, and overstates the pilot.", "Source for the features: Microsoft Support, Create a presentation from a file, and Add speaker notes with Copilot."])))
    s.append(check("c6chk", "c6", f"Slide 3 says Q3 training requests: <b>{D.TRAIN_ROWS_EXPORT}</b>. Your checked summary says <b>{D.TRAIN_TRUE}</b>. <b>What do you do?</b>",
        [("Keep both numbers, with a footnote", 0, "Two numbers confuse the reader."),
         ("Fix the slide to match the checked summary", 1, "Right. The checked figure wins, everywhere."),
         ("Ask Copilot to make a new deck", 0, "A new deck can repeat the same mistake.")],
        n=N(say="(Tap after hands.) The checked figure wins, on every page and every slide.")))
    s.append(rule("c6deb", "c6", "Block 6 · debrief", "Copilot builds the deck. <span class=\"hl\">You check every slide.</span>",
        "The decks that were ready to present had every number from the source, the open question asked on screen, and notes a colleague could present from.",
        n=N(do="(Ask one person to show one slide and its notes.)", say="Look at the speaker notes. If a colleague had to present your deck tomorrow, could they? That is the test.")))
    # Wrap · which app for which job
    s.append(tslide("c8apps", "c8", "Which app for which job", "Five apps. <span class=\"hl\">One habit.</span>", ["HR job", "Where", "Remember"],
        [["Prepare a meeting", "Copilot Chat or Word", "Only approved facts"], ["Recap a meeting", "Teams (Premium) or Chat with the transcript", "What, who, by when"],
         ["Follow up and remind", "Outlook", "Same owners, same dates"], ["Check a figure", "Excel, or Chat with the file", "Against a control total"],
         ["Brief management", "Word", "Finding, limits, next step"], ["Present to managers", "PowerPoint, or Chat for the outline", "Every number matches its source"]],
        "Copilot drafts. You check. Authorized HR staff decide.",
        n=N(time="14:50-15:00", say="Here is today on one slide. Six jobs, the app that fits, and the one check you never skip. "
              "Take a photo if you like; it is also on the cheat sheet. Which row will you use first at work?", expect="Recaps and follow-ups.")))
    s.append(wrap("w2", "close", "Safe data, checked figures, <span class=\"hl\">clear slides.</span>",
        [(1, "You built", "A redacted note, a meeting pack and recap, checked figures and a chart, a summary and two decks."),
         (2, "You found", "Six sensitive details, an idea nobody agreed, duplicate requests, and payroll or overtime items to confirm."),
         (3, "The habit", "Copilot drafts. You check. Authorized HR staff decide.")],
        "Tomorrow: two HR agents, a Power Automate demo, and how to map and improve an HR workflow.",
        n=N(say="Look at what you made today. (Read the three cards.) Tomorrow we build tools that other people can use, and we look at whole HR processes, not single tasks.")))
    return s

# ------------------------------------------------------------------ Day 3 · HR Agents and an Introduction to Power Automate
def day3():
    s = opening(3)
    s.append(rule("e0rule", "e0", "Callback · Day 2", "Safe data, checked figures, <span class=\"hl\">clear slides.</span>",
        "Yesterday you redacted a note, recapped a meeting into actions, checked a training count and a payroll or overtime file, and built two decks. Three questions, then today.",
        n=N(time="09:00-09:10", do="(Ask for hands.) Who used Copilot at work after yesterday?", say="Good morning, and welcome to the last day. Three quick questions on yesterday first.")))
    s.append(check("e0chk1", "e0", "A colleague wants Copilot to check a salary list <b>with every employee's name</b>. <b>What color is it?</b>",
        [("Green: it stays inside HR", 0, "Inside HR is not the test. Named salaries are red."),
         ("Amber: fine in the approved account", 0, "Named salaries never go into a prompt."),
         ("Red: never in a prompt", 1, "Right. Named salaries are red in any account.")],
        n=N(say="(Tap after hands.) Red. If the names come out, the task can change color.")))
    s.append(check("e0chk2", "e0", "Which recap line is <b>ready to send</b>?",
        [("“Action: send the agenda · Noura · by Monday 30 November”", 1, "Right. What, who and by when."),
         ("“Action: someone sends the agenda soon”", 0, "No owner and no date."),
         ("“Action: discuss the agenda again next month”", 0, "That is a meeting, not an action.")],
        n=N(say="(Tap after hands.) What, who, by when.")))
    s.append(check("e0chk3", "e0", "Copilot counts <b>412</b> rows. The control total is <b>398</b>. <b>What do you look for first?</b>",
        [("A missing value in one row", 0, "A missing value makes a total too low."),
         ("Duplicate request IDs", 1, "Right. Too high: look for duplicates."),
         ("A formula error in Copilot's count", 0, "The count was right. The rows were wrong.")],
        n=N(say="(Tap after hands.) Too high, duplicates. Good. Today we stop making one document at a time and start building tools.")))
    # Block 1 · Build an HR agent
    s.append(story("e1story", "e1", "Block 1 · Build an HR agent", "Thursday 12 November, 16:00",
        f"Fatma counts her week: <b>64 emails</b> from staff. Twenty ask how many leave days carry over. She answers each one by hand, from the same section 4.",
        "The same question, <span class=\"hl\">twenty times a week.</span>", "Build an HR agent that answers from approved policies, and test it before anyone uses it.",
        n=N(time="09:10-10:05", say="(Read the story.) Which question does your unit answer again and again? Call it out.", expect="Leave balances, allowances, letters, training dates.")))
    s.append(rule("e1an", "e1", "Block 1 · the picture", "A new colleague with <span class=\"hl\">a binder and a script.</span>",
        "The script says what to answer, what to ask first and what to refer. The binder holds the approved policies. That is an agent.",
        n=N(say="Picture a new colleague at the HR counter. You give them a binder with the approved policies, and a script: answer from the binder, ask first when you need more, "
                "and send anything personal to us. That colleague can answer twenty leave questions a week without you. That is exactly what we build this morning.")))
    s.append(tslide("e1cmp", "e1", "Block 1 · Copilot Chat or an agent", "Write it once. <span class=\"hl\">Use it many times.</span>", ["", "Copilot Chat", "An agent"],
        [["Instructions", "You type them each time", "Written once and saved"], ["Files", "You attach them each time", "Saved as its knowledge"],
         ["Who uses it", "You", "Anyone you share it with"], ["Best for", "One-off drafts", "The same questions, many times"]],
        "Same engine. An agent remembers the instructions and the files.",
        n=N(time="6 min", say="Same engine underneath. The difference is what is saved. In a chat, you bring the instructions and the files every time. "
                "An agent keeps them, so everyone who uses it gets the same rules.", silent="Ask: which of your unit's questions would you put in an agent?")))
    s.append(listslide("e1parts", "e1", "Block 1 · the parts of an agent", "Five parts. <span class=\"hl\">You know four already.</span>",
        ["<b>Name and description:</b> what it is for, in one line.", "<b>Instructions:</b> the five checklist parts, written once.",
         "<b>Knowledge:</b> the approved files it answers from.", "<b>Starter prompts</b> and the <b>test pane:</b> how people start, and how you test it."],
        "An agent answers. It does not send, route or approve.",
        n=N(time="5 min", say="In Microsoft 365 Copilot you choose Create agent, and the Configure tab shows these parts. Instructions are your checklist, nothing new. "
                "Knowledge is the files you have attached all week. One limit to remember: this agent answers questions. Sending, routing and approving need something else, and I show you that after the break.",
            more=["Agent Builder: Microsoft 365 Copilot app, Create agent, Configure tab. Actions that send or update data need Copilot Studio (outside this workshop).",
                  "If Agent Builder is off on some accounts, the fallback is the same instructions pasted into Copilot Chat with the files attached."])))
    s.append(live("e1live", "e1", "d31", "An HR agent, <span class=\"hl\">built live.</span>",
        "The Mutla HR Policy Helper: name, instructions, five policy files and three starter prompts.", "Where each checklist part goes, and the section number in the first answer.",
        n=N(time="8 min, live", say="(Build it step by step, reading each field aloud.) Name. Description. Now the instructions: look, it is the checklist, part by part. "
                "(Upload the five files.) Knowledge. (Add the starter prompts, then ask the first one.) Fifteen days, the deadline and section 4. Our first agent.")))
    s.append(check("e1chk", "e1", "Where does the rule <b>“never give a named person's salary”</b> belong?",
        [("In a starter prompt", 0, "Starter prompts are questions people ask."),
         ("In the Constraints part of the instructions", 1, "Right. Constraints hold the rules that protect people."),
         ("In the agent's description", 0, "The description says what it is for, not its limits.")],
        n=N(say="(Tap after hands.) Constraints. If you remember one thing when you write instructions, write the never-rules there.")))
    s.append(task("e1task1", "e1", "t31", n=N(say="Your turn. Before you open Agent Builder, write the instructions in a document, all five parts. Twelve minutes. (Start the timer.)")))
    s.append(task("e1task2", "e1", "t32", n=N(say="Second exercise: build it. Paste your instructions, upload the five files, add three starter prompts, and ask one normal question. Fifteen minutes. (Start the timer.)",
                                                  fallback="No Agent Builder on an account: paste the instructions into a new Copilot Chat, attach the five files, and test there.")))
    s.append(rule("e1deb", "e1", "Block 1 · debrief", "The instructions are <span class=\"hl\">the agent's job description.</span>",
        "The agents that answered well had clear limits, the dates of both allowances versions, and a place to send what they could not answer.",
        n=N(do="(Ask two people to read their Constraints line aloud.)", expect="Some forgot to say where to refer people.",
            say="Vague instructions give a vague agent. The clear ones in the room said what to answer, what never to answer, and where to send people.")))
    # Block 2 · Test, fix and build a second agent
    s.append(tslide("e2tests", "e2", "Block 2 · three tests", "Three tests <span class=\"hl\">before anyone uses it.</span>", ["Test", "You ask", "It passes when"],
        [["Normal", "A complete, ordinary question", "It answers with the policy and section"], ["Incomplete", "A question that depends on the person", "It asks first, or gives both rules with dates"],
         ["Sensitive", "A named person's pay, or a decision", "It declines and refers to HR"]],
        "Fix one instruction line at a time, then ask again.",
        n=N(time="10:05-10:45", say="An agent you have not tested is a risk you share with everyone who uses it. Three tests, every time. The sensitive one matters most.")))
    s.append(live("e2live", "e2", "d33", "Three tests, <span class=\"hl\">then one fix.</span>",
        "The three test questions in the test pane, one fix to the instructions, and the same question again.", "The answer to the sensitive question, before and after the fix.",
        n=N(say="(Ask the three questions.) Normal: section 4. Incomplete: it asks for the grade. Sensitive: (read the answer). "
                "If it fails, watch me: I change one line in Constraints, not the whole text, and I ask again. One line, one test.")))
    s.append(task("e2task1", "e2", "t33", n=N(say="Your turn. Test your agent three times, keep a short log, and fix one line. Twelve minutes. (Start the timer.)")))
    s.append(task("e2task2", "e2", "t34", n=N(say="Second exercise: a second agent, and you choose which. The coach helps line managers draft job descriptions and never gives a grade. The buddy helps people in their first month. Eighteen minutes. (Start the timer.)")))
    s.append(rule("e2deb", "e2", "Block 2 · debrief", "The second agent <span class=\"hl\">took half the time.</span>",
        "Same checklist, same three tests. Once you know the method, each new agent is quicker to build.",
        n=N(do="(Ask one person what the coach did with the incomplete test.)", expect="It asked for the duties first.",
            say="Did your coach ask for the duties? Did your buddy ask where the new joiner works? If it guessed instead, you know which line to fix. Break now. (Press the cup button.)")))
    # Block 3 · Power Automate: a trainer demo
    s.append(story("e3story", "e3", "Block 3 · Power Automate: a trainer demo", "Sunday 8 November, 08:30",
        "Noura receives 30 training requests a week. Each one is an email, a form, a signature, a scan and two lines typed into a tracker. <b>Nobody asks a question</b>, so an agent cannot help.",
        "Not a question. <span class=\"hl\">A process.</span>", "See what a Power Automate flow does, and when you need one instead of Copilot or an agent.",
        n=N(time="11:00-11:35", say="Welcome back. This block is a demo: you watch, you do not build. (Read the story.) "
              "Copilot waits for someone to type. An agent waits for a question. Who is waiting here?", expect="The form. The manager. Noura.")))
    s.append(term("e3t1", "e3", "Block 3 · the idea", "It starts <span class=\"hl\">by itself.</span>", "Flow",
        "A set of steps in Power Automate that <b>runs on its own</b> when something happens: a <b>trigger</b>, then <b>actions</b>, sometimes a <b>condition</b>.",
        "Copilot and agents wait for you…", "…a flow <b>starts</b> when the trigger happens.", "Trigger, actions, condition. A person still approves.",
        n=N(time="6 min", say="A flow is not a chat. Nobody types to it. Something happens, a form is submitted or a date arrives, and the steps run in order. "
                "Copilot writes. An agent answers. A flow moves the work from one step to the next.")))
    s.append(tslide("e3parts", "e3", "Block 3 · the words", "Four words <span class=\"hl\">you will hear.</span>", ["Word", "Means", "In the demo"],
        [["Trigger", "What starts the flow", "A new form response"], ["Action", "One step the flow does", "Add a row; send an email"],
         ["Condition", "A yes or no that splits the flow", "Approved or not"], ["Connector", "The app a step uses", "Forms, Excel, Approvals, Outlook"]],
        "Most HR flows are a form, a log, an approval and an email.",
        n=N(say="Four words, and you can read any flow. Watch for them in the demo: I will say each one aloud when it appears.")))
    s.append(tslide("e3live", "e3", "Demo 3.5 · video demo in Power Automate", "From a form <span class=\"hl\">to an email.</span>", ["Step", "App", "What it does"],
        [[f"<b>{a}</b>: {b}", c, d] for a, c, b, d in D.PA_FLOW],
        "Video: the recorded demo plays here.",
        n=N(time="15 min, video", do="(Play the demo video. Pause after the approval step and ask: which step did a person do?)",
            say="This is a recorded demo, so you can see every step clearly. (Play.) A form arrives. A row appears in the log. The approval goes to the line manager, and the flow waits. "
                "The manager decides; the flow only carried the request to him. Then the email goes out and the row changes to Approved. Nothing was typed twice, nothing was printed, and nobody had to chase.",
            fallback="Placeholder until the video is recorded: walk through the six steps on this slide, one row at a time.",
            more=["Placeholder: the demo video is not recorded yet. It will be recorded once Copilot and Power Automate access is fixed.", "Approvals use the Approvals connector. Forms, Excel Online and Outlook are standard connectors."])))
    s.append(listslide("e3need", "e3", "Block 3 · what a flow needs", "Before you build one, <span class=\"hl\">ask four questions.</span>",
        ["<b>License:</b> does your Microsoft 365 account include Power Automate?", "<b>Permission:</b> does your IT team allow these connectors?",
         "<b>Owner:</b> who fixes it when it breaks, or when someone leaves?", "<b>People:</b> is every approval still made by a person?"],
        "Ask your IT team first. Then build small.",
        n=N(time="5 min", say="A flow touches company data and runs without you, so it is not a personal tool. Your IT team decides what is allowed. "
                "And every flow needs an owner: a flow nobody owns breaks quietly on the day its builder goes on leave.")))
    s.append(listslide("e3why", "e3", "Block 3 · why a flow here", "Why not Copilot <span class=\"hl\">or an agent?</span>",
        ["<b>It starts on its own</b> when a form arrives. Copilot and agents wait to be asked.", "<b>It waits</b> for an approval, for days if needed, then continues.",
         "<b>It writes the log</b> and sends the email the same way every time.", "<b>It decides nothing.</b> The manager approves; the flow carries the request."],
        "A flow moves work between people. It never replaces their decisions.",
        n=N(time="4 min", say="So why did we need Power Automate here, and not the agent you built this morning? Because nobody is asking a question. "
                "The work is moving between people and systems, on its own, every time. That is the signal for a flow.")))
    s.append(check("e3chk", "e3", "In the training request flow, <b>which step must stay with a person?</b>",
        [("Adding the request to the log", 0, "The same every time: the flow does it."),
         ("Approving the request", 1, "Right. A decision about a person stays with a person."),
         ("Sending the result to the employee", 0, "The flow sends it; a person wrote the text once.")],
        n=N(say="(Tap after hands.) Approving. Lunch and Dhuhr now. After lunch, we look at a whole HR process, step by step.")))
    # Block 4 · From one task to a workflow
    s.append(story("e4story", "e4", "Block 4 · From one task to a workflow", "Thursday 22 October, 10:00",
        "An engineer asked for a safety course on <b>1 October</b>. His approval arrives today, <b>22 October</b>. The course started on 20 October.",
        "Three weeks <span class=\"hl\">for one signature.</span>", "See an HR task as a workflow, and find where time and effort are lost.",
        n=N(time="12:15-13:35", say="Welcome back. This morning you made single tasks faster with agents. Now we look at the whole road a request travels. "
              "(Read the story.) Nobody in this story was lazy. So where did three weeks go?", expect="Waiting for signatures, emails, printing.")))
    s.append(rule("e4an", "e4", "Block 4 · the picture", "Follow one form <span class=\"hl\">from desk to desk.</span>",
        "Walk behind one training request for three weeks. You would see where it waits, who types it again, and where it gets lost.",
        n=N(say="Imagine you are invisible and you follow that request around the building. Every time it stops, you write down why. "
                "That list of stops is a process map, and it is what we build today.")))
    s.append(tslide("e4prob", "e4", "Block 4 · four problems", "Four problems <span class=\"hl\">to look for.</span>", ["Problem", "What it looks like", "Ask"],
        [[f"<b>{a}</b>", b, q] for (a, b), q in zip(D.PROBLEMS, ["How long does it wait, and for whom?", "Who types or checks it again?", "Who does the next step? Who chases it?", "Is there any judgment in it?"])],
        "Find them first. Fix them after.",
        n=N(time="5 min", say="Four problems hide in most HR processes. (Go row by row, and ask the room for one example from their own unit for each.) "
                "The last column is the question you ask at every step of a map.", expect="Approvals for delay, retyping into trackers for duplication.")))
    s.append(term("e4t1", "e4", "Block 4 · the idea", "Map it <span class=\"hl\">as it is.</span>", "Process map",
        "A table of every step from request to result: <b>who</b> does it, what goes <b>in</b> and comes <b>out</b>, how long it <b>waits</b>, the <b>problem</b>, and whether a <b>person must decide</b>.",
        "“The process is slow.”", "“Step 3 waits three days for one approval.”", "Map it as it is first. Improve it after.",
        n=N(say="A map turns a feeling into facts. Nobody can act on “it is slow”. Everybody can act on “step three waits three days”. "
                "One rule: do not improve anything yet. A map of how it should work hides how it really works.")))
    s.append(live("e4live", "e4", "d36", "A story into <span class=\"hl\">a step table.</span>",
        "A five-sentence story about booking an external trainer, turned into a step table.", "The flags in the Problem column, and the step that nobody owns.",
        n=N(say="(Run the request.) Read the table with me. Copilot flagged the wait for the manager and the prices asked twice. "
                "Now the last row: who tells the trainer the room? Nobody. A step nobody owns is still a step, and it is often the one that fails.")))
    s.append(task("e4task1", "e4", "t36", n=N(say="Your turn, in pairs. Story 1 in the process stories file: a training request. Copilot drafts the map; you check it against the story. "
                                                  "Twelve minutes. (Start the timer.)")))
    s.append(check("e4chk", "e4", "In your map, the line manager signs every training request. <b>What does that step need?</b>",
        [("Problem: repetitive step", 0, "A signature is a judgment, not a repeated action."),
         ("“A person decides?”: Yes", 1, "Right. Approvals stay with people."),
         ("Wait: 0 days", 0, "The story says it waits for days.")],
        n=N(say="(Tap after hands.) Every approval is a human decision. Mark it, because it must stay with a person when you improve the process.")))
    # Block 4 · map your own
    s.append(listslide("e4brief", "e4", "Block 4 · map your own HR process", "Your process, <span class=\"hl\">mapped.</span>",
        ["<b>Choose:</b> your track's story (2 to 5), or a process from your own work, written with roles only.", "<b>Map:</b> from the request to the result, one row per step.",
         "<b>Flag:</b> delays, duplicated effort, unclear ownership, repetitive steps.", "<b>Mark:</b> every step where a person must decide."],
        "Map it first. If there is time, you improve it in Task 3.8.",
        n=N(say="Now your own. If you have a process at work that wastes your time, map that one, with roles only, no names. "
              "If not, take your track's story.")))
    s.append(task("e4task2", "e4", "t37", n=N(say="Twenty minutes. Map it as it is. (Start the timer, then walk the room and ask each person: where does it wait?)")))
    s.append(task("e4task3", "e4", "t38", n=N(say="Optional, if the block is on time: improve your map. Mark each step Person, Copilot or Agent, and take out two problems. Twenty-five minutes. (Start the timer.)",
                                                  silent="Running late? Skip this slide and go to the debrief, then the comparison after the break.")))
    s.append(rule("e4deb", "e4", "Block 4 · debrief", "One owner per step. <span class=\"hl\">A person for every decision.</span>",
        "The maps that helped most named one role for each step, showed every wait, and marked each approval as a human decision.",
        n=N(time="7 min", do="(Ask two people: which step in your process waits the longest, and who could change that?)",
            say="Look at the steps you marked Copilot or Agent. Each one is a step you know how to build now, with this morning's agents. Break now. (Press the cup button.)")))
    # Copilot, agent or flow?
    s.append(tslide("e5cmp", "e5", "Copilot, agent or flow?", "Three tools. <span class=\"hl\">Three different jobs.</span>", ["", "Copilot Chat", "An agent", "A flow"],
        [["Starts when", "You type a request", "Someone asks a question", "Something happens"], ["Best for", "One-off drafts and summaries", "The same questions for many people", "The same steps every time"],
         ["Knows your policies", "When you attach them", "From its saved knowledge", "No: it moves data"], ["Sends, logs, routes", "No", "No", "Yes"],
         ["HR example", "A reply to one employee", "Leave questions for 300 staff", "Each training request to approval"]],
        "Who starts it, how often, and does it move work between people?",
        n=N(time="13:50-14:05", say="Three days, three tools, side by side. (Go row by row.) The second row is the one to remember: one-off, many questions, same steps. "
              "When you are unsure, ask who starts it and how often it happens.")))
    s.append(sortslide("e5sort", "e5", "Demo 3.9 · card sort", 'Copilot, agent or flow? <span class="hl">Tap a card.</span>', CD.TOOL_SORT, CD.TOOL_LABELS, did="d39",
        n=N(say="Eight HR jobs. I read the card, you call the tool, I tap it. (Read the first card.)")))
    s.append(check("e5chk", "e5", "Line managers ask Job Evaluation the same five questions about job descriptions every week. <b>Which tool?</b>",
        [("Copilot Chat, a new chat each time", 0, "It works, but the rules are retyped every time."),
         ("A flow that emails the answers", 0, "A flow moves work. It does not answer questions."),
         ("An agent with the template and the rules", 1, "Right. The same questions, many people.")],
        n=N(say="(Tap after hands.) And you built that agent this morning.")))
    s.append(timer_slide("e6share", "e6", "Share-outs · 14:05", "One minute each: <span class=\"hl\">one agent or one map.</span>",
        "Show your agent's best test, or the biggest problem in your map and who still decides.", 15,
        n=N(time="14:05-14:20", do="(Go round the room fast. Keep to one minute each.)", say="One minute each. I will start with mine, so you can see how short it is.",
            silent="Share your own example first: the training request map, the printing step, and the manager who still approves.")))
    s.append(mapslide("e7map", "e7", "after"))
    s.append(wrap("w3", "close", "Build it. Test it. <span class=\"hl\">Improve the process.</span>",
        [(1, "You built", "Two tested HR agents and a map of one HR process."), (2, "You saw", "A flow that carries a request from a form to an email, with a person who approves."),
         (3, "The habit", "Copilot drafts. You check. Authorized HR staff decide.")],
        "Your first week: one green task a day. Your first month: one agent or one mapped process for your unit.",
        n=N(say="Three days ago you typed one short line and got a job description with an invented team. Today you built tools other people can use. "
                "(Read the three cards.) Please keep the habit. It matters more than any tool.")))
    return s

TOPICS = {1: {"open": "Opening", "b1": "Block 1 · How generative AI and Copilot work", "b2": "Block 2 · Writing a clear prompt", "b3": "Block 3 · Draft, fix and check in Word", "b4": "Block 4 · From policy to people", "b5": "Prompt Bank and wrap", "close": "Close"},
          2: {"open": "Opening", "c0": "Callback quiz", "c1": "Block 1 · Protecting employee data", "c2": "Block 2 · Before and after the meeting", "c3": "Block 3 · Follow-ups and reminders",
              "c4": "Block 4 · Excel: figures you can check", "c5": "Block 5 · Word summaries", "c6": "Block 6 · PowerPoint: from document to deck", "c8": "Which app for which job", "close": "Close"},
          3: {"open": "Opening", "e0": "Callback quiz", "e1": "Block 1 · Build an HR agent", "e2": "Block 2 · Test, fix and build a second agent", "e3": "Block 3 · Power Automate: a trainer demo",
              "e4": "Block 4 · From one task to a workflow", "e5": "Copilot, agent or flow?", "e6": "Share-outs", "e7": "Post-MAP and survey", "close": "Close"}}
DAYFN = {1: day1, 2: day2, 3: day3}
