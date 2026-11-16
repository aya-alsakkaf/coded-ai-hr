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
 2: [("Opening", "g-mark", ["open", "c0"]), ("Word", "g-code", ["c1"]), ("Outlook", "g-frame", ["c2"]), ("Teams", "g-impact", ["c3"]), ("Excel", "g-code", ["c4"]), ("PowerPoint", "g-frame", ["c5"]), ("Case", "g-impact", ["c6"]), ("Close", "g-progress", ["c7", "close"])],
 3: [("Opening", "g-mark", ["open", "e0"]), ("Gallery", "g-code", ["e1"]), ("Agent", "g-frame", ["e2"]), ("Capstone", "g-impact", ["e3", "e4", "e5"]), ("Close", "g-progress", ["e6", "close"])],
}
FLOW = {
 1: (["AI", "Prompt", "Word", "Outlook", "Save"], {"b1": 0, "b2": 1, "b3": 2, "b4": 3, "b5": 4}),
 2: (["Word", "Outlook", "Teams", "Excel", "PPT", "Case"], {"c1": 0, "c2": 1, "c3": 2, "c4": 3, "c5": 4, "c6": 5}),
 3: (["Gallery", "Agent", "Capstone", "Peer test"], {"e1": 0, "e2": 1, "e3": 2, "e4": 3}),
}
COVER_NOTES = {
 1: N(time="09:00-09:10", do="(Before 09:00: helpers walk the room and check that every laptop is signed in to Copilot Chat with a work account.)",
      more=["Housekeeping: breaks at 10:30 and 13:20, lunch and Dhuhr at 11:35. Prayer room and toilets."],
      say="Good morning, everyone. Please open your laptop and sign in to Copilot Chat with your work account while I set up. "
          "If anything does not work, raise your hand and one of us will come to you. We start in two minutes."),
 2: N(do="Welcome back.", more=["Sign-in check: Copilot Chat open, the tracker and the thread file downloaded.", "The callback quiz comes after today's map."],
      say="Yesterday you wrote five-input requests and traced every line to its source. Today the same habit goes into five apps.", silent="ask one person which request they tried at work last night.", time="09:00"),
 3: N(do="Welcome to the last day.", more=["Check: Agent Builder opens on at least the presenting laptop (New agent).", "Remind the room: post-MAP and survey at 14:20, certificates at 14:40."],
      say="Today your best requests become things a colleague can use without you.", silent="ask who saved a request in the Prompt Bank yesterday.", time="09:00"),
}
OUTCOMES_NOTES = {d: N(expect="Most people pick the checking outcome.", silent="pick the one you use most yourself and say why.",
                       say="These are the four things you will be able to do by the end of today, on fictional Mutla files. "
                           "Which one matters most for your own job? Tell your neighbor in one sentence.") for d in (1, 2, 3)}
ROAD = {d: {"title": "One company. <span class=\"hl\">Five HR units.</span>",
            "n": N(do="(Point to each block, then to the breaks.)", say="This is our day. Mutla Oil Company has five HR units, the same as many real HR departments. "
                   "Pick the unit closest to your own job: you will use it in the tasks. When I press the cup button, the break clock starts.")} for d in (1, 2, 3)}
CLOSE = {
 1: {"big": "Ask clearly. <span class=\"hl\">Check everything.</span>", "next": "Tomorrow: safe data first, then meetings, Excel, PowerPoint, and a map of one HR process.",
     "n": N(say="Thank you for a great first day. Please bring the same laptop tomorrow, and the HR process you want to fix. See you at 9:00.")},
 2: {"big": "Five apps. <span class=\"hl\">One review.</span>", "next": "Tomorrow: an HR assistant, a new case, and a colleague who tests your work.",
     "n": N(do="Recap the day in one line.", more=["Ask everyone to finish organizing the Prompt Bank tonight if they did not."], say="Thank you. See you tomorrow at 9:00.")},
 3: {"big": "Copilot drafts. <span class=\"hl\">People decide.</span>", "next": "Thank you. Copilot drafts. You check. Authorized HR staff decide.",
     "n": N(do="Recap the three days in one line. Hand out certificates.", more=["Point to the take-home guide and the safe-use card."], say="Start with one green task at work this week.")},
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
        "Same tool. Same role. <span class=\"hl\">Watch what the request changes.</span>", "See why the request decides the quality of the draft.",
        n=N(time="09:20-09:30", say="Here is our first story. (Read the story aloud.) Before I show you anything: what would you type? Call it out. "
              "(Wait for two or three answers.) Most of us type one short line. Let us see what that gives us.",
            expect="Short answers like “write a JD for a compensation analyst”.")))
    s.append(live("b0live", "open", "d10", "Same tool. Same role. <span class=\"hl\">Two requests.</span>",
        "One short line in the first tab. The full request, with two files, in the second tab.", "The duties, the team size and the grade line in each answer.",
        n=N(say="(Run the one-line request in tab 1.) Look at this. It sounds professional. Now read it slowly: a team to manage, a senior grade, duties nobody approved. "
                "(Run the full request in tab 2.) Same tool, same role. This one follows our template, uses only the six approved duties, and leaves the grade for the committee. "
                "The only thing that changed is what we gave Copilot. That is today's whole story.")))
    # Block 1 · How generative AI and Copilot work
    s.append(story("b1story", "b1", "Block 1 · How generative AI and Copilot work", "Monday 2 November, 08:40",
        f"Fatma in Personnel asks Copilot: <b>“How many days of leave can staff carry over?”</b> The answer comes at once: <b>30 days.</b> Mutla's policy says {D.LEAVE['carry']}.",
        "Confident, fast <span class=\"hl\">and wrong.</span>", "See why Copilot can write a confident sentence that is wrong.",
        n=N(time="09:30-10:30", say="Block 1. Before we write a single request, we need to know how this tool works, because it explains every mistake you will see this week. "
              "(Read the story.) Has an AI tool ever given you a wrong number at work? Tell us in one sentence.",
            expect="Two or three short stories.", silent="Share one of your own wrong-number stories.")))
    s.append(rule("b1an", "b1", "Block 1 · the picture", "Your phone keyboard guesses <span class=\"hl\">your next word.</span>",
        "Copilot does the same thing with a much bigger memory. Its guesses sound right because it learned from a huge amount of text.",
        n=N(do="(Ask two people to type “I will be there in” on their phone and read the suggestions.)",
            say="Your keyboard does not know where you are. It only knows what people usually type after those words. Hold on to that idea.",
            expect="“5 minutes”, “a bit”, “10”.")))
    s.append(term("b1t1", "b1", "Block 1 · the idea", "What Copilot <span class=\"hl\">really does.</span>", "Next-word prediction",
        "Copilot writes by <b>predicting the next word</b>, one word at a time, from patterns in the text it learned from.",
        "Like your phone keyboard…", "…it picks a <b>likely</b> next word. Numbers and dates are words too.", "It predicts. Without the source, it guesses or searches the web, and nothing checks it against Mutla's policy.",
        n=N(say="So the official name is next-word prediction. Copilot is not looking anything up in our policy unless we give it the policy. "
                "It writes what usually comes next. And here is the part people forget: to Copilot, a number is just another word.",
            silent="Ask: is the most common number always Mutla's number?")))
    s.append(llmslide("b1llm", "b1", "Block 1 · live widget", "It writes by guessing <span class=\"hl\">the next word.</span>",
        "At each step, every possible next word gets a score. The model picks one and repeats.", f"It predicts <b>likely</b> words. Mutla's policy says {D.LEAVE['carry']}, but 30 is more common.",
        n=N(time="7 min", do="(Read the start of the sentence. Ask the room for the next word, then click it.)",
            more=["Click Pick the top word: 30 wins, because it is common in policies everywhere.", "Start again and pick 15: Mutla's real number is only the second guess.", "Pick camel (1%). The sentence still sounds confident.", "The percentages are illustrative."],
            say="Watch what wins. (Click the top word.) Thirty. Not because it is our rule, but because thirty follows these words most often in the world. "
                "(Start again, pick camel.) And even nonsense comes out sounding confident. The tone tells you nothing about the truth.")))
    s.append(term("b1t2", "b1", "Block 1 · the risk", "Fluent <span class=\"hl\">and wrong.</span>", "Hallucination",
        "When Copilot writes something that <b>sounds right but is not true</b>: a wrong number, date, rule or name.",
        "A likely next word…", "…is not always a <b>true</b> one. Nothing checks it for you.", "Check every number, date and rule against the approved source.",
        n=N(say="This has a name: hallucination. It does not mean Copilot is broken. It means Copilot did exactly what it does, predicted a likely word, and the likely word was wrong. "
                "Go back to Fatma. Thirty was likely. It was not true.", silent="Ask: what would have caught Fatma's 30 days?")))
    s.append(check("b1chk1", "b1", "An employee forwards you Copilot's answer: <b>Hajj leave is 30 days.</b> <b>What do you check before you reply?</b>",
        [("How sure Copilot sounded in its answer", 0, "Sounding sure is not evidence. Check the source."),
         ("A second answer from a new Copilot chat", 0, "A second prediction is not a check. Read the policy."),
         ("The Hajj section of the leave policy", 1, f"Right. The policy says {D.LEAVE['hajj']} days. The approved policy decides.")],
        n=N(say="Quick check. Hands up for A. For B. For C. (Tap the most popular.) A second chat is just a second guess. Only the policy can answer this.")))
    s.append(rule("b1key", "b1", "Block 1 · a second picture", "A colleague with <span class=\"hl\">your keycard.</span>",
        "They can open every door you can open, and no other door. That is how Copilot reaches your work files.",
        n=N(do="(Hold up your own badge or keycard.)",
            say="Second question: what can Copilot see? Imagine a colleague borrows this card. Which rooms can they enter? Only mine. Not one more. Keep this card in mind for the next slide.",
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
            say="Three wrong numbers, written in perfect English. If this had gone to an employee, nobody would have noticed until it was too late. Certainty is a writing style. It is not evidence.")))
    s.append(cards3("b1groups", "b1", "Block 1 · three groups", "Sort the task <span class=\"hl\">before you type.</span>",
        [(a, b, c, "") for a, b, c in C.GROUPS], "Grades, pay, ratings, discipline and selection stay with authorized HR staff.",
        n=N(say="Last idea of this block: where Copilot's role stops. Every HR task falls into one of these three groups. "
                "Give me one task from your own unit for each group. (Take one example per group.)",
            expect="Job descriptions and recaps go to drafts; grades stay with people.", silent="Give your own example for each group.")))
    s.append(term("b1t4", "b1", "Block 1 · the idea", "Some decisions <span class=\"hl\">stay with people.</span>", "Human decision",
        "A decision that changes a person's pay, grade, rating, record or job is made by <b>authorized HR staff</b>. Copilot may prepare the file. It never decides.",
        "Copilot prepares…", "…a person with authority <b>decides</b>.", "Drafts, yes. Decisions about people, no.",
        n=N(say="This is the line we never cross. However good the draft is, the decision about a person belongs to a person with the authority to make it. "
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
        "On their first day, a new colleague needs to know who they write as, why, what to do, with which facts, within which limits, in what voice and in what shape.",
        n=N(say="Think about a new colleague on their first morning. You would never say only “write a reminder” and walk away. "
                "You would brief them. What would you tell them? (Collect answers.) Everything you just said has a place in a request.",
            expect="What to do, who it is for, which file, how it should look.")))
    s.append(tslide("b2check", "b2", "Block 2 · the prompt checklist", "Seven parts <span class=\"hl\">before you press Send.</span>", ["Part", "It tells Copilot", "Example"],
        [[f"<b>{a}</b>", b, c] for a, b, c in D.CHECKLIST], D.PARTS_LINE + ".",
        n=N(time="12 min", say="Here is the whole checklist. Seven parts. Each one answers a question Copilot would otherwise guess: who am I, why, what, with what, within which limits, in what voice, in what shape. "
                "(Go row by row and ask the room for a second example of each.) You do not need to remember the order. You need to check that nothing is missing.",
            expect="Constraints and output format are the parts people leave out.")))
    s.append(term("b2t1", "b2", "Block 2 · the part people forget", "Constraints: <span class=\"hl\">the limits.</span>", "Constraints",
        "The <b>limits</b> Copilot must keep: use only these files, add no grade, change no date, stay under one page.",
        "Without constraints…", "…Copilot <b>fills the gaps</b> with likely words.", "Write what it must not add, change or guess.",
        n=N(say="If you remember one part from this block, make it this one. Constraints are the fence. Without a fence, Copilot fills every gap with the most likely words, "
                "and in HR the most likely words are often someone else's policy.")))
    s.append(live("b2live", "b2", "d12", "Seven short sentences, <span class=\"hl\">typed live.</span>",
        "A reminder to all staff about carrying over leave, built one part at a time.", "The number and the date in the email. Do they match section 4?",
        n=N(say="Now I will fix Fatma's request, live, one part at a time. Tell me what to type for each part. (Type each part as the room suggests it, then send.) "
                "Read the email with me. Fifteen days, the deadline, nothing invented. Same tool as Fatma. A better brief.")))
    s.append(check("b2chk", "b2", "Copilot's email adds a rule from section 3 that you did not ask for. <b>Which part of the checklist would stop it?</b>",
        [("Tone: friendly and clear", 0, "Tone changes the voice, not what goes in."),
         ("Constraints: use only section 4", 1, "Right. Constraints set the limits."),
         ("Role: a Personnel officer", 0, "The role sets the point of view, not the limits.")],
        n=N(say="Quick check on the fence. (Wait for hands, then tap.) Exactly: constraints.")))
    s.append(task("b2task", "b2", "t12", n=N(say="Your turn. Here are five weak requests, one from each HR unit. Choose two: one from your own unit, plus any other. "
                                                 "Give each of them all seven parts. Then swap: can your neighbor tell what Copilot will produce? Fourteen minutes. "
                                                 "If you are stuck, the Day 1 lab page has hints. (Start the timer.)")))
    s.append(rule("b2deb", "b2", "Block 2 · debrief", "Seven parts <span class=\"hl\">beat one clever sentence.</span>",
        "The best rewrites in the room were not long for the sake of it. Each line answered a question Copilot would otherwise guess.",
        n=N(do="(Ask two people to read a rewrite aloud. Ask the room which part is strongest and which is missing.)",
            say="Notice what made the strong ones strong. Not fancy words. Every part answered a question. Lunch now, and Dhuhr. We start again at 12:15 sharp.",
            expect="Most rewrites miss constraints or the output format at first.")))
    # Block 3 · Draft, fix and check in Word
    s.append(story("b3story", "b3", "Block 3 · Draft, fix and check in Word", "Wednesday 11 November, 12:15",
        "Hessa's checklist draft looks perfect. Then she reads it twice: <b>“Manages a team of six analysts.”</b> and <b>“Grade 8.”</b> Neither is in the role information. And it is two pages.",
        "Good is not <span class=\"hl\">finished.</span>", "Fix a draft with follow-up instructions, and ask for the source of every line.",
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
                "Look: the duty is added, the length is right, and everything else stayed where it was. Three short messages, no starting again.")))
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
        n=N(say="Three failures to hunt for. The source trace finds the first one for you. For the other two, you still open the source and read. That is why the last step is always yours.")))
    s.append(live("b3live2", "b3", "d13b", "Every line, <span class=\"hl\">with its source.</span>",
        "A finished-looking draft, checked line by line against the role sheet.", "The NOT IN SOURCE lines. Then the role sheet, to prove they are not there.",
        n=N(say="(Run the source trace.) Two lines come back with no source: the team of six and the grade. (Open the role sheet.) "
                "I do not trust Copilot on this either: I check the role sheet myself. They really are not there. They go.")))
    s.append(check("b3chk", "b3", "The source trace marks one duty <b>NOT IN SOURCE</b>. What now?",
        [("Delete it, or check it with the owner", 1, "Right. No source, no line."),
         ("Keep it, because it sounds right for the role", 0, "Sounding right is how hallucinations look."),
         ("Ask Copilot if it is sure", 0, "It may say yes again. The role sheet decides.")],
        n=N(say="Quick check. (Tap after hands.) Sounding right is exactly what a hallucination looks like.")))
    s.append(task("b3task", "b3", "t13", n=N(say="Your turn, with your own unit's role. Write your own request: all seven parts, both files attached. Fix the draft with two follow-ups. "
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
                "Two numbers checked by a person. Now the summary can go out.")))
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
                "(Point to the number and the date in each.) Same facts, every time.")))
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
    s.append(rule("b4deb", "b4", "Block 4 · debrief", "Warmer, <span class=\"hl\">never different.</span>",
        "Read each version once for tone, and once for every date, time and rule. Two readings, two different checks.",
        n=N(do="(Ask two people to read their reply to Mubarak.)", expect="One reply promises an exception: discuss why it should not.",
            say="Did anyone promise Mubarak an exception? It is easy when you are trying to be kind. Kind is good. A promise the rules do not allow is not ours to make.")))
    # Prompt Bank and wrap
    s.append(listslide("b5bank", "b5", "Prompt Bank", "A request you checked <span class=\"hl\">is worth saving.</span>",
        ["<b>Task:</b> what it is for, in one line.", "<b>Request:</b> the seven parts, with [brackets] for what changes each time.", "<b>Files:</b> which approved files it needs.", "<b>Check:</b> how you check the result."],
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
        "Tomorrow: safe data first, then meetings, Excel, PowerPoint and a map of one HR process.",
        n=N(say="Look at what you made today. (Read the three cards.) Tonight, think of one HR process in your unit that annoys you: too many emails, too many steps. We map it tomorrow afternoon.")))
    return s

# ------------------------------------------------------------------ Day 2 · Copilot Across HR Documents, Communication and Reporting
def day2():
    s = opening(2)
    s.append(rule("c0rule", "c0", "Callback · Day 1", "Five inputs in. <span class=\"hl\">A source for every line out.</span>",
        "Yesterday: one job description, three ways, every line traced to its source. Today the same habit goes into five apps.",
        n=N(do="Ask: who tried a five-input request at work last night?", expect="One or two hands.", say="Three quick questions on yesterday. Then Word.", time="09:00-09:10")))
    s.append(check("c0chk1", "c0", f"Yesterday a draft said: <b>\u201c{D.LEAVE_ERRORS[1][1]}\u201d</b> The policy says {D.LEAVE['emergency']} days. <b>What would have stopped it?</b>",
        [("A longer request with more detail about the employee", 0, "Length does not check a number."),
         ("Attaching the policy, then checking", 1, "Right. Ground it, then check it."),
         ("Asking Copilot to be careful", 0, "Copilot cannot check against a source it does not have.")]))
    s.append(check("c0chk2", "c0", "Which input gives Copilot <b>the facts of this case</b>?",
        [("Tone", 0, "Tone is how it sounds."),
         ("Context", 0, "Context is why and for whom."),
         ("Data", 1, "Right. Data is the facts; sources are the rules.")]))
    s.append(check("c0chk3", "c0", "A source trace marks a line <b>NOT IN SOURCE</b>. What do you do?",
        [("Delete it, or ask the owner", 1, "Right. No source, no line."),
         ("Keep it if it sounds right and fits the template", 0, "Sounding right is the problem."),
         ("Ask Copilot again", 0, "The source decides, not Copilot.")]))
    # Block 1 · Word
    s.append(story("c1story", "c1", "Block 1 · Word: policies and job evaluation", "Sunday 8 November, 09:15",
        f"The Allowances Policy version 4 arrives. Yousef asks Abdulaziz one question: <b>what changed from version 3?</b> He needs it by noon, with the section of every change.",
        "One question. <span class=\"hl\">Two versions.</span>", "Compare policy versions, and organize job-evaluation evidence with no grade.",
        n=N(do="Ask: how do you find changes between two versions today?", expect="Read both, or Track Changes if someone kept it.", silent="Ask who has been asked “what changed?” this month.", time="09:10-10:00")))
    s.append(rule("c1an", "c1", "Block 1 · the picture", "Spot the difference <span class=\"hl\">between two photos.</span>",
        "Slow by eye, and you always miss one. Copilot can list the differences; you confirm each one.",
        n=N(do="Ask: who has played spot the difference? How many did you miss?", expect="Laughter. Everyone misses one.", say="Copilot finds them fast. You still check each one in both files.")))
    s.append(term("c1t1", "c1", "Block 1 · the idea", "List every change, <span class=\"hl\">with its section.</span>", "Compare versions",
        "Ask Copilot to list <b>every change</b> between two files in a table: section, old text, new text. Then open both files and check each row.",
        "Like spot the difference…", "…a list you can <b>tick against both files</b>.", "Section numbers make every change checkable.",
        n=N(do="Show a two-row change table.", expect="People ask about renumbered sections: they are not policy changes.", silent="Ask: why insist on section numbers?")))
    s.append(cards3("c1ever", "c1", "Block 1 · three requests for long policies", "Three requests <span class=\"hl\">you will use every month.</span>",
        [("Summarize", "With section numbers", "A one-page summary where every point names its section.", ""), ("Compare", "Two versions", "Every change: section, old, new.", ""),
         ("Answer", "From the policy only", "Answer this question from the policy; if it does not say, say so.", "")],
        "Each one ends with the same habit: open the section and check.", n=N(do="Ask which of the three their unit needs most.", expect="Compare, before every new version.", silent="Say Compensation uses compare most.")))
    s.append(rule("c1clerk", "c1", "Block 1 · a second picture", "The clerk prepares the file. <span class=\"hl\">The committee decides.</span>",
        "A good clerk sorts the evidence so the committee can judge. A clerk who writes the verdict has overstepped.",
        n=N(do="Ask Job Evaluation participants how the committee works at their company.", expect="Evidence first, then a decision by the committee.", say="Copilot can be an excellent clerk. Never the committee.")))
    s.append(term("c1t2", "c1", "Block 1 · the idea", "Organize the evidence. <span class=\"hl\">Never the grade.</span>", "Evidence by factor",
        "Copilot sorts the evidence against the <b>evaluation factors</b>, with the note it came from. The level and grade column stays empty for the committee.",
        "Like the clerk's case file…", "…evidence in order, <b>the decision left blank</b>.", "If Copilot suggests a grade, delete it.",
        n=N(do="Point to the empty Level column on the next slide.", expect="People ask what to do if a manager asks for a suggested grade: say the committee decides.", silent="Ask: why does the empty column matter?")))
    s.append(player("c1pp", "c1", "d21"))
    s.append(check("c1chk2", "c1", "Copilot's evidence table lists <b>\u201cparking at the head office is full\u201d</b> under Working conditions. What do you do?",
        [("Remove it: it is not evidence for the job", 1, "Right. Only evidence about the job goes to the committee."),
         ("Keep it, because the job holder said it in the interview", 0, "Said in the interview is not the same as evidence."),
         ("Move it to a new factor called Other", 0, "The factors are fixed. Noise stays out.")]))
    s.append(listslide("c1rec", "c1", "Block 1 · recruitment, at a high level", "Recruitment: <span class=\"hl\">drafts only.</span>",
        ["<b>Vacancy text</b> from an approved job description, every duty kept.", "<b>Structured interview questions</b> from the approved competencies.",
         "<b>Never</b> ranking, scoring or selecting candidates.", "<b>Never</b> a CV with personal data in a prompt."],
        "Copilot drafts the words. People choose the person.", n=N(do="Keep this short: recruitment is not today's focus.", expect="One question about CV screening: the answer is no.", silent="Move on after one minute.")))
    s.append(check("c1chk1", "c1", "Copilot turns the approved job description into vacancy text. It adds <b>\u201ca fast-growing team\u201d</b>. What do you do?",
        [("Keep it, because it makes the vacancy more attractive", 0, "Attractive is not approved. It promises something."),
         ("Ask Copilot to make the whole text more exciting", 0, "More excitement means more invented claims."),
         ("Remove it: the job description does not say it", 1, "Right. Vacancy text keeps to the approved job description.")]))
    s.append(player("c1pp2", "c1", "d21c"))
    s.append(task("c1task", "c1", "t21"))
    s.append(check("c1chk3", "c1", "Copilot lists a change in <b>section 6</b> that is only a new section number. <b>Is it a policy change?</b>",
        [("Yes, every new section number is a policy change", 0, "Renumbering moves text; it does not change a rule."),
         ("No. Section 5 is new, so the text moved", 1, "Right. Report the three rule changes, and note the renumbering."),
         ("Only if Copilot says so", 0, "The two files decide, not Copilot.")]))
    # Block 2 · Outlook
    s.append(story("c2story", "c2", "Block 2 · Outlook: thread to message", "Thursday 12 November, 10:00",
        "Fatma opens the attendance thread: <b>30 messages</b>, four reply-alls, one early date that changed later. She must write the staff announcement today.",
        "Thirty messages. <span class=\"hl\">Who decided what?</span>", "Turn a long thread into decisions and owners, and change the tone without changing the facts.",
        n=N(do="Ask: hands up when you know the start date from the thread. Give them one minute.", expect="Few hands, and two different dates.", silent="Point to message 3 and message 24.", time="10:00-10:40")))
    s.append(rule("c2an", "c2", "Block 2 · the picture", "A long thread is <span class=\"hl\">a meeting with no minutes.</span>",
        "Everyone was there, everyone remembers it differently, and the final decision is in message 24.",
        n=N(do="Ask: who has acted on an old decision from early in a thread?", expect="Several hands.", say="Copilot can write the minutes of the thread, if you ask for decisions, owners and dates.")))
    s.append(scene("c2scene", "c2", "Block 2 · the picture, drawn", "Thirty emails in. <span class=\"hl\">Four decisions out.</span>",
        "The thread goes in. Out comes a short list: each decision, its owner, its date and the message that settled it.",
        "Decisions, owners, dates, and the message number.",
        [{"ground": 268}, {"mail": (70, 120), "tone": "dim"}, {"mail": (100, 150), "tone": "dim"}, {"mail": (70, 180), "tone": "dim"}, {"mail": (100, 210), "tone": "dim"},
         {"laptop": (240, 220), "tone": "hot", "label": "Copilot"}, {"doc": (400, 170), "tone": "ok", "label": "4 decisions"},
         {"move": "mail", "path": [(130, 170), (230, 170), (380, 170)], "dur": 4}],
        n=N(do="Point to the stack of emails, then the one page.", expect="People ask about attachments in the thread: attach them too.", silent="Ask: what would you lose if the summary skipped message numbers?")))
    s.append(term("c2t1", "c2", "Block 2 · the idea", "Ask for <span class=\"hl\">decisions, not a summary.</span>", "Thread summary",
        "A summary that lists <b>each decision, its owner and its date</b>, the message that settled it, and the questions still open.",
        "Like minutes of the thread…", "…<b>what was decided</b>, by whom, when.", "Later decisions replace earlier ones. Ask Copilot to say which.",
        n=N(do="Stress the last line: message 3 versus message 24.", expect="People see why the message number matters.", silent="Ask: what if two messages disagree?")))
    s.append(term("c2t2", "c2", "Block 2 · tone", "Turn the tone dial. <span class=\"hl\">Keep the facts.</span>", "Tone dial",
        "The same facts can be written for <b>employees, managers or senior stakeholders</b>. Name the facts that must not change.",
        "“Make it friendlier.”", "“Make it warmer; keep every date, time and rule as written.”", "Name what must not change.",
        n=N(do="Read both requests. Ask which one is safer.", expect="The second: it names the facts.", silent="Ask: what could “friendlier” change by mistake?")))
    s.append(player("c2pp", "c2", "d22"))
    s.append(check("c2chk", "c2", "Fatma rewrites the staff announcement <b>for line managers</b>. What changes?",
        [("The start date, because managers need more notice", 0, "The facts stay the same for every reader."),
         ("What managers must do, such as approving permissions", 1, "Right. The reader changes the focus, not the facts."),
         ("The number of permissions, so managers can plan", 0, "A rule does not change with the reader.")]))
    s.append(task("c2task", "c2", "t22", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(rule("c2deb", "c2", "Block 2 · debrief", "Warmer, <span class=\"hl\">never different.</span>",
        "Read your announcement once for tone, and once for every date, time and rule. Two readings, two different checks.",
        n=N(do="Ask two people to read their reply to Mubarak.", expect="One reply promises an exception: discuss why it should not.", silent="Read the backup reply yourself.", say="The tone is yours to change. The rule is not.")))
    s.append(check("c2chk2", "c2", f"Message 3 proposes {D.ATT['old_start']}. Message 24 approves {D.ATT['start']}. <b>Which date goes in the announcement?</b>",
        [(D.ATT["start"], 1, "Right. The later, approved decision stands."),
         (D.ATT["old_start"], 0, "That was a proposal. A later message replaced it."),
         ("Both, so staff can choose", 0, "Two dates confuse everyone. Use the approved one.")]))
    # Block 3 · Teams
    s.append(story("c3story", "c3", "Block 3 · Teams: meetings and notes", "Monday 16 November, 10:30",
        f"Yousef's staffing meeting for the new <b>{D.NEW_SECTION}</b> section ended at 10:23. The actions were said aloud, but nobody wrote them down. Two days later, Finance asked <b>who was sending the manpower request.</b>",
        "No written actions means <span class=\"hl\">no follow-up.</span>", "Recap a meeting into actions, and keep investigation notes to a timeline.",
        n=N(do="Ask: who writes the actions after your meetings?", expect="Nobody, or the manager, late.", silent="Ask how many have missed an action because of it.", time="10:55-11:35")))
    s.append(listslide("c3before", "c3", "Block 3 · before the meeting", "Before: <span class=\"hl\">an agenda and a brief.</span>",
        ["<b>Agenda:</b> items, owner of each item, minutes.", "<b>Background brief:</b> one page of facts from the approved files.", "<b>One question</b> the meeting must answer."],
        "A good meeting starts with a good page.", n=N(do="Show one agenda request from the prompt sheet.", expect="People ask about calendar invites: Outlook Copilot can draft them too.", silent="Ask: what is the one question for your next meeting?")))
    s.append(term("c3t1", "c3", "Block 3 · the idea", "After: <span class=\"hl\">action, owner, deadline.</span>", "Meeting recap",
        "A recap lists <b>decisions</b>, then a table of <b>action, owner and deadline</b>, then the open questions. In Teams, Copilot needs the meeting transcript for this.",
        "A meeting nobody recaps…", "…becomes <b>a table everyone can act on</b>.", "No transcript in Teams: use the notes or a transcript file.",
        n=N(do="Say: in class we use a transcript file, so no live meeting is needed.", expect="People ask how to turn on transcription: Teams meeting controls, if their company allows it.", silent="Ask: who owns sending the recap?")))
    s.append(player("c3pp", "c3", "d23"))
    s.append(check("c3chk1", "c3", "The recap lists an action <b>nobody agreed in the meeting</b>. What do you do?",
        [("Keep it; it is a good idea", 0, "Good or not, nobody owns it."),
         ("Give it to the HR Section Head to approve later", 0, "That assigns work nobody agreed."),
         ("Delete it, or ask about it", 1, "Right. A recap records what was agreed.")]))
    s.append(check("c3chk2", "c3", "Hessa wants Copilot to recap her Teams meeting afterwards. <b>What must she do during the meeting?</b>",
        [("Share her screen for the whole meeting", 0, "Screen sharing does not give Copilot the words."),
         ("Keep the meeting chat open, with no transcript", 0, "Without a transcript, the recap has little to work with."),
         ("Start transcription", 1, "Right. Copilot recaps the meeting from the transcript.")]))
    s.append(rule("c3board", "c3", "Block 3 · a second picture", "A timeline on a whiteboard, <span class=\"hl\">not a verdict.</span>",
        "Investigators lay out what happened and when. Deciding who is at fault comes later, by people with authority.",
        n=N(do="Ask: who in your company decides the outcome of an investigation?", expect="A committee or a named manager.", say="Copilot can draw the timeline. It never writes the verdict.")))
    s.append(term("c3t2", "c3", "Block 3 · the idea", "Organize the notes. <span class=\"hl\">No finding.</span>", "Investigation notes",
        "Copilot may turn notes into a <b>timeline and open questions</b>. It never writes a finding, blames a person or recommends an action. Use roles, never names.",
        "Like the whiteboard…", "…<b>what happened and when</b>, and what we still need to ask.", "An opinion in the notes stays an opinion.",
        n=N(do="Point out: the notes for Task 2.3 already use roles.", expect="People ask about real cases: redact first, and follow the company's investigation policy.", silent="Ask: what is the difference between a fact and an opinion in a note?")))
    s.append(player("c3pp2", "c3", "d23c"))
    s.append(task("c3task", "c3", "t23", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(check("c3chk3", "c3", "The notes say a manager thinks <b>Employee C is clearly at fault</b>. Where does that line go in your output?",
        [("In the findings", 0, "An opinion is not a finding."),
         ("Nowhere, or only as what someone said", 1, "Right. It stays an opinion, attributed to who said it."),
         ("In the recommended actions", 0, "Copilot recommends no action about a person.")]))
    # Block 4 · Excel
    s.append(story("c4story", "c4", "Block 4 · Excel: HR trackers", "Tuesday 10 November, 12:15",
        f"Noura's quarterly report says <b>{D.TRAIN_ROWS_EXPORT} training requests</b> for Q3. The training system's control total says <b>{D.TRAIN_TRUE}</b>. The Head of L&D asks which number is right.",
        "Fast numbers <span class=\"hl\">still need a check.</span>", "Ask Copilot about a tracker, see the rows, and check against the control total.",
        n=N(do="Ask: how often do two HR numbers for the same thing disagree?", expect="Often.", silent="Ask who has had to explain a wrong number to a manager.", time="12:15-13:00")))
    s.append(rule("c4an", "c4", "Block 4 · the picture", "A calculator that <span class=\"hl\">shows what it pressed.</span>",
        "You trust it because you can see every step. Ask Copilot for the rows or the formula behind every number.",
        n=N(do="Ask: why trust a receipt more than a guess at the total?", expect="You can see the lines.", say="The rows are the receipt.")))
    s.append(term("c4t1", "c4", "Block 4 · the idea", "Ask, then <span class=\"hl\">see the rows.</span>", "Rows behind the number",
        "Ask in plain language, then ask Copilot to <b>show the formula or the rows</b> it counted. A number with no rows is a guess.",
        "Like the calculator's tape…", "…the <b>rows</b> show what was counted.", "Copilot in Excel works on a saved .xlsx workbook; in Copilot Chat, attach it.",
        n=N(do="Show where Copilot sits in Excel on the presenting laptop, if it has an M365 Copilot label.", expect="Copilot Chat (Basic) users attach the file in Copilot Chat.", silent="Ask: what would you check first in the rows?")))
    s.append(term("c4t2", "c4", "Block 4 · spot-check", "Check against <span class=\"hl\">the control total.</span>", "Control total",
        "A <b>control total</b> is a checked figure from the system of record. Compare two figures with it before any number goes in a report.",
        "Copilot's count…", "…next to the <b>control total</b>. If they differ, find the rows.", "Too high: look for duplicates. Too low: look for a missing value.",
        n=N(do="Ask: what can make a count too high? Too low?", expect="Rows counted twice; a zero or blank where a number should be.", silent="Give one example: the same request entered twice.")))
    s.append(player("c4pp", "c4", "d24"))
    s.append(check("c4chk1", "c4", "Before a Copilot count goes into your report, <b>what do you compare it with?</b>",
        [("Last year's report", 0, "Last year is a different period."),
         ("The control total from the system", 1, "Right. The control total is the checked number."),
         ("A second Copilot answer", 0, "Two unchecked answers are still unchecked.")]))
    s.append(task("c4task", "c4", "t24"))
    s.append(check("c4chk2", "c4", "Total vacancies are <b>too low</b>. What is the most likely cause?",
        [("A section with 0 approved", 1, "Right. A blank or zero where a number should be."),
         ("Duplicate rows in the Training sheet", 0, "Duplicates usually make a total too high."),
         ("Copilot's math", 0, "The math was right on the rows it had.")]))
    s.append(listslide("c4deb", "c4", "Block 4 · debrief", "Two numbers, <span class=\"hl\">two different reasons.</span>",
        ["<b>Training too high:</b> duplicate request IDs.", "<b>Vacancies too low:</b> one section with 0 approved positions.", "<b>Copilot's sums were right.</b> The file was wrong.", "<b>Your check</b> found both."],
        "A number goes in a report only after it matches the control total.", n=N(do="Ask two pairs for their corrected figures.", expect="Most find the duplicates; fewer find the zero.", silent="Show the lab page for Day 2.")))
    # Block 5 · PowerPoint
    s.append(story("c5story", "c5", "Block 5 · PowerPoint: briefings", "Wednesday 11 November, 13:00",
        "Line managers meet on Monday 23 November to explain the new attendance rules to their teams. Fatma has a <b>two-page brief</b> and <b>20 minutes</b> to turn it into slides.",
        "Same facts. <span class=\"hl\">Fewer words.</span>", "Turn a document into a short briefing, every number checked.",
        n=N(do="Ask: how long does a five-slide briefing take you today?", expect="An hour or more.", silent="Say most of that hour is formatting.", time="13:00-13:30")))
    s.append(term("c5t1", "c5", "Block 5 · the idea", "From document <span class=\"hl\">to deck.</span>", "Document to deck",
        "Copilot in PowerPoint can build slides from a Word file (with an M365 Copilot label). In Copilot Chat, ask for a <b>five-slide outline with speaker notes</b>.",
        "A two-page brief…", "…<b>five slides</b> a busy manager can present.", "The deck is the brief made visible. Check every number.",
        n=N(do="If the presenting laptop has an M365 Copilot label, show how to build slides from the Word brief: type / in the Copilot box and pick the file.", expect="Copilot Chat (Basic) users use the outline.", silent="Ask: what goes first on a briefing?")))
    s.append(player("c5pp", "c5", "d25"))
    s.append(listslide("c5chk", "c5", "Block 5 · check every slide", "Four checks <span class=\"hl\">on every slide.</span>",
        ["<b>Numbers:</b> each time, date and percentage matches the brief.", "<b>Tone:</b> plain words managers can say aloud.", "<b>Nothing added:</b> no promise the brief does not make.", "<b>Contact:</b> where questions go."],
        "Fast to make, quick to check.", n=N(do="Read the four checks, then start Task 2.5.", expect="People find the pilot number changed most often.", silent="Ask: which check is easiest to skip?")))
    s.append(task("c5task", "c5", "t25", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(check("c5q", "c5", f"Your slide says late arrivals fell by 40%. The brief says {D.ATT['pilot_drop']}%. <b>What do you do?</b>",
        [("Keep 40%; it is close enough for a short briefing", 0, "Close is not the same as correct."),
         ("Delete the number", 0, "The number is useful; make it right."),
         (f"Change it to {D.ATT['pilot_drop']}% and check the other numbers", 1, "Right. One changed number means you check them all.")]))
    # Integration · One case, four outputs
    s.append(listslide("c6brief", "c6", "Integration · one case, four outputs", "Your unit. <span class=\"hl\">Four outputs. One review.</span>",
        ["<b>Word:</b> a one-page summary of the case.", "<b>Outlook:</b> a message to the right person.", "<b>Teams:</b> a brief for the meeting in the case.", "<b>Excel or PowerPoint:</b> a summary or a short briefing."],
        "Then the four-point review on each one.", n=N(do="Ask everyone to open their track's case file now.", expect="People ask whether to do all four: two done well beat four done fast.", silent="Read the five case titles.", time="13:40-14:40")))
    s.append(tslide("c6cases", "c6", "Integration · the five cases", "Pick <span class=\"hl\">your track's case.</span>", ["Track", "Case", "File"],
        [[n, D.CASES[k]["title"], D.CASES[k]["file"]] for k, n in D.TRACKS], "Accuracy · Confidentiality · Neutrality · Source alignment.",
        n=N(do="Ask each table which track they are taking.", expect="Most tracks are covered.", silent="Assign a track to anyone undecided.")))
    s.append(tslide("c6review", "c6", "Integration · the four-point review", "Four checks <span class=\"hl\">on every output.</span>", ["Check", "What to look for"],
        [[f"<b>{a}</b>", b] for a, b in C.CHECKS], "Copilot drafts. You check. Authorized HR staff decide.",
        n=N(do="Ask which check catches the most problems in HR drafts.", expect="Accuracy first, then neutrality.", silent="Say confidentiality is the one you cannot undo.")))
    s.append(task("c6task", "c6", "t26", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(timer_slide("c6gallery", "c6", "Integration · 14:30", "Gallery: <span class=\"hl\">one output from each track.</span>",
        "One person per track shows one output and the problem the review caught. 10 minutes.", 10,
        n=N(do="Pick one volunteer per track. Two minutes each.", expect="Most catches are dates and promises.", silent="Show the backup facts for one case.", fallback="If nobody volunteers, show the case facts and ask what a review would catch.")))
    # Wrap
    s.append(listslide("c7bank", "c7", "Wrap · the Prompt Bank by task", "Organize the bank <span class=\"hl\">by task.</span>",
        ["<b>Draft:</b> job descriptions, announcements, vacancy text.", "<b>Compare:</b> policy versions.", "<b>Summarize:</b> threads, meetings, trackers.", "<b>Review:</b> the four-point check."],
        "Tomorrow your best entries become a prompt set and an assistant.", n=N(do="Give five minutes to move today's requests into the bank.", expect="Review entries are the most often missing.", silent="Show your own bank.", time="14:40-15:00")))
    s.append(wrap("w2", "close", "Five apps, <span class=\"hl\">one review.</span>",
        [(1, "You built", "A change table, an announcement, a timeline, two checked figures, a briefing and a case set."), (2, "You found", "3 policy changes, 1 superseded date, 14 duplicates and 1 missing value."), (3, "The habit", "Copilot drafts. You check. Authorized HR staff decide.")],
        "Tomorrow: your best requests become an assistant your colleagues can use."))
    return s

# ------------------------------------------------------------------ Day 3 · Reusable HR Assistants and Applied Capstone
def day3():
    s = opening(3)
    s.append(rule("e0rule", "e0", "Callback · Day 2", "Five apps. <span class=\"hl\">One review before anything goes out.</span>",
        "Yesterday: one case, four outputs, every one checked for accuracy, confidentiality, neutrality and source alignment.",
        n=N(do="Ask: which app saved you the most time yesterday?", expect="Word and Outlook.", say="Three questions on yesterday. Then reuse.", time="09:00-09:10")))
    s.append(check("e0chk1", "e0", "A draft for the Job Evaluation committee includes a <b>pay figure</b> that Copilot worked out. What do you do?",
        [("Remove it; people decide pay", 1, "Right. Copilot organizes. People decide pay."),
         ("Move it to a note at the end of the draft", 0, "A note still puts Copilot's figure in front of the committee."),
         ("Round it to a clean number", 0, "Rounding does not fix who decides.")]))
    s.append(check("e0chk2", "e0", "Yesterday the manpower vacancies were too low. <b>Which check found the cause?</b>",
        [("Sorting the sheet by date", 0, "Dates do not show a missing approval."),
         ("Comparing approved positions with the structure", 1, "Right. One section had 0 approved positions."),
         ("Counting the rows in each sheet against last month's file", 0, "The sheets were all there.")]))
    s.append(check("e0chk3", "e0", "From investigation notes, Copilot writes <b>\u201cEmployee C was careless.\u201d</b> What do you do?",
        [("Keep it if the manager agrees", 0, "Agreement does not make it an event."),
         ("Soften it to \u201cmay have been careless\u201d", 0, "A softer judgment is still a judgment."),
         ("Remove it: it is a judgment, not an event", 1, "Right. Keep events and open questions only.")]))
    # Block 1 · Prompt Gallery
    s.append(story("e1story", "e1", "Block 1 · Reuse before you rebuild", "Thursday 12 November, 09:10",
        "Mutla's L&D team sends course nominations every month. <b>Five people write the same email five different ways</b>, and one always forgets the closing date.",
        "Write it once. <span class=\"hl\">Test it. Share it.</span>", "Find, adapt and save prompts in the Prompt Gallery.",
        n=N(do="Ask: which request do you type again and again?", expect="Reports, replies, nominations.", silent="Offer the nomination email as the example.", time="09:10-09:40")))
    s.append(rule("e1an", "e1", "Block 1 · the picture", "A shared recipe book <span class=\"hl\">for the whole kitchen.</span>",
        "Every cook makes the dish the same way, because everyone uses the same tested recipe.",
        n=N(do="Ask: what makes a recipe worth sharing?", expect="It was tested and it works.", say="Share only requests you have tested on a file.")))
    s.append(term("e1t1", "e1", "Block 1 · the idea", "The Prompt Gallery: <span class=\"hl\">find, save, share.</span>", "Prompt Gallery",
        "In Copilot, the Prompt Gallery has <b>Suggested</b> prompts from Microsoft, <b>Your Prompts</b> that you saved, and <b>Teams</b>: prompts shared with your team.",
        "Like the recipe book…", "…a tested request <b>saved for everyone</b>.", "Suggested is a start. Add the five inputs before you save.",
        n=N(do="Open the Prompt Gallery live (the More options (...) button or a prompt pill below the message box in Copilot Chat).", expect="People find it under the chat box.", silent="Show the three tabs.", fallback="If it does not open, use the player on the next slide.")))
    s.append(player("e1pp", "e1", "d31"))
    s.append(check("e1chk", "e1", "Before you share a request in the Prompt Gallery, <b>what must it have?</b>",
        [("A long title", 0, "A title helps people find it. It does not make it work."),
         ("The five inputs and a check, tested", 1, "Right. Share only what you have tested."),
         ("Your name, today's date and the team it is for", 0, "Nice to have. Not what makes it reliable.")]))
    s.append(listslide("e1names", "e1", "Block 1 · name it so you find it", "Name each prompt <span class=\"hl\">by its task.</span>",
        ["<b>JD</b> · draft from the role sheet", "<b>Policy</b> · compare two versions", "<b>Thread</b> · decisions and owners", "<b>Review</b> · four-point check"],
        "A month from now, the name is all you remember.", n=N(do="Ask everyone to rename one saved prompt now.", expect="Names get shorter and clearer.", silent="Show your own saved names.")))
    s.append(task("e1task", "e1", "t31", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Block 2 · Agent Builder
    s.append(story("e2story", "e2", "Block 2 · Build an HR assistant", "Thursday 12 November, 09:40",
        "Fatma answers the <b>same 20 policy questions</b> every week, by email and by phone. Carry-over days. Transport allowance. Permissions. Nomination deadlines.",
        "The same answer, <span class=\"hl\">twenty times a week.</span>", "Build an HR assistant from approved policies, and test it three ways.",
        n=N(do="Ask: which question does your unit answer most often?", expect="Leave balances, allowances, training dates.", silent="Read three of Fatma's 20 questions.", time="09:40-10:40")))
    s.append(rule("e2an", "e2", "Block 2 · the picture", "A new receptionist <span class=\"hl\">with a binder and a script.</span>",
        "The binder holds the approved policies. The script says what to answer, what never to answer, and when to call HR.",
        n=N(do="Ask: what would you put in the receptionist's script?", expect="Be polite, use the binder, never discuss someone's salary.", say="Instructions are the script. Knowledge is the binder.")))
    s.append(scene("e2scene", "e2", "Block 2 · the picture, drawn", "The script, the binder, <span class=\"hl\">and the phone to HR.</span>",
        "The assistant answers from the approved binder, follows the script, and passes anything personal to HR.",
        "Instructions · Knowledge · Refer to HR.",
        [{"ground": 268}, {"person": (240, 268), "tone": "hot", "label": "Assistant", "anim": "nod"}, {"doc": (110, 170), "tone": "ok", "label": "Policies"},
         {"doc": (370, 170), "label": "Script"}, {"phone": (420, 250), "label": "HR"}, {"person": (60, 268), "label": "Employee", "anim": "bob", "delay": .4},
         {"move": "mail", "path": [(90, 220), (230, 200)], "dur": 4}],
        n=N(do="Point to the binder, the script and the phone.", expect="People connect the phone to the sensitive test.", silent="Ask: when should the assistant pick up the phone?")))
    s.append(term("e2t1", "e2", "Block 2 · the idea", "Instructions: <span class=\"hl\">the script.</span>", "Instructions",
        "What the assistant is, what it answers, its tone, <b>what it must not answer</b>, and <b>when to refer the person to HR</b>. Up to 8,000 characters.",
        "Like the receptionist's script…", "…it decides <b>what may be said</b> and when to pass the call.", "Write the must-not lines first.",
        n=N(do="Read the Must not answer line from the prompt sheet.", expect="People add their own unit's sensitive topics.", silent="Ask: what must your unit's assistant never answer?")))
    s.append(term("e2t2", "e2", "Block 2 · the idea", "Knowledge: <span class=\"hl\">the approved binder.</span>", "Knowledge",
        "The files the assistant answers from. In Agent Builder you can upload <b>up to 20 files</b> from your device, or point to SharePoint. Approved files only.",
        "Like the binder…", "…every policy goes in <b>with its dates</b>.", "Both allowance versions go in, each with the date it applies.",
        n=N(do="Show the five Mutla policy files you will upload.", expect=f"People ask about version 3 of allowances: it goes in, because it applies until version 4 starts on {D.ALLOW_V4_DATE}.", silent="Ask: what goes wrong if only version 4 goes in?", more=["Source: Microsoft Learn, Add knowledge sources in Agent Builder (20 embedded files)."])))
    s.append(listslide("e2steps", "e2", "Block 2 · step by step", "Build it <span class=\"hl\">in six steps.</span>",
        ["<b>New agent</b> in Microsoft 365 Copilot, then <b>Configure</b>.", "<b>Name and description:</b> " + D.AGENT_NAME + ", one line on what it does.", "<b>Instructions:</b> paste the script from the prompt sheet.",
         "<b>Knowledge:</b> upload the five approved policy files.", "<b>Starter prompts:</b> two common questions.", "<b>Try it</b>, fix, then <b>Create</b>."],
        "Agents are limited on a basic label. Use the fallback on the task slide if Agent Builder is missing.",
        n=N(do="Build it live on the presenting laptop while you talk through the steps.", expect="People switch between Configure and Try it as they build.", silent="Ask: which step would you skip? (None.)", fallback="If the live build fails, use the player on the next slides.")))
    s.append(tslide("e2tests", "e2", "Block 2 · three tests", "Test it with <span class=\"hl\">hard questions.</span>", ["Test", "Question", "Pass if"],
        [[a, b, d] for a, b, _c, d in D.AGENT_TESTS], "Normal, incomplete, sensitive. Before anyone else uses it.",
        n=N(do="Read the sensitive test aloud. Ask what a pass looks like.", expect="It declines and refers to HR.", silent="Ask: which test do people forget?")))
    s.append(cards3("e2never", "e2", "Block 2 · what it must never do", "Three things <span class=\"hl\">it must never do.</span>",
        [("red", "Never", "Name a salary", "No pay or allowance of a named person.", ""), ("red", "Never", "Decide a case", "No exception, no approval, no warning.", ""),
         ("amber", "Ask first", "Guess a situation", "Ask for the grade or the case before answering.", "")],
        "If it does any of these in Try it, fix the instructions.", n=N(do="Map each card to a line in the instructions.", expect="People see the Ask first line in action.", silent="Ask: which card would the incomplete test catch?")))
    s.append(player("e2pp", "e2", "d32"))
    s.append(check("e2chk", "e2", "Which part of the assistant holds the <b>approved policies</b> it answers from?",
        [("Instructions", 0, "Instructions say how to behave, not which files to use."),
         ("Description", 0, "The description tells people what it is for."),
         ("Knowledge", 1, "Right. Knowledge holds the approved files.")]))
    s.append(task("e2task", "e2", "t32", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(check("e2chk2", "e2", "In Try it, the assistant answers a question about <b>overtime pay</b>. No overtime policy is in Knowledge. What now?",
        [("Add: answer only from the files, or refer to HR", 1, "Right. Then test it again."),
         ("Fine. The answer sounds right, so mark it as a pass", 0, "It has no source. It guessed."),
         ("Add more starter prompts", 0, "Starter prompts do not stop a guess.")]))
    s.append(rule("e2deb", "e2", "Block 2 · debrief", "A test you did not run <span class=\"hl\">is a problem you meet later.</span>",
        "Run the three tests again after every change to the instructions or the files. Then let one colleague try it before your unit does.",
        n=N(do="Ask two people which test failed first and how they fixed it.", expect="The incomplete test fails most: it answers without asking for the grade.", silent="Show the backup test table.", say="Every change means the three tests again.")))
    # Capstone briefing
    s.append(story("e3story", "e3", "Capstone", "Thursday 19 November, 10:55",
        "Your manager asks for <b>one recurring task you will do faster from next month</b>, in a way a colleague could run while you are on leave. You have a new case, Copilot, and 100 minutes.",
        "A new case <span class=\"hl\">proves the method.</span>", "Complete a new case by chaining two Copilot apps, and save a prompt set a colleague can run.",
        n=N(do="Hand out the five capstone files by track.", expect="People notice the case is new.", silent="Read one case aloud.", time="10:55-11:10")))
    s.append(tslide("e3cases", "e3", "Capstone · the five cases", "Your track. <span class=\"hl\">A case you have not seen.</span>", ["Track", "Case", "File"],
        [[n, D.CAPSTONE[k]["title"], D.CAPSTONE[k]["file"]] for k, n in D.TRACKS], "New to you on purpose: it tests the method, not your memory.",
        n=N(do="Confirm each person's track.", expect="Tracks match yesterday's.", silent="Assign anyone undecided.")))
    s.append(listslide("e3core", "e3", "Capstone · core and extension", "Core for everyone. <span class=\"hl\">Extension if you finish.</span>",
        ["<b>Core:</b> plan the steps, chain at least two Copilot apps, five-input requests grounded in the case files.", "<b>Core:</b> review every output with the four-point check.",
         "<b>Core:</b> save the requests as a prompt set in Word.", "<b>Extension:</b> connect it to your HR assistant, or add a starter prompt."],
        "At 13:30 a colleague from another unit runs your set with no instructions.", n=N(do="Stress the 13:30 peer test.", expect="People start writing clearer requests at once.", silent="Ask: what would a colleague need to run your set?")))
    s.append(listslide("e3self", "e3", "Capstone · the self-check", "Five checks <span class=\"hl\">before the peer test.</span>", C.SELFCHECK,
        "The same list is on the Day 3 lab page.", n=N(do="Point to the Day 3 lab page on the hub.", expect="People open it on a second tab.", silent="Read the last check aloud.")))
    _t33 = dict(DEMOS["t33"]); DEMOS["t33"].update(minutes=C.CAPSTONE_PART1, title="A tested workflow, part 1")
    s.append(task("e3task", "e3", "t33",
        n=N(expect="A plan and the first requests, ready to continue after lunch.", do="Start the timer. Walk the room. Ask each person what they found so far.", time="11:10-11:35", more=[f"Part 1 is {C.CAPSTONE_PART1} minutes before lunch. Part 2 is {_t33['minutes'] - C.CAPSTONE_PART1} minutes after lunch, on the next slide."])))
    DEMOS["t33"].update(minutes=_t33["minutes"], title=_t33["title"])
    # Build part 2 and peer test
    s.append(timer_slide("e4build", "e4", "Capstone · build, part 2", "Outputs, review, <span class=\"hl\">the prompt set.</span>",
        "Finish your outputs, review each one, and save the requests as a prompt set. The peer test starts at 13:30.", 75,
        n=N(do="Start the timer after lunch. Walk the room. Ask each person to show one review.", expect="Most people finish the core by 13:00.", silent="Ask the quietest table what step they are on.", fallback="Anyone stuck uses the plan request on the Task 3.3 slide.", time="12:15-13:30")))
    s.append(rule("e4rule", "e4", "Peer test", "If a colleague needs you to explain it, <span class=\"hl\">it is not finished.</span>",
        "Hand your prompt set to someone from another unit. Say nothing. Watch where they stop.",
        n=N(do="Pair people from different units.", expect="Some pairs ask to explain first: do not allow it.", say="The silence is the test.", time="13:30-13:50")))
    s.append(task("e4task", "e4", "t34"))
    s.append(listslide("e4fixes", "e4", "Peer test · common fixes", "The fixes <span class=\"hl\">most sets need.</span>",
        ["<b>Name the files</b> each request needs.", "<b>Say what to do</b> when data is missing.", "<b>Add the output format.</b>", "<b>End with the check.</b>"],
        "Each fix is a missing input, not a new task.", n=N(do="Ask which fix each pair made.", expect="Naming the files is the most common.", silent="Show the four fixes and ask for hands.")))
    s.append(timer_slide("e5share", "e5", "Share-outs · 14:05", "One minute each: <span class=\"hl\">what broke, and the fix.</span>",
        "Say what your colleague could not do, and what you changed. One minute.", 15,
        n=N(do="Go round the room fast. Keep to one minute each.", expect="Missing files and missing formats.", silent="Start with your own example.", time="14:05-14:20")))
    s.append(mapslide("e6map", "e6", "after"))
    s.append(wrap("w3", "close", "Build it once. <span class=\"hl\">Test it. Let a colleague run it.</span>",
        [(1, "You built", "An HR assistant, a capstone workflow and a tested prompt set."), (2, "You found", "Where your work depended on you, and fixed it."), (3, "The habit", "Copilot drafts. You check. Authorized HR staff decide.")],
        "Your first week: one five-input request a day. Your first month: one tested set for your unit."))
    return s

TOPICS = {1: {"open": "Opening", "b1": "Block 1 · How generative AI and Copilot work", "b2": "Block 2 · Writing a clear prompt", "b3": "Block 3 · Draft, fix and check in Word", "b4": "Block 4 · From policy to people", "b5": "Prompt Bank and wrap", "close": "Close"},
          2: {"open": "Opening", "c0": "Callback quiz", "c1": "Block 1 · Word", "c2": "Block 2 · Outlook", "c3": "Block 3 · Teams", "c4": "Block 4 · Excel", "c5": "Block 5 · PowerPoint", "c6": "Integration · One case", "c7": "Wrap", "close": "Close"},
          3: {"open": "Opening", "e0": "Callback quiz", "e1": "Block 1 · Prompt Gallery", "e2": "Block 2 · Agent Builder", "e3": "Capstone", "e4": "Peer test", "e5": "Share-outs", "e6": "Post-MAP and survey", "close": "Close"}}
DAYFN = {1: day1, 2: day2, 3: day3}
