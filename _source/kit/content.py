# -*- coding: utf-8 -*-
"""Single source of truth for the program shape: days, blocks, outcomes, cards, MAP test, labs, survey words.
AI Fundamentals for HR · CODED Professionals open workshop · approved handoff, 9 Nov 2026."""
import data as D

TITLE = "AI Fundamentals for HR"
SUBTITLE = "Microsoft Copilot for daily HR work: give it the right inputs, check what comes back, and know where its role stops"
CODE = "ai-hr"
BRAND = "CODED · Professionals"
TOOL_MODE = "ai"
CLIENT = None                          # CODED only: an open workshop
DATES = "Tue 17 to Thu 19 November 2026"
DAYDATE = {1: "Tuesday 17 Nov", 2: "Wednesday 18 Nov", 3: "Thursday 19 Nov"}
HOURS = "09:00-15:00"
VENUE = "CODED, Alsharekh room, Frontend Campus"
TOOL = "Copilot"
TOOLS = "Microsoft 365 Copilot: Copilot Chat with file upload, Copilot in Word, Outlook, Teams, Excel and PowerPoint, the Prompt Gallery and Agent Builder"
NDAYS = 3
AUDIENCE = "Junior and middle-level HR employees: Job Evaluation, Salary Scaling, Manpower, Personnel and Administration, Compensation, L&D"
SAMPLE_NOTE = "All sample files are fictional, made for training. Mutla Oil Company is not a real company."
THRU = "Copilot drafts. You check. Authorized HR staff decide."
STORY = "Every exercise uses Mutla Oil Company, a fictional Kuwaiti oil and gas company with five HR units. A lunch and Dhuhr break each day."

SOURCES = {
 "license": ("Copilot Chat with and without a Microsoft 365 Copilot license (Microsoft Support)", "https://support.microsoft.com/en-au/topic/what-s-the-difference-between-using-copilot-chat-with-or-without-a-microsoft-365-copilot-license-5810b659-fbe0-48ee-9fe6-d731fe86cdeb"),
 "agent": ("Build agents in Agent Builder (Microsoft Learn)", "https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents"),
 "knowledge": ("Add knowledge sources in Agent Builder (Microsoft Learn)", "https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge"),
 "gallery": ("Copilot Prompt Gallery (Microsoft Learn)", "https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-prompt-gallery"),
 "teams": ("Get started with Copilot in Microsoft Teams meetings (Microsoft Support)", "https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1"),
 "samsung": D.SAMSUNG["src"],
}

OUTCOMES = ["I can explain how Copilot produces an answer, what it can see, and why I check it.",
            "I can decide which HR tasks Copilot can support, and keep personal, salary and case details out of prompts.",
            "I can write a request with the five inputs: instructions, context, data, tone and approved sources.",
            "I can use Copilot in Word, Outlook, Teams, Excel and PowerPoint for HR documents, messages, meeting records and summaries, and check every figure.",
            "I can build and test a simple HR assistant in Agent Builder.",
            "I can build a reusable prompt set for one recurring task in my unit, and test it with a colleague."]

DAYS = {
1: {"title": "Directing Copilot for Reliable HR Work", "claim": "The request decides the answer. You check it.",
    "sub": "How Copilot writes, what it can see, what never goes in a prompt, and the five inputs that make an HR draft reliable.",
    "brief": "Day 1 starts with one job description and two requests. Then you see how Copilot writes and what it can see. You sort HR tasks before you type, learn the five inputs, and check a draft line by line against its source. You leave with a checked job description and the first entry in your HR Prompt Bank.",
    "artifact": "A checked job description and Prompt Bank entry 1",
    "blocks": [("09:00-09:10", "Welcome and sign-in check", "Open Copilot Chat and read the license label under your name"),
               ("09:10-09:20", "Pre-MAP test", "10 minutes. Scan the QR code. It also checks your laptop"),
               ("09:20-09:30", "Opener: one job description, two requests", "The same role, a weak and a strong request"),
               ("09:30-10:30", "Block 1 · How Copilot produces an answer", "Next-word prediction, what Copilot can see · Task 1.1"),
               ("10:30-10:45", "Break", ""),
               ("10:45-11:35", "Block 2 · Rules before the first request", "What stays with people, green, amber, red · Task 1.2"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:35", "Block 3 · The five inputs of a reliable request", "Instructions, context, data, tone, approved sources · Task 1.3"),
               ("13:35-13:50", "Break", ""),
               ("13:50-14:35", "Block 4 · Grounding and checking", "Ask for the source of every line · Task 1.4"),
               ("14:35-14:50", "Integration: your first Prompt Bank entry", "Save it, then read one aloud"),
               ("14:50-15:00", "Wrap and the hook for Day 2", "What you built, the habit")],
    "outcomes": ["Explain why Copilot can write a <b>confident sentence that is wrong</b>, and what it can see.",
                 "Sort HR tasks before you type, and <b>redact</b> a note before Copilot sees it.",
                 "Write a request with the <b>five inputs</b>.",
                 "Ask for the <b>source of every line</b>, and delete what has none."]},
2: {"title": "Copilot Across HR Documents, Communication and Reporting", "claim": "Five inputs, five apps, one review.",
    "sub": "Policies and job evaluation in Word, a long thread in Outlook, meetings and investigation notes in Teams, HR trackers in Excel, a briefing in PowerPoint.",
    "brief": "Day 2 puts the five inputs to work where HR spends its day. Each block has a short story, a demo, and a task on a Mutla file. You end with one case from your unit track, turned into four outputs and checked with the four-point review.",
    "artifact": "One case, four reviewed outputs",
    "blocks": [("09:00-09:10", "Callback quiz", "Three questions on Day 1"),
               ("09:10-10:00", "Block 1 · Word: policies, versions and job evaluation", "Compare versions, organize evidence, no grade · Task 2.1"),
               ("10:00-10:40", "Block 2 · Outlook: from a long thread to a clear message", "Decisions, owners, tone · Task 2.2"),
               ("10:40-10:55", "Break", ""),
               ("10:55-11:35", "Block 3 · Teams: meetings and investigation notes", "Recap into actions; a timeline, not a verdict · Task 2.3"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:00", "Block 4 · Excel: HR trackers you can check", "Ask, see the rows, check the control total · Task 2.4"),
               ("13:00-13:30", "Block 5 · PowerPoint: a briefing from a document", "Five slides, every number checked · Task 2.5"),
               ("13:30-13:40", "Break", ""),
               ("13:40-14:40", "Integration · One case, four outputs", "Your unit track's case · Task 2.6"),
               ("14:40-15:00", "Wrap and the hook for Day 3", "The Prompt Bank by task")],
    "outcomes": ["Compare policy versions and organize <b>job-evaluation evidence</b> with no grade.",
                 "Turn a long thread into <b>decisions and owners</b>, and change tone without changing facts.",
                 "Recap a meeting into actions, and keep investigation notes to a <b>timeline</b>.",
                 "Check every Excel figure against a <b>control total</b>, and every slide against its brief."]},
3: {"title": "Reusable HR Assistants and Applied Capstone", "claim": "Build it once. Test it. Let a colleague run it.",
    "sub": "Save tested prompts in the Prompt Gallery, build an HR assistant in Agent Builder, then complete a new case and pass a colleague's peer test.",
    "brief": "Day 3 turns skill into something reusable. You save your best requests, build an HR assistant from five approved policy files and test it three ways. Then you complete a new case from your unit track, and a colleague from another unit runs your work with no instructions.",
    "artifact": "A tested prompt set and an HR assistant",
    "blocks": [("09:00-09:10", "Callback quiz", "Three questions on Day 2"),
               ("09:10-09:40", "Block 1 · Reuse before you rebuild: the Prompt Gallery", "Find, adapt, save, share · Task 3.1"),
               ("09:40-10:40", "Block 2 · Build an HR assistant with Agent Builder", "Instructions, knowledge, three tests · Task 3.2"),
               ("10:40-10:55", "Break", ""),
               ("10:55-11:10", "Capstone briefing", "Your new case, core and extension, the self-check"),
               ("11:10-11:35", "Capstone build, part 1", "Plan and first requests · Task 3.3"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:30", "Capstone build, part 2", "Outputs, review, the prompt set · Task 3.3"),
               ("13:30-13:50", "Peer test", "A colleague runs it with no instructions · Task 3.4"),
               ("13:50-14:05", "Break", ""),
               ("14:05-14:20", "One-minute share-outs", "What broke and how you fixed it"),
               ("14:20-14:40", "Post-MAP test, then the final survey", "Two QR codes"),
               ("14:40-15:00", "Close and certificates", "The habit, one last time")],
    "outcomes": ["Find, adapt and save prompts in the <b>Prompt Gallery</b>.",
                 "Build an <b>HR assistant</b> and test it with a normal, an incomplete and a sensitive question.",
                 "Complete a <b>new case</b> by chaining two Copilot apps and reviewing every output.",
                 "Hand your prompt set to a colleague who can run it <b>with no instructions</b>."]},
}

SEGMENTS = {
 1: [("09:30-10:30", "Block 1 · How Copilot produces an answer", [("09:30", 5, "Story: the 30-day answer"), ("09:35", 20, "Next-word prediction, what Copilot can see, Chat and the apps"), ("09:55", 8, "Demo 1.1"), ("10:03", 5, "Quick checks"), ("10:08", 12, "Task 1.1"), ("10:20", 10, "Debrief")]),
     ("10:45-11:35", "Block 2 · Rules before the first request", [("10:45", 5, "Story: the salary memo"), ("10:50", 5, "When it was real"), ("10:55", 9, "Three groups, the safe-use card"), ("11:04", 8, "Demo 1.2 card sort"), ("11:12", 5, "Redact in four moves"), ("11:17", 3, "Demo 1.2b: redact, then ask"), ("11:20", 12, "Task 1.2"), ("11:32", 3, "Debrief")]),
     ("12:15-13:35", "Block 3 · The five inputs", [("12:15", 12, "Felt problem: by hand, then one line"), ("12:27", 18, "The five inputs"), ("12:45", 8, "Demo 1.3"), ("12:53", 4, "Quick check"), ("12:57", 25, "Task 1.3"), ("13:22", 13, "Debrief")]),
     ("13:50-14:35", "Block 4 · Grounding and checking", [("13:50", 4, "Story: the team of six"), ("13:54", 12, "Source trace, three failures"), ("14:06", 7, "Demo 1.4"), ("14:13", 15, "Task 1.4"), ("14:28", 7, "Debrief")])],
 2: [("09:10-10:00", "Block 1 · Word", [("09:10", 4, "Story: what changed by noon"), ("09:14", 8, "Compare versions, evidence with no grade"), ("09:22", 6, "Demo 2.1"), ("09:28", 7, "Quick checks and recruitment"), ("09:35", 5, "Demo 2.1b: compare two versions"), ("09:40", 15, "Task 2.1"), ("09:55", 5, "Debrief")]),
     ("10:00-10:40", "Block 2 · Outlook", [("10:00", 5, "Felt problem: 30 messages"), ("10:05", 10, "Thread summary, tone dial"), ("10:15", 7, "Demo 2.2"), ("10:22", 12, "Task 2.2"), ("10:34", 6, "Debrief")]),
     ("10:55-11:35", "Block 3 · Teams", [("10:55", 4, "Story: the meeting with no actions"), ("10:59", 4, "Before and after a meeting"), ("11:03", 6, "Demo 2.3"), ("11:09", 4, "Quick checks; timeline, not verdict"), ("11:13", 4, "Demo 2.3b: a timeline"), ("11:17", 12, "Task 2.3"), ("11:29", 6, "Debrief")]),
     ("12:15-13:00", "Block 4 · Excel", [("12:15", 4, "Story: 412 or 398"), ("12:19", 12, "Ask, see the rows, spot-check"), ("12:31", 7, "Demo 2.4"), ("12:38", 3, "Quick check"), ("12:41", 15, "Task 2.4"), ("12:56", 4, "Debrief")]),
     ("13:00-13:30", "Block 5 · PowerPoint", [("13:00", 8, "Document to deck"), ("13:08", 7, "Demo 2.5"), ("13:15", 10, "Task 2.5"), ("13:25", 5, "Debrief")]),
     ("13:40-14:40", "Integration · One case, four outputs", [("13:40", 5, "Brief"), ("13:45", 45, "Task 2.6"), ("14:30", 10, "Gallery")])],
 3: [("09:10-09:40", "Block 1 · Prompt Gallery", [("09:10", 3, "Story: five nomination emails"), ("09:13", 8, "Suggested, Your Prompts, Teams"), ("09:21", 5, "Demo 3.1"), ("09:26", 10, "Task 3.1"), ("09:36", 4, "Debrief")]),
     ("09:40-10:40", "Block 2 · Agent Builder", [("09:40", 3, "Story: the same 20 questions"), ("09:43", 12, "Instructions, knowledge, Try it, three tests"), ("09:55", 8, "Demo 3.2"), ("10:03", 30, "Task 3.2"), ("10:33", 7, "Debrief")])],
}

# ------------------------------------------------------------------ next-word widget: a Mutla sentence about leave carry-over
LLM_TREE = {
 "start": {"prompt": "Unused annual leave may be carried over up to", "opts": [["30", 34], ["15", 21], ["10", 14], ["half", 9], ["one", 7], ["the", 6], ["camel", 1]]},
 "30": [["days.", 72], ["working days.", 20], ["days each year.", 6], ["moons.", 1]],
 "15": [["days.", 70], ["working days.", 22], ["days each year.", 6], ["moons.", 1]],
 "10": [["days.", 68], ["working days.", 24], ["days each year.", 6], ["moons.", 1]],
 "half": [["of the balance.", 60], ["a year.", 30], ["the days.", 8], ["a camel.", 1]],
 "one": [["year.", 55], ["month.", 30], ["week.", 13], ["moon.", 1]],
 "the": [["next year.", 58], ["end of March.", 30], ["limit.", 10], ["moon.", 1]],
 "camel": [["load.", 50], ["days.", 30], ["race.", 18], ["moon.", 1]],
}
LLM = {"tree": LLM_TREE, "foot": "Percentages are illustrative. Mutla's policy says 15 days."}

# ------------------------------------------------------------------ the four-point review (Day 2; cheat sheet, hub)
CHECKS = [("Accuracy", "Every date, number, name and rule matches the source."),
          ("Confidentiality", "No civil ID, named salary, medical detail or case detail that names a person."),
          ("Neutrality", "No opinion, blame, promise or decision that belongs to a person."),
          ("Source alignment", "Every point traces back to an approved file. No source, no line.")]

# ------------------------------------------------------------------ safe-use card and sort (Day 1, Block 2)
SAFE = [("green", "Green: go ahead", "Fictional or public data, and your own drafting.", ["Practice on the Mutla files", "Improve the tone of your own announcement", "Explain a COUNTIF formula"]),
        ("amber", "Amber: approved account, minimum data", "Internal HR information, only in your company's approved Copilot account, with names removed.", ["Summarize an approved policy", "Count training requests by unit with employee codes, no names"]),
        ("red", "Red: never in a prompt", "Civil IDs, named salaries, medical details, case details that name people, personal files.", ["A case note with names", "A salary list with names", "A sick-leave certificate"])]
SORT = [("Practice on the Mutla sample files", "green"), ("Paste a case note that names the employee and the witness", "red"),
        ("Make your own announcement warmer and clearer", "green"), ("Summarize the approved leave policy in your company's Copilot", "amber"),
        ("Upload a salary list with names to check a formula", "red"), ("Count training requests by unit, employee codes only, in your company's Copilot", "amber"),
        ("Ask Copilot to explain a COUNTIF formula", "green"), ("Paste a medical certificate to draft a sick-leave letter", "red")]
SORT_LABELS = {"green": "Green · go ahead", "amber": "Amber · approved account, no names", "red": "Red · never in a prompt"}
SAFE_SKILL = "1.2"
GROUPS = [("Do it yourself", "Decisions about people", "Grades, pay, ratings, discipline and selection stay with authorized HR staff."),
          ("Copilot supports", "You lead, it helps", "It finds, compares and checks; you write the result."),
          ("Copilot drafts, you review", "First draft in minutes", "Job descriptions, announcements, summaries, recaps. You check every line.")]
RISKS = [("Wrong facts", "Copilot predicts words. It can be fluent and wrong.", "Check every date, number and rule against the source."),
         ("Data in the wrong place", "A personal account, or a note with names and salaries.", "Sort first: green, amber or red. Redact before you type."),
         ("Decisions handed over", "A draft that sets a grade, blames a person or promises an exception.", "Copilot drafts. Authorized HR staff decide.")]

# ------------------------------------------------------------------ capstone self-check (Day 3 lab, answer key)
SELFCHECK = ["Every request has the five inputs.", "Every request names its approved files.", "No personal, salary or case detail in any prompt.",
             "Every figure and date checked against the case file.", "A person decides: no grade, exception or blame in any output."]

# ------------------------------------------------------------------ cheat sheet and take-home guide
CHEAT = [("Part 1 · Ask well", "The five inputs", "Use all five every time.",
          [(a, b, c, "") for a, b, c in D.INPUTS],
          "Instructions · Context · Data · Tone · Approved sources."),
         ("Part 2 · Six HR requests that work", "Copy, then change the details", "Each one has the five inputs.",
          [("Job description", "Role sheet + template", "Draft a job description from the attached role information, in the template's order. Leave the grade blank.", "Then trace every duty to the role sheet."),
           ("Compare versions", "Two policy files", "List every change between the two versions with its section number: section, old, new.", "Open both files and check each change."),
           ("Warmer, same facts", "Your announcement", "Make it warmer; keep every date, time and rule as written.", "The facts stay. Only the tone changes."),
           ("Meeting recap", "A transcript or notes", "Decisions, then a table of action, owner, deadline, then open questions. Add nothing nobody agreed.", "Check each owner and date."),
           ("Tracker figure", "An Excel file", "Count by unit and show the rows you counted. Then compare with the control total.", "A total that is too high: look for duplicates."),
           ("Investigation notes", "Notes with roles, no names", "Timeline and open questions. No finding, no blame, no recommended action.", "People investigate and decide.")],
          "Copy the shape, not the words. Your unit and your files change the details."),
         ("Part 3 · The four-point review", "Before anything goes out", "Four checks, every output.",
          [(a, b, "", "") for a, b in CHECKS],
          "Copilot drafts. You check. Authorized HR staff decide."),
         ("Part 4 · Where Copilot sits", "Know your tools", "Read the label under your name first.",
          [("Copilot Chat", "Every license", "Upload files, ask, draft. Your work files only when you upload them on a Basic label.", "Copilot Chat (Basic), M365 Copilot (Basic) or M365 Copilot (Premium)."),
           ("Copilot in the apps", "Word, Outlook, Teams, Excel, PowerPoint", "Draft, summarize and analyze inside the app.", "What you get depends on your license."),
           ("Prompt Gallery", "Suggested, Your Prompts, Teams", "Find, save and share tested prompts.", "Share only prompts you tested."),
           ("Agent Builder", "New agent, Configure, Try it", "An assistant with instructions and approved files.", "Test it three ways before anyone uses it.")],
          "The same five inputs work in every one.")]
CHEAT_LEDE = "The five inputs, six HR requests that work, the four-point review, and where Copilot sits. On one page."
GUIDE_INTRO = "Repeat what you built, on your own work, safely. Start with green tasks. Your company's AI and data policy comes first."
GUIDE = [("Your first week", ["Write one five-input request a day on a green task.", "Run the four-point review on each result before it goes anywhere.",
                              "Read the license label under your name, so you know which Copilot you have."]),
         ("Your first month", ["Pick one task your unit does every month.", "Build a prompt set or an HR assistant for it, with approved files only.",
                               "Ask a colleague from another unit to run it with no instructions, then fix what broke.", "Save the tested requests in the Prompt Gallery and share them with your team."])]
GUIDE_HABIT = "Copilot drafts. You check. Authorized HR staff decide. Your company's AI and data policy comes first."
GUIDE_META = [("home", "Your own work, safely"), ("list", "First week, first month"), ("shield", "Policy first")]

# ------------------------------------------------------------------ MAP test: same 14 questions before and after, 6 confidence items (approved handoff)
CONFIDENCE = OUTCOMES
CAPSTONE_PART1 = 25   # Task 3.3 is 100 minutes: 25 before lunch (e3task), 75 after (e4build)
MAP = [
 {"q": f"Copilot tells an employee that a medical certificate is needed only after 5 days of sick leave. Mutla's leave policy says after {D.LEAVE['sick_cert']} days. Why can this happen?",
  "o": ["Copilot copied the number from another employee's chat", "It predicts likely words, and nothing checked the policy", "The question did not say which kind of leave", "The policy file was too long for Copilot to read in full"],
  "a": 1, "day": 1, "topic": "How Copilot writes", "where": "Day 1 · Block 1 · next-word prediction and hallucination"},
 {"q": "Hessa uses Copilot with a Microsoft 365 Copilot license. Which files can it use to answer her?",
  "o": ["Every file on the company SharePoint, including restricted HR folders", "Only the files she uploads in this chat", "Only files, emails and chats she already has permission to open", "Public websites only, never company files"],
  "a": 2, "day": 1, "topic": "What Copilot can see", "where": "Day 1 · Block 1 · what Copilot can see"},
 {"q": "Which task stays with authorized HR staff and is not handed to Copilot?",
  "o": ["Drafting a job description from approved role information", "Summarizing a long leave policy with section numbers", "Deciding the grade of a re-evaluated job", "Changing the tone of a staff announcement"],
  "a": 2, "day": 1, "topic": "What stays with people", "where": "Day 1 · Block 2 · three groups"},
 {"q": "Khaled wants Copilot to summarize a grievance letter that names the employee, her manager and her civil ID. What does he do first?",
  "o": ["Replace the names and remove the civil ID before he uploads it", "Ask Copilot, in the prompt, to keep the whole letter strictly confidential", "Open a new chat so that the letter stays private", "Shorten the letter so that Copilot reads it faster"],
  "a": 0, "day": 1, "topic": "Redact first", "where": "Day 1 · Block 2 · redact, Task 1.2"},
 {"q": "Copilot's job description lists duties that are not in Mutla's role information. Which input was missing?",
  "o": ["A friendlier tone", "Context about who will read the job description", "A longer instruction", "Data: the approved role information"],
  "a": 3, "day": 1, "topic": "The five inputs", "where": "Day 1 · Block 3 · the five inputs"},
 {"q": "Noura must tell unit heads what changed between the 2025 and 2026 training policies. Which request is best?",
  "o": ["\"Is the 2026 policy better than the 2025 one?\"", "\"List each difference and the section it is in.\"", "\"Summarize the 2026 training policy for unit heads.\"", "\"Rewrite the 2026 policy in the words of the 2025 one.\""],
  "a": 1, "day": 2, "topic": "Compare versions", "where": "Day 2 · Block 1 · Task 2.1"},
 {"q": "A colleague asks Copilot to organize evidence for a Safety Officer job against the factors. The output ends with \"This job should move up one grade.\" What should happen?",
  "o": ["Remove the line and send the evidence to the evaluation committee", "Keep the line, because Copilot followed every approved evaluation factor", "Ask Copilot to explain the line, then keep it", "Send the line to the job holder to confirm it"],
  "a": 0, "day": 2, "topic": "Evidence, no grade", "where": "Day 2 · Block 1 · Demo 2.1"},
 {"q": "Hessa asks Copilot to make the Eid holiday notice warmer. The new version no longer says when the office reopens. Which request would have stopped this?",
  "o": ["\"Make it warmer, and keep the original greeting at the top.\"", "\"Make it warmer, and keep it the same length as before.\"", "\"Make it warmer, and change no day or time in it.\"", "\"Make it warmer, and keep the original headings and layout.\""],
  "a": 2, "day": 2, "topic": "Tone, same facts", "where": "Day 2 · Block 2 · tone dial, Task 2.2"},
 {"q": "Khaled's notes on a late delivery to the main stores go into an HR case file. Which line of Copilot's draft can stay?",
  "o": ["\"The stores team is to blame for the three-hour delay.\"", "\"10 November, 14:00: the truck arrived late (gate log).\"", "\"The stores supervisor should be moved to another shift.\"", "\"The driver's account is more believable than the clerk's.\""],
  "a": 1, "day": 2, "topic": "Timeline, not verdict", "where": "Day 2 · Block 3 · Task 2.3"},
 {"q": f"Khaled asks Copilot how many employees joined Mutla in {D.MAP_Q10['quarter']}. Copilot says {D.MAP_Q10['count']}. The HR system's checked total is {D.MAP_Q10['control']}. What does he do first?",
  "o": [f"Use {D.MAP_Q10['count']}, because Copilot read every row of the file", f"Report {(D.MAP_Q10['count'] + D.MAP_Q10['control']) // 2}, the number halfway between the two", "Ask Copilot to round both numbers to the nearest ten", f"Ask for the rows it counted and find the {D.MAP_Q10['count'] - D.MAP_Q10['control']} extra"],
  "a": 3, "day": 2, "topic": "Control totals", "where": "Day 2 · Block 4 · Task 2.4"},
 {"q": "Three Personnel officers each write their own request for the monthly reminder to managers about leave requests waiting for approval. The results differ. What should they do?",
  "o": ["Save one tested request in the Prompt Gallery and share it with the team", "Keep the request in each person's own chat history and copy it from there", "Put the request in the starter prompts of one agent", "Write a new request each time, so that it fits the case"],
  "a": 0, "day": 3, "topic": "Prompt Gallery", "where": "Day 3 · Block 1"},
 {"q": "Employees ask your HR assistant for advice on their own disciplinary cases. In Agent Builder, where do you add the line that stops this and refers them to HR?",
  "o": ["Knowledge", "Instructions", "Starter prompts", "Description"],
  "a": 1, "day": 3, "topic": "Agent instructions", "where": "Day 3 · Block 2 · Demo 3.2"},
 {"q": "A supervisor asks the HR assistant: \"Which person in my team took the most sick days this year?\" What is the right response?",
  "o": ["It answers from the leave policy file", "It estimates from the team's leave balances", "It asks for the team's employee numbers, then answers", "It declines and refers the person to HR"],
  "a": 3, "day": 3, "topic": "Sensitive test", "where": "Day 3 · Block 2 · Task 3.2"},
 {"q": "A colleague runs your prompt set on a new case with no instructions from you, and it fails. What does this tell you?",
  "o": ["Your colleague did not use the prompt set the way you meant", "Copilot cannot be trusted for HR work", "The prompt set depends on something only you know", "The new case was too hard to test fairly"],
  "a": 2, "day": 3, "topic": "Peer test", "where": "Day 3 · Capstone · Task 3.4"},
]
MAP_KEY = " · ".join(f"{i} {'abcd'[q['a']]}" for i, q in enumerate(MAP, 1))

# ------------------------------------------------------------------ the approved slide plan (the validator checks the decks against it)
SLIDES = {1: 61, 2: 64, 3: 40}

# ------------------------------------------------------------------ MAP tests and the final survey (CODED portal)
PORTAL = "https://platform.joincoded.com/sv/"
FORMS = {
    "pre":    {"name": "Pre-MAP test", "when": "Day 1 · Tue 17 Nov · 09:10", "slug": "coded-ai-fundamentals-for-hr-map-test-pre-day-1",
               "url": PORTAL + "coded-ai-fundamentals-for-hr-map-test-pre-day-1", "id": "57d00a52-7a47-47e3-be99-0632b171174e"},
    "post":   {"name": "Post-MAP test", "when": "Day 3 · Thu 19 Nov · 14:20", "slug": "coded-ai-fundamentals-for-hr-map-test-post-day-3",
               "url": PORTAL + "coded-ai-fundamentals-for-hr-map-test-post-day-3", "id": "310d6449-0665-4781-b5bc-f2c10c07b263"},
    "survey": {"name": "Final satisfaction survey", "when": "Day 3 · Thu 19 Nov · 14:30", "slug": "coded-ai-fundamentals-for-hr-final-satisfaction-survey",
               "url": PORTAL + "coded-ai-fundamentals-for-hr-final-satisfaction-survey", "id": "b84d43f1-d405-42f7-8ba0-d4f0c5e2183c"},
}
MAP_MIN = 10

# ------------------------------------------------------------------ the workshop home (hub)
DAYS[1].update({"cat": "Directing Copilot", "icon": "doc", "tag": "five inputs",
                "bullets": ["How Copilot writes, and what it can see", "What stays with people; green, amber, red", "The five inputs, and a source for every line"]})
DAYS[2].update({"cat": "Across the apps", "icon": "mail", "tag": "five Microsoft 365 apps",
                "bullets": ["Policy versions and job-evaluation evidence", "Threads, meetings and investigation notes", "Trackers and briefings you can check"]})
DAYS[3].update({"cat": "Reuse and capstone", "icon": "flask", "tag": "Agent Builder · peer test",
                "bullets": ["Save tested prompts in the Prompt Gallery", "Build and test an HR assistant", "A new case, checked by a colleague"]})
HUB = {
    "headline": ["AI Fundamentals", "for HR"],
    "sub": "A three-day, hands-on Microsoft Copilot workshop for HR employees. Give Copilot the right instructions, context, data, tone and approved sources, check what comes back, and keep decisions about people with people.",
    "meta": "Microsoft Copilot",
    "program_title": "Three days, from one weak request to a prompt set a colleague can run.",
    "program_lead": "One fictional company, Mutla Oil Company, carries all three days: its policies, job descriptions, trackers, threads and cases, in five HR unit tracks. Every file is made up, so you can practice safely. Bring a laptop signed in to Microsoft 365 with Copilot.",
    "habit_eyebrow": "How the days run", "habit_title": "Copilot drafts. You check.",
    "habit_text": "Copilot drafts. You check. Authorized HR staff decide. Run the four-point review before anything goes out:", "habit_list": CHECKS,
    "files_title": "One company. Five HR units. Three days.",
    "takeaway_text": "The cheat sheet: the five inputs, six HR requests that work, the four-point review and where Copilot sits. The safe-use card says what never goes into a prompt. The take-home guide says what to do in your first week and your first month. Every request from each day is on that day's prompt sheet with a COPY button.",
    "map_text": "14 questions. The same on Day 1 and Day 3. Not graded. It measures what this workshop changes. Phone only, no AI. Scan the QR code on the screen, or open the link on your phone. On Day 3, the final survey comes right after.",
    "about": "AI Fundamentals for HR is a CODED Professionals open workshop.",
    "day_tool_note": "Use Microsoft 365 Copilot, signed in with your work account.",
}
SHEET = {"howto": ["<b>Watch the trainer first.</b> Then find the same card here.", "<b>Download the file</b> on the card. In Copilot Chat, start a new chat and attach it (the + or paperclip button).",
                   "Click <b>COPY</b>, paste the request into Copilot, then press <code>Enter</code>.", "<b>Check the answer</b> against the file before you trust it: dates, numbers, names and rules."],
         "note": "<b>Answers vary.</b> Copilot may word things differently from the trainer's screen. That is normal, and it is why we check. Use only the fictional Mutla files here, or green tasks from your own work."}
TASK_FALLBACK_LINE = "Copilot slow, or a daily limit reached? Continue from the backup on the screen."

# ------------------------------------------------------------------ the safe-use card page
CARD = {"lede": "<b>Before you type anything into Copilot, sort the task.</b> Your company's AI and data policy always comes first.",
        "meta": [("shield", "Green, amber, red"), ("check", "Three risks"), ("pin", "Policy first")],
        "cards": SAFE, "risks_title": "Three risks, three habits", "risks_head": ["Risk", "What it looks like", "The habit"], "risks": RISKS,
        "policy_title": "Your company's policy comes first",
        "policy": ["Ask your IT or information-security team which Copilot account your company approves for HR work.", "If your company has no approved Copilot account, amber becomes red.",
                   "Grades, pay, ratings, discipline and selection stay with authorized HR staff, whatever the tool can do.", "When you are not sure, treat the task as red and ask first."]}

# ------------------------------------------------------------------ trainer pages
LESSON_INTRO = "CODED Professionals open workshop. 10 to 25 junior and middle-level HR employees, mixed AI familiarity, no coding. Story: Mutla Oil Company (fictional), five HR unit tracks."
RUNBOOK_PREFLIGHT = ["Sign in to Microsoft 365 Copilot on the presenting laptop with the training account. Test one file upload (the leave policy).",
                     "Read the license label under your name on the Microsoft 365 home page: Copilot Chat (Basic), M365 Copilot (Basic) or M365 Copilot (Premium). Day 2 app demos need an M365 Copilot label (Basic or Premium); Teams recaps need Premium.",
                     "Day 3: open Agent Builder (New agent) once before the day starts. If it is missing, use the fallback in the runbook.",
                     "Open this runbook, the backup results and the answer key on your own screen.",
                     "Copy today's sample files to the presenting laptop and to a USB stick.",
                     "Test the projector with the deck at full screen (F). Step through one prompt-player slide and press R to reset it."]
FACILITATOR = [
 ("open", "Before Day 1", "confirm by Sunday 15 November", [("ul", [
    "The three portal surveys are linked to cohort AIFHR-Nov/Nov-26. The QR codes on the slides open them.",
    "Send the joining note: bring a laptop signed in to Microsoft 365 with Copilot, charged, and know your password.",
    "Ask participants to check the label under their name on the Microsoft 365 home page before Day 1: Copilot Chat (Basic), M365 Copilot (Basic) or M365 Copilot (Premium).",
    "Keep 5 backup laptops with working accounts. Past Copilot rooms had uneven licenses and hit daily limits on Day 2."])]),
 ("room", "Room and laptops", "pre-flight", [("ol", [
    "Tables of four, by unit track where possible, facing the screen. Pairs sit side by side for Tasks 1.1, 2.1, 2.4 and 3.4.",
    "Wi-Fi name and password on the board before 08:45.",
    "Day 1, 09:00: every laptop opens Copilot Chat and is signed in. The pre-MAP QR at 09:10 is also the pre-flight.",
    "Print one safe-use card and one cheat sheet per person."])]),
 ("failplan", "If something fails", "Plan A, B, C", [("table", [["What fails", "Plan B", "Plan C"],
    ["Copilot is slow or busy", "Keep teaching the point with the prompt player slide.", "Show the backup result."],
    ["A daily limit is reached", "Pair with a neighbor.", "Continue from the backup result."],
    ["No Copilot in Word, Excel or PowerPoint", "Use Copilot Chat with the file attached.", "Trainer demo only."],
    ["No Agent Builder", "Save the instructions as a request in Copilot Chat with the five policy files.", "Pair with a neighbor who has it."],
    ["No internet", "Phone hotspot.", "Printed files, the backup results and the decks work offline."]])]),
 ("capstone", "Capstone", "Day 3", [("ul", ["Each participant takes the capstone file for their unit track. It is new to them.", "Core: two Copilot apps, five-input requests, every output reviewed.",
    "Extension: connect to the HR assistant, or a starter prompt.", "Peer test at 13:30: pairs from different units. No scoring; the self-check is on the Day 3 lab page."])]),
]

# ------------------------------------------------------------------ browser labs: one per day; answers only in the staff lab key
LABS = {
 1: {"title": "Check a Copilot answer, step by step", "intro": "Work through the steps at your own pace after Task 1.1. Your done marks stay in this browser.",
     "steps": [
        {"title": "Open the files", "do": ["Download mutla-leave-policy-2026.docx and mutla-copilot-leave-answer.docx.", "Open both side by side."],
         "hint": "The policy is the source. The answer is what Copilot wrote.", "check": {"kind": "note", "label": "Which file is the source?"},
         "answer": [("p", "The leave policy is the source. Every number in the answer must match it.")]},
        {"title": "Check the carry-over", "do": ["Find what the answer says about carrying over leave.", "Find the same rule in the policy."],
         "hint": "Look at section 4.", "check": {"kind": "flag", "label": "Type the number of days the policy allows (digits only)", "answer": str(D.LEAVE["carry"])},
         "answer": [("p", f"The answer says 30 days. Section 4 says {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']}.")]},
        {"title": "Check the emergency leave", "do": ["Compare the emergency leave days in the answer and in the policy."],
         "hint": "Look at section 5.", "check": {"kind": "note", "label": "Write the correct rule and its section"},
         "answer": [("p", f"The answer says 5 days. Section 5 says {D.LEAVE['emergency']} days a year.")]},
        {"title": "Check the notice period", "do": ["Compare how early staff must request annual leave."],
         "hint": "Look at section 3.", "check": {"kind": "flag", "label": "Type the number of days of notice (digits only)", "answer": str(D.LEAVE["notice"])},
         "answer": [("p", f"The answer says 7 days. Section 3 says {D.LEAVE['notice']} days.")]},
     ]},
 2: {"title": "Spot-check the HR tracker", "intro": "Use mutla-hr-trackers-q3-2026.xlsx. Check two figures yourself before you trust them.",
     "steps": [
        {"title": "Open the tracker", "do": ["Download mutla-hr-trackers-q3-2026.xlsx and open it in Excel.", "Find the Training, Manpower and Control totals sheets."],
         "hint": "The Control totals sheet holds the checked numbers.", "check": {"kind": "note", "label": "How many rows does the Training sheet have?"},
         "answer": [("p", f"The Training sheet has {D.TRAIN_ROWS_EXPORT} request rows. The Control totals sheet says {D.TRAIN_TRUE} requests.")]},
        {"title": "Find why Training is too high", "do": ["Select the Request ID column. Use Conditional Formatting, Duplicate Values, or Remove Duplicates on a copy."],
         "hint": "Each request ID should appear once.", "check": {"kind": "flag", "label": "Type how many extra rows Remove Duplicates takes out (digits only)", "answer": str(D.TRAIN_DUPES)},
         "answer": [("p", f"{D.TRAIN_DUPES} request IDs appear twice. Without them, the count is {D.TRAIN_TRUE}.")]},
        {"title": "Find why vacancies are too low", "do": ["In the Manpower sheet, compare each section's approved positions with the approved structure on the Control totals sheet."],
         "hint": "One new section shows 0 approved positions.", "check": {"kind": "flag", "label": "Type the name of that section", "answer": D.MP_WRONG},
         "answer": [("p", f"{D.MP_WRONG} shows 0 approved positions; it should be {D.STAFF_POSITIONS}. Total vacancies are {D.MP_VACANT}, not {D.MP_VACANT_EXPORT}.")]},
     ]},
 3: {"title": "Capstone self-check", "intro": "Use this list before the peer test at 13:30. Mark each step when it is true for your work.",
     "steps": [{"title": t, "do": [t], "hint": h, "check": {"kind": "note", "label": "Where in your work does this show?"}, "answer": [("p", a)]}
               for t, h, a in [(SELFCHECK[0], "Instructions, context, data, tone, approved sources.", "Each request in the prompt set has all five inputs."),
                               (SELFCHECK[1], "A colleague cannot guess which file you meant.", "Each request names the files it needs."),
                               (SELFCHECK[2], "Use employee codes or roles, never names.", "No civil ID, named salary, medical or case detail anywhere."),
                               (SELFCHECK[3], "Open the case file and compare.", "Every figure and date matches the case file."),
                               (SELFCHECK[4], "Look for any grade, exception or blame.", "No output makes a decision that belongs to a person.")]]},
}

# ------------------------------------------------------------------ portal survey words (Arabic; surveys.py builds the payloads)
SURVEY = {
 "program": "the CODED Professionals open workshop", "program_ar": "أساسيات الذكاء الاصطناعي للموارد البشرية",
 "client": "", "cohort": "AIFHR-Nov/Nov-26", "subtitle": {"en": "CODED Professionals", "ar": "CODED للمحترفين"},
 "folder": "a8f8146d-144f-47ed-9121-ef8e437f2f11", "name_prefix": "CODED ·", "note": "", "test_min": 10,
 "dept_label": ("Your company", "اسم الشركة"),
 "confidence_ar": ["أستطيع أن أشرح كيف يُنتج Copilot إجابته، وما الذي يمكنه رؤيته، ولماذا أتحقق منها.",
                   "أستطيع أن أحدد مهام الموارد البشرية التي يمكن أن يدعمها Copilot، وأبقي التفاصيل الشخصية وتفاصيل الرواتب والحالات خارج الطلبات.",
                   "أستطيع كتابة طلب يتضمن المدخلات الخمسة: التعليمات والسياق والبيانات والأسلوب والمصادر المعتمدة.",
                   "أستطيع استخدام Copilot في Word وOutlook وTeams وExcel وPowerPoint لمستندات الموارد البشرية والرسائل ومحاضر الاجتماعات والملخصات، وأتحقق من كل رقم.",
                   "أستطيع بناء مساعد بسيط للموارد البشرية في Agent Builder واختباره.",
                   "أستطيع بناء مجموعة طلبات قابلة لإعادة الاستخدام لمهمة متكررة في وحدتي، واختبارها مع زميل."],
 "map_ar": [
  ("أخبر Copilot موظفاً أن الشهادة الطبية لا تُطلب إلا بعد 5 أيام من الإجازة المرضية. سياسة الإجازات في Mutla تنص على أنها تُطلب بعد يومين. لماذا يمكن أن يحدث هذا؟",
   ["نسخ Copilot الرقم من محادثة موظف آخر", "يتوقع الكلمات المرجحة، ولم يتحقق شيء من السياسة", "لم يحدد السؤال نوع الإجازة", "كان ملف السياسة أطول من أن يقرأه Copilot كاملاً"]),
  ("تستخدم حصة Copilot مع ترخيص Microsoft 365 Copilot. ما الملفات التي يمكنه استخدامها للإجابة عليها؟",
   ["كل ملف على SharePoint في الشركة، بما فيها مجلدات الموارد البشرية المقيدة", "الملفات التي ترفعها في هذه المحادثة فقط", "الملفات والرسائل والمحادثات التي لديها صلاحية فتحها فقط", "المواقع العامة فقط، وليس ملفات الشركة أبداً"]),
  ("أي مهمة تبقى لدى موظفي الموارد البشرية المخوّلين ولا تُسند إلى Copilot؟",
   ["صياغة وصف وظيفي من معلومات الدور المعتمدة", "تلخيص سياسة إجازات طويلة مع أرقام البنود", "تحديد درجة وظيفة أعيد تقييمها", "تغيير أسلوب إعلان موجّه للموظفين"]),
  ("يريد خالد أن يلخّص Copilot رسالة تظلّم تذكر اسم الموظفة واسم مديرها ورقم بطاقتها المدنية. ما الذي يفعله أولاً؟",
   ["يستبدل الأسماء ويحذف رقم البطاقة المدنية قبل رفعها", "يطلب من Copilot في الطلب نفسه أن يُبقي الرسالة كلها سرية تماماً", "يفتح محادثة جديدة حتى تبقى الرسالة خاصة", "يختصر الرسالة حتى يقرأها Copilot أسرع"]),
  ("يتضمن الوصف الوظيفي الذي كتبه Copilot مهاماً غير موجودة في معلومات الدور لدى Mutla. أي مُدخل كان ناقصاً؟",
   ["أسلوب أكثر وداً", "سياق عن الأشخاص الذين سيقرؤون الوصف الوظيفي", "تعليمات أطول", "البيانات: معلومات الدور المعتمدة"]),
  ("على نورة أن تخبر رؤساء الوحدات بما تغيّر بين سياستي التدريب لعامي 2025 و2026. أي طلب هو الأفضل؟",
   ["\"هل سياسة 2026 أفضل من سياسة 2025؟\"", "\"اذكر كل فرق والبند الذي ورد فيه.\"", "\"لخّص سياسة التدريب لعام 2026 لرؤساء الوحدات.\"", "\"أعد كتابة سياسة 2026 بكلمات سياسة 2025.\""]),
  ("يطلب زميل من Copilot ترتيب أدلة وظيفة مسؤول سلامة حسب العوامل. ينتهي الناتج بعبارة \"يجب رفع هذه الوظيفة درجة واحدة.\" ما الذي يجب أن يحدث؟",
   ["حذف العبارة وإرسال الأدلة إلى لجنة التقييم", "إبقاء العبارة لأن Copilot اتبع كل عوامل التقييم المعتمدة", "طلب شرح العبارة من Copilot ثم إبقاؤها", "إرسال العبارة إلى شاغل الوظيفة ليؤكدها"]),
  ("تطلب حصة من Copilot أن يجعل إعلان عطلة العيد أكثر دفئاً. لم تعد النسخة الجديدة تذكر موعد عودة المكتب إلى العمل. أي طلب كان سيمنع ذلك؟",
   ["\"اجعله أكثر دفئاً، واحتفظ بالتحية الأصلية في أعلاه.\"", "\"اجعله أكثر دفئاً، واحتفظ بطوله كما كان.\"", "\"اجعله أكثر دفئاً، ولا تغيّر أي يوم أو وقت فيه.\"", "\"اجعله أكثر دفئاً، واحتفظ بالعناوين والتنسيق الأصليين.\""]),
  ("تدخل ملاحظات خالد عن تأخر شحنة إلى المخازن الرئيسية في ملف حالة لدى الموارد البشرية. أي سطر من مسودة Copilot يمكن أن يبقى؟",
   ["\"فريق المخازن هو المسؤول عن التأخير لمدة ثلاث ساعات.\"", "\"10 نوفمبر، 14:00: وصلت الشاحنة متأخرة (سجل البوابة).\"", "\"يجب نقل مشرف المخازن إلى نوبة عمل أخرى.\"", "\"رواية السائق أكثر مصداقية من رواية الموظف في المخزن.\""]),
  (f"يسأل خالد Copilot عن عدد الموظفين الذين انضموا إلى Mutla في الربع الثالث. يقول Copilot إن العدد {D.MAP_Q10['count']}. الإجمالي المدقق في نظام الموارد البشرية هو {D.MAP_Q10['control']}. ماذا يفعل أولاً؟",
   [f"يستخدم {D.MAP_Q10['count']} لأن Copilot قرأ كل صف في الملف", f"يذكر {(D.MAP_Q10['count'] + D.MAP_Q10['control']) // 2}، الرقم الذي يقع في منتصف المسافة بين الرقمين", "يطلب من Copilot تقريب الرقمين إلى أقرب عشرة", f"يطلب الصفوف التي عدّها ويبحث عن الـ {D.MAP_Q10['count'] - D.MAP_Q10['control']} الزائدة"]),
  ("يكتب ثلاثة موظفين في وحدة شؤون الموظفين كلٌّ منهم طلبه الخاص للتذكير الشهري للمديرين بطلبات الإجازة التي تنتظر الموافقة. وتختلف النتائج. ماذا يفعلون؟",
   ["يحفظون طلباً مختبراً في Prompt Gallery ويشاركونه", "يحتفظ كل شخص بالطلب في سجل محادثاته وينسخه من هناك", "يضعون الطلب في طلبات البداية لوكيل واحد", "يكتبون طلباً جديداً في كل مرة ليناسب الحالة"]),
  ("يسأل الموظفون مساعد الموارد البشرية عن نصيحة في قضاياهم التأديبية. أين تضيف في Agent Builder السطر الذي يمنع ذلك ويحيلهم إلى الموارد البشرية؟",
   ["المعرفة (Knowledge)", "التعليمات (Instructions)", "طلبات البداية (Starter prompts)", "الوصف (Description)"]),
  ("يسأل مشرف مساعد الموارد البشرية: \"من الشخص في فريقي الذي أخذ أكثر أيام إجازة مرضية هذا العام؟\" ما الاستجابة الصحيحة؟",
   ["يجيب من ملف سياسة الإجازات", "يقدّر الإجابة من أرصدة إجازات الفريق", "يطلب الأرقام الوظيفية للفريق ثم يجيب", "يرفض ويحيل السائل إلى الموارد البشرية"]),
  ("شغّل زميلك مجموعة طلباتك على حالة جديدة دون أي تعليمات منك، وفشلت. ماذا يخبرك هذا؟",
   ["لم يستخدم زميلك مجموعة الطلبات بالطريقة التي قصدتها", "لا يمكن الوثوق بـ Copilot في عمل الموارد البشرية", "مجموعة الطلبات تعتمد على شيء تعرفه أنت فقط", "كانت الحالة الجديدة أصعب من أن تكون اختباراً عادلاً"]),
 ],
 "day_ar": {1: "توجيه Copilot لعمل موثوق في الموارد البشرية", 2: "Copilot في مستندات الموارد البشرية والتواصل والتقارير", 3: "مساعدات الموارد البشرية القابلة لإعادة الاستخدام والمشروع الختامي"},
 "relevance": ("The content was high quality and relevant to my HR work.", "كان المحتوى عالي الجودة وذا صلة بعملي في الموارد البشرية."),
 "hands_on": ("The hands-on parts, such as the job descriptions, policy comparisons, the HR tracker, the HR assistant and the capstone, helped me apply what I learned.",
              "ساعدتني الأجزاء التطبيقية، مثل الأوصاف الوظيفية ومقارنة السياسات وجدول الموارد البشرية ومساعد الموارد البشرية والمشروع الختامي، على تطبيق ما تعلّمته."),
 "materials": ("The workshop website, the cheat sheet, the safe-use card and the take-home guide were clear and useful.",
               "كانت مواد ورشة العمل (الموقع وورقة المراجعة السريعة وبطاقة الاستخدام الآمن ودليل ما بعد ورشة العمل) واضحةً ومفيدة."),
 "logistics": ("The venue, the daily timing and access to Microsoft Copilot worked well for me.", "كان المكان والتوقيت اليومي وإمكانية الوصول إلى Microsoft Copilot مناسباً لي."),
}
