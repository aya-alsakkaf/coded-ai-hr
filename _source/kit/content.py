# -*- coding: utf-8 -*-
"""Single source of truth for the program shape: days, blocks, outcomes, cards, MAP test, labs, survey words.
AI Fundamentals for HR · CODED Professionals open workshop · approved handoff, 9 Nov 2026."""
import data as D

TITLE = "AI Fundamentals for HR"
SUBTITLE = "Microsoft Copilot for daily HR work: clear requests, checked drafts, safe data, mapped workflows and a first HR agent"
CODE = "ai-hr"
BRAND = "CODED · Professionals"
TOOL_MODE = "ai"
CLIENT = None                          # CODED only: an open workshop
DATES = "Tue 17 to Thu 19 November 2026"
DAYDATE = {1: "Tuesday 17 Nov", 2: "Wednesday 18 Nov", 3: "Thursday 19 Nov"}
HOURS = "09:00-15:00"
VENUE = "CODED, Alsharekh room, Frontend Campus"
TOOL = "Copilot"
TOOLS = "Microsoft 365 Copilot: Copilot Chat with file upload, Copilot in Word, Outlook, Excel and PowerPoint, and Agent Builder. Microsoft Forms and Power Automate in a trainer demo"
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
            "I can write a request with role, context, task, data, constraints, tone and output format, and fix a weak draft with follow-up instructions.",
            "I can use Copilot in Word and Outlook to draft HR documents and messages, and change the tone for each reader.",
            "I can keep personal, salary and case details out of prompts.",
            "I can use Copilot for meeting notes, follow-ups, Excel figures and PowerPoint summaries, and check every figure.",
            "I can map an HR process, build and test a simple HR agent, and tell when a Power Automate flow is needed."]

DAYS = {
1: {"title": "Copilot Foundations for HR Documents and Communication", "claim": "Ask clearly. Check everything. People decide.",
    "sub": "How Copilot writes and what it can see, the prompt checklist, follow-up instructions, and HR documents and messages in Word and Outlook.",
    "brief": "Day 1 starts with one job description and two requests. You see how Copilot writes, what it can see, and which HR decisions it must never make. You learn the prompt checklist, fix weak drafts with follow-up instructions, and check every line against its source. Then you write a job description and an experience letter in Word, a policy summary for staff, and one announcement in Outlook for three different readers.",
    "artifact": "A checked job description, an experience letter, a policy summary, an announcement for three readers, and two Prompt Bank entries",
    "blocks": [("09:00-09:10", "Welcome and sign-in check", "CODED, your trainer, and the label under your name"),
               ("09:10-09:20", "Pre-MAP test", "10 minutes. Scan the QR code on the screen"),
               ("09:20-09:30", "Opener: one job description, two requests", "The same role, a one-line request and a full one, live"),
               ("09:30-10:30", "Block 1 · How generative AI and Copilot work", "Next-word prediction, what Copilot can see, what stays with people · Task 1.1"),
               ("10:30-10:45", "Break", ""),
               ("10:45-11:35", "Block 2 · Writing a clear prompt", "The prompt checklist: seven parts · Task 1.2"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:20", "Block 3 · Draft, fix and check in Word", "Follow-up instructions and the source of every line · Tasks 1.3 and 1.4"),
               ("13:20-13:35", "Break", ""),
               ("13:35-14:40", "Block 4 · From policy to people: Word, then Outlook", "A policy summary, then one message for three readers · Tasks 1.5 and 1.6"),
               ("14:40-15:00", "Prompt Bank and wrap", "Save two requests, and where Copilot sits")],
    "outcomes": ["Explain why Copilot can write a <b>confident sentence that is wrong</b>, what it can see, and which HR decisions stay with people.",
                 "Write a request with the <b>prompt checklist</b>: role, context, task, data, constraints, tone and output format.",
                 "Improve a weak draft with <b>follow-up instructions</b>, and ask for the source of every line.",
                 "Draft HR documents in Word and messages in Outlook, and <b>change the tone</b> for each reader without changing the facts."]},
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
 1: [("09:30-10:30", "Block 1 · How generative AI and Copilot work", [("09:30", 3, "Story: the 30-day answer"), ("09:33", 12, "Next-word prediction and hallucination"), ("09:45", 8, "What Copilot can see; your label"), ("09:53", 5, "Demo 1.1"), ("09:58", 12, "Task 1.1"), ("10:10", 4, "Debrief"), ("10:14", 8, "What stays with people; Demo 1.1b card sort"), ("10:22", 4, "Quick check"), ("10:26", 4, "Practice files only today")]),
     ("10:45-11:35", "Block 2 · Writing a clear prompt", [("10:45", 3, "Story: the one-line reminder"), ("10:48", 4, "Brief a new colleague"), ("10:52", 12, "The prompt checklist"), ("11:04", 4, "Constraints"), ("11:08", 6, "Demo 1.2"), ("11:14", 2, "Quick check"), ("11:16", 14, "Task 1.2"), ("11:30", 5, "Debrief")]),
     ("12:15-13:20", "Block 3 · Draft, fix and check in Word", [("12:15", 3, "Story: the team of six"), ("12:18", 5, "Follow-up instructions"), ("12:23", 5, "Demo 1.3"), ("12:28", 5, "Source trace, three failures"), ("12:33", 4, "Demo 1.3b"), ("12:37", 22, "Task 1.3"), ("12:59", 15, "Task 1.4"), ("13:14", 6, "Debrief")]),
     ("13:35-14:40", "Block 4 · From policy to people", [("13:35", 3, "Story: version 4 arrives"), ("13:38", 5, "Summaries you can check"), ("13:43", 5, "Demo 1.5"), ("13:48", 15, "Task 1.5"), ("14:03", 4, "The tone dial"), ("14:07", 5, "Demo 1.6"), ("14:12", 17, "Task 1.6"), ("14:29", 2, "Quick check"), ("14:31", 9, "Debrief")])],
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
CHEAT = [("Part 1 · Ask well", "The prompt checklist", "Seven parts. Use all seven for anything that matters.",
          [(a, b, c, "") for a, b, c in D.CHECKLIST],
          D.PARTS_LINE + "."),
         ("Part 2 · Six HR requests that work", "Copy, then change the details", "Each one has the parts that matter most for it.",
          [("Job description", "Role sheet + template", "Draft the job description from the attached role information, in the template's order. Use only the attached files. Leave the grade blank.", "Then trace every duty to the role sheet."),
           ("Fix with a follow-up", "The same chat", "The draft is missing one duty from the role sheet. Add it, word for word. Change nothing else.", "Name the problem, and say what to keep."),
           ("Warmer, same facts", "Your announcement", "Rewrite it for line managers. Keep every date, time and rule as written.", "The facts stay. Only the tone changes."),
           ("Summary with sections", "One policy", "Summarize the attached policy for staff. Give the section number for every point. Keep every number as written.", "Then check two numbers yourself."),
           ("Flag, do not fix", "A request and its record", "List every point where the request differs from the record or breaks the template rules. Do not change anything.", "Copilot lists. A person decides."),
           ("Tracker figure", "An Excel file", "Count by unit and show the rows you counted. Then compare with the control total.", "A total that is too high: look for duplicates.")],
          "Copy the shape, not the words. Your unit and your files change the details."),
         ("Part 3 · The four-point review", "Before anything goes out", "Four checks, every output.",
          [(a, b, "", "") for a, b in CHECKS],
          "Copilot drafts. You check. Authorized HR staff decide."),
         ("Part 4 · Where Copilot sits", "Know your tools", "Read the label under your name first.",
          [("Copilot Chat", "Every license", "Upload files, ask, draft. Your work files only when you upload them on a Basic label.", "Copilot Chat (Basic), M365 Copilot (Basic) or M365 Copilot (Premium)."),
           ("Copilot in the apps", "Word, Outlook, Excel, PowerPoint", "Draft, summarize and analyze inside the app.", "What you get depends on your license."),
           ("Agent Builder", "Create agent, Configure, Test", "An agent with your instructions and approved files that answers the same questions for many people.", "It answers. It does not send, route or approve."),
           ("Power Automate", "A flow, not a chat", "Runs on its own when something happens: a form is sent, a date arrives. Routes approvals, sends emails, logs rows.", "Ask your IT team before you build one.")],
          "The same checklist works in every Copilot tool.")]
CHEAT_LEDE = "The prompt checklist, six HR requests that work, the four-point review, and where Copilot sits. On one page."
GUIDE_INTRO = "Repeat what you built, on your own work, safely. Start with green tasks. Your company's AI and data policy comes first."
GUIDE = [("Your first week", ["Write one checklist request a day on a green task.", "Fix the first draft with a follow-up instead of starting again.",
                              "Run the four-point review on each result before it goes anywhere.", "Read the license label under your name, so you know which Copilot you have."]),
         ("Your first month", ["Map one process your unit runs every month. Mark each step: a person, Copilot, an agent or a flow.",
                               "Build an agent for the questions your unit answers most, with approved files only. Test it three ways.",
                               "Ask a colleague from another unit to try it with no instructions, then fix what broke.",
                               "For steps that need a flow, ask your IT team whether Power Automate is allowed."])]
GUIDE_HABIT = "Copilot drafts. You check. Authorized HR staff decide. Your company's AI and data policy comes first."
GUIDE_META = [("home", "Your own work, safely"), ("list", "First week, first month"), ("shield", "Policy first")]

# ------------------------------------------------------------------ MAP test: same 14 questions before and after, 6 confidence items
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
  "a": 2, "day": 1, "topic": "What stays with people", "where": "Day 1 · Block 1 · Demo 1.1b"},
 {"q": "Copilot's job description lists duties that are not in Mutla's role information. Which part of the request was missing?",
  "o": ["Tone: a friendlier voice", "Context: who will read the job description", "Output format: the template's headings", "Data: the approved role information, attached"],
  "a": 3, "day": 1, "topic": "The prompt checklist", "where": "Day 1 · Block 2 · the prompt checklist"},
 {"q": "Hessa's first draft from Copilot is good, but it is two pages, and the template allows one. What does she do next?",
  "o": ["Reply in the same chat: make it one page, and keep all six duties", "Send the same request again in a new chat, so that Copilot starts fresh", "Delete the second page herself, whatever is on it", "Ask Copilot to write the job description again, but shorter"],
  "a": 0, "day": 1, "topic": "Follow-up instructions", "where": "Day 1 · Block 3 · Demo 1.3"},
 {"q": "Hessa asks Copilot to make the Eid holiday notice warmer. The new version no longer says when the office reopens. Which request would have stopped this?",
  "o": ["\"Make it warmer, and keep the original greeting at the top.\"", "\"Make it warmer, and keep it the same length as before.\"", "\"Make it warmer, and change no day or time in it.\"", "\"Make it warmer, and keep the original headings and layout.\""],
  "a": 2, "day": 1, "topic": "Tone, same facts", "where": "Day 1 · Block 4 · tone dial, Task 1.6"},
 {"q": "Khaled wants Copilot to summarize a grievance letter that names the employee, her manager and her civil ID. What does he do first?",
  "o": ["Replace the names and remove the civil ID before he uploads it", "Ask Copilot, in the prompt, to keep the whole letter strictly confidential", "Open a new chat so that the letter stays private", "Shorten the letter so that Copilot reads it faster"],
  "a": 0, "day": 2, "topic": "Redact first", "where": "Day 2 · Block 1 · redact"},
 {"q": "Abdulaziz wants Copilot to find a mistake in a salary list that shows each employee's name. Which color is this task on the safe-use card?",
  "o": ["Green: go ahead, because the list never leaves HR", "Red: never in a prompt, in any account", "Amber: fine in the company's approved Copilot account", "Amber: fine if he deletes the chat afterwards"],
  "a": 1, "day": 2, "topic": "Green, amber, red", "where": "Day 2 · Block 1 · the safe-use card"},
 {"q": "After a meeting about Ramadan working hours, which line of the recap is ready to send?",
  "o": ["Action: the Ramadan hours proposal, as soon as possible", "Action: someone in HR sends the Ramadan hours proposal", "Action: discuss the Ramadan hours again next month", "Action: send the Ramadan hours proposal · Owner: Fatma · By Sunday 7 February"],
  "a": 3, "day": 2, "topic": "Meeting recap", "where": "Day 2 · Block 2 · meeting actions"},
 {"q": f"Khaled asks Copilot how many employees joined Mutla in {D.MAP_Q10['quarter']}. Copilot says {D.MAP_Q10['count']}. The HR system's checked total is {D.MAP_Q10['control']}. What does he do first?",
  "o": [f"Use {D.MAP_Q10['count']}, because Copilot read every row of the file", f"Report {(D.MAP_Q10['count'] + D.MAP_Q10['control']) // 2}, the number halfway between the two", "Ask Copilot to round both numbers to the nearest ten", f"Ask for the rows it counted and find the {D.MAP_Q10['count'] - D.MAP_Q10['control']} extra"],
  "a": 3, "day": 2, "topic": "Control totals", "where": "Day 2 · Excel · control totals"},
 {"q": "Training requests arrive by email. The coordinator prints each one for the manager to sign, then types it into the tracker. What does the process map show?",
  "o": ["Unclear ownership: nobody knows who approves", "Duplicated effort: the same request is handled three times", "A decision about people that Copilot should make", "A delay that only a new HR system can fix"],
  "a": 1, "day": 2, "topic": "Process problems", "where": "Day 2 · mapping an HR process"},
 {"q": "Employees ask your HR agent for advice on their own disciplinary cases. In Agent Builder, where do you add the line that stops this and refers them to HR?",
  "o": ["Knowledge", "Instructions", "Starter prompts", "Description"],
  "a": 1, "day": 3, "topic": "Agent instructions", "where": "Day 3 · Agent Builder"},
 {"q": "A supervisor asks the HR agent: \"Which person in my team took the most sick days this year?\" What is the right response?",
  "o": ["It answers from the leave policy file", "It estimates from the team's leave balances", "It asks for the team's employee numbers, then answers", "It declines and refers the person to HR"],
  "a": 3, "day": 3, "topic": "Sensitive test", "where": "Day 3 · testing the agent"},
 {"q": "Every training request must go to the line manager to approve, then into the tracker, and the employee must get an email with the result. Which tool fits?",
  "o": ["A Copilot Chat request that HR sends for each training request", "An agent in Agent Builder that answers questions about training", "A Power Automate flow with an approval step", "A saved request in the HR Prompt Bank"],
  "a": 2, "day": 3, "topic": "Copilot, agent or flow", "where": "Day 3 · the Power Automate demo"},
]
MAP_KEY = " · ".join(f"{i} {'abcd'[q['a']]}" for i, q in enumerate(MAP, 1))

# ------------------------------------------------------------------ the approved slide plan (the validator checks the decks against it)
SLIDES = {1: 64, 2: 64, 3: 40}

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
DAYS[1].update({"cat": "Copilot foundations", "icon": "doc", "tag": "prompt checklist · Word · Outlook",
                "bullets": ["How Copilot writes, and what it can see", "The prompt checklist and follow-up instructions", "Job descriptions, letters, summaries, announcements"]})
DAYS[2].update({"cat": "Across the apps", "icon": "mail", "tag": "five Microsoft 365 apps",
                "bullets": ["Policy versions and job-evaluation evidence", "Threads, meetings and investigation notes", "Trackers and briefings you can check"]})
DAYS[3].update({"cat": "Reuse and capstone", "icon": "flask", "tag": "Agent Builder · peer test",
                "bullets": ["Save tested prompts in the Prompt Gallery", "Build and test an HR assistant", "A new case, checked by a colleague"]})
HUB = {
    "headline": ["AI Fundamentals", "for HR"],
    "sub": "A three-day, hands-on Microsoft Copilot workshop for HR employees. Write clear requests, check what comes back, keep people's data safe, map your HR work and build a first HR agent. Decisions about people stay with people.",
    "meta": "Microsoft Copilot",
    "program_title": "Three days, from one weak request to an HR agent and a better workflow.",
    "program_lead": "One fictional company, Mutla Oil Company, carries all three days: its policies, job descriptions, trackers, threads and cases, in five HR unit tracks. Every file is made up, so you can practice safely. Bring a laptop signed in to Microsoft 365 with Copilot.",
    "habit_eyebrow": "How the days run", "habit_title": "Copilot drafts. You check.",
    "habit_text": "Copilot drafts. You check. Authorized HR staff decide. Run the four-point review before anything goes out:", "habit_list": CHECKS,
    "files_title": "One company. Five HR units. Three days.",
    "takeaway_text": "The cheat sheet: the prompt checklist, six HR requests that work, the four-point review and where Copilot sits. The safe-use card says what never goes into a prompt. The take-home guide says what to do in your first week and your first month. Every request from each day is on that day's prompt sheet with a COPY button.",
    "map_text": "14 questions. The same on Day 1 and Day 3. Not graded. It measures what this workshop changes. Phone only, no AI. Scan the QR code on the screen, or open the link on your phone. On Day 3, the final survey comes right after.",
    "about": "AI Fundamentals for HR is a CODED Professionals open workshop.",
    "day_tool_note": "Use Microsoft 365 Copilot, signed in with your work account.",
}
SHEET = {"howto": ["<b>Watch the trainer first.</b> Then find the same card here.", "<b>Download the file</b> on the card. In Copilot Chat, start a new chat and attach it (the + or paperclip button).",
                   "Click <b>COPY</b>, paste the request into Copilot, then press <code>Enter</code>.", "<b>Check the answer</b> against the file before you trust it: dates, numbers, names and rules."],
         "note": "<b>Answers vary.</b> Copilot may word things differently from the trainer's screen. That is normal, and it is why we check. Requests you write yourself are not on this sheet: write them with the checklist, and use the hints on the day's lab page if you are stuck. Use only the fictional Mutla files here, or green tasks from your own work."}
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
RUNBOOK_PREFLIGHT = ["Sign in to Microsoft 365 Copilot on the presenting laptop with the training account. Test one file upload (the leave policy). Every demo runs live.",
                     "Read the license label under your name on the Microsoft 365 home page: Copilot Chat (Basic), M365 Copilot (Basic) or M365 Copilot (Premium). Day 2 app demos need an M365 Copilot label (Basic or Premium); Teams recaps need Premium.",
                     "Day 3: open Agent Builder (New agent) once before the day starts. If it is missing, use the fallback in the runbook.",
                     "Open this runbook, the backup results and the answer key on your own screen.",
                     "Copy today's sample files to the presenting laptop and to a USB stick.",
                     "Test the projector with the deck at full screen (F). Open the backup results for today on your own screen, in case Copilot is slow."]
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
    "Everything is digital: the safe-use card and the cheat sheet are on the workshop site. Nothing is printed."])]),
 ("failplan", "If something fails", "Plan A, B, C", [("table", [["What fails", "Plan B", "Plan C"],
    ["Copilot is slow or busy", "Wait one minute, then send the request again.", "Show the backup result on your own screen."],
    ["A daily limit is reached", "Pair with a neighbor.", "Continue from the backup result."],
    ["No Copilot in Word, Excel or PowerPoint", "Use Copilot Chat with the file attached.", "Trainer demo only."],
    ["No Agent Builder", "Save the instructions as a request in Copilot Chat with the five policy files.", "Pair with a neighbor who has it."],
    ["No internet", "Phone hotspot.", "The files on the USB stick, the backup results and the decks work offline."]])]),
 ("capstone", "Capstone", "Day 3", [("ul", ["Each participant takes the capstone file for their unit track. It is new to them.", "Core: two Copilot apps, five-input requests, every output reviewed.",
    "Extension: connect to the HR assistant, or a starter prompt.", "Peer test at 13:30: pairs from different units. No scoring; the self-check is on the Day 3 lab page."])]),
]

# ------------------------------------------------------------------ browser labs: one per day; answers only in the staff lab key
LABS = {
 1: {"title": "Day 1, step by step, with hints", "intro": "One step for each task of Day 1. Download the files under the step that uses them. Write your own requests first; open a hint only when you are stuck. Your done marks stay in this browser.",
     "steps": [
        {"title": "Task 1.1 · Check the carry-over rule", "files": ["mutla-copilot-leave-answer.docx", "mutla-leave-policy-2026.docx"],
         "do": ["Open both files side by side. The policy is the source.", "Find what the answer says about carrying over leave, then find the same rule in the policy."],
         "hint": "Look at section 4 of the policy.", "hints": ["Look at section 4 of the policy.", "The answer says 30. Section 4 gives a different number and a deadline."],
         "check": {"kind": "flag", "label": "Type the date by which carried-over days must be used (for example: 30 June)", "answer": D.LEAVE["carry_by"]},
         "answer": [("p", f"The answer says 30 days. Section 4 says {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']}.")]},
        {"title": "Task 1.1 · Check the notice period and emergency leave", "files": ["mutla-copilot-leave-answer.docx", "mutla-leave-policy-2026.docx"],
         "do": ["Compare how early staff must request annual leave: the answer, then section 3.", "Compare the emergency leave days: the answer, then section 5."],
         "hint": "Sections 3 and 5.", "hints": ["Sections 3 and 5.", "Both numbers in the answer are wrong."],
         "check": {"kind": "flag", "label": "Type the number of days of notice in section 3 (digits only)", "answer": str(D.LEAVE["notice"])},
         "answer": [("p", f"Notice: the answer says 7 days; section 3 says {D.LEAVE['notice']}. Emergency leave: the answer says 5 days; section 5 says {D.LEAVE['emergency']}.")]},
        {"title": "Task 1.2 · Rewrite a weak request", "files": [],
         "do": ["Pick the weak request closest to your unit from the Task 1.2 slide.", "Write all seven parts: role, context, task, data, constraints, tone, output format.", "Paste your rewrite in the box."],
         "hint": "Start with the role: who would write this at Mutla?", "hints": ["Start with the role: who would write this at Mutla?", "Constraints are the limits: what must Copilot not add or change?"],
         "prompt": f"You are a Compensation officer at {D.COMPANY}. Staff keep asking about allowances. Summarize the attached allowances policy for staff. Use only mutla-allowances-policy-v4.docx. Give the section number for every point, and keep every amount as written. Plain and friendly. One page of bullets, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your rewrite here"},
         "answer": [("p", "Accept any rewrite with all seven parts and a named file. The Task 1.2 answer key has a model rewrite for each weak request.")]},
        {"title": "Task 1.3 · Your job description", "files": ["mutla-role-information-2026.docx", "mutla-jd-template-2026.docx"],
         "do": ["Find your track's role in the role information file.", "Write your checklist request and attach both files.", "Send two follow-ups that fix what is weak. Then run the source-trace request from the prompt sheet."],
         "hint": "Data names both files. Constraints say what Copilot must not add.", "hints": ["Data names both files. Constraints say what Copilot must not add.", "Constraints for a job description: only the attached files; no duties, team size or grade added; one page."],
         "prompt": f"You are an HR officer at {D.COMPANY}. It is for the 2026 job evaluation round; the Job Evaluation committee will read it. Draft the job description for the [your track's role]. Use the attached role information and the attached 2026 template. Use only the attached files. Do not add duties, a team size or a grade. Leave the grade line blank. One page. Formal, neutral, plain English; each duty starts with a verb. The template's headings, in order. Start with the line: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your request and your two follow-ups here"},
         "answer": [("p", "Six duties from the role sheet, a blank grade, the template's order, and the DRAFT line at the top.")]},
        {"title": "Task 1.4 · Ali's experience letter", "files": ["mutla-experience-letter-requests.docx"],
         "do": ["Read the template rules, the HR system record and Ali Al-Harbi's request.", "Write your checklist request for his letter, then run the flag request from the prompt sheet.", "Check his dates by hand against the HR system record."],
         "hint": "The HR system record decides the dates.", "hints": ["The HR system record decides the dates.", "Ali's request asks for one thing the template rules do not allow."],
         "prompt": f"You are a Personnel officer at {D.COMPANY}. Ali Al-Harbi needs an experience letter for his new employer. Draft his letter. Use the template and the HR system record in the attached file. Use the dates in the record, not in his request. No salary, no opinion about his work and no reason for leaving. Formal and short. The letter text only, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "flag", "label": "Type Ali's start date as it must appear in the letter (for example: 1 May 2020)", "answer": D.LETTER_ALI[4]},
         "answer": [("p", f"{D.LETTER_ALI[4]} to {D.LETTER_ALI[5]}, from the HR system record. He wrote 2014. \"The best technician in my team\" is an opinion and stays out.")]},
        {"title": "Task 1.5 · The allowances policy for staff", "files": ["mutla-allowances-policy-v4.docx", "mutla-allowances-policy-v3.docx"],
         "do": ["Write your checklist request for a one-page summary for staff, every point with its section number.", "Check three numbers by hand: the housing maximum, the transport grades, the remote-site days.", "Find the date version 4 starts. Does your summary say so?"],
         "hint": "Read the title of the policy file.", "hints": ["Read the title of the policy file.", "Until version 4 starts, version 3 still applies. Staff need both rules and the date."],
         "prompt": f"You are a Compensation officer at {D.COMPANY}. Staff will ask what the allowances are. Summarize the attached policy for staff. Use only mutla-allowances-policy-v4.docx. Give the section number for every point. Keep every amount and date as written, and say from which date this version applies. Plain and friendly. One page of bullets, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "flag", "label": "Type the date version 4 starts (for example: 1 May 2020)", "answer": D.ALLOW_V4_DATE},
         "answer": [("p", f"Version 4 applies from {D.ALLOW_V4_DATE}. Until then, version 3 applies (housing maximum KWD {D.ALLOW['housing_v3']}, transport for grades {D.ALLOW['transport_v3']}).")]},
        {"title": "Task 1.6 · One announcement, three readers", "files": ["mutla-email-thread-attendance.docx"],
         "do": ["Run the decisions request from the prompt sheet. Find the approved start date.", "Write your checklist request for the staff announcement, then the versions for line managers and senior leadership.", "Write the reply to Mubarak in message 29. Check every date and time against message 24."],
         "hint": "The start date changed during the thread.", "hints": ["The start date changed during the thread.", "Message 3 proposed a date. Message 24 approved another one."],
         "prompt": f"You are a Personnel officer at {D.COMPANY}. The new attendance rules were approved in the attached thread. Write the staff announcement. Use only the final decisions in the thread. Keep every date, time and rule as written; promise nothing about Ramadan hours. Warm and clear. A subject line and under 150 words, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "flag", "label": "Type the day and month of the approved start date (for example: 15 March)", "answer": "1 December"},
         "answer": [("p", f"The rules start on {D.ATT['start']} (message 24), not {D.ATT['old_start']} (message 3).")]},
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
                   "أستطيع كتابة طلب يتضمن الدور والسياق والمهمة والبيانات والقيود والأسلوب وشكل الناتج، وتحسين مسودة ضعيفة بتعليمات متابعة.",
                   "أستطيع استخدام Copilot في Word وOutlook لصياغة مستندات الموارد البشرية ورسائلها، وتغيير الأسلوب بحسب كل قارئ.",
                   "أستطيع إبقاء التفاصيل الشخصية وتفاصيل الرواتب والحالات خارج الطلبات.",
                   "أستطيع استخدام Copilot لملاحظات الاجتماعات والمتابعات وأرقام Excel وملخصات PowerPoint، وأتحقق من كل رقم.",
                   "أستطيع رسم مسار عملية في الموارد البشرية، وبناء وكيل بسيط للموارد البشرية واختباره، وتحديد متى نحتاج إلى مسار عمل في Power Automate."],
 "map_ar": [
  ("أخبر Copilot موظفاً أن الشهادة الطبية لا تُطلب إلا بعد 5 أيام من الإجازة المرضية. سياسة الإجازات في Mutla تنص على أنها تُطلب بعد يومين. لماذا يمكن أن يحدث هذا؟",
   ["نسخ Copilot الرقم من محادثة موظف آخر", "يتوقع الكلمات المرجحة، ولم يتحقق شيء من السياسة", "لم يحدد السؤال نوع الإجازة", "كان ملف السياسة أطول من أن يقرأه Copilot كاملاً"]),
  ("تستخدم حصة Copilot مع ترخيص Microsoft 365 Copilot. ما الملفات التي يمكنه استخدامها للإجابة عليها؟",
   ["كل ملف على SharePoint في الشركة، بما فيها مجلدات الموارد البشرية المقيدة", "الملفات التي ترفعها في هذه المحادثة فقط", "الملفات والرسائل والمحادثات التي لديها صلاحية فتحها فقط", "المواقع العامة فقط، وليس ملفات الشركة أبداً"]),
  ("أي مهمة تبقى لدى موظفي الموارد البشرية المخوّلين ولا تُسند إلى Copilot؟",
   ["صياغة وصف وظيفي من معلومات الدور المعتمدة", "تلخيص سياسة إجازات طويلة مع أرقام البنود", "تحديد درجة وظيفة أعيد تقييمها", "تغيير أسلوب إعلان موجّه للموظفين"]),
  ("يتضمن الوصف الوظيفي الذي كتبه Copilot مهاماً غير موجودة في معلومات الدور لدى Mutla. أي جزء من الطلب كان ناقصاً؟",
   ["الأسلوب (Tone): صياغة أكثر وداً", "السياق (Context): من سيقرأ الوصف الوظيفي", "شكل الناتج (Output format): عناوين القالب", "البيانات (Data): معلومات الدور المعتمدة، مرفقة"]),
  ("مسودة حصة الأولى من Copilot جيدة، لكنها من صفحتين والقالب يسمح بصفحة واحدة. ماذا تفعل بعد ذلك؟",
   ["ترد في المحادثة نفسها: اجعلها صفحة واحدة، واحتفظ بالمهام الست كلها", "ترسل الطلب نفسه مرة أخرى في محادثة جديدة ليبدأ Copilot من جديد", "تحذف الصفحة الثانية بنفسها مهما كان فيها", "تطلب من Copilot أن يكتب الوصف الوظيفي من جديد بشكل أقصر"]),
  ("تطلب حصة من Copilot أن يجعل إعلان عطلة العيد أكثر دفئاً. لم تعد النسخة الجديدة تذكر موعد عودة المكتب إلى العمل. أي طلب كان سيمنع ذلك؟",
   ["\"اجعله أكثر دفئاً، واحتفظ بالتحية الأصلية في أعلاه.\"", "\"اجعله أكثر دفئاً، واحتفظ بطوله كما كان.\"", "\"اجعله أكثر دفئاً، ولا تغيّر أي يوم أو وقت فيه.\"", "\"اجعله أكثر دفئاً، واحتفظ بالعناوين والتنسيق الأصليين.\""]),
  ("يريد خالد أن يلخّص Copilot رسالة تظلّم تذكر اسم الموظفة واسم مديرها ورقم بطاقتها المدنية. ما الذي يفعله أولاً؟",
   ["يستبدل الأسماء ويحذف رقم البطاقة المدنية قبل رفعها", "يطلب من Copilot في الطلب نفسه أن يُبقي الرسالة كلها سرية تماماً", "يفتح محادثة جديدة حتى تبقى الرسالة خاصة", "يختصر الرسالة حتى يقرأها Copilot أسرع"]),
  ("يريد عبدالعزيز من Copilot أن يجد خطأً في كشف رواتب يظهر فيه اسم كل موظف. ما لون هذه المهمة في بطاقة الاستخدام الآمن؟",
   ["أخضر: يمكنه المتابعة لأن الكشف لا يخرج من الموارد البشرية", "أحمر: لا يدخل في أي طلب، في أي حساب", "كهرماني: مقبول في حساب Copilot المعتمد في الشركة", "كهرماني: مقبول إذا حذف المحادثة بعد ذلك"]),
  ("بعد اجتماع عن ساعات العمل في رمضان، أي سطر من ملخص الاجتماع جاهز للإرسال؟",
   ["الإجراء: مقترح ساعات رمضان، في أقرب وقت ممكن", "الإجراء: يرسل شخص ما في الموارد البشرية مقترح ساعات رمضان", "الإجراء: مناقشة ساعات رمضان مرة أخرى الشهر القادم", "الإجراء: إرسال مقترح ساعات رمضان · المسؤولة: فاطمة · قبل الأحد 7 فبراير"]),
  (f"يسأل خالد Copilot عن عدد الموظفين الذين انضموا إلى Mutla في الربع الثالث. يقول Copilot إن العدد {D.MAP_Q10['count']}. الإجمالي المدقق في نظام الموارد البشرية هو {D.MAP_Q10['control']}. ماذا يفعل أولاً؟",
   [f"يستخدم {D.MAP_Q10['count']} لأن Copilot قرأ كل صف في الملف", f"يذكر {(D.MAP_Q10['count'] + D.MAP_Q10['control']) // 2}، الرقم الذي يقع في منتصف المسافة بين الرقمين", "يطلب من Copilot تقريب الرقمين إلى أقرب عشرة", f"يطلب الصفوف التي عدّها ويبحث عن الـ {D.MAP_Q10['count'] - D.MAP_Q10['control']} الزائدة"]),
  ("تصل طلبات التدريب بالبريد الإلكتروني. تطبع المنسقة كل طلب ليوقعه المدير، ثم تكتبه في جدول المتابعة. ماذا تُظهر خريطة هذه العملية؟",
   ["عدم وضوح المسؤولية: لا أحد يعرف من يوافق", "جهد مكرر: يُعالَج الطلب نفسه ثلاث مرات", "قرار يخص الأشخاص يجب أن يتخذه Copilot", "تأخير لا يحله إلا نظام جديد للموارد البشرية"]),
  ("يسأل الموظفون وكيل الموارد البشرية عن نصيحة في قضاياهم التأديبية. أين تضيف في Agent Builder السطر الذي يمنع ذلك ويحيلهم إلى الموارد البشرية؟",
   ["المعرفة (Knowledge)", "التعليمات (Instructions)", "طلبات البداية (Starter prompts)", "الوصف (Description)"]),
  ("يسأل مشرف وكيل الموارد البشرية: \"من الشخص في فريقي الذي أخذ أكثر أيام إجازة مرضية هذا العام؟\" ما الاستجابة الصحيحة؟",
   ["يجيب من ملف سياسة الإجازات", "يقدّر الإجابة من أرصدة إجازات الفريق", "يطلب الأرقام الوظيفية للفريق ثم يجيب", "يرفض ويحيل السائل إلى الموارد البشرية"]),
  ("يجب أن يذهب كل طلب تدريب إلى المدير المباشر للموافقة، ثم يُسجَّل في جدول المتابعة، ويصل إلى الموظف بريد إلكتروني بالنتيجة. أي أداة تناسب ذلك؟",
   ["طلب في Copilot Chat يرسله فريق الموارد البشرية لكل طلب تدريب", "وكيل في Agent Builder يجيب عن الأسئلة حول التدريب", "مسار عمل في Power Automate فيه خطوة موافقة", "طلب محفوظ في بنك الطلبات (Prompt Bank)"]),
 ],
 "day_ar": {1: "أساسيات Copilot لمستندات الموارد البشرية والتواصل", 2: "الاجتماعات والتقارير ورسم مسار عمل الموارد البشرية", 3: "وكلاء الموارد البشرية ومقدمة في Power Automate"},
 "relevance": ("The content was high quality and relevant to my HR work.", "كان المحتوى عالي الجودة وذا صلة بعملي في الموارد البشرية."),
 "hands_on": ("The hands-on parts, such as the job descriptions, the announcements, the HR tracker, the process map and the HR agent, helped me apply what I learned.",
              "ساعدتني الأجزاء التطبيقية، مثل الأوصاف الوظيفية والإعلانات وجدول الموارد البشرية وخريطة العملية ووكيل الموارد البشرية، على تطبيق ما تعلّمته."),
 "materials": ("The workshop website, the cheat sheet, the safe-use card and the take-home guide were clear and useful.",
               "كانت مواد ورشة العمل (الموقع وورقة المراجعة السريعة وبطاقة الاستخدام الآمن ودليل ما بعد ورشة العمل) واضحةً ومفيدة."),
 "logistics": ("The venue, the daily timing and access to Microsoft Copilot worked well for me.", "كان المكان والتوقيت اليومي وإمكانية الوصول إلى Microsoft Copilot مناسباً لي."),
}
