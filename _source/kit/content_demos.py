# -*- coding: utf-8 -*-
"""Every demo and hands-on task of AI Fundamentals for HR: requests, expected results, backups and answer keys.
Numbers and names come from data.py, so the decks, prompt sheets, runbooks, backups and answer keys always agree.
Every demo runs live in the real tool. The slide says what to show, what to watch for and which files to use;
the speaker notes keep the click steps and the backup."""
import data as D
import content as C
from data import kwd

# ------------------------------------------------------------------ the sample files (names never change once built)
F = {
 "leave": "mutla-leave-policy-2026.docx", "answer": "mutla-copilot-leave-answer.docx", "case": "mutla-case-note-unredacted.docx",
 "oldjd": "mutla-jd-hr-officer-2019.docx", "tpl": "mutla-jd-template-2026.docx", "roles": "mutla-role-information-2026.docx",
 "catchjd": "mutla-catchup-jd-draft.docx", "bank": "mutla-prompt-bank-template.docx",
 "v3": "mutla-allowances-policy-v3.docx", "v4": "mutla-allowances-policy-v4.docx", "factors": "mutla-job-evaluation-factors.docx",
 "evidence": "mutla-je-evidence-notes.docx", "thread": "mutla-email-thread-attendance.docx", "transcript": "mutla-meeting-transcript-staffing.docx",
 "inv": "mutla-investigation-notes.docx", "trackers": "mutla-hr-trackers-q3-2026.xlsx", "brief": "mutla-policy-change-brief.docx",
 "attendance": "mutla-attendance-rules-2026.docx", "training": "mutla-training-policy-2026.docx", "catchbank": "mutla-catchup-prompt-bank.docx",
 "fresh": "mutla-capstone-fresh-input.docx", "letters": "mutla-experience-letter-requests.docx",
 "stories": "mutla-process-stories.docx", "maptpl": "mutla-process-map-template.docx",
 "card": "mutla-workflow-card-template.docx", "palog": "mutla-training-request-log.xlsx",
 "vid1": "power-automate-demo-1-training-request.mp4", "vid2": "power-automate-demo-2-weekly-vendor-brief.mp4", "vid3": "power-automate-demo-3-vendor-quotation.mp4",
 "payroll": "mutla-payroll-check-oct-nov-2026.xlsx", "onboard": "mutla-onboarding-checklist-2026.docx",
 "overtime": "mutla-overtime-export-oct-2026.xlsx", "otmemo": "mutla-overtime-memo-draft.docx",
 "q3report": "mutla-hr-quarterly-report-q3-2026.docx", "messydeck": "mutla-q3-hr-update-messy.pptx",
 "r360": "mutla-360-feedback-emp-4127.docx", "welcome": "mutla-welcome-letter-2019.docx",
 "tnbrief": "mutla-training-needs-brief-2027.docx", "tnresp": "mutla-training-needs-responses-2027.xlsx",
}
CASE_FILES = [D.CASES[k]["file"] for k, _n in D.TRACKS]
CAP_FILES = [D.CAPSTONE[k]["file"] for k, _n in D.TRACKS]
ALL_FILES = [F["leave"], F["answer"], F["case"], F["oldjd"], F["tpl"], F["roles"], F["catchjd"], F["bank"], F["letters"],
             F["r360"], F["welcome"], F["v3"], F["v4"], F["thread"], F["transcript"], F["trackers"], F["payroll"], F["overtime"], F["tnbrief"], F["tnresp"], F["brief"], F["otmemo"], F["q3report"], F["messydeck"]] + CASE_FILES + [F["stories"], F["maptpl"],
             F["attendance"], F["training"], F["factors"], F["onboard"], F["card"], F["palog"], F["vid1"], F["vid2"], F["vid3"], F["catchbank"]]
assert len(ALL_FILES) == len(set(ALL_FILES))

# What each file is for: what it is, who uses it at Mutla, and where it is used in the workshop. Lab steps and the "About this file" box use it.
FILE_ABOUT = {
 F["leave"]: ("Mutla's approved leave policy: annual, emergency, sick and Hajj leave, and carry-over.", "Every employee; Personnel answers questions from it.", "Day 1 demos, Task 1.1 and the Block 3 notebook; the HR assistant's knowledge on Day 3."),
 F["answer"]: ("An answer Copilot wrote to an employee's leave questions. Nobody has checked it yet.", "Personnel, before the answer is sent.", "Task 1.1: check it against the leave policy."),
 F["case"]: ("An Employee Relations case note about a phased return to work. It still has personal details in it.", "Employee Relations and Personnel.", "Task 2.12: remove the personal details before anything goes to Copilot."),
 F["oldjd"]: ("An old job description from 2019, in the old format.", "Job Evaluation, as background only.", "Background only: an example of the old style. Do not copy from it."),
 F["tpl"]: ("The approved 2026 job description template: the headings, in order, and the rules.", "Everyone who writes a job description.", "Demo 1.0 and Task 3.4."),
 F["roles"]: ("The approved duties for one role in each HR unit. The source for every job description.", "Job Evaluation and line managers.", "Demo 1.0."),
 F["catchjd"]: ("A job description Copilot drafted. It looks finished but has not been checked.", "Anyone who needs to check a draft.", "Extra practice: check it line by line against the role information."),
 F["bank"]: ("An empty Prompt Bank: four columns for the requests you want to keep.", "You, after the workshop.", "End of Day 1, and Task 3.1 (Prompt Coach)."),
 F["letters"]: ("Three experience letter requests, the HR system record for each person and the letter rules.", "Personnel and Administration.", "Extra practice: check each request against the HR system record."),
 F["v3"]: ("The allowances policy in force today, version 3.", "Compensation, and every employee who gets an allowance.", "The HR assistant's knowledge on Day 3."),
 F["v4"]: ("The new allowances policy, version 4, approved this year.", "Compensation, and every employee who gets an allowance.", "The HR assistant's knowledge on Day 3."),
 F["r360"]: (f"360 feedback for one Senior HR Officer ({D.R360_EMP}): a self-review and comments from the manager, three peers and two team members.", "The line manager and HR, before the review meeting.", "Task 1.6: summarize it in Word."),
 F["welcome"]: ("The welcome letter Personnel sent to new graduates in 2019. Long, formal and partly out of date.", "Personnel and Administration, for every new joiner.", "Task 1.7: rewrite it in Word."),
 F["thread"]: ("Thirty emails in which managers agreed the new attendance rules. Some early ideas were changed later.", "Personnel and Administration, before the staff announcement.", "Task 1.8."),
 F["transcript"]: ("The Teams transcript of a staffing meeting about the new Drilling Support section.", "The people at the meeting, and Manpower.", "Tasks 2.2 and 2.3: recap and follow up."),
 F["trackers"]: ("The Q3 HR trackers exported from the HR system: training requests, manpower and control totals.", "L&D and Manpower, before the quarterly report.", "Demo 2.5 and Task 2.5."),
 F["payroll"]: ("October and November payroll for one payroll group, and the list of approved changes for November.", "Compensation and Personnel, before the bank file is sent.", "Task 2.6, option A."),
 F["overtime"]: (f"The {D.OT_MONTH} overtime claims as the time and attendance system exported them, before anyone cleaned them, and the approved totals.", "Personnel and Administration checks it; Compensation pays from it.", "Task 2.6, option B: clean it, chart it, check it."),
 F["brief"]: ("A one-page brief on the new attendance rules for line managers, with the pilot result.", "Line managers and the Head of HR.", "Demos 2.10 and 2.11."),
 F["otmemo"]: ("A Production Superintendent's first draft of a memo to staff about overtime, and the approved overtime rules.", "Personnel checks it before it goes to staff.", "Extra practice: rewrite it in plain English for staff. The approved rules at the end win."),
 F["q3report"]: ("The HR quarterly report for July to September 2026: people, recruitment, attendance, training, pay and risks.", "The HR Director, then the Management Committee.", "Extra practice: summarize it in five bullets with section numbers."),
 F["tnbrief"]: ("The Head of L&D's brief for the 2027 training needs survey: the decisions L&D must make, the rules for the form, the units and the course list.", "Learning and Development, before the survey opens on " + D.TNS["open"] + ".", "Demos 2.7 and 2.8, Tasks 2.7 and 2.8: requirements first, then the form."),
 F["tnresp"]: (f"A practice export of the 2027 training needs survey, as Microsoft Forms gives it when the survey closes: {len(D.TN_EXPORT)} answers from line managers, and the list of managers invited.", "Learning and Development, before the 2027 training plan.", "Demo 2.9 and Task 2.9: clean, count and check the results. Your findings feed Task 2.10."),
 F["messydeck"]: ("A nine-slide Q3 HR update that someone made in a hurry: too much text, repeated slides, a wrong number and personal data.", "It was meant for the Management Committee.", "Task 2.11, option A: fix it."),
 F["stories"]: ("Five short stories of how HR work is done today, one for each HR unit.", "You, to practice mapping a process.", "Demo 3.6 and Tasks 3.6 and 3.7."),
 F["maptpl"]: ("An empty table for a process map: step, who, in, out, wait, problem.", "You, to map a process.", "Tasks 3.6 and 3.7."),
 F["card"]: ("An empty card for an improved workflow: trigger, inputs, steps, approvals, what you removed.", "You, to plan a better process.", "Task 3.8 (optional)."),
 F["palog"]: ("The training request log that the Power Automate flow fills in, one row per request.", "Learning and Development.", "Demo 3.5, the approval flow."),
 F["vid1"]: ("A recorded Power Automate demo with no sound (2:16): a training request goes from a form to an approval, a row in Excel and an email.", "Learning and Development and line managers.", "Demo 3.5. Watch it again after the workshop."),
 F["vid2"]: ("A recorded Power Automate demo with no sound (1:50): every Sunday, the week's training requests become a DRAFT vendor brief for L&D.", "Learning and Development.", "Demo 3.5b. Watch it again after the workshop."),
 F["vid3"]: ("A recorded Power Automate demo with no sound (1:42): a vendor quotation email is read, scored by AI and added to Excel as a row to review.", "Learning and Development.", "Demo 3.5c. Watch it again after the workshop."),
 F["attendance"]: ("The approved attendance rules: start times, core hours and permissions.", "Every employee; Personnel answers questions from it.", "The Block 3 notebook on Day 1; the HR assistant's knowledge on Day 3."),
 F["training"]: ("The training policy: how employees request and attend training.", "Learning and Development, line managers and employees.", "Day 1 Task 1.2 and the Block 3 notebook; the HR assistant's knowledge on Day 3."),
 F["factors"]: ("The five factors the Job Evaluation committee uses to compare jobs.", "Job Evaluation and Salary Scaling.", "Task 3.4: the Job Description Coach's knowledge."),
 F["onboard"]: ("The checklist for a new joiner's first day, first week and first month.", "Personnel and Administration, and every new joiner.", "Task 1.7 (the source for the welcome letter) and Task 3.4 (the Onboarding Buddy's knowledge)."),
 F["catchbank"]: ("Eight requests that were tested in class, ready to copy.", "Anyone who missed a task or wants a model.", "Catch-up file for every day."),
}
for _k, _n in D.TRACKS: FILE_ABOUT[D.CASES[_k]["file"]] = (f"The {_n} case: {D.CASES[_k]['title'].lower()}. The facts, the people, the meeting and the open question.", f"{_n}.", "Tasks 2.1, 2.4 and 2.11.")
assert set(FILE_ABOUT) == set(ALL_FILES), set(ALL_FILES) ^ set(FILE_ABOUT)
BOX_FILES = [F["case"], F["transcript"], F["trackers"], F["payroll"], F["overtime"], F["tnbrief"], F["tnresp"], F["otmemo"], F["q3report"], F["messydeck"],
             F["stories"], F["maptpl"], F["card"], F["palog"], F["catchbank"]] + CASE_FILES
def about_lines(f): w, who, use = FILE_ABOUT[f]; return [f"What it is: {w}", f"Who uses it at Mutla: {who}", f"In this workshop: {use}"]
def about(f): return f"{f}: {FILE_ABOUT[f][0]}"

# prompt sheet sections: sec -> (day, name)
BLOCK = {1: (1, "Opener"), 2: (1, "Block 1 · How Copilot works"), 3: (1, "Block 2 · A clear prompt"),
         4: (1, "Block 3 · Word: draft, fix, check"), 5: (1, "Block 4 · Word, then Outlook"),
         6: (2, "Block 1 · Prepare and recap"), 7: (2, "Block 2 · Outlook follow-ups"), 8: (2, "Block 3 · Excel: check figures"),
         9: (2, "Block 4 · Forms: training needs"), 10: (2, "Block 5 · PowerPoint"), 11: (2, "Block 6 · Protect employee data"),
         12: (3, "Block 1 · Built-in agents"), 13: (3, "Block 2 · Build your own agent"), 14: (3, "Block 3 · Power Automate: when to automate"),
         15: (3, "Block 4 · Map a workflow"), 16: (3, "Copilot, agent or flow?")}

DEMOS = {}
def demo(did, **kw):
    kw.setdefault("stretch", []); kw.setdefault("stretch_prompts", []); kw.setdefault("files", [])
    kw["card"] = ("Task " if kw.get("hands_on") else "Demo ") + kw["skill"]
    DEMOS[did] = kw
def tbl(head, rows): return ("table", [head] + [list(r) for r in rows])
def joined(parts): return " ".join(v for _k, v in parts)
SEVEN = ("Role", "Context", "Task", "Data", "Constraints", "Tone", "Output format")
def five(parts):
    """The five-part checklist: Role goes into Context; Tone and Output format become Format. The words do not change."""
    d = dict(parts); assert set(d) <= set(SEVEN), set(d) - set(SEVEN)
    out = [["Context", " ".join(x for x in (d.get("Role"), d.get("Context")) if x)]] if ("Role" in d or "Context" in d) else []
    out += [[k, d[k]] for k in ("Task", "Data", "Constraints") if k in d]
    fmt = " ".join(x for x in (d.get("Tone"), d.get("Output format")) if x)
    return out + ([["Format", fmt]] if fmt else [])
TRACK_LINE = "Pick your unit track: " + "; ".join(f"{n}" for _k, n in D.TRACKS) + "."

# ===================================================================== the requests (one place: demos, sheets, the catch-up bank)
R = D.ROLES["cmp"]
DL = D.DRAFT_LINE
JD_CMP = five([["Role", f"You are an HR officer at {D.COMPANY}."],
          ["Context", "It is for the 2026 job evaluation round. The Job Evaluation committee will read it."],
          ["Task", f"Draft the job description for the {R['title']}."],
          ["Data", f"Use the attached role information for the {R['title']} and the attached 2026 template."],
          ["Constraints", "Use only the attached files. Do not add duties, a team size or a grade. Leave the grade line blank. One page."],
          ["Tone", "Formal, neutral, plain English. Each duty starts with a verb."],
          ["Output format", f"The template's headings, in order. Start with the line: {DL}"]])
LEAVE_Q = [["Question", "How many days of unused annual leave can staff carry over to next year?"],
           ["Data and constraints", f"Answer only from the attached {F['leave']}. Give the section number. If the policy does not say, write: not in the policy."]]
CARRY = five([["Role", f"You are a Personnel officer at {D.COMPANY}."],
         ["Context", "The year is ending. Some employees do not know that unused leave over the limit is lost."],
         ["Task", "Write a short reminder email to all staff about carrying over annual leave."],
         ["Data", f"Use the attached {F['leave']}, section 4."],
         ["Constraints", "Use only section 4. Keep every number and date exactly as written. Name no employee and no balance. Under 120 words."],
         ["Tone", "Friendly and clear."],
         ["Output format", f"A subject line, then the email. Start with the line: {DL}"]])
FOLLOWUPS = [["Fix what is missing", "The role information has six duties. Your draft has five. Add the missing duty, word for word from the role information. Change nothing else."],
             ["Fix the shape", "Shorten it to one page. Keep every duty. Remove the introduction paragraph."],
             ["Show your guesses", "List every assumption you made that is not in the attached files. One line each."]]
TRACE = five([["Task", "Check the attached job description line by line."],
         ["Data", f"Use only the attached {F['roles']} and {F['tpl']}."],
         ["Constraints", "Do not fix anything. Only check."],
         ["Output format", "A table: the line of the draft, then the line of the role information it comes from, or NOT IN SOURCE."]])
LETTER_FLAG = ("Flag, do not fix", "Compare Ali Al-Harbi's request with his HR system record and the template rules in the attached file. "
               "List every point where the request differs from the record, or asks for something the rules do not allow. Do not change the letter. Only list the points.")
SUM_LEAVE = five([["Role", f"You are a Personnel officer at {D.COMPANY}."],
             ["Context", "New joiners ask the same leave questions in their first month."],
             ["Task", "Summarize the attached leave policy for new joiners."],
             ["Data", f"Use only the attached {F['leave']}."],
             ["Constraints", "Give the section number for every point. Keep every number exactly as written. If the policy does not say, do not guess."],
             ["Tone", "Plain and friendly."],
             ["Output format", f"Up to eight short bullets on one page. Start with the line: {DL}"]])
TONE = five([["Task", "Rewrite the reminder above for line managers. Then write a three-line version for senior leadership."],
        ["Constraints", "Keep every number and date exactly as written. Add no new rule."],
        ["Tone", "Line managers: practical, what they need to do. Senior leadership: short and factual."],
        ["Output format", f"Two emails, each with a subject line. Start each one with the line: {DL}"]])
THREAD = five([["Task", "Summarize the attached email thread: every decision, then the open questions."],
          ["Context", "I am writing the staff announcement and must not miss a decision."],
          ["Data", f"Use only {F['thread']}."],
          ["Constraints", "If a later message changed an earlier one, use the later decision and say so. Leave out personal notes that are not decisions."],
          ["Output format", "A table: decision, owner, date, message number. Then a list of open questions."]])
COMPARE = ("Compare", "Compare the two attached versions of the allowances policy. List every change, with its section number, in a table: section, version 3, version 4. "
                      "Quote the exact numbers. Do not summarize parts that did not change.")
LEAVE_RESULT = f"Up to {D.LEAVE['carry']} days of unused annual leave may be carried over. They must be used by {D.LEAVE['carry_by']} (section 4)."
JD_RESULT_LINES = [DL, f"<b>Job title:</b> {R['title']} · <b>Unit:</b> {R['unit']} · <b>Reports to:</b> {R['reports']}",
                   f"<b>Purpose:</b> {R['purpose']}", "<b>Key duties:</b> " + "; ".join(R["duties"][:3]) + " …", "<b>Grade:</b> blank, for the Job Evaluation committee"]
A = D.ALLOW
ALI = D.LETTER_ALI

# ===================================================================== DAY 1 · Copilot Foundations for HR Documents and Communication
demo("d10", day=1, skill="1.0", sec=2, title="One job description, two requests", tool="Copilot Chat", files=[F["tpl"], F["roles"]],
 setup=["[T] Open Copilot Chat in two browser tabs, signed in with the training account.", "[T] Tab 1: paste the one-line request, with no file.",
        f"[T] Tab 2: attach {F['tpl']} and {F['roles']}, then paste the checklist request.", "[T] Put the two answers side by side. Read the duties and the grade line aloud."],
 prompts=[("One line", f"Write a job description for a {R['title'].lower()}."), ("The checklist", joined(JD_CMP))],
 expected="One line: a generic job description with invented duties, a team to manage and a senior grade. The checklist: Mutla's template order, the six duties from the role sheet, the grade left blank, and the DRAFT line at the top.",
 say="Same tool, same role, same afternoon. One request gave Copilot nothing to work from. The other gave it everything a new colleague would need.",
 point="The request decides the answer. You decide what goes out.",
 backup=[("h", "One-line request: typical result"), ("p", "“The Compensation Analyst leads a team of analysts, designs reward strategy for the company and advises the Board. Grade: senior.”"),
         ("h", "Checklist request: typical result")] + [("p", x) for x in JD_RESULT_LINES],
 fallback="Show the backup results on the trainer screen.",
 hint="Which answer could go to the committee after a check?")

demo("d11", day=1, skill="1.1", sec=2, title="The same question, with and without the policy", tool="Copilot Chat", files=[F["leave"]],
 setup=["[T] Open a new Copilot Chat. Ask the question below with no file. Read the answer aloud.", f"[T] Open another new chat. Attach {F['leave']} and paste the full request.",
        "[T] Open section 4 of the policy on the screen. Compare the two answers with it."],
 prompts=[("No file", LEAVE_Q[0][1]), ("With the policy", joined(LEAVE_Q))],
 expected=f"With no file, Copilot guesses a common rule, often 30 days or \"it depends on your company\". With the policy attached, it says {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']}, and names section 4.",
 say="Without the file, Copilot predicts a likely answer. With the file and a request to name the section, you can check it in ten seconds.",
 point="Give Copilot the approved file, and ask where each point comes from.",
 backup=[("h", "Typical result with the policy attached"), ("p", f"“{LEAVE_RESULT}”"), ("h", "Typical result with no file"), ("p", "“Most companies allow up to 30 days of unused leave to be carried over. Check your HR policy.”")],
 fallback="Show the backup answers on the trainer screen.",
 hint="Open section 4 of the policy. Does the number match?")

demo("t11", day=1, skill="1.1", sec=2, title="Spot the confident mistakes", tool="Your eyes + the policy", files=[F["leave"], F["answer"]], kind="task", hands_on=True, minutes=10, solo="in pairs",
 setup=[f"Open {F['answer']}. It is a Copilot answer to an employee's leave questions.", f"Open {F['leave']} next to it.",
        "Check every number and rule in the answer against the policy, by hand. No AI for this step.", "Write each mistake: what the answer says, and the section that is right."],
 prompts=[("Then ask Copilot (only after you check by hand)", "Compare the attached answer with the attached leave policy. List every statement in the answer that does not match the policy, and quote the section that is right.")],
 expected="Three mistakes: " + "; ".join(f"{a.lower()}: the answer says “{b}” but {c}" for a, b, c in D.LEAVE_ERRORS) + ".",
 say="The answer reads well. Three of its numbers are wrong. Fluent is not the same as correct.",
 point="Check every number against the approved source before it reaches an employee.",
 backup=[("h", "The three mistakes"), tbl(["Topic", "The answer says", "The policy says"], D.LEAVE_ERRORS)],
 answer=[("h", "The three planted mistakes"), tbl(["Topic", "The answer says", "The policy says"], D.LEAVE_ERRORS),
         ("note", "Lines in the answer that are right: 30 days of annual leave a year (section 2), and Hajj leave of 21 days once in service (section 7). Accept a pair that also flags the missing deadline for carried-over days.")],
 deliverable="The three wrong statements, each with the section that is right.",
 fallback="If a pair cannot open the files, they read them on the Day 1 lab page.",
 hint="There are three mistakes: one about carry-over, one about emergency leave and one about notice.",
 stretch=["For each mistake, write the one-line constraint that would have stopped it."],
 stretch_prompts=[("A safer request", "Answer only from the attached leave policy. For every number, give the section. If the policy does not say, write: not in the policy.")])

GROUP_SORT = [("Decide the grade of a re-evaluated job", "self"), ("Draft a job description from approved role information", "drafts"),
              ("Find what changed between two policy versions", "supports"), ("Approve an allowance exception for one employee", "self"),
              ("Check a tracker total against the control total", "supports"), ("Draft a staff announcement about new attendance rules", "drafts"),
              ("Choose which candidate gets the job offer", "self"), ("Summarize course feedback for the trainer", "drafts")]
GROUP_LABELS = {"self": "Do it yourself", "supports": "Copilot supports", "drafts": "Copilot drafts, you review"}
demo("d11b", day=1, skill="1.1b", sec=2, title="Do it yourself, Copilot supports, or Copilot drafts?", tool="Card sort", kind="sort",
 setup=["[T] Read each card aloud. The room calls the group, then tap the card."],
 prompts=[], expected="Do it yourself: the grade, the allowance exception, the job offer. Copilot supports: comparing versions, checking a total. Copilot drafts: the job description, the announcement, the feedback summary.",
 say="A decision about a person stays with a person. Everything else, Copilot can help with, and you check it.", point="Sort the task before you type.",
 backup=[("h", "The card sort answers"), tbl(["Task", "Group"], [(t, GROUP_LABELS[g]) for t, g in GROUP_SORT])],
 fallback="If the slide fails, read the cards from the backup table and ask for a show of hands.", hint="Ask: does this decide something about a person?")

demo("d12", day=1, skill="1.2", sec=3, title="Build a request, part by part", tool="Copilot Chat", files=[F["leave"]],
 setup=["[T] Open a new Copilot Chat. Attach the leave policy.", "[T] Type the request one part at a time, saying each part aloud before you type it.",
        "[T] Send it. Read the email against section 4 of the policy."],
 prompts=[("The checklist request", joined(CARRY))],
 expected=f"A subject line and a short email: up to {D.LEAVE['carry']} days carry over to next year; carried-over days must be used by {D.LEAVE['carry_by']}; days not used by then are lost. The DRAFT line is at the top. No employee is named.",
 say="Five short parts. Each one answers a question Copilot would otherwise guess.",
 point="Context, task, data, constraints, format.",
 backup=[("h", "Typical result"), ("p", f"{DL}<br>Subject: Plan your leave: carry-over ends on {D.LEAVE['carry_by']}<br>Dear colleagues, up to {D.LEAVE['carry']} days of unused annual leave may be carried over to next year. "
                                         f"Carried-over days must be used by {D.LEAVE['carry_by']}. Days not used by then are lost (Leave Policy, section 4). Please plan your leave with your line manager. Personnel and Administration")],
 fallback="Show the backup email on the trainer screen.",
 hint="If the email adds a rule from another section, the constraints were not strict enough.")

WEAK = ["Write an email about the training course.", "Summarize the allowances policy.", "Make the vacancy report.", "Reply to this employee about his leave.", "Check this job description."]
demo("t12", day=1, skill="1.2", sec=3, title="Rewrite weak requests", tool="Copilot Chat", files=[F["leave"], F["v4"], F["training"]], kind="task", hands_on=True, minutes=14, solo="on your own, then swap",
 setup=["Pick two weak requests: one close to your unit, and one more.", "Rewrite each with all five parts. Name the file to attach.",
        "Swap with a neighbor. Then run one rewrite in Copilot Chat and check it."],
 prompts=[], examples=WEAK,
 expected="Two rewrites, each with context, a single task, the data and file, constraints and a format. Run on its file, the rewrite gives a usable draft.",
 say="A weak request usually has a task and nothing else. Your job is to add the other four parts.",
 point="Five parts: context, task, data, constraints, format.",
 backup=[("h", "A model rewrite: the allowances summary"), ("p", f"You are a Compensation officer at {D.COMPANY}. Staff keep asking about allowances. Summarize the attached allowances policy for staff. Use only {F['v4']}. "
                                                                "Give the section number for every point and keep every amount as written. Plain and friendly. One page of bullets, starting with: " + DL)],
 answer=[("h", "Model rewrites (accept any version with all five parts)"),
         tbl(["Weak request", "A strong rewrite"], [
            (WEAK[0], f"You are a training coordinator at {D.COMPANY}. Nominations for January courses close soon. Write an email to line managers asking for nominations. Use {F['training']}, section 5. Keep the 30-day rule exactly as written; name no employee. Friendly and short. A subject line and up to 100 words."),
            (WEAK[1], f"You are a Compensation officer at {D.COMPANY}. Staff ask the same allowance questions. Summarize the attached policy for staff. Use only {F['v4']}. Every point gives its section; amounts as written. Plain. One page of bullets."),
            (WEAK[2], f"You are a Manpower officer at {D.COMPANY}. The Production division needs its monthly report. List open positions and how long each has been open. Use the attached vacancy data. No names of candidates. Neutral. A table, then three bullets on what is blocked."),
            (WEAK[3], f"You are a Personnel officer at {D.COMPANY}. An employee asked how many leave days he can carry over. Reply to him. Use {F['leave']}, section 4. Do not guess his balance. Polite and short. Three sentences."),
            (WEAK[4], f"You are a Job Evaluation specialist at {D.COMPANY}. The committee meets next week. Check the attached job description against the role information. Use {F['roles']} and {F['tpl']}. Do not fix it; only list problems. Neutral. A table: line, problem.")])],
 deliverable="Two rewrites with all five parts.",
 fallback="If Copilot is slow, swap requests with a neighbor and judge each other's rewrites against the checklist.",
 hint="For each weak request ask five questions: who is it for and why, what exactly, with which facts, within which limits, and in what shape?",
 stretch=["Rewrite a third weak request, from a unit that is not yours."])

NB_FILES = [F["leave"], F["attendance"], F["training"]]
NB_INSTR = (f"You answer employees' questions about {D.COMPANY}'s HR policies. Use only the files in this notebook. For every answer, name the file and the section. "
            "If the files do not answer the question, say so and suggest the employee asks Personnel. Never guess a number or a date. Plain English, short sentences.")
NB_Q = [("Noura, Drilling", "I still have 22 days of annual leave. How many can I carry into next year, and by when must I use them?"),
        ("Saad, Finance", "When the new rules start, can I come in at 6:45 and leave earlier? What hours must I be at work?"),
        ("Mariam, HSE", "How do I ask for a training course, and who has to approve it?"),
        ("Not in the files", "What are the working hours in Ramadan?")]
demo("d13", day=1, skill="1.3", sec=4, title="Build a notebook in four steps", tool="Copilot Notebooks", files=NB_FILES,
 setup=["[T] m365.cloud.microsoft, then Notebooks, then New notebook. Name it Mutla HR policies (practice).",
        "[T] Add the three policies as references, then Create.", "[T] Paste the notebook instruction into the notebook's instructions.",
        "[T] Ask the test question. Open the leave policy at the section it names and check the number."],
 prompts=[("Notebook instruction", NB_INSTR), ("A test question", NB_Q[0][1])],
 expected=f"The answer gives {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']}, and names the leave policy, section 4.",
 say="A notebook keeps the files and the rules for answering in one place. You set it up once and use it every week.",
 point="Copilot answers only from the files you add. It names the file and the section, and you open it.",
 backup=[("h", "Typical answer"), ("p", f"You can carry over up to {D.LEAVE['carry']} days. Use them by {D.LEAVE['carry_by']}. (Leave policy, section 4.)")],
 fallback="No Notebooks on the left: attach the three files to Copilot Chat and paste the instruction first.",
 hint="Which file, which section, and does the number match?")

demo("t13", day=1, skill="1.3", sec=4, title="Build your HR policy notebook", tool="Copilot Notebooks", files=NB_FILES, kind="task", hands_on=True, minutes=22, solo="on your own",
 setup=["Save the three policies to OneDrive. In m365.cloud.microsoft, select Notebooks, then New notebook.",
        "Name it Mutla HR policies (practice). Add the three files as references, then Create.",
        "Paste the notebook instruction into the notebook's instructions.",
        "Test it: one question for each file. Check the file and section in every answer."],
 prompts=[("Notebook instruction", NB_INSTR)],
 expected="A notebook with three references and the instruction. Each test answer names a file and a section, and every number matches the policy.",
 say="Your own notebook, with the three policies Personnel answers from every week.",
 point="Set it up once. Check every answer against its file.",
 backup=[("h", "If Notebooks is not on your account"), ("p", "Attach the three files to Copilot Chat, paste the instruction as your first message, then ask the test questions.")],
 answer=[("h", "Check the notebook for"), ("ul", ["Three references: leave policy, attendance rules, training policy.", "The instruction is in the notebook's instructions, not only in one chat.",
         "Every test answer names a file and a section.", "Every number matches the policy when you open it."])],
 deliverable="Your notebook, and one test answer with its file and section.",
 fallback="No Notebooks on the left: Copilot Chat with the three files attached and the instruction as the first message.",
 hint="Can't find a file under Add references? Check it is in OneDrive, or upload it in the same panel.",
 stretch=["Add the allowances policies (version 3 and version 4). Ask: will my housing allowance change in January?"])

demo("t14", day=1, skill="1.4", sec=4, title="Answer three employees from your notebook", tool="Copilot Notebooks · Outlook", files=[], kind="task", hands_on=True, minutes=20, solo="on your own",
 setup=["Ask your notebook each question, one at a time. Open each file at the section named and check it.",
        "Draft a reply to one employee in Outlook or Word with Copilot. Start with the DRAFT line."],
 prompts=NB_Q,
 expected=(f"Noura: up to {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']} (leave policy, section 4). "
           f"Saad: from {D.ATT['start']}, start between {D.ATT['flex_from']} and {D.ATT['flex_to']}, be at work {D.ATT['core_from']} to {D.ATT['core_to']}, {D.ATT['hours']} hours a day (attendance rules). "
           "Mariam: the steps and the approval as written in the training policy, with its section. Ramadan: the files do not say, so the notebook says it does not know."),
 say="Three real questions and one the files cannot answer. The last one is the most important test.",
 point="A good answer names its source. A good notebook says when it does not know.",
 backup=[("h", "What the notebook should say"), ("ul", [f"Noura: up to {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']}. Leave policy, section 4.",
          f"Saad: from {D.ATT['start']}, start between {D.ATT['flex_from']} and {D.ATT['flex_to']}; at work {D.ATT['core_from']} to {D.ATT['core_to']}; {D.ATT['hours']} hours a day.",
          "Mariam: the request steps and the approver, from the training policy, with the section.", "Ramadan: not in the files. Personnel will confirm."])],
 answer=[("h", "Accept"), ("ul", ["Every answer names a file and a section.", "Every number, time and date matches the policy.", "The Ramadan answer says the files do not cover it; nothing is guessed.",
         "The reply starts with the DRAFT line and promises nothing the policy does not say."])],
 deliverable="Three checked answers, the Ramadan test, and one reply draft.",
 fallback="No notebook: Copilot Chat with the three files attached and the notebook instruction as the first message.",
 hint="If an answer has no file or section, ask for them. Then open the file yourself.",
 stretch=["Ask the notebook for a one-page FAQ for new joiners from the three files. Check five answers."])

HSE = D.HSE_MEMO
MEMO_DEMO = five([("Role", f"You are the Head of Learning and Development at {D.COMPANY}."), ("Context", "The memo goes to all staff."),
    ("Task", "Write a short memo about the HSE Induction e-learning."),
    ("Data", f"Every employee must complete the {HSE['course']} by {HSE['due']}. It takes about {HSE['minutes']} minutes. It is in {HSE['where']}. Questions: {HSE['contact']}."),
    ("Constraints", "Use only these facts. Add no link, no name and no date."), ("Tone", "Clear and friendly."),
    ("Output format", f"A subject line, then under 120 words, starting with: {D.DRAFT_LINE}")])
TNS = D.TNS
TNS_FACTS = (f"The 2027 training needs survey opens on {TNS['open']} and closes on {TNS['close']}. It is in {TNS['where']}. Line managers add {TNS['what']}. "
             f"L&D shares the 2027 training plan by {TNS['plan']}. Questions: {TNS['contact']}.")
MEMO_TASK = five([("Role", f"You are the Head of Learning and Development at {D.COMPANY}."), ("Context", "The memo goes to all line managers."),
    ("Task", "Write a memo asking them to complete the 2027 training needs survey."), ("Data", TNS_FACTS),
    ("Constraints", "Use only these facts. Add no link, no name and no date. Keep every date as written."), ("Tone", "Formal and clear."),
    ("Output format", f"A subject line, the steps as numbered points, under 200 words, starting with: {D.DRAFT_LINE}")])
demo("d15", day=1, skill="1.5", sec=5, title="Draft a memo from a prompt", tool="Word · Copilot", files=[],
 setup=["[T] Open a blank Word document. Select Draft with Copilot. (No Copilot in Word: the same request in Copilot Chat.)",
        "[T] Paste the request. Read the memo aloud.", "[T] Check the date and the minutes against the request. Look for anything Copilot added: a link, a name, a date."],
 prompts=[("A memo from a prompt", joined(MEMO_DEMO))],
 expected=f"A short memo: the {HSE['course']} by {HSE['due']}, about {HSE['minutes']} minutes, in {HSE['where']}, questions to {HSE['contact']}. Nothing added.",
 say="With no file, your prompt is the only source. Every fact in the memo must come from what you typed.",
 point="Draft from a prompt: the facts in your request are the only facts.",
 backup=[("h", "Typical memo"), ("p", f"Subject: Complete the {HSE['course']} by {HSE['due']}"), ("p", f"Every employee must complete the {HSE['course']} by {HSE['due']}. It takes about {HSE['minutes']} minutes and you will find it in {HSE['where']}. Questions: {HSE['contact']}.")],
 fallback="Show the backup memo on the trainer screen.",
 hint="Did Copilot add a link, a name or a date that was not in the request?")

demo("t15", day=1, skill="1.5", sec=5, title="The training needs survey memo", tool="Word · Copilot", files=[], kind="task", hands_on=True, minutes=10, solo="on your own",
 setup=["Open a blank Word document. Select Draft with Copilot. (No Copilot in Word? Use Copilot Chat.)",
        "Write your own request with all five parts. Paste the facts below as your Data.",
        "Check every date in the memo against the facts. Delete anything Copilot added."],
 prompts=[("The facts for your memo", TNS_FACTS)],
 expected=f"A memo to line managers: the survey runs {TNS['open']} to {TNS['close']} in {TNS['where']}; one skill for now and one for two years per team member; the plan by {TNS['plan']}; questions to {TNS['contact']}. No link, name or extra date.",
 say="A memo you send to every line manager. With no file, your request is the only source.",
 point="Every fact in the memo comes from your request. Anything else gets deleted.",
 backup=[("h", "A model request"), ("p", joined(MEMO_TASK))],
 answer=[("h", "Check the memo for"), ("ul", [f"Opens {TNS['open']}, closes {TNS['close']}.", f"Where: {TNS['where']}.", f"What managers add: {TNS['what']}.",
         f"The 2027 plan by {TNS['plan']}.", f"Questions: {TNS['contact']}.", "No link, no person's name, no extra date or deadline.", "The DRAFT line at the top."])],
 deliverable="A one-page memo to line managers, every date as in the facts.",
 fallback="No Copilot in Word: write the same request in Copilot Chat and paste the memo into Word.",
 hint="Copilot likes to add a link or a contact name. Neither is in the facts.",
 stretch=["Select one paragraph and use Rewrite: make it shorter. Check the dates did not move."])

demo("d17", day=1, skill="1.6", sec=5, title="Summarize the leave policy for new joiners", tool="Word · Copilot", files=[F["leave"]],
 setup=["[T] Open the leave policy in Word. Copilot, then Summarize this document. (No Copilot in Word: a new chat with the file attached.)", "[T] Paste the summary request. Read the bullets aloud.",
        "[T] Check two numbers by hand against the policy: the carry-over days and the notice period."],
 prompts=[("Summary for new joiners", joined(SUM_LEAVE))],
 expected=f"Up to eight bullets, each with its section: {D.LEAVE['annual']} days a year (2), request {D.LEAVE['notice']} days before (3), carry over up to {D.LEAVE['carry']} days used by {D.LEAVE['carry_by']} (4), "
          f"{D.LEAVE['emergency']} days emergency leave (5), a certificate after {D.LEAVE['sick_cert']} days of sick leave (6), {D.LEAVE['hajj']} days Hajj leave once (7), balances from Personnel and Administration (8).",
 say="A summary you can check has section numbers. A summary you cannot check is a rumor.",
 point="Every point gives its section. You check two numbers yourself.",
 backup=[("h", "Typical result")] + [("p", f"Section {n}. {t}: {s}") for n, t, s in D.LEAVE_SECTIONS[1:]],
 fallback="Show the backup summary on the trainer screen.",
 hint="Pick two numbers and find them in the policy yourself.")

R360Q = five([("Role", f"You are a Senior HR Officer at {D.COMPANY}."), ("Context", "The line manager reads this before the review meeting."),
    ("Task", f"Summarize the attached 360 feedback for {D.R360_EMP}."), ("Data", "Use only the attached file."),
    ("Constraints", "Group it into strengths, development areas and projects. Name who said each point, by role. Leave out anything about private life. Do not suggest a rating."),
    ("Tone", "Neutral and fair."), ("Output format", f"Three short headings with bullets, one page at most, starting with: {D.DRAFT_LINE}")])
demo("t17", day=1, skill="1.6", sec=5, title="Summarize 360 feedback for a review", tool="Word · Copilot", files=[F["r360"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Open the 360 feedback file in Word. Copilot, then Summarize this document. (No Copilot in Word? Attach it to Copilot Chat.)",
        "Then ask for strengths, development areas and projects, with who said each point.",
        "Read the summary against the file. Is anything there that should not be? Is anything missing?"],
 prompts=[],
 expected=f"Strengths, development areas and projects for {D.R360_EMP}, each point with its reviewer (self, manager, peer, team member). The comment about problems at home and the suggested rating are left out.",
 say="A summary that goes to a review meeting. Fair to the person, and only about work.",
 point="Each point says who said it. Private life and ratings stay out.",
 backup=[("h", "What a good summary covers"), ("ul", ["Strengths: reliable, delivers on time (manager); helpful with data (peer 1); clear instructions (team).",
          "Development: presenting to senior managers (self, manager); delegating (manager); Thursday deadlines (peer 1, team).",
          "Projects: the Drilling Support staffing plan; the manpower tracker clean-up; onboarding 12 graduates."])],
 answer=[("h", "The two planted traps"), tbl(["Trap", "Where", "What to do"], D.R360_TRAPS), ("h", "A model request"), ("p", joined(R360Q))],
 deliverable="A one-page summary with three headings, each point with its reviewer.",
 fallback="No Copilot in Word: attach the file to Copilot Chat and ask for the same summary.",
 hint="Two lines in the file should not reach a review meeting. Which ones, and why?",
 stretch=["Ask Copilot: which comments disagree with each other? Check its answer in the file."])

demo("d18", day=1, skill="1.7", sec=5, title="Rewrite a paragraph, keep the facts", tool="Word · Copilot", files=[],
 setup=["[T] Go back to the memo from Demo 1.5. Select the first paragraph.", "[T] Copilot, then Rewrite. Show the versions. Pick one, then Replace.",
        "[T] Read the date and the minutes again. Did they change?"],
 prompts=[("A rewrite with a rule", "Rewrite this paragraph for new joiners: shorter and warmer. Keep the date and the time exactly as written.")],
 expected=f"A shorter, warmer paragraph with the same date ({HSE['due']}) and the same {HSE['minutes']} minutes.",
 say="Rewrite changes how it sounds. You check that it did not change what it says.",
 point="New words, same facts.",
 backup=[("h", "Typical rewrite"), ("p", f"Welcome to Mutla. Please finish the {HSE['course']} by {HSE['due']}. It takes about {HSE['minutes']} minutes.")],
 fallback="No Copilot in Word: paste the paragraph into Copilot Chat with the same request.",
 hint="Compare the numbers before and after.")

demo("t18", day=1, skill="1.7", sec=5, title="Rewrite the 2019 welcome letter", tool="Word · Copilot", files=[F["welcome"], F["onboard"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Open the 2019 letter in Word. Select one paragraph at a time, then Copilot, Rewrite. (No Copilot in Word? Paste each paragraph into Copilot Chat.)",
        "Make it warm, short and clear for a new graduate. The first day goes in a short list.",
        "Check every time, place and document against the onboarding checklist. Where the letter is out of date, the checklist wins."],
 prompts=[],
 expected="A short, warm letter. First day, documents and probation follow the 2026 checklist, not the 2019 letter.",
 say="An old letter, a new joiner. Rewrite gives you new words fast. The checklist decides the facts.",
 point="Rewrite the words. The checklist decides the facts.",
 backup=[("h", "What the checklist says")] + [("p", f"<b>{a}:</b> {c}") for a, _b, c in D.WELCOME_FIXES],
 answer=[("h", "Three things the 2019 letter gets wrong"), tbl(["Topic", "The 2019 letter", "The 2026 checklist"], D.WELCOME_FIXES),
         ("note", "Rewrite alone keeps the old facts in new words. Accept a letter only when all three follow the checklist.")],
 deliverable="A rewritten welcome letter with the first day, documents and probation from the checklist.",
 fallback="Without the Word app: Copilot Chat, one paragraph at a time, with your rewrite request.",
 hint="Rewrite keeps the old facts. Read the checklist's section 2 and section 4.",
 stretch=["Ask Copilot for a version for field site staff. Check the time and place against the checklist."])

demo("d16", day=1, skill="1.8", sec=5, title="Turn the tone dial, keep the facts", tool="Copilot Chat · Outlook", files=[F["leave"]],
 setup=["[T] Go back to the chat from Demo 1.2, with the carry-over reminder.", "[T] Paste the tone request. Read both versions aloud.",
        "[T] Point to the number and the date in each version: they did not change.", "[T] Where the account allows it, open a new email in Outlook and use Draft with Copilot (the Copilot button) with the same request."],
 prompts=[("Two more readers", joined(TONE))],
 expected=f"A version for line managers (remind your team, approve leave plans before {D.LEAVE['carry_by']}) and three lines for senior leadership. Both keep {D.LEAVE['carry']} days and {D.LEAVE['carry_by']} exactly.",
 say="The reader changes what comes first and how it sounds. The facts do not change for anyone.",
 point="Change the tone. Keep the facts.",
 backup=[("h", "Typical result for line managers"), ("p", f"{DL}<br>Subject: Please help your team plan their leave before {D.LEAVE['carry_by']}<br>Dear managers, only {D.LEAVE['carry']} days of unused leave carry over, and carried-over days must be used by {D.LEAVE['carry_by']}. Please remind your team and approve their leave plans in good time."),
         ("h", "Typical result for senior leadership"), ("p", f"{DL}<br>Subject: Leave carry-over reminder sent to staff<br>Staff were reminded that up to {D.LEAVE['carry']} days carry over and must be used by {D.LEAVE['carry_by']}. Line managers will approve leave plans. No policy change.")],
 fallback="Show the backup versions on the trainer screen.",
 hint="Find the number and the date in every version.")

demo("t16", day=1, skill="1.8", sec=5, title="Announce and reply in Outlook", tool="Copilot Chat · Outlook", files=[F["thread"]], kind="task", hands_on=True, minutes=17, solo="on your own",
 setup=[f"Attach {F['thread']} to a new chat, or open the thread in Outlook with Copilot.", "Run the decisions request below. Find the approved start date.",
        "Write your own checklist request for the staff announcement. Then ask for a version for line managers and a three-line version for senior leadership. The facts stay the same.",
        "Write a reply to Mubarak's request in message 29. Do not promise an exception.", "Check every date and time by hand against message 24."],
 prompts=[("Decisions first (step 2)", joined(THREAD))],
 expected=f"Announcements with {D.ATT['start']}, the {D.ATT['flex_from']} to {D.ATT['flex_to']} start, core hours {D.ATT['core_from']} to {D.ATT['core_to']} and the {D.ATT['permissions']} permissions, in three tones with the same facts. A reply to Mubarak: {D.MUBARAK_ANSWER}",
 say="Three readers, one set of facts. And one reply that is kind without promising what the rules do not allow.",
 point="Change the tone for each reader. Keep every date and rule.",
 backup=[("h", "The decisions"), tbl(["Decision", "Owner", "Date or source"], D.ATT_DECISIONS),
         ("h", "Typical reply to Mubarak"), ("p", f"“{DL}<br>Dear Mubarak, thank you for your message. Under the new rules, the earliest start is {D.ATT['flex_from']}. You can use one of your {D.ATT['permissions']} monthly permissions of up to {D.ATT['perm_hours']} hours, with your line manager's approval. Personnel and Administration”")],
 answer=[("h", "Traps in the thread"), tbl(["Where", "What to do"], D.THREAD_TRAPS), ("h", "Check the announcement for"), ("ul", [f"Start date {D.ATT['start']} (not {D.ATT['old_start']}).", f"Flexible start {D.ATT['flex_from']} to {D.ATT['flex_to']}.",
          f"Core hours {D.ATT['core_from']} to {D.ATT['core_to']}; {D.ATT['hours']} working hours.", f"{D.ATT['permissions']} permissions a month, up to {D.ATT['perm_hours']} hours each.", "No promise about Ramadan hours.", "The same facts in all three versions."]),
         ("h", "The reply to Mubarak"), ("p", D.MUBARAK_ANSWER)],
 deliverable="Three versions of the announcement (staff, line managers, senior leadership) and a reply to Mubarak, every date and rule unchanged.",
 fallback="If the thread file will not open, use the decisions table in the backup on the trainer screen.",
 hint="The start date changed during the thread. The approved one is in message 24.",
 stretch=["Ask Copilot to check your three versions against each other: list any date, time or number that differs."])

# ===================================================================== DAY 2 · Meetings, Reporting and Mapping Your HR Workflow
RED = five([["Role", f"You are a Personnel officer at {D.COMPANY}."],
       ["Context", "The note below is already redacted. It goes to the Personnel Supervisor."],
       ["Task", "Turn the note into a short, neutral case summary for the HR file: what happened, the request and the next step."],
       ["Data", "Employee A, a technician, was absent on two days in late October. [Medical detail removed.] Employee A asks to work at a different site for one month. Colleague B can cover the shift."],
       ["Constraints", "Use only the note. Do not guess any removed detail. Name nobody."],
       ["Tone", "Neutral, short, plain English."],
       ["Output format", f"Three labeled lines, starting with: {DL}"]])
O = D.ORIENT
PREP = five([["Role", f"You are a Personnel officer at {D.COMPANY}."],
        ["Context", "We meet for 30 minutes on Monday to plan the orientation day for new joiners. Personnel, IT and L&D attend."],
        ["Task", "Prepare an agenda, a one-paragraph background brief and three discussion points."],
        ["Data", "The facts: " + " ".join(O["facts"])],
        ["Constraints", "Use only these facts. Give each agenda item an owner and minutes that add up to 30. Turn each open question into a discussion point."],
        ["Tone", "Short and practical."],
        ["Output format", f"An agenda table (item, owner, minutes), then the brief, then the discussion points. Start with: {DL}"]])
NOTES_REQ = five([["Task", "Turn the meeting notes below into decisions, a table of action, owner and deadline, and the open questions."],
             ["Data", "The notes: " + " ".join(O["notes"])],
             ["Constraints", "Add no action that nobody agreed. If an action has no deadline, write: no deadline set."],
             ["Output format", "Decisions, then the action table, then the open questions."]])
RECAP = five([["Role", f"You are an HR officer at {D.COMPANY}."],
         ["Context", "The recap goes to everyone at the meeting and to the HR Section Head."],
         ["Task", "Turn the attached meeting transcript into a recap."],
         ["Data", f"Use only {F['transcript']}."],
         ["Constraints", "Add no action that nobody agreed. Use names and dates exactly as said. List anything not decided as an open question."],
         ["Tone", "Short, neutral, clear."],
         ["Output format", f"Decisions, then a table of action, owner, deadline, then open questions. Start with: {DL}"]])
FOLLOW = five([["Task", "From the action table above, write a follow-up email to everyone at the meeting. Then write a short reminder to Noura about the agenda she promised."],
          ["Constraints", "Keep every owner and date exactly as in the table. No blame. The reminder asks; it does not order."],
          ["Tone", "Polite and short."],
          ["Output format", f"Two emails, each with a subject line. Start each one with: {DL}"]])
TRACKER = five([["Task", "Count the training requests in the Training sheet for Q3 2026, by unit."],
           ["Data", f"Use the attached {F['trackers']}, sheet Training."],
           ["Constraints", "Show the formula or the rows you counted. Then compare your total with the Control totals sheet. Do not fix anything."],
           ["Output format", "A table by unit, then the total, the control total and the difference."]])
PILOT = five([["Role", f"You are an HR analyst at {D.COMPANY}."],
         ["Context", "The Head of HR wants one short note on the attendance pilot for the management meeting."],
         ["Task", "Summarize the pilot result in the attached brief."],
         ["Data", f"Use only {F['brief']}."],
         ["Constraints", "Keep every number as written. Say what the pilot does not show."],
         ["Tone", "Neutral and short."],
         ["Output format", f"A title and three bullets. Start with: {DL}"]])
DECK = five([["Task", "Turn the attached brief into a five-slide outline for the line managers' meeting, with speaker notes."],
        ["Data", f"Use only {F['brief']}."],
        ["Constraints", "Keep every date, time and number exactly as written. End with a slide on where to send questions."],
        ["Tone", "Clear and practical, for busy managers."],
        ["Output format", "Five slides: a title and three bullets each, plus two sentences of speaker notes per slide."]])
BOOK = ("To book an external trainer, the Training Coordinator emails three providers for prices. She copies each price into a spreadsheet by hand. "
        "Her manager approves the choice by email, usually after three days. She then emails Procurement, who asks for the same three prices again. "
        "Nobody tells the trainer the room number until the day before.")
MAPREQ = five([["Task", "Turn the process story below into a step table."],
          ["Data", "The story: " + BOOK],
          ["Constraints", "Do not improve the process. Only map it. Flag each step that has a delay, duplicated effort, unclear ownership or a repetitive step. Mark every step where a person must decide."],
          ["Output format", "A table: step, who, what happens, input, output, wait, problem, a person decides?"]])
MAP_FILE = five([["Task", "Turn process story 1 in the attached file into a step table."],
            ["Data", "Use only story 1 in the attached file."],
            ["Constraints", "Do not improve the process. Only map it. Flag each step that has a delay, duplicated effort, unclear ownership or a repetitive step. Mark every step where a person must decide."],
            ["Output format", "A table: step, who, what happens, input, output, wait, problem, a person decides?"]])
AT = D.ATT
L = D.STORIES["ld"]

demo("d21", day=2, skill="2.12", sec=11, title="Green, amber or red: eight HR tasks", tool="Card sort", kind="sort",
 setup=["[T] Read each card aloud. The room calls green, amber or red, then tap the card."],
 prompts=[], expected="Red: anything with a civil ID, a named salary, medical details or a named person in a case. Amber: internal HR information with no names, in the company's approved Copilot account. Green: fictional files and your own drafting.",
 say="The answer may be right and the decision still wrong. Look at the light before you type.", point="Policy first. Then green, amber or red.",
 backup=[("h", "The card sort answers"), tbl(["Task", "Color"], [(t, c) for t, c in C.SORT])],
 fallback="If the slide fails, read the cards from the backup table and ask for a show of hands.", hint="Ask: is there personal data? Is this my company's approved account?")

demo("d21b", day=2, skill="2.12b", sec=11, title="Redact, then ask", tool="Copilot Chat",
 setup=["[T] Show the note before redaction on the trainer screen only. Never paste it.", "[T] Redact it aloud: roles for names, no ID, phone, salary or medical detail.",
        "[T] Open a new Copilot Chat. Paste the request with the redacted note in it. Read the summary: does it guess the removed detail?"],
 prompts=[("Summarize a redacted note", joined(RED))],
 expected="A three-line summary (what happened, the request, the next step) that names nobody and does not guess the removed detail.",
 say="Copilot only ever sees the redacted note. The redaction happens before the prompt, not inside it.",
 point="Redact first. Then ask.",
 backup=[("h", "Typical result"), tbl(["Part", "Summary"], [("What happened", "Employee A was absent on two days in late October."), ("The request", "To work at a different site for one month."), ("Next step", "The Personnel Supervisor decides. Colleague B can cover the shift.")])],
 fallback="Show the backup table on the trainer screen.",
 hint="If the summary guesses a removed detail, add: do not guess anything removed.")

demo("t21", day=2, skill="2.12", sec=11, title="Redact a case note", tool="Your eyes + Word", files=[F["case"]], kind="task", hands_on=True, minutes=11, solo="on your own",
 setup=[f"Open {F['case']} in Word. Save a copy with -redacted at the end of the name.", "Find every detail that identifies a person or is sensitive.",
        "Replace names with roles (Employee A, Colleague B). Remove the civil ID, phone number, salary and medical reason.", "Read it once more. Could anyone outside HR tell who this is?"],
 prompts=[("Only on the redacted copy", "Read the attached note. List any detail that could still identify a person or is sensitive. Do not repeat the detail itself; give its paragraph number.")],
 expected="Six items removed or replaced: " + "; ".join(f"{a.lower()} → {c}" for a, _b, c in D.CASE_SENSITIVE) + ".",
 say="Redact first, then ask. Copilot can help you tidy the note only after nothing sensitive is left in it.",
 point="Replace names with roles. Remove IDs, numbers, salaries and medical details.",
 backup=[("h", "What a redacted note replaces"), tbl(["Sensitive item", "Replace with"], [(a, c) for a, _b, c in D.CASE_SENSITIVE])],
 answer=[("h", "The six planted items"), tbl(["Item", "In the note", "Replace with"], D.CASE_SENSITIVE),
         ("note", "The facts of the case (dates of absence, the request, the next step) stay in. Accept other neutral labels for people, used the same way throughout. Also accept a note that makes the dates or the unit general.")],
 deliverable="A redacted copy of the case note that is safe to use with Copilot.",
 fallback="If Word is not available, mark the items in the file preview and list them in a note.",
 hint="Six items: two names, an ID number, a phone number, a salary and a medical reason.",
 stretch=["On the redacted copy only, ask Copilot whether any personal detail is left."])

OPENQ = {"je": "The employee asks whether the grade will change. Only the committee decides.",
         "cmp": "Employees will ask whether the change is automatic. It is: no request is needed.",
         "mp": "Two technician positions: contract or permanent? Not decided.",
         "pa": "How to handle exceptions to the new rules.",
         "ld": "Which requests are still pending, with KWD 3,100 left in the Q4 budget."}
CO = {"mp": "Recruitment, about the hiring order for the new section", "cmp": "the Compensation Supervisor, before the meeting with Finance",
      "pa": "the line managers, on Monday 23 November, to agree how to handle exceptions", "ld": "the Head of Learning and Development, about the Q4 budget",
      "je": "the Job Evaluation committee, on Thursday 10 December"}
TO = {"mp": "Finance, about the manpower request", "cmp": "Finance, with the cost estimate", "pa": "the line managers, before their meeting",
      "ld": "the line managers, about pending requests and the nomination deadline", "je": "the employee who asked whether the grade will change"}
demo("d22", day=2, skill="2.1", sec=6, title="Agenda, brief and discussion points", tool="Copilot Chat · Word",
 setup=["[T] Open a new Copilot Chat (or a new Word document with Copilot).", "[T] Paste the request: the meeting facts are inside it.",
        "[T] Add up the minutes in the agenda aloud. Check that each open question became a discussion point."],
 prompts=[("Prepare the meeting", joined(PREP))],
 expected=f"An agenda with an owner for each item and 30 minutes in total, a short brief ({O['joiners']} new joiners on {O['date']}, {O['room']}), and three discussion points, one of them the Medical Services check.",
 say="A meeting goes well when the page before it is good. Two minutes with Copilot, then you check the minutes add up.",
 point="Agenda, brief, discussion points: from approved facts only.",
 backup=[("h", "Typical agenda"), tbl(["Item", "Owner", "Minutes"], [("ID cards and laptop accounts", "Personnel and IT", "10"), ("Welcome session and safety briefing", "L&D", "10"), ("Medical Services check: same day?", "Personnel", "5"), ("Actions and owners", "Chair", "5")])],
 fallback="Show the backup agenda on the trainer screen.",
 hint="Do the minutes add up to 30?")

demo("t22", day=2, skill="2.1", sec=6, title="Prepare your track's meeting", tool="Copilot Chat · Word", files=CASE_FILES, kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=["Open the case file for your unit track. Find the meeting coming up in it.",
        "Write your own checklist request: an agenda, a one-paragraph background brief and three discussion points. Attach the case file.",
        "Check by hand: does every agenda item have an owner? Do the minutes add up? Is every fact in the case file?"],
 prompts=[],
 expected="An agenda with owners and minutes, a brief that uses only the case facts, and discussion points that include the case's open question.",
 say="Same method as the demo, your own unit's meeting.",
 point="A good meeting starts with a good page.",
 backup=[("h", "The meeting in each case")] + [("p", f"<b>{n}:</b> {CO[k]}.") for k, n in D.TRACKS],
 answer=[("h", "The meeting and the open question in each case"), tbl(["Track", "Meeting", "Open question to discuss"],
         [(n, CO[k], OPENQ[k]) for k, n in D.TRACKS])],
 deliverable="An agenda, a background brief and three discussion points for your track's meeting.",
 fallback="If your case file will not open, use the Personnel and Administration case.",
 hint="Turn the open question in your case into a discussion point.",
 stretch=["Ask Copilot to list the facts the brief needs that the case file does not give. Do not let it invent them."])

demo("d23", day=2, skill="2.2", sec=6, title="Notes into decisions and actions", tool="Copilot Chat",
 setup=["[T] Open a new Copilot Chat. Paste the request: the notes are inside it.", "[T] Read the action table aloud. Ask the room: is there an action nobody agreed?"],
 prompts=[("Notes into actions", joined(NOTES_REQ))],
 expected="Four actions with owners; three have deadlines and one says no deadline set. The idea of inviting the CEO is not an action: nobody agreed. One open question: the Medical Services check.",
 say="A recap records what was agreed. An idea that nobody agreed to is not an action, however good it sounds.",
 point="Action, owner, deadline. Nothing nobody agreed.",
 backup=[("h", "Typical action table"), tbl(["Action", "Owner", "Deadline"], D.ORIENT_ACTIONS)],
 fallback="Show the backup table on the trainer screen.",
 hint="Find the line that nobody agreed to.")

demo("t23", day=2, skill="2.2", sec=6, title="Recap the staffing meeting", tool="Copilot Chat · Teams", files=[F["transcript"]], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=[f"Attach {F['transcript']} to a new chat. (In Teams, Copilot recaps a meeting only when it was transcribed.)",
        "Write your own checklist request for a recap: decisions, then action, owner and deadline, then open questions.",
        "Check every owner and deadline by hand against the transcript. Delete anything nobody agreed."],
 prompts=[],
 expected=f"Four actions with owners and deadlines for the new {D.NEW_SECTION} section, and one open question: whether two positions are contract or permanent.",
 say="A meeting nobody summarizes is a meeting nobody remembers.",
 point="Every action has an owner and a deadline from the transcript.",
 backup=[("h", "Typical result"), tbl(["Action", "Owner", "Deadline"], D.STAFF_ACTIONS), ("h", "Open question"), ("ul", D.STAFF_OPEN)],
 answer=[("h", "The actions"), tbl(["Action", "Owner", "Deadline"], D.STAFF_ACTIONS), ("h", "Open question"), ("ul", D.STAFF_OPEN),
         ("note", "A recap that turns the open question into a decision (for example, \"two contract positions\") is wrong: it was not decided.")],
 deliverable="A recap: decisions, an action table with owners and deadlines, and the open question.",
 fallback="If the transcript will not open, use the backup table on the trainer screen.",
 hint="One question in the meeting was not decided. It belongs in the open questions.",
 stretch=["Ask Copilot to list every name and date in your recap with the transcript line it came from."])

demo("d24", day=2, skill="2.3", sec=7, title="A follow-up and a reminder", tool="Copilot Chat · Outlook",
 setup=["[T] In Outlook with the training mailbox: open the thread Orientation day for new joiners, Sunday 6 December, and select Summarize. Check the laptop date (2 December), the briefing time (8:30 to 10:30), the action hidden in an older message (the list of new joiners to IT by 26 November) and the open question (which 6 new joiners come on Monday 7 December).",
        "[T] Go back to the chat from Demo 2.2, with the action table.", "[T] Paste the follow-up request. Read both emails aloud.",
        "[T] Point to each owner and date: did any change?", "[T] Where the account allows it, open a new email in Outlook and use Draft with Copilot with the same request."],
 prompts=[("Follow-up and reminder", joined(FOLLOW))],
 expected="A follow-up email to everyone with the four actions, owners and dates unchanged, and a polite two-line reminder to Noura about the agenda due on Monday 30 November.",
 say="The recap is only useful when it reaches people. A follow-up today and a reminder before the deadline: two short emails.",
 point="Same owners, same dates. Polite, never blaming.",
 backup=[("h", "Typical reminder"), ("p", f"{DL}<br>Subject: Reminder: agenda for the new joiners<br>Dear Noura, a quick reminder that the agenda for the new joiners is due on Monday 30 November. Thank you. Fatma")],
 fallback="Show the backup reminder on the trainer screen.",
 hint="Check every owner and date against the table.")

demo("t24", day=2, skill="2.3", sec=7, title="Follow up the staffing meeting", tool="Copilot Chat · Outlook", files=[F["transcript"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Use your recap from Task 2.2. No recap? Copy the action table the trainer shows.",
        "Write your own checklist request for a follow-up email to everyone at the meeting, with the action table.",
        "Then write a polite reminder to Khaled about the action he owns, two days before its deadline.",
        "Check every owner and date by hand against the transcript."],
 prompts=[],
 expected=f"A follow-up with the four actions, owners and deadlines unchanged, and a reminder to Khaled about the manpower request due {D.STAFF_ACTIONS[0][2]}, with no blame.",
 say="Two short emails that make sure the meeting turns into work.",
 point="Follow up today. Remind before the deadline, not after.",
 backup=[("h", "The actions"), tbl(["Action", "Owner", "Deadline"], D.STAFF_ACTIONS)],
 answer=[("h", "Check the emails for"), ("ul", ["All four actions, each with its owner and deadline as in the transcript.", f"The reminder names the manpower request and {D.STAFF_ACTIONS[0][2]}.", "No blame, no new task, no promise the meeting did not make.", "The open question stays open."])],
 deliverable="A follow-up email to the meeting and a reminder to Khaled.",
 fallback="No recap from Task 2.2: show the four actions from the backup on the trainer screen.",
 hint="The reminder asks politely and gives the deadline. It does not blame.",
 stretch=["Write the same reminder for a manager who has already missed a deadline. Keep it polite."])

demo("t25", day=2, skill="2.4", sec=7, title="Your track's message", tool="Copilot Chat · Outlook", files=CASE_FILES, kind="task", hands_on=True, minutes=10, solo="on your own",
 setup=["Open your track's case file again. Find who needs a message, and why.", "Write your own checklist request for that message. Attach the case file.",
        "Check every date and number by hand against the case file. No names of employees in the message."],
 prompts=[],
 expected="One message per track, with every date and number from the case file and nothing promised that the case does not say.",
 say="A different reader and a different reason. Same checklist.",
 point="The right reader, the facts as written, nothing promised.",
 backup=[("h", "Who gets the message in each case")] + [("p", f"<b>{n}:</b> {TO[k]}.") for k, n in D.TRACKS],
 answer=[("h", "The message in each case"), tbl(["Track", "To", "Must include"], [(n, TO[k], "; ".join(D.CASES[k]["facts"][-2:])) for k, n in D.TRACKS]),
         ("note", "Job Evaluation: the reply must say that only the committee decides the grade, and give no grade.")],
 deliverable="One message for your track's case, checked against the case file.",
 fallback="Short of time: write the subject line and the first two sentences, then check them.",
 hint="Who reads it, and what must they do after reading it?")

demo("d26", day=2, skill="2.5", sec=8, title="Ask the tracker, then see the rows", tool="Copilot Chat · Excel", files=[F["trackers"]],
 setup=[f"[T] Attach {F['trackers']} to a new chat, or open it in Excel with Copilot (a saved .xlsx workbook).", "[T] Paste the count request. Open the Control totals sheet on the screen.",
        "[T] Put the two totals side by side. Ask the room what could make a total too high.", "[T] Run the chart request. Point to the axis (from zero) and to the gap in every unit."],
 prompts=[("Count and compare", joined(TRACKER)),
          ("A chart you can check", "Make a clustered column chart by unit: the Training sheet count next to the Control totals count. Start the axis at zero. Do not change any data.")],
 expected=(f"Copilot counts {D.TRAIN_ROWS_EXPORT} rows. The Control totals sheet says {D.TRAIN_TRUE}. The difference is {D.TRAIN_DUPES}. "
           "On the chart, every unit's bar is 1 to 3 higher than its control bar: the problem is spread across the units, so look for repeated rows."),
 say="Copilot counted every row correctly. The rows were wrong. Only the check found it.",
 point="Ask, see the rows, then check against the control total.",
 backup=[("h", "Typical result"), tbl(["Count", "Number"], [("Rows in the Training sheet", str(D.TRAIN_ROWS_EXPORT)), ("Control total", str(D.TRAIN_TRUE)), ("Difference", str(D.TRAIN_DUPES))])],
 fallback="Show the backup table. If upload fails, use a PivotTable in Excel.",
 hint="A total that is too high: look for duplicate request IDs.")

demo("t26", day=2, skill="2.5", sec=8, title="Training requests: find the duplicates", tool="Copilot Chat + Excel", files=[F["trackers"]], kind="task", hands_on=True, minutes=12, solo="in pairs",
 setup=[f"Attach {F['trackers']}. Run the request below to find the duplicate request IDs.", "Check by hand in Excel: select the Request ID column, then Home > Conditional Formatting > Highlight Cells Rules > Duplicate Values.",
        "Write the corrected total, and why it changed."],
 prompts=[("The rows behind the difference", "The Training sheet total does not match the Control totals sheet. List every request ID that appears more than once, with its row numbers. Do not delete anything.")],
 expected=f"{D.TRAIN_DUPES} request IDs appear twice. The corrected count is {D.TRAIN_TRUE}.",
 say="Copilot finds the rows. Excel confirms them. You write the corrected figure.",
 point="Too high: look for duplicates. Then check them yourself.",
 backup=[("h", "The figure"), tbl(["Figure", "In the file", "Correct", "Why"], [("Q3 training requests", str(D.TRAIN_ROWS_EXPORT), str(D.TRAIN_TRUE), f"{D.TRAIN_DUPES} duplicate request IDs")])],
 answer=[("h", "The planted problem"), tbl(["Figure", "In the file", "Correct", "Cause"], [("Q3 training requests", str(D.TRAIN_ROWS_EXPORT), str(D.TRAIN_TRUE), f"{D.TRAIN_DUPES} duplicate request IDs: " + ", ".join(D.TRAIN_DUP_IDS))])],
 deliverable="The corrected training total and the reason.",
 fallback="If upload fails, pairs use Conditional Formatting and Remove Duplicates on a copy in Excel.",
 hint="Each request ID should appear once.",
 stretch=["Ask for a chart of training requests by unit after removing the duplicates. Check that the axis starts at zero."])

PAYREQ = ("Compare the October and November sheets by employee code. List every code whose total changed, and every code that is in only one month. "
          "Then check each line of the Movements sheet against November. For each item, say whether the Movements sheet explains it. "
          "Do not recalculate any salary. Do not fix anything.")
OTREQ = ("List every cleaning problem in the Overtime sheet: unit names written in more than one way, hours stored as text, "
         f"dates in other formats, blank or repeated rows, and any day above {D.OT_MAX_DAY} hours. Give the row numbers. Do not change anything.")
OTCHART = ("From the cleaned copy, make a column chart of overtime hours by unit. Start the axis at zero and put the total under the chart. "
           "Then compare each unit's total with the Control totals sheet and list every unit that does not match. Do not change any hours.")
_OT_TOT = [(u, f"{D.OT_CLEAN_TOTALS[u]:g}", f"{D.OT_CONTROL[u]:g}", f"{D.OT_CLEAN_TOTALS[u] - D.OT_CONTROL[u]:g}") for u in D.OT_UNITS]
demo("t27", day=2, skill="2.6", sec=8, title="Payroll, or clean and chart", tool="Copilot Chat + Excel", files=[F["payroll"], F["overtime"]], kind="task", hands_on=True, minutes=12, solo="in pairs",
 setup=["Choose one. A: payroll, October against November. B: the October overtime export.",
        "A: run request A. Check each item in Excel. One line per item to confirm. Change no salary.",
        "B: run request B, or Data > Clean Data. Fix a copy, chart hours by unit, compare with Control totals. Change no hours."],
 prompts=[("A · Two months and the movements", PAYREQ), ("B · The cleaning problems", OTREQ)],
 stretch_prompts=[("B · The chart and the check", OTCHART)],
 expected=("A: four differences between the months. The Movements sheet explains three of them: " + "; ".join(f"{c} ({w.split(':')[0].lower()})" for c, w in D.PAY_EXPLAINED) +
           ". Three items need a person to confirm: " + " ".join(f"{c}: {w}" for c, w, _a in D.PAY_ISSUES) +
           f" B: six kinds of problem (unit names, hours as text, dates, a repeated claim, a blank row, two days above {D.OT_MAX_DAY} hours). After cleaning, "
           "three units match the control totals. " + " ".join(f"{u}: {g}" for u, g, _w in D.OT_GAPS)),
 say="Two kinds of check. Payroll: what changed, and is it approved? Overtime: is the data clean enough to count? Either way, Copilot finds it and a person confirms it.",
 point="Clean it, count it, check it against a reference. Never fix a number yourself.",
 backup=[("h", "A · Items to confirm"), tbl(["Employee code", "What is wrong", "Next step"], D.PAY_ISSUES), ("h", "A · Explained by the Movements sheet"), tbl(["Employee code", "Movement"], D.PAY_EXPLAINED),
         ("h", "B · After cleaning, against the control totals"), tbl(["Unit", "Clean total (hours)", "Control total (hours)", "Gap"], _OT_TOT)],
 answer=[("h", "A · The three planted items"), tbl(["Employee code", "What is wrong", "Next step"], D.PAY_ISSUES),
         ("note", "Comparing the two months finds only EMP-3346. The leaver did not change, and the missing joiner is in neither month: only the Movements sheet shows them. Accept any wording that asks a person to confirm and changes no salary."),
         ("h", "B · The planted problems"), tbl(["Problem", "Rows", "Fix"], D.OT_ISSUES),
         ("h", "B · The two gaps"), tbl(["Unit", "What the rows show", "Who confirms"], D.OT_GAPS), tbl(["Unit", "Clean total (hours)", "Control total (hours)", "Gap"], _OT_TOT),
         ("note", "Accept a chart with one bar per unit (five bars), the axis from zero and the total under it. A chart with eight or more bars still has unit names written two ways.")],
 deliverable="A: three payroll items to confirm. B: a clean copy, a chart of hours by unit, and one line for each gap.",
 fallback="If upload fails: A, sort both months by employee code and compare them side by side. B, filter the Unit column and look at every name in the list.",
 hint="A: the Movements sheet finds two of the three. B: a unit written two ways becomes two bars.",
 stretch=["Do the other option. Or open the trackers file: on the Manpower sheet, total vacancies look too low. Find out why."])

# ===================================================================== DAY 2 · Block 4 · Microsoft Forms: find the training needs (Aya, 18 Nov 2026)
TNB = F["tnbrief"]; TNR = F["tnresp"]
TN_WEAK = "Create a training needs survey for our employees."
REQS = five([["Role", f"You are a Learning and Development specialist at {D.COMPANY}."],
        ["Context", f"L&D builds the 2027 training plan from a training needs survey that {D.TN_INVITED_TOTAL} line managers answer in December. Last year's survey was a Word form, and the answers were hard to count."],
        ["Task", "Before writing any question, list the decisions L&D must make from this survey and the information each decision needs. Then suggest one question for each piece of information."],
        ["Data", f"Use only the attached brief, {TNB}."],
        ["Constraints", "At most 10 questions. Every question serves one decision. One idea per question. Use choices wherever the brief gives a list. Never ask for an employee's name, civil ID, performance rating, salary or health."],
        ["Output format", "A table: decision, information needed, question, question type (choice, number or text), required (yes or no)."]])
FORMQ = (f"Create a form called \"Mutla 2027 training needs survey\" for line managers. It must take under 5 minutes. "
         f"Start with one line: your answers help L&D build the 2027 training plan by {D.TNS['plan']}. Questions: "
         f"1. Your unit (choice: {', '.join(D.TN_INVITED)}). 2. Your section (short text). 3. How many people do you manage? (number). "
         f"4. The one skill your team needs most now (choice: {', '.join(D.TN_NOW)}, Other). 5. How many of your team need it now? (number). "
         f"6. One skill your team will need in the next two years (choice: {', '.join(D.TN_LATER)}, Other). "
         f"7. How should they learn it? (choice: {', '.join(D.TN_HOW)}). 8. Best quarter for this training in 2027 (choice: Q1, Q2, Q3, Q4). "
         "9. Anything else L&D should know? (long text, optional; under it write: Please do not write names or personal details). "
         "Questions 1 to 8 are required. Add no other question.")
TNCOUNT = "Count the answers to \"The one skill your team needs most now\", from most to least. Show the count for each answer exactly as written."
TNPROB = ("Before we trust these counts, list every row that should not be counted (a test, or a manager who answered twice) and every skill that is written in more than one way. "
          "Give the row ID for each. Also list any comment that names a person or gives a health detail, by row ID only: do not repeat it. Do not change or delete anything.")
TNCLEAN = ("Count again without the test answer and without the first of the two answers from the same manager. Count every way of writing Excel as Excel for HR reporting. "
           "Give the top three skills with the number of answers and the total number of people who need each. Then give the answers by unit against the Invited sheet.")
_TN_TOP = [(s, str(D.TN_COUNT[s]), str(D.TN_SEATS[s])) for s in D.TN_TOP]
_TN_RAW = [(s, str(D.TN_RAW_COUNT[s])) for s in D.TN_RAW_TOP]
_TN_UNITS = [(u, str(D.TN_INVITED[u]), str(D.TN_BY_UNIT[u])) for u in D.TN_INVITED]
_TN_REMOVE = [(str(D.TN_TEST_ID), "A test answer (section TEST)", "Do not count it."),
              (f"{D.TN_FIRST_ID} and {D.TN_SECOND_ID}", "The same HR manager (Payroll) answered twice, 19 minutes apart", f"Count only the second answer, {D.TN_SECOND_ID}: the comment asks for it."),
              ("Five rows", "Excel written five ways under Other: " + ", ".join(D.TN_EXCEL_OTHER), "Count them as Excel for HR reporting."),
              (str(D.TN_RED_ID), "A comment names an employee, his code and a health detail", "Never copy, paste or summarize it. Keep only: some staff cannot join field courses this year."),
              (str(D.TN_ASK_ID), "A comment asks L&D to approve a course now", "Not a finding. L&D decides with the plan.")]
TN_FINDINGS = [f"{len(D.TN_VALID)} of {D.TN_INVITED_TOTAL} line managers answered ({D.TN_RATE}%). {D.TN_LOW_UNIT} answered least: {D.TN_BY_UNIT[D.TN_LOW_UNIT]} of {D.TN_INVITED[D.TN_LOW_UNIT]}.",
               "Top needs now: " + "; ".join(f"{s}, {c} answers, {n} people" for s, c, n in _TN_TOP) + ".",
               f"Before cleaning, Excel looked third ({D.TN_RAW_COUNT['Excel for HR reporting']} answers): five managers wrote it in their own words.",
               f"Two rows were not counted: a test answer and a manager's first answer. One comment held personal details and was left out.",
               f"Next step: L&D follows up with {D.TN_LOW_UNIT} before the plan is due on {D.TNS['plan']}."]

demo("dfm1", day=2, skill="2.7", sec=9, title="From a vague ask to requirements", tool="Copilot Chat", files=[TNB],
 setup=["[T] Open a new Copilot Chat. Paste the weak request first, with no file. Read the questions aloud.",
        f"[T] Ask the room: which of these questions helps L&D decide anything? Who would answer it, staff or managers?",
        f"[T] Open a new chat. Attach {TNB}. Paste the requirements request. Read the table row by row.",
        "[T] Point to each question and ask: which decision does it serve? Delete any question with no decision behind it."],
 prompts=[("A weak start", TN_WEAK), ("Requirements first", joined(REQS))],
 expected=("The weak request gives a generic employee survey: name, job title, rate your skills, which courses you like. Nothing ties to a decision, and some questions collect personal data. "
           f"The requirements request gives the five decisions in the brief and eight or nine questions: unit, section, team size, the skill needed now, how many need it, the skill for two years, how to learn, the best quarter, and an optional comment."),
 say="A form is only as good as the decisions behind it. Write the decisions first, and the questions almost write themselves.",
 point="Decisions first. Then the information. Then the questions.",
 backup=[("h", "The decisions and the information they need"), tbl(["Decision", "Information needed"], D.TN_DECISIONS)],
 fallback="Show the backup table on the trainer screen.",
 hint="For every question, ask: which decision does it serve?")

demo("tfm1", day=2, skill="2.7", sec=9, title="Brainstorm the requirements", tool="Copilot Chat", files=[TNB], kind="task", hands_on=True, minutes=12, solo="in pairs",
 setup=[f"Choose one. A: the company's 2027 training needs survey, from {TNB}. B: a training needs form for your own unit or department.",
        "Write your own checklist request: the decisions first, then the information each decision needs, then one question for each. A: attach the brief. B: write three or four facts about your unit as your Data.",
        "Test every question three ways: Which decision does it serve? Can a manager answer it in under a minute? Does it ask for anyone's personal data? Delete what fails.",
        "Keep eight questions or fewer. Write your question plan: question, type (choice, number or text), the choices, required or not."],
 prompts=[],
 expected=("A: the five decisions in the brief, and eight or nine questions with the 8 units and the course list as choices, no personal data, and the comment question optional. "
           "B: a short plan for one unit where every question serves a decision and nothing asks about one named person."),
 say="Same method as the demo: decisions, information, questions. Then cut.",
 point="Every question serves a decision. Nothing asks about one person.",
 backup=[("h", "The decisions in the brief"), tbl(["Decision", "Information needed"], D.TN_DECISIONS)],
 answer=[("h", "A · A good question plan"), tbl(["Question", "Type", "Serves"], [("Your unit", "Choice: the 8 units", "Which units come first"), ("Your section", "Short text", "Which units come first"),
          ("How many people do you manage?", "Number", "How many seats"), ("The one skill your team needs most now", "Choice: the course list, Other", "Which courses"),
          ("How many of your team need it now?", "Number", "How many seats"), ("One skill for the next two years", "Choice, Other", "What to prepare for later"),
          ("How should they learn it?", "Choice", "How to deliver"), ("Best quarter in 2027", "Choice: Q1 to Q4", "When to run it"), ("Anything else? (no names)", "Long text, optional", "Context")]),
         ("h", "Delete on sight"), ("ul", ["Employee name, civil ID or employee code.", "Rate this employee's performance.", "Salary or grade.", "Any health or personal reason.", "Two ideas in one question, for example: which course and when?"]),
         ("note", "B: accept any plan where every question serves a decision, choices are used where a list exists, and nothing asks about one named person.")],
 deliverable="A question plan of eight questions or fewer: question, type, choices, required.",
 fallback="No Copilot: write the decisions and questions by hand from the brief. The method matters more than the tool.",
 hint="Start from the five decisions in the brief. Which question does each one need?",
 stretch=["Ask Copilot: which of my questions could a manager misread? Rewrite the two weakest."])

demo("dfm2", day=2, skill="2.8", sec=9, title="Draft the form with Copilot in Forms", tool="Microsoft Forms · Copilot", files=[TNB],
 setup=["[T] Open forms.cloud.microsoft (or forms.office.com) with the training account. Select New Form. In the Draft with Copilot box, paste the request. Select Keep it.",
        "[T] Check every question against the plan: the type, the 8 units, the course list with Other, the numbers, required or not. Fix one thing by hand on screen.",
        "[T] Open Settings: only people in my organization can respond. Talk about whether to record names (see the discussion).",
        "[T] Select Collect responses, then copy the link or show the QR code. The room answers once with made-up answers: two minutes. Keep the form open for Demo 2.9.",
        "[T] No Draft with Copilot: ask Copilot Chat for the same questions as a numbered list with each choice on its own line, paste it into Word, save it, then Forms > Quick import."],
 prompts=[("Draft the form", FORMQ)],
 expected="A nine-question form called Mutla 2027 training needs survey. Copilot may add a question (often name or email), turn a number into ranges, or make the comment required. Each of these gets fixed by hand before the link goes out.",
 say="Copilot builds the form in a minute. You are still the person who decides what it asks.",
 point="Copilot drafts the form. You check every question against the plan.",
 backup=[("h", "The nine questions"), ("ol", ["Your unit (choice)", "Your section (short text)", "How many people do you manage? (number)", "The one skill your team needs most now (choice, Other)",
          "How many of your team need it now? (number)", "One skill for the next two years (choice, Other)", "How should they learn it? (choice)", "Best quarter in 2027 (choice)", "Anything else L&D should know? (optional, no names)"])],
 fallback="No Copilot in Forms: Copilot Chat writes the questions, then Quick import from Word (choice and text questions only), or build the nine questions by hand.",
 hint="Did Copilot add a question you did not ask for?")

demo("tfm2", day=2, skill="2.8", sec=9, title="Build your form", tool="Microsoft Forms · Copilot", files=[TNB], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=["Open forms.cloud.microsoft (or forms.office.com) and select New Form.",
        "In the Draft with Copilot box, write a request from your Task 2.7 plan: the title, who answers, every question with its type and choices, which are required. Select Keep it.",
        "Check every question against your plan. Delete what you did not ask for. Fix types and choices by hand.",
        "Settings: only people in your organization can respond. Preview it on your phone.",
        "Send the link to your partner. Answer each other's form twice, with made-up answers."],
 prompts=[],
 expected="A working form that matches the plan from Task 2.7, shared with a partner, with at least two test answers.",
 say="Your plan, your form. Copilot does the typing.",
 point="The form matches the plan. Nothing extra, nothing personal.",
 backup=[("h", "No Draft with Copilot?"), ("ol", ["Ask Copilot Chat: write my questions as a numbered list, each choice on its own line.", "Paste the list into Word and save it.", "In Forms, select Quick import and upload the file. Check every question it made.", "Number questions arrive as text: set them to Number by hand."])],
 answer=[("h", "Check the form for"), ("ul", ["Every question from the plan, and none that is not in it.", "Choices where the plan has a list; Other only where it said so.", "Numbers set as Number.", "The comment question optional, with the no-names line.", "Only people in the organization can respond.", "Two or more test answers."])],
 deliverable="A working form, shared with your partner, with at least two test answers.",
 fallback="No Copilot in Forms: Quick import from Word, or build it by hand. No Forms at all: write the form in Word as a table and pair with a neighbor who has Forms.",
 hint="Copilot follows a list best. Give it every question, its type and its choices.",
 stretch=["Ask Copilot in Forms to review your form. Accept only the suggestions that serve your plan."])

demo("dfm3", day=2, skill="2.9", sec=9, title="From responses to findings", tool="Forms · Excel · Copilot", files=[TNR],
 setup=["[T] In the demo form, open Responses. Show the room's answers. Open Copilot in Forms and ask for the main training needs by unit, with the number of answers behind each point. Check one number against the chart.",
        f"[T] Then: imagine it is {D.TNS['close']} and the survey has closed. Open {TNR} in Excel with Copilot, or attach it to Copilot Chat.",
        "[T] Run the count request. Write the top three on the board.",
        "[T] Run the problems request. Show the test row, the manager who answered twice and Excel written five ways. Do not read the personal comment aloud: point to its row ID only.",
        "[T] Run the clean count. Compare the new top three with the board."],
 prompts=[("1 · Count as it is", TNCOUNT), ("2 · Find the problems", TNPROB), ("3 · Count again, cleaned", TNCLEAN)],
 expected=(f"Count as it is: {', '.join(f'{s} {c}' for s, c in _TN_RAW)}. Problems: row {D.TN_TEST_ID} is a test; rows {D.TN_FIRST_ID} and {D.TN_SECOND_ID} are the same manager; Excel is written five ways; "
           f"row {D.TN_RED_ID} names a person and a health detail. Cleaned: " + "; ".join(f"{s} {c} answers, {n} people" for s, c, n in _TN_TOP) +
           f". {len(D.TN_VALID)} of {D.TN_INVITED_TOTAL} managers answered ({D.TN_RATE}%); {D.TN_LOW_UNIT} {D.TN_BY_UNIT[D.TN_LOW_UNIT]} of {D.TN_INVITED[D.TN_LOW_UNIT]}."),
 say="The form collects the answers. Copilot counts them. But the first count was wrong, and only the check showed it.",
 point="Clean, then count. Then check against who was invited.",
 backup=[("h", "Before cleaning"), tbl(["Skill", "Answers"], _TN_RAW), ("h", "After cleaning"), tbl(["Skill", "Answers", "People who need it"], _TN_TOP),
         ("h", "Rows to handle"), tbl(["Row ID", "What it is", "What to do"], _TN_REMOVE)],
 fallback="If Copilot in Forms is not available, use Open results in Excel. If the upload fails, show the backup tables.",
 hint="Before you trust a count, look for tests, repeats and the same answer written two ways.")

demo("tfm3", day=2, skill="2.9", sec=9, title="Analyze the 2027 responses", tool="Excel · Forms · Copilot", files=[TNR], kind="task", hands_on=True, minutes=15, solo="in pairs",
 setup=[f"Choose one. A (recommended): the practice export, {TNR}, in Excel with Copilot or in Copilot Chat. B: your own form's answers, with Copilot in Forms.",
        "A: find the rows not to count and the skills written more than one way. Change nothing yet.",
        "A: count again, cleaned. Write the top three skills with answers and people, and the answers by unit against the Invited sheet.",
        "B: on the Responses page, ask Copilot for the main needs. Check two numbers against the answers (Open results in Excel).",
        "Write your findings in five lines for the Head of L&D, starting with the DRAFT line. You use them in Task 2.10."],
 prompts=[("A · Find the problems", TNPROB)],
 stretch_prompts=[("A · Count again, cleaned", TNCLEAN)],
 expected=(f"A: two rows not counted (rows {D.TN_FIRST_ID} and {D.TN_TEST_ID}), Excel counted once, " + "; ".join(f"{s} {c} answers and {n} people" for s, c, n in _TN_TOP) +
           f"; {len(D.TN_VALID)} of {D.TN_INVITED_TOTAL} answered; {D.TN_LOW_UNIT} answered least; the personal comment left out. B: a summary where two numbers match the raw answers."),
 say="Clean, count, check. Then write what a manager needs to know.",
 point="Clean, then count. Personal comments never travel.",
 backup=[("h", "After cleaning"), tbl(["Skill", "Answers", "People who need it"], _TN_TOP), ("h", "Answers by unit"), tbl(["Unit", "Invited", "Answered"], _TN_UNITS)],
 answer=[("h", "A · Rows to handle"), tbl(["Row ID", "What it is", "What to do"], _TN_REMOVE),
         ("h", "A · The counts"), tbl(["Skill", "Before cleaning", "After cleaning", "People who need it"], [(s, str(D.TN_RAW_COUNT[s]), str(D.TN_COUNT[s]), str(D.TN_SEATS[s])) for s in D.TN_NOW]),
         ("h", "A · Answers by unit"), tbl(["Unit", "Invited", "Answered"], _TN_UNITS),
         ("h", "A · Five good findings"), ("ul", TN_FINDINGS),
         ("note", f"HR shows {D.TN_RAW_BY_UNIT['HR']} rows for 5 managers before cleaning: more answers than managers is the clue. Accept findings that keep every number, name no person and leave out row {D.TN_RED_ID}'s details. B: accept any summary where two numbers were checked against the answers.")],
 deliverable="Five lines of findings for the Head of L&D: answers and rate, the top three needs, the unit to follow up, what you left out and why.",
 fallback="If the upload fails: in Excel, filter the skill column and read every value in the list. Short of time: show the backup tables.",
 hint="A unit with more answers than managers has a problem. So does a skill written in five ways.",
 stretch=["Ask for a chart of the top five needs, cleaned, with the axis from zero. Check one bar against your count."])

DECK_PROMPT = f"Create a five-slide presentation for {D.COMPANY} line managers about the new attendance rules."
demo("d210", day=2, skill="2.10", sec=10, title="From a prompt, then from a document", tool="Copilot Chat · PowerPoint", files=[F["brief"]],
 setup=["[T] First, from a prompt only: in PowerPoint, Copilot > Create a presentation about..., with the one-line request and no file. Read the times on the slides aloud.",
        "[T] Then from a document: Create a presentation from file, and pick the brief. In Copilot Chat: attach the brief and paste the full request.",
        "[T] Put the two decks side by side. Check the times and the pilot number against the brief."],
 prompts=[("From a prompt only", DECK_PROMPT), ("From the brief", joined(DECK))],
 expected=(f"From the prompt: tidy slides with times and rules Copilot made up (often a start between 7:00 and 9:00) and no pilot result. "
           f"From the brief: five slides: why the change, the new times, permissions, the pilot result ({AT['pilot_drop']}% fewer late arrivals in {AT['pilot_weeks']} weeks), and where to send questions."),
 say="A prompt gives you a structure. A document gives you the facts. For HR slides you need both.",
 point="From a prompt: a structure. From a document: the facts. Check every number.",
 backup=[("h", "Typical outline"), ("ol", ["Why we are changing attendance rules", f"Your new day: start {AT['flex_from']} to {AT['flex_to']}, core {AT['core_from']} to {AT['core_to']}",
          f"Permissions: {AT['permissions']} a month, up to {AT['perm_hours']} hours", f"The pilot: {AT['pilot_drop']}% fewer late arrivals", "Questions: Personnel and Administration"])],
 fallback="Show the backup outline on the trainer screen.",
 hint="Which deck has times that are not in the brief?")

demo("t210", day=2, skill="2.10", sec=10, title="From a prompt, then from your findings", tool="Copilot Chat · PowerPoint", files=[TNR], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["From a prompt: ask PowerPoint (or Copilot Chat) for five slides on Mutla's 2027 training needs, with no file. Circle every number it made up.",
        "From a document: paste your five findings from Task 2.9 into a Word file and save it. Create a presentation from it, or ask Copilot Chat for a five-slide outline with speaker notes.",
        "Check every number on every slide against your findings. No comment from a manager goes on a slide. Delete the first deck."],
 prompts=[],
 expected=("The prompt-only deck has needs and numbers Copilot made up. The deck from the findings shows " + f"{len(D.TN_VALID)} of {D.TN_INVITED_TOTAL} answers, " +
           "; ".join(f"{s} {c} answers and {n} people" for s, c, n in _TN_TOP) + f", {D.TN_LOW_UNIT} to follow up, and the next step, every number matching the findings."),
 say="Fast to make, quick to check. Read every number once.",
 point="Every number on a slide matches the findings.",
 backup=[("h", "The findings every slide must match"), ("ul", TN_FINDINGS)],
 answer=[("h", "Facts to check"), ("ul", [f"{len(D.TN_VALID)} of {D.TN_INVITED_TOTAL} managers answered ({D.TN_RATE}%).", "The top three needs, cleaned: " + ", ".join(f"{s} ({c}, {n} people)" for s, c, n in _TN_TOP) + ".",
          f"{D.TN_LOW_UNIT}: {D.TN_BY_UNIT[D.TN_LOW_UNIT]} of {D.TN_INVITED[D.TN_LOW_UNIT]} answered.", "No names, no employee codes and no comment from a manager on any slide."])],
 deliverable="Five slides, or a five-slide outline, each number checked against your findings.",
 fallback="Without Copilot in PowerPoint, the outline from Copilot Chat is enough. No findings from Task 2.9: use the findings on the trainer screen.",
 hint="Check the top three and the response rate on every slide where they appear.")

DECK_EDIT = five([["Task", "In the deck you just made, add a slide after slide 2 called \"What changes for managers\" with three bullets. Then rewrite slide 4 in plain English for line managers. Then add two sentences of speaker notes to every slide."],
                  ["Constraints", "Use only the facts already in the deck and the brief. Change no date, time or number."],
                  ["Output format", "Short bullets, no more than eight words each."]])
demo("d211", day=2, skill="2.11", sec=10, title="Edit a deck with Copilot", tool="PowerPoint · Copilot Chat", files=[F["brief"]],
 setup=["[T] Stay in the deck from Demo 2.10. Open Copilot in PowerPoint. (Without it: paste the outline into Copilot Chat with the same request.)",
        "[T] Paste the edit request. Show the new slide, the rewritten slide and the notes.", "[T] Use Designer for a layout if it is available. Then check every number on screen against the brief."],
 prompts=[("Edit the deck", joined(DECK_EDIT))],
 expected=f"A new slide 3 with three bullets for managers, a plainer slide 4, and speaker notes on every slide. The times ({AT['flex_from']} to {AT['flex_to']}) and the pilot result ({AT['pilot_drop']}%) are unchanged.",
 say="The first draft is the easy part. Most of the work in a deck is the second round: a missing slide, a slide for a different reader, the notes.",
 point="Edit in rounds. Check every number after each round.",
 backup=[("h", "What the edits look like"), ("ul", ["Slide 3: What changes for managers (three bullets).", "Slide 4: the same facts in shorter, plainer words.", "Speaker notes: two sentences on every slide."])],
 fallback="Show the backup on the trainer screen. Without Copilot in PowerPoint, run the request in Copilot Chat on the outline.",
 hint="Did any time or number change during the edits?")

demo("t211", day=2, skill="2.11", sec=10, title="Fix a messy deck, or build your own", tool="PowerPoint · Copilot Chat", files=[F["messydeck"]] + CASE_FILES, kind="task", hands_on=True, minutes=18, solo="on your own",
 setup=["Choose one. A: fix the messy Q3 HR update. B: slides for your track's meeting, from your Task 2.1 agenda and brief.",
        "A: delete the About box on slide 1. Ask Copilot for a fix list, slide by slide. Then fix in rounds: merge, cut text, remove personal data, add notes.",
        "A: check every number against your checked figures and the brief. Mark anything with no source.",
        "B: four slides with speaker notes, and one slide that asks the open question. Check every date and number against the case file."],
 prompts=[],
 stretch_prompts=[("A · A fix list, slide by slide", "Review the attached deck slide by slide. For each slide, list what to fix: too much text, a repeated slide, a number with no source, personal data, and missing speaker notes. Do not change anything yet.")],
 expected=(f"A: nine slides become eight: one training slide with {D.TRAIN_TRUE}, no names or salaries, the pilot at {AT['pilot_drop']}% for one division, owners or [to confirm] on the next steps, and speaker notes throughout. "
           "B: a deck that follows the agenda, a slide that asks the open question, speaker notes, and every date and number as in the case file."),
 say="Most decks you get at work are not new. Someone made them in a hurry, and you have to fix them. Or you build your own meeting's slides from this morning's work.",
 point="Fix in rounds. Check every number after each round.",
 backup=[("h", "A · What to fix in the messy deck"), tbl(["Slide", "Problem", "Fix"], D.MESSY_FIXES), ("h", "B · The open question in each case")] + [("p", f"<b>{n}:</b> {OPENQ[k]}") for k, n in D.TRACKS],
 answer=[("h", "A · The planted problems"), tbl(["Slide", "Problem", "Fix"], D.MESSY_FIXES),
         ("h", "B · Check the slides for"), ("ul", ["They follow the agenda from Task 2.1.", "The open question is asked, not answered.", "Every date and number matches the case file.", "Job Evaluation: no grade on any slide."])],
 deliverable="A: the fixed deck, with notes on every slide. B: four or five slides with speaker notes for your track's meeting.",
 fallback="Without Copilot in PowerPoint: A, paste the fix list from Copilot Chat and edit by hand. B, ask Copilot Chat for the outline first.",
 hint="A: which slides say the same thing? B: which question is not decided yet?",
 stretch=[f"Turn the onboarding checklist ({F['onboard']}) into a five-slide welcome deck for new joiners."])

# ===================================================================== DAY 3 · HR Agents and an Introduction to Power Automate
AGENT = five([["Role", f"You are {D.AGENT_NAME}, an assistant for {D.COMPANY} employees."],
         ["Context", "Employees ask about leave, allowances, attendance and training. Authorized HR staff decide every case."],
         ["Task", "Answer each question from the knowledge files, with the policy name and section."],
         ["Data", f"Use only the five knowledge files. Allowances: version 3 applies until 31 December 2026; version 4 applies from {D.ALLOW_V4_DATE}. Give today's rule first, then the change and its date."],
         ["Constraints", "Never give or guess the salary, allowance or personal data of a named person. Never decide a case. If the answer depends on the person's grade or situation, ask first. If the files do not answer it, say so and refer the person to the right HR unit."],
         ["Tone", "Polite, short, plain English."],
         ["Output format", "Two to four sentences, then the source: policy name and section."]])
STARTERS = D.AGENT_STARTERS
COACH = five([["Role", f"You are {D.COACH_NAME}. You help {D.COMPANY} HR staff and line managers draft job descriptions."],
         ["Context", "The drafts go to the Job Evaluation committee, which sets the level and the grade."],
         ["Task", "Draft a job description from the duties the user gives you, in the 2026 template's order."],
         ["Data", "Use the 2026 template and the job evaluation factors file in your knowledge, and only the duties the user gives."],
         ["Constraints", "If the user gives no duties, ask for them before you write. Add no duty, team size, grade or salary. If asked about a grade, say the Job Evaluation committee decides and refer the user to Job Evaluation and Salary Scaling."],
         ["Tone", "Formal, neutral, plain English."],
         ["Output format", f"The template's headings in order, with the grade line blank. Start with: {DL}"]])
BUDDY = five([["Role", f"You are the {D.BUDDY_NAME}. You help new joiners at {D.COMPANY} in their first month."],
         ["Context", "New joiners ask practical questions before and after their first day. Personnel and Administration owns the onboarding checklist."],
         ["Task", "Answer each question from the onboarding checklist, with the section."],
         ["Data", "Use only the onboarding checklist in your knowledge."],
         ["Constraints", "If the answer depends on where the person works (head office or a field site), ask first. Never answer about salary, grade, allowance amounts or contract terms: refer the person to Personnel and Administration or Compensation. If the checklist does not answer it, say so and name the unit to ask."],
         ["Tone", "Friendly, short, plain English."],
         ["Output format", "Two to four sentences, then the checklist section."]])
KNOW = [F["leave"], F["v3"], F["v4"], F["attendance"], F["training"]]

# Block 1 · built-in agents (Prompt Coach for everyone; Researcher and Analyst need the Microsoft 365 Copilot license)
COACH_ASK = (f"Here is a request I use at work: \"{D.BUILTIN_WEAK}\" Review it. Tell me what is missing, "
             f"then suggest a better request for an HR officer at {D.COMPANY}.")
COACH_BETTER = five([["Role", f"You are an L&D officer at {D.COMPANY}."],
         ["Context", "Line managers must nominate staff for the January courses. Many forget the deadline."],
         ["Task", "Write a short reminder email to line managers."],
         ["Data", "Use only the course list and the nomination deadline I paste below."],
         ["Constraints", "No employee names. Do not promise anyone a place: L&D confirms places."],
         ["Tone", "Polite and short."],
         ["Output format", "A subject line and at most 120 words, with the deadline in the first sentence."]])
demo("d30", day=3, skill="3.1", sec=12, title="Two built-in agents, live", tool="Copilot Chat · Agents",
 setup=["[T] In Microsoft 365 Copilot, open Agents, then All agents. Show the Built by Microsoft list for ten seconds.",
        "[T] Open Prompt Coach. Paste the first request below. Read its feedback aloud: which checklist parts does it say are missing?",
        "[T] Copy the better request it suggests and run it in Copilot Chat. Compare the two answers in one sentence.",
        "[T] Open Researcher. Paste the research question. While it works (a few minutes), go back to the slides.",
        "[T] Open the report. Click two sources and check one fact in each against the report."],
 prompts=[("Prompt Coach · review a weak request", COACH_ASK), ("Researcher · a public HR question", D.BUILTIN_RESEARCH)],
 expected="Prompt Coach says the request has no context, data, constraints or format, asks a question or two, and suggests a fuller request. Researcher returns a report with numbered sources after a few minutes. The trainer opens two sources and checks one fact in each.",
 say="Microsoft already built some agents for you. Each one is Copilot with saved instructions for one job. You still check what comes back.",
 point="Built-in agents save you the instructions. They do not save you the check.",
 backup=[("h", "Built-in agents in Microsoft 365 Copilot"), tbl(["Agent", "What it does", "Try it on", "Who has it"], D.BUILTIN),
         ("h", "A better version of the weak request"), tbl(["Part", "Request"], COACH_BETTER)],
 fallback="If Prompt Coach is not in the list, paste the same request into Copilot Chat and add: answer as a prompt coach. If Researcher is missing (no license), ask Copilot Chat the research question and ask for a source for each point.",
 hint="Which of the five checklist parts does Prompt Coach say are missing?")

demo("t30", day=3, skill="3.1", sec=12, title="Use an agent Microsoft built", tool="Prompt Coach, and Researcher if you have it", kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["In Microsoft 365 Copilot, open Agents, then All agents. Find Prompt Coach under Built by Microsoft. If you see Add, add it.",
        "Give Prompt Coach one request from your Prompt Bank (Day 1), or the weak request below. Read what it says is missing.",
        "Run its better request in Copilot Chat. Is the answer better? Save the best version in your Prompt Bank.",
        "If you have Researcher, ask it the research question below. When the report is ready, open two sources and check one fact in each."],
 prompts=[("Prompt Coach · review my request", COACH_ASK), ("Researcher · a public HR question", D.BUILTIN_RESEARCH)],
 expected="A better request in the Prompt Bank, with the missing parts added: context, data, constraints and format. With Researcher: a report with sources, and two facts checked against their sources.",
 say="Use the agent, then judge it. Did it make your request better? Can you trace each fact to a source you opened?",
 point="A better request in your Prompt Bank. Two sources checked.",
 backup=[("h", "A better version of the weak request"), tbl(["Part", "Request"], COACH_BETTER)],
 answer=[("h", "A good result"), ("ul", ["Prompt Coach names what is missing: who it is for, the facts, the limits and the format.",
                                         "The better request has all five checklist parts and no real names or data.",
                                         "Researcher: every point you keep has a source you opened. Remove any point with no source."]),
         ("h", "A better version of the weak request"), tbl(["Part", "Request"], COACH_BETTER)],
 deliverable="One improved request saved in your Prompt Bank and, with Researcher, two checked sources.",
 fallback="No Prompt Coach: paste the request into Copilot Chat and add: answer as a prompt coach. No Researcher: ask Copilot Chat the research question and ask for a source for each point.",
 hint="Put the better request next to the five checklist parts. Which part did your first request miss?",
 stretch=["Ask Prompt Coach what good instructions for an HR policy agent must say. Keep the answer for Task 3.2."])

demo("d31", day=3, skill="3.2", sec=13, title="An HR agent, built live", tool="Agent Builder", files=KNOW,
 setup=["[T] In Microsoft 365 Copilot, choose Create agent. Open the Configure tab.", f"[T] Name: {D.AGENT_NAME}. Description: answers staff questions from Mutla's HR policies.",
        "[T] Paste the instructions. Read the five parts aloud as you scroll.", "[T] Under Knowledge, upload the five policy files. Add the three starter prompts.",
        "[T] In the test pane, ask the first starter prompt. Point to the section number in the answer.",
        "[T] Say: Prompt Coach was built the same way, with instructions and a name. Microsoft offers it as a template in Agent Builder too."],
 prompts=[("Instructions", joined(AGENT))] + [(f"Starter prompt {i}", q) for i, q in enumerate(STARTERS, 1)],
 expected=f"An agent with a name, a description, instructions in five parts, five knowledge files and three starter prompts. In the test pane it answers the carry-over question: up to {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']}, leave policy section 4.",
 say="An agent is a saved set of instructions with its own files. You write the instructions once; everyone who uses it gets the same rules.",
 point="Instructions, knowledge, starter prompts. Then test.",
 backup=[("h", "What the agent holds"), tbl(["Part", "What goes in"], [("Name", D.AGENT_NAME), ("Instructions", "The five checklist parts"), ("Knowledge", ", ".join(KNOW)), ("Starter prompts", " · ".join(STARTERS))])],
 fallback="If Agent Builder is off on the account, paste the same instructions into Copilot Chat, attach the five files, and ask the same question.",
 hint="Watch where each checklist part goes in the instructions.")

demo("t32", day=3, skill="3.2", sec=13, title="Write and build your agent", tool="Word, then Agent Builder", files=KNOW, kind="task", hands_on=True, minutes=20, solo="on your own",
 setup=[f"In a blank document, write the instructions for {D.AGENT_NAME} with the five checklist parts: which files it uses, the dates of the two allowances versions, what it never answers, when it asks first, and where it refers people.",
        "In Microsoft 365 Copilot, choose Create agent, then the Configure tab. Add a name, a one-line description and your instructions.",
        "Upload the five policy files under Knowledge. Add three starter prompts.", "Ask one normal question in the test pane. Does the answer give the section?"],
 prompts=[(f"Starter prompt {i}", q) for i, q in enumerate(STARTERS, 1)],
 expected="Instructions in five parts: answer only from the five files with the section; v3 until 31 December 2026 and v4 from 1 January 2027; ask for the grade first when it matters; never a named person's pay or data; refer anything else to the right HR unit. A saved agent with five knowledge files and three starter prompts that answers a normal question with the policy name and section.",
 say="The instructions are the agent's job description. Write them first, then build. Vague instructions give a vague agent.",
 point="What it answers, from which files, what it never answers, and where it refers.",
 backup=[("h", "What the instructions must cover"), ("ul", ["Only the five knowledge files, with the section.", "The two allowances versions and their dates.", "Ask first when the answer depends on the person.", "Never a named person's pay or data. Never decide a case.", "Refer to the right HR unit."]),
         ("h", "The parts of the agent"), tbl(["Part", "What goes in"], [("Name", D.AGENT_NAME), ("Knowledge", ", ".join(KNOW)), ("Starter prompts", " · ".join(STARTERS))])],
 answer=[("h", "A model set of instructions"), tbl(["Part", "Instructions"], AGENT),
         ("h", "Check the agent for"), ("ul", ["Five knowledge files uploaded.", "Three starter prompts that staff would really ask.", "A normal question answered with the policy name and section."])],
 deliverable="A saved agent with your instructions, five knowledge files and three starter prompts, that answers a normal question with its source.",
 fallback="No Agent Builder: paste your instructions into a new Copilot Chat, attach the five files, and test there. Or pair with a neighbor who has it. Short of time: use the instructions from the Day 3 lab page and change one line.",
 hint="Constraints hold the rules that protect people: never, ask first, refer. No section number in the answer? Check the Format line.")

demo("d33", day=3, skill="3.3", sec=13, title="Three tests, then one fix", tool="Agent Builder",
 setup=["[T] In the test pane, ask the three test questions one by one.", "[T] When one fails, find the instruction line that should have stopped it. Change that line only.",
        "[T] Ask the same question again. Show that it passes now."],
 prompts=[(f"Test · {a}", b) for a, b, _c, _d in D.AGENT_TESTS],
 expected="The normal question gets the rule and section 4. The incomplete question gets a question back about the grade, or both versions with dates. The sensitive question is declined and referred.",
 say="Build, test, fix one line, test again. That loop is the whole skill.",
 point="Normal, incomplete, sensitive. Fix one line at a time.",
 backup=[("h", "The three tests"), tbl(["Test", "Question", "A pass looks like", "Result"], D.AGENT_TESTS)],
 fallback="If the agent passes every test first time, ask the sensitive question in a softer way and show what it does.",
 hint="Which instruction line should have stopped the wrong answer?")

demo("t33", day=3, skill="3.3", sec=13, title="Test and fix your agent", tool="Agent Builder", files=KNOW, kind="task", hands_on=True, minutes=10, solo="on your own",
 setup=["Ask your agent the three test questions below.", "Write a test log: question, answer, pass or fix.", "Fix one instruction line that failed, update the agent, and test again."],
 prompts=[(f"Test · {a}", b) for a, b, _c, _d in D.AGENT_TESTS],
 expected="A three-line test log. The agent cites section 4, asks for the grade (or gives both versions with dates) before the transport answer, and declines the named salary.",
 say="A test you did not run is a problem a colleague finds later.",
 point="Three tests, one log, one fix.",
 backup=[("h", "The three tests"), tbl(["Test", "Question", "A pass looks like", "Result"], D.AGENT_TESTS)],
 answer=[("h", "Pass marks"), tbl(["Test", "Question", "A pass looks like", "Result"], D.AGENT_TESTS), ("h", "Finished early: the fourth test"), tbl(["Test", "Question", "A pass looks like"], [D.AGENT_TEST4])],
 deliverable="A three-line test log and one fixed instruction.",
 fallback="No Agent Builder: run the tests in the Copilot Chat with your instructions and the five files.",
 hint="If it answers the salary question, make the Constraints line say never, and refer.",
 stretch=["Run a fourth test with a question the files do not cover. It must say so and refer."],
 stretch_prompts=[("Test 4 · Out of scope", D.AGENT_TEST4[1])])

demo("t34", day=3, skill="3.4", sec=13, title="Optional: a second agent", tool="Agent Builder", files=[F["tpl"], F["factors"], F["onboard"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=[f"Choose one. The {D.COACH_NAME.replace('Mutla ', '')} helps line managers draft job descriptions. The {D.BUDDY_NAME.replace('Mutla ', '')} answers new joiners from the onboarding checklist.",
        "Write its instructions with the checklist. Knowledge: the 2026 template and the evaluation factors, or the onboarding checklist.",
        "Run its three tests (on the prompt sheet and the Day 3 lab page) and log them.", "Fix one line if a test fails, and test again."],
 prompts=[("Coach: three tests, one at a time", " | ".join(b for _a, b, _c, _d in D.COACH_TESTS)), ("Buddy: three tests, one at a time", " | ".join(b for _a, b, _c, _d in D.BUDDY_TESTS))],
 expected="A second agent that drafts or answers only from its knowledge, asks first when the question leaves something out, and refers grades, salaries and allowances to the right unit.",
 say="Same method, a different job. Pick the agent your unit would use first.",
 point="Ask first, add nothing, refer the personal questions.",
 backup=[("h", "Job Description Coach: three tests"), tbl(["Test", "Question", "A pass looks like", "Result"], D.COACH_TESTS),
         ("h", "Onboarding Buddy: three tests"), tbl(["Test", "Question", "A pass looks like", "Result"], D.BUDDY_TESTS)],
 answer=[("h", "Job Description Coach: model instructions"), tbl(["Part", "Instructions"], COACH), ("h", "Pass marks"), tbl(["Test", "Question", "A pass looks like", "Result"], D.COACH_TESTS),
         ("h", "Onboarding Buddy: model instructions"), tbl(["Part", "Instructions"], BUDDY), ("h", "Pass marks"), tbl(["Test", "Question", "A pass looks like", "Result"], D.BUDDY_TESTS)],
 deliverable="A second agent and a three-line test log.",
 fallback="Short of time: skip it in class and build it at work this week. The tests are on the Day 3 lab page.",
 hint="The incomplete test leaves something out. What must your agent ask before it answers?")

def _vsteps(flow): return "; ".join(f"{a.lower()}: {c}" for a, _b, c, _d in flow)
def _vparts(k): return tbl(["Part", "Means", "In this flow"], [(a, m, x) for a, m, x in zip(D.PA_PARTS, D.PA_MEANS, D.PA_DEMOS[k]["parts"])])
VIDFALL = "If the video does not play, open it from the Day 3 page (sample files) or the USB stick. If that fails too, walk through the four parts on the slide and the step table in the backup."
demo("d35", day=3, skill="3.5", sec=14, title="A training request approval (recorded flow)", tool="Power Automate · recorded demo", files=[F["vid1"], F["palog"]],
 setup=["[T] Click play on the video (no sound). Pause on each step card and name the part: trigger, action, connector, output.",
        "[T] Pause after Start and wait for an approval. Ask the room which step a person does.",
        "[T] Play to the end: the run took seconds except the approval. Point to the new Excel row and the email."],
 prompts=[],
 expected="The steps: " + _vsteps(D.PA_FLOW) + ". One form response becomes one approval, one row in the log and one email. The approver decides; the flow only carries the request.",
 say="A flow starts on its own and does the same steps every time. When a decision is needed, it stops and waits for a person.",
 point="The flow carries the request. A person decides.",
 backup=[("h", "The four parts"), _vparts(0), ("h", "The flow, step by step"), tbl(["Step", "Connector", "What it does"], [(f"{a}: {c}", b, d) for a, b, c, d in D.PA_FLOW]),
         ("h", "The log"), tbl(D.PA_LOG_HEAD, D.PA_LOG)],
 fallback=VIDFALL,
 hint="Which step needs a person? Which steps happen the same way every time?")

demo("d35b", day=3, skill="3.5b", sec=14, title="Weekly training demand to a vendor brief (recorded flow)", tool="Power Automate · recorded demo", files=[F["vid2"]],
 setup=["[T] Click play. Pause on the schedule: this flow starts on a date, not an event.",
        "[T] Pause on Create CSV table: the flow keeps only four columns, so the AI step sees only what it needs.",
        "[T] Pause on Run a prompt: AI is one step inside the flow. Play to the email: DRAFT for review, in L&D's inbox."],
 prompts=[],
 expected="The steps: " + _vsteps(D.PA_FLOW2) + ". Every Sunday at 8:00, L&D gets a draft that groups the week's training demand and outlines what to ask vendors for. Nothing goes to a vendor on its own.",
 say="A flow can start on a schedule, and one of its steps can be AI. The AI drafts the brief; a person in L&D checks it and decides what goes out.",
 point="AI drafts inside the flow. L&D decides.",
 backup=[("h", "The four parts"), _vparts(1), ("h", "The flow, step by step"), tbl(["Step", "Connector", "What it does"], [(f"{a}: {c}", b, d) for a, b, c, d in D.PA_FLOW2])],
 fallback=VIDFALL,
 hint="What starts this flow? Who reads the draft before a vendor sees it?")

demo("d35c", day=3, skill="3.5c", sec=14, title="A vendor quotation, read and scored (recorded flow)", tool="Power Automate · recorded demo", files=[F["vid3"]],
 setup=["[T] Click play. Pause on the quotation email: price, dates, duration and learners, all inside one long message.",
        "[T] Pause on Run a prompt: the AI reads the offer and this term's requests, then scores the fit against " + str(len(D.PA_GOALS)) + " company goals.",
        f"[T] Pause on the Excel row: {D.PA_QUOTE['total']:,} KWD for {D.PA_QUOTE['learners']} learners is {D.PA_QUOTE['per']} KWD each, so the score is {D.PA_QUOTE['score']} out of 10. Status: {D.PA_QUOTE['status']}.",
        "[T] Play to the DRAFT email. Say: the flow does not answer the vendor. L&D decides."],
 prompts=[],
 expected="The steps: " + _vsteps(D.PA_FLOW3) + f". The fictional offer from {D.PA_QUOTE['vendor']} ({D.PA_QUOTE['course']}, {D.PA_QUOTE['duration']}, {D.PA_QUOTE['dates']}) becomes one row with a score of {D.PA_QUOTE['score']} out of 10: {D.PA_QUOTE['per']} KWD per learner is above the 150 KWD goal.",
 say="The flow does the copying: it reads the offer, pulls out the numbers and puts them in a row. The score helps L&D compare offers. L&D still decides.",
 point="AI reads and scores. L&D decides.",
 backup=[("h", "The four parts"), _vparts(2), ("h", "The flow, step by step"), tbl(["Step", "Connector", "What it does"], [(f"{a}: {c}", b, d) for a, b, c, d in D.PA_FLOW3]),
         ("h", "The goals the AI scores against"), ("ul", D.PA_GOALS),
         ("h", "The row it adds"), tbl(["Vendor", "Course", "Total", "Learners", "Per learner", "Duration", "Dates", "Score", "Status"],
                                       [(D.PA_QUOTE["vendor"], D.PA_QUOTE["course"], f"{D.PA_QUOTE['total']:,} KWD", D.PA_QUOTE["learners"], f"{D.PA_QUOTE['per']} KWD", D.PA_QUOTE["duration"], D.PA_QUOTE["dates"], f"{D.PA_QUOTE['score']} / 10", D.PA_QUOTE["status"])])],
 fallback=VIDFALL,
 hint="Which number made the score low? Who decides which vendor to use?")

demo("d36", day=3, skill="3.6", sec=15, title="A story into a step table", tool="Copilot Chat",
 setup=["[T] Open a new Copilot Chat. Paste the request: the story is inside it.", "[T] Read the table aloud. Ask the room which problem Copilot missed, if any.",
        "[T] Point out that Copilot flags the problems and does not fix them."],
 prompts=[("Map a story", joined(MAPREQ))],
 expected="Five or six steps. Delay: the manager's approval after three days. Duplicated effort: prices copied by hand, then asked for again by Procurement. Unclear ownership: nobody tells the trainer the room. A person decides: the manager approves the choice.",
 say="First we see the process as it really is. We improve it after we can see it.",
 point="Map it as it is. Flag the problems. Do not fix them yet.",
 backup=[("h", "Typical step table"), tbl(["Step", "Who", "Problem", "A person decides?"], [("1 Ask three providers for prices", "Coordinator", "", ""), ("2 Copy prices into a spreadsheet", "Coordinator", "Repetitive step", ""),
         ("3 Approve the choice", "Manager", "Delay (3 days)", "Yes"), ("4 Send to Procurement; prices asked again", "Coordinator, Procurement", "Duplicated effort", ""), ("5 Tell the trainer the room", "Nobody", "Unclear ownership", "")])],
 fallback="Show the backup table on the trainer screen.",
 hint="A step nobody owns is still a step.")

demo("t36", day=3, skill="3.6", sec=15, title="Map the training request", tool="Copilot Chat + Word", files=[F["stories"], F["maptpl"]], kind="task", hands_on=True, minutes=12, solo="in pairs",
 setup=["Open the process stories file. Read story 1, the training request.", "Run the request below to draft the step table.",
        "Check it by hand against the story. Add any step or problem Copilot missed.", "Copy the final table into the map template."],
 prompts=[("Map story 1", joined(MAP_FILE))],
 expected="About nine steps. Delays: the manager (4 to 6 days) and L&D (up to a week). Duplicated effort: printing, scanning and typing twice. Repetitive step: sending the Word form each time. Unclear ownership: nobody chases late approvals. A person decides: the line manager and L&D.",
 say="Copilot drafts the map. You know the work, so you check it.",
 point="Map it as it is. Mark the problems and the human decisions.",
 backup=[("h", "The map of story 1"), tbl(D.MAP_COLS, L["map"])],
 answer=[("h", "The map of story 1"), tbl(D.MAP_COLS, L["map"]), ("note", "The step nobody owns (chasing late approvals) is the one most maps miss. Count it as a step.")],
 deliverable="A step table of the training request, with problems and human decisions marked.",
 fallback="If Copilot is slow, map the story by hand in the template.",
 hint="Find the step that nobody owns.",
 stretch=["Count the days from the request to the decision in the worst case."])

demo("t37", day=3, skill="3.7", sec=15, title="Map your own HR process", tool="Copilot Chat + Word", files=[F["stories"], F["maptpl"]], kind="task", hands_on=True, minutes=20, solo="on your own",
 setup=["Choose: your track's story (stories 2 to 5) or a process from your own work. For your own work, write the story with roles only: no names, no real data.",
        "Write your own checklist request to turn the story into a step table. Flag the problems; do not fix them.",
        "Check the table by hand. Mark every step where a person must decide.", "Save the map. If there is time, you improve it in Task 3.8."],
 prompts=[],
 expected="A step table from request to completion with an owner for each step, the waits, the four kinds of problem flagged and the human decisions marked.",
 say="Map your own process now. If there is time, you improve it in the next task.",
 point="From request to completion. Owners, waits, problems, human decisions.",
 backup=[("h", "Stories 2 to 5")] + [("p", f"<b>Story {i}: {D.STORIES[k]['title']}</b> ({D.STORIES[k]['owner']})") for i, k in enumerate(["pa", "cmp", "mp", "je"], 2)],
 answer=[("h", "What each story hides")] + [x for k in ("pa", "cmp", "mp", "je") for x in (("p", f"<b>{D.STORIES[k]['title']}</b>"), ("ul", D.STORY_KEY[k]))],
 deliverable="A map of one HR process, with problems and human decisions marked.",
 fallback="Short of time: map the first five steps well.",
 hint="Start where the request starts, and stop when the requester has the result.")


demo("t38", day=3, skill="3.8", sec=15, title="Optional: improve your map", tool="Word + Copilot Chat or Agent Builder", files=[F["card"]], kind="task", hands_on=True, minutes=25, solo="on your own",
 setup=["Mark each step on your map: Person, Copilot or Agent. Keep every approval and decision with a person.", "Remove at least two problems you flagged. Give every step one owner.",
        "Fill in the workflow card. Run the check request below, then check the card yourself.", "If time is left: build the piece for one Copilot or Agent step, and test it once."],
 prompts=[("Check my card", "Check the attached workflow card. List any step with no owner, any decision that is given to Copilot or an agent instead of a person, and any problem from the map that is still in the process. Do not rewrite the card.")],
 expected="A workflow card: every step marked Person, Copilot or Agent with one owner, every decision with a person, two problems removed, and, if time allows, one tested piece.",
 say="Fix the process first. Copilot and agents only make a slow process faster if the steps make sense.",
 point="One owner per step. Every decision with a person.",
 backup=[("h", "The filled-in example: a training request"), tbl(["Card line", "Example"], list(zip(D.CARD_FIELDS, D.CARD_EXAMPLE)))],
 answer=[("h", "A strong card has"), ("ul", ["Every step marked Person, Copilot or Agent, with one owner.", "Every approval and decision with a person.", "At least two problems from the map removed.", "No real names or real data."]),
         ("h", "The example card"), tbl(["Card line", "Example"], list(zip(D.CARD_FIELDS, D.CARD_EXAMPLE)))],
 deliverable="An improved workflow card for your process.",
 fallback="Short of time: skip this task and go to the comparison. The trainer decides.",
 hint="Start with the steps you marked as a problem. Which can disappear, and which can Copilot or an agent help with?")

TOOL_SORT = [("Draft a one-off reply to an employee's complaint", "copilot"), ("Answer the same leave questions for 300 employees", "agent"),
             ("Log every training request and send it for approval", "flow"), ("Summarize this week's meeting transcript", "copilot"),
             ("Help line managers write job descriptions in the template", "agent"), ("Send a reminder 2 days before each nomination deadline", "flow"),
             ("Rewrite an announcement for senior leadership", "copilot"), ("Copy each approved claim into the payroll change list", "flow")]
TOOL_LABELS = {"copilot": "Copilot Chat", "agent": "An agent", "flow": "A flow"}
demo("d39", day=3, skill="3.9", sec=16, title="Copilot, an agent or a flow?", tool="Card sort", kind="sort",
 setup=["[T] Read each card aloud. The room calls Copilot, agent or flow, then tap the card."],
 prompts=[], expected="Copilot Chat: one-off drafts and summaries. An agent: the same questions or the same kind of draft for many people. A flow: the same steps every time something happens.",
 say="One-off writing: Copilot. The same questions again and again: an agent. The same steps every time: a flow.",
 point="Who asks, how often, and does it move work between people?",
 backup=[("h", "The card sort answers"), tbl(["Task", "Tool"], [(t, TOOL_LABELS[k]) for t, k in TOOL_SORT])],
 fallback="If the slide fails, read the cards from the backup table and ask for a show of hands.", hint="How often does it happen, and who starts it?")

# ===================================================================== the weak and strong opener (Day 1)
SHOWCASE = {
 "eyebrow": "Opener · one job description", "title": "One role, <span class=\"hl\">two requests.</span>", "tool": "Copilot Chat", "file": F["roles"],
 "weak": f"Write a job description for a {R['title'].lower()}.",
 "weak_answer": ["Leads a team of compensation analysts.", "Designs reward strategy and advises the Board.", "Grade: senior. Competitive package."],
 "weak_flags": ["Invented duties", "Invented team and grade", "Not Mutla's template"],
 "parts": JD_CMP,
 "table": [["Part", "Weak request", "Five inputs"], ["Duties", "Invented", "The role sheet's six"], ["Team size", "\"Leads a team\"", "None"], ["Grade", "\"Senior\"", "Blank, for the committee"]],
 "strong_answer": [f"<b>{R['title']}</b> · {R['unit']} · reports to the {R['reports']}.", f"<b>Purpose:</b> {R['purpose']} <b>Grade:</b> blank, for the committee."],
 "strong_flags": ["Mutla's template", "Duties from the role sheet", "Ready after a check"],
 "score": [["Follows the template?", "No", "Yes"], ["Duties traceable?", "No", "Every one"], ["Ready for the committee?", "Start again", "After a check"]],
 "punch": "The request decides the answer.", "punch_sub": "Same tool, same role. The only difference is what you gave Copilot.",
}

AI_DEMOS = [k for k, v in DEMOS.items() if v.get("kind") in ("player", "showcase")]

# ===================================================================== Day 2 demo runbook guide (Aya, 18 Nov 2026): what each demo must prove,
# a short script with stage directions in brackets, and questions for the room with what to listen for. Shown on the staff runbook only.
RUNGUIDE = {
 "d22": {"prove": "Copilot prepares a meeting page in a minute, but only from the facts you give it. The trainer still checks the minutes, the owners and where the open question went.",
         "script": ["(Show the request on screen.) Before a meeting I need three things: an agenda, a short brief and the questions we must discuss. The facts are inside my request, and nothing else.",
                    "(Run it.) Under a minute. Now my part starts.",
                    "(Add the minutes aloud.) Do they add up to 30? (Point to each owner.) Is every owner in the facts?",
                    "(Point to the discussion points.) The Medical Services question is something to discuss. Copilot did not decide it for us."],
         "discuss": [("Which of your regular meetings has no agenda today?", "Weekly unit meetings, committee meetings, meetings called the same day."),
                     ("What would you never put in a brief that goes to everyone at the meeting?", "Names in a case, salaries, a decision that is not made yet.")]},
 "d23": {"prove": "A recap holds only what people agreed. An idea nobody agreed is not an action, and a missing deadline stays missing.",
         "script": ["(Paste the request with the notes.) These are rough notes, the kind we all write.",
                    "(Run it. Read the action table aloud.) Four actions. One says: no deadline set. That is honest, and it is right.",
                    "(Find the CEO line in the notes.) Somebody had an idea. Nobody agreed. It is not in the table, and if it were, I would delete it."],
         "discuss": [("Who writes the recap in your team today, and how long after the meeting does it go out?", "Often nobody, or days later. That is the gap Copilot closes."),
                     ("What happens when a recap gives someone a task they never agreed to?", "People argue about the recap instead of doing the work.")]},
 "d24": {"prove": "Copilot in Outlook reads the whole thread, but it can still pick an old date. You check every owner and date against the latest message before you send.",
         "script": ["(Open the training mailbox in Outlook and the thread Orientation day for new joiners, Sunday 6 December. Without the mailbox, go back to the chat from Demo 2.2.)",
                    "(Select Summarize.) Read the summary with me. Which date does it give for the laptops? (The thread says 1 December first, then 2 December.)",
                    "(Check the briefing time: 9:00 to 11:00 moved to 8:30 to 10:30. Check the open question: which 6 new joiners come on Monday 7 December.)",
                    "(Find the action that hides in an older message: Fatma sends IT the list of new joiners by Thursday 26 November. Did the summary catch it?)",
                    "(Reply to Noura with Draft with Copilot, or paste the follow-up request in Copilot Chat.) A follow-up with the action table, then a short reminder. Read every owner and date before Send."],
         "discuss": [("Which of your email threads would you most like Copilot to summarize?", "Long approval threads, threads with many people, threads where a date changed."),
                     ("When is a reminder too early, and when is it too late?", "Two days before the deadline is polite. After the deadline, add the reason and keep it polite."),
                     ("The summary gave the old laptop date. Whose mistake is it if the email goes out?", "Ours. Copilot drafts; the sender checks.")]},
 "d26": {"prove": "Copilot can count every row correctly and still give the wrong total, because the rows themselves were wrong. Only a check against a reference shows it.",
         "script": ["(Attach the trackers file and run the count request.) Copilot counts " + str(D.TRAIN_ROWS_EXPORT) + " rows. It did not make a mistake.",
                    "(Open the Control totals sheet.) The HR system says " + str(D.TRAIN_TRUE) + ". Which number goes in the report?",
                    "(Run the chart request.) Every unit is a little too high, not one unit. What kind of problem does that? (Wait for: duplicates.)",
                    "(Point to the axis.) It starts at zero, so the bars do not exaggerate the gap."],
         "discuss": [("What reference do you have for your own figures?", "HR system totals, last month's approved figure, headcount from Manpower."),
                     ("Who checks your figures before a report goes to management?", "Often nobody. A control total is the check you can do yourself.")]},
 "dfm1": {"prove": "A form is only as good as the decisions behind it. A vague request gives a generic survey; requirements first give questions that each serve a decision, with no personal data.",
          "script": ["(Run the weak request, no file.) A training survey in ten seconds. Let us read it.",
                     "(Point to each question.) Who answers this: staff or managers? Which decision does it help L&D make? (Point to any name or rating question.) Would you collect this?",
                     "(New chat. Attach the brief. Run the requirements request.) Now Copilot starts from the decisions L&D must make.",
                     "(Read the table row by row.) Every question has a decision next to it. If a row has no decision, we delete it.",
                     "(Close.) This is the brainstorm. The form comes after it, not before."],
          "discuss": [("Last time your team ran a survey, what did you do with the answers?", "Often nothing, or the answers were too messy to count."),
                      ("Should a training needs form ask for the employee's name?", "No. Managers answer for the team. Names belong in nomination, later, through the approved process."),
                      ("For your own unit, what is the one decision a training needs form must help you make?", "Which course first, how many seats, when.")]},
 "dfm2": {"prove": "Copilot in Forms builds a working form in a minute from a clear request. The trainer still checks every question, every choice and the settings before the link goes out.",
          "script": ["(New Form. Paste the request into Draft with Copilot.) I give it every question, its type and its choices. Copilot follows a list best.",
                     "(Keep it. Go question by question.) Is the unit a choice with the 8 units? Is the number a number? Did it add anything I did not ask for?",
                     "(Fix one thing by hand on screen.) Copilot drafts. I decide what the form asks.",
                     "(Open Settings.) Only people in our organization. Now the big question for the room: do we record names? (Take answers.)",
                     "(Show the QR code.) Please answer my form now, with made-up answers. Two minutes. We use your answers in the next demo."],
          "discuss": [("Record names or keep it anonymous? What do you gain and lose?", "Names let you follow up and stop double answers. Anonymous answers can be more honest. Decide before the link goes out, and say it on the form."),
                      ("Copilot added a question you did not ask for. What do you do?", "Delete it. The plan decides, not Copilot."),
                      ("Who should approve a form before it goes to 52 managers?", "The owner of the decision, for example the Head of L&D.")]},
 "dfm3": {"prove": "Forms collects the answers and Copilot counts them in seconds, but the first count was wrong. Cleaning changed the top need from Safety leadership to Excel. Only a check against who was invited shows the rows that should not count.",
          "script": ["(Open the demo form's Responses page.) These are your answers from two minutes ago. (Open Copilot in Forms and ask for the main needs.) Check one number with me against the chart.",
                     "(Open the practice export.) Now imagine the survey has closed. " + str(len(D.TN_EXPORT)) + " rows. (Run the count.) Write the top three on the board.",
                     "(Run the problems request.) A test answer. A manager who answered twice. Excel written five ways. (Point to the comment row by its ID only. Do not read it aloud.)",
                     "(Run the clean count.) Look at the board. Which need is first now? (Excel.) Nothing in the data changed. Only the cleaning did.",
                     "(Open the Invited sheet.) " + str(len(D.TN_VALID)) + " of " + str(D.TN_INVITED_TOTAL) + " managers answered. Which unit do we chase? (IT.)"],
          "discuss": [("Copilot in Forms or Excel: when would you use each?", "Forms for a quick look while answers come in. Excel when you must clean, count and keep a record."),
                      ("HR shows " + str(D.TN_RAW_BY_UNIT["HR"]) + " answers but only 5 HR managers were invited. What does that tell you?", "Something should not be counted: a test, or someone who answered twice."),
                      ("One comment names an employee and his surgery. What do you do with it?", "Never copy it into Copilot, a slide or a summary. Keep only the point without the person: some staff cannot join field courses. This is where the last block of today starts.")]},
 "d210": {"prove": "A deck from a prompt only looks finished but holds facts Copilot guessed. A deck from a document carries the real facts. For HR slides you need the document.",
          "script": ["(One-line request, no file.) Five tidy slides in a minute. (Read the start times aloud.) Where did these times come from? Nowhere. Copilot guessed.",
                     "(Create a presentation from the brief.) Now every time comes from the brief.",
                     "(Put the two decks side by side. Check the times and the pilot number against the brief.)",
                     "A prompt gives you a structure. A document gives you the facts."],
          "discuss": [("How long does a ten-slide deck take you today?", "Two hours to half a day. The drafting part shrinks; the checking part stays."),
                      ("Which number on a slide would embarrass you most if it were wrong?", "Headcount, budget, a date. Those are the ones to check first.")]},
 "d211": {"prove": "Editing a deck is a series of rounds. Each round is a new draft, so the numbers are checked again after every round.",
          "script": ["(Stay in the deck from Demo 2.10. Paste the edit request.) A new slide for managers, a plainer slide 4, notes on every slide.",
                     "(Read the new slide aloud. Then check the times and the pilot number again.) Did anything move while Copilot edited?",
                     "(Open the speaker notes.) Could a colleague present this tomorrow from these notes?"],
          "discuss": [("Who presents decks that someone else made, in your team?", "Section heads, supervisors. Speaker notes are what make that possible."),
                      ("What would you never let Copilot change in a deck?", "Numbers, dates, names of approvers, anything a decision rests on.")]},
 "d21": {"prove": "Before any prompt, the task is sorted green, amber or red. The answer can be right and the prompt still wrong.",
         "script": ["(Read the first card aloud.) Green, amber or red? Call it out. (Tap the card.)",
                    "(When the room disagrees, stop.) Why amber and not red? What would make it red? (Usually: names, IDs, salaries, health.)",
                    "(After the last card.) Remember the survey comment from Block 4? Which color was it? (Red.)"],
         "discuss": [("Which task from your own week sits in amber?", "Policy summaries, counts with employee codes, internal reports."),
                     ("If your company has no approved Copilot account, what happens to amber?", "Amber becomes red.")]},
 "d21b": {"prove": "Redaction happens before the prompt, not inside it. Copilot gives a useful summary from a note that names nobody, and it should not guess what was removed.",
          "script": ["(Show the note on your own screen only.) I am not pasting this anywhere.",
                     "(Redact aloud.) Names become roles. The ID, the phone, the salary and the medical reason go.",
                     "(Run the request with the redacted text.) Read the summary with me. Did it guess a reason for the absence? If it did, we delete that line.",
                     "Asking Copilot to keep a secret protects nothing. The protection is what you never typed."],
          "discuss": [("Where do sensitive details hide in a document?", "Inside sentences: a salary in brackets, a reason for absence, an ID in a signature."),
                      ("Is redaction enough to make a red task amber?", "Only with an approved account and your company's policy. When unsure, treat it as red and ask.")]},
}
# Day 3 runbook guide (Aya, 18 Nov 2026): the built-in agents demo and the three recorded flows she narrates (the videos have no sound)
RUNGUIDE.update({
 "d30": {"prove": "A built-in agent is Copilot with saved instructions for one job. It saves you the instructions, not the check.",
         "script": ["(Open Agents, then All agents.) Microsoft already built these. Each one has instructions for one job.",
                    "(Open Prompt Coach. Paste the weak request.) This is the kind of one-line request we fixed on Day 1. Let us see what the coach says.",
                    "(Read the feedback aloud.) Context, data, limits, format: the same checklist we learned. (Run the better request.) Same Copilot, a better answer.",
                    "(Open Researcher. Paste the question.) Researcher reads many sources, so it takes a few minutes. We come back to it.",
                    "(Open the report.) A report with sources. Before I trust it, I open two sources and check one fact in each."],
         "discuss": [("What did Prompt Coach add that your Day 1 request missed?", "Context, the limits, the format."),
                     ("Would you send the Researcher report to your manager as it is?", "No. Open the sources first, and remove any point with no source.")]},
 "d35": {"prove": "A flow starts on its own, does the same steps every time, and stops to wait when a person must decide.",
         "script": ["(Play. Pause on the first card.) Four parts, the same in every flow: trigger, actions, connectors, output.",
                    "(Pause on 1 · TRIGGER.) What starts it: a new answer in the training request form. Nobody presses a button.",
                    "(Pause on Start and wait for an approval.) The flow stops here, for hours or days if needed, until a person decides.",
                    "(Pause on the condition.) Approve takes one path. Reject takes the other.",
                    "(Play to RESULT.) The approval took a minute and a half. Every other step took seconds. (Play to the end.) A row in Excel that nobody typed, and an email to the employee."],
         "discuss": [("Which step did a person do?", "The approval. Everything else is the same every time."),
                     ("Where does a request like this wait in your unit today?", "Signatures, email, printing and scanning.")]},
 "d35b": {"prove": "A flow can start on a date and use AI as one of its steps. The AI drafts; L&D reviews before anything goes to a vendor.",
          "script": ["(Play.) Demo 1 started when a form arrived. This one starts on a date: every Sunday at 8:00.",
                     "(Pause on the data.) These are the week's training requests from the form. The flow keeps only four columns, so the AI sees only what it needs.",
                     "(Pause on Run a prompt.) This is AI inside the flow: a prompt that groups the demand and drafts an outline for vendors. I wrote and tested the prompt once.",
                     "(Play to the email.) It lands in L&D's inbox, marked DRAFT for review. Nothing goes to a vendor on its own."],
          "discuss": [("Why does the email say DRAFT?", "AI drafts. A person checks it and decides what goes out."),
                      ("Which weekly summary in your unit could start like this?", "Training demand, vacancies, overtime, attendance exceptions.")]},
 "d35c": {"prove": "A flow can read an email, pull the facts into Excel and score the offer against company goals. The score helps L&D compare; L&D decides.",
          "script": ["(Play.) The trigger this time is an email: any message with Quotation in the subject.",
                     "(Pause on the quotation.) A vendor offer as vendors really send it: price, dates, duration and learners, all in one long email. The vendor is fictional.",
                     "(Pause on Run a prompt.) The AI reads the offer and our requests, then scores the fit against four goals. One goal: 150 KWD or less per learner.",
                     "(Play to the Excel row.) One row per offer: price, duration, dates, score, strengths, concerns. Status: To review.",
                     f"(Play to the email.) Score {D.PA_QUOTE['score']} out of 10: {D.PA_QUOTE['total']:,} KWD for {D.PA_QUOTE['learners']} learners is {D.PA_QUOTE['per']} KWD each, above our limit. The flow does not answer the vendor. L&D decides."],
          "discuss": [("Would you accept the score as it is?", "No. Check the price per learner and the dates yourself, then decide."),
                      ("What else arrives by email that you copy into Excel by hand?", "CVs, invoices, timesheets, certificates, course feedback.")]},
})
for _k, _v in RUNGUIDE.items(): DEMOS[_k].update(_v)

# ===================================================================== Day 2 teaching order (Aya, 18 Nov 2026): meetings, Outlook, Excel, Forms, PowerPoint, then safe data last
_D2_LAST = ("d21", "d21b", "t21")
_order = sorted(DEMOS, key=lambda k: (DEMOS[k]["day"], 1 if (DEMOS[k]["day"] == 2 and k in _D2_LAST) else 0, list(DEMOS).index(k)))
_items = [(k, DEMOS[k]) for k in _order]; DEMOS.clear(); DEMOS.update(_items)

# lab prompts that live in this file: filled into the Day 2 and Day 3 labs (content.py cannot import this file)
CHECKCARD = DEMOS["t38"]["prompts"][0][1]
assert " a flow " not in CHECKCARD
_FILL = {"RECAP": joined(RECAP), "MAP_FILE": joined(MAP_FILE), "AGENT": joined(AGENT), "COACH": joined(COACH), "CHECKCARD": CHECKCARD, "REQS": joined(REQS), "FORMQ": FORMQ, "TNPROB": TNPROB, "TNCLEAN": TNCLEAN, "PAYREQ": PAYREQ, "OTREQ": OTREQ, "MEMO": joined(MEMO_TASK), "R360": joined(R360Q),
         "COACH_ASK": COACH_ASK, "RESEARCH": D.BUILTIN_RESEARCH,
         "COACH_BUDDY": "Job Description Coach: " + joined(COACH) + "\n\nOnboarding Buddy: " + joined(BUDDY)}
for _L in C.LABS.values():
    for _s in _L["steps"]:
        if str(_s.get("prompt", "")).startswith("FILL:"): _s["prompt"] = _FILL[_s["prompt"][5:]]
        _s["templates"] = [(a, _FILL[b[5:]] if b.startswith("FILL:") else b) for a, b in _s.get("templates", [])]
        _fs = _s.get("files", [])                                  # say what each file is, before the first step
        _ab = (["About your track's case file: the facts, the people, the meeting and the open question for your HR unit."] if set(CASE_FILES) <= set(_fs) else [])
        _ab += [f"About {f}: {FILE_ABOUT[f][0]}" for f in _fs if f not in CASE_FILES]
        if _ab and not str(_s["do"][0]).startswith("About "): _s["do"] = _ab + list(_s["do"])

# hub stat strip: the card sort is not a prompt demo
C.HUB["stats"] = [(len(C.DAYS), "days"), (None, "slides"), (sum(1 for v in DEMOS.values() if v.get("hands_on")), "hands-on tasks"),
                  (sum(1 for v in DEMOS.values() if not v.get("hands_on") and v.get("kind") != "sort" and "recorded demo" not in v["tool"]), "prompt demos"),
                  (len(ALL_FILES), "sample files"), (len(C.MAP), "MAP questions")]
