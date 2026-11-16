# -*- coding: utf-8 -*-
"""The fictional sample files for AI Fundamentals for HR (Mutla Oil Company).
    python3 gen_files.py OUTDIR        (the kit keeps them in ../files; the site copies them unchanged)
Names never change once built: participants download them. Every fact and number comes from data.py.
The planted problems are deliberate: three wrong leave statements, six sensitive items in the case note,
two unsupported lines in the catch-up job description, one superseded date in the thread, one opinion in the
investigation notes, 14 duplicate training rows and one section entered with 0 approved positions."""
import sys, os, re, io, zipfile, datetime as dt
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import data as D
import content as C
from content_demos import F, CASE_FILES, ALL_FILES, DEMOS, JD_CMP, TRACE, THREAD, RECAP, TRACKER, DECK, COMPARE, LETTER_FLAG, joined

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "files")
os.makedirs(OUT, exist_ok=True)
FIXED = dt.datetime(2026, 11, 9, 9, 0, 0)
STAMP = FIXED.strftime("%Y-%m-%dT%H:%M:%SZ")
HEADER = f"{D.COMPANY} (fictional) · training file made by CODED"
GREY = RGBColor(0x55, 0x5F, 0x6D)
NAVY = "00112F"
A = D.ATT
WRITTEN = []

def grab(pattern, text):
    """A value taken from a sentence in data.py, so the files never retype it."""
    m = re.search(pattern, text)
    assert m, f"gen_files: {pattern!r} not found in {text!r}"
    return m.group(1)

# ------------------------------------------------------------------ byte-stable zips (python-docx and openpyxl stamp the clock)
def _stable(path):
    raw = open(path, "rb").read()
    zin = zipfile.ZipFile(io.BytesIO(raw)); buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == "docProps/core.xml":
                data = re.sub(rb"(<dcterms:modified[^>]*>)[^<]*(</dcterms:modified>)", rb"\g<1>" + STAMP.encode() + rb"\g<2>", data)
            zi = zipfile.ZipInfo(info.filename, date_time=FIXED.timetuple()[:6])
            zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = info.external_attr
            zout.writestr(zi, data)
    open(path, "wb").write(buf.getvalue())

# ------------------------------------------------------------------ Word helpers
def _shade(cell, fill):
    pr = cell._tc.get_or_add_tcPr(); s = OxmlElement("w:shd")
    s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), fill); pr.append(s)

def _table(d, rows, widths=None, height=None):
    """A real Word table. Row 0 is the header row."""
    t = d.add_table(rows=0, cols=len(rows[0])); t.style = "Table Grid"
    for i, r in enumerate(rows):
        row = t.add_row()
        if height and i: row.height = Cm(height)
        for j, v in enumerate(r):
            c = row.cells[j]; c.text = str(v)
            if widths: c.width = Cm(widths[j])
            if i == 0:
                for run in c.paragraphs[0].runs: run.bold = True
                _shade(c, "E3ECFB")
    if widths:
        for j, w in enumerate(widths): t.columns[j].width = Cm(w)
    d.add_paragraph()

def _box(d, title, lines):
    t = d.add_table(rows=1, cols=1); t.style = "Table Grid"
    c = t.rows[0].cells[0]; _shade(c, "F2F4F8")
    c.paragraphs[0].add_run(title).bold = True
    for x in lines: c.add_paragraph(x, style="List Bullet")
    d.add_paragraph()

def doc(name, title, blocks, top=None):
    d = Document()
    st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11)
    hr = d.sections[0].header.paragraphs[0].add_run(HEADER); hr.font.size = Pt(8); hr.font.color.rgb = GREY
    if top:
        tr = d.add_paragraph().add_run(top); tr.bold = True; tr.font.size = Pt(9.5); tr.font.color.rgb = GREY
    d.add_heading(title, 1)
    for b in blocks:
        kind, val = b[0], (b[1] if len(b) > 1 else None)
        if kind == "p": d.add_paragraph(val)
        elif kind == "i": d.add_paragraph().add_run(val).italic = True
        elif kind == "lbl": d.add_paragraph().add_run(val).bold = True
        elif kind == "b": d.add_paragraph(val, style="List Bullet")
        elif kind == "h": d.add_heading(val, 2)
        elif kind == "h3": d.add_heading(val, 3)
        elif kind == "kv":
            p = d.add_paragraph(); p.add_run(val[0] + ": ").bold = True; p.add_run(val[1])
        elif kind == "qa":
            for lab, txt in (("Q", val[0]), ("A", val[1])):
                p = d.add_paragraph(); p.add_run(lab + ": ").bold = True; p.add_run(txt)
        elif kind == "sp":                                   # a transcript line: "Name  [10:03]: text"
            p = d.add_paragraph(); p.add_run(f"{val[0]}  [{val[1]}]").bold = True; p.add_run(": " + val[2])
        elif kind == "t": _table(d, val, *b[2:])
        elif kind == "box": _box(d, *val)
        elif kind == "pb": d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        else: raise ValueError(f"gen_files: unknown block {kind}")
    d.add_paragraph().add_run(D.FICTION).italic = True
    cp = d.core_properties
    cp.author = "CODED"; cp.title = title; cp.created = FIXED; cp.modified = FIXED; cp.last_modified_by = "CODED"
    cp.comments = "Fictional training file made by CODED."
    path = os.path.join(OUT, name); d.save(path); _stable(path); WRITTEN.append(name)

def policy(name, title, sections, intro):
    doc(name, title, [("p", intro)] + [x for n, t, s in sections for x in (("h", f"Section {n}. {t}"), ("p", s))])

def role_blocks(r, head=None, hk="h"):
    b = [(hk, head)] if head else []
    b += [("kv", ("Job title", r["title"])), ("kv", ("Unit", r["unit"])), ("kv", ("Reports to", r["reports"])),
          ("kv", ("Purpose", r["purpose"])), ("lbl", "Duties")]
    b += [("p", f"Duty {i}: {x}.") for i, x in enumerate(r["duties"], 1)]
    return b + [("kv", ("Qualifications", r["quals"])), ("kv", ("Working relationships", r["works"]))]

RULES_LINE = ("kv", ("Rules", "use approved files only; no names in prompts; a person decides."))

# ================================================================== DAY 1
# 1 · leave policy (the source)
policy(F["leave"], f"{D.COMPANY} · Leave Policy {D.YEAR}", D.LEAVE_SECTIONS,
       "Owner: Personnel and Administration. This is the approved version.")

# 2 · a Copilot answer with exactly three wrong statements (D.LEAVE_ERRORS) and two right ones; no other numbers
L = D.LEAVE
doc(F["answer"], "Copilot answer: leave questions from an employee (check before sending)", [
    ("i", "Saved by an HR officer from Copilot Chat. Not checked yet."),
    ("p", "An employee asked five questions about leave. Copilot answered:"),
    ("qa", ("How many days of annual leave do I get each year?", f"You get {L['annual']} days of annual leave a year.")),
    ("qa", ("Can I carry over the leave I do not use?", "Yes. " + D.LEAVE_ERRORS[0][1])),
    ("qa", ("How much emergency leave can I take?", D.LEAVE_ERRORS[1][1])),
    ("qa", ("How early must I request annual leave?", D.LEAVE_ERRORS[2][1] + " Your line manager approves the request.")),
    ("qa", ("Can I take Hajj leave?", f"Yes. You can take {L['hajj']} days of Hajj leave once in your service.")),
    ("p", "I hope this helps. For your own leave balance, please contact Personnel and Administration."),
])

# 3 · the case note with six sensitive items (D.CASE_SENSITIVE) and neutral facts
S = [b for _a, b, _c in D.CASE_SENSITIVE]          # name, colleague, civil ID, mobile, salary, medical reason
doc(F["case"], "Case note: request for a phased return to work", [
    ("kv", ("Prepared by", "Personnel Officer, Personnel and Administration")),
    ("kv", ("Date", "Monday 9 November 2026")),
    ("p", f"1. {S[0]} (civil ID {S[2]}, mobile {S[3]}) works in Production Operations. He was absent on sick leave from 12 October to 2 November 2026."),
    ("p", f"2. The sick leave was for {S[5]}. Medical Services holds the medical certificate."),
    ("p", "3. On 3 November he asked for a phased return to work: 4-hour days for 2 weeks, then full days."),
    ("p", f"4. His colleague {S[1]} has covered his main duties since 12 October. She says the team can support a phased return."),
    ("p", f"5. Compensation asked how shorter days affect his pay. He has a {S[4]} a month. Not decided."),
    ("p", "6. Next step: a meeting with his line manager on Tuesday 10 November to agree the return plan. Personnel and Administration records the outcome in the HR system."),
], top="Personnel and Administration · Case note (training copy: redact before using any AI tool)")

# 4 · the outdated 2019 job description: old layout, none of the template headings
O = D.OLD_JD
doc(F["oldjd"], f"{D.COMPANY.upper()} · JOB DESCRIPTION", [
    ("kv", ("Position", O["title"])), ("kv", ("Department", "Personnel")), ("kv", ("Issued", str(O["year"]))),
    ("kv", ("Grade", "5")), ("kv", ("Supervises", "none")),
    ("lbl", "DUTIES AND RESPONSIBILITIES:"),
] + [("p", f"{chr(97 + i)}) {x}.") for i, x in enumerate(O["duties"])] + [
    ("kv", ("Requirements", "Secondary school certificate. Typing skills. Good handwriting.")),
    ("p", "Other duties as assigned by the supervisor."),
])

# 5 · the 2026 template: one heading per D.JD_TEMPLATE item, a guidance note, a rules box
GUIDE = ["Use the title in the approved role information. Do not add words like senior or lead.",
         "The unit name in the approved structure.",
         "The job title of the direct manager, not a person's name.",
         "One sentence: what the job does and why it matters to Mutla.",
         "5 to 8 duties. Each starts with a verb. Only duties in the approved role information.",
         "The degree, years of experience and key skills in the role information.",
         "The main units and people the job works with, inside and outside Mutla.",
         "Leave this line blank. The Job Evaluation committee sets the grade."]
assert len(GUIDE) == len(D.JD_TEMPLATE)
doc(F["tpl"], f"Job Description Template {D.YEAR}",
    [("p", "Use this template for every new or updated job description. Keep the headings in this order. One page.")] +
    [x for h, g in zip(D.JD_TEMPLATE, GUIDE) for x in (("h", h), ("i", g))] +
    [("box", ("Rules", ["No team size unless the role information gives one.",
                        "The grade is left blank. The Job Evaluation committee sets it.",
                        "No salary or allowance figures.",
                        "Plain English and a neutral tone: no sales language."]))])

# 6 · approved role information: one role per track, no grade, no team size, no salary
doc(F["roles"], f"Approved role information {D.YEAR}",
    [("p", f"Approved by HR for the {D.YEAR} job evaluation round. One role for each unit track. Use only these facts in a job description."),
     ("p", "Grades are not part of this file. The Job Evaluation committee sets them.")] +
    [x for k, n in D.TRACKS for x in role_blocks(D.ROLES[k], f"{n} track: {D.ROLES[k]['title']}")])

# 7 · the catch-up Copilot draft: correct except the two lines in D.JD_UNSUPPORTED
R = D.ROLES["cmp"]
_duties = R["duties"][:2] + [D.JD_UNSUPPORTED[0][0]] + R["duties"][2:]
doc(F["catchjd"], f"Copilot draft: {R['title']} job description (catch-up file, check before use)", [
    ("i", "Made with Copilot from the role information. Not checked yet."),
    ("kv", ("Job title", R["title"])), ("kv", ("Unit", R["unit"])), ("kv", ("Reports to", R["reports"])),
    ("kv", ("Job purpose", R["purpose"])),
    ("lbl", "Key duties"),
] + [("b", x) for x in _duties] + [
    ("kv", ("Qualifications and experience", R["quals"])),
    ("kv", ("Working relationships", R["works"])),
    ("kv", ("Grade", D.JD_UNSUPPORTED[1][0])),
])

# 8 · the Prompt Bank template (and 25 · the catch-up bank in the same layout)
BANK_HEAD = ["Task", "Request", "Files", "Check"]
BANK_W = [3.0, 7.4, 3.0, 3.0]
BANK_SECTIONS = ["Draft", "Compare", "Summarize", "Review"]
def bank_intro():
    return [("p", "Save every request that worked, so you never start from a blank page. One line per entry:"),
            ("b", "Task: what you needed, in a few words."),
            ("b", "Request: the full request, with the seven parts of the prompt checklist (" + ", ".join(a.lower() for a, _b, _c in D.INPUTS) + ")."),
            ("b", "Files: the approved files you attached."),
            ("b", "Check: how you checked the result before it went out.")]
doc(F["bank"], "My HR Prompt Bank",
    bank_intro() + [("kv", ("Name", "____________________")), ("kv", ("Unit track", "____________________"))] +
    [x for h in BANK_SECTIONS for x in (("h", h), ("t", [BANK_HEAD] + [[""] * 4] * 2, BANK_W, 1.6))])

# 8b · experience letters (Task 1.4): the approved template and its rules, the HR system record, three requests (two with planted problems)
doc(F["letters"], "Experience letter requests: November 2026", [
    ("i", "Personnel and Administration. Three requests arrived this week. Use the template and its rules for every letter."),
    ("h", "1. The approved template"), ("p", D.LETTER_TEMPLATE),
    ("box", ("Template rules", D.LETTER_RULES)),
    ("h", "2. The HR system record"),
    ("t", [["Employee code", "Name", "Job title", "Unit", "Start date", "End date"]] + [list(r) for r in D.LETTER_RECORD], [2.4, 3.2, 3.2, 3.2, 2.6, 2.6]),
    ("h", "3. The requests"),
] + [x for code, name, text in D.LETTER_REQUESTS for x in (("lbl", f"{code} · {name}"), ("p", f"“{text}”"))])

# ================================================================== DAY 2
# 9 and 10 · allowances policy v3 and v4 (only the title and the sections differ)
for v, date in ((3, D.ALLOW_V3_DATE), (4, D.ALLOW_V4_DATE)):
    policy(F[f"v{v}"], f"{D.COMPANY} · Allowances Policy, version {v} (applies from {date})", D.allowances_sections(v), "Owner: Compensation.")

# 11 · the five evaluation factors
doc(F["factors"], "Job Evaluation Factors", [
    ("p", "The Job Evaluation committee uses five factors to evaluate every job at Mutla. An evidence file gives the facts for each factor, with the source of each fact."),
    ("t", [["Factor", "What it measures"]] + [[a, b] for a, b in D.FACTORS], [5.0, 11.0]),
    ("h", "The rule"),
    ("p", "The committee sets the level and the grade. Evidence files never suggest a grade."),
    ("h", "How to prepare an evidence file"),
    ("b", "One row for each factor, with the factor names above."),
    ("b", "For each fact, give its source (for example, the note number)."),
    ("b", "Leave the level column blank. It is for the committee."),
    ("b", "Facts only: no opinion about the level of the job."),
])

# 13 · the 30-message email thread
YS, FA, KA = f"{D.HEAD} (HR Section Head)", f"{D.P['pa']} (Personnel and Administration)", f"{D.P['mp']} (Manpower)"
AM, HK, NR = f"{D.P['cmp']} (Compensation)", f"{D.P['je']} (Job Evaluation and Salary Scaling)", f"{D.P['ld']} (Learning and Development)"
HD, MH = "Hamad Al-Dosari (IT)", "Mubarak Al-Harbi (Production)"
BO, MA, DS = "Bashayer Al-Otaibi (Finance)", "Mishari Al-Azmi (Drilling Operations)", "Dalal Al-Saleh (HSE)"
APPROVED_ON = "Monday 9 November 2026"
OLD = " ".join(A["old_start"].split()[1:3])            # "15 November"
TIMES = f"flexible start between {A['flex_from']} and {A['flex_to']}, core hours {A['core_from']} to {A['core_to']}, {A['hours']} working hours a day"
PERMS = f"up to {A['permissions']} permissions a month, each up to {A['perm_hours']} hours, with line manager approval"
MSGS = [
 (YS, "Sunday 1 November 2026, 8:05", ["Dear all, late arrivals at head office keep rising. I would like new attendance rules for all staff, based on the Finance pilot.", "Please send your comments in this thread by Thursday 5 November."]),
 (BO, "Sunday 1 November 2026, 9:20", [f"Happy to share our results. In our {A['pilot_weeks']}-week pilot in the {A['pilot_unit']}, late arrivals fell by {A['pilot_drop']}%.", "Staff liked the flexible start most."]),
 (FA, "Sunday 1 November 2026, 10:45", [f"Thank you, Bashayer. I propose we start the new rules on {A['old_start']}.", "I will share the draft times tomorrow."]),
 (HD, "Monday 2 November 2026, 8:30", [f"{OLD} is too early for IT. We must set up the new rules in the attendance system and test them.", "We need about three weeks after the rules are approved."]),
 (KA, "Monday 2 November 2026, 9:10", ["One question: do the new rules cover field staff on rotation? Their shifts work differently."]),
 (FA, "Monday 2 November 2026, 13:15", [f"Draft times, as in the Finance pilot: {TIMES}.", f"Permissions: {PERMS}.", "The draft table is attached."]),
 (MA, "Monday 2 November 2026, 14:02", ["Agreed from Drilling Operations. Most of my team already starts early."]),
 (NR, "Monday 2 November 2026, 15:30", [f"Good idea. Our courses start at {A['core_from']}, so this works for Learning and Development."]),
 (DS, "Tuesday 3 November 2026, 8:15", ["What happens in Ramadan? Working hours are shorter then."]),
 (FA, "Tuesday 3 November 2026, 9:00", ["Good question, Dalal. Ramadan hours are not decided yet. I will raise it with Yousef."]),
 (MA, "Tuesday 3 November 2026, 10:12", ["Fatma, can we talk about my team's overtime claims next week? Thursday morning is best for me."]),
 (MA, "Tuesday 3 November 2026, 10:14", ["Apologies, everyone. My last message was meant for Fatma only. Please ignore it."]),
 (HD, "Tuesday 3 November 2026, 12:40", ["To be clear: IT can be ready only if the start date moves to 1 December or later."]),
 (AM, "Tuesday 3 November 2026, 14:05", ["Agreed. The new rules do not change any allowance, so nothing changes for Compensation."]),
 (KA, "Wednesday 4 November 2026, 8:45", ["Following up on my question about field staff on rotation. Any view?"]),
 (FA, "Wednesday 4 November 2026, 9:30", ["Khaled, I am not sure yet. Can Manpower check which rotation groups the rules would cover?"]),
 (KA, "Wednesday 4 November 2026, 10:05", ["Yes, Manpower will check. It will take some time, because each field site has its own shift schedule."]),
 (FA, "Wednesday 4 November 2026, 11:40", [f"Correction: the table attached to my message of 2 November shows 6:00 as the earliest start. That is a typing error. The earliest start is {A['flex_from']}, as written in the email."]),
 (BO, "Wednesday 4 November 2026, 12:10", ["Thanks for the correction. In the pilot, staff asked for permissions in the HR system. It worked well."]),
 (HK, "Wednesday 4 November 2026, 13:30", ["Agreed. No effect on job descriptions or grades from our side."]),
 (DS, "Thursday 5 November 2026, 9:15", ["Agreed for HSE. Please remember the shift workers at the field sites."]),
 (FA, "Thursday 5 November 2026, 11:00", [f"Thank you, all. Yousef, for your approval: start on {A['start']}, because IT needs the time.",
                                         f"The times: {TIMES}. Permissions: {PERMS}.", "Still open: Ramadan hours, and field staff on rotation (Manpower is checking)."]),
 (YS, "Sunday 8 November 2026, 8:10", ["Thank you, Fatma. I will review it today and reply tomorrow."]),
 (YS, f"{APPROVED_ON}, 8:30", [f"Approved. The new attendance rules start on {A['start']}, not on {OLD}.",
                               f"Flexible start between {A['flex_from']} and {A['flex_to']}; core hours {A['core_from']} to {A['core_to']}; {A['hours']} working hours a day.",
                               f"Up to {A['permissions']} permissions a month, each up to {A['perm_hours']} hours, with line manager approval."]),
 (FA, "Monday 9 November 2026, 9:05", [f"Thank you, Yousef. I will send the staff announcement by {A['announce_by']}."]),
 (HD, "Monday 9 November 2026, 10:20", [f"Noted. IT will update the attendance system by {A['system_by']}."]),
 (YS, "Monday 9 November 2026, 11:00", [f"Agreed. Fatma: the staff announcement by {A['announce_by']}. Hamad: the attendance system by {A['system_by']}.",
                                        "Ramadan hours and field staff on rotation stay open for now."]),
 (BO, "Tuesday 10 November 2026, 8:40", ["Great news. Finance already works this way, so nothing changes for my team."]),
 (MH, "Wednesday 11 November 2026, 7:15", ["Dear Fatma, can I start at 6:00 under the new rules?", "Then I can collect my children from school after my shift."]),
 (FA, "Thursday 12 November 2026, 8:00", ["Thank you, Mubarak. I will reply to you directly this week."]),
]
assert len(MSGS) == 30 and MSGS[23][0] == YS and MSGS[2][2][0].endswith(A["old_start"] + ".") and MSGS[28][0] == MH
assert D.ATT_DECISIONS[2][1] == D.P["pa"] and D.ATT_DECISIONS[3][1].startswith("Hamad Al-Dosari")
doc(F["thread"], "Email thread (exported): New attendance rules",
    [("kv", ("Subject", "New attendance rules")), ("kv", ("To", "HR team; line managers")),
     ("i", "Exported from Outlook on 12 November 2026. 30 messages, oldest first.")] +
    [x for i, (who, when, lines) in enumerate(MSGS, 1) for x in [("h3", f"Message {i}"), ("kv", ("From", who)), ("kv", ("Date", when))] + [("p", l) for l in lines]])

# 14 · the staffing meeting transcript
MPF = D.CASES["mp"]["facts"]
POS = [(int(x.split(" ", 1)[0]), x.split(" ", 1)[1]) for x in MPF[1].split(": ", 1)[1].rstrip(".").split(", ")]
assert sum(n for n, _l in POS) == D.STAFF_POSITIONS
POS_TEXT = ", ".join(f"{n} {l}" for n, l in POS[:-1]) + f" and {POS[-1][0]} {POS[-1][1]}"
OPENS = grab(r"section on (.+?)\.$", MPF[0])
ACT = {D.P[k].split()[0]: (a, dl) for a, owner, dl in D.STAFF_ACTIONS for k in D.P if D.P[k] == owner}
assert set(ACT) == {"Khaled", "Abdulaziz", "Noura", "Hessa"}
N = D.STAFF_POSITIONS
LD_PLAN, LD_BY = ACT["Noura"][1].split(" by ")
YSn, KAn, AMn, NRn, HKn = D.HEAD, D.P["mp"], D.P["cmp"], D.P["ld"], D.P["je"]
LINES = [
 (YSn, "10:00", f"Good morning, everyone. Thank you for joining. Today we agree the staffing of the new {D.NEW_SECTION} section."),
 (YSn, "10:01", f"The section opens on {OPENS}. I want clear owners and dates before we leave."),
 (KAn, "10:02", f"Thank you, Yousef. The approved structure has {N} positions."),
 (KAn, "10:02", f"That is {POS_TEXT}."),
 (HKn, "10:03", "Are all of these existing job titles at Mutla?"),
 (KAn, "10:04", "Most of them. The engineers and the technicians use existing titles from Drilling Operations."),
 (HKn, "10:04", "Then the section head and the coordinator are new job titles. They need an evaluation."),
 (YSn, "10:05", f"Agreed. Hessa, please evaluate the two new job titles by {ACT['Hessa'][1]}."),
 (HKn, "10:06", f"Yes. The Job Evaluation committee meets on {ACT['Hessa'][1]}. I will take both titles to that meeting."),
 (KAn, "10:07", f"For the manpower request: Finance needs it by {ACT['Khaled'][1]}."),
 (YSn, "10:08", f"Then that is yours, Khaled. The manpower request for the {N} positions, by {ACT['Khaled'][1]}."),
 (KAn, "10:08", "Agreed."),
 (KAn, "10:09", "Recruitment asked about the hiring order. They want the section head first, then the engineers."),
 (YSn, "10:09", "That makes sense. Please include it in the manpower request."),
 (AMn, "10:10", f"Finance will also ask what the {N} positions cost. I can price them from the salary scales."),
 (YSn, "10:11", f"Please do, Abdulaziz. Send the cost estimate to Finance by {ACT['Abdulaziz'][1]}."),
 (AMn, "10:11", f"{ACT['Abdulaziz'][1]}. Fine."),
 (AMn, "10:12", "One question. Two of the technician positions: are they contract or permanent? The cost is different."),
 (KAn, "10:13", "Drilling Operations has not decided yet."),
 (YSn, "10:13", "We cannot decide that today. It stays open."),
 (AMn, "10:14", "Understood."),
 (NRn, "10:15", "The new staff will need induction training before they start work on site."),
 (NRn, "10:16", "At least Safety leadership for everyone, and the Well control refresher for the technicians."),
 (YSn, "10:17", "Noura, please plan the induction training for the new section."),
 (NRn, "10:18", f"I will put it in the {LD_PLAN} and share the plan by {LD_BY}."),
 (YSn, "10:18", "Good. Let me read the actions back."),
] + [(YSn, t, f"{who}: {a[0].lower() + a[1:]}. Deadline: {dl}.") for t, (who, (a, dl)) in zip(("10:19", "10:19", "10:20", "10:20"), [(w, ACT[w]) for w in ("Khaled", "Abdulaziz", "Noura", "Hessa")])] + [
 (YSn, "10:21", f"One question stays open. {D.STAFF_OPEN[0]}."),
 (KAn, "10:21", "All clear."),
 (NRn, "10:22", "Clear, thank you."),
 (HKn, "10:22", "Clear."),
 (YSn, "10:23", "Thank you, everyone. That is all for today."),
]
assert 25 <= len(LINES) <= 35
doc(F["transcript"], f"Teams meeting transcript (exported): {D.NEW_SECTION} section staffing, Monday 16 November 2026, 10:00",
    [("kv", ("Organizer", YSn)), ("kv", ("Attendees", ", ".join([KAn, AMn, NRn, HKn]))), ("i", "Transcription started.")] +
    [("sp", x) for x in LINES] + [("i", "Transcription stopped.")])

# 16 · the HR trackers workbook: 412 training rows (14 duplicates), Manpower with one section at 0
def _head(ws, row):
    for c in ws[row]:
        if c.value is not None: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=NAVY); c.alignment = Alignment(vertical="center")

def trackers(path):
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Training"
    ws.append(["Request ID", "Date", "Unit", "Employee code", "Course", "Status", "Cost (KWD)"]); _head(ws, 1)
    for r in D.TRAIN_EXPORT:
        ws.append([r["id"], dt.datetime(*r["date"]), r["unit"], r["emp"], r["course"], r["status"], r["cost"]])
    for row in ws.iter_rows(min_row=2):
        row[1].number_format = "dd/mm/yyyy"; row[6].number_format = "#,##0"
    for col, w in zip("ABCDEFG", (14, 12, 14, 15, 36, 11, 12)): ws.column_dimensions[col].width = w
    ws.freeze_panes = "A2"

    mp = wb.create_sheet("Manpower")
    mp.append(["Section", "Approved positions", "Filled", "Vacancies"]); _head(mp, 1)
    for s, a, f in D.SECTIONS:
        a = 0 if s == D.MP_WRONG else a                      # the planted error: approved positions entered as 0
        mp.append([s, a, f, a - f])
    for col, w in zip("ABCD", (24, 20, 10, 12)): mp.column_dimensions[col].width = w
    mp.freeze_panes = "A2"

    cs = wb.create_sheet("Control totals")
    cs.append(["Control totals · Q3 2026"]); cs["A1"].font = Font(bold=True, size=13)
    cs.append(["Checked by HR Systems from the HR system."])
    cs.append([])
    cs.append(["Training requests Q3 2026", D.TRAIN_TRUE]); cs.cell(cs.max_row, 1).font = Font(bold=True)
    cs.append([])
    cs.append(["Unit", "Training requests"]); _head(cs, cs.max_row)
    assert sum(D.TRAIN_BY_UNIT.values()) == D.TRAIN_TRUE
    for u in D.UNITS: cs.append([u, D.TRAIN_BY_UNIT[u]])
    cs.append(["All units", D.TRAIN_TRUE]); cs.cell(cs.max_row, 1).font = Font(bold=True)
    cs.append([])
    cs.append(["Approved structure by section"]); cs.cell(cs.max_row, 1).font = Font(bold=True)
    cs.append(["Section", "Approved positions", "Filled", "Vacancies"]); _head(cs, cs.max_row)
    for s, a, f in D.SECTIONS: cs.append([s, a, f, a - f])
    cs.append(["All sections", D.MP_APPROVED, D.MP_FILLED, D.MP_VACANT])
    for c in cs[cs.max_row]: c.font = Font(bold=True)
    for col, w in zip("ABCD", (30, 20, 10, 12)): cs.column_dimensions[col].width = w

    ns = wb.create_sheet("Notes")
    ns.append(["About this file"]); ns["A1"].font = Font(bold=True)
    for line in ["Training: training requests for Q3 2026 (July to September), exported from the HR system.",
                 "One row = one training request.",
                 "Manpower: approved positions, filled positions and vacancies by section, exported from the HR system.",
                 "Control totals: the checked figures from the HR system. Compare any total from the other sheets with them.",
                 "Employee codes only. No names, salaries or personal data.", D.FICTION]:
        ns.append([line])
    ns.column_dimensions["A"].width = 110
    for sh in wb.worksheets: sh.oddHeader.center.text = HEADER
    wb.properties.creator = "CODED"; wb.properties.lastModifiedBy = "CODED"; wb.properties.title = "HR trackers Q3 2026"
    wb.properties.created = FIXED; wb.properties.modified = FIXED
    wb.save(path); _stable(path)

    chk = openpyxl.load_workbook(path)                       # the planted numbers, read back from the saved file
    assert chk["Training"].max_row - 1 == D.TRAIN_ROWS_EXPORT, "Training rows != D.TRAIN_ROWS_EXPORT"
    assert sum(r[3] for r in chk["Manpower"].iter_rows(min_row=2, values_only=True)) == D.MP_VACANT_EXPORT, "Manpower vacancies != D.MP_VACANT_EXPORT"
trackers(os.path.join(OUT, F["trackers"])); WRITTEN.append(F["trackers"])

# 17 · the two-page brief for line managers
PAF = D.CASES["pa"]["facts"]
LM_MEET = grab(r"meet on (.+?) to ", PAF[4])
doc(F["brief"], "Brief: new attendance rules (for line managers)", [
    ("i", "For all line managers. From Personnel and Administration."),
    ("h", "Why we are changing"),
    ("p", "Late arrivals have increased across Mutla. They delay shift handovers and meetings, and they put pressure on the people who arrive on time."),
    ("p", f"The {A['pilot_unit']} tested flexible start times first. The result of the pilot is in the list below."),
    ("h", "What changes"),
] + [("b", x) for x in D.BRIEF_POINTS] + [
    ("p", f"Arrival after {A['flex_to']} is recorded as lateness."),
    ("h", "Key dates"),
    ("t", [["Date", "What happens"],
           [f"By {A['announce_by']}", "Personnel and Administration sends the staff announcement."],
           [LM_MEET, "Line managers meet to agree how to handle exceptions."],
           [f"By {A['system_by']}", "IT updates the attendance system."],
           [A["start"], "The new rules start."]], [5.5, 10.5]),
    ("h", "What we ask of you"),
    ("b", "Explain the new times to your team before the start date."),
    ("b", "Approve or decline permission requests in the HR system."),
    ("b", "Send any question you cannot answer to Personnel and Administration."),
    ("pb",),
    ("h", "Frequently asked questions"),
    ("qa", ("What are the working hours in Ramadan?", "To be announced. Personnel and Administration will confirm them.")),
    ("qa", ("Do the new rules apply to field staff on rotation?", "Manpower is checking which rotation groups the rules cover. Personnel and Administration will confirm the answer.")),
    ("qa", ("How does an employee request a permission?", f"In the HR system. Each employee has up to {A['permissions']} permissions a month, each up to {A['perm_hours']} hours.")),
    ("qa", ("Who approves a permission?", "The line manager approves or declines each permission in the HR system.")),
    ("h", "Who to contact"),
    ("p", "Personnel and Administration answers questions about the rules, permissions and attendance records."),
    ("kv", ("Contact", f"{D.P['pa']}, Personnel and Administration")),
])

# 18 to 22 · one case per track (Task 2.6)
CMPF, LDF, JEF = D.CASES["cmp"]["facts"], D.CASES["ld"]["facts"], D.CASES["je"]["facts"]
_n_max = int(grab(r"^(\d+) employees", CMPF[1]))
_cost = [int(x.replace(",", "")) for x in re.findall(r"\d[\d,]*", CMPF[2])]   # 140, 50, 7000, 84000
_inc = D.ALLOW["housing_v4"] - D.ALLOW["housing_v3"]
assert _cost == [_n_max, _inc, _n_max * _inc, _n_max * _inc * 12]
_courses = [(c, int(n)) for c, n in re.findall(r"([A-Z][A-Za-z ]+?) \((\d+)\)", LDF[1])]
assert len(_courses) == 3 and all(c in dict(D.COURSES) for c, _n in _courses)
TECH_NOTE = MPF[2]
CASE_OUT = {
 "mp": dict(to=f"Finance, about the manpower request (due {grab(r'by (.+?)\.$', MPF[3])})", meet="your meeting with Recruitment about the hiring order",
            four="for example, an Excel table of the 12 positions", files=[],
            table=[["Position", "Number", "Note"]] + [[l.capitalize(), str(n), TECH_NOTE if "technician" in l else ""] for n, l in POS] + [["Total", str(D.STAFF_POSITIONS), ""]]),
 "cmp": dict(to=f"Finance, with the cost estimate (due {grab(r'by (.+?)\.$', CMPF[3])})", meet="the Compensation Supervisor, before the meeting with Finance",
             four="for example, an Excel cost table", files=[F["v4"]],
             table=[["Item", "Figure"], ["Employees paid at the current maximum", str(_n_max)], ["Increase for each employee", f"{D.kwd(_inc)} a month"],
                    ["Extra cost a month", D.kwd(_n_max * _inc)], ["Extra cost a year", D.kwd(_n_max * _inc * 12)]]),
 "pa": dict(to=f"the line managers, before their meeting on {LM_MEET}", meet=f"the line managers' meeting on {LM_MEET}",
            four="for example, a PowerPoint briefing for the line managers", files=[F["attendance"], F["brief"]], table=None),
 "ld": dict(to=f"the line managers, about pending requests and the nomination deadline ({grab(r'close on (.+?)\.$', LDF[3])})",
            meet="your meeting with the Head of Learning and Development about the Q4 budget",
            four="for example, an Excel summary of requests by course", files=[F["training"]],
            table=[["Course", "Requests"]] + [[c, str(n)] for c, n in _courses]),
 "je": dict(to="the employee who asked about the grade (only the committee decides)", meet=f"the Job Evaluation committee meeting on {grab(r'meets on (.+?)\.$', JEF[3])}",
            four="for example, a PowerPoint briefing for the committee", files=[F["factors"], F["tpl"]], table=None),
}
for k, n in D.TRACKS:
    cs_, co = D.CASES[k], CASE_OUT[k]
    blocks = [("i", f"Case for Tasks 2.2 and 2.5 · {n} track"), ("h", "The facts")] + [("p", f"{i}. {x}") for i, x in enumerate(cs_["facts"], 1)]
    if co["table"]: blocks += [("t", co["table"])]
    blocks += [("h", "Your two outputs"),
               ("p", f"1. Task 2.2: an agenda, a background brief and three discussion points for {co['meet']}."),
               ("p", f"2. Task 2.5: a message to {co['to']}."),
               ("h", "Before anything goes out"),
               ("p", "Check every date and number against this file. No employee names. Start each output with: " + D.DRAFT_LINE),
               ("kv", ("Approved files to attach", ", ".join(["this case file"] + co["files"])))]
    doc(cs_["file"], cs_["title"], blocks)

# ================================================================== DAY 3
# 23 · attendance rules (agent knowledge)
policy(F["attendance"], f"{D.COMPANY} · Attendance Rules {D.YEAR} (approved)", [
    ("1", "Scope", "These rules apply to Mutla employees on day work. Manpower is checking whether they apply to field staff on rotation."),
    ("2", "Start date", f"These rules apply from {A['start']}."),
    ("3", "Flexible start", f"Employees may start work at any time between {A['flex_from']} and {A['flex_to']}."),
    ("4", "Core hours", f"All employees must be at work between {A['core_from']} and {A['core_to']}."),
    ("5", "Daily working hours", f"Employees work {A['hours']} hours a day. Working hours in Ramadan will be announced separately."),
    ("6", "Permissions", f"Employees may take up to {A['permissions']} permissions a month. Each permission is up to {A['perm_hours']} hours. Employees request a permission in the HR system, and the line manager approves or declines it."),
    ("7", "Lateness", f"Arrival after {A['flex_to']}, the end of the flexible start, is recorded as lateness. The attendance system records it automatically."),
    ("8", "Questions", "Questions about these rules go to Personnel and Administration."),
], f"Approved by the HR Section Head on {APPROVED_ON}. Owner: Personnel and Administration.")

# 24 · training policy (agent knowledge)
policy(F["training"], f"{D.COMPANY} · Training Policy {D.YEAR}", D.TRAINING_POLICY, "Owner: Learning and Development.")

# 25 · the catch-up Prompt Bank: eight tested requests from content_demos
CATCH = {
 "Draft": [("Draft a job description from the role sheet", joined(JD_CMP), f"{F['roles']}, {F['tpl']}", "Trace every duty to the role sheet. The grade line is blank."),
           ("Turn a brief into a five-slide outline", joined(DECK), F["brief"], "Every time, date and number matches the brief.")],
 "Compare": [("Compare two versions of a policy", COMPARE[1], f"{F['v3']}, {F['v4']}", "Open both files. Check each change at its section number."),
             ("Count tracker rows and compare with the control total", joined(TRACKER), F["trackers"], "The total matches the Control totals sheet, or you can name the rows behind the difference.")],
 "Summarize": [("Decisions and owners from a long email thread", joined(THREAD), F["thread"], "The start date matches the approval message. Every decision has its message number."),
               ("Recap a meeting transcript", joined(RECAP), F["transcript"], "Every owner and deadline matches the transcript. No action that nobody agreed.")],
 "Review": [("Trace each line of a draft to its source", joined(TRACE), f"Your draft (or {F['catchjd']}), {F['roles']}, {F['tpl']}", "Delete or check every NOT IN SOURCE line."),
            ("Flag problems in a request, do not fix them", LETTER_FLAG[1], F["letters"], "You decide each point. Check the dates against the HR record yourself.")],
}
assert sum(len(v) for v in CATCH.values()) == 8 and list(CATCH) == BANK_SECTIONS
doc(F["catchbank"], "Catch-up Prompt Bank: eight tested requests",
    [("i", "Use this bank if you missed a day. Every request has been tested on the Mutla files.")] + bank_intro() +
    [x for h in BANK_SECTIONS for x in (("h", h), ("t", [BANK_HEAD] + [list(e) for e in CATCH[h]], BANK_W))])

# 26 · five process stories (Day 2, Tasks 2.10 and 2.11): as-is, with the four problems hidden in each
STORY_ORDER = ["ld", "pa", "cmp", "mp", "je"]
assert sorted(STORY_ORDER) == sorted(D.STORIES) and STORY_ORDER[0] == "ld"
doc(F["stories"], "HR process stories: how the work is done today", [
    ("i", "Five stories, one for each HR unit track. Each one describes a process as it runs today, from the request to the result. Map it first. Do not improve it yet."),
    ("t", [["Look for", "What it means"]] + [[a, b] for a, b in D.PROBLEMS], [4.5, 11.5]),
] + [x for i, k in enumerate(STORY_ORDER, 1) for x in
     [("h", f"Story {i}: {D.STORIES[k]['title']}"), ("lbl", f"Owner: {D.STORIES[k]['owner']}")] + [("p", line) for line in D.STORIES[k]["story"]]])

# 27 · the process map template (Day 2): the step table, empty
MAP_W = [1.2, 2.2, 3.6, 2.0, 2.0, 1.6, 2.2, 1.6]
doc(F["maptpl"], "Process map template", [
    ("p", "Map one HR process as it runs today, from the request to the result. One row for each step. Do not improve it yet: that is Day 3."),
    ("kv", ("Process", "")), ("kv", ("Track", "")), ("kv", ("Mapped by", "")),
    ("t", [D.MAP_COLS] + [[""] * len(D.MAP_COLS) for _ in range(10)], MAP_W, 0.9),
    ("h", "Mark these in the Problem column"),
    ("t", [["Problem", "What it means"]] + [[a, b] for a, b in D.PROBLEMS], [4.5, 11.5]),
    ("h", "Before you finish"),
    ("b", "Every step has one owner (a role, not \"HR\" or \"the team\")."),
    ("b", "Every wait has a length."),
    ("b", "Every approval or decision is marked in the last column."),
    ("b", "Roles only: no real names and no real data."),
])

# 28 · the workflow card template (Day 3 final project), with the filled-in example
assert len(D.CARD_FIELDS) == len(D.CARD_EXAMPLE) == 9
doc(F["card"], "Final project: improved workflow card", [
    ("p", "Turn your process map into a better process. Mark each step Person, Copilot, Agent or Flow. Keep every approval and decision with a person."),
    ("h", "Your card"),
    ("t", [["Card line", "Your process"]] + [[f, ""] for f in D.CARD_FIELDS], [5.6, 10.4], 1.2),
    ("h", "Your tests"),
    ("t", [["Test", "What you tried", "Result", "Fix"], ["Normal", "", "", ""], ["Incomplete", "", "", ""], ["Sensitive", "", "", ""]], [2.6, 5.4, 4.0, 4.0], 1.2),
    ("pb",),
    ("h", "A filled-in example: a training request"),
    ("t", [["Card line", "Example"]] + [[a, b] for a, b in zip(D.CARD_FIELDS, D.CARD_EXAMPLE)], [5.6, 10.4]),
    ("h", "Submit"),
    ("p", "Submit your card and your tested piece on the CODED platform, with the link your trainer shares. Start the card with: " + D.DRAFT_LINE),
])

# 29 · the training request log (Day 3, Power Automate demo): one Excel table the flow adds rows to
def palog(path):
    from openpyxl.worksheet.table import Table, TableStyleInfo
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Log"
    ws.append(D.PA_LOG_HEAD); _head(ws, 1)
    for r in D.PA_LOG: ws.append(list(r))
    t = Table(displayName="TrainingRequests", ref=f"A1:{chr(64 + len(D.PA_LOG_HEAD))}{len(D.PA_LOG) + 1}")
    t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True); ws.add_table(t)
    for col, w in zip("ABCDEFGH", (13, 18, 15, 26, 17, 11, 14, 18)): ws.column_dimensions[col].width = w
    ws.freeze_panes = "A2"
    ns = wb.create_sheet("Read me")
    for line in ["The Power Automate demo adds one row to the table TrainingRequests for each form response.",
                 "Employee codes only. No names, salaries or personal data.", D.FICTION]:
        ns.append([line])
    ns.column_dimensions["A"].width = 100
    for sh in wb.worksheets: sh.oddHeader.center.text = HEADER
    wb.properties.creator = "CODED"; wb.properties.lastModifiedBy = "CODED"; wb.properties.title = "Training request log"
    wb.properties.created = FIXED; wb.properties.modified = FIXED
    wb.save(path); _stable(path)
    chk = openpyxl.load_workbook(path)
    assert "TrainingRequests" in chk["Log"].tables and chk["Log"].max_row == len(D.PA_LOG) + 1
palog(os.path.join(OUT, F["palog"])); WRITTEN.append(F["palog"])

# ------------------------------------------------------------------ every file in ALL_FILES, nothing more
assert sorted(WRITTEN) == sorted(ALL_FILES), f"gen_files: wrote {sorted(set(WRITTEN) ^ set(ALL_FILES))} out of step with ALL_FILES"
for f in ALL_FILES: print(f"{os.path.getsize(os.path.join(OUT, f)):>8}  {f}")
print(f"{len(ALL_FILES)} files in {os.path.abspath(OUT)}")
