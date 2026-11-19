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
TOOLS = "Microsoft 365 Copilot: Copilot Chat with file upload, Copilot in Word, Outlook, Excel and PowerPoint, built-in agents (Prompt Coach, Researcher) and Agent Builder. Copilot in Microsoft Forms, and Power Automate in recorded trainer demos"
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
            "I can write a request with context, task, data, constraints and format, and fix a weak draft with follow-up instructions.",
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
               ("09:20-10:30", "Block 1 · How generative AI and Copilot work", "What AI is, where LLMs fit, next-word prediction, real cases, where your chat goes, what Copilot can see, then Copilot live: one job description, two requests · Task 1.1"),
               ("10:30-10:45", "Break", ""),
               ("10:45-11:35", "Block 2 · Writing a clear prompt", "The prompt checklist: five parts · Task 1.2"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:20", "Block 3 · Copilot Notebooks: your policies in one place", "Build a notebook from three policies, then answer three employees from it · Tasks 1.3 and 1.4"),
               ("13:20-13:35", "Break", ""),
               ("13:35-14:40", "Block 4 · Copilot in Word, then Outlook", "Draft a memo, summarize 360 feedback, rewrite a welcome letter, then one message for three readers · Tasks 1.5 to 1.8"),
               ("14:40-15:00", "Prompt Bank and wrap", "Save two requests, and where Copilot sits")],
    "outcomes": ["Explain why Copilot can write a <b>confident sentence that is wrong</b>, what it can see, and which HR decisions stay with people.",
                 "Write a request with the <b>prompt checklist</b>: context, task, data, constraints and format.",
                 "Improve a weak draft with <b>follow-up instructions</b>, and ask for the source of every line.",
                 "Draft HR documents in Word and messages in Outlook, and <b>change the tone</b> for each reader without changing the facts."]},
2: {"title": "Meetings, Reporting and Presentations", "claim": "Clear meetings, checked figures, safe data.",
    "sub": "Meetings and follow-ups, Excel figures you can check, a training needs form in Microsoft Forms, decks in PowerPoint, and protecting employee data.",
    "brief": "Day 2 starts with meetings: you prepare one, recap it into actions and follow it up in Outlook. In Excel you check a training count against a control total, then choose payroll or a messy overtime export to clean and chart. In Microsoft Forms you turn a vague training question into requirements, build the form with Copilot and analyze the answers in Excel or Forms. In PowerPoint you present what you found and fix a messy deck. The day ends with the most important habit: what may go into a prompt, and how to redact what may not.",
    "artifact": "A meeting pack and recap, follow-up emails, a training count, a payroll or overtime check, a training needs form and its findings, two decks, and a redacted case note",
    "blocks": [("09:00-09:10", "Callback quiz", "Three questions on Day 1, and the old way and the AI way"),
               ("09:10-10:10", "Block 1 · Before and after the meeting", "Agenda, brief, discussion points; notes into actions · Tasks 2.1 and 2.2"),
               ("10:10-10:45", "Block 2 · Follow-ups and reminders in Outlook", "Same owners, same dates · Tasks 2.3 and 2.4"),
               ("10:45-11:00", "Break", ""),
               ("11:00-11:35", "Block 3 · Excel: figures you can check", "A control total, a chart, payroll or cleaning data · Tasks 2.5 and 2.6"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:20", "Block 4 · Microsoft Forms: find the training needs", "Requirements first, a form with Copilot, then the answers in Excel or Forms · Tasks 2.7, 2.8 and 2.9"),
               ("13:20-13:35", "Break", ""),
               ("13:35-14:20", "Block 5 · PowerPoint: present what you found", "From a prompt, from your findings, fix a messy deck · Tasks 2.10 and 2.11"),
               ("14:20-14:50", "Block 6 · Protecting employee data", "Green, amber, red; redact, then ask · Task 2.12"),
               ("14:50-15:00", "Which app for which job, and wrap", "Outlook, Teams, Excel, Forms, PowerPoint")],
    "outcomes": ["Prepare a meeting, recap it into <b>actions, owners and deadlines</b>, and follow it up in Outlook.",
                 "Check Excel figures against a <b>control total</b> or a list of approved changes.",
                 "Turn a training question into <b>requirements</b>, build the form with Copilot in Forms, and <b>clean before you count</b> the answers.",
                 "Present checked findings in <b>PowerPoint</b>, and sort any HR task as <b>green, amber or red</b> before Copilot sees it."]},
3: {"title": "HR Agents, Workflows and an Introduction to Power Automate", "claim": "Build it, test it, then look at the whole process.",
    "sub": "Put a request on a timer, use two built-in agents, build and test your own HR agent in Agent Builder, see three Power Automate flows run on their own, and map an HR process from request to result.",
    "brief": "Day 3 starts with Copilot working for you on a timer: the trainer schedules a tested request to run every week. Then you use agents that Microsoft built: Prompt Coach improves one of your Prompt Bank requests, and Researcher answers a public HR question with sources that you check. Then you build a New Hire Onboarding Buddy in Agent Builder from three files (an onboarding checklist, an IT setup guide and a first-week FAQ), and test it with a normal, an incomplete and a sensitive question. Before lunch the trainer explains what automation means and when to automate, then talks you through three recorded Power Automate flows: a training request approval, a weekly AI brief for vendors, and a vendor quotation that AI reads and scores. After lunch you map a whole HR process: every step, every owner, every wait and every human decision.",
    "artifact": "A scheduled request, a better request from Prompt Coach, and a tested Onboarding Buddy",
    "blocks": [("09:00-09:10", "Callback quiz", "Three questions on Day 2"),
               ("09:10-09:50", "Block 1 · Scheduled prompts and built-in agents", "A request on a timer; Prompt Coach and Researcher · Tasks 3.0 and 3.1"),
               ("09:50-10:45", "Block 2 · Build your own agent", "Instructions, knowledge, starter prompts, three tests · Tasks 3.2 and 3.3, Task 3.4 if time allows"),
               ("10:45-11:00", "Break", ""),
               ("11:00-11:35", "Block 3 · Power Automate: when to automate", "Trigger, actions, connectors, output; three recorded flows"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:35", "Block 4 · From one task to a workflow", "Delays, duplicates, owners, human decisions · Tasks 3.6 and 3.7, Task 3.8 if time allows"),
               ("13:35-13:50", "Break", ""),
               ("13:50-14:05", "Copilot, agent or flow?", "The tools side by side, and a card sort"),
               ("14:05-14:20", "One-minute share-outs", "One agent or one map"),
               ("14:20-14:40", "Post-MAP test, then the final survey", "Two QR codes"),
               ("14:40-15:00", "Close and certificates", "The habit, one last time")],
    "outcomes": ["Explain what a <b>scheduled prompt</b> does, and use a <b>built-in agent</b> such as Prompt Coach or Researcher, checking what it gives you.",
                 "Build an HR agent with the <b>prompt checklist</b> and approved files, and test it with a <b>normal, an incomplete and a sensitive</b> question.",
                 "Explain <b>when to automate</b>, and name the trigger, actions, connectors and output of a Power Automate flow.",
                 "Map an HR process from request to result, and mark the <b>delays, duplicates, owners and human decisions</b>."]},
}

SEGMENTS = {
 1: [("09:20-10:30", "Block 1 · How generative AI and Copilot work", [("09:20", 3, "Who used AI this week?"), ("09:23", 4, "What AI is; AI you already use"), ("09:27", 5, "Where LLMs fit; what LLM means"), ("09:32", 9, "Next-word prediction and hallucination"), ("09:41", 4, "Real cases; quick check"), ("09:45", 4, "Where your chat goes"), ("09:49", 6, "What Copilot can see; your label"), ("09:55", 8, "Meet Copilot: Demo 1.0"), ("10:03", 4, "Demo 1.1"), ("10:07", 10, "Task 1.1"), ("10:17", 3, "Debrief"), ("10:20", 8, "What stays with people; Demo 1.1b card sort"), ("10:28", 1, "Quick check"), ("10:29", 1, "Practice files only today")]),
     ("10:45-11:35", "Block 2 · Writing a clear prompt", [("10:45", 3, "Story: the one-line reminder"), ("10:48", 4, "Brief a new colleague"), ("10:52", 12, "The prompt checklist"), ("11:04", 4, "Constraints"), ("11:08", 6, "Demo 1.2"), ("11:14", 2, "Quick check"), ("11:16", 14, "Task 1.2"), ("11:30", 5, "Debrief")]),
     ("12:15-13:20", "Block 3 · Copilot Notebooks: your policies in one place", [("12:15", 2, "Story: the same questions every week"), ("12:17", 4, "What a notebook is; its three parts"), ("12:21", 5, "Demo 1.3"), ("12:26", 22, "Task 1.3"), ("12:48", 2, "Quick check"), ("12:50", 20, "Task 1.4"), ("13:10", 3, "Quick check"), ("13:13", 7, "Debrief")]),
     ("13:35-14:40", "Block 4 · Copilot in Word, then Outlook", [("13:35", 2, "Story: three jobs, one app"), ("13:37", 3, "Three things Copilot does in Word"), ("13:40", 3, "Demo 1.5: draft"), ("13:43", 10, "Task 1.5"), ("13:53", 3, "Demo 1.6: summarize"), ("13:56", 12, "Task 1.6"), ("14:08", 1, "Quick check"), ("14:09", 3, "Demo 1.7: rewrite"), ("14:12", 12, "Task 1.7"), ("14:24", 1, "The tone dial (Outlook, if time allows)"), ("14:25", 3, "Demo 1.8"), ("14:28", 10, "Task 1.8, or tomorrow"), ("14:38", 2, "Debrief")])],
 2: [("09:10-10:10", "Block 1 · Before and after the meeting", [("09:10", 3, "Story: the meeting with no actions"), ("09:13", 6, "Before, during, after; what Teams needs"), ("09:19", 6, "Demo 2.1"), ("09:25", 15, "Task 2.1"), ("09:40", 5, "Demo 2.2"), ("09:45", 2, "Quick check"), ("09:47", 15, "Task 2.2"), ("10:02", 8, "Debrief")]),
     ("10:10-10:45", "Block 2 · Follow-ups and reminders", [("10:10", 3, "Story: the deadline nobody chased"), ("10:13", 5, "Demo 2.3"), ("10:18", 12, "Task 2.3"), ("10:30", 10, "Task 2.4"), ("10:40", 5, "Debrief")]),
     ("11:00-11:35", "Block 3 · Excel", [("11:00", 2, "Story: 412 or 398"), ("11:02", 4, "Ask, see the rows, check"), ("11:06", 5, "Demo 2.5"), ("11:11", 10, "Task 2.5"), ("11:21", 12, "Task 2.6"), ("11:33", 2, "Debrief")]),
     ("12:15-13:20", "Block 4 · Microsoft Forms", [("12:15", 2, "Story: 52 managers, 31 answers"), ("12:17", 3, "What Copilot does in Forms"), ("12:20", 4, "Demo 2.7"), ("12:24", 12, "Task 2.7"), ("12:36", 5, "Demo 2.8"), ("12:41", 13, "Task 2.8"), ("12:54", 5, "Demo 2.9"), ("12:59", 15, "Task 2.9"), ("13:14", 6, "Quick check and debrief")]),
     ("13:35-14:20", "Block 5 · PowerPoint", [("13:35", 2, "Story: the deck for Sunday"), ("13:37", 3, "What Copilot does in PowerPoint"), ("13:40", 5, "Demo 2.10"), ("13:45", 12, "Task 2.10"), ("13:57", 4, "Demo 2.11"), ("14:01", 14, "Task 2.11"), ("14:15", 5, "Quick check and debrief")]),
     ("14:20-14:50", "Block 6 · Protecting employee data", [("14:20", 2, "Story: the comment with a name"), ("14:22", 4, "Green, amber, red"), ("14:26", 6, "Demo 2.12 card sort"), ("14:32", 4, "Demo 2.12b: redact, then ask"), ("14:36", 10, "Task 2.12"), ("14:46", 4, "Quick check and debrief")])],
 3: [("09:10-09:50", "Block 1 · Scheduled prompts and built-in agents", [("09:10", 2, "Scheduled prompts: the idea"), ("09:12", 5, "Demo 3.0"), ("09:17", 2, "Before you schedule"), ("09:19", 6, "Task 3.0"), ("09:25", 2, "Story: two jobs before lunch"), ("09:27", 3, "What an agent is; agents built by Microsoft"), ("09:30", 7, "Demo 3.1"), ("09:37", 10, "Task 3.1"), ("09:47", 3, "Quick check")]),
     ("09:50-10:45", "Block 2 · Build your own agent", [("09:50", 3, "Story: the same 20 questions"), ("09:53", 4, "Built-in or your own; the parts of an agent"), ("09:57", 6, "Demo 3.2"), ("10:03", 20, "Task 3.2"), ("10:23", 5, "Three tests; Demo 3.3"), ("10:28", 12, "Task 3.3; Task 3.4 if time allows"), ("10:40", 5, "Debrief")]),
     ("11:00-11:35", "Block 3 · Power Automate: when to automate", [("11:00", 2, "Story: requests and quotations"), ("11:02", 3, "What automation means"), ("11:05", 3, "When to automate"), ("11:08", 5, "Automate it or not? The room votes"), ("11:13", 3, "Trigger, actions, connectors, output"), ("11:16", 5, "Demo 3.5: approval"), ("11:21", 4, "Demo 3.5b: weekly brief"), ("11:25", 4, "Demo 3.5c: quotation"), ("11:29", 2, "What a flow needs"), ("11:31", 2, "Why a flow"), ("11:33", 2, "Quick check")]),
     ("12:15-13:35", "Block 4 · From one task to a workflow", [("12:15", 3, "Story: three weeks for one course"), ("12:18", 5, "Four problems"), ("12:23", 3, "The step table"), ("12:26", 5, "Demo 3.6"), ("12:31", 12, "Task 3.6"), ("12:43", 20, "Task 3.7"), ("13:03", 25, "Task 3.8 (if time allows)"), ("13:28", 7, "Debrief")]),
     ("13:50-14:05", "Copilot, agent or flow?", [("13:50", 5, "The tools side by side"), ("13:55", 8, "Demo 3.9 card sort"), ("14:03", 2, "Quick check")])],
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
SELFCHECK = ["Every step has one owner, and a role, not \"HR\".", "Every approval and decision about a person is marked Person.",
             "At least two problems from the map are removed.", "The piece you built has all five checklist parts.",
             "Three tests are logged: normal, incomplete, sensitive.", "No real names or real data anywhere on the card."]

# ------------------------------------------------------------------ cheat sheet and take-home guide
CHEAT = [("Part 1 · Ask well", "The prompt checklist", "Five parts. Use all five for anything that matters.",
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
           ("Scheduled prompts", "Hover over a request, then Schedule this prompt", "Runs a tested request at a set time. The answer waits in your Copilot chats. It does not send or approve.", "Microsoft 365 Copilot license; up to 10 per person."),
           ("Built-in agents", "Agents, then All agents", "Agents Microsoft built for one job: Prompt Coach for better requests, Researcher for reports with sources.", "Researcher and Analyst need the Microsoft 365 Copilot license."),
           ("Copilot in the apps", "Word, Outlook, Excel, PowerPoint", "Draft, summarize and analyze inside the app.", "What you get depends on your license."),
           ("Agent Builder", "Create agent, Configure, Test", "An agent with your instructions and approved files that answers the same questions for many people.", "It answers. It does not send, route or approve."),
           ("Power Automate", "A flow, not a chat", "Runs on its own when something happens: a form is sent, an email arrives, a date comes. Routes approvals, logs rows, sends emails, and can include an AI step.", "Ask your IT team before you build one.")],
          "The same checklist works in every Copilot tool.")]
CHEAT_LEDE = "The prompt checklist, six HR requests that work, the four-point review, and where Copilot sits. On one page."
GUIDE_INTRO = "Repeat what you built, on your own work, safely. Start with green tasks. Your company's AI and data policy comes first."
GUIDE = [("Your first week", ["Write one checklist request a day on a green task.", "Fix the first draft with a follow-up instead of starting again.",
                              "Run the four-point review on each result before it goes anywhere.", "Read the license label under your name, so you know which Copilot you have.",
                              "Give one weak request to Prompt Coach and save the better version in your Prompt Bank."]),
         ("Your first month", ["Map one process your unit runs every month. Mark each step: a person, Copilot, an agent or a flow.",
                               "Build an agent for the questions your unit answers most, with approved files only. Test it three ways.",
                               "Ask a colleague from another unit to try it with no instructions, then fix what broke.",
                               "For steps that need a flow, ask your IT team whether Power Automate is allowed."])]
GUIDE_HABIT = "Copilot drafts. You check. Authorized HR staff decide. Your company's AI and data policy comes first."
GUIDE_META = [("home", "Your own work, safely"), ("list", "First week, first month"), ("shield", "Policy first")]

# ------------------------------------------------------------------ MAP test: same 14 questions before and after, 6 confidence items
CONFIDENCE = OUTCOMES
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
  "o": ["Format: a friendlier tone", "Context: who will read the job description", "Constraints: one page at most", "Data: the approved role information, attached"],
  "a": 3, "day": 1, "topic": "The prompt checklist", "where": "Day 1 · Block 2 · the prompt checklist"},
 {"q": "Hessa's first draft from Copilot is good, but it is two pages, and the template allows one. What does she do next?",
  "o": ["Reply in the same chat: make it one page, and keep all six duties", "Send the same request again in a new chat, so that Copilot starts fresh", "Delete the second page herself, whatever is on it", "Ask Copilot to write the job description again, but shorter"],
  "a": 0, "day": 1, "topic": "Follow-up instructions", "where": "Day 1 · Block 3 · Demo 1.3"},
 {"q": "Hessa asks Copilot to make the Eid holiday notice warmer. The new version no longer says when the office reopens. Which request would have stopped this?",
  "o": ["\"Make it warmer, and keep the original greeting at the top.\"", "\"Make it warmer, and keep it the same length as before.\"", "\"Make it warmer, and change no day or time in it.\"", "\"Make it warmer, and keep the original headings and layout.\""],
  "a": 2, "day": 1, "topic": "Tone, same facts", "where": "Day 1 · Block 4 · tone dial, Task 1.6"},
 {"q": "Khaled wants Copilot to summarize a grievance letter that names the employee, her manager and her civil ID. What does he do first?",
  "o": ["Replace the names and remove the civil ID before he uploads it", "Ask Copilot, in the prompt, to keep the whole letter strictly confidential", "Open a new chat so that the letter stays private", "Shorten the letter so that Copilot reads it faster"],
  "a": 0, "day": 2, "topic": "Redact first", "where": "Day 2 · Block 6 · redact"},
 {"q": "Abdulaziz wants Copilot to find a mistake in a salary list that shows each employee's name. Which color is this task on the safe-use card?",
  "o": ["Green: go ahead, because the list never leaves HR", "Red: never in a prompt, in any account", "Amber: fine in the company's approved Copilot account", "Amber: fine if he deletes the chat afterwards"],
  "a": 1, "day": 2, "topic": "Green, amber, red", "where": "Day 2 · Block 6 · the safe-use card"},
 {"q": "After a meeting about Ramadan working hours, which line of the recap is ready to send?",
  "o": ["Action: the Ramadan hours proposal, as soon as possible", "Action: someone in HR sends the Ramadan hours proposal", "Action: discuss the Ramadan hours again next month", "Action: send the Ramadan hours proposal · Owner: Fatma · By Sunday 7 February"],
  "a": 3, "day": 2, "topic": "Meeting recap", "where": "Day 2 · Block 1 · meeting actions"},
 {"q": f"Khaled asks Copilot how many employees joined Mutla in {D.MAP_Q10['quarter']}. Copilot says {D.MAP_Q10['count']}. The HR system's checked total is {D.MAP_Q10['control']}. What does he do first?",
  "o": [f"Use {D.MAP_Q10['count']}, because Copilot read every row of the file", f"Report {(D.MAP_Q10['count'] + D.MAP_Q10['control']) // 2}, the number halfway between the two", "Ask Copilot to round both numbers to the nearest ten", f"Ask for the rows it counted and find the {D.MAP_Q10['count'] - D.MAP_Q10['control']} extra"],
  "a": 3, "day": 2, "topic": "Control totals", "where": "Day 2 · Excel · control totals"},
 {"q": "Training requests arrive by email. The coordinator prints each one for the manager to sign, then types it into the tracker. What does the process map show?",
  "o": ["Unclear ownership: nobody knows who approves", "Duplicated effort: the same request is handled three times", "A decision about people that Copilot should make", "A delay that only a new HR system can fix"],
  "a": 1, "day": 3, "topic": "Process problems", "where": "Day 3 · Block 4 · mapping an HR process"},
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
SLIDES = {1: 70, 2: 61, 3: 57}

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
DAYS[2].update({"cat": "Meetings, reporting, presentations", "icon": "mail", "tag": "Outlook · Excel · Forms · PowerPoint · safe data",
                "bullets": ["Meetings, follow-ups and checked figures", "A training needs form with Copilot, and its findings", "Decks in PowerPoint, then green, amber, red"]})
DAYS[3].update({"cat": "Agents, workflows, Power Automate", "icon": "flask", "tag": "Scheduled prompts · built-in agents · Agent Builder · Power Automate demos · process maps",
                "bullets": ["Schedule a request, use built-in agents, then build and test your own", "See three Power Automate flows, and know when to automate", "Map an HR process from request to result"]})
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
DAY_NO_TASKS = True     # day pages show no "Your turn" list: tasks live on the slides and the lab page (engine option, approved 16 Nov 2026)
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
                     "Day 2: open forms.cloud.microsoft with the training account and check that New Form shows the Draft with Copilot box. If it does not, prepare the Quick import fallback (a Word file with the nine questions).",
                     "Day 2: open the training mailbox in Outlook and check that the thread Orientation day for new joiners, Sunday 6 December is there, with three messages.",
                     "Day 3: in Copilot Chat on the presenting laptop, check that Schedule this prompt appears when you hover over a request (Microsoft 365 Copilot license).",
                     "Day 3: open Agents on the presenting laptop and check that Prompt Coach and Researcher open. Start one Researcher run before 09:00: it takes a few minutes and has a monthly limit.",
                     "Day 3: open Agent Builder (Create agent) once before the day starts. If it is missing, use the fallback in the runbook.",
                     "Day 3: open the deck on the workshop site and play the first seconds of the three Power Automate videos (no sound: you narrate). Copy the three video files from the Day 3 page to the laptop and the USB stick.",
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
    "Tables of four, by unit track where possible, facing the screen. Pairs sit side by side for Tasks 1.1, 2.5, 2.6, 2.7, 2.9 and 3.6.",
    "Wi-Fi name and password on the board before 08:45.",
    "Day 1, 09:00: every laptop opens Copilot Chat and is signed in. The pre-MAP QR at 09:10 is also the pre-flight.",
    "Everything is digital: the safe-use card and the cheat sheet are on the workshop site. Nothing is printed."])]),
 ("failplan", "If something fails", "Plan A, B, C", [("table", [["What fails", "Plan B", "Plan C"],
    ["Copilot is slow or busy", "Wait one minute, then send the request again.", "Show the backup result on your own screen."],
    ["A daily limit is reached", "Pair with a neighbor.", "Continue from the backup result."],
    ["No Copilot in Word, Excel or PowerPoint", "Use Copilot Chat with the file attached.", "Trainer demo only."],
    ["No Schedule this prompt option", "No Microsoft 365 Copilot license, or the admin turned it off: watch the trainer's demo.", "Show the steps on the slide."],
    ["No Prompt Coach or Researcher", "Paste the request into Copilot Chat and ask it to answer as a prompt coach, or to give a source for each point.", "Watch the trainer's demo."],
    ["No Agent Builder", "Save the instructions as a request in Copilot Chat with the knowledge files attached.", "Pair with a neighbor who has it."],
    ["A demo video does not play", "Open the video file from the Day 3 page or the USB stick.", "Walk through the four parts on the slide."],
    ["No internet", "Phone hotspot.", "The files on the USB stick, the backup results and the decks work offline."]])]),
 ("project", "Workflow block", "Day 3, 12:15", [("ul", ["Tasks 3.6 and 3.7 map a process as it runs today. Task 3.8 improves the map, only if the block is on time.",
    "Running late: skip Task 3.8 and its slide, give the debrief, and go to the comparison after the break.",
    "Task 3.8 marks each step Person, Copilot or Agent. Flows stay in the trainer demo.",
    "Walk the room during Task 3.7 and ask one question per person: where does it wait, and who decides?"])]),
 ("pa", "Power Automate demos", "Day 3, 11:00", [("ul", ["Trainer demo only: participants do not build flows. Three recorded videos with no sound: you narrate each one. The script is in the runbook (Demos 3.5, 3.5b, 3.5c).",
    "Explain the four parts first: trigger, actions, connectors, output. Then name them aloud as each video shows them.",
    "Demo 1 is a form, an approval, a row and an email. Demo 2 starts on a schedule and uses an AI prompt to draft a vendor brief. Demo 3 starts when a quotation email arrives; AI pulls out the details and scores the offer.",
    "Say it in the room: a flow needs a Microsoft 365 account that includes Power Automate, and the company's IT approval. The AI prompt step uses AI credits that the company's plan must include.",
    "Keep every decision with a person: the approver approves, L&D reviews the draft brief and chooses the vendor. The AI step drafts and scores."])]),
]

# ------------------------------------------------------------------ the final project page (Day 3 lab): the brief, the options, the example card
PROJECT_OPTIONS = [(n, D.STORIES[k]["title"]) for k, n in D.TRACKS] + [("Your own task", "A process from your own work, written with roles only")]
PROJECT_SUBMIT = None   # the CODED platform form for the final project; until it exists, the trainer shares the link in class
def _row(cells, tag="td"): return "<tr>" + "".join(f"<{tag}>{x}</{tag}>" for x in cells) + "</tr>"
PROJECT_LEDE = ('<div class="wrap"><div class="sheet">'
    '<div class="sh-part rvl"><div class="sh-ph">Task 3.8, if time allows: improve your map</div>'
    '<p>If there is time in Block 4, improve the process you mapped in Task 3.7. Mark each step Person, Copilot or Agent, remove the problems you found, '
    'and fill in the workflow card. Every approval and every decision about a person stays with a person.</p>'
    '<div class="tblwrap"><table class="tbl"><thead>' + _row(["Track", "Process"], "th") + '</thead><tbody>' + "".join(_row([a, b]) for a, b in PROJECT_OPTIONS) + '</tbody></table></div></div>'
    '<div class="sh-part rvl"><div class="sh-ph">A filled-in example: a training request</div>'
    '<div class="tblwrap"><table class="tbl"><thead>' + _row(["Card line", "Example"], "th") + '</thead><tbody>' + "".join(_row([a, b]) for a, b in zip(D.CARD_FIELDS, D.CARD_EXAMPLE)) + '</tbody></table></div></div>'
    '</div></div>')

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
         "do": ["Pick the weak request closest to your unit from the Task 1.2 slide.", "Write all five parts: context, task, data, constraints, format.", "Paste your rewrite in the box."],
         "hint": "Start with the context: who writes this at Mutla, and who reads it?", "hints": ["Start with the context: who writes this at Mutla, and who reads it?", "Constraints are the limits: what must Copilot not add or change?"],
         "prompt": f"You are a Compensation officer at {D.COMPANY}. Staff keep asking about allowances. Summarize the attached allowances policy for staff. Use only mutla-allowances-policy-v4.docx. Give the section number for every point, and keep every amount as written. Plain and friendly. One page of bullets, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your rewrite here"},
         "answer": [("p", "Accept any rewrite with all five parts and a named file. The Task 1.2 answer key has a model rewrite for each weak request.")]},
        {"title": "Task 1.3 · Build your HR policy notebook", "files": ["mutla-leave-policy-2026.docx", "mutla-attendance-rules-2026.docx", "mutla-training-policy-2026.docx"],
         "do": ["A notebook keeps your files and your instructions together. Copilot answers only from the files you add, not from the web.",
                "Download the three files, then save them to OneDrive (Documents).",
                "Go to m365.cloud.microsoft and sign in with your work account. On the left, select Notebooks, then New notebook.",
                "Name it: Mutla HR policies (practice). Under Add references, search for each file and select Add. Then select Create.",
                "Open the notebook's instructions and paste the notebook instruction below (use COPY).",
                "Test it: one question for each file. Check the file and section in every answer."],
         "templates": [("Notebook instruction", f"You answer employees' questions about {D.COMPANY}'s HR policies. Use only the files in this notebook. For every answer, name the file and the section. If the files do not answer the question, say so and suggest the employee asks Personnel. Never guess a number or a date. Plain English, short sentences.")],
         "hint": "No Notebooks on the left? Attach the three files to Copilot Chat and paste the instruction as your first message.",
         "hints": ["No Notebooks on the left? Attach the three files to Copilot Chat and paste the instruction as your first message.",
                   "Can't find a file under Add references? Check it is saved in OneDrive, or upload it from your computer in the same panel."],
         "check": {"kind": "note", "label": "Paste one test question, the answer, and the file and section it named"},
         "answer": [("p", "Three references, the instruction in the notebook's instructions, and test answers that name a file and section with numbers that match the policy.")]},
        {"title": "Task 1.4 · Answer three employees from your notebook", "files": [],
         "do": ["Ask your notebook each question below, one at a time.",
                "Noura, Drilling: I still have 22 days of annual leave. How many can I carry into next year, and by when must I use them?",
                "Saad, Finance: When the new rules start, can I come in at 6:45 and leave earlier? What hours must I be at work?",
                "Mariam, HSE: How do I ask for a training course, and who has to approve it?",
                "Then ask: What are the working hours in Ramadan?",
                "Open each file at the section named and check every number, time and date. Then draft a reply to one employee in Outlook or Word with Copilot, starting with the DRAFT line."],
         "hints": ["If an answer names no file or section, ask for them. Then open the file yourself.", "The Ramadan question is a test. What should a notebook say when the files do not answer?"],
         "check": {"kind": "note", "label": "Paste your reply draft, and the file and section you checked it against"},
         "answer": [("p", f"Noura: up to {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']} (section 4). Saad: from {D.ATT['start']}, start between {D.ATT['flex_from']} and {D.ATT['flex_to']}, at work {D.ATT['core_from']} to {D.ATT['core_to']}. Mariam: as the training policy says, with its section. Ramadan: not in the files; Personnel will confirm.")]},
        {"title": "Task 1.5 · Draft the training needs survey memo", "files": [],
         "do": ["Open a blank Word document and select Draft with Copilot. No Copilot in Word? Use Copilot Chat.",
                f"The facts: the 2027 training needs survey opens on {D.TNS['open']} and closes on {D.TNS['close']}. It is in {D.TNS['where']}. Line managers add {D.TNS['what']}. L&D shares the 2027 training plan by {D.TNS['plan']}. Questions: {D.TNS['contact']}.",
                "Write your own request with all five parts. Paste the facts as your Data.",
                "Check every date in the memo against the facts. Delete anything Copilot added."],
         "hints": ["Constraints: use only these facts; add no link, name or date.", "Format: a subject line, the steps as numbered points, under 200 words, the DRAFT line first."],
         "prompt": "FILL:MEMO",
         "check": {"kind": "note", "label": "Paste your memo's subject line and first sentence"},
         "answer": [("p", "Every date as in the facts, the steps numbered, and no link, name or extra date added.")]},
        {"title": "Task 1.6 · Summarize 360 feedback", "files": ["mutla-360-feedback-emp-4127.docx"],
         "do": ["Open the file in Word. Select Copilot, then Summarize this document. No Copilot in Word? Attach it to Copilot Chat.",
                "Ask for strengths, development areas and projects, with who said each point (by role).",
                "Read the summary against the file. Is anything there that should not reach a review meeting?"],
         "hints": ["Two lines in the file are not about the work.", "Constraints: name who said each point; leave out private life; do not suggest a rating."],
         "prompt": "FILL:R360",
         "check": {"kind": "note", "label": "List what you left out of the summary, by type only, and why"},
         "answer": [("p", "A comment about problems at home (private life) and a suggested rating (the manager and HR decide). Every other point has its reviewer.")]},
        {"title": "Task 1.7 · Rewrite the 2019 welcome letter", "files": ["mutla-welcome-letter-2019.docx", "mutla-onboarding-checklist-2026.docx"],
         "do": ["Open the 2019 letter in Word. Select one paragraph at a time, then Copilot, Rewrite. No Copilot in Word? Paste each paragraph into Copilot Chat.",
                "Make it warm, short and clear for a new graduate. Put the first day in a short list.",
                "Check every time, place and document against the onboarding checklist. Where they differ, the checklist wins."],
         "hints": ["Rewrite changes the words, not the facts. Old facts stay old.", "Read section 2 and section 4 of the checklist."],
         "prompt": "Rewrite this paragraph for a new graduate: short, warm and clear. Use the attached onboarding checklist for every time, place and document. Where the paragraph differs from the checklist, use the checklist and tell me what changed.",
         "check": {"kind": "note", "label": "List the facts you changed because the checklist says something different"},
         "answer": [("p", "First day, documents and probation now follow the 2026 checklist.")]},
        {"title": "Task 1.8 · One announcement, three readers", "files": ["mutla-email-thread-attendance.docx"],
         "do": ["Run the decisions request from the prompt sheet. Find the approved start date.", "Write your checklist request for the staff announcement, then the versions for line managers and senior leadership.", "Write the reply to Mubarak in message 29. Check every date and time against message 24."],
         "hint": "The start date changed during the thread.", "hints": ["The start date changed during the thread.", "Message 3 proposed a date. Message 24 approved another one."],
         "prompt": f"You are a Personnel officer at {D.COMPANY}. The new attendance rules were approved in the attached thread. Write the staff announcement. Use only the final decisions in the thread. Keep every date, time and rule as written; promise nothing about Ramadan hours. Warm and clear. A subject line and under 150 words, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "flag", "label": "Type the day and month of the approved start date (for example: 15 March)", "answer": "1 December"},
         "answer": [("p", f"The rules start on {D.ATT['start']} (message 24), not {D.ATT['old_start']} (message 3).")]},
     ]},
 2: {"title": "Day 2, step by step, with hints", "intro": "One step for each task of Day 2, and one for each option where a task lets you choose. Download the files under the step that uses them. Write your own requests first; open a hint only when you are stuck. Your done marks stay in this browser.",
     "steps": [
        {"title": "Task 2.1 · Prepare your track's meeting", "files": [D.CASES[k]["file"] for k, _n in D.TRACKS],
         "do": ["Open your track's case file. Find the meeting in it.", "Write your checklist request for an agenda, a background brief and three discussion points. Attach the case file.", "Check: an owner for every item, minutes that add up, every fact in the case file."],
         "hints": ["The case file says who meets, and about what.", "Turn the open question in the case into a discussion point. Constraints: only the case file; an owner and minutes for each item."],
         "prompt": f"You are an HR officer at {D.COMPANY}. I meet [who] for 30 minutes about [topic]. Prepare an agenda, a one-paragraph background brief and three discussion points. Use only the attached case file. Give each agenda item an owner and minutes that add up to 30. Turn each open question into a discussion point. Short and practical. An agenda table (item, owner, minutes), then the brief, then the discussion points. Start with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your request here"},
         "answer": [("p", "Accept an agenda with owners and minutes, a brief from the case facts only, and the case's open question as a discussion point.")]},
        {"title": "Task 2.2 · Recap the staffing meeting", "files": ["mutla-meeting-transcript-staffing.docx"],
         "do": ["Attach the transcript to a new chat.", "Write your checklist request for a recap: decisions, then action, owner and deadline, then open questions.", "Check each owner and deadline against the transcript. Delete anything nobody agreed."],
         "hints": ["Look for the lines where a person says \"I will\" and gives a day.", "One question in the meeting was not decided. It goes under open questions, not decisions."],
         "prompt": "FILL:RECAP",
         "check": {"kind": "flag", "label": "Type the day and month of Khaled's deadline (for example: 1 June)", "answer": D.STAFF_ACTIONS[0][2].split(" ", 1)[1]},
         "answer": [("p", f"Khaled Al-Ajmi prepares the manpower request by {D.STAFF_ACTIONS[0][2]}. Open question: {D.STAFF_OPEN[0]}.")]},
        {"title": "Task 2.3 · Follow up, and remind Khaled", "files": ["mutla-meeting-transcript-staffing.docx"],
         "do": ["Use your recap from Task 2.2.", "Write your checklist request for a follow-up email to everyone at the meeting.", "Then ask for a polite reminder to Khaled, two days before his deadline.", "Check every owner and date against the transcript."],
         "hints": ["The reminder asks. It does not blame.", "Constraints: keep every owner and date exactly as in the recap. Ask for two emails, each with a subject line."],
         "prompt": f"From the recap above, write a follow-up email to everyone at the meeting with the action table. Then write a short reminder to Khaled about the manpower request, two days before its deadline. Keep every owner and date exactly as in the recap. No blame. Polite and short. Two emails, each with a subject line, each starting with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste the subject lines of your two emails"},
         "answer": [("p", "All four actions with owners and deadlines unchanged; a reminder that names the manpower request and its deadline, with no blame.")]},
        {"title": "Task 2.4 · Your track's message", "files": [D.CASES[k]["file"] for k, _n in D.TRACKS],
         "do": ["Open your track's case file again. Find who needs a message, and why.", "Write your checklist request for that message. Attach the case file.", "Check every date and number. No employee names in the message."],
         "hints": ["Who reads it, and what must they do after reading it?", "Data: the case file. Constraints: every date and number as written; promise nothing the case does not say."],
         "prompt": f"You are an HR officer at {D.COMPANY}. [Who] needs to know [what] before [date]. Write the message. Use only the attached case file. Keep every date and number as written; promise nothing the case does not say; no employee names. Polite and clear. A subject line and under 150 words, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your subject line and first sentence"},
         "answer": [("p", "Job Evaluation: the reply gives no grade and says only the committee decides. Other tracks: every date and number from the case file.")]},
        {"title": "Task 2.5 · Training requests: find the duplicates", "files": ["mutla-hr-trackers-q3-2026.xlsx"],
         "do": ["Attach the tracker. Ask Copilot for every request ID that appears more than once.", "Check in Excel: select the Request ID column, then Conditional Formatting, Highlight Cells Rules, Duplicate Values.", "Write the corrected total, and why it changed."],
         "hints": ["Compare the Training sheet's row count with the Control totals sheet.", "Each request ID should appear once. Count the IDs that appear twice."],
         "prompt": "The Training sheet total does not match the Control totals sheet. List every request ID that appears more than once, with its row numbers. Do not delete anything.",
         "check": {"kind": "flag", "label": "Type the corrected number of Q3 training requests (digits only)", "answer": str(D.TRAIN_TRUE)},
         "answer": [("p", f"{D.TRAIN_DUPES} request IDs appear twice. Without them, the count is {D.TRAIN_TRUE}, not {D.TRAIN_ROWS_EXPORT}.")]},
        {"title": "Task 2.6 · Option A: payroll, two months", "files": ["mutla-payroll-check-oct-nov-2026.xlsx"],
         "do": ["Attach the payroll file. It has employee codes and no names, so use your company's approved account.", "Ask Copilot to compare October with November, then to check the Movements sheet.", "Check each item yourself in Excel. Write one line for each item a person must confirm. Change no salary."],
         "hints": ["Comparing the two months shows only what changed. A person who should have left did not change.", "Check every line of the Movements sheet against the November sheet."],
         "prompt": "FILL:PAYREQ",
         "check": {"kind": "flag", "label": "Type the employee code of the leaver who is still paid (for example: EMP-1000)", "answer": D.PAY_ISSUES[1][0]},
         "answer": [("p", "EMP-3346: an increase with no movement behind it. EMP-2731: left on 31 October, still paid. EMP-5114: joined on 1 November, missing.")]},
        {"title": "Task 2.6 · Option B: clean, chart and check the overtime export", "files": ["mutla-overtime-export-oct-2026.xlsx"],
         "do": ["Attach the file to Copilot Chat, or open it in Excel with Copilot. Ask for every cleaning problem, with row numbers. Change nothing yet.",
                "On a copy: one name per unit, hours as numbers, dates as dates. Remove the repeated claim and the blank row, after you check them. In Excel, Data > Clean Data helps.",
                "Ask for a column chart of hours by unit, with the axis from zero. Then compare each unit with the Control totals sheet.",
                "Write one line for each unit that does not match, for its supervisor. Change no hours yourself."],
         "hints": ["Five units, so five bars. More bars means a unit is still written two ways.", f"Look for days above {D.OT_MAX_DAY} hours, and for a row whose approval is not given yet."],
         "prompt": "FILL:OTREQ",
         "check": {"kind": "flag", "label": "Type Production's total hours after cleaning, before anyone confirms anything (for example: 12.5)", "answer": f"{D.OT_CLEAN_TOTALS['Production']:g}"},
         "answer": [("p", f"Six problems: unit names, hours as text, dates as text, a repeated claim, a blank row, two days above {D.OT_MAX_DAY} hours. After cleaning, Drilling, HSE and Supply Chain match. "
                          + " ".join(f"{u}: {g} {w}" for u, g, w in D.OT_GAPS))]},
        {"title": "Task 2.7 · Option A: requirements for the 2027 survey", "files": ["mutla-training-needs-brief-2027.docx"],
         "do": ["Read the brief: the decisions L&D must make, the rules and the lists.", "Write your own checklist request: the decisions first, then the information each needs, then one question for each. Attach the brief.",
                "Test every question: Which decision does it serve? Can a manager answer it in under a minute? Does it ask for anyone's personal data?", "Keep eight questions or fewer. Write your plan: question, type, choices, required."],
         "hints": ["Start from the five decisions in the brief. Which question does each one need?", "Constraints: at most 10 questions; choices wherever the brief gives a list; no names, IDs, ratings, salaries or health."],
         "prompt": "FILL:REQS",
         "check": {"kind": "note", "label": "Paste your question plan (question, type, choices)"},
         "answer": [("p", "Unit (8 choices), section, team size, the skill needed now (course list and Other), how many need it, the skill for two years, how to learn, the best quarter, and an optional comment with a no-names line. Nothing about one named person.")]},
        {"title": "Task 2.7 · Option B: requirements for your own unit", "files": [],
         "do": ["Pick your unit or department. Write three or four facts about it: who answers, how many, by when, what you must decide.", "Write your own checklist request: the decisions first, then the information, then one question for each.",
                "Test every question three ways (decision, under a minute, personal data). Keep eight or fewer."],
         "hints": ["What is the one decision this form must help your manager make?", "If a question could only be answered about one named person, delete it."],
         "prompt": f"You are an HR officer in [your unit] at {D.COMPANY}. [Who] will answer a short training needs form by [date]. Before writing any question, list the decisions we must make from the answers and the information each needs. Then suggest one question for each. Use only these facts: [three or four facts]. At most 8 questions; every question serves one decision; choices wherever there is a list; never ask for an employee's name, ID, rating, salary or health. A table: decision, information needed, question, type, required.",
         "check": {"kind": "note", "label": "Paste your question plan"},
         "answer": [("p", "Accept any plan where every question serves a decision, choices are used where a list exists, and nothing asks about one named person.")]},
        {"title": "Task 2.8 · Build your form with Copilot in Forms", "files": [],
         "do": ["Open forms.cloud.microsoft (or forms.office.com) and select New Form.", "In the Draft with Copilot box, write a request from your plan: the title, who answers, every question with its type and choices, which are required. Select Keep it.",
                "Check every question against your plan. Delete anything you did not ask for. Fix types and choices by hand.", "Settings: only people in your organization can respond. Preview it on your phone.",
                "Send the link to your partner. Answer each other's form twice, with made-up answers."],
         "hints": ["Copilot follows a list best: give it every question, its type and its choices.", "No Draft with Copilot? Ask Copilot Chat for your questions as a numbered list, each choice on its own line. Paste it into Word, save it, then use Quick import in Forms."],
         "prompt": "FILL:FORMQ",
         "check": {"kind": "note", "label": "How many questions does your form have, and did Copilot add any you deleted?"},
         "answer": [("p", "Every question from the plan and none that is not in it; numbers set as Number; the comment question optional with the no-names line; only people in the organization can respond; two or more test answers.")]},
        {"title": "Task 2.9 · Option A: clean, count and check the 2027 responses", "files": ["mutla-training-needs-responses-2027.xlsx"],
         "do": ["Open the file in Excel with Copilot, or attach it to Copilot Chat. Imagine the survey has just closed.", "Ask for the rows that should not be counted and the skills written in more than one way. Change nothing yet.",
                "Count again, cleaned. Write the top three skills with the number of answers and of people, and the answers by unit against the Invited sheet.",
                "Write five lines of findings for the Head of L&D, starting with the DRAFT line. Leave out every personal comment. You use the findings in Task 2.10."],
         "hints": ["Compare the answers in each unit with the Invited sheet. One unit has more answers than managers.", "Filter the skill column and read every value. How many ways is Excel written?"],
         "prompt": "FILL:TNPROB",
         "templates": [("Count again, cleaned", "FILL:TNCLEAN")],
         "check": {"kind": "flag", "label": "After cleaning, how many people need the top skill? (digits only)", "answer": str(D.TN_SEATS[D.TN_TOP[0]])},
         "answer": [("p", f"Do not count row {D.TN_TEST_ID} (a test) or row {D.TN_FIRST_ID} (the first of two answers from one manager). Excel is written five ways. Cleaned: " + "; ".join(f"{x} {D.TN_COUNT[x]} answers, {D.TN_SEATS[x]} people" for x in D.TN_TOP) + f". {len(D.TN_VALID)} of {D.TN_INVITED_TOTAL} answered; {D.TN_LOW_UNIT} least. Row {D.TN_RED_ID}'s comment names a person: never copy it.")]},
        {"title": "Task 2.9 · Option B: your own form, with Copilot in Forms", "files": [],
         "do": ["Open your form from Task 2.8 and select Responses. You need three or more answers.", "Open Copilot in Forms and ask for the main training needs, with the number of answers behind each point.",
                "Select Open results in Excel and check two of Copilot's numbers against the answers.", "Write three lines of findings. Then try Option A: it has the real problems."],
         "hints": ["A summary is only as good as the numbers behind it. Check two.", "Few answers? Ask three neighbors to answer your form first."],
         "check": {"kind": "note", "label": "Which two numbers did you check, and did they match?"},
         "answer": [("p", "Accept any summary where two numbers were checked against the answers.")]},
        {"title": "Task 2.10 · Five slides: from a prompt, then from your findings", "files": [],
         "do": ["From a prompt: ask PowerPoint (or Copilot Chat) for five slides on Mutla's 2027 training needs, with no file. Circle every number it made up.",
                "From a document: paste your Task 2.9 findings into a Word file and save it. In PowerPoint, Copilot > Create a presentation from file. Or ask Copilot Chat for a five-slide outline with speaker notes.",
                "Check every number on every slide against your findings. No comment from a manager goes on a slide. Then delete the first deck."],
         "hints": ["Check the top three and the response rate on every slide where they appear.", "Ask for a title and three bullets per slide, plus two sentences of speaker notes."],
         "prompt": "Turn the attached findings into a five-slide outline for the Head of L&D's planning meeting, with speaker notes. Use only the attached findings. Keep every number exactly as written. No names and no comments from managers. Clear and practical. Five slides: a title and three bullets each, plus two sentences of speaker notes per slide.",
         "check": {"kind": "note", "label": "Paste your five slide titles"},
         "answer": [("p", "Every number on the slides matches the findings; no names or comments; the last slide gives the next step.")]},
        {"title": "Task 2.11 · Option A: fix the messy deck", "files": ["mutla-q3-hr-update-messy.pptx"],
         "do": ["Open the deck in PowerPoint. Read the About box on slide 1, then delete it.",
                "Ask Copilot for a fix list, slide by slide. Change nothing yet.",
                "Fix in rounds: merge the repeated slides, cut the long text, take out personal data, one font. Then Copilot: add speaker notes to all slides.",
                "Check every number against your checked figures and the policy brief. Where there is no source, write [to confirm]."],
         "hints": ["Two slides say the same thing with two different numbers.", "One slide shows names and salaries. A committee deck needs neither."],
         "prompt": "Review the attached deck slide by slide. For each slide, list what to fix: too much text, a repeated slide, a number with no source, personal data, and missing speaker notes. Do not change anything yet.",
         "check": {"kind": "flag", "label": "Type the number of Q3 training requests your fixed deck shows (digits only)", "answer": str(D.TRAIN_TRUE)},
         "answer": [("p", f"One training slide with {D.TRAIN_TRUE}; no names or salaries; the pilot at {D.ATT['pilot_drop']}% for the {D.ATT['pilot_unit']} only; owners and dates or [to confirm] on the next steps; notes on every slide.")]},
        {"title": "Task 2.11 · Option B: slides for your track's meeting", "files": [D.CASES[k]["file"] for k, _n in D.TRACKS],
         "do": ["Use your agenda and brief from Task 2.1, and your track's case file.", "Write your checklist request for four slides with speaker notes, then ask for one more slide that asks the meeting's open question.", "Check every date and number against the case file. Add the DRAFT line to the first slide."],
         "hints": ["Follow the agenda: one slide for each agenda item.", "Which question in your case is not decided yet? Give it its own slide, written as a question."],
         "prompt": f"You are an HR officer at {D.COMPANY}. I present at [which meeting] on [date]. Turn the agenda and brief above into four slides with speaker notes. Use only the agenda, the brief and the attached case file. Keep every date and number as written. Clear and short. A title and three bullets per slide, two sentences of speaker notes per slide. The first slide starts with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your slide titles"},
         "answer": [("p", "Slides that follow the agenda, the open question asked and not answered, every number from the case file. Job Evaluation: no grade.")]},
        {"title": "Task 2.12 · Redact the case note", "files": ["mutla-case-note-unredacted.docx"],
         "do": ["Remember the survey comment from Task 2.9? Names and health details hide inside sentences. Open the case note in Word. Save a copy with -redacted at the end of the name.", "Replace each name with a role. Remove the ID, the phone number, the salary and the medical reason.", "Read it once more: could anyone outside HR tell who this is?"],
         "hints": ["Six items: two names and four details.", "Look for a civil ID, a mobile number, a salary figure and the medical reason for the absence."],
         "prompt": "Read the attached note. List any detail that could still identify a person or is sensitive. Do not repeat the detail itself; give its paragraph number.",
         "check": {"kind": "note", "label": "List the six items you replaced, by type only (for example: civil ID). Never type the real values."},
         "answer": [("p", "Two names (to Employee A and Colleague B), the civil ID, the mobile number, the salary and the medical reason. Use the prompt only on the redacted copy.")]},
     ]},
 3: {"title": "Agents, then a whole HR process",
     "intro": "Step 1 schedules one of your requests. Step 2 uses a built-in agent. Steps 3 to 5 build and test your own agent. Steps 6 and 7 map an HR process. Step 8 improves your map, if there is time.",
     "lede_html": PROJECT_LEDE,
     "steps": [
        {"title": "Task 3.0 · Schedule one of your requests", "files": [],
         "do": ["Choose one request from your Prompt Bank that you want every week or every month, or use one of the requests below. Run it once in Copilot Chat.",
                "Hover over your request and select Schedule this prompt. Choose how often and the time. Save.",
                "Open Settings, then Scheduled prompts, and check that it is there."],
         "hints": ["Pick something you do every week: a summary, a reminder, a list of what is still waiting. Daily is often too much.",
                   "No Schedule this prompt option? You need the Microsoft 365 Copilot license. Test the request in Copilot Chat and write the schedule next to it in your Prompt Bank."],
         "prompt": "FILL:SCHED",
         "templates": [("A monthly request to schedule", "FILL:SCHED_M")],
         "check": {"kind": "note", "label": "Paste your request and when it runs"},
         "answer": [("p", "A tested request, weekly or monthly, with no pay, health or named-person details, listed under Scheduled prompts (or written in the Prompt Bank with its schedule).")]},
        {"title": "Task 3.1 · Use an agent Microsoft built", "files": [],
         "do": ["In Microsoft 365 Copilot, open Agents, then All agents. Find Prompt Coach under Built by Microsoft.", "Give it one request from your Prompt Bank, or the weak request below. Run the better request it suggests.", "If you have Researcher, ask it the research question below. Open two sources and check one fact in each."],
         "hints": ["Put the better request next to the five checklist parts. Which part did your first request miss?", "Researcher and Analyst need the Microsoft 365 Copilot license. No Researcher: ask Copilot Chat and ask for a source for each point.",
                   "Have the Microsoft 365 Copilot license? Hover over your better request and choose Schedule this prompt."],
         "prompt": "FILL:COACH_ASK",
         "templates": [("Researcher · a public HR question", "FILL:RESEARCH")],
         "check": {"kind": "note", "label": "Paste your better request"},
         "answer": [("p", "A request with all five checklist parts: context, task, data, constraints and format. With Researcher: two sources opened and one fact checked in each.")]},
        {"title": "Task 3.2 · Write and build the Onboarding Buddy", "files": ["mutla-onboarding-checklist-2026.docx", "mutla-it-setup-guide-2026.docx", "mutla-first-week-faq-2026.docx"],
         "do": [f"Write the instructions for the {D.BUDDY_NAME} with the five checklist parts: its three files, steps in order, ask head office or field site first, never pay or contract answers, and where it refers.",
                "In Microsoft 365 Copilot, choose Create agent, then the Configure tab. Add a name, a one-line description and your instructions. Upload the three files under Knowledge.",
                "Add three starter prompts. Ask one normal question in the test pane."],
         "hints": ["Constraints hold the rules that protect people: never, ask first, refer.", "Format: numbered steps when there are steps, then the file and the section."],
         "prompt": "FILL:BUDDY",
         "templates": [(f"Starter prompt {i}", q) for i, q in enumerate(D.BUDDY_STARTERS, 1)],
         "check": {"kind": "note", "label": "Paste the answer to your normal question"},
         "answer": [("p", "Five parts; only the three files; steps in order; ask head office or field site first; never salary, grade, allowance amounts or contract terms; refer to the right unit. Three knowledge files, three starter prompts, and a normal answer with the file and section.")]},
        {"title": "Task 3.3 · Test and fix your Onboarding Buddy", "files": [],
         "do": ["Ask the three test questions below. Write a test log: question, answer, pass or fix.", "Fix one instruction line that failed. Test again."],
         "hints": ["If it gives an allowance amount, your Constraints line is not clear enough.", "Change one line at a time, then ask the same question again."],
         "templates": [(f"Test · {a}", b) for a, b, _c, _d in D.BUDDY_TESTS],
         "check": {"kind": "note", "label": "Paste your three-line test log"},
         "answer": [("p", "Normal: the sign-in steps in order, IT setup guide section 2. Incomplete: it asks head office or field site first. Sensitive: no amount, and it refers to Compensation.")]},
        {"title": "Task 3.4 · Optional: the JD and Interview Generator", "files": ["mutla-hiring-guide-2026.docx", "mutla-jd-template-2026.docx"],
         "do": [f"Build the {D.HIRE_NAME}: it writes job postings and structured interview rubrics for hiring managers.",
                "Write its instructions with the five checklist parts, and bake in the hiring guide: Mutla's tone, the inclusive language rules and the competency framework. Knowledge: the hiring guide and the 2026 template.",
                "Run its three tests below and log them. Fix one line if a test fails."],
         "hints": ["The incomplete test leaves out the duties. What must your agent ask before it writes?", "Constraints: no age, gender, marital status or native speaker; no grade or salary; no questions about family, religion, health or nationality."],
         "prompt": "FILL:HIRE",
         "templates": [(f"Test · {a}", b) for a, b, _c, _d in D.HIRE_TESTS],
         "check": {"kind": "note", "label": "Paste your three-line test log"},
         "answer": [("p", "Normal: a posting in the template's order and a rubric with two questions per competency. Incomplete: it asks for the duties. Sensitive: it removes the age, gender and native-speaker words and refuses the marriage question, with a reason.")]},
        {"title": "Task 3.6 · Map the training request", "files": ["mutla-process-stories.docx", "mutla-process-map-template.docx"],
         "do": ["Read story 1 in the process stories file.", "Run the request from the prompt sheet to draft the step table.", "Check it against the story. Add any step or problem Copilot missed.", "Copy the final table into the map template."],
         "hints": ["Find the step that nobody owns.", "Count the places where the same information is printed, scanned or typed again."],
         "prompt": "FILL:MAP_FILE",
         "check": {"kind": "flag", "label": "Type how many working days the line manager usually takes to sign (for example: 1 to 2)", "answer": "4 to 6"},
         "answer": [("p", "About nine steps. The line manager takes 4 to 6 working days and L&D up to a week. Nobody chases late approvals.")]},
        {"title": "Task 3.7 · Map your own HR process", "files": ["mutla-process-stories.docx", "mutla-process-map-template.docx"],
         "do": ["Choose your track's story (2 to 5) or a process from your own work. For your own work, write it with roles only.", "Write your checklist request to turn it into a step table. Flag the problems; do not fix them.", "Check the table yourself. Mark every step where a person must decide. Save the map: Task 3.8 uses it."],
         "hints": ["Start where the request starts. Stop when the requester has the result.", "Your own work: write the story in five to eight sentences first, roles only, then ask Copilot to map it."],
         "prompt": "Turn the process story below into a step table. Story: [paste your story, roles only]. Do not improve the process. Only map it. Flag each step that has a delay, duplicated effort, unclear ownership or a repetitive step. Mark every step where a person must decide. A table: step, who, what happens, input, output, wait, problem, a person decides?",
         "check": {"kind": "note", "label": "Name your process and its biggest problem"},
         "answer": [("p", "A map from request to result, one owner per step, waits and problems marked, human decisions marked. No real names.")]},
        {"title": "Task 3.8 · Optional: improve your map", "files": ["mutla-workflow-card-template.docx"],
         "do": ["Mark each step on your map: Person, Copilot or Agent. Every approval and decision stays with a person.", "Remove at least two problems you flagged. Give every step one owner.", "Fill in the workflow card. Run the check request below, then check the card yourself."],
         "hints": ["Copilot: one-off drafting or summarizing. Agent: the same questions or the same kind of draft for many people. Person: approving, deciding, anything about one person's case.", "Start with the steps you marked as a problem. A step that types the same data again can often disappear."],
         "templates": [("Check my card", "FILL:CHECKCARD")],
         "check": {"kind": "note", "label": "Which two problems did you remove?"},
         "answer": [("p", "Every step marked Person, Copilot or Agent with one owner; every decision with a person; two problems removed.")]},
     ]},
}

# ------------------------------------------------------------------ portal survey words (Arabic; surveys.py builds the payloads)
SURVEY = {
 "program": "the CODED Professionals open workshop", "program_ar": "أساسيات الذكاء الاصطناعي للموارد البشرية",
 "client": "", "cohort": "AIFHR-Nov/Nov-26", "subtitle": {"en": "CODED Professionals", "ar": "CODED للمحترفين"},
 "folder": "a8f8146d-144f-47ed-9121-ef8e437f2f11", "name_prefix": "CODED ·", "note": "", "test_min": 10,
 "dept_label": ("Your company", "اسم الشركة"),
 "confidence_ar": ["أستطيع أن أشرح كيف يُنتج Copilot إجابته، وما الذي يمكنه رؤيته، ولماذا أتحقق منها.",
                   "أستطيع كتابة طلب يتضمن السياق والمهمة والبيانات والقيود والشكل، وتحسين مسودة ضعيفة بتعليمات متابعة.",
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
   ["الشكل (Format): أسلوب أكثر وداً", "السياق (Context): من سيقرأ الوصف الوظيفي", "القيود (Constraints): صفحة واحدة كحد أقصى", "البيانات (Data): معلومات الدور المعتمدة، مرفقة"]),
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
 "day_ar": {1: "أساسيات Copilot لمستندات الموارد البشرية والتواصل", 2: "الاجتماعات والتقارير والعروض التقديمية", 3: "وكلاء الموارد البشرية ومسارات العمل ومقدمة في Power Automate"},
 "relevance": ("The content was high quality and relevant to my HR work.", "كان المحتوى عالي الجودة وذا صلة بعملي في الموارد البشرية."),
 "hands_on": ("The hands-on parts, such as the job descriptions, the announcements, the HR tracker, the process map and the HR agent, helped me apply what I learned.",
              "ساعدتني الأجزاء التطبيقية، مثل الأوصاف الوظيفية والإعلانات وجدول الموارد البشرية وخريطة العملية ووكيل الموارد البشرية، على تطبيق ما تعلّمته."),
 "materials": ("The workshop website, the cheat sheet, the safe-use card and the take-home guide were clear and useful.",
               "كانت مواد ورشة العمل (الموقع وورقة المراجعة السريعة وبطاقة الاستخدام الآمن ودليل ما بعد ورشة العمل) واضحةً ومفيدة."),
 "logistics": ("The venue, the daily timing and access to Microsoft Copilot worked well for me.", "كان المكان والتوقيت اليومي وإمكانية الوصول إلى Microsoft Copilot مناسباً لي."),
}

# The kit's own slide CSS: the "where your chat goes" animation on Day 1 (build_deck.trainslide)
EXTRA_CSS = """
.wtc-slide .wtc-lede{max-width:1180px;margin:2px 0 8px}
.wtc{display:grid;gap:10px;margin:0 0 8px;width:100%;max-width:1320px;align-self:stretch;align-content:start;flex:0 0 auto;box-sizing:border-box}
.wtc-lane,.wtc-track,.wtc-box{min-width:0;box-sizing:border-box}
.wtc-lane{border:1px solid rgba(255,255,255,.14);border-radius:16px;padding:12px 22px 10px;background:rgba(255,255,255,.035)}
.wtc-bad{border-color:rgba(255,138,138,.45)}.wtc-ok{border-color:rgba(127,224,168,.45)}
.wtc-tag{font-family:var(--cd-font-mono);font-size:15px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:6px}
.wtc-bad .wtc-tag{color:#FF8A8A}.wtc-ok .wtc-tag{color:#7FE0A8}
.wtc-track{position:relative;display:grid;grid-template-columns:1fr 90px 1fr 90px 1fr;align-items:center;padding-top:30px}
.wtc-ok .wtc-track{grid-template-columns:2.25fr 90px 1fr}
.wtc-box{position:relative;display:grid;grid-template-columns:1fr 90px 1fr;align-items:center;border:2px dashed rgba(127,224,168,.7);border-radius:14px;padding:8px 12px 22px}
.wtc-boxl{position:absolute;bottom:3px;left:14px;font-family:var(--cd-font-mono);font-size:12px;color:#7FE0A8}
.wtc-node{background:var(--cd-surf-2);border:1px solid rgba(255,255,255,.18);border-radius:12px;padding:8px 14px;text-align:center}
.wtc-node b{display:block;font-size:24px}.wtc-node span{display:block;font-size:17px;opacity:.8;margin-top:2px}
.wtc-bad .wtc-model{border-color:#FF8A8A;animation:wtcGlow 4s ease-in-out infinite}
.wtc-off{opacity:.45;border-style:dashed}
.wtc-line{height:3px;margin:0 8px;background:repeating-linear-gradient(90deg,rgba(255,255,255,.55) 0 10px,transparent 10px 18px);background-size:36px 3px;animation:wtcDash 1.2s linear infinite}
.wtc-cut{position:relative;background:repeating-linear-gradient(90deg,rgba(255,138,138,.5) 0 10px,transparent 10px 18px);animation:none}
.wtc-cut i{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-style:normal;font-weight:800;font-size:30px;color:#FF8A8A;line-height:1}
.wtc-pkt{position:absolute;top:14px;left:0;transform:translate(-50%,-50%);padding:5px 12px;border-radius:999px;font-size:16px;font-weight:700;white-space:nowrap;pointer-events:none}
.wtc-go{background:#FF8A8A;color:#2a0b0b;animation:wtcGo 5s ease-in-out infinite}
.wtc-there{background:#7FE0A8;color:#082a18;animation:wtcThere 5s ease-in-out infinite}
.wtc-back{background:#7FE0A8;color:#082a18;animation:wtcBack 5s ease-in-out infinite}
.wtc-cap{margin:8px 0 2px;font-size:19px;opacity:.92}
@keyframes wtcDash{to{background-position:36px 0}}
@keyframes wtcGlow{0%,60%{box-shadow:none}80%{box-shadow:0 0 0 4px rgba(255,138,138,.35)}100%{box-shadow:none}}
@keyframes wtcGo{0%{left:16%;opacity:0}8%{opacity:1}40%{left:50%}55%{left:50%}85%{left:84%;opacity:1}100%{left:84%;opacity:0}}
@keyframes wtcThere{0%{left:12%;opacity:0}8%{opacity:1}42%{left:44%;opacity:1}50%{left:44%;opacity:0}100%{left:44%;opacity:0}}
@keyframes wtcBack{0%,50%{left:44%;opacity:0}58%{opacity:1}92%{left:12%;opacity:1}100%{left:12%;opacity:0}}
@media (prefers-reduced-motion:reduce){.wtc *{animation:none!important}.wtc-pkt{display:none}}
.aon-slide .aon-lede{max-width:1180px;margin:2px 0 8px}
.aon{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;width:100%;max-width:1180px;margin:0 0 8px;box-sizing:border-box}
.aon-card{all:unset;box-sizing:border-box;cursor:pointer;display:flex;flex-direction:column;gap:8px;min-height:150px;padding:12px 16px;border:1px solid rgba(255,255,255,.16);border-radius:14px;background:rgba(255,255,255,.04);color:inherit;font:inherit;text-align:left}
.aon-card:hover{border-color:rgba(255,255,255,.32)}
.aon-card:focus-visible{outline:2px solid var(--cd-accent);outline-offset:2px}
.aon-n{font-family:var(--cd-font-mono);font-size:13px;opacity:.6}
.aon-task{font-size:19px;line-height:1.3}
.aon-ans{margin-top:auto;visibility:hidden;padding-top:8px;border-top:1px solid rgba(255,255,255,.14)}
.aon-ans b{display:block;font-family:var(--cd-font-mono);font-size:13px;letter-spacing:.06em;text-transform:uppercase}
.aon-ans span{display:block;font-size:15px;line-height:1.3;opacity:.9;margin-top:2px}
.aon-card.aon-open .aon-ans{visibility:visible}
.aon-card.aon-open.aon-auto{border-color:rgba(127,224,168,.6)}.aon-auto .aon-ans b{color:#7FE0A8}
.aon-card.aon-open.aon-person{border-color:rgba(245,194,107,.6)}.aon-person .aon-ans b{color:#F5C26B}
.aon-card.aon-open.aon-both{border-color:rgba(127,224,168,.6)}.aon-both .aon-ans b{color:#7FE0A8}
.aon-card.aon-open.aon-chat{border-color:rgba(160,180,255,.6)}.aon-chat .aon-ans b{color:#A9B9FF}
.pa-vid{display:grid;grid-template-columns:auto minmax(280px,440px);justify-content:start;gap:24px;align-items:start;width:100%;max-width:1320px;margin:4px 0 8px;box-sizing:border-box}
.pa-vid-play{display:flex;flex-direction:column;align-items:flex-start;gap:6px;min-width:0}
.pa-vid-play video{display:block;height:min(50vh,470px);width:auto;max-width:100%;aspect-ratio:16/9;background:#000;border:1px solid rgba(255,255,255,.18);border-radius:14px;object-fit:contain}
.pa-vid-play small{font-family:var(--cd-font-mono);font-size:14px;opacity:.75}
.pa-vid-parts{list-style:none;margin:0;padding:0;display:grid;gap:8px;min-width:0}
.pa-vid-parts li{border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:7px 14px;background:rgba(255,255,255,.035)}
.pa-vid-parts b{display:block;font-family:var(--cd-font-mono);font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--cd-accent)}
.pa-vid-parts span{display:block;font-size:17px;line-height:1.3;margin-top:2px}
.pa-vid-parts .pa-vid-person{border-color:rgba(127,224,168,.45)}
.pa-vid-parts .pa-vid-person b{color:#7FE0A8}
"""
# The recorded Power Automate demos on Day 3 (build_deck.vidslide): the video source works on the site (/file), and from a folder copy
# (public/ or public/staff/); Space or K plays and pauses a focused video instead of changing the slide; a video pauses when its slide leaves.
EXTRA_JS = r"""
(function () {
  var vids = Array.prototype.slice.call(document.querySelectorAll('video[data-pa-src]'));
  if (!vids.length) return;
  var base = location.protocol === 'file:' ? (/\/staff\/[^\/]*$/.test(location.pathname) ? '../' : '') : '/';
  vids.forEach(function (v) { v.src = base + v.getAttribute('data-pa-src') + '#t=1'; });   // #t=1: the title card shows before play
  addEventListener('keydown', function (ev) {
    var t = ev.target;
    if (t && t.tagName === 'VIDEO' && (ev.key === ' ' || ev.key === 'k' || ev.key === 'K')) {
      ev.preventDefault(); ev.stopImmediatePropagation();
      if (t.paused) { var pr = t.play(); if (pr && pr.catch) pr.catch(function () {}); } else { t.pause(); }
    }
  }, true);
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (x) { if (!x.isIntersecting && !x.target.paused) x.target.pause(); }); });
    vids.forEach(function (v) { io.observe(v); });
  }
})();
// "Automate it or not?" (Day 3, build_deck.aonslide): a click on a card shows or hides its answer
(function () {
  document.addEventListener('click', function (ev) {
    var c = ev.target && ev.target.closest ? ev.target.closest('.aon-card') : null;
    if (!c) return;
    var open = c.classList.toggle('aon-open');
    c.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
"""
