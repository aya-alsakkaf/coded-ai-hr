# -*- coding: utf-8 -*-
"""Every demo and hands-on task of AI Fundamentals for HR: requests, expected results, backups, answer keys and prompt-player data.
Numbers and names come from data.py, so the decks, prompt sheets, runbooks, backups and answer keys always agree."""
import data as D
import content as C
from data import kwd

# ------------------------------------------------------------------ the 31 sample files (names never change once built)
F = {
 "leave": "mutla-leave-policy-2026.docx", "answer": "mutla-copilot-leave-answer.docx", "case": "mutla-case-note-unredacted.docx",
 "oldjd": "mutla-jd-hr-officer-2019.docx", "tpl": "mutla-jd-template-2026.docx", "roles": "mutla-role-information-2026.docx",
 "catchjd": "mutla-catchup-jd-draft.docx", "bank": "mutla-prompt-bank-template.docx",
 "v3": "mutla-allowances-policy-v3.docx", "v4": "mutla-allowances-policy-v4.docx", "factors": "mutla-job-evaluation-factors.docx",
 "evidence": "mutla-je-evidence-notes.docx", "thread": "mutla-email-thread-attendance.docx", "transcript": "mutla-meeting-transcript-staffing.docx",
 "inv": "mutla-investigation-notes.docx", "trackers": "mutla-hr-trackers-q3-2026.xlsx", "brief": "mutla-policy-change-brief.docx",
 "attendance": "mutla-attendance-rules-2026.docx", "training": "mutla-training-policy-2026.docx", "catchbank": "mutla-catchup-prompt-bank.docx",
 "fresh": "mutla-capstone-fresh-input.docx",
}
CASE_FILES = [D.CASES[k]["file"] for k, _n in D.TRACKS]
CAP_FILES = [D.CAPSTONE[k]["file"] for k, _n in D.TRACKS]
ALL_FILES = [F["leave"], F["answer"], F["case"], F["oldjd"], F["tpl"], F["roles"], F["catchjd"], F["bank"],
             F["v3"], F["v4"], F["factors"], F["evidence"], F["thread"], F["transcript"], F["inv"], F["trackers"], F["brief"]] + CASE_FILES + \
            [F["attendance"], F["training"], F["catchbank"]] + CAP_FILES + [F["fresh"]]
assert len(ALL_FILES) == 31 and len(set(ALL_FILES)) == 31

# prompt sheet sections: sec -> (day, name)
BLOCK = {1: (1, "Opener"), 2: (1, "Block 1 · How Copilot produces an answer"), 3: (1, "Block 2 · Rules before the first request"),
         4: (1, "Block 3 · The five inputs"), 5: (1, "Block 4 · Grounding and checking"),
         6: (2, "Block 1 · Word: policies and evaluation"), 7: (2, "Block 2 · Outlook: thread to message"), 8: (2, "Block 3 · Teams: meetings and notes"),
         9: (2, "Block 4 · Excel: HR trackers"), 10: (2, "Block 5 · PowerPoint: briefings"), 11: (2, "Integration · One case"),
         12: (3, "Block 1 · The Prompt Gallery"), 13: (3, "Block 2 · Agent Builder"), 14: (3, "Capstone")}

DEMOS = {}
def demo(did, **kw):
    kw.setdefault("stretch", []); kw.setdefault("stretch_prompts", []); kw.setdefault("files", [])
    kw["card"] = ("Task " if kw.get("hands_on") else "Demo ") + kw["skill"]
    DEMOS[did] = kw
def tbl(head, rows): return ("table", [head] + [list(r) for r in rows])
def joined(parts): return " ".join(v for _k, v in parts)
TRACK_LINE = "Pick your unit track: " + "; ".join(f"{n}" for _k, n in D.TRACKS) + "."

# ===================================================================== the requests (one place: opener, players, sheets)
R = D.ROLES["cmp"]
JD_CMP = [["Instructions", f"You are an HR officer at {D.COMPANY}. Draft a job description for the {R['title']}, one page, in the order of the attached template."],
          ["Context", "It is for the 2026 job evaluation round. The Job Evaluation committee will read it."],
          ["Data", f"Use only the attached role information for the {R['title']}. Do not add duties, a team size or a grade."],
          ["Tone", "Formal, neutral, plain English. Each duty starts with a verb."],
          ["Approved sources", f"Follow {F['tpl']}. Leave the grade line blank for the committee."]]
LEAVE_Q = [["Question", "How many days of unused annual leave can staff carry over to next year?"],
           ["Approved source", f"Answer only from the attached {F['leave']}. Give the section number. If the policy does not say, write: not in the policy."]]
TRACE = [["Instructions", "Check the attached job description line by line. Give a table: the line, the line of the role information it comes from, or NOT IN SOURCE."],
         ["Data", f"Use only the attached {F['roles']}."],
         ["Approved sources", f"Check the order and the headings against {F['tpl']}. The grade must stay blank."]]
JE = [["Instructions", f"Organize the attached evidence notes for the {D.JE_ROLE} against the five evaluation factors. Give a table: factor, evidence, note number."],
      ["Context", "The Job Evaluation committee will use it. You prepare the file; the committee decides."],
      ["Data", f"Use only {F['evidence']}."],
      ["Tone", "Neutral and factual. No opinion about the level of the job."],
      ["Approved sources", f"Use the factor names in {F['factors']}. Add a last column, Level: for the committee. Do not suggest a grade."]]
THREAD = [["Instructions", "Summarize the attached email thread: every decision with its owner and date, then the open questions."],
          ["Context", "I am writing the staff announcement and must not miss a decision."],
          ["Data", f"Use only {F['thread']}. If an early message was changed later, use the later decision and say so."],
          ["Tone", "Short and neutral."],
          ["Approved sources", "Quote the message number for each decision."]]
RECAP = [["Instructions", "Turn the attached meeting transcript into a recap: decisions, then a table of action, owner, deadline, then open questions."],
         ["Context", "It goes to everyone at the meeting and to the HR Section Head."],
         ["Data", f"Use only {F['transcript']}. Do not add actions nobody agreed."],
         ["Tone", "Short, neutral, clear."],
         ["Approved sources", "Use the names and dates exactly as said in the transcript."]]
TRACKER = [["Instructions", f"How many training requests are in the Training sheet for Q3 2026? Give the count by unit, and show the formula or the rows you counted."],
           ["Context", "The number goes in the quarterly report to the Head of L&D."],
           ["Data", f"Use the attached {F['trackers']}, sheet Training."],
           ["Tone", "Plain numbers, no commentary."],
           ["Approved sources", "Then compare your total with the Control totals sheet and list any difference."]]
DECK = [["Instructions", "Turn the attached brief into a five-slide outline for the line managers' meeting: a title and three bullets per slide, plus speaker notes."],
        ["Context", "Line managers must explain the new attendance rules to their teams next week."],
        ["Data", f"Use only {F['brief']}. Keep every date, time and number exactly as written."],
        ["Tone", "Clear and practical, for busy managers."],
        ["Approved sources", "End with a slide: where to send questions (Personnel and Administration)."]]
GALLERY = [["Suggested prompt", "Draft an email to my team about an upcoming training course."],
           ["Instructions", "You are a training coordinator at Mutla. Draft a course nomination email."],
           ["Context", "To line managers; nominations close 30 days before the course."],
           ["Data", "Use the course name, dates and seats I paste below."],
           ["Tone", "Friendly, short, one clear action."],
           ["Approved sources", f"Follow {F['training']}, section 5."]]
AGENT = [["Role", f"You are {D.AGENT_NAME}. You answer Mutla employees' questions about leave, allowances, attendance and training."],
         ["Scope", f"Answer only from the knowledge files. Give the policy name and section for every answer. Allowances: version 3 applies until version 4 starts on {D.ALLOW_V4_DATE}. Give today's rule first, then the change and its date."],
         ["Tone", "Polite, short, plain English."],
         ["Must not answer", "Never give or guess the salary, allowance or personal data of a named person. Never decide a case."],
         ["Refer to HR", "If a question needs a personal record, a decision or is not in the files, say so and refer the person to the right HR unit."],
         ["Ask first", "If the answer depends on the person's grade or situation, ask for it before you answer."]]

LEAVE_RESULT = f"Up to {D.LEAVE['carry']} days of unused annual leave may be carried over. They must be used by {D.LEAVE['carry_by']} (section 4)."
JD_RESULT_LINES = [f"<b>Job title:</b> {R['title']} · <b>Unit:</b> {R['unit']} · <b>Reports to:</b> {R['reports']}",
                   f"<b>Purpose:</b> {R['purpose']}", "<b>Key duties:</b> " + "; ".join(R["duties"][:3]) + " …", "<b>Grade:</b> blank, for the Job Evaluation committee"]

# ===================================================================== DAY 1
demo("d10", day=1, skill="1.0", sec=1, title="One job description, two requests", tool="Copilot Chat", files=[F["tpl"], F["roles"]], kind="showcase",
 setup=["[T] Open Copilot Chat in two browser tabs, signed in with the training account.", f"[T] In the second tab, attach {F['tpl']} and {F['roles']}.",
        "[T] Paste the weak request in the first tab and the five-input request in the second."],
 prompts=[("Weak", f"Write a job description for a {R['title'].lower()}."), ("Strong", joined(JD_CMP))],
 expected=f"Weak: a generic job description with invented duties, a team to manage and a senior grade. Strong: Mutla's template order, the six duties from the role sheet, and the grade left blank.",
 say="Same tool, same afternoon. One request gave Copilot nothing to work from. The other gave it five things.",
 point="The request decides the answer. You decide what goes out.",
 backup=[("h", "Weak request: typical result"), ("p", "“The Compensation Analyst leads a team of analysts, designs reward strategy for the company and advises the Board. Grade: senior.”"),
         ("h", "Five-input request: typical result")] + [("p", x) for x in JD_RESULT_LINES],
 fallback="Play the opener in the deck; it shows both runs step by step.",
 hint="Compare the two answers. Which one could go to the committee after a check?")

demo("d11", day=1, skill="1.1", sec=2, title="The same question, with and without the policy", tool="Copilot Chat", files=[F["leave"]], kind="player",
 setup=["Open a new Copilot Chat. Ask the question below with no file. Note the answer.", f"Open another new chat. Attach {F['leave']} and paste the full request."],
 prompts=[("No file", LEAVE_Q[0][1]), ("With the policy", joined(LEAVE_Q))],
 expected=f"With no file, Copilot guesses a common rule, often 30 days or \"it depends on your company\". With the policy attached, it says {D.LEAVE['carry']} days, used by {D.LEAVE['carry_by']}, and names section 4.",
 say="Without the file Copilot predicts a likely answer. With the file and an instruction to cite it, you can check it in ten seconds.",
 point="Give Copilot the approved source, and ask where each point comes from.",
 backup=[("h", "Typical result with the policy attached"), ("p", f"“{LEAVE_RESULT}”")],
 fallback="Show the backup answer on the screen.",
 hint="Open section 4 of the policy. Does the number match?",
 player={"parts": LEAVE_Q,
         "table": [["Question", "No file", "With the policy"], ["Days carried over", "30 (a guess)", f"{D.LEAVE['carry']}"], ["Deadline to use them", "Not given", D.LEAVE["carry_by"]], ["Where it says so", "Nowhere", "Section 4"]],
         "best": 2, "reco": ["<b>With the source:</b> a number you can check in ten seconds.", "<b>Without it:</b> a likely number, said with the same confidence.", "<b>Your job:</b> open section 4 and confirm."],
         "control": "Open the section Copilot names and check the number before you reply."})

demo("t11", day=1, skill="1.1", sec=2, title="Spot the confident mistakes", tool="Your eyes + the policy", files=[F["leave"], F["answer"]], kind="task", hands_on=True, minutes=12, solo="in pairs",
 setup=[f"Open {F['answer']}. It is a Copilot answer to an employee's leave questions.", f"Open {F['leave']} next to it.",
        "Check every number and rule in the answer against the policy. No AI for this step.", "Write each mistake: what the answer says, and the correct section."],
 prompts=[("Then ask Copilot (only after you check by hand)", f"Compare the attached answer with the attached leave policy. List every statement in the answer that does not match the policy, and quote the section that is right.")],
 expected="Three mistakes: " + "; ".join(f"{a.lower()}: the answer says “{b}” but {c}" for a, b, c in D.LEAVE_ERRORS) + ".",
 say="The answer reads well. Three of its numbers are wrong. Fluent is not the same as correct.",
 point="Check every number against the approved source before it reaches an employee.",
 backup=[("h", "The three mistakes"), tbl(["Topic", "The answer says", "The policy says"], D.LEAVE_ERRORS)],
 answer=[("h", "The three planted mistakes"), tbl(["Topic", "The answer says", "The policy says"], D.LEAVE_ERRORS),
         ("note", "Lines in the answer that are right: 30 days of annual leave a year (section 2), and Hajj leave of 21 days once in service (section 7). Accept a pair that also flags the missing deadline for carried-over days.")],
 deliverable="The three wrong statements, each with the correct section.",
 fallback="If a pair cannot open the files, use the printed copies from the facilitator kit.",
 hint="There are three mistakes: one about carry-over, one about emergency leave and one about notice.",
 stretch=["For each mistake, write the one-line instruction that would have stopped it."],
 stretch_prompts=[("A safer request", "Answer only from the attached leave policy. For every number, give the section. If the policy does not say, write: not in the policy.")])

demo("d12", day=1, skill="1.2", sec=3, title="Green, amber or red: eight HR tasks", tool="The safe-use card", files=[], kind="sort",
 setup=["[T] Read each card aloud. The room calls green, amber or red, then tap the card."],
 prompts=[], expected="Red: anything with a civil ID, a named salary, medical details or a named person in a case. Amber: internal HR information with no names, in the company's approved Copilot account. Green: fictional files and your own drafting.",
 say="The answer may be right and the decision still wrong. Look at the light before you type.", point="Policy first. Then green, amber or red.",
 backup=[("h", "The card sort answers"), tbl(["Task", "Color"], [(t, c) for t, c in C.SORT])],
 fallback="If the slide fails, read the cards from the backup table and ask for hands up.", hint="Ask: is there personal data? Is this my company's approved account?")

# ----- Demo 1.2b: redact, then ask (a different, already redacted note, so Task 1.2 stays fresh)
RED_PARTS = [["Instructions", "Turn the note below into a short, neutral case summary for the HR file: what happened, the request and the next step."],
             ["Context", "The note is already redacted. It goes to the Personnel Supervisor."],
             ["Data", "Employee A, a technician, was absent on two days in late October. [Medical detail removed.] Employee A asks to work at a different site for one month. Colleague B can cover the shift."],
             ["Tone", "Neutral, short, plain English."],
             ["Approved sources", "Use only the note above. Do not guess any removed detail."]]
demo("d12b", day=1, skill="1.2b", sec=3, title="Redact, then ask", tool="Copilot Chat", files=[], kind="player",
 setup=["Redact the note first: roles for names, no ID, phone, salary or medical detail.", "Then paste the request with the redacted note in it."],
 prompts=[("Summarize a redacted note", joined(RED_PARTS))],
 expected="A three-part summary (what happened, the request, the next step) that names nobody and does not guess the removed detail.",
 say="Copilot only ever sees the redacted note. The redaction happens before the prompt, not inside it.",
 point="Redact first. Then ask.",
 backup=[("h", "Typical result"), tbl(["Part", "Summary"], [("What happened", "Employee A was absent on two days in late October."), ("The request", "To work at a different site for one month."), ("Next step", "The Personnel Supervisor decides. Colleague B can cover the shift.")])],
 fallback="Show the backup table.",
 hint="If the summary guesses a removed detail, add: do not guess anything removed.",
 player={"parts": RED_PARTS,
         "table": [["Part", "Summary"], ["What happened", "Absent two days, late October"], ["The request", "A different site for one month"], ["Next step", "The supervisor decides"]],
         "best": 1, "reco": ["<b>Redacted first:</b> no name, ID, salary or medical detail.", "<b>Removed stays removed:</b> no guessing.", "<b>A person decides</b> the request."],
         "control": "Read the summary once more. Could anyone outside HR tell who this is?"})

demo("t12", day=1, skill="1.2", sec=3, title="Redact a case note", tool="Your eyes + Word", files=[F["case"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=[f"Open {F['case']} in Word. Save a copy with -redacted at the end of the name.", "Find every detail that identifies a person or is sensitive.",
        "Replace names with roles (Employee A, Colleague B). Remove the civil ID, phone number, salary and medical reason.", "Read it once more. Could anyone outside HR tell who this is?"],
 prompts=[("Only on the redacted copy", "Read the attached note. List any detail that could still identify a person or is sensitive. Do not repeat the detail itself; give its paragraph number.")],
 expected="Six items removed or replaced: " + "; ".join(f"{a.lower()} → {c}" for a, _b, c in D.CASE_SENSITIVE) + ".",
 say="Redact first, then ask. Copilot can help you tidy the note only after nothing sensitive is left in it.",
 point="Replace names with roles. Remove IDs, numbers, salaries and medical details.",
 backup=[("h", "What a redacted note replaces"), tbl(["Sensitive item", "Replace with"], [(a, c) for a, _b, c in D.CASE_SENSITIVE])],
 answer=[("h", "The six planted items"), tbl(["Item", "In the note", "Replace with"], D.CASE_SENSITIVE),
         ("note", "The facts of the case (dates of absence, the request, the next step) stay in. Accept other neutral labels for people, as long as they are used the same way throughout. Also accept a note that makes the absence dates or the unit general (for example, two days in late October): the deck's rule is to remove anything that could point to the person.")],
 deliverable="A redacted copy of the case note that is safe to use with Copilot.",
 fallback="If Word is not available, mark the items on the printed note.",
 hint="Six items: two names, an ID number, a phone number, a salary and a medical reason.",
 stretch=["On the redacted copy only, ask Copilot whether any personal detail is left."])

demo("d13", day=1, skill="1.3", sec=4, title="The five inputs, one at a time", tool="Copilot Chat", files=[F["tpl"], F["roles"]], kind="player",
 setup=[f"Open a new Copilot Chat. Attach {F['tpl']} and {F['roles']}.", "Paste the five-input request. Read the result against the role information."],
 prompts=[("Five-input request", joined(JD_CMP))],
 expected=f"The {R['title']} job description in the template's order: purpose, the six duties from the role sheet, qualifications, working relationships, and a blank grade line.",
 say="Instructions, context, data, tone, approved sources. Watch what each one adds.",
 point="Five inputs, then check the result against the source.",
 backup=[("h", "Typical result")] + [("p", x) for x in JD_RESULT_LINES],
 fallback="Show the backup result on the screen.",
 hint="Check each duty against the role information. Is the grade blank?",
 player={"parts": JD_CMP,
         "table": [["Template section", "In the draft", "From"], ["Job purpose", "One sentence", "Role information"], ["Key duties", "6 duties, each starts with a verb", "Role information"],
                   ["Qualifications", "Degree and 2 years", "Role information"], ["Grade", "Blank", "Template rule"]],
         "best": 2, "reco": ["<b>Instructions and sources:</b> the template's order and rules.", "<b>Data:</b> every duty comes from the role sheet.", "<b>Context and tone:</b> written for the committee, neutral."],
         "control": "Check every duty against the role information before the draft goes to the committee."})

demo("t13", day=1, skill="1.3", sec=4, title="One job description, three ways", tool="Copilot Chat", files=[F["roles"], F["tpl"], F["oldjd"]], kind="task", hands_on=True, minutes=25, solo="on your own",
 setup=["Pick your unit track. Find your track's role in the role information file.",
        "Request 1: one line only, no files. Save the answer in Word.",
        "Request 2: a structured request with instructions, context and tone. No files.",
        f"Request 3: all five inputs, with {F['roles']} and {F['tpl']} attached.",
        "Write one sentence: which version is best, and why."],
 prompts=[("Request 1 · one line", "Write a job description for a [your track's role]."),
          ("Request 3 · five inputs", f"You are an HR officer at {D.COMPANY}. Draft a job description for the [role], one page, in the order of the attached template. It is for the 2026 job evaluation round; the Job Evaluation committee will read it. Use only the attached role information for this role. Do not add duties, a team size or a grade. Formal, neutral, plain English; each duty starts with a verb. Follow {F['tpl']} and leave the grade line blank.")],
 expected="Three versions. Request 1 is generic and invents duties. Request 3 follows the template, uses only the role sheet's duties and leaves the grade blank.",
 say="Same role, three requests. The difference is what you gave Copilot to work from.",
 point="Five inputs: instructions, context, data, tone, approved sources.",
 backup=[("h", "Request 3: a typical result (Compensation Analyst)")] + [("p", x) for x in JD_RESULT_LINES],
 answer=[("h", "What a good Request 3 result has"), ("ul", ["The template's eight headings, in order.", "Only the duties in the role sheet (6 for every track's role), each starting with a verb.",
          "No team size, no grade, no salary.", "A neutral tone: no \"dynamic\", \"exciting\" or \"world-class\"."]),
         ("h", "The roles by track"), tbl(["Track", "Role"], [(n, D.ROLES[k]["title"]) for k, n in D.TRACKS])],
 deliverable="Three versions of one job description, and one sentence on which is best and why.",
 fallback="Anyone whose Copilot is slow uses the backup result and checks it against the role sheet.",
 hint="Request 3 needs both files attached and all five inputs.",
 stretch=["Turn your best version into vacancy text for a job board, keeping every duty and adding no promises."],
 stretch_prompts=[("Vacancy text", "Turn this job description into vacancy text for a job board. Keep every duty and qualification. Add no salary, grade or promise.")])

demo("d14", day=1, skill="1.4", sec=5, title="Ask for the source of every line", tool="Copilot Chat", files=[F["catchjd"], F["roles"], F["tpl"]], kind="player",
 setup=[f"Open a new chat. Attach {F['catchjd']}, {F['roles']} and {F['tpl']}.", "Paste the source-trace request. Read every NOT IN SOURCE line."],
 prompts=[("Source trace", joined(TRACE))],
 expected=f"A table with one row per line of the draft. Two lines come back NOT IN SOURCE: {D.JD_UNSUPPORTED[0][0].lower()}, and {D.JD_UNSUPPORTED[1][0]}.",
 say="Ask Copilot to show its work. A line with no source is a line you delete or check.",
 point="No source, no line.",
 backup=[("h", "Typical result: the two lines with no source"), tbl(["Line in the draft", "Why it fails"], D.JD_UNSUPPORTED)],
 fallback="Show the backup table.",
 hint="Every line needs a line of the role sheet behind it.",
 player={"parts": TRACE,
         "table": [["Line in the draft", "Source"], ["Check allowance requests against the policy", "Role sheet, duty 1"], [D.JD_UNSUPPORTED[0][0], "NOT IN SOURCE"],
                   ["Prepare cost estimates for policy changes", "Role sheet, duty 5"], [D.JD_UNSUPPORTED[1][0], "NOT IN SOURCE"]],
         "best": 1, "reco": ["<b>Two lines</b> have no source: a team size and a grade.", "<b>Delete them</b>, or check them with the line manager.", "<b>The grade</b> belongs to the committee."],
         "control": "Delete or check every NOT IN SOURCE line before the draft goes anywhere."})

demo("t14", day=1, skill="1.4", sec=5, title="Check, fix and save", tool="Copilot Chat + Word", files=[F["catchjd"], F["roles"], F["tpl"], F["bank"]], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=[f"Use your Request 3 job description from Task 1.3, or {F['catchjd']} if you missed it.", "Run the source-trace request on it.",
        "Delete or fix every NOT IN SOURCE line. Check the grade is blank.", f"Open {F['bank']}. Save your best request as entry 1: task, request, files, check."],
 prompts=[("Source trace", joined(TRACE))],
 expected=f"A corrected job description with no unsupported lines, and Prompt Bank entry 1. With the catch-up draft: delete \"{D.JD_UNSUPPORTED[0][0]}\" and \"{D.JD_UNSUPPORTED[1][0]}\".",
 say="Check, fix, then save. Tomorrow you start from entry 1, not from a blank page.",
 point="A request you have checked is worth saving.",
 backup=[("h", "The catch-up draft: lines to delete"), tbl(["Line", "Why"], D.JD_UNSUPPORTED)],
 answer=[("h", "What a finished entry has"), ("ul", ["Task: one line (for example: draft a job description for the 2026 evaluation round).", "Request: all five inputs.",
          "Files: the role information and the template.", "Check: every duty traced to the role sheet; grade blank."]),
         ("h", "The catch-up draft"), tbl(["Line", "Why it goes"], D.JD_UNSUPPORTED)],
 deliverable="A corrected job description and Prompt Bank entry 1.",
 fallback=f"Anyone without a Task 1.3 draft uses {F['catchjd']}.",
 hint="A team size and a grade that the role information does not give.",
 stretch=["Ask Copilot to list every assumption it made in your job description, then remove each one by adding the missing context."],
 stretch_prompts=[("Assumptions", "List every assumption you made in this job description that is not in the attached role information. One line each.")])

# ===================================================================== DAY 2
demo("d21", day=2, skill="2.1", sec=6, title="Job-evaluation evidence, no grade", tool="Copilot Chat · Word", files=[F["evidence"], F["factors"]], kind="player",
 setup=[f"Open a new chat (or Copilot in Word). Attach {F['evidence']} and {F['factors']}.", "Paste the request. Check the last column is empty."],
 prompts=[("Evidence by factor", joined(JE))],
 expected=f"A five-row table for the {D.JE_ROLE}: one row per factor with the evidence and its note number, and an empty level column for the committee." + " Leave out " + " and ".join(f"{a} ({b.split(':')[0].lower()})" for a, b in D.JE_TRAPS) + ".",
 say="Copilot prepares the file. The committee decides the level. The empty column says that out loud.",
 point="Organize the evidence. Never assign the grade.",
 backup=[("h", "Typical result"), tbl(["Factor", "Evidence", "Note", "Level"], [(a, b, c, "for the committee") for a, b, c in D.JE_EVIDENCE]), ("h", "Left out on purpose"), tbl(["Note", "Why"], D.JE_TRAPS)],
 fallback="Show the backup table.",
 hint="Each row needs a note number. The level column stays empty.",
 player={"parts": JE,
         "table": [["Factor", "Evidence", "Note"]] + [[a, b, c] for a, b, c in D.JE_EVIDENCE[:3]],
         "best": 1, "reco": ["<b>Five factors</b>, each with evidence and a note number.", "<b>Level:</b> for the committee.", "<b>No grade</b>, no opinion."],
         "control": "If Copilot suggests a grade, delete it. The committee decides."})

# ----- Demo 2.1b: compare two versions (a short excerpt, so Task 2.1 stays fresh)
AT = D.ATT; AO = D.ATT_OLD
CMP_PARTS = [["Instructions", "Compare the old and new attendance rules below. List every change in a table: section, old text, new text."],
             ["Context", "Staff will ask what changed. I answer only from the approved text."],
             ["Data", f"Old, section 2: work starts at {AO['start']} and ends at {AO['end']}. New, section 2: staff start between {AT['flex_from']} and {AT['flex_to']}; core hours are {AT['core_from']} to {AT['core_to']}; {AT['hours']} working hours a day. Old, section 3: {AO['permissions']} permissions a month. New, section 3: {AT['permissions']} permissions a month, up to {AT['perm_hours']} hours each."],
             ["Tone", "Neutral. No opinion on which version is better."],
             ["Approved sources", "Use only the two texts above. Write No change for any section that did not change."]]
demo("d21c", day=2, skill="2.1b", sec=6, title="Compare two versions", tool="Copilot Chat · Word", files=[], kind="player",
 setup=["Open a new chat. Paste the request with both short texts in it.", "Check each row against the two texts."],
 prompts=[("Compare two versions", joined(CMP_PARTS))],
 expected=f"A table with two rows: section 2 (fixed {AO['start']} start becomes a {AT['flex_from']} to {AT['flex_to']} start with core hours) and section 3 ({AO['permissions']} permissions become {AT['permissions']}, up to {AT['perm_hours']} hours each).",
 say="A change you can point to has a section number. Without it, nobody can check.",
 point="Section, old text, new text: every change checkable.",
 backup=[("h", "Typical result"), tbl(["Section", "Old", "New"], [("2 · Hours", f"Start {AO['start']}, end {AO['end']}", f"Start {AT['flex_from']} to {AT['flex_to']}; core {AT['core_from']} to {AT['core_to']}"), ("3 · Permissions", f"{AO['permissions']} a month", f"{AT['permissions']} a month, up to {AT['perm_hours']} hours each")])],
 fallback="Show the backup table.",
 hint="Every row needs a section number. Check it in both texts.",
 player={"parts": CMP_PARTS,
         "table": [["Section", "Old", "New"], ["2 · Hours", f"Start {AO['start']}", f"Start {AT['flex_from']} to {AT['flex_to']}"], ["3 · Permissions", f"{AO['permissions']} a month", f"{AT['permissions']}, up to {AT['perm_hours']} hours"]],
         "best": 1, "reco": ["<b>Two changes</b>, each with its section.", "<b>Old and new text</b> side by side.", "<b>No opinion</b> on which is better."],
         "control": "Open both texts and check every row yourself."})

demo("t21", day=2, skill="2.1", sec=6, title="What changed between v3 and v4", tool="Copilot Chat · Word", files=[F["v3"], F["v4"]], kind="task", hands_on=True, minutes=15, solo="in pairs",
 setup=[f"Attach {F['v3']} and {F['v4']} to a new chat.", "Run the compare request.", "Open both files. Check each change Copilot lists against the sections.", "Write a change table: section, version 3, version 4."],
 prompts=[("Compare", "Compare the two attached versions of the allowances policy. List every change, with its section number, in a table: section, version 3, version 4. Quote the exact numbers. Do not summarize parts that did not change.")],
 expected="Three changes: " + "; ".join(f"{a}: {b} → {c}" for a, b, c in D.ALLOW_CHANGES) + ". The later sections are renumbered because of the new section 5.",
 say="Your manager asked one question: what changed? Answer it with section numbers.",
 point="Compare versions with section numbers. Check each change in both files.",
 backup=[("h", "The three changes"), tbl(["Section", "Version 3", "Version 4"], D.ALLOW_CHANGES)],
 answer=[("h", "The three planted changes"), tbl(["Section", "Version 3", "Version 4"], D.ALLOW_CHANGES),
         ("note", f"Also accept: the version date changed ({D.ALLOW_V3_DATE} → {D.ALLOW_V4_DATE}), and sections 5 and 6 of v3 became 6 and 7. These are not policy changes.")],
 deliverable="A change table with section numbers.",
 fallback="If Copilot misses a change, pairs compare sections 2, 3 and 5 by hand.",
 hint="The housing cap, the transport grades and one new section.",
 stretch=["Draft a three-line note to staff about the changes, every number unchanged."],
 stretch_prompts=[("Note to staff", "Write a three-line note to staff about these changes. Keep every number and date exactly as in version 4.")])

demo("d22", day=2, skill="2.2", sec=7, title="A long thread into decisions", tool="Copilot Chat · Outlook", files=[F["thread"]], kind="player",
 setup=[f"Attach {F['thread']} to a new chat. (In Outlook with Copilot, open the thread and select Summary by Copilot, or Summarize, at the top of the thread.)", "Paste the request. Check the start date against message 24."],
 prompts=[("Decisions from the thread", joined(THREAD)), ("Reply to a staff question", "Draft a short, polite reply to a staff member who asks whether the core hours change. Use only the approved decisions in your summary. If the thread does not answer it, say so.")],
 expected=f"Four decisions with owners and dates. The start date is {D.ATT['start']} (message 24), not the {D.ATT['old_start']} that message 3 proposed. Two open questions: Ramadan hours and field staff on rotation." + " Two traps: " + " ".join(f"{a}: {b}" for a, b in D.THREAD_TRAPS) + f" Reply: from {D.ATT['start']}, core hours are {D.ATT['core_from']} to {D.ATT['core_to']} (message 24). The thread does not give the current hours, so the reply says so and refers the person to Personnel and Administration.",
 say="Thirty messages, four decisions. One early date was changed later. The summary must say which one stands.",
 point="Decisions, owners, dates, and which message says so.",
 backup=[("h", "Typical result"), tbl(["Decision", "Owner", "Date or source"], D.ATT_DECISIONS), ("h", "Open questions"), ("ul", D.ATT_OPEN),
         ("h", "Typical reply to a staff question"), ("p", f"“Thank you for your question. From {D.ATT['start']}, core hours are {D.ATT['core_from']} to {D.ATT['core_to']}, as approved in message 24. The thread does not give the current hours, so please check them with Personnel and Administration.”")],
 fallback="Show the backup table.",
 hint="Find the message where the start date was approved.",
 player={"parts": THREAD, "table": [["Decision", "Owner", "When"]] + [list(x) for x in D.ATT_DECISIONS[:3]], "best": 0,
         "reco": [f"<b>Start date:</b> {D.ATT['start']}, the later decision.", "<b>Open:</b> Ramadan hours, field staff.", "<b>Each decision</b> cites its message."],
         "control": "Check the start date in message 24 before the announcement goes out."})

demo("t22", day=2, skill="2.2", sec=7, title="Announce and reply", tool="Copilot Chat · Outlook", files=[F["thread"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=[f"Use {F['thread']} and your decisions summary.", "Request 1: the staff announcement, in a warm and clear tone, every date and rule unchanged.",
        "Request 2: a reply to Mubarak's request in message 29.", "Check every time and date against the thread."],
 prompts=[("Announcement", f"Write a staff announcement about the new attendance rules from the attached thread. Use only the final decisions. Make it warm and clear; keep every date, time and rule as written. Under 150 words."),
          ("Reply to Mubarak", "Write a short, polite reply to Mubarak's request in message 29. Use only the final rules in the thread. Do not promise an exception.")],
 expected=f"An announcement with {D.ATT['start']}, the {D.ATT['flex_from']} to {D.ATT['flex_to']} start, core hours {D.ATT['core_from']} to {D.ATT['core_to']} and the {D.ATT['permissions']} permissions. A reply to Mubarak: {D.MUBARAK_ANSWER}",
 say="Warmer, never different. The tone can change; the facts cannot.",
 point="Change the tone. Keep the facts.",
 backup=[("h", "Typical reply to Mubarak"), ("p", f"“Dear Mubarak, thank you for your message. Under the new rules, the earliest start is {D.ATT['flex_from']}. You can use one of your {D.ATT['permissions']} monthly permissions of up to {D.ATT['perm_hours']} hours, with your line manager's approval. Personnel and Administration”")],
 answer=[("h", "Traps in the thread"), tbl(["Where", "What to do"], D.THREAD_TRAPS), ("h", "Check the announcement for"), ("ul", [f"Start date {D.ATT['start']} (not {D.ATT['old_start']}).", f"Flexible start {D.ATT['flex_from']} to {D.ATT['flex_to']}.",
          f"Core hours {D.ATT['core_from']} to {D.ATT['core_to']}; {D.ATT['hours']} working hours.", f"{D.ATT['permissions']} permissions a month, up to {D.ATT['perm_hours']} hours each.", "No promise about Ramadan hours."]),
         ("h", "The reply to Mubarak"), ("p", D.MUBARAK_ANSWER)],
 deliverable="A staff announcement and a reply to Mubarak, every date and rule unchanged.",
 fallback="If the thread file will not open, use the decisions table on the slide.",
 hint="Mubarak's request is message 29. The earliest start is in message 24.",
 stretch=["Write a version of the announcement for line managers: what changes for them."])

demo("d23", day=2, skill="2.3", sec=8, title="A transcript into actions", tool="Copilot Chat · Teams", files=[F["transcript"]], kind="player",
 setup=[f"Attach {F['transcript']} to a new chat. (In Teams, Copilot recaps a meeting only when it was transcribed.)", "Paste the recap request. Check each owner and deadline."],
 prompts=[("Recap", joined(RECAP))],
 expected=f"Four actions with owners and deadlines for the new {D.NEW_SECTION} section, and one open question: whether two positions are contract or permanent.",
 say="A meeting nobody summarizes is a meeting nobody remembers. Action, owner, deadline.",
 point="Every action has an owner and a deadline from the transcript.",
 backup=[("h", "Typical result"), tbl(["Action", "Owner", "Deadline"], D.STAFF_ACTIONS), ("h", "Open question"), ("ul", D.STAFF_OPEN)],
 fallback="Show the backup table.",
 hint="Check each owner's name and each date in the transcript.",
 player={"parts": RECAP, "table": [["Action", "Owner", "Deadline"]] + [list(x) for x in D.STAFF_ACTIONS[:3]], "best": 0,
         "reco": [f"<b>{len(D.STAFF_ACTIONS)} actions</b>, each with an owner and a deadline.", "<b>Open:</b> contract or permanent for two positions.", "<b>Nothing added</b> that nobody agreed."],
         "control": "Check every owner and deadline against the transcript before you send the recap."})

# ----- Demo 2.3b: a timeline, not a verdict (a short excerpt, so Task 2.3 stays fresh)
TL_PARTS = [["Instructions", "Put the events in the notes below in date order, in a table: date and time, what happened, who reported it. Then list the open questions."],
            ["Context", "The notes are for an HR case file. HR has made no finding."],
            ["Data", " ".join(f"{a}: {b[:-1]} (source: {c})." for a, b, c in D.TL_NOTES) + " " + D.TL_OPINION],
            ["Tone", "Neutral and factual. No blame and no words that judge a person."],
            ["Approved sources", "Use only the notes above. An opinion is not an event: leave it out of the table."]]
demo("d23c", day=2, skill="2.3b", sec=8, title="A timeline, not a verdict", tool="Copilot Chat · Word", files=[], kind="player",
 setup=["Open a new chat. Paste the request with the short notes in it.", "Check that no row judges a person."],
 prompts=[("Timeline and open questions", joined(TL_PARTS))],
 expected=f"A {len(D.TL_NOTES)}-row timeline in date order and two or three open questions. The supervisor's opinion is not in the table.",
 say="A timeline lists what happened. A verdict says who is wrong. Copilot writes the first. People decide the second.",
 point="Events and questions. No blame.",
 backup=[("h", "Typical result"), tbl(["Date and time", "What happened", "Source"], D.TL_NOTES), ("p", "<b>Open questions:</b> Was the broken printer reported? Who signs the checklist when it cannot be printed?"), ("p", "<b>Left out:</b> the supervisor's opinion. It is not an event.")],
 fallback="Show the backup table.",
 hint="Every row is an event with a date. No row says who is at fault.",
 player={"parts": TL_PARTS,
         "table": [["Date and time", "What happened", "Source"]] + [[a, b, c] for a, b, c in D.TL_NOTES],
         "best": 1, "reco": ["<b>Three events</b> in date order.", "<b>Open questions</b> at the end.", "<b>The opinion</b> stays out."],
         "control": "Read every row against the notes. Delete any word that blames a person."})

demo("t23", day=2, skill="2.3", sec=8, title="Timeline, not verdict", tool="Copilot Chat", files=[F["inv"]], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=[f"Attach {F['inv']} to a new chat. The notes use roles, not names.", "Run the timeline request.",
        "Read the result for any finding, blame or recommended action. Delete it.", "Check each date against the notes."],
 prompts=[("Timeline and questions", "From the attached notes, make a timeline of events: date, time, what happened, source. Then list the open questions HR still needs to answer. Do not give a finding, do not say who is at fault, and do not recommend an action.")],
 expected=f"A five-row timeline from 1 to 8 November and four open questions. The manager's opinion (“{D.INV_OPINION}”) appears, if at all, only as what someone said, never as a finding.",
 say="Copilot organizes the facts. People investigate and decide. A timeline, not a verdict.",
 point="Timeline and open questions. No findings, no blame, no action.",
 backup=[("h", "Typical timeline"), tbl(["When", "What happened"], D.INV_EVENTS), ("h", "Open questions"), ("ul", D.INV_QUESTIONS)],
 answer=[("h", "Timeline"), tbl(["When", "What happened"], D.INV_EVENTS), ("h", "Open questions (accept similar)"), ("ul", D.INV_QUESTIONS),
         ("note", f"The planted trap: the line “{D.INV_OPINION}” must not become a finding or a recommendation in the output.")],
 deliverable="A timeline and an open-questions list, with no conclusion in it.",
 fallback="If Copilot adds a conclusion, show the trap on the screen and delete it together.",
 hint="One line in the notes is an opinion. It must not become a finding.",
 stretch=[f"Write the agenda for the follow-up meeting from {F['transcript']}."],
 stretch_prompts=[("Agenda", "Write a 30-minute agenda for a follow-up meeting from the attached transcript: items, owner of each item, minutes.")])

demo("d24", day=2, skill="2.4", sec=9, title="Ask the tracker, then see the rows", tool="Copilot Chat · Excel", files=[F["trackers"]], kind="player",
 setup=[f"Attach {F['trackers']} to a new chat, or open it in Excel with Copilot (a saved .xlsx workbook).", "Paste the request. Compare the total with the Control totals sheet."],
 prompts=[("Count and compare", joined(TRACKER))],
 expected=f"Copilot counts {D.TRAIN_ROWS_EXPORT} rows. The Control totals sheet says {D.TRAIN_TRUE}. The difference, {D.TRAIN_DUPES}, is the duplicate request IDs.",
 say="Copilot counted every row correctly. The rows were wrong. Your check found it.",
 point="Ask, see the rows, then check against the control total.",
 backup=[("h", "Typical result"), tbl(["Count", "Number"], [("Rows in the Training sheet", str(D.TRAIN_ROWS_EXPORT)), ("Control total", str(D.TRAIN_TRUE)), ("Difference", str(D.TRAIN_DUPES))])],
 fallback="Show the backup table. If upload fails, use a PivotTable in Excel.",
 hint="A total that is too high: look for duplicate request IDs.",
 player={"parts": TRACKER, "table": [["Unit", "Rows"]] + [[u, str(D.TRAIN_BY_UNIT_EXPORT[u])] for u in D.UNITS[:4]], "best": 1,
         "reco": [f"<b>Rows counted:</b> {D.TRAIN_ROWS_EXPORT}.", f"<b>Control total:</b> {D.TRAIN_TRUE}.", "<b>Next:</b> find the rows behind the difference."],
         "control": "A total goes in a report only after it matches the control total."})

demo("t24", day=2, skill="2.4", sec=9, title="Two figures, checked", tool="Copilot Chat + Excel", files=[F["trackers"]], kind="task", hands_on=True, minutes=15, solo="in pairs",
 setup=[f"Attach {F['trackers']}. Run the count request on the Training sheet.", "Compare with the Control totals sheet. Ask Copilot for the rows behind the difference.",
        "Then ask for total vacancies in the Manpower sheet. Compare with the Control totals sheet.", "Find why each figure is wrong. Check it in Excel yourself."],
 prompts=[("Training: the rows behind the difference", "The Training sheet total does not match the Control totals sheet. List every request ID that appears more than once, with its row numbers."),
          ("Manpower: vacancies", "In the Manpower sheet, calculate total vacancies (approved positions minus filled). Show the result by section. Then compare with the Control totals sheet.")],
 expected=f"Training: {D.TRAIN_ROWS_EXPORT} rows, {D.TRAIN_DUPES} duplicate request IDs, true count {D.TRAIN_TRUE}. Manpower: {D.MP_VACANT_EXPORT} vacancies in the file; {D.MP_WRONG} shows 0 approved positions instead of {D.STAFF_POSITIONS}, so the true total is {D.MP_VACANT}.",
 say="Two numbers, two different reasons. Duplicates make a total too high; a missing value makes one too low.",
 point="Check every figure against a control total before it goes in a report.",
 backup=[("h", "The two figures"), tbl(["Figure", "In the file", "Correct", "Why"], [("Q3 training requests", str(D.TRAIN_ROWS_EXPORT), str(D.TRAIN_TRUE), f"{D.TRAIN_DUPES} duplicate request IDs"),
                                                                             ("Total vacancies", str(D.MP_VACANT_EXPORT), str(D.MP_VACANT), f"{D.MP_WRONG}: approved positions entered as 0")])],
 answer=[("note", f"{D.MP_WRONG} opens later, but its {D.STAFF_POSITIONS} positions are approved in the structure, so they count. Accept {D.MP_VACANT_EXPORT} only if the participant flags the 0 approved and says why."), ("h", "The two planted problems"), tbl(["Figure", "In the file", "Correct", "Cause"], [("Q3 training requests", str(D.TRAIN_ROWS_EXPORT), str(D.TRAIN_TRUE), f"{D.TRAIN_DUPES} duplicate request IDs: " + ", ".join(D.TRAIN_DUP_IDS)),
                                                                                         ("Total vacancies", str(D.MP_VACANT_EXPORT), str(D.MP_VACANT), f"{D.MP_WRONG}: approved positions 0, should be {D.STAFF_POSITIONS}")])],
 deliverable="The two corrected figures and the reason for each.",
 fallback="If upload fails, pairs use a PivotTable and Remove Duplicates in Excel.",
 hint="One total is too high and one is too low.",
 stretch=["Ask for a chart of training requests by unit after removing the duplicates. Check that the axis starts at zero."])

demo("d25", day=2, skill="2.5", sec=10, title="A brief into five slides", tool="Copilot Chat · PowerPoint", files=[F["brief"]], kind="player",
 setup=[f"Attach {F['brief']} to a new chat. (In PowerPoint with Copilot: create a presentation from the file.)", "Paste the request. Check every number against the brief."],
 prompts=[("Five slides", joined(DECK))],
 expected=f"Five slides: why the change, the new times, permissions, the pilot result ({D.ATT['pilot_drop']}% fewer late arrivals in {D.ATT['pilot_weeks']} weeks), and where to send questions.",
 say="A deck is the brief made visible. Same facts, fewer words.",
 point="Every number on a slide matches the brief.",
 backup=[("h", "Typical outline"), ("ol", ["Why we are changing attendance rules", f"Your new day: start {D.ATT['flex_from']} to {D.ATT['flex_to']}, core {D.ATT['core_from']} to {D.ATT['core_to']}",
          f"Permissions: {D.ATT['permissions']} a month, up to {D.ATT['perm_hours']} hours", f"The pilot: {D.ATT['pilot_drop']}% fewer late arrivals", "Questions: Personnel and Administration"])],
 fallback="Show the backup outline.",
 hint="Check the times and the pilot number against the brief.",
 player={"parts": DECK, "table": [["Slide", "Title"], ["1", "Why we are changing"], ["2", "Your new day"], ["3", "Permissions"], ["4", "The pilot result"], ["5", "Questions"]], "best": 4,
         "reco": ["<b>Five slides</b>, three bullets each.", "<b>Speaker notes</b> in plain English.", "<b>Check:</b> times and the pilot number."],
         "control": "Check every time and number against the brief before the meeting."})

demo("t25", day=2, skill="2.5", sec=10, title="Five slides for the managers' meeting", tool="Copilot Chat · PowerPoint", files=[F["brief"]], kind="task", hands_on=True, minutes=10, solo="on your own",
 setup=[f"Attach {F['brief']}. Run the five-slide request (or Copilot in PowerPoint).", "Check every time, date and number against the brief.", "Fix anything that changed."],
 prompts=[("Five slides", joined(DECK))],
 expected=f"A five-slide outline or deck with {D.ATT['start']}, the {D.ATT['flex_from']} to {D.ATT['flex_to']} start, core hours, {D.ATT['permissions']} permissions and the {D.ATT['pilot_drop']}% pilot result, all matching the brief.",
 say="Fast to make, quick to check. Read every number once.",
 point="Every number on a slide matches the brief.",
 backup=[("h", "The facts every slide must match"), ("ul", D.BRIEF_POINTS)],
 answer=[("h", "Facts to check"), ("ul", D.BRIEF_POINTS)],
 deliverable="A five-slide deck or outline, each number checked against the brief.",
 fallback="Without Copilot in PowerPoint, the outline from Copilot Chat is enough.",
 hint="Five facts: the date, the start window, core hours, permissions, the pilot.",
 stretch=["Ask for speaker notes in plain English, two sentences per slide."])

demo("t26", day=2, skill="2.6", sec=11, title="One case, four outputs", tool="Copilot Chat + the apps", files=CASE_FILES + [F["attendance"], F["training"], F["tpl"], F["factors"], F["v4"], F["brief"]], kind="task", hands_on=True, minutes=45, solo="on your own",
 setup=["Open the case file for your unit track.", "Output 1: a Word summary of the case. Output 2: an Outlook message to the right person.",
        "Output 3: a brief for the meeting in the case. Output 4: an Excel summary or a PowerPoint briefing.", "Run the four-point review on each output: accuracy, confidentiality, neutrality, source alignment."],
 prompts=[("Summary", "You are an HR officer at Mutla. Summarize the attached case in one page: the facts, the dates, who owns what and the open questions. Use only the case file. Neutral and plain English."),
          ("Review", "Review this draft against the attached case file. Check four things: accuracy of every date and number, any personal or confidential detail, neutral wording, and that every point comes from the file. List any problem with the line it is in.")],
 expected="Four outputs per participant, each matching the case file's dates and numbers, with no personal data and no decision that belongs to a person.",
 say="Same five inputs, four apps, one case from your own unit. Then the review.",
 point="Accuracy, confidentiality, neutrality, source alignment: before anything goes out.",
 backup=[("h", "The facts in each case")] + [x for k, n in D.TRACKS for x in (("p", f"<b>{n}:</b> {D.CASES[k]['title']}"), ("ul", D.CASES[k]["facts"]))],
 answer=[("h", "What to check in each output"), ("ul", ["Every date and number matches the case file.", "No named salary, no personal record, no medical detail.",
          "No decision that belongs to a person (a grade, an exception, a promise).", "Each output fits its reader: staff, a manager, Finance or a committee."])] +
        [x for k, n in D.TRACKS for x in (("h", f"{n} · {D.CASES[k]['title']}"), ("ul", D.CASES[k]["facts"]))],
 deliverable="Four reviewed outputs for your track's case: a Word summary, an Outlook message, a meeting brief, and an Excel summary or PowerPoint briefing.",
 fallback="Short of time: two outputs done well beat four done fast.",
 hint="Start with the summary; the other three outputs reuse it.",
 stretch=["Write your own review request for the riskiest output in your case, without copying the Review request on the prompt sheet. Add it to the Prompt Bank under Review."])

# ===================================================================== DAY 3
demo("d31", day=3, skill="3.1", sec=12, title="Adapt a suggested prompt", tool="Copilot Chat · Prompt Gallery", files=[F["training"]], kind="player",
 setup=["In Copilot Chat, open the Prompt Gallery (the More options (...) button or a prompt pill below the message box). Find a prompt about a team email.", "Adapt it with the five inputs. Save it under Your Prompts."],
 prompts=[("Adapted prompt", joined(GALLERY[1:]))],
 expected="A suggested prompt from the gallery turned into Mutla's nomination email request, saved under Your Prompts.",
 say="Start from a suggested prompt, add the five inputs, save it once, use it every month.",
 point="Find, adapt, save, share.",
 backup=[("h", "The adapted prompt"), ("p", joined(GALLERY[1:]))],
 fallback="If the gallery does not open, show the backup prompt and save it in the Prompt Bank in Word.",
 hint="Your Prompts holds what you save; Teams holds what your team shares.",
 player={"parts": GALLERY, "table": [["Where", "What is there"], ["Suggested", "Prompts from Microsoft"], ["Your Prompts", "Prompts you saved"], ["Teams", "Prompts shared with your team"]], "best": 1,
         "reco": ["<b>Suggested</b> is a start, not an answer.", "<b>Add the five inputs</b>, then save.", "<b>Share</b> the tested ones with your team."],
         "control": "Test a prompt on a fictional file before you share it with your team."})

demo("t31", day=3, skill="3.1", sec=12, title="Save your best three", tool="Copilot Chat · Prompt Gallery", files=[F["bank"], F["catchbank"]], kind="task", hands_on=True, minutes=10, solo="on your own",
 setup=[f"Open your Prompt Bank (or {F['catchbank']} if you missed a day).", "Pick your three best tested requests.", "Save each one in the Prompt Gallery under Your Prompts, with a clear name.", "Organize the Prompt Bank by task: Draft, Compare, Summarize, Review."],
 prompts=[],
 expected="Three requests saved under Your Prompts with clear names, and a Prompt Bank organized by task.",
 say="The best request is the one you already tested. Save it where you will find it.",
 point="Saved, named, organized.",
 backup=[("h", "Good prompt names"), ("ul", ["JD · draft from role sheet (5 inputs)", "Policy · compare two versions", "Thread · decisions and owners", "Review · four-point check"])],
 answer=[("h", "Check"), ("ul", ["Three prompts saved with names that say the task.", "Each prompt has the five inputs.", "The Prompt Bank has task headings."])],
 deliverable="Three tested requests saved under Your Prompts and a Prompt Bank organized by task.",
 fallback="If saving in the gallery fails, the Prompt Bank in Word is enough.",
 hint="Name each prompt by its task, so you find it in a month.",
 stretch=["Share one prompt with a team, if your account has one."])

demo("d32", day=3, skill="3.2", sec=13, title="The assistant's instructions, part by part", tool="Agent Builder", files=[F["leave"], F["v3"], F["v4"], F["attendance"], F["training"]], kind="player",
 setup=["In Microsoft 365 Copilot, choose New agent, then Configure.", "Name, description, then paste the instructions.", "Add the five policy files under Knowledge. Test in Try it."],
 prompts=[("Instructions", joined(AGENT))],
 expected="An assistant that answers from the four policies with the section, asks for the grade before an allowance answer, and declines a named person's salary.",
 say="Instructions are the script, knowledge is the binder, Try it is the rehearsal.",
 point="Instructions decide what it may answer, and when it refers to HR.",
 backup=[("h", "Three tests and what passes"), tbl(["Test", "Question", "A pass looks like", "Result"], D.AGENT_TESTS)],
 fallback="If Agent Builder is not available, show the backup tests and build the same instructions as a saved request in Copilot Chat.",
 hint="Test the sensitive question last. It must decline and refer.",
 player={"parts": AGENT, "table": [["Test", "Question", "Pass if"]] + [[a, b, d] for a, b, _c, d in D.AGENT_TESTS], "best": 2,
         "reco": ["<b>Knowledge:</b> five policy files, each with its dates.", "<b>Must not answer:</b> named salaries, decisions.", "<b>Refer:</b> personal records go to HR."],
         "control": "Test with a normal, an incomplete and a sensitive question before anyone else uses it."})

demo("t32", day=3, skill="3.2", sec=13, title=f"Build the {D.AGENT_NAME}", tool="Agent Builder", files=[F["leave"], F["v3"], F["v4"], F["attendance"], F["training"]], kind="task", hands_on=True, minutes=30, solo="on your own",
 setup=["New agent → Configure. Name it and write a one-line description.", "Paste the instructions from Demo 3.2 on the prompt sheet. Add the five policy files under Knowledge.",
        "In Try it, ask the three test questions. Write a test log: question, answer, pass or fix.", "Fix one instruction that failed, then test again. Create the agent."],
 prompts=[(f"Test · {a}", b) for a, b, _c, _d in D.AGENT_TESTS],
 expected="A working assistant and a three-line test log. It cites the section, asks for the grade before the transport answer, and declines the named salary.",
 say="Build it, then test it with hard questions. A test you did not run is a problem you will meet later.",
 point="Normal, incomplete, sensitive: three tests before anyone uses it.",
 backup=[("h", "The three tests"), tbl(["Test", "Question", "A pass looks like", "Result"], D.AGENT_TESTS)],
 answer=[("h", "Pass marks"), tbl(["Test", "Question", "A pass looks like", "Result"], D.AGENT_TESTS), ("h", "Finished early: the fourth test"), tbl(["Test", "Question", "A pass looks like"], [D.AGENT_TEST4])],
 deliverable="A working assistant and a three-line test log.",
 fallback="No Agent Builder on your account: save the instructions as a request in Copilot Chat, attach the five policy files, and run the same three tests. Or pair with a neighbor.",
 hint="If it answers the salary question, add a clearer line under Must not answer.",
 stretch=[f"Extend the assistant to a second scenario: {D.AGENT_SCENARIO2[0].lower() + D.AGENT_SCENARIO2[1:]}. Add two starter prompts for it, then run a fourth test with a question the files do not cover. It must refer the person to HR."],
 stretch_prompts=[("Test 4 · Out of scope", D.AGENT_TEST4[1])])

# ===================================================================== capstone and peer-test keys (staff only), computed from data.py
def _months(a, b): return (b[0] - a[0]) * 12 + (b[1] - a[1]) - (1 if b[2] < a[2] else 0)
def _leave_key(rows, when):
    cap = D.LEAVE["carry"]
    over = [c for c, _u, b, _p in rows if b > cap]
    after = [c for c, _u, b, p in rows if b - p > cap]
    edge = [c for c, _u, b, _p in rows if b == cap]
    line = f"Balance over {cap} days ({when}): {', '.join(over)}. Still over {cap} after the days they planned: {', '.join(after)} (the exceptions for line managers)."
    return line + (f" {', '.join(edge)} has exactly {cap} days: not over the limit." if edge else "")
def _vac_key(rows, asof, label):
    old = [f"{pos} (since {o[2]} {['January','February','March','April','May','June','July','August','September','October','November','December'][o[1]-1]})" for pos, _s, o, _st, _b in rows if _months(o, asof) > 6]
    blocked = [f"{pos}: {b[0].lower() + b[1:]}" for pos, _s, _o, _st, b in rows if not b.startswith("None")]
    edge = [pos for pos, _s, o, _st, _b in rows if _months(o, asof) == 6]
    line = f"{len(rows)} open positions ({label}). Open for more than 6 months: {'; '.join(old)}. Blocked or waiting: {'; '.join(blocked)}."
    return line + (f" {', '.join(edge)}: just over 6 months. Accept it in either list if the report says why." if edge else "")
A = D.ALLOW
CAP_KEY = [
 ("Job Evaluation and Salary Scaling", "Three job descriptions in the template order. Evidence notes under the five factors. No grade, no team size, no duty that is not in the role information."),
 ("Compensation", f"EMP-3021: 25% of basic salary, up to KWD {A['housing_v4']} from {D.ALLOW_V4_DATE}. EMP-5532 (grade 7): yes from {D.ALLOW_V4_DATE} (grades {A['transport_v4']}), KWD {A['transport']}; the reply must give the date. "
                  f"EMP-2290: KWD {A['child'] * A['child_max']} (KWD {A['child']} for up to {A['child_max']} children). EMP-6104: {A['remote_pct']}% of basic salary for February (more than {A['remote_days']} days, new section 5). "
                  "EMP-4417: decline. Another employee's allowance is confidential. Remove the colleague's name before prompting; the reply names nobody. EMP-7785: the housing allowance stops; tell Personnel and Administration within 30 days."),
 ("Manpower", _vac_key(D.VAC_OCT, (2026, 10, 31), "31 October") + " Last month's example said 8 open and 2 over 6 months: the new report must use the October data, not copy September."),
 ("Personnel and Administration", _leave_key(D.LEAVE_OCT, "31 October") + " Employee codes only in every prompt and reminder."),
 ("Learning and Development", "One comment insults the Safety leadership trainer. The trainer summary reports it neutrally (one participant was very unhappy with the trainer's style) and never quotes the insult. The low rating from a participant whose laptop had no Excel is a logistics point, not a trainer point."),
]
FRESH_KEY = [
 ("Job Evaluation and Salary Scaling", "Payroll Officer: the same template order and five factors. No grade, no team size."),
 ("Compensation", f"EMP-3388 (grade 8): yes from {D.ALLOW_V4_DATE}, KWD {A['transport']}. EMP-4120: the allowance for that child stops when he turns 18. EMP-5076: 12 days is not more than {A['remote_days']}, so no remote-site allowance. EMP-6231: request it in the HR system; Compensation checks it and the Compensation Supervisor approves."),
 ("Manpower", _vac_key(D.VAC_NOV, (2026, 11, 15), "15 November")),
 ("Personnel and Administration", _leave_key(D.LEAVE_NOV, "15 November")),
 ("Learning and Development", "One comment names a participant (Saud from Drilling). The summary removes the name and keeps the point: phones were a distraction."),
]

demo("t33", day=3, skill="3.3", sec=14, title="A tested workflow for a new case, in two parts", tool="Copilot Chat + the apps", files=CAP_FILES + [F["tpl"], F["factors"], F["leave"], F["v4"], F["training"], F["bank"]], kind="task", hands_on=True, minutes=100, solo="on your own",
 setup=["Open the capstone case for your track. It is new to you. Part 1 runs to 11:35; part 2 runs 12:15 to 13:30.", "Plan the steps: which outputs, which app, which files.",
        "Write five-input requests for each step. Chain at least two Copilot apps.", "Review every output with the four-point check.", "Save the requests as a reusable prompt set in Word."],
 prompts=[("Plan the workflow", "You are an HR officer at Mutla. Read the attached capstone case. List the steps to complete this recurring task with Copilot: for each step, the output, the app, the files and the check. Do not do the task yet.")],
 expected="A finished set of outputs for the case and a reusable prompt set in Word: every request has the five inputs, cites its files and ends with a check.",
 say="A new case proves the method, not your memory. Plan, request, review, save.",
 point="Chain two apps, review every output, save the set.",
 backup=[("h", "The five capstone cases")] + [x for k, n in D.TRACKS for x in (("p", f"<b>{n}: {D.CAPSTONE[k]['title']}.</b> {D.CAPSTONE[k]['task']}"),)],
 answer=[("h", "Self-check (also on the Day 3 lab page)"), ("ul", C.SELFCHECK), ("h", "What each case file tests"), tbl(["Track", "A good set catches this"], CAP_KEY)] + [x for k, n in D.TRACKS for x in (("h", f"{n} · {D.CAPSTONE[k]['title']}"), ("p", D.CAPSTONE[k]["task"]), ("ul", D.CAPSTONE[k]["inputs"]))],
 deliverable="The outputs for your case and a reusable prompt set in Word.",
 fallback="Short of time: one step done and reviewed is better than four unchecked.",
 hint="Start with the plan request. It turns the case into steps.",
 stretch=["Connect the workflow to your HR assistant, or turn one request into a starter prompt."])

demo("t34", day=3, skill="3.4", sec=14, title="Peer test", tool="A colleague + Copilot", files=[F["fresh"]], kind="task", hands_on=True, minutes=20, solo="in pairs",
 setup=["Swap with a colleague from a different unit.", f"Run their prompt set on their track's fresh input in {F['fresh']}. Ask them nothing.",
        "Write down where it failed or where you had to guess.", "Swap back. Fix your set and write the fix into it."],
 prompts=[],
 expected="Each pair finds at least one place where a set depended on something only its owner knew, and writes one fix into it.",
 say="If a colleague needs you to explain your prompt set, it is not finished yet.",
 point="Work someone else can run with no instructions.",
 backup=[("h", "Common fixes after a peer test"), ("ul", ["Name the files the request needs.", "Say what to do when data is missing.", "Add the output format.", "Add the check step at the end."])],
 answer=[("h", "Check"), ("ul", ["The colleague ran the set without help.", "At least one fix is written into the set.", "The fix is a missing input, not a new task."]), ("h", "What each fresh input tests"), tbl(["Track", "A good set catches this"], FRESH_KEY)],
 deliverable="One fix written into your prompt set.",
 fallback="Odd number: a group of three, in a circle.",
 hint="Watch where your colleague stops to ask. That is your fix.",
 stretch=["Run a second colleague's set."])

# ===================================================================== the weak and strong opener (Day 1)
SHOWCASE = {
 "eyebrow": "Opener · one job description", "title": "Same tool. Same role. <span class=\"hl\">Two requests.</span>", "tool": "Copilot Chat", "file": F["roles"],
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

# hub stat strip: the card sort is not a prompt demo
C.HUB["stats"] = [(len(C.DAYS), "days"), (None, "slides"), (sum(1 for v in DEMOS.values() if v.get("hands_on")), "hands-on tasks"),
                  (sum(1 for v in DEMOS.values() if not v.get("hands_on") and v.get("kind") != "sort"), "prompt demos"),
                  (len(ALL_FILES), "sample files"), (len(C.MAP), "MAP questions")]
