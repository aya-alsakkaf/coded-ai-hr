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
 "payroll": "mutla-payroll-check-oct-nov-2026.xlsx", "onboard": "mutla-onboarding-checklist-2026.docx",
}
CASE_FILES = [D.CASES[k]["file"] for k, _n in D.TRACKS]
CAP_FILES = [D.CAPSTONE[k]["file"] for k, _n in D.TRACKS]
ALL_FILES = [F["leave"], F["answer"], F["case"], F["oldjd"], F["tpl"], F["roles"], F["catchjd"], F["bank"], F["letters"],
             F["v3"], F["v4"], F["thread"], F["transcript"], F["trackers"], F["payroll"], F["brief"]] + CASE_FILES + [F["stories"], F["maptpl"],
             F["attendance"], F["training"], F["factors"], F["onboard"], F["card"], F["palog"], F["catchbank"]]
assert len(ALL_FILES) == len(set(ALL_FILES))

# prompt sheet sections: sec -> (day, name)
BLOCK = {1: (1, "Opener"), 2: (1, "Block 1 · How Copilot works"), 3: (1, "Block 2 · A clear prompt"),
         4: (1, "Block 3 · Word: draft, fix, check"), 5: (1, "Block 4 · Word, then Outlook"),
         6: (2, "Block 1 · Protect employee data"), 7: (2, "Block 2 · Prepare and recap"), 8: (2, "Block 3 · Outlook follow-ups"),
         9: (2, "Block 4 · Excel: check figures"), 10: (2, "Block 5 · Word summaries"), 11: (2, "Block 6 · PowerPoint"),
         12: (3, "Block 1 · Build an HR agent"), 13: (3, "Block 2 · Test, fix, build again"), 14: (3, "Block 3 · Power Automate demo"),
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
demo("d10", day=1, skill="1.0", sec=1, title="One job description, two requests", tool="Copilot Chat", files=[F["tpl"], F["roles"]],
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

demo("d13", day=1, skill="1.3", sec=4, title="Fix it with follow-up instructions", tool="Copilot Chat", files=[F["roles"], F["tpl"]],
 setup=[f"[T] Open a new Copilot Chat. Attach {F['roles']} and {F['tpl']}. Paste the checklist request for the {R['title']}.",
        "[T] Read the draft aloud. Name one thing that is weak.", "[T] Send the follow-up that fixes it. Say which part of the draft you want kept.",
        "[T] Send the third follow-up: the list of assumptions. Delete what has no source."],
 prompts=[("The checklist request", joined(JD_CMP))] + [(f"Follow-up · {a}", b) for a, b in FOLLOWUPS],
 expected="After the follow-ups: a one-page job description with the six duties from the role sheet, no introduction, the grade blank. The assumption list shows anything Copilot added on its own, for example a system name or years of experience.",
 say="The first draft is a draft. Say exactly what to change, and say what to keep. You do not start again.",
 point="A follow-up names the problem and what to keep.",
 backup=[("h", "Typical assumption list"), ("ul", ["I assumed the job uses an HR system to record allowances.", "I assumed the job holder writes in English and Arabic.", "I assumed the job description should include an introduction paragraph."])],
 fallback="Show the backup list on the trainer screen.",
 hint="Name the problem, and say what must not change.")

demo("d13b", day=1, skill="1.3b", sec=4, title="Ask for the source of every line", tool="Copilot Chat", files=[F["catchjd"], F["roles"], F["tpl"]],
 setup=["[T] Open a new chat. Attach the three files listed on the slide.", "[T] Paste the source-trace request. Scroll to every NOT IN SOURCE line.",
        "[T] Open the role sheet and show that the line really is not there."],
 prompts=[("Source trace", joined(TRACE))],
 expected=f"A table with one row per line of the draft. Two lines come back NOT IN SOURCE: {D.JD_UNSUPPORTED[0][0].lower()}, and {D.JD_UNSUPPORTED[1][0]}.",
 say="Copilot does the searching. You do the deciding. A line with no source is a line you delete or check with the owner.",
 point="No source, no line.",
 backup=[("h", "Typical result: the two lines with no source"), tbl(["Line in the draft", "Why it fails"], D.JD_UNSUPPORTED)],
 fallback="Show the backup table on the trainer screen.",
 hint="Every line needs a line of the role sheet behind it.")

demo("t13", day=1, skill="1.3", sec=4, title="Your job description: draft, fix, check", tool="Copilot Chat · Word", files=[F["roles"], F["tpl"], F["oldjd"]], kind="task", hands_on=True, minutes=22, solo="on your own",
 setup=["Pick your unit track. Find your track's role in the role information file.",
        "Write your own checklist request (all five parts). Attach the role information and the 2026 template.",
        "Read the draft. Send two follow-up instructions that fix what is weak.",
        "Run the source-trace request below. Delete or fix every NOT IN SOURCE line.",
        f"Check by hand: count the duties against the role sheet. Is the grade blank? Does it start with {DL}?"],
 prompts=[("Source trace (step 4)", joined(TRACE))],
 expected="A one-page job description in the template's order: only the role sheet's six duties, no team size, a blank grade line, and the DRAFT line at the top. Two follow-ups that each name a problem and what to keep.",
 say="Same method, your own role: write it, fix it, check it.",
 point="Draft with the checklist. Fix with follow-ups. Check every line.",
 backup=[("h", "A typical result (Compensation Analyst)")] + [("p", x) for x in JD_RESULT_LINES],
 answer=[("h", "What a good request has"), ("ul", ["Context: an HR officer at Mutla; the 2026 evaluation round; the committee reads it.", "Task: the job description for the track's role.",
          "Data: both files attached and named.", "Constraints: only the files; no duties, team size or grade added; one page.", f"Format: formal and neutral; the template's headings; starts with {DL}"]),
         ("h", "What a good result has"), ("ul", ["The template's eight headings, in order.", "Only the duties in the role sheet (6 for every track's role), each starting with a verb.",
          "No team size, no grade, no salary.", "A neutral tone: no \"dynamic\", \"exciting\" or \"world-class\"."]),
         ("h", "The roles by track"), tbl(["Track", "Role"], [(n, D.ROLES[k]["title"]) for k, n in D.TRACKS])],
 deliverable="Your job description, fixed and checked, with your request and your two follow-ups.",
 fallback=f"Anyone whose draft fails can check {F['catchjd']} instead, from step 4.",
 hint="Data names both files. Constraints say what Copilot must not add: duties, a team size, a grade.",
 stretch=["Turn your job description into vacancy text for a job board. Keep every duty. Add no promise, salary or grade."])

demo("t14", day=1, skill="1.4", sec=4, title="An experience letter: draft, fix, check", tool="Copilot Chat · Word", files=[F["letters"]], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=[f"Open {F['letters']}. Read the template rules, the HR system record and the three requests.",
        f"Write a checklist request for Ali Al-Harbi's letter ({ALI[0]}). Attach the file.",
        "Run the flag request below. Copilot lists the problems; it does not fix them. You decide.",
        "Fix the draft with one follow-up instruction. Then check the dates and the job title by hand against the HR record."],
 prompts=[LETTER_FLAG],
 expected=f"A letter for {ALI[1]}, {ALI[0]}, {ALI[2]} in {ALI[3]}, from {ALI[4]} to {ALI[5]}. No opinion and no salary. Two points flagged: " + "; ".join(f"{a.lower()}: {b}" for a, b in D.LETTER_TRAPS["EMP-3108"]),
 say="A different document, the same method. The record decides the dates. The template decides what may be said.",
 point="Flag, then decide. Copilot lists the problem; a person fixes it.",
 backup=[("h", "Ali's letter: typical result"), ("p", f"{DL}<br>To whom it may concern. This is to certify that {ALI[1]}, employee number {ALI[0]}, worked at {D.COMPANY} as {ALI[2]} in {ALI[3]} from {ALI[4]} to {ALI[5]}. "
                                                       "This letter is issued at the employee's request. Personnel Supervisor, Personnel and Administration."),
         ("h", "The points to flag"), tbl(["Point", "Why"], D.LETTER_TRAPS["EMP-3108"])],
 answer=[("h", "Ali Al-Harbi (EMP-3108): the planted problems"), tbl(["Point", "What to do"], D.LETTER_TRAPS["EMP-3108"]),
         ("h", "Finished early: Dana Al-Khaldi (EMP-4250)"), tbl(["Point", "What to do"], D.LETTER_TRAPS["EMP-4250"]),
         ("note", "Maryam Al-Otaibi's request has no problem: it is the control. A participant who flags nothing for her is right.")],
 deliverable="Ali's letter, checked against the HR record, and the list of points Copilot flagged.",
 fallback="If Copilot misses a point, compare the request with the HR record row by hand.",
 hint="Two things in Ali's request do not belong in the letter.",
 stretch=["Do Dana Al-Khaldi's letter (EMP-4250). Write one sentence to tell her where to ask for a salary certificate."])

demo("d15", day=1, skill="1.5", sec=5, title="A policy summary with section numbers", tool="Copilot Chat · Word", files=[F["leave"]],
 setup=["[T] Open a new chat, or the leave policy in Word with Copilot.", "[T] Paste the summary request. Read the bullets aloud.",
        "[T] Check two numbers by hand against the policy: the carry-over days and the notice period."],
 prompts=[("Summary for new joiners", joined(SUM_LEAVE))],
 expected=f"Up to eight bullets, each with its section: {D.LEAVE['annual']} days a year (2), request {D.LEAVE['notice']} days before (3), carry over up to {D.LEAVE['carry']} days used by {D.LEAVE['carry_by']} (4), "
          f"{D.LEAVE['emergency']} days emergency leave (5), a certificate after {D.LEAVE['sick_cert']} days of sick leave (6), {D.LEAVE['hajj']} days Hajj leave once (7), balances from Personnel and Administration (8).",
 say="A summary you can check has section numbers. A summary you cannot check is a rumor.",
 point="Every point gives its section. You check two numbers yourself.",
 backup=[("h", "Typical result")] + [("p", f"Section {n}. {t}: {s}") for n, t, s in D.LEAVE_SECTIONS[1:]],
 fallback="Show the backup summary on the trainer screen.",
 hint="Pick two numbers and find them in the policy yourself.")

demo("t15", day=1, skill="1.5", sec=5, title="The allowances policy for staff", tool="Copilot Chat · Word", files=[F["v4"], F["v3"]], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=[f"Attach {F['v4']} to a new chat, or open it in Word with Copilot.",
        "Write your own checklist request: a one-page summary of the policy for staff, every point with its section number.",
        "Check three numbers by hand against the policy: the housing maximum, the transport grades and the remote-site days.",
        "Check the date: from when does version 4 apply? Does your summary say so?"],
 prompts=[],
 expected=f"A one-page summary with sections 2 to 7: housing 25% of basic salary up to KWD {A['housing_v4']}; transport KWD {A['transport']} for grades {A['transport_v4']}; child KWD {A['child']} for up to {A['child_max']} children; "
          f"remote-site {A['remote_pct']}% for more than {A['remote_days']} days; requests in the HR system; changes reported within 30 days. It says version 4 applies from {D.ALLOW_V4_DATE}, and version 3 until then.",
 say="Your summary will be read by people who never open the policy. Every number and date must be right.",
 point="Section numbers, numbers as written, and the date it applies.",
 backup=[("h", "The facts the summary must match")] + [("p", f"Section {n}. {t}: {s}") for n, t, s in D.allowances_sections(4)[1:]] + [("p", f"Version 4 applies from {D.ALLOW_V4_DATE}. Until then, version 3 applies.")],
 answer=[("h", "The planted problem"), ("p", f"The policy title says version 4 applies from {D.ALLOW_V4_DATE}. A summary that says \"the housing maximum is KWD {A['housing_v4']}\" with no date is wrong today: version 3 (KWD {A['housing_v3']}) applies until then. Accept a summary that gives both, with the date."),
         ("h", "Numbers to check"), ("ul", [f"Housing: 25% of basic salary, up to KWD {A['housing_v4']} (section 2).", f"Transport: KWD {A['transport']} for grades {A['transport_v4']} (section 3).", f"Remote site: {A['remote_pct']}% for more than {A['remote_days']} days in a month (section 5)."])],
 deliverable=f"A one-page summary for staff, with section numbers and the date version 4 starts.",
 fallback="If Copilot is slow, write the three numbers and the date by hand from the policy.",
 hint="Look at the title of the policy. From which date does it apply?",
 stretch=["Compare version 3 and version 4: list every change with its section number."],
 stretch_prompts=[COMPARE])

demo("d16", day=1, skill="1.6", sec=5, title="Turn the tone dial, keep the facts", tool="Copilot Chat · Outlook", files=[F["leave"]],
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

demo("t16", day=1, skill="1.6", sec=5, title="Announce and reply in Outlook", tool="Copilot Chat · Outlook", files=[F["thread"]], kind="task", hands_on=True, minutes=17, solo="on your own",
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

demo("d21", day=2, skill="2.1", sec=6, title="Green, amber or red: eight HR tasks", tool="Card sort", kind="sort",
 setup=["[T] Read each card aloud. The room calls green, amber or red, then tap the card."],
 prompts=[], expected="Red: anything with a civil ID, a named salary, medical details or a named person in a case. Amber: internal HR information with no names, in the company's approved Copilot account. Green: fictional files and your own drafting.",
 say="The answer may be right and the decision still wrong. Look at the light before you type.", point="Policy first. Then green, amber or red.",
 backup=[("h", "The card sort answers"), tbl(["Task", "Color"], [(t, c) for t, c in C.SORT])],
 fallback="If the slide fails, read the cards from the backup table and ask for a show of hands.", hint="Ask: is there personal data? Is this my company's approved account?")

demo("d21b", day=2, skill="2.1b", sec=6, title="Redact, then ask", tool="Copilot Chat",
 setup=["[T] Show the note before redaction on the trainer screen only. Never paste it.", "[T] Redact it aloud: roles for names, no ID, phone, salary or medical detail.",
        "[T] Open a new Copilot Chat. Paste the request with the redacted note in it. Read the summary: does it guess the removed detail?"],
 prompts=[("Summarize a redacted note", joined(RED))],
 expected="A three-line summary (what happened, the request, the next step) that names nobody and does not guess the removed detail.",
 say="Copilot only ever sees the redacted note. The redaction happens before the prompt, not inside it.",
 point="Redact first. Then ask.",
 backup=[("h", "Typical result"), tbl(["Part", "Summary"], [("What happened", "Employee A was absent on two days in late October."), ("The request", "To work at a different site for one month."), ("Next step", "The Personnel Supervisor decides. Colleague B can cover the shift.")])],
 fallback="Show the backup table on the trainer screen.",
 hint="If the summary guesses a removed detail, add: do not guess anything removed.")

demo("t21", day=2, skill="2.1", sec=6, title="Redact a case note", tool="Your eyes + Word", files=[F["case"]], kind="task", hands_on=True, minutes=11, solo="on your own",
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
demo("d22", day=2, skill="2.2", sec=7, title="Agenda, brief and discussion points", tool="Copilot Chat · Word",
 setup=["[T] Open a new Copilot Chat (or a new Word document with Copilot).", "[T] Paste the request: the meeting facts are inside it.",
        "[T] Add up the minutes in the agenda aloud. Check that each open question became a discussion point."],
 prompts=[("Prepare the meeting", joined(PREP))],
 expected=f"An agenda with an owner for each item and 30 minutes in total, a short brief ({O['joiners']} new joiners on {O['date']}, {O['room']}), and three discussion points, one of them the Medical Services check.",
 say="A meeting goes well when the page before it is good. Two minutes with Copilot, then you check the minutes add up.",
 point="Agenda, brief, discussion points: from approved facts only.",
 backup=[("h", "Typical agenda"), tbl(["Item", "Owner", "Minutes"], [("ID cards and laptop accounts", "Personnel and IT", "10"), ("Welcome session and safety briefing", "L&D", "10"), ("Medical Services check: same day?", "Personnel", "5"), ("Actions and owners", "Chair", "5")])],
 fallback="Show the backup agenda on the trainer screen.",
 hint="Do the minutes add up to 30?")

demo("t22", day=2, skill="2.2", sec=7, title="Prepare your track's meeting", tool="Copilot Chat · Word", files=CASE_FILES, kind="task", hands_on=True, minutes=15, solo="on your own",
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

demo("d23", day=2, skill="2.3", sec=7, title="Notes into decisions and actions", tool="Copilot Chat",
 setup=["[T] Open a new Copilot Chat. Paste the request: the notes are inside it.", "[T] Read the action table aloud. Ask the room: is there an action nobody agreed?"],
 prompts=[("Notes into actions", joined(NOTES_REQ))],
 expected="Four actions with owners; three have deadlines and one says no deadline set. The idea of inviting the CEO is not an action: nobody agreed. One open question: the Medical Services check.",
 say="A recap records what was agreed. An idea that nobody agreed to is not an action, however good it sounds.",
 point="Action, owner, deadline. Nothing nobody agreed.",
 backup=[("h", "Typical action table"), tbl(["Action", "Owner", "Deadline"], D.ORIENT_ACTIONS)],
 fallback="Show the backup table on the trainer screen.",
 hint="Find the line that nobody agreed to.")

demo("t23", day=2, skill="2.3", sec=7, title="Recap the staffing meeting", tool="Copilot Chat · Teams", files=[F["transcript"]], kind="task", hands_on=True, minutes=15, solo="on your own",
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

demo("d24", day=2, skill="2.4", sec=8, title="A follow-up and a reminder", tool="Copilot Chat · Outlook",
 setup=["[T] Go back to the chat from Demo 2.3, with the action table.", "[T] Paste the follow-up request. Read both emails aloud.",
        "[T] Point to each owner and date: did any change?", "[T] Where the account allows it, open a new email in Outlook and use Draft with Copilot with the same request."],
 prompts=[("Follow-up and reminder", joined(FOLLOW))],
 expected="A follow-up email to everyone with the four actions, owners and dates unchanged, and a polite two-line reminder to Noura about the agenda due on Monday 30 November.",
 say="The recap is only useful when it reaches people. A follow-up today and a reminder before the deadline: two short emails.",
 point="Same owners, same dates. Polite, never blaming.",
 backup=[("h", "Typical reminder"), ("p", f"{DL}<br>Subject: Reminder: agenda for the new joiners<br>Dear Noura, a quick reminder that the agenda for the new joiners is due on Monday 30 November. Thank you. Fatma")],
 fallback="Show the backup reminder on the trainer screen.",
 hint="Check every owner and date against the table.")

demo("t24", day=2, skill="2.4", sec=8, title="Follow up the staffing meeting", tool="Copilot Chat · Outlook", files=[F["transcript"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Use your recap from Task 2.3. No recap? Copy the action table the trainer shows.",
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
 fallback="No recap from Task 2.3: show the four actions from the backup on the trainer screen.",
 hint="The reminder asks politely and gives the deadline. It does not blame.",
 stretch=["Write the same reminder for a manager who has already missed a deadline. Keep it polite."])

demo("t25", day=2, skill="2.5", sec=8, title="Your track's message", tool="Copilot Chat · Outlook", files=CASE_FILES, kind="task", hands_on=True, minutes=10, solo="on your own",
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

demo("d26", day=2, skill="2.6", sec=9, title="Ask the tracker, then see the rows", tool="Copilot Chat · Excel", files=[F["trackers"]],
 setup=[f"[T] Attach {F['trackers']} to a new chat, or open it in Excel with Copilot (a saved .xlsx workbook).", "[T] Paste the count request. Open the Control totals sheet on the screen.",
        "[T] Put the two totals side by side. Ask the room what could make a total too high."],
 prompts=[("Count and compare", joined(TRACKER))],
 expected=f"Copilot counts {D.TRAIN_ROWS_EXPORT} rows. The Control totals sheet says {D.TRAIN_TRUE}. The difference is {D.TRAIN_DUPES}.",
 say="Copilot counted every row correctly. The rows were wrong. Only the check found it.",
 point="Ask, see the rows, then check against the control total.",
 backup=[("h", "Typical result"), tbl(["Count", "Number"], [("Rows in the Training sheet", str(D.TRAIN_ROWS_EXPORT)), ("Control total", str(D.TRAIN_TRUE)), ("Difference", str(D.TRAIN_DUPES))])],
 fallback="Show the backup table. If upload fails, use a PivotTable in Excel.",
 hint="A total that is too high: look for duplicate request IDs.")

demo("t26", day=2, skill="2.6", sec=9, title="Training requests: find the duplicates", tool="Copilot Chat + Excel", files=[F["trackers"]], kind="task", hands_on=True, minutes=12, solo="in pairs",
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
demo("t27", day=2, skill="2.7", sec=9, title="Payroll: compare two months", tool="Copilot Chat + Excel", files=[F["payroll"]], kind="task", hands_on=True, minutes=12, solo="in pairs",
 setup=["Attach the payroll file. It has employee codes and no names, so it is an amber task: use your company's approved account.",
        "Run the request below. Copilot compares October with November, then checks the Movements sheet.",
        "Check each item yourself in Excel. Mark it explained (on the Movements sheet) or to confirm.",
        "Write one line for each item to confirm. Change no salary."],
 prompts=[("Two months and the movements", PAYREQ)],
 expected=("Four differences between the months. The Movements sheet explains three of them: " + "; ".join(f"{c} ({w.split(':')[0].lower()})" for c, w in D.PAY_EXPLAINED) +
           ". Three items need a person to confirm: " + " ".join(f"{c}: {w}" for c, w, _a in D.PAY_ISSUES)),
 say="A payroll system calculates the salaries. Copilot is a second pair of eyes before the file goes to the bank: it lists what changed and asks why.",
 point="List every change. Check it against the approved movements. Ask why; never recalculate.",
 backup=[("h", "Items to confirm"), tbl(["Employee code", "What is wrong", "Next step"], D.PAY_ISSUES), ("h", "Explained by the Movements sheet"), tbl(["Employee code", "Movement"], D.PAY_EXPLAINED)],
 answer=[("h", "The three planted items"), tbl(["Employee code", "What is wrong", "Next step"], D.PAY_ISSUES),
         ("note", "Comparing the two months finds only EMP-3346. The leaver did not change, and the missing joiner is in neither month: only the Movements sheet shows them. Accept any wording that asks a person to confirm and changes no salary.")],
 deliverable="Three payroll items to confirm, one line each.",
 fallback="If upload fails, pairs sort both months by employee code in Excel and compare them side by side.",
 hint="Comparing the two months finds one problem. The Movements sheet finds the other two.",
 stretch=["Finished early? Open the trackers file. On the Manpower sheet, total vacancies look too low. Find out why."])

demo("d28", day=2, skill="2.8", sec=10, title="A finding into a note for management", tool="Copilot Chat · Word", files=[F["brief"]],
 setup=[f"[T] Attach {F['brief']} to a new chat, or open it in Word with Copilot.", "[T] Paste the request. Read the three bullets aloud.", "[T] Check the percentage and the weeks by hand in the brief."],
 prompts=[("A note for the Head of HR", joined(PILOT))],
 expected=f"A title and three bullets: late arrivals fell by {AT['pilot_drop']}% in an {AT['pilot_weeks']}-week pilot in the {AT['pilot_unit']}; one division and eight weeks only; the rules start for everyone on {AT['start']}.",
 say="Managers read the first three lines. Put the finding there, with its limits.",
 point="The finding, its limits, the next step.",
 backup=[("h", "Typical result"), ("ul", [f"{AT['pilot_drop']}% fewer late arrivals in {AT['pilot_weeks']} weeks ({AT['pilot_unit']}).", "One division and eight weeks: not yet proof for the whole company.", f"The rules start for all day staff on {AT['start']}."])],
 fallback="Show the backup bullets on the trainer screen.",
 hint="What does the pilot not show?")

demo("t28", day=2, skill="2.8", sec=10, title="A management summary in Word", tool="Copilot Chat · Word", files=[F["trackers"], F["payroll"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Use your results from Tasks 2.6 and 2.7: the corrected training count and the payroll items to confirm. Missing one? Ask the trainer.",
        "Write your own checklist request for a half-page summary for the Head of HR: what you found, what you corrected, and what still needs a person to confirm.",
        "Check every number and employee code by hand. Make sure it starts with the DRAFT line."],
 prompts=[],
 expected=f"A short summary: {D.TRAIN_TRUE} training requests (not {D.TRAIN_ROWS_EXPORT}, duplicates removed) and three November payroll items to confirm before the file goes to the bank, with no blame.",
 say="Your checked numbers are worth something only when someone reads them.",
 point="Corrected figures, the reason, no blame.",
 backup=[("h", "The two checks"), tbl(["Check", "In the file", "Result", "Why"], [("Q3 training requests", str(D.TRAIN_ROWS_EXPORT), str(D.TRAIN_TRUE), "duplicate request IDs"), ("November payroll", "3 items not explained", "to confirm", "an unexplained increase, a leaver still paid, a missing joiner")])],
 answer=[("h", "A good summary"), ("ul", ["The corrected training count, and the figure that was in the file.", "The three payroll items, by employee code, each with the person who confirms it.", "No blame on a unit or a person.", "A next step: for example, the same two checks before each report and each payroll run."])],
 deliverable="A half-page management summary in Word.",
 fallback="Nothing from before lunch? Show the backup tables on the trainer screen.",
 hint="Say what the file showed, what is correct, and who must confirm what is still open.")

demo("t29", day=2, skill="2.9", sec=10, title="Three lines for the HR team", tool="Copilot Chat · Word or Teams", files=[], kind="task", hands_on=True, minutes=10, solo="on your own",
 setup=["Use your summary from Task 2.8.", "Write your checklist request: turn it into a three-line update for the HR team channel.",
        "Keep every number. Take out every employee code: a team channel is wider than the Head of HR.", "Read the three lines against your summary. Is anything changed or lost?"],
 prompts=[],
 expected=f"Three short lines: the training count is {D.TRAIN_TRUE}, not {D.TRAIN_ROWS_EXPORT}; three November payroll items are with Compensation and Personnel to confirm; the next step. No employee codes.",
 say="The same facts for a wider reader. Shorter, and with less personal detail.",
 point="Same numbers, fewer words, no employee codes.",
 backup=[("h", "A typical update"), ("ul", [f"Q3 training requests: {D.TRAIN_TRUE} after removing duplicates (the file showed {D.TRAIN_ROWS_EXPORT}).", "November payroll: three items are with Compensation and Personnel to confirm before the bank file.", "Next: the same two checks before every report and payroll run."])],
 answer=[("h", "Check the update for"), ("ul", ["Three lines, every number as in the summary.", "No employee codes and no names.", "No blame on a unit or a person."])],
 deliverable="A three-line update for the HR team, with no employee codes.",
 fallback="No summary from Task 2.8: use the backup on the trainer screen.",
 hint="Who reads a team channel? Leave out anything that points to one employee.")

demo("d210", day=2, skill="2.10", sec=11, title="A brief into five slides", tool="Copilot Chat · PowerPoint", files=[F["brief"]],
 setup=["[T] In PowerPoint with Copilot: Create a presentation from a file, and pick the brief. In Copilot Chat: attach the brief and paste the request.",
        "[T] Read the slide titles aloud. Check the times and the pilot number on the slides against the brief."],
 prompts=[("Five slides", joined(DECK))],
 expected=f"Five slides: why the change, the new times, permissions, the pilot result ({AT['pilot_drop']}% fewer late arrivals in {AT['pilot_weeks']} weeks), and where to send questions.",
 say="A deck is the document made visible. Same facts, fewer words.",
 point="Every number on a slide matches its source.",
 backup=[("h", "Typical outline"), ("ol", ["Why we are changing attendance rules", f"Your new day: start {AT['flex_from']} to {AT['flex_to']}, core {AT['core_from']} to {AT['core_to']}",
          f"Permissions: {AT['permissions']} a month, up to {AT['perm_hours']} hours", f"The pilot: {AT['pilot_drop']}% fewer late arrivals", "Questions: Personnel and Administration"])],
 fallback="Show the backup outline on the trainer screen.",
 hint="Check the times and the pilot number against the brief.")

demo("t210", day=2, skill="2.10", sec=11, title="Five slides from your summary", tool="Copilot Chat · PowerPoint", files=[], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Save your Task 2.8 summary as a Word file.", "In PowerPoint with Copilot: Create a presentation from a file, and pick your summary. In Copilot Chat: attach it and ask for a five-slide outline with speaker notes.",
        "Check every number on every slide against your summary."],
 prompts=[],
 expected="Five slides (or an outline) with the corrected figures, the reasons and the next step, every number matching the summary.",
 say="Fast to make, quick to check. Read every number once.",
 point="Every number on a slide matches the summary.",
 backup=[("h", "The figures every slide must match"), ("ul", [f"Q3 training requests: {D.TRAIN_TRUE}.", "November payroll: three items to confirm (EMP-3346, EMP-2731, EMP-5114)."])],
 answer=[("h", "Facts to check"), ("ul", [f"Q3 training requests: {D.TRAIN_TRUE}.", "The three payroll items, by employee code.", "The reason for each one.", "No blame."])],
 deliverable="Five slides, or a five-slide outline, each number checked.",
 fallback="Without Copilot in PowerPoint, the outline from Copilot Chat is enough.",
 hint="Check the training count and the three employee codes on every slide where they appear.")

DECK_EDIT = five([["Task", "In the deck you just made, add a slide after slide 2 called \"What changes for managers\" with three bullets. Then rewrite slide 4 in plain English for line managers. Then add two sentences of speaker notes to every slide."],
                  ["Constraints", "Use only the facts already in the deck and the brief. Change no date, time or number."],
                  ["Output format", "Short bullets, no more than eight words each."]])
demo("d211", day=2, skill="2.11", sec=11, title="Edit a deck with Copilot", tool="PowerPoint · Copilot Chat", files=[F["brief"]],
 setup=["[T] Stay in the deck from Demo 2.10. Open Copilot in PowerPoint. (Without it: paste the outline into Copilot Chat with the same request.)",
        "[T] Paste the edit request. Show the new slide, the rewritten slide and the notes.", "[T] Use Designer for a layout if it is available. Then check every number on screen against the brief."],
 prompts=[("Edit the deck", joined(DECK_EDIT))],
 expected=f"A new slide 3 with three bullets for managers, a plainer slide 4, and speaker notes on every slide. The times ({AT['flex_from']} to {AT['flex_to']}) and the pilot result ({AT['pilot_drop']}%) are unchanged.",
 say="The first draft is the easy part. Most of the work in a deck is the second round: a missing slide, a slide for a different reader, the notes.",
 point="Edit in rounds. Check every number after each round.",
 backup=[("h", "What the edits look like"), ("ul", ["Slide 3: What changes for managers (three bullets).", "Slide 4: the same facts in shorter, plainer words.", "Speaker notes: two sentences on every slide."])],
 fallback="Show the backup on the trainer screen. Without Copilot in PowerPoint, run the request in Copilot Chat on the outline.",
 hint="Did any time or number change during the edits?")

demo("t211", day=2, skill="2.11", sec=11, title="Slides for your track's meeting", tool="PowerPoint · Copilot Chat", files=CASE_FILES, kind="task", hands_on=True, minutes=18, solo="on your own",
 setup=["Use your agenda and brief from Task 2.2, and your track's case file.", "Write your checklist request for four slides for that meeting, with speaker notes.",
        "Then ask for one edit: a slide for the meeting's open question, written as a question for the room.", "Check every date and number against the case file. Add the DRAFT line to the first slide."],
 prompts=[],
 expected="Four or five slides that follow the agenda, a slide that asks the open question, speaker notes, and every date and number as in the case file.",
 say="Your own meeting, on screen. You already did the thinking this morning.",
 point="Follow the agenda. Ask the open question. Check every number.",
 backup=[("h", "The open question in each case")] + [("p", f"<b>{n}:</b> {OPENQ[k]}") for k, n in D.TRACKS],
 answer=[("h", "Check the slides for"), ("ul", ["They follow the agenda from Task 2.2.", "The open question is asked, not answered.", "Every date and number matches the case file.", "Job Evaluation: no grade on any slide."])],
 deliverable="Four or five slides with speaker notes for your track's meeting.",
 fallback="No agenda from Task 2.2: ask Copilot for one from the case file first, then the slides.",
 hint="Which question in your case is not decided yet? Give it its own slide.",
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

demo("d31", day=3, skill="3.1", sec=12, title="An HR agent, built live", tool="Agent Builder", files=KNOW,
 setup=["[T] In Microsoft 365 Copilot, choose Create agent. Open the Configure tab.", f"[T] Name: {D.AGENT_NAME}. Description: answers staff questions from Mutla's HR policies.",
        "[T] Paste the instructions. Read the five parts aloud as you scroll.", "[T] Under Knowledge, upload the five policy files. Add the three starter prompts.",
        "[T] In the test pane, ask the first starter prompt. Point to the section number in the answer."],
 prompts=[("Instructions", joined(AGENT))] + [(f"Starter prompt {i}", q) for i, q in enumerate(STARTERS, 1)],
 expected=f"An agent with a name, a description, instructions in five parts, five knowledge files and three starter prompts. In the test pane it answers the carry-over question: up to {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']}, leave policy section 4.",
 say="An agent is a saved set of instructions with its own files. You write the instructions once; everyone who uses it gets the same rules.",
 point="Instructions, knowledge, starter prompts. Then test.",
 backup=[("h", "What the agent holds"), tbl(["Part", "What goes in"], [("Name", D.AGENT_NAME), ("Instructions", "The five checklist parts"), ("Knowledge", ", ".join(KNOW)), ("Starter prompts", " · ".join(STARTERS))])],
 fallback="If Agent Builder is off on the account, paste the same instructions into Copilot Chat, attach the five files, and ask the same question.",
 hint="Watch where each checklist part goes in the instructions.")

demo("t31", day=3, skill="3.1", sec=12, title="Write the agent's instructions", tool="Word or Notepad", files=KNOW, kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=[f"Open a blank document. Write the instructions for {D.AGENT_NAME} with the five checklist parts.",
        "Say which files it may use, and the dates of the two allowances versions.", "Say what it must never answer, when it must ask first, and where it refers people.",
        "Read it as if you were the agent. Could you answer a question you are not sure about?"],
 prompts=[],
 expected="Instructions in five parts: answer only from the five files with the section; v3 until 31 December 2026 and v4 from 1 January 2027; ask for the grade first when it matters; never a named person's pay or data; refer anything else to the right HR unit.",
 say="The instructions are the agent's job description. Vague instructions give a vague agent.",
 point="What it answers, from which files, what it never answers, and where it refers.",
 backup=[("h", "What the instructions must cover"), ("ul", ["Only the five knowledge files, with the section.", "The two allowances versions and their dates.", "Ask first when the answer depends on the person.", "Never a named person's pay or data. Never decide a case.", "Refer to the right HR unit."])],
 answer=[("h", "A model set of instructions"), tbl(["Part", "Instructions"], AGENT)],
 deliverable="The agent's instructions, in five parts.",
 fallback="Short of time: use the instructions from the Day 3 lab page, and change one line to make them yours.",
 hint="Constraints hold the rules that protect people: never, ask first, refer.")

demo("t32", day=3, skill="3.2", sec=12, title="Build it in Agent Builder", tool="Agent Builder", files=KNOW, kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=["In Microsoft 365 Copilot, choose Create agent, then the Configure tab.", "Add a name and a one-line description. Paste your instructions from Task 3.1.",
        "Upload the five policy files under Knowledge. Add three starter prompts.", "Ask one normal question in the test pane. Does the answer give the section?"],
 prompts=[(f"Starter prompt {i}", q) for i, q in enumerate(STARTERS, 1)],
 expected="A saved agent with five knowledge files and three starter prompts, that answers a normal question with the policy name and section.",
 say="Build it now. Tomorrow nobody will remember the instructions you only wrote down.",
 point="Name, instructions, knowledge, starter prompts, one test.",
 backup=[("h", "The parts of the agent"), tbl(["Part", "What goes in"], [("Name", D.AGENT_NAME), ("Knowledge", ", ".join(KNOW)), ("Starter prompts", " · ".join(STARTERS))])],
 answer=[("h", "Check the agent for"), ("ul", ["Five knowledge files uploaded.", "Three starter prompts that staff would really ask.", "A normal question answered with the policy name and section."])],
 deliverable="A saved agent that answers a normal question with its source.",
 fallback="No Agent Builder: paste your instructions into a new Copilot Chat, attach the five files, and test there. Or pair with a neighbor who has it.",
 hint="If the answer has no section number, check the Format line in your instructions.")

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

demo("t33", day=3, skill="3.3", sec=13, title="Test and fix your agent", tool="Agent Builder", files=KNOW, kind="task", hands_on=True, minutes=12, solo="on your own",
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

demo("t34", day=3, skill="3.4", sec=13, title="A second agent: choose one", tool="Agent Builder", files=[F["tpl"], F["factors"], F["onboard"]], kind="task", hands_on=True, minutes=18, solo="on your own",
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
 fallback="Short of time: write the instructions only, and test them in Copilot Chat with the knowledge files attached.",
 hint="The incomplete test leaves something out. What must your agent ask before it answers?")

PAF = [("Trigger", "When a new response is submitted (Microsoft Forms)"), ("Action", "Get response details (Microsoft Forms)"),
       ("Action", "Add a row into a table (Excel Online)"), ("Action", "Start and wait for an approval (Approvals)"),
       ("Condition", "Outcome is equal to Approve"), ("Action", "Send an email (V2) (Outlook)")]
assert [a for a, _b in PAF] == [a for a, _b, _c, _d in D.PA_FLOW]
demo("d35", day=3, skill="3.5", sec=14, title="A training request flow, from form to email (video)", tool="Power Automate · video demo", files=[F["palog"]],
 setup=["[T] Play the demo video of the flow: " + "; ".join(f"{a.lower()}: {b}" for a, b in PAF) + ".",
        "[T] Pause after the approval step. Ask the room which step a person did.", "[T] Placeholder until the video is recorded: walk through the six steps on the slide."],
 prompts=[],
 expected="One form response becomes one row in the TrainingRequests table, one approval request to the line manager, and one email to the employee with the result. The manager approves; the flow only carries the request.",
 say="A flow is for the steps that happen the same way every time. Copilot writes; an agent answers; a flow moves the work from one step to the next. A person still approves.",
 point="Trigger, actions, a condition. A person still decides.",
 backup=[("h", "The flow, step by step"), tbl(["Step", "Connector", "What it does"], [(f"{a}: {b}", c, d) for a, c, b, d in D.PA_FLOW]),
         ("h", "The log after the demo"), tbl(D.PA_LOG_HEAD, D.PA_LOG)],
 fallback="If the video does not play, walk through the six steps on the slide and the backup table.",
 hint="Which step needs a person? Which steps happen the same way every time?")

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

# lab prompts that live in this file: filled into the Day 2 and Day 3 labs (content.py cannot import this file)
CHECKCARD = DEMOS["t38"]["prompts"][0][1]
assert " a flow " not in CHECKCARD
_FILL = {"RECAP": joined(RECAP), "MAP_FILE": joined(MAP_FILE), "AGENT": joined(AGENT), "COACH": joined(COACH), "CHECKCARD": CHECKCARD, "PAYREQ": PAYREQ,
         "COACH_BUDDY": "Job Description Coach: " + joined(COACH) + "\n\nOnboarding Buddy: " + joined(BUDDY)}
for _L in C.LABS.values():
    for _s in _L["steps"]:
        if str(_s.get("prompt", "")).startswith("FILL:"): _s["prompt"] = _FILL[_s["prompt"][5:]]
        _s["templates"] = [(a, _FILL[b[5:]] if b.startswith("FILL:") else b) for a, b in _s.get("templates", [])]

# hub stat strip: the card sort is not a prompt demo
C.HUB["stats"] = [(len(C.DAYS), "days"), (None, "slides"), (sum(1 for v in DEMOS.values() if v.get("hands_on")), "hands-on tasks"),
                  (sum(1 for v in DEMOS.values() if not v.get("hands_on") and v.get("kind") != "sort"), "prompt demos"),
                  (len(ALL_FILES), "sample files"), (len(C.MAP), "MAP questions")]
