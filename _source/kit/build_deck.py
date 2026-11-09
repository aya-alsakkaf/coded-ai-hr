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
 1: [("Opening", "g-mark", ["open"]), ("Block 1", "g-code", ["b1"]), ("Block 2", "g-frame", ["b2"]), ("Block 3", "g-impact", ["b3"]), ("Block 4", "g-code", ["b4"]), ("Close", "g-progress", ["b5", "close"])],
 2: [("Opening", "g-mark", ["open", "c0"]), ("Word", "g-code", ["c1"]), ("Outlook", "g-frame", ["c2"]), ("Teams", "g-impact", ["c3"]), ("Excel", "g-code", ["c4"]), ("PowerPoint", "g-frame", ["c5"]), ("Case", "g-impact", ["c6"]), ("Close", "g-progress", ["c7", "close"])],
 3: [("Opening", "g-mark", ["open", "e0"]), ("Gallery", "g-code", ["e1"]), ("Agent", "g-frame", ["e2"]), ("Capstone", "g-impact", ["e3", "e4", "e5"]), ("Close", "g-progress", ["e6", "close"])],
}
FLOW = {
 1: (["B1", "B2", "B3", "B4", "Save"], {"b1": 0, "b2": 1, "b3": 2, "b4": 3, "b5": 4}),
 2: (["Word", "Outlook", "Teams", "Excel", "PPT", "Case"], {"c1": 0, "c2": 1, "c3": 2, "c4": 3, "c5": 4, "c6": 5}),
 3: (["Gallery", "Agent", "Capstone", "Peer test"], {"e1": 0, "e2": 1, "e3": 2, "e4": 3}),
}
COVER_NOTES = {
 1: N(do="Welcome. Introduce yourself and CODED in one minute.", more=["Housekeeping: breaks at 10:30 and 13:35, lunch and Dhuhr at 11:35. Prayer room and toilets.",
      "Sign-in check: every laptop opens Copilot Chat and is signed in with a work account. Helpers walk the room.", "Ask everyone to read the label under their name at the bottom of the Microsoft 365 home page. Note who has an M365 Copilot label."],
      say="Quick hands-up: who has used Copilot at work this month?", silent="ask who has typed one question into any AI chat. That is enough to start.", time="09:00-09:10"),
 2: N(do="Welcome back.", more=["Sign-in check: Copilot Chat open, the tracker and the thread file downloaded.", "The callback quiz comes after today's map."],
      say="Yesterday you wrote five-input requests and traced every line to its source. Today the same habit goes into five apps.", silent="ask one person which request they tried at work last night.", time="09:00"),
 3: N(do="Welcome to the last day.", more=["Check: Agent Builder opens on at least the presenting laptop (New agent).", "Remind the room: post-MAP and survey at 14:20, certificates at 14:40."],
      say="Today your best requests become things a colleague can use without you.", silent="ask who saved a request in the Prompt Bank yesterday.", time="09:00"),
}
OUTCOMES_NOTES = {d: N(do="Read the four outcomes. Ask which one matters most for their unit.", expect="Most people pick the checking outcome.",
                       say="Four things you will do yourself today, on fictional Mutla files.", silent="pick the one you use most and say why.") for d in (1, 2, 3)}
ROAD = {d: {"title": "One company. <span class=\"hl\">Five HR units.</span>",
            "n": N(do="Point to the breaks: the cup button starts the break clock.", say="Mutla Oil Company is made up, so you can make mistakes safely. Pick the unit track closest to your job.")} for d in (1, 2, 3)}
CLOSE = {
 1: {"big": "Request → draft → <span class=\"hl\">check.</span>", "next": "Tomorrow: Word, Outlook, Teams, Excel and PowerPoint, and one case from your own unit.",
     "n": N(do="Recap the day in one line.", more=["Remind everyone to bring the same laptop and the recurring task they wrote down."], say="Thank you. See you tomorrow at 9:00.")},
 2: {"big": "Five apps. <span class=\"hl\">One review.</span>", "next": "Tomorrow: an HR assistant, a new case, and a colleague who tests your work.",
     "n": N(do="Recap the day in one line.", more=["Ask everyone to finish organizing the Prompt Bank tonight if they did not."], say="Thank you. See you tomorrow at 9:00.")},
 3: {"big": "Copilot drafts. <span class=\"hl\">People decide.</span>", "next": "Thank you. Copilot drafts. You check. Authorized HR staff decide.",
     "n": N(do="Recap the three days in one line. Hand out certificates.", more=["Point to the take-home guide and the safe-use card."], say="Start with one green task at work this week.")},
}

R = D.ROLES["cmp"]

# ------------------------------------------------------------------ Day 1 · Directing Copilot for Reliable HR Work
def day1():
    opener = [story("b0story", "open", "Opener · one job description", "Sunday 1 November, 09:20",
        f"Yousef, the HR Section Head, needs a job description for the new <b>{R['title']}</b> before the evaluation round. Abdulaziz opens Copilot and types one short line.",
        "Same tool. Same role. <span class=\"hl\">Watch what the request changes.</span>", "See why the request decides the quality of the draft.",
        n=N(do="Read the story. Ask: what would you type?", expect="Short answers like “write a JD for a compensation analyst”.", silent="Say what most people type: one short line.")),
        showcase("ws", "open", CD.SHOWCASE, n=N(do="Press → for each step.", more=["Steps 2 and 3: the weak request and its answer. Read the red flags.",
                 "Steps 4 to 8: the five inputs, one per press. Ask what each adds.", "The strong answer: point at the blank grade line.", "Optional: run both requests live (prompt sheet, Demo 1.0)."],
                 silent="ask before the five inputs: would you send the weak draft to the committee?", say="Same tool. Same role. The only change is what Copilot was given.", time="10 min"))]
    s = opening(1, opener=opener)
    # Block 1 · How Copilot produces an answer
    s.append(story("b1story", "b1", "Block 1 · How Copilot produces an answer", "Monday 2 November, 08:40",
        f"Fatma in Personnel asks Copilot: <b>“How many days of leave can staff carry over?”</b> The answer comes at once: <b>30 days.</b> Mutla's policy says {D.LEAVE['carry']}.",
        "Confident, fast <span class=\"hl\">and wrong.</span>", "See why Copilot can write a confident sentence that is wrong.",
        n=N(do="Ask: has an AI tool ever given you a wrong number at work?", expect="Two or three short stories.", silent="Share one of your own.", time="09:30-10:30")))
    s.append(rule("b1an", "b1", "Block 1 · the picture", "Your phone keyboard guesses <span class=\"hl\">your next word.</span>",
        "Copilot does the same thing with a much bigger memory. Its guesses sound right because it learned from a huge amount of text.",
        n=N(do="Ask two people to type “I will be there in” on their phone and read the suggestions.", expect="“5 minutes”, “a bit”, “10”.", say="Your keyboard does not know where you are. It guesses what usually comes next.")))
    s.append(term("b1t1", "b1", "Block 1 · the idea", "What Copilot <span class=\"hl\">really does.</span>", "Next-word prediction",
        "Copilot writes by <b>predicting the next word</b>, one word at a time, from patterns in the text it learned from.",
        "Like your phone keyboard…", "…it picks a <b>likely</b> next word. Numbers and dates are words too.", "It predicts. Without the source, it guesses or searches the web, and nothing checks it against Mutla's policy.",
        n=N(do="Link back to the phone keyboard: same idea, far bigger memory.", expect="People connect “likely” with “not checked”.", silent="Ask: is the most common number always Mutla's number?")))
    s.append(llmslide("b1llm", "b1", "Block 1 · live widget", "It writes by guessing <span class=\"hl\">the next word.</span>",
        "At each step, every possible next word gets a score. The model picks one and repeats.", f"It predicts <b>likely</b> words. Mutla's policy says {D.LEAVE['carry']}, but 30 is more common.",
        n=N(do="Read the start aloud. Ask the room for the next word, then click it.", more=["Click Pick the top word: 30 wins, because it is common in policies everywhere.", "Start again and pick 15: Mutla's real number is only the second guess.", "Pick camel (1%). The sentence still sounds confident.", "The percentages are illustrative."],
            say="It is not reading our policy. It is predicting a number that often follows these words.", silent="ask one person to choose for the room.", time="7 min")))
    s.append(term("b1t2", "b1", "Block 1 · the risk", "Fluent <span class=\"hl\">and wrong.</span>", "Hallucination",
        "When Copilot writes something that <b>sounds right but is not true</b>: a wrong number, date, rule or name.",
        "A likely next word…", "…is not always a <b>true</b> one. Nothing checks it for you.", "Check every number, date and rule against the approved source.",
        n=N(do="Go back to Fatma's answer: the number was likely, not true.", expect="Hallucination means fluent and wrong.", silent="Ask: what would have caught Fatma's 30 days?")))
    s.append(check("b1chk1", "b1", "An employee forwards you Copilot's answer: <b>Hajj leave is 30 days.</b> <b>What do you check before you reply?</b>",
        [("How sure Copilot sounded in its answer", 0, "Sounding sure is not evidence. Check the source."),
         ("A second answer from a new Copilot chat", 0, "A second prediction is not a check. Read the policy."),
         ("The Hajj section of the leave policy", 1, f"Right. The policy says {D.LEAVE['hajj']} days. The approved policy decides.")]))
    s.append(rule("b1key", "b1", "Block 1 · a second picture", "A colleague with <span class=\"hl\">your keycard.</span>",
        "They can open every door you can open, and no other door. That is how Copilot reaches your work files.",
        n=N(do="Ask: if a colleague borrows your keycard, which rooms can they enter?", expect="Only the rooms I can enter.", say="Copilot works with your permissions. It never gets more than you have.")))
    s.append(scene("b1scene", "b1", "Block 1 · the picture, drawn", "Copilot opens <span class=\"hl\">only your doors.</span>",
        "With a Microsoft 365 Copilot license, Copilot can use the files, emails and chats you already have permission to open. A restricted folder stays closed.",
        "Your permissions decide what Copilot can see.",
        [{"ground": 268}, {"person": (80, 268), "tone": "hot", "label": "You", "anim": "nod"}, {"building": (250, 268), "tone": "dim"},
         {"lock": (390, 150), "tone": "bad", "label": "Restricted"}, {"doc": (250, 150), "tone": "ok", "label": "Your files"},
         {"move": "doc", "path": [(120, 210), (250, 170)], "dur": 4}, {"pill": "Your access", "at": (130, 40), "tone": "hot"}, {"pill": "No access", "at": (370, 40)}],
        n=N(do="Point to the open file and the locked folder.", expect="People ask about shared drives: same rule, it depends on their access.", silent="Ask: could Copilot show you a colleague's appraisal?", say="If you cannot open it, Copilot cannot use it.")))
    s.append(term("b1t3", "b1", "Block 1 · the idea", "What Copilot <span class=\"hl\">can see.</span>", "Permissions",
        "With a Microsoft 365 Copilot license (the M365 Copilot (Premium) label), Copilot uses <b>only what you can already open</b>. On Copilot Chat (Basic), it uses <b>the web and the files you upload</b>, and you also get Copilot in Outlook. M365 Copilot (Basic) adds Copilot in Word, Excel and PowerPoint.",
        "Like the borrowed keycard…", "…it opens <b>your</b> doors, never more.", "Your access is the limit. The decision about what to share is still yours.",
        n=N(do="Ask everyone to look at the label under their name now.", expect="A mix of Basic and Premium in most rooms.", silent="Show your own label on the screen.", fallback="Anyone unsure: open the Microsoft 365 home page (m365.cloud.microsoft) and read the label under your name, at the bottom.")))
    s.append(tslide("b1lic", "b1", "Block 1 · your label", "Read the label <span class=\"hl\">under your name.</span>", ["Label", "What Copilot can use", "In this workshop"],
        [["Copilot Chat (Basic)", "The web, files you upload, and Copilot in Outlook", "Every task works with uploaded files"],
         ["M365 Copilot (Basic)", "The web and files you upload, plus standard Copilot in Word, Excel and PowerPoint", "Every task, and most Day 2 app demos"],
         ["M365 Copilot (Premium)", "Your files, emails, chats and meetings (the Microsoft 365 Copilot license)", "Full Copilot in the apps, including Teams recaps"]],
        "Every task works in Copilot Chat with a file attached.",
        n=N(do="Ask people with an M365 Copilot label (Basic or Premium) to raise a hand: they can try the in-app demos on Day 2. Teams recaps need Premium.", expect="A mix of the three labels.", silent="Say which label the training account has.", more=["Source: Microsoft Support, What Copilot license do I have (cheat sheet, Part 4)."])))
    s.append(check("b1chk2", "b1", "Khaled has an M365 Copilot (Premium) label. A folder of salary files is closed to him. <b>Can Copilot use those files for him?</b>",
        [("Yes, if his manager has access to the folder", 0, "No. Copilot never opens a door that is closed to him."),
         ("Yes, if he names the folder in his prompt to Copilot", 0, "Asking does not change his permissions."),
         ("No. It uses only what he can already open", 1, "Right. His permissions are the limit.")]))
    s.append(listslide("b1seats", "b1", "Block 1 · one engine, many seats", "Copilot Chat and <span class=\"hl\">Copilot in the apps.</span>",
        ["<b>Copilot Chat:</b> ask, upload a file, draft. Works on every label.", "<b>Copilot in Word, Outlook, Teams, Excel, PowerPoint:</b> the same engine, inside the app you already use.",
         "<b>Agent Builder:</b> an assistant with your instructions and approved files (Day 3).", "<b>The same five inputs</b> work in every seat."],
        "Choose the seat. The request matters more than the seat.", n=N(do="Show where Copilot sits in Word on the presenting laptop, if it has an M365 Copilot label.", expect="People recognize the Copilot button.", silent="Ask: where do you spend most of your day?")))
    s.append(player("b1pp", "b1", "d11"))
    s.append(check("b1chk3", "b1", "The second answer was right. <b>What made it easy to check?</b>",
        [("It named its source: the policy section", 1, "Right. You open section 4 and confirm in seconds."),
         ("It was longer and more detailed", 0, "Length proves nothing."),
         ("It used formal HR words", 0, "Formal words sound right. They prove nothing.")]))
    s.append(task("b1task", "b1", "t11"))
    s.append(rule("b1deb", "b1", "Block 1 · debrief", "Fluent is <span class=\"hl\">not the same as correct.</span>",
        "Every statement in that answer sounded certain. Only the policy could tell the right ones from the wrong ones.",
        n=N(do="Ask two pairs for one mistake each and the section that fixes it.", expect="Carry-over, emergency leave and notice.", silent="Read the first mistake yourself and ask for the section.", say="Certainty is a writing style, not evidence.")))
    # Block 2 · Rules before the first request
    s.append(story("b2story", "b2", "Block 2 · Rules before the first request", "Tuesday 3 November, 10:50",
        "Abdulaziz pastes a salary exception memo into a chat to make it sound professional. It has <b>two names and their salaries.</b> His finger is on Enter. He stops.",
        "The draft might be good. <span class=\"hl\">The decision is wrong.</span>", "Sort HR tasks before you type, and redact before Copilot sees anything.",
        n=N(do="Ask: why did Abdulaziz stop?", expect="Names, salaries, personal data.", silent="Ask: what would you do in his place?", time="10:45-11:35")))
    s.append(stats("b2real", "b2", "When it was real · 2023", "It happened at <span class=\"hl\">a global company.</span>",
        [(str(D.SAMSUNG["incidents"]), "incidents", "Employees pasted source code and recorded meeting notes into a public AI chat."),
         ("2023", "the year", "Weeks after the company allowed the tool at work."),
         (D.SAMSUNG["limit"], "per question", "The emergency limit on uploads that followed.")],
        "One paste can leave the company forever.", src=f"Source: {D.SAMSUNG['src'][0]}.",
        n=N(do="Tell the story in two sentences: staff wanted help with code and meeting minutes.", expect="People notice the meeting notes: that is HR work too.", silent="Ask: what in your week is like those meeting notes?", more=["The company was Samsung; the report came from Korean media via The Register."])))
    s.append(rule("b2an", "b2", "Block 2 · the picture", "A new temp drafts letters. <span class=\"hl\">They never sign them.</span>",
        "On day one, a temp can prepare drafts. They do not decide a raise, a grade or a warning. Copilot sits in the same seat.",
        n=N(do="Ask: what would you never let a temp decide on day one?", expect="Pay, grades, discipline, hiring.", say="Copilot is fast and tireless. It is still the temp.")))
    s.append(cards3("b2groups", "b2", "Block 2 · three groups", "Sort the task <span class=\"hl\">before you type.</span>",
        [(a, b, c, "") for a, b, c in C.GROUPS], "Grades, pay, ratings, discipline and selection stay with authorized HR staff.",
        n=N(do="Ask for one task from each group from the room.", expect="Job descriptions and recaps go to drafts; grades stay with people.", silent="Give your own example for each group.")))
    s.append(term("b2t1", "b2", "Block 2 · the idea", "Some decisions <span class=\"hl\">stay with people.</span>", "Human decision",
        "A decision that changes a person's pay, grade, rating, record or job is made by <b>authorized HR staff</b>. Copilot may prepare the file. It never decides.",
        "Like the temp who drafts…", "…Copilot <b>prepares</b>. A person with authority <b>decides</b>.", "Drafts, yes. Decisions about people, no.",
        n=N(do="Ask: which decisions in your unit change a person's pay or record?", expect="Grades, allowances, warnings, promotions.", silent="Name two from Mutla: a grade and an allowance exception.")))
    s.append(check("b2chk1", "b2", "Noura works on next quarter's training. <b>Which step stays with authorized HR staff?</b>",
        [("Approving which employees join a course", 1, "Right. A choice about a person stays with people."),
         ("Booking the training room for the course", 0, "A booking is not a decision about a person."),
         ("Checking course dates against the training calendar", 0, "Copilot can help. A person checks it.")]))
    s.append(rule("b2light", "b2", "Block 2 · a second picture", "Traffic lights <span class=\"hl\">for your data.</span>",
        "Green: go. Amber: slow down and check the conditions. Red: stop, whatever the tool can do.",
        n=N(do="Ask: what does amber mean in real traffic?", expect="Slow down, check, then decide.", say="Before you type, look at the light.")))
    s.append(cards3("b2safe", "b2", "Block 2 · the safe-use card", "Green, amber, red: <span class=\"hl\">sort before you type.</span>",
        [(k, h.split(":")[0], h.split(": ", 1)[1][0].upper() + h.split(": ", 1)[1][1:], p, " · ".join(ex_)) for k, h, p, ex_ in C.SAFE], "Your company's AI and data policy comes first.",
        n=N(do="Read one example from each card.", expect="People ask where their own tasks fit: answer in the sort.", silent="Ask: are the Mutla files green or red? (Green: fictional.)")))
    s.append(rule("b2policy", "b2", "Block 2 · policy first", "Your company's policy <span class=\"hl\">comes first.</span>",
        "Before the color, ask: does my company approve this Copilot account for this data? If there is no approved account, amber becomes red.",
        n=N(do="Ask: who knows their company's AI policy?", expect="Few hands. Tell them to ask IT or information security this week.", say="The card is a habit. Your company's policy is the rule.")))
    s.append(sortslide("b2sort", "b2", f"Demo {C.SAFE_SKILL} · The safe-use card", 'Green, amber or red? <span class="hl">Tap a card.</span>', C.SORT, C.SORT_LABELS, did="d12",
        n=N(more=["Amber depends on your company's approved account. Without one, amber becomes red."])))
    s.append(term("b2t2", "b2", "Block 2 · the idea", "Redact <span class=\"hl\">before you ask.</span>", "Redact",
        "To <b>redact</b> is to remove or replace every detail that identifies a person or is sensitive, before the text goes anywhere.",
        "“Bader, civil ID…, salary…”", "“Employee A, [ID removed], [salary removed]”", "Replace names with roles. Remove numbers, salaries and medical details.",
        n=N(do="Show one sentence before and after on the screen.", expect="People ask whether roles are still useful: yes, the facts stay.", silent="Ask: what is left in the note after redaction? (The facts and the request.)")))
    s.append(listslide("b2moves", "b2", "Block 2 · redact in four moves", "Four moves <span class=\"hl\">before any prompt.</span>",
        ["<b>Names</b> become roles: Employee A, Colleague B.", "<b>ID and phone numbers</b> are removed.", "<b>Salaries and allowances</b> of named people are removed.", "<b>Medical and case details</b> that point to a person are removed."],
        "Then read it once more: could someone outside HR tell who this is?", n=N(do="Walk through the four moves with the case note open.", expect="Most people miss the phone number.", silent="Ask: which move is easiest to forget?")))
    s.append(check("b2chk2", "b2", "Fatma has redacted a sick-leave complaint. <b>Which detail can stay in the text she gives Copilot?</b>",
        [("The civil ID, since HR holds it anyway", 0, "A civil ID never goes into a prompt."),
         ("The dates of the absence", 1, "Right. Facts about the case can stay once nobody can tell who it is."),
         ("The diagnosis, so the reply sounds caring", 0, "Medical details stay out. The reply can be kind without them.")]))
    s.append(player("b2pp2", "b2", "d12b"))
    s.append(task("b2task", "b2", "t12", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Block 3 · The five inputs
    s.append(story("b3story", "b3", "Block 3 · The five inputs", "Wednesday 4 November, 12:15",
        f"Fatma must update the <b>{D.OLD_JD['year']} job description</b> for the {D.OLD_JD['title']} role in her unit. It still mentions a typewriter and a fax machine. The evaluation round starts next week.",
        "Try it by hand first. <span class=\"hl\">Then we compare.</span>", "Write a request with the five inputs.",
        n=N(do="Hand out the 2019 job description. Start the next slide's timer.", expect="People laugh at the fax machine.", silent="Read the oldest duty aloud.", time="12:15-13:35")))
    s.append(timer_slide("b3timer", "b3", "Felt problem · 8 minutes", "Update it <span class=\"hl\">by hand.</span>",
        f"Open {CD.F['oldjd']}. Rewrite it in the 2026 template for 8 minutes. No AI. Then stop, wherever you are.", 8,
        n=N(do="Start the timer. Walk the room.", expect="Most people finish about half.", silent="Ask how far they got.", say="Remember this feeling. It is the cost we are about to cut.")))
    s.append(listslide("b3one", "b3", "Block 3 · the one-line request", "One line. Fast. <span class=\"hl\">And not usable.</span>",
        ["It invents duties nobody approved.", "It adds a team to manage and a grade.", "It ignores Mutla's template.", "It sounds polished, so the errors are easy to miss."],
        "A fast answer with no inputs needs more fixing.", n=N(do="Run the one-line request live, or show the weak answer from the opener.", expect="The room spots the invented grade first.", silent="Ask: which line would the committee reject first?")))
    s.append(rule("b3an", "b3", "Block 3 · the picture", "Brief Copilot like <span class=\"hl\">a new colleague.</span>",
        "On the first day, a new colleague needs to know what to do, why, with which facts, in what voice, and which rules to follow.",
        n=N(do="Ask: what do you tell a new colleague before their first task?", expect="What to do, who it is for, which file, how it should look.", say="You would never say only “write a JD”. You would brief them.")))
    s.append(scene("b3scene", "b3", "Block 3 · the picture, drawn", "A good brief has <span class=\"hl\">five parts.</span>",
        "You give a new colleague five things before the first task. A request is the same brief, written down.",
        "Instructions · Context · Data · Tone · Approved sources.",
        [{"ground": 268}, {"building": (240, 268), "tone": "dim"}, {"person": (86, 268), "tone": "hot", "label": "You", "anim": "nod"}, {"person": (396, 268), "label": "Copilot", "anim": "bob", "delay": .4},
         {"move": "doc", "path": [(118, 214), (240, 168), (362, 214)], "dur": 5},
         {"pill": "Instructions", "at": (120, 30), "tone": "hot", "delay": 0}, {"pill": "Context", "at": (360, 30), "tone": "hot", "delay": 1.2},
         {"pill": "Data", "at": (90, 74), "tone": "hot", "delay": 2.4}, {"pill": "Tone", "at": (240, 74), "tone": "hot", "delay": 3.6}, {"pill": "Sources", "at": (390, 74), "tone": "hot", "delay": 4.8}],
        n=N(do="Point to each part as it appears. Ask what goes wrong if one is missing.", expect="No data: invented duties. No sources: wrong template.", silent="Name one missing part yourself, then ask for the next.", say="A request is a brief. Five parts, every time.")))
    s.append(tslide("b3five", "b3", "Block 3 · the five inputs", "Five inputs <span class=\"hl\">before you press Send.</span>", ["Input", "It tells Copilot", "Example"],
        [[f"<b>{a}</b>", b, c] for a, b, c in D.INPUTS], "Instructions · Context · Data · Tone · Approved sources.",
        n=N(do="Map each input to the new-colleague brief.", expect="Data and Approved sources are the ones people forget.", silent="Ask: which input would have stopped the invented grade?")))
    s.append(term("b3t1", "b3", "Block 3 · two inputs people mix up", "Data <span class=\"hl\">is not the same as sources.</span>", "Data and approved sources",
        "<b>Data</b> is the facts of this case: the role information, the figures. <b>Approved sources</b> are the rules to follow: the template, the policy.",
        "Data says <b>what is true here</b>…", "…sources say <b>how it must be done</b>.", "Give both. Without rules, Copilot ignores the template. Without facts, it invents details.",
        n=N(do="Hold up the role information, then the template: facts, then rules.", expect="People see that both files are needed.", silent="Ask: is the leave policy data or a source? (A source.)")))
    s.append(tslide("b3gcse", "b3", "Block 3 · Microsoft's words", "Same idea, <span class=\"hl\">Microsoft's words.</span>", ["Microsoft says", "Our five inputs"],
        [[a, b] for a, b in D.GCSE], "Use whichever words you remember. Give Copilot all of it.",
        n=N(do="Say Microsoft's training uses Goal, Context, Source, Expectations.", expect="People are relieved the two match.", silent="Ask: which of ours is Microsoft's Source?")))
    s.append(player("b3pp", "b3", "d13"))
    s.append(check("b3chk", "b3", "Copilot's job description uses a 2019 layout, not Mutla's 2026 template. <b>Which input would have stopped it?</b>",
        [("Tone: formal, neutral and in plain English", 0, "Tone changes the voice, not the layout."),
         ("Approved sources: the attached 2026 template", 1, "Right. Approved sources say how it must be done."),
         ("Context: the evaluation round starts next week", 0, "Context explains why. It does not set the layout.")]))
    s.append(task("b3task", "b3", "t13", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    s.append(check("b3chk2", "b3", "Your Request 3 draft still ends with <b>“Grade 7”</b>. What do you do?",
        [("Keep it, since Copilot used the template", 0, "The template says the grade stays blank."),
         ("Change it to the grade you think is right", 0, "That is still a decision for the committee."),
         ("Delete it; the grade is the committee's", 1, "Right. The committee sets grades.")]))
    # Block 4 · Grounding and checking
    s.append(story("b4story", "b4", "Block 4 · Grounding and checking", "Thursday 5 November, 13:50",
        "Hessa's grounded draft looks perfect. Then she reads it twice: <b>“Manages a team of six analysts.”</b> and <b>“Grade 8.”</b> Neither is in the role information.",
        "Grounded is better. <span class=\"hl\">It is not finished.</span>", "Ask for the source of every line, and delete what has none.",
        n=N(do="Ask: how would you find these two lines in a three-page draft?", expect="Read every line against the role sheet.", silent="Point out that the two lines sound the most official.", time="13:50-14:35")))
    s.append(rule("b4an", "b4", "Block 4 · the picture", "An auditor ticks <span class=\"hl\">every line against a receipt.</span>",
        "A line with no receipt is not paid. A line in a draft with no source is not sent.",
        n=N(do="Ask: what does an auditor do with an expense that has no receipt?", expect="Rejects it or asks for proof.", say="Treat every line of a Copilot draft like an expense claim.")))
    s.append(term("b4t1", "b4", "Block 4 · the idea", "Ask Copilot <span class=\"hl\">to show its receipts.</span>", "Source trace",
        "A table where <b>every line of the draft</b> shows the line of the source it came from, or says <b>NOT IN SOURCE</b>.",
        "Like the auditor's receipts…", "…every line has its source, or it goes.", "No source, no line.",
        n=N(do="Show a two-line source trace on the screen.", expect="People like that NOT IN SOURCE does the searching.", silent="Ask: what do you do with a NOT IN SOURCE line?")))
    s.append(cards3("b4fail", "b4", "Block 4 · three ways a draft fails", "Three failures <span class=\"hl\">to look for.</span>",
        [("Unsupported claim", "A line with no source", "“Manages a team of six.”", ""), ("Missing information", "A source line left out", "A duty from the role sheet is gone.", ""),
         ("Confident mistake", "A source line changed", "15 days became 30.", "")],
        "The source trace catches the first. Reading the source catches the other two.",
        n=N(do="Ask for one real example of each from Task 1.3.", expect="Unsupported claims are the most common.", silent="Use the three examples on the slide.")))
    s.append(scene("b4scene", "b4", "Block 4 · the picture, drawn", "Every line, <span class=\"hl\">ticked or crossed.</span>",
        "The draft sits next to the role information. Each line gets a tick and its source, or a cross and NOT IN SOURCE.",
        "No source, no line.",
        [{"ground": 268}, {"doc": (130, 170), "label": "Draft"}, {"doc": (350, 170), "tone": "ok", "label": "Role sheet"}, {"magnifier": (240, 120), "anim": "bob"},
         {"stamp": "✓ 6", "at": (350, 60), "tone": "ok"}, {"stamp": "✗ 2", "at": (130, 60), "tone": "bad"}, {"line": [(170, 170), (310, 170)]}],
        n=N(do="Point to the two crosses: the team size and the grade.", expect="People connect the crosses to Hessa's two lines.", silent="Ask: which cross is the more dangerous one?", say="Six lines ticked, two crossed. The crossed ones go.")))
    s.append(player("b4pp", "b4", "d14"))
    s.append(check("b4chk", "b4", "The source trace marks one duty <b>NOT IN SOURCE</b>. What now?",
        [("Delete it, or check it with the owner", 1, "Right. No source, no line."),
         ("Keep it, because it sounds right for the role", 0, "Sounding right is how hallucinations look."),
         ("Ask Copilot if it is sure", 0, "It may say yes again. The role sheet decides.")]))
    s.append(task("b4task", "b4", "t14", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.")))
    # Integration · first Prompt Bank entry
    s.append(listslide("b5bank", "b5", "Integration · your Prompt Bank", "A request you checked <span class=\"hl\">is worth saving.</span>",
        ["<b>Task:</b> what it is for, in one line.", "<b>Request:</b> the five inputs, ready to copy.", "<b>Files:</b> which approved files it needs.", "<b>Check:</b> how you check the result."],
        "Tomorrow you start from entry 1, not from a blank page.", n=N(do="Show entry 1 in the Prompt Bank template on the screen.", expect="People ask whether to save the weak versions: no, only tested ones.", silent="Read your own entry 1 aloud.", time="14:35-14:50")))
    s.append(timer_slide("b5go", "b5", "Integration · 14:35", "Save entry 1, <span class=\"hl\">then read it to a neighbor.</span>",
        f"Fill entry 1 in {CD.F['bank']}. Then read it to the person next to you. Would they get the same draft from it? 15 minutes.", 15,
        n=N(do="Start the timer. After 10 minutes, ask two people to read their entry aloud.", expect="Most entries miss the Check column at first.", silent="Read one entry yourself and ask what is missing.", fallback="Anyone without a draft uses the catch-up file from Task 1.4.")))
    s.append(wrap("w1", "close", "Request, draft, check: <span class=\"hl\">the habit for every HR draft.</span>",
        [(1, "You built", "A redacted note, a checked job description and Prompt Bank entry 1."), (2, "You found", "3 wrong numbers and 2 lines with no source."), (3, "The habit", "Copilot drafts. You check. Authorized HR staff decide.")],
        "Tomorrow: write down one recurring task from your own unit tonight. We use it in Word, Outlook, Teams, Excel and PowerPoint."))
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

TOPICS = {1: {"open": "Opening", "b1": "Block 1 · How Copilot produces an answer", "b2": "Block 2 · Rules before the first request", "b3": "Block 3 · The five inputs", "b4": "Block 4 · Grounding and checking", "b5": "Integration · Prompt Bank", "close": "Close"},
          2: {"open": "Opening", "c0": "Callback quiz", "c1": "Block 1 · Word", "c2": "Block 2 · Outlook", "c3": "Block 3 · Teams", "c4": "Block 4 · Excel", "c5": "Block 5 · PowerPoint", "c6": "Integration · One case", "c7": "Wrap", "close": "Close"},
          3: {"open": "Opening", "e0": "Callback quiz", "e1": "Block 1 · Prompt Gallery", "e2": "Block 2 · Agent Builder", "e3": "Capstone", "e4": "Peer test", "e5": "Share-outs", "e6": "Post-MAP and survey", "close": "Close"}}
DAYFN = {1: day1, 2: day2, 3: day3}
