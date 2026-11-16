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
               ("09:20-09:30", "Opener: one job description, two requests", "The same role, a one-line request and a full one, live"),
               ("09:30-10:30", "Block 1 · How generative AI and Copilot work", "What AI is, where LLMs fit, next-word prediction, what Copilot can see, what stays with people · Task 1.1"),
               ("10:30-10:45", "Break", ""),
               ("10:45-11:35", "Block 2 · Writing a clear prompt", "The prompt checklist: five parts · Task 1.2"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:20", "Block 3 · Draft, fix and check in Word", "Follow-up instructions and the source of every line · Tasks 1.3 and 1.4"),
               ("13:20-13:35", "Break", ""),
               ("13:35-14:40", "Block 4 · From policy to people: Word, then Outlook", "A policy summary, then one message for three readers · Tasks 1.5 and 1.6"),
               ("14:40-15:00", "Prompt Bank and wrap", "Save two requests, and where Copilot sits")],
    "outcomes": ["Explain why Copilot can write a <b>confident sentence that is wrong</b>, what it can see, and which HR decisions stay with people.",
                 "Write a request with the <b>prompt checklist</b>: context, task, data, constraints and format.",
                 "Improve a weak draft with <b>follow-up instructions</b>, and ask for the source of every line.",
                 "Draft HR documents in Word and messages in Outlook, and <b>change the tone</b> for each reader without changing the facts."]},
2: {"title": "Meetings, Reporting and Presentations", "claim": "Safe data, checked figures and clear slides.",
    "sub": "Protecting employee data, meetings and follow-ups, Excel figures you can check, summaries in Word, and decks in PowerPoint.",
    "brief": "Day 2 starts with the most important habit: what may go into a prompt, and how to redact what may not. Then you prepare a meeting, recap it into actions and follow it up in Outlook. In Excel you check a training count against a control total, then choose payroll or a messy overtime export to clean and chart. In Word you write a summary for management, then rewrite or summarize a document of your choice. In PowerPoint you build slides from a prompt and from a document, then fix a messy deck or build your own meeting's slides, and check every number on every slide.",
    "artifact": "A redacted case note, a meeting pack and recap, a training count, a payroll or overtime check, a summary, and two decks",
    "blocks": [("09:00-09:10", "Callback quiz", "Three questions on Day 1, and the old way and the AI way"),
               ("09:10-09:45", "Block 1 · Protecting employee data", "Green, amber, red; redact, then ask · Task 2.1"),
               ("09:45-10:45", "Block 2 · Before and after the meeting", "Agenda, brief, discussion points; notes into actions · Tasks 2.2 and 2.3"),
               ("10:45-11:00", "Break", ""),
               ("11:00-11:35", "Block 3 · Follow-ups and reminders in Outlook", "Same owners, same dates · Tasks 2.4 and 2.5"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:00", "Block 4 · Excel: figures you can check", "A control total, a chart, payroll or cleaning data · Tasks 2.6 and 2.7"),
               ("13:00-13:35", "Block 5 · Word: a summary for management", "Draft, rewrite, summarize · Tasks 2.8 and 2.9"),
               ("13:35-13:50", "Break", ""),
               ("13:50-14:50", "Block 6 · PowerPoint: from document to deck", "From a prompt, from a document, fix a messy deck · Tasks 2.10 and 2.11"),
               ("14:50-15:00", "Which app for which job, and wrap", "Word, Outlook, Teams, Excel, PowerPoint")],
    "outcomes": ["Sort any HR task as <b>green, amber or red</b>, and redact a note before Copilot sees it.",
                 "Prepare a meeting, recap it into <b>actions, owners and deadlines</b>, and follow it up in Outlook.",
                 "Check Excel figures against a <b>control total</b> or a list of approved changes.",
                 "Turn checked facts into a <b>Word summary</b> and a <b>PowerPoint deck</b>, and check every number on every slide."]},
3: {"title": "HR Agents, Workflows and an Introduction to Power Automate", "claim": "Build it, test it, then look at the whole process.",
    "sub": "Build and test two HR agents in Agent Builder, watch a Power Automate flow run from form to email, and map an HR process from request to result.",
    "brief": "Day 3 turns good requests into tools other people can use. You write an agent's instructions with the prompt checklist, build it in Agent Builder with five policy files, and test it with a normal, an incomplete and a sensitive question. Then you build a second agent of your choice. The trainer shows a Power Automate flow, so you can see when a flow is the right tool. After lunch you map a whole HR process: every step, every owner, every wait and every human decision. If there is time, you improve your map and mark the steps that Copilot or an agent can take.",
    "artifact": "Two tested HR agents and a map of one HR process",
    "blocks": [("09:00-09:10", "Callback quiz", "Three questions on Day 2"),
               ("09:10-10:05", "Block 1 · Build an HR agent", "Instructions, knowledge, starter prompts · Tasks 3.1 and 3.2"),
               ("10:05-10:45", "Block 2 · Test, fix and build a second agent", "Normal, incomplete, sensitive; your choice of agent · Tasks 3.3 and 3.4"),
               ("10:45-11:00", "Break", ""),
               ("11:00-11:35", "Block 3 · Power Automate: a trainer demo", "Trigger, actions, a condition, a person who approves"),
               ("11:35-12:15", "Lunch and Dhuhr prayer", ""),
               ("12:15-13:35", "Block 4 · From one task to a workflow", "Delays, duplicates, owners, human decisions · Tasks 3.6 and 3.7, Task 3.8 if time allows"),
               ("13:35-13:50", "Break", ""),
               ("13:50-14:05", "Copilot, agent or flow?", "The tools side by side, and a card sort"),
               ("14:05-14:20", "One-minute share-outs", "One agent or one map"),
               ("14:20-14:40", "Post-MAP test, then the final survey", "Two QR codes"),
               ("14:40-15:00", "Close and certificates", "The habit, one last time")],
    "outcomes": ["Write an agent's instructions with the <b>prompt checklist</b>, and build it in Agent Builder with approved files.",
                 "Test an agent with a <b>normal, an incomplete and a sensitive</b> question, and fix one line at a time.",
                 "Explain what a <b>Power Automate flow</b> does, and when an agent or Copilot cannot do the job.",
                 "Map an HR process from request to result, and mark the <b>delays, duplicates, owners and human decisions</b>."]},
}

SEGMENTS = {
 1: [("09:30-10:30", "Block 1 · How generative AI and Copilot work", [("09:30", 3, "Who used AI this week?"), ("09:33", 5, "What AI is; AI you already use"), ("09:38", 5, "Where LLMs fit; what LLM means"), ("09:43", 2, "Story: the 30-day answer"), ("09:45", 10, "Next-word prediction and hallucination"), ("09:55", 6, "What Copilot can see; your label"), ("10:01", 4, "Demo 1.1"), ("10:05", 10, "Task 1.1"), ("10:15", 3, "Debrief"), ("10:18", 8, "What stays with people; Demo 1.1b card sort"), ("10:26", 2, "Quick check"), ("10:28", 2, "Practice files only today")]),
     ("10:45-11:35", "Block 2 · Writing a clear prompt", [("10:45", 3, "Story: the one-line reminder"), ("10:48", 4, "Brief a new colleague"), ("10:52", 12, "The prompt checklist"), ("11:04", 4, "Constraints"), ("11:08", 6, "Demo 1.2"), ("11:14", 2, "Quick check"), ("11:16", 14, "Task 1.2"), ("11:30", 5, "Debrief")]),
     ("12:15-13:20", "Block 3 · Draft, fix and check in Word", [("12:15", 3, "Story: the team of six"), ("12:18", 5, "Follow-up instructions"), ("12:23", 5, "Demo 1.3"), ("12:28", 5, "Source trace, three failures"), ("12:33", 4, "Demo 1.3b"), ("12:37", 22, "Task 1.3"), ("12:59", 15, "Task 1.4"), ("13:14", 6, "Debrief")]),
     ("13:35-14:40", "Block 4 · From policy to people", [("13:35", 3, "Story: version 4 arrives"), ("13:38", 5, "Summaries you can check"), ("13:43", 5, "Demo 1.5"), ("13:48", 15, "Task 1.5"), ("14:03", 4, "The tone dial"), ("14:07", 5, "Demo 1.6"), ("14:12", 17, "Task 1.6"), ("14:29", 2, "Quick check"), ("14:31", 9, "Debrief")])],
 2: [("09:10-09:45", "Block 1 · Protecting employee data", [("09:10", 3, "Story: the note with a civil ID"), ("09:13", 5, "Green, amber, red"), ("09:18", 8, "Demo 2.1 card sort"), ("09:26", 5, "Demo 2.1b: redact, then ask"), ("09:31", 11, "Task 2.1"), ("09:42", 3, "Debrief")]),
     ("09:45-10:45", "Block 2 · Before and after the meeting", [("09:45", 3, "Story: the meeting with no actions"), ("09:48", 6, "Before, during, after; what Teams needs"), ("09:54", 6, "Demo 2.2"), ("10:00", 15, "Task 2.2"), ("10:15", 5, "Demo 2.3"), ("10:20", 2, "Quick check"), ("10:22", 15, "Task 2.3"), ("10:37", 8, "Debrief")]),
     ("11:00-11:35", "Block 3 · Follow-ups and reminders", [("11:00", 3, "Story: the deadline nobody chased"), ("11:03", 5, "Demo 2.4"), ("11:08", 12, "Task 2.4"), ("11:20", 10, "Task 2.5"), ("11:30", 5, "Debrief")]),
     ("12:15-13:00", "Block 4 · Excel", [("12:15", 3, "Story: 412 or 398"), ("12:18", 6, "Ask, see the rows, check"), ("12:24", 6, "Demo 2.6"), ("12:30", 12, "Task 2.6"), ("12:42", 12, "Task 2.7"), ("12:54", 6, "Debrief")]),
     ("13:00-13:35", "Block 5 · Word summaries", [("13:00", 3, "A management summary"), ("13:03", 4, "Demo 2.8"), ("13:07", 12, "Task 2.8"), ("13:19", 10, "Task 2.9"), ("13:29", 6, "Quick check and debrief")]),
     ("13:50-14:50", "Block 6 · PowerPoint", [("13:50", 3, "Story: the deck for Sunday"), ("13:53", 5, "What Copilot does in PowerPoint"), ("13:58", 6, "Demo 2.10"), ("14:04", 14, "Task 2.10"), ("14:18", 6, "Demo 2.11"), ("14:24", 18, "Task 2.11"), ("14:42", 3, "Quick check"), ("14:45", 5, "Debrief")])],
 3: [("09:10-10:05", "Block 1 · Build an HR agent", [("09:10", 3, "Story: the same 20 questions"), ("09:13", 6, "Copilot Chat or an agent"), ("09:19", 5, "The parts of an agent"), ("09:24", 8, "Demo 3.1"), ("09:32", 12, "Task 3.1"), ("09:44", 15, "Task 3.2"), ("09:59", 6, "Debrief")]),
     ("10:05-10:45", "Block 2 · Test, fix, build again", [("10:05", 5, "Demo 3.3"), ("10:10", 12, "Task 3.3"), ("10:22", 18, "Task 3.4"), ("10:40", 5, "Debrief")]),
     ("11:00-11:35", "Block 3 · Power Automate demo", [("11:00", 3, "Story: 30 requests a week"), ("11:03", 6, "Trigger, action, condition"), ("11:09", 15, "Demo 3.5"), ("11:24", 5, "What a flow needs"), ("11:29", 4, "Copilot, agent, flow"), ("11:33", 2, "Quick check")]),
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
SLIDES = {1: 69, 2: 55, 3: 46}

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
DAYS[2].update({"cat": "Meetings, reporting, presentations", "icon": "mail", "tag": "safe data · Outlook · Excel · Word · PowerPoint",
                "bullets": ["Green, amber, red, and redact before you ask", "Meetings, follow-ups and checked figures", "A Word summary and decks in PowerPoint"]})
DAYS[3].update({"cat": "Agents, workflows, Power Automate", "icon": "flask", "tag": "Agent Builder · Power Automate demo · process maps",
                "bullets": ["Build and test two HR agents", "Watch a Power Automate flow, and know when to use one", "Map an HR process from request to result"]})
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
                     "Day 3: open Agent Builder (Create agent) once before the day starts. If it is missing, use the fallback in the runbook.",
                     "Day 3: check that the Power Automate demo video plays with sound on the presenting laptop. Until the video is recorded, present the six steps on the slide.",
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
    "Tables of four, by unit track where possible, facing the screen. Pairs sit side by side for Tasks 1.1, 2.6, 2.7 and 3.6.",
    "Wi-Fi name and password on the board before 08:45.",
    "Day 1, 09:00: every laptop opens Copilot Chat and is signed in. The pre-MAP QR at 09:10 is also the pre-flight.",
    "Everything is digital: the safe-use card and the cheat sheet are on the workshop site. Nothing is printed."])]),
 ("failplan", "If something fails", "Plan A, B, C", [("table", [["What fails", "Plan B", "Plan C"],
    ["Copilot is slow or busy", "Wait one minute, then send the request again.", "Show the backup result on your own screen."],
    ["A daily limit is reached", "Pair with a neighbor.", "Continue from the backup result."],
    ["No Copilot in Word, Excel or PowerPoint", "Use Copilot Chat with the file attached.", "Trainer demo only."],
    ["No Agent Builder", "Save the instructions as a request in Copilot Chat with the five policy files.", "Pair with a neighbor who has it."],
    ["No internet", "Phone hotspot.", "The files on the USB stick, the backup results and the decks work offline."]])]),
 ("project", "Workflow block", "Day 3, 12:15", [("ul", ["Tasks 3.6 and 3.7 map a process as it runs today. Task 3.8 improves the map, only if the block is on time.",
    "Running late: skip Task 3.8 and its slide, give the debrief, and go to the comparison after the break.",
    "Task 3.8 marks each step Person, Copilot or Agent. Flows stay in the trainer demo.",
    "Walk the room during Task 3.7 and ask one question per person: where does it wait, and who decides?"])]),
 ("pa", "Power Automate demo", "Day 3, 11:09", [("ul", ["Trainer demo only: participants do not build flows.",
    "The demo is a recorded video (a placeholder until it is recorded). Test that it plays with sound before 09:00. The six steps on the slide are the backup.",
    "Say it in the room: a flow needs a Microsoft 365 account that includes Power Automate, and the company's IT approval. Approvals use the Approvals connector; the first approval in a new environment sets up a database and can take a few minutes.",
    "Keep every approval with a person. The flow only moves the request."])]),
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
 2: {"title": "Day 2, step by step, with hints", "intro": "One step for each task of Day 2, and one for each option where a task lets you choose. Download the files under the step that uses them. Write your own requests first; open a hint only when you are stuck. Your done marks stay in this browser.",
     "steps": [
        {"title": "Task 2.1 · Redact the case note", "files": ["mutla-case-note-unredacted.docx"],
         "do": ["Open the case note in Word. Save a copy with -redacted at the end of the name.", "Replace each name with a role. Remove the ID, the phone number, the salary and the medical reason.", "Read it once more: could anyone outside HR tell who this is?"],
         "hints": ["Six items: two names and four details.", "Look for a civil ID, a mobile number, a salary figure and the medical reason for the absence."],
         "prompt": "Read the attached note. List any detail that could still identify a person or is sensitive. Do not repeat the detail itself; give its paragraph number.",
         "check": {"kind": "note", "label": "List the six items you replaced, by type only (for example: civil ID). Never type the real values."},
         "answer": [("p", "Two names (to Employee A and Colleague B), the civil ID, the mobile number, the salary and the medical reason. Use the prompt only on the redacted copy.")]},
        {"title": "Task 2.2 · Prepare your track's meeting", "files": [D.CASES[k]["file"] for k, _n in D.TRACKS],
         "do": ["Open your track's case file. Find the meeting in it.", "Write your checklist request for an agenda, a background brief and three discussion points. Attach the case file.", "Check: an owner for every item, minutes that add up, every fact in the case file."],
         "hints": ["The case file says who meets, and about what.", "Turn the open question in the case into a discussion point. Constraints: only the case file; an owner and minutes for each item."],
         "prompt": f"You are an HR officer at {D.COMPANY}. I meet [who] for 30 minutes about [topic]. Prepare an agenda, a one-paragraph background brief and three discussion points. Use only the attached case file. Give each agenda item an owner and minutes that add up to 30. Turn each open question into a discussion point. Short and practical. An agenda table (item, owner, minutes), then the brief, then the discussion points. Start with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your request here"},
         "answer": [("p", "Accept an agenda with owners and minutes, a brief from the case facts only, and the case's open question as a discussion point.")]},
        {"title": "Task 2.3 · Recap the staffing meeting", "files": ["mutla-meeting-transcript-staffing.docx"],
         "do": ["Attach the transcript to a new chat.", "Write your checklist request for a recap: decisions, then action, owner and deadline, then open questions.", "Check each owner and deadline against the transcript. Delete anything nobody agreed."],
         "hints": ["Look for the lines where a person says \"I will\" and gives a day.", "One question in the meeting was not decided. It goes under open questions, not decisions."],
         "prompt": "FILL:RECAP",
         "check": {"kind": "flag", "label": "Type the day and month of Khaled's deadline (for example: 1 June)", "answer": D.STAFF_ACTIONS[0][2].split(" ", 1)[1]},
         "answer": [("p", f"Khaled Al-Ajmi prepares the manpower request by {D.STAFF_ACTIONS[0][2]}. Open question: {D.STAFF_OPEN[0]}.")]},
        {"title": "Task 2.4 · Follow up, and remind Khaled", "files": ["mutla-meeting-transcript-staffing.docx"],
         "do": ["Use your recap from Task 2.3.", "Write your checklist request for a follow-up email to everyone at the meeting.", "Then ask for a polite reminder to Khaled, two days before his deadline.", "Check every owner and date against the transcript."],
         "hints": ["The reminder asks. It does not blame.", "Constraints: keep every owner and date exactly as in the recap. Ask for two emails, each with a subject line."],
         "prompt": f"From the recap above, write a follow-up email to everyone at the meeting with the action table. Then write a short reminder to Khaled about the manpower request, two days before its deadline. Keep every owner and date exactly as in the recap. No blame. Polite and short. Two emails, each with a subject line, each starting with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste the subject lines of your two emails"},
         "answer": [("p", "All four actions with owners and deadlines unchanged; a reminder that names the manpower request and its deadline, with no blame.")]},
        {"title": "Task 2.5 · Your track's message", "files": [D.CASES[k]["file"] for k, _n in D.TRACKS],
         "do": ["Open your track's case file again. Find who needs a message, and why.", "Write your checklist request for that message. Attach the case file.", "Check every date and number. No employee names in the message."],
         "hints": ["Who reads it, and what must they do after reading it?", "Data: the case file. Constraints: every date and number as written; promise nothing the case does not say."],
         "prompt": f"You are an HR officer at {D.COMPANY}. [Who] needs to know [what] before [date]. Write the message. Use only the attached case file. Keep every date and number as written; promise nothing the case does not say; no employee names. Polite and clear. A subject line and under 150 words, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your subject line and first sentence"},
         "answer": [("p", "Job Evaluation: the reply gives no grade and says only the committee decides. Other tracks: every date and number from the case file.")]},
        {"title": "Task 2.6 · Training requests: find the duplicates", "files": ["mutla-hr-trackers-q3-2026.xlsx"],
         "do": ["Attach the tracker. Ask Copilot for every request ID that appears more than once.", "Check in Excel: select the Request ID column, then Conditional Formatting, Highlight Cells Rules, Duplicate Values.", "Write the corrected total, and why it changed."],
         "hints": ["Compare the Training sheet's row count with the Control totals sheet.", "Each request ID should appear once. Count the IDs that appear twice."],
         "prompt": "The Training sheet total does not match the Control totals sheet. List every request ID that appears more than once, with its row numbers. Do not delete anything.",
         "check": {"kind": "flag", "label": "Type the corrected number of Q3 training requests (digits only)", "answer": str(D.TRAIN_TRUE)},
         "answer": [("p", f"{D.TRAIN_DUPES} request IDs appear twice. Without them, the count is {D.TRAIN_TRUE}, not {D.TRAIN_ROWS_EXPORT}.")]},
        {"title": "Task 2.7 · Option A: payroll, two months", "files": ["mutla-payroll-check-oct-nov-2026.xlsx"],
         "do": ["Attach the payroll file. It has employee codes and no names, so use your company's approved account.", "Ask Copilot to compare October with November, then to check the Movements sheet.", "Check each item yourself in Excel. Write one line for each item a person must confirm. Change no salary."],
         "hints": ["Comparing the two months shows only what changed. A person who should have left did not change.", "Check every line of the Movements sheet against the November sheet."],
         "prompt": "FILL:PAYREQ",
         "check": {"kind": "flag", "label": "Type the employee code of the leaver who is still paid (for example: EMP-1000)", "answer": D.PAY_ISSUES[1][0]},
         "answer": [("p", "EMP-3346: an increase with no movement behind it. EMP-2731: left on 31 October, still paid. EMP-5114: joined on 1 November, missing.")]},
        {"title": "Task 2.7 · Option B: clean, chart and check the overtime export", "files": ["mutla-overtime-export-oct-2026.xlsx"],
         "do": ["Attach the file to Copilot Chat, or open it in Excel with Copilot. Ask for every cleaning problem, with row numbers. Change nothing yet.",
                "On a copy: one name per unit, hours as numbers, dates as dates. Remove the repeated claim and the blank row, after you check them. In Excel, Data > Clean Data helps.",
                "Ask for a column chart of hours by unit, with the axis from zero. Then compare each unit with the Control totals sheet.",
                "Write one line for each unit that does not match, for its supervisor. Change no hours yourself."],
         "hints": ["Five units, so five bars. More bars means a unit is still written two ways.", f"Look for days above {D.OT_MAX_DAY} hours, and for a row whose approval is not given yet."],
         "prompt": "FILL:OTREQ",
         "check": {"kind": "flag", "label": "Type Production's total hours after cleaning, before anyone confirms anything (for example: 12.5)", "answer": f"{D.OT_CLEAN_TOTALS['Production']:g}"},
         "answer": [("p", f"Six problems: unit names, hours as text, dates as text, a repeated claim, a blank row, two days above {D.OT_MAX_DAY} hours. After cleaning, Drilling, HSE and Supply Chain match. "
                          + " ".join(f"{u}: {g} {w}" for u, g, w in D.OT_GAPS))]},
        {"title": "Task 2.8 · A management summary in Word", "files": [],
         "do": ["Use your results from Tasks 2.6 and 2.7: the corrected training count, and the payroll or overtime items to confirm.", "Write your checklist request for a half-page summary for the Head of HR: what you found, what you corrected, and what a person must still confirm.", "Check both figures by hand. It starts with the DRAFT line."],
         "hints": ["Say what the file showed, what is correct, and why.", "Constraints: no blame on a unit or a person; one next step."],
         "prompt": f"You are an HR analyst at {D.COMPANY}. The Head of HR reads this before the quarterly report and the November payroll. Write a half-page summary of two checks. Data: [the training count: in the file, correct, why]; [the payroll or overtime items to confirm, by employee code or unit]. Keep every number and code as written. No blame on a unit or a person. Add one next step. Neutral and short. A title, then three short paragraphs, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your summary's first line"},
         "answer": [("p", "The corrected training count and the figure in the file, the three payroll items with who confirms each, no blame, one next step.")]},
        {"title": "Task 2.9 · Option A: three lines for the HR team", "files": [],
         "do": ["Use your summary from Task 2.8.", "Write your checklist request: a three-line update for the HR team channel.", "Keep every number. Take out every employee code. Check the three lines against your summary."],
         "hints": ["Who reads a team channel? Leave out anything that points to one employee.", "Constraints: three lines; every number as written; no employee codes or names."],
         "prompt": "Turn the summary above into a three-line update for the HR team channel. Keep every number exactly as written. Leave out every employee code and name. Neutral and short. Three lines, no headings.",
         "check": {"kind": "note", "label": "Paste your three lines"},
         "answer": [("p", "Three lines, every number as in the summary, no employee codes or names, no blame.")]},
        {"title": "Task 2.9 · Option B: rewrite the overtime memo", "files": ["mutla-overtime-memo-draft.docx"],
         "do": ["Open the memo in Word. Read the approved rules at the end first.",
                "Select one paragraph at a time, then Copilot > Rewrite. Or attach the file to Copilot Chat and ask for the whole notice.",
                "Ask for a plain notice for staff: under 150 words, short sentences, the rules as bullets.",
                "Check every number against the approved rules. Where the memo is different, use the approved rule and tell the Superintendent."],
         "hints": ["Two numbers in the memo are not the same as the approved rules.", "Constraints: use the approved rules at the end of the file; keep every number as written there; add no new rule."],
         "prompt": f"You are a Personnel officer at {D.COMPANY}. The Production Superintendent wrote the attached memo for staff. Rewrite it as a plain notice for Production staff. Use only the approved overtime rules at the end of the file. Where the memo differs from the approved rules, use the approved rule and list the difference after the notice. Add no new rule. Plain English, short sentences. A subject line, under 150 words, the rules as bullets, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Name the two rules the memo gets wrong (the rule names only)"},
         "answer": [("p", f"The notice uses the approved rules: {D.OT_MAX_DAY} hours a day (the memo says 5) and claims within {D.OT_CLAIM_DAYS} working days after the month ends (the memo says 10 days).")]},
        {"title": "Task 2.9 · Option C: summarize the Q3 HR report", "files": ["mutla-hr-quarterly-report-q3-2026.docx"],
         "do": ["Open the report in Word and ask Copilot to summarize it, or attach it to Copilot Chat.",
                "Ask for five bullets for the HR Director, each with its section number, every number as written.",
                "Check three numbers by hand in the report. Did the summary keep the risks in section 8?"],
         "hints": ["A summary that has only good news has left something out.", "Constraints: five bullets; a section number on each; no new facts and no opinions."],
         "prompt": f"You are an HR analyst at {D.COMPANY}. The HR Director has one minute before the Management Committee. Summarize the attached Q3 HR report in five bullets. Use only the report. Give the section number for every bullet and keep every number as written. Include the main risk. Neutral and short. Five bullets, starting with: {D.DRAFT_LINE}",
         "check": {"kind": "flag", "label": "Type the number of vacancies filled in Q3 (digits only)", "answer": str(D.Q3["vac_filled"])},
         "answer": [("p", f"Five bullets with section numbers: headcount {D.Q3['hc_end']:,}; {D.Q3['vac_filled']} vacancies filled, time to fill {D.Q3['time_to_fill']} days against {D.Q3['time_target']}; {D.TRAIN_TRUE} training requests; the attendance pilot and the start date; and a risk from section 8.")]},
        {"title": "Task 2.10 · Five slides: from a prompt, then from your summary", "files": [],
         "do": ["From a prompt: ask PowerPoint (or Copilot Chat) for five slides on Q3 training requests and your Task 2.7 check, with no file. Circle every number it made up.",
                "From a document: save your Task 2.8 summary as a Word file. In PowerPoint, Copilot > Create a presentation from file. Or ask Copilot Chat for a five-slide outline with speaker notes.",
                "Check every number on every slide against your summary. Then delete the first deck."],
         "hints": ["Check the training count and the payroll items on every slide where they appear.", "Ask for a title and three bullets per slide, plus two sentences of speaker notes."],
         "prompt": "Turn the attached summary into a five-slide outline for the Head of HR's meeting, with speaker notes. Use only the attached summary. Keep every number exactly as written. Clear and practical. Five slides: a title and three bullets each, plus two sentences of speaker notes per slide.",
         "check": {"kind": "note", "label": "Paste your five slide titles"},
         "answer": [("p", "Every number on the slides matches the summary; the last slide gives the next step.")]},
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
         "do": ["Use your agenda and brief from Task 2.2, and your track's case file.", "Write your checklist request for four slides with speaker notes, then ask for one more slide that asks the meeting's open question.", "Check every date and number against the case file. Add the DRAFT line to the first slide."],
         "hints": ["Follow the agenda: one slide for each agenda item.", "Which question in your case is not decided yet? Give it its own slide, written as a question."],
         "prompt": f"You are an HR officer at {D.COMPANY}. I present at [which meeting] on [date]. Turn the agenda and brief above into four slides with speaker notes. Use only the agenda, the brief and the attached case file. Keep every date and number as written. Clear and short. A title and three bullets per slide, two sentences of speaker notes per slide. The first slide starts with: {D.DRAFT_LINE}",
         "check": {"kind": "note", "label": "Paste your slide titles"},
         "answer": [("p", "Slides that follow the agenda, the open question asked and not answered, every number from the case file. Job Evaluation: no grade.")]},
     ]},
 3: {"title": "Your agents, then a whole HR process",
     "intro": "Steps 1 to 4 are the agent tasks. Steps 5 and 6 map an HR process. Step 7 improves your map, if there is time.",
     "lede_html": PROJECT_LEDE,
     "steps": [
        {"title": "Task 3.1 · Write the agent's instructions", "files": ["mutla-leave-policy-2026.docx", "mutla-allowances-policy-v3.docx", "mutla-allowances-policy-v4.docx", "mutla-attendance-rules-2026.docx", "mutla-training-policy-2026.docx"],
         "do": [f"Write the instructions for {D.AGENT_NAME} with the five checklist parts.", "Say which files it may use, and the dates of the two allowances versions.", "Say what it must never answer, when it must ask first, and where it refers people."],
         "hints": ["Constraints hold the rules that protect people: never, ask first, refer.", "Data: version 3 applies until 31 December 2026; version 4 from 1 January 2027. Format: a short answer, then the policy name and section."],
         "prompt": "FILL:AGENT",
         "check": {"kind": "note", "label": "Paste your Constraints line"},
         "answer": [("p", "Five parts; only the five files; both allowances dates; ask first; never a named person's pay or data; refer to the right HR unit.")]},
        {"title": "Task 3.2 · Build it in Agent Builder", "files": ["mutla-leave-policy-2026.docx", "mutla-allowances-policy-v3.docx", "mutla-allowances-policy-v4.docx", "mutla-attendance-rules-2026.docx", "mutla-training-policy-2026.docx"],
         "do": ["In Microsoft 365 Copilot, choose Create agent, then the Configure tab.", "Add a name, a one-line description and your instructions. Upload the five policy files under Knowledge.", "Add three starter prompts. Ask one normal question in the test pane."],
         "hints": ["Starter prompts are questions staff would really ask.", "No section number in the answer? Check the Format line in your instructions."],
         "templates": [(f"Starter prompt {i}", q) for i, q in enumerate(D.AGENT_STARTERS, 1)],
         "check": {"kind": "note", "label": "Paste the answer to your normal question"},
         "answer": [("p", f"Five knowledge files, three starter prompts, and a normal answer with the policy name and section.")]},
        {"title": "Task 3.3 · Test and fix your agent", "files": [],
         "do": ["Ask the three test questions below. Write a test log: question, answer, pass or fix.", "Fix one instruction line that failed. Test again."],
         "hints": ["If it answers the salary question, your Constraints line is not clear enough.", "Change one line at a time, then ask the same question again."],
         "templates": [(f"Test · {a}", b) for a, b, _c, _d in D.AGENT_TESTS],
         "check": {"kind": "note", "label": "Paste your three-line test log"},
         "answer": [("p", "Normal: the rule and section 4. Incomplete: it asks for the grade, or gives both versions with dates. Sensitive: it declines and refers.")]},
        {"title": "Task 3.4 · A second agent: choose one", "files": ["mutla-jd-template-2026.docx", "mutla-job-evaluation-factors.docx", "mutla-onboarding-checklist-2026.docx"],
         "do": [f"Choose one: the {D.COACH_NAME} (it helps line managers draft job descriptions) or the {D.BUDDY_NAME} (it answers new joiners from the onboarding checklist).",
                "Write its instructions with the five checklist parts. Knowledge: the 2026 template and the evaluation factors, or the onboarding checklist.", "Run its three tests below and log them. Fix one line if a test fails."],
         "hints": ["The incomplete test leaves something out. What must your agent ask before it answers?", "Constraints: ask first when something is missing; add nothing; refer grades, salaries and allowances to the right unit."],
         "prompt": "FILL:COACH_BUDDY",
         "templates": [(f"Coach test · {a}", b) for a, b, _c, _d in D.COACH_TESTS] + [(f"Buddy test · {a}", b) for a, b, _c, _d in D.BUDDY_TESTS],
         "check": {"kind": "note", "label": "Which agent did you build? Paste your three-line test log"},
         "answer": [("p", "Coach: drafts from the given duties only, asks for duties when none are given, refers the grade question. Buddy: answers from the checklist, asks head office or field site, refers the allowance question.")]},
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
