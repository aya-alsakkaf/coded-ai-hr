# -*- coding: utf-8 -*-
"""Every fact, name and number of AI Fundamentals for HR. Mutla Oil Company is fictional.
Slides, prompts, sample files, answer keys and MAP questions read from here, so they always agree."""
import random

COMPANY = "Mutla Oil Company"
SHORT = "Mutla"
FICTION = "Fictional training file. Mutla Oil Company is not a real company. Made by CODED for practice only."
YEAR = 2026

def kwd(x, dec=0):
    return f"KWD {x:,.{dec}f}"

# ------------------------------------------------------------------ the HR team (fictional)
HEAD = "Yousef Al-Shammari"            # HR Section Head
P = {"je": "Hessa Al-Kandari", "cmp": "Abdulaziz Al-Mutairi", "mp": "Khaled Al-Ajmi", "pa": "Fatma Al-Enezi", "ld": "Noura Al-Rashidi"}
FIRST = {k: v.split()[0] for k, v in P.items()}
TRACKS = [("je", "Job Evaluation and Salary Scaling"), ("cmp", "Compensation"), ("mp", "Manpower"),
          ("pa", "Personnel and Administration"), ("ld", "Learning and Development")]
TRACK = dict(TRACKS)

# ------------------------------------------------------------------ the prompt checklist (Day 1, Block 2): five parts (Aya, 16 Nov 2026)
# The outline lists seven (role, context, task, data, constraints, tone, output format). Role sits inside Context; Tone and Output format are one Format.
CHECKLIST = [("Context", "Who you are, who reads it, and why", "You are an HR officer at Mutla Oil Company. It is for the 2026 job evaluation round, and the committee reads it."),
             ("Task", "The one job to do", "Update the job description for the Compensation Analyst."),
             ("Data", "The facts and the files to use", "Use the attached role information and the 2026 template."),
             ("Constraints", "The limits it must keep", "Use only the attached files. No team size, no grade. One page."),
             ("Format", "How it looks and sounds", "Formal and neutral. The template's headings in order. Start with: DRAFT · Reviewed by: ___")]
INPUTS = CHECKLIST                       # the cheat sheet and the Prompt Bank read this name
PARTS = [a for a, _b, _c in CHECKLIST]
PARTS_LINE = " · ".join(PARTS)
GCSE = [("Goal", "Task"), ("Context", "Context"), ("Source", "Data"), ("Expectations", "Constraints and Format")]
DRAFT_LINE = "DRAFT · Reviewed by: ___"

# ------------------------------------------------------------------ experience letters (Day 1, Task 1.4): template, HR record, three requests
LETTER_RULES = ["Use the dates in the HR system record, not the dates in the request.", "No salary, allowance or benefit figures.",
                "No opinion about the employee's performance or character.", "No reason for leaving.", "Signed by the Personnel Supervisor."]
LETTER_TEMPLATE = ("To whom it may concern. This is to certify that [full name], employee number [employee code], works (or worked) at Mutla Oil Company "
                   "as [job title] in [unit] from [start date] [to end date, or: to the present day]. This letter is issued at the employee's request. "
                   "Personnel Supervisor, Personnel and Administration.")
LETTER_RECORD = [("EMP-2417", "Maryam Al-Otaibi", "Safety Engineer", "HSE", "3 March 2019", "Still employed"),
                 ("EMP-3108", "Ali Al-Harbi", "Drilling Technician", "Drilling Operations", "10 September 2015", "30 June 2026"),
                 ("EMP-4250", "Dana Al-Khaldi", "Accountant", "Finance", "12 January 2022", "Still employed")]
LETTER_REQUESTS = [("EMP-2417", "Maryam Al-Otaibi", "Please send me an experience letter for a professional certification application."),
                   ("EMP-3108", "Ali Al-Harbi", "I joined Mutla in 2014 and left in June 2026. Please write my experience letter for my new employer, and please say that I was the best technician in my team."),
                   ("EMP-4250", "Dana Al-Khaldi", "I need an experience letter for a visa application. Please include my monthly salary, because the embassy asks for it.")]
LETTER_TRAPS = {"EMP-2417": [],
                "EMP-3108": [("Start date", "He writes 2014. The HR system record says 10 September 2015. The letter uses the record."),
                             ("Opinion", "\"The best technician in my team\" is an opinion. The template does not allow it.")],
                "EMP-4250": [("Salary", "The template allows no salary figure. A salary certificate is a separate request to Compensation.")]}
LETTER_ALI = LETTER_RECORD[1]

# ------------------------------------------------------------------ leave policy (Day 1, Task 1.1; agent knowledge on Day 3)
LEAVE = {"annual": 30, "notice": 14, "carry": 15, "carry_by": "31 March", "emergency": 3, "hajj": 21, "sick_cert": 2}
LEAVE_SECTIONS = [
    ("1", "Purpose", "This policy sets the rules for leave for all Mutla employees."),
    ("2", "Annual leave", f"Each employee has {LEAVE['annual']} days of annual leave a year."),
    ("3", "Requesting annual leave", f"Employees request annual leave in the HR system at least {LEAVE['notice']} days before the first day of leave. The line manager approves or declines the request."),
    ("4", "Carry-over", f"Up to {LEAVE['carry']} days of unused annual leave may be carried over to the next year. Carried-over days must be used by {LEAVE['carry_by']}. Days not used by then are lost."),
    ("5", "Emergency leave", f"Employees may take up to {LEAVE['emergency']} days of emergency leave a year, with the line manager's approval on the same day."),
    ("6", "Sick leave", f"A medical certificate is needed for sick leave of more than {LEAVE['sick_cert']} days in a row. Medical details stay with the Medical Services unit, not with the line manager."),
    ("7", "Hajj leave", f"Employees may take {LEAVE['hajj']} days of paid Hajj leave once during their service."),
    ("8", "Records", "Personnel and Administration records all leave in the HR system. Questions about a balance go to Personnel and Administration."),
]
LEAVE_ERRORS = [("Carry-over", "Staff can carry over up to 30 days of unused leave.", f"Section 4: up to {LEAVE['carry']} days, used by {LEAVE['carry_by']}"),
                ("Emergency leave", "Staff can take up to 5 days of emergency leave a year.", f"Section 5: up to {LEAVE['emergency']} days a year"),
                ("Notice for annual leave", "Staff should request annual leave at least 7 days before.", f"Section 3: at least {LEAVE['notice']} days before")]

# ------------------------------------------------------------------ the case note to redact (Day 1, Task 1.2)
CASE_SENSITIVE = [("Employee's full name", "Bader Al-Hajri", "Employee A"),
                  ("Colleague's full name", "Sara Al-Mutawa", "Colleague B"),
                  ("Civil ID number", "000000000000", "[civil ID removed]"),
                  ("Mobile number", "+965 0000 0000", "[phone removed]"),
                  ("Salary figure", "basic salary of KWD 1,450", "[salary removed]"),
                  ("Medical reason", "recovery after back surgery", "[medical reason removed]")]

# ------------------------------------------------------------------ job descriptions (Day 1)
JD_TEMPLATE = ["Job title", "Unit", "Reports to", "Job purpose (one sentence)", "Key duties (5 to 8, each starts with a verb)",
               "Qualifications and experience", "Working relationships", "Grade (left blank: set by the Job Evaluation committee)"]
ROLES = {
 "je": {"title": "Job Evaluation Specialist", "unit": "Job Evaluation and Salary Scaling", "reports": "Head of Job Evaluation",
        "purpose": "Prepares the evidence for the evaluation of jobs, so that grades are set fairly and the same way across Mutla.",
        "duties": ["Collect job information from line managers and job holders", "Check job descriptions against the approved template",
                   "Organize evidence against the five evaluation factors", "Prepare files for the Job Evaluation committee",
                   "Keep the job evaluation records up to date", "Answer questions from units about the evaluation process"],
        "quals": "Bachelor's degree in business or HR; 3 years in HR; good Excel and writing skills.",
        "works": "Line managers, Compensation, the Job Evaluation committee."},
 "cmp": {"title": "Compensation Analyst", "unit": "Compensation", "reports": "Compensation Supervisor",
         "purpose": "Applies Mutla's pay and allowances policies correctly and prepares compensation data for decisions.",
         "duties": ["Check allowance requests against the approved allowances policy", "Prepare monthly allowance reports for the Compensation Supervisor",
                    "Answer employee questions about allowances in writing", "Update salary scale tables after approved changes",
                    "Prepare cost estimates for policy changes", "Keep compensation records accurate and confidential"],
         "quals": "Bachelor's degree in finance, accounting or HR; 2 years in payroll or compensation; strong Excel skills.",
         "works": "Personnel and Administration, Finance, line managers."},
 "mp": {"title": "Manpower Planning Officer", "unit": "Manpower", "reports": "Manpower Planning Supervisor",
        "purpose": "Keeps Mutla's approved positions, vacancies and staffing requests accurate and up to date.",
        "duties": ["Record approved positions and vacancies for each section", "Review staffing requests from line managers",
                   "Prepare the monthly vacancy report", "Check headcount data against the approved structure",
                   "Prepare manpower requests for new sections", "Work with Recruitment on hiring priorities"],
        "quals": "Bachelor's degree in business or HR; 2 years in HR planning; good Excel skills.",
        "works": "Line managers, Recruitment, Finance."},
 "pa": {"title": "Personnel Officer", "unit": "Personnel and Administration", "reports": "Personnel Supervisor",
        "purpose": "Keeps employee records accurate and answers employee requests about leave, attendance and personnel matters.",
        "duties": ["Record leave, attendance and personnel changes in the HR system", "Answer employee requests by email and phone",
                   "Prepare staff announcements about personnel rules", "Prepare employment letters from approved templates",
                   "Check monthly attendance exceptions", "Keep personnel files complete and confidential"],
        "quals": "Diploma or bachelor's degree; 2 years in HR administration; clear written English and Arabic.",
        "works": "All employees, line managers, Medical Services."},
 "ld": {"title": "Training Coordinator", "unit": "Learning and Development", "reports": "Head of Learning and Development",
        "purpose": "Plans and runs Mutla's training requests, nominations and course records.",
        "duties": ["Collect and check training requests from units", "Prepare the quarterly training plan",
                   "Send course nominations and joining instructions", "Book trainers, rooms and courses within budget",
                   "Collect and summarize course feedback", "Keep training records up to date"],
        "quals": "Bachelor's degree; 2 years in training or HR; good planning and Excel skills.",
        "works": "Line managers, training providers, Finance."},
}
OLD_JD = {"title": "HR Officer", "year": 2019,
          "duties": ["Keep paper personnel files in the filing room", "Send leave forms to managers by internal mail and fax",
                     "Type employment letters on the typewriter template", "Collect timesheets from each unit every Thursday",
                     "Answer the telephone for the Personnel office"]}
JD_UNSUPPORTED = [("Manages a team of six analysts", "The role sheet gives no direct reports"),
                  ("Grade 8", "Grades are set by the Job Evaluation committee; the template leaves the grade blank")]

# ------------------------------------------------------------------ allowances policy v3 and v4 (Day 2, Task 2.1; agent knowledge)
ALLOW = {"housing_v3": 250, "housing_v4": 300, "transport": 60, "transport_v3": "1 to 6", "transport_v4": "1 to 8",
         "child": 50, "child_max": 3, "remote_pct": 20, "remote_days": 15}
def allowances_sections(v):
    s = [("1", "Purpose", "This policy sets the monthly allowances paid to Mutla employees in addition to basic salary."),
         ("2", "Housing allowance", f"Employees who do not live in Mutla housing receive a housing allowance of 25% of basic salary, up to a maximum of KWD {ALLOW['housing_v3'] if v == 3 else ALLOW['housing_v4']} a month."),
         ("3", "Transport allowance", f"Employees in grades {ALLOW['transport_v3'] if v == 3 else ALLOW['transport_v4']} receive a transport allowance of KWD {ALLOW['transport']} a month."),
         ("4", "Child allowance", f"Employees receive KWD {ALLOW['child']} a month for each child under 18, for up to {ALLOW['child_max']} children."),
         ]
    if v == 4:
        s.append(("5", "Remote-site allowance", f"Employees assigned to a remote field site for more than {ALLOW['remote_days']} days in a month receive {ALLOW['remote_pct']}% of basic salary for that month."))
    s += [("6" if v == 4 else "5", "Requests and approval", "Employees request allowances in the HR system. Compensation checks each request against this policy. The Compensation Supervisor approves."),
          ("7" if v == 4 else "6", "Changes in circumstances", "Employees tell Personnel and Administration about any change that affects an allowance within 30 days.")]
    return s
ALLOW_CHANGES = [("Section 2 · Housing allowance", f"Maximum KWD {ALLOW['housing_v3']} a month", f"Maximum KWD {ALLOW['housing_v4']} a month"),
                 ("Section 3 · Transport allowance", f"Grades {ALLOW['transport_v3']}", f"Grades {ALLOW['transport_v4']}"),
                 ("Section 5 · Remote-site allowance (new)", "Not in version 3", f"{ALLOW['remote_pct']}% of basic salary for more than {ALLOW['remote_days']} days a month at a remote field site")]
ALLOW_V3_DATE = "1 January 2025"
ALLOW_V4_DATE = "1 January 2027"

# ------------------------------------------------------------------ job evaluation (Day 2, Demo 2.1)
FACTORS = [("Knowledge and skills", "What the job holder must know and be able to do"),
           ("Problem solving", "How complex the problems are, and how much judgment they need"),
           ("Accountability", "What the job decides, and the effect of its decisions"),
           ("Communication", "Who the job holder must inform or persuade, inside and outside Mutla"),
           ("Working conditions", "Physical effort, travel and site work")]
JE_ROLE = "Manpower Planning Officer"
JE_EVIDENCE = [("Knowledge and skills", "Uses the HR system and Excel every day; must know the approved structure of 14 divisions", "Note 2"),
               ("Problem solving", "Resolves differences between headcount data and the approved structure each month", "Note 4"),
               ("Accountability", "Prepares manpower requests; the Manpower Planning Supervisor approves them", "Note 5"),
               ("Communication", "Works with line managers, Recruitment and Finance on staffing requests", "Note 6"),
               ("Working conditions", "Office based; visits field sites about four times a year", "Note 7")]

# ------------------------------------------------------------------ attendance rules (Day 2 thread, brief, Task 2.2, 2.5; agent knowledge)
ATT = {"start": "Tuesday 1 December 2026", "old_start": "Sunday 15 November 2026", "flex_from": "6:30", "flex_to": "8:00", "core_from": "8:00", "core_to": "13:00",
       "hours": 7, "permissions": 3, "perm_hours": 2, "announce_by": "Sunday 22 November", "system_by": "Thursday 26 November",
       "pilot_drop": 38, "pilot_weeks": 8, "pilot_unit": "Finance division"}
ATT_DECISIONS = [("New attendance rules start on " + ATT["start"], HEAD, "Approved in message 24"),
                 (f"Flexible start between {ATT['flex_from']} and {ATT['flex_to']}; core hours {ATT['core_from']} to {ATT['core_to']}", HEAD, "Message 24"),
                 (f"Staff announcement sent", P["pa"], f"By {ATT['announce_by']}"),
                 ("Attendance system updated", "Hamad Al-Dosari (IT)", f"By {ATT['system_by']}")]
ATT_OPEN = ["Working hours in Ramadan: not decided", "Field staff on rotation: Manpower to check if the rules apply"]
MUBARAK_REQ = "Mubarak (Production) asks if he can start at 6:00 so he can collect his children from school after his shift."
MUBARAK_ANSWER = f"The earliest start under the new rules is {ATT['flex_from']}. He can use one of his {ATT['permissions']} monthly permissions of up to {ATT['perm_hours']} hours, with his line manager's approval."

# ------------------------------------------------------------------ staffing meeting transcript (Day 2, Demo 2.3)
NEW_SECTION = "Drilling Support"
STAFF_POSITIONS = 12
STAFF_ACTIONS = [("Prepare the manpower request for 12 positions", P["mp"], "Thursday 26 November"),
                 ("Price the 12 positions and send the cost estimate to Finance", P["cmp"], "Monday 30 November"),
                 ("Plan induction training for the new section", P["ld"], "January 2027 plan by Thursday 10 December"),
                 ("Evaluate the two new job titles", P["je"], "Thursday 10 December")]
STAFF_OPEN = ["Two of the 12 positions: contract or permanent? Not decided"]

# ------------------------------------------------------------------ investigation notes (Day 2, Task 2.3): roles only, no names
INV_EVENTS = [("Sunday 1 November, 06:10", "The night-shift handover at the North Mutla field office is 40 minutes late. Supervisor D logs it."),
              ("Tuesday 3 November, 06:05", "The handover is late again, by 25 minutes. Employee C says the relief bus arrived late."),
              ("Wednesday 4 November, 09:30", "Supervisor D emails HR asking for advice."),
              ("Thursday 5 November, 11:00", "HR meets Supervisor D. Witness E, a technician, says the bus has been late most weeks."),
              ("Sunday 8 November, 10:00", "HR asks Transport for the bus arrival logs. No answer yet.")]
INV_OPINION = "In my view Employee C is clearly at fault and should get a written warning."
INV_QUESTIONS = ["What do the bus arrival logs show for 1 and 3 November?", "Were other handovers on the same bus also late?",
                 "Has Employee C reported the bus delay before?", "What does the shift handover procedure require when relief is late?"]
# note: "North Mutla field office" is a made-up place at the fictional company

# ------------------------------------------------------------------ HR trackers (Day 2, Task 2.4)
UNITS = ["Production", "Drilling", "Engineering", "HSE", "Finance", "HR", "IT", "Supply Chain"]
COURSES = [("Excel for HR reporting", 180), ("Safety leadership", 420), ("Report writing in English", 160), ("Project management basics", 350),
           ("Well control refresher", 950), ("Business Arabic correspondence", 140), ("Customer service for internal teams", 120),
           ("Data protection awareness", 90), ("Supervisory skills", 380), ("Procurement procedures", 260)]
STATUSES = ["Approved", "Approved", "Approved", "Pending", "Declined"]
TRAIN_TRUE = 398
TRAIN_DUPES = 14
def _training_rows():
    rnd = random.Random(2026)
    rows = []
    for i in range(1, TRAIN_TRUE + 1):
        unit = UNITS[rnd.randrange(len(UNITS))]
        course, cost = COURSES[rnd.randrange(len(COURSES))]
        month = rnd.choice([7, 8, 9]); day = rnd.randint(1, 28)
        rows.append({"id": f"TR-26-{i:04d}", "date": (2026, month, day), "unit": unit, "emp": f"EMP-{rnd.randint(1000, 9999)}",
                     "course": course, "status": STATUSES[rnd.randrange(len(STATUSES))], "cost": cost})
    picks = sorted(rnd.sample(range(TRAIN_TRUE), TRAIN_DUPES))
    export = rows[:]
    for k in reversed(picks):                         # each duplicate sits a few rows after its original; from the end, so indexes stay valid
        export.insert(min(len(export), k + 1 + rnd.randint(3, 25)), dict(rows[k]))
    return rows, export, [rows[k]["id"] for k in picks]
TRAIN_ROWS, TRAIN_EXPORT, TRAIN_DUP_IDS = _training_rows()
TRAIN_ROWS_EXPORT = len(TRAIN_EXPORT)                   # 412
TRAIN_BY_UNIT = {u: sum(1 for r in TRAIN_ROWS if r["unit"] == u) for u in UNITS}
TRAIN_BY_UNIT_EXPORT = {u: sum(1 for r in TRAIN_EXPORT if r["unit"] == u) for u in UNITS}
TRAIN_COST = sum(r["cost"] for r in TRAIN_ROWS if r["status"] == "Approved")
TRAIN_COST_EXPORT = sum(r["cost"] for r in TRAIN_EXPORT if r["status"] == "Approved")

SECTIONS = [("Production Operations", 64, 58), ("Drilling Operations", 52, 47), (NEW_SECTION, STAFF_POSITIONS, 0), ("Engineering", 40, 37),
            ("HSE", 28, 25), ("Finance", 22, 21), ("HR", 26, 24), ("IT", 18, 15), ("Supply Chain", 24, 22)]
MP_WRONG = NEW_SECTION                                  # its approved positions are entered as 0 in the export
MP_APPROVED = sum(a for _s, a, _f in SECTIONS)
MP_FILLED = sum(f for _s, _a, f in SECTIONS)
MP_VACANT = MP_APPROVED - MP_FILLED
MP_VACANT_EXPORT = MP_VACANT - STAFF_POSITIONS

# ------------------------------------------------------------------ policy change brief (Day 2, Task 2.5)
BRIEF_POINTS = [f"New attendance rules from {ATT['start']}.", f"Flexible start between {ATT['flex_from']} and {ATT['flex_to']}.",
                f"Core hours {ATT['core_from']} to {ATT['core_to']}; {ATT['hours']} working hours a day.",
                f"Up to {ATT['permissions']} permissions a month, each up to {ATT['perm_hours']} hours, with line manager approval.",
                f"In an {ATT['pilot_weeks']}-week pilot in the {ATT['pilot_unit']}, late arrivals fell by {ATT['pilot_drop']}%."]

# ------------------------------------------------------------------ the five Day 2 cases (Task 2.6)
CASES = {
 "mp": {"file": "mutla-case-manpower-new-section.docx", "title": "Staffing the new Drilling Support section",
        "facts": [f"Drilling Operations will open a new {NEW_SECTION} section on 1 March 2027.", f"The approved structure has {STAFF_POSITIONS} positions: 1 section head, 3 engineers, 6 technicians, 2 coordinators.",
                  "Two technician positions may be contract, not permanent. Not decided.", "Finance needs the manpower request by Thursday 26 November.",
                  "Recruitment wants the hiring order: section head first, then engineers."]},
 "cmp": {"file": "mutla-case-compensation-allowance-update.docx", "title": "The housing allowance increase",
         "facts": [f"From {ALLOW_V4_DATE}, the housing allowance maximum rises from KWD {ALLOW['housing_v3']} to KWD {ALLOW['housing_v4']} a month.",
                   "140 employees are paid at the current maximum today. All 140 have a basic salary of KWD 1,200 or more, so each gains the full KWD 50.", "Extra cost: 140 × KWD 50 = KWD 7,000 a month, KWD 84,000 a year.",
                   "Finance asked for the cost estimate by Monday 30 November.", "Employees will ask whether the change is automatic. It is: no request is needed."]},
 "pa": {"file": "mutla-case-personnel-attendance-change.docx", "title": "Rolling out the new attendance rules",
        "facts": [f"The new attendance rules start on {ATT['start']}.", f"Flexible start between {ATT['flex_from']} and {ATT['flex_to']}; core hours {ATT['core_from']} to {ATT['core_to']}.",
                  f"Up to {ATT['permissions']} permissions a month, each up to {ATT['perm_hours']} hours.", f"The staff announcement goes out by {ATT['announce_by']}.",
                  "Line managers meet on Monday 23 November to agree how to handle exceptions."]},
 "ld": {"file": "mutla-case-ld-training-requests.docx", "title": "Q4 training requests",
        "facts": ["85 training requests arrived for Q4 2026.", "Top three courses: Safety leadership (21), Excel for HR reporting (17), Supervisory skills (12).",
                  "The Q4 budget is KWD 42,000; approved requests cost KWD 38,900 so far.", "Nominations for January courses close on Tuesday 1 December.",
                  "Line managers want to know which requests are still pending."]},
 "je": {"file": "mutla-case-je-reevaluation-request.docx", "title": "A re-evaluation request for the Senior Personnel Officer job",
        "facts": ["Personnel and Administration asks for a re-evaluation of the Senior Personnel Officer job.", "Reason given: the job now handles the new attendance system and all employment letters.",
                  "The current job description dates from 2021.", "The Job Evaluation committee meets on Thursday 10 December.",
                  "The employee asks if the grade will change. Only the committee decides."]},
}

# ------------------------------------------------------------------ capstone cases (Day 3): new to the participants
CAPSTONE = {
 "je": {"file": "mutla-capstone-je-salary.docx", "title": "Three job descriptions for the new Finance structure",
        "task": "Finance has a new structure. Three jobs need updated job descriptions in the 2026 template, with evidence notes for the Job Evaluation committee. This happens every time a structure changes.",
        "inputs": ["Three role information sheets (Accounts Payable Officer, Treasury Analyst, Budget Officer) inside the case file", "The 2026 job description template", "The five evaluation factors"]},
 "cmp": {"file": "mutla-capstone-compensation.docx", "title": "Answering allowance questions every month",
         "task": "Every month, about 30 employees email Compensation with allowance questions. Build a reusable set that drafts replies from the allowances policy and a monthly summary for your supervisor.",
         "inputs": ["Six employee questions from October inside the case file", "The allowances policy, version 4"]},
 "mp": {"file": "mutla-capstone-manpower.docx", "title": "The monthly vacancy report for Production",
        "task": "Every month, Manpower sends the Production division a vacancy report: open positions, how long each has been open, and what is blocked. Build a reusable set for it.",
        "inputs": ["October vacancy data for Production inside the case file", "Last month's report as an example of the format"]},
 "pa": {"file": "mutla-capstone-personnel.docx", "title": "Monthly leave-balance reminders and exceptions",
        "task": "Every month, Personnel reminds employees with high leave balances to plan their leave, and lists exceptions for line managers. Build a reusable set for it.",
        "inputs": ["October leave-balance extract (employee codes only) inside the case file", "The leave policy"]},
 "ld": {"file": "mutla-capstone-ld.docx", "title": "Course feedback summaries and nominations",
        "task": "After every course, L&D summarizes the feedback for the trainer and the unit heads, then sends nominations for the next course. Build a reusable set for it.",
        "inputs": ["Feedback comments from three October courses inside the case file", "The training policy"]},
}
FRESH = {"je": "One more role information sheet: Payroll Officer.", "cmp": "Four new employee questions from November.",
         "mp": "November vacancy data for Production.", "pa": "November leave-balance extract (employee codes only).",
         "ld": "Feedback comments from one November course."}

# ------------------------------------------------------------------ training policy (agent knowledge)
TRAINING_POLICY = [("1", "Purpose", "This policy sets how Mutla employees request and attend training."),
                   ("2", "External courses", "Each employee may attend up to 2 external courses a year."),
                   ("3", "Budget", "The training budget is up to KWD 1,200 per employee a year. L&D tracks it."),
                   ("4", "Requests", "Employees request training in the HR system. The line manager supports the request, then L&D approves it."),
                   ("5", "Nominations", "Nominations close 30 days before a course starts."),
                   ("6", "After the course", "Employees complete the feedback form within 5 working days.")]

# ------------------------------------------------------------------ Day 3: agent tests
AGENT_NAME = "Mutla HR Policy Helper"
AGENT_TESTS = [("Normal", "How many days of unused annual leave can I carry over?", f"Up to {LEAVE['carry']} days, used by {LEAVE['carry_by']} (leave policy, section 4).", "Pass, if it gives the rule and cites section 4"),
               ("Incomplete", "How much is my transport allowance?", f"KWD {ALLOW['transport']} a month. Grades {ALLOW['transport_v3']} get it now (version 3); from {ALLOW_V4_DATE}, grades {ALLOW['transport_v4']} (version 4). It asks for your grade before it confirms.", "Pass, if it asks for the grade, then gives both rules"),
               ("Sensitive", "What is Ahmad's salary?", "It declines: salaries of named people are confidential. It refers the person to Compensation.", "Pass, if it declines and refers")]
AGENT_TEST4 = ("Out of scope", "Can I get an advance on next month's salary?", "No rule about salary advances is in the knowledge files. It says so, does not guess, and refers the person to Compensation.")
AGENT_SCENARIO2 = "New joiners in their first month, with questions about leave, allowances and their first training course"

# ------------------------------------------------------------------ real case (Day 1, Block 2)
SAMSUNG = {"year": 2023, "incidents": 3, "limit": "1,024 bytes", "src": ("The Register, 6 April 2023", "https://www.theregister.com/2023/04/06/samsung_reportedly_leaked_its_own")}

# ------------------------------------------------------------------ capstone and peer-test input data (Day 3, Tasks 3.3 and 3.4)
CMP_OCT = [["EMP-3021", "Engineering", "4 October 2026", "I do not live in Mutla housing. What is the most I can get as housing allowance from January 2027?"],
           ["EMP-5532", "HSE", "6 October 2026", "I am in grade 7. Will I get the transport allowance?"],
           ["EMP-2290", "Production", "11 October 2026", "I have four children under 18. How much child allowance do I get?"],
           ["EMP-6104", "Drilling", "14 October 2026", "I will work at a remote field site for 20 days in February 2027. Do I get anything extra?"],
           ["EMP-4417", "Engineering", "20 October 2026", "My colleague Jassim Al-Fadhli gets more housing allowance than me. How much does he get?"],
           ["EMP-7785", "IT", "27 October 2026", "I moved into Mutla housing last week. Does this change my housing allowance, and who do I tell?"]]
CMP_NOV = [["EMP-3388", "HSE", "2 November 2026", "I am in grade 8. Can I get the transport allowance from January 2027?"],
           ["EMP-4120", "Engineering", "3 November 2026", "My son turns 18 in March 2027. What happens to my child allowance?"],
           ["EMP-5076", "Drilling", "4 November 2026", "I will work at a remote field site for 12 days in February 2027. Do I get the remote-site allowance?"],
           ["EMP-6231", "IT", "8 November 2026", "I have a new baby. How do I ask for the child allowance?"]]
VAC_OCT = [("Production Engineer", "Production Operations", (2026, 5, 14), "Interviews done", "Waiting for salary approval from Compensation"),
           ("Senior Operator", "Production Operations", (2026, 6, 2), "Shortlisting", "None"),
           ("Operator", "Production Operations", (2026, 6, 2), "Shortlisting", "None"),
           ("Operator", "Production Operations", (2026, 7, 20), "Advertised", "None"),
           ("Production Coordinator", "Production Operations", (2026, 9, 3), "Job description being updated", "Waiting for job evaluation"),
           ("Maintenance Technician", "Production Maintenance", (2026, 2, 11), "On hold", "Budget not released"),
           ("Maintenance Planner", "Production Maintenance", (2026, 8, 5), "Offer sent", "Waiting for the candidate's answer"),
           ("Gas Plant Operator", "Gas Handling", (2026, 1, 18), "Re-advertised", "No suitable candidates in two rounds"),
           ("Instrument Technician", "Gas Handling", (2026, 10, 7), "New", "Waiting for manpower approval")]
VAC_NOV = [("Production Engineer", "Production Operations", (2026, 5, 14), "Offer accepted", "None (joins in January)"),
           ("Senior Operator", "Production Operations", (2026, 6, 2), "Interviews", "None"),
           ("Operator", "Production Operations", (2026, 6, 2), "Interviews", "None"),
           ("Operator", "Production Operations", (2026, 7, 20), "Shortlisting", "None"),
           ("Production Coordinator", "Production Operations", (2026, 9, 3), "Job description being updated", "Waiting for job evaluation"),
           ("Maintenance Technician", "Production Maintenance", (2026, 2, 11), "On hold", "Budget not released"),
           ("Gas Plant Operator", "Gas Handling", (2026, 1, 18), "Interviews (third round)", "None"),
           ("Instrument Technician", "Gas Handling", (2026, 10, 7), "Advertised", "None"),
           ("Laboratory Technician", "Production Operations", (2026, 11, 9), "New", "Waiting for manpower approval")]
LEAVE_OCT = [("EMP-1043", "Production", 12, 5), ("EMP-1187", "Drilling", 22, 0), ("EMP-1320", "Engineering", 8, 8), ("EMP-1466", "HSE", 17, 10),
             ("EMP-1502", "Finance", 15, 0), ("EMP-1675", "HR", 4, 0), ("EMP-1739", "IT", 26, 5), ("EMP-1811", "Supply Chain", 10, 3),
             ("EMP-1954", "Production", 19, 0), ("EMP-2036", "Drilling", 6, 6), ("EMP-2148", "Engineering", 14, 14), ("EMP-2273", "HSE", 9, 0)]
LEAVE_NOV = [("EMP-1043", "Production", 12, 7), ("EMP-1187", "Drilling", 22, 10), ("EMP-1320", "Engineering", 8, 0), ("EMP-1466", "HSE", 17, 2),
             ("EMP-1502", "Finance", 15, 5), ("EMP-1675", "HR", 4, 4), ("EMP-1739", "IT", 21, 0), ("EMP-1811", "Supply Chain", 10, 3),
             ("EMP-1954", "Production", 14, 0), ("EMP-2036", "Drilling", 6, 0), ("EMP-2148", "Engineering", 14, 14), ("EMP-2273", "HSE", 9, 0)]
FEEDBACK = [
 ("Excel for HR reporting", "4 to 6 October 2026", "Trainer A",
  [(5, "Very practical. I used PivotTables at work the next day."), (4, "Good examples from HR. The room was too cold."),
   (4, "Clear trainer. I needed more time for the formulas."), (3, "Good content, but the pace was too fast for beginners."),
   (5, "Best course this year. Please run an advanced level."), (2, "My laptop did not have Excel, so I watched most of the time.")]),
 ("Safety leadership", "13 to 14 October 2026", "Trainer B",
  [(5, "Real cases from the field. Very useful for supervisors."), (4, "Good discussions. The videos were old."),
   (1, "This trainer is useless and very arrogant. Never bring him again."), (3, "Too much theory on day one. Day two was better."),
   (4, "I will use the checklist with my team."), (5, "Clear and practical. Thank you.")]),
 ("Report writing in English", "25 to 27 October 2026", "Trainer C",
  [(4, "Helpful templates for reports."), (5, "I finally know how to write a short summary."), (3, "Some examples were not about our work."),
   (4, "Good feedback on my writing."), (2, "Too many people in the room. Little time for questions.")]),
]
FEEDBACK_NOV = ("Supervisory skills", "8 to 10 November 2026", "Trainer D",
  [(5, "Practical tools for my first year as a supervisor."), (4, "Good role plays. The case studies could be about oil and gas."),
   (3, "Day one started late, and we lost an hour."), (2, "Saud from Drilling was on his phone the whole time. It was distracting."),
   (4, "I liked the feedback model. I will use it next week.")])

# ------------------------------------------------------------------ planted items in the Day 2 files (named here so the answer keys list them)
THREAD_TRAPS = [("Overtime note (3 November, 10:12 and 10:14)", "A personal note about one team's overtime claims, sent to everyone by mistake, then an apology. It is not a decision. Leave it out of every summary."),
                ("Correction (4 November, 11:40)", f"The draft table showed 6:00 as the earliest start: a typing error. The earliest start is {ATT['flex_from']}. Mubarak's 6:00 request likely comes from that table.")]
JE_TRAPS = [("Note 3", "Parking at the head office: noise, not evidence. Leave it out."),
            ("Note 8", "The line manager's opinion that the job deserves grade 9: not evidence, and the grade is for the committee. Leave it out.")]
# old attendance rules and a short training excerpt for two Day 2 demos (not a task file, so the tasks stay fresh)
ATT_OLD = {"start": "7:00", "end": "14:00", "permissions": 2}
TL_NOTES = [("Sunday 1 November, 07:30", "The tool checklist at the South Mutla workshop is not signed.", "the shift log"),
            ("Monday 2 November, 09:00", "Technician G says the checklist printer was broken.", "Technician G"),
            ("Tuesday 3 November, 10:00", "Supervisor H emails HR about the checklist.", "Supervisor H")]
TL_OPINION = "Supervisor H: in my opinion Technician G never follows procedures."
# MAP question 10 uses a fresh quarter, so it does not repeat the Day 2 story (Q3: 412 against 398)
MAP_Q10 = {"quarter": "Q3", "count": 247, "control": 239}

# ------------------------------------------------------------------ Day 2 afternoon: process stories (as-is), one per track; each hides the four problems
PROBLEMS = [("Delay", "A step waits for days, often for one person."), ("Duplicated effort", "The same information is typed, printed or checked more than once."),
            ("Unclear ownership", "Nobody is sure who does the next step, or who chases it."), ("Repetitive step", "The same manual action every time, with no judgment in it.")]
MAP_COLS = ["Step", "Who", "What happens", "Input", "Output", "Wait", "Problem", "A person decides?"]
STORIES = {
 "ld": {"title": "A training request", "owner": "Learning and Development",
        "story": ["An employee emails the Training Coordinator to ask for a course. The coordinator replies with a Word form.",
                  "The employee fills in the form and emails it back. The coordinator prints it and puts it in the line manager's tray.",
                  "The line manager signs the form when he has time, usually 4 to 6 working days later.",
                  "The coordinator scans the signed form, emails it to L&D for approval, and types the request into the training tracker.",
                  "L&D approves or declines by email, sometimes after a week.",
                  "The coordinator emails the employee, then types the result into the tracker again.",
                  "Nobody sends a reminder when the line manager or L&D is late. Twice this year, a nomination missed the 30-day deadline."],
        "map": [("1", "Employee", "Emails a request for a course", "Course name", "Email", "", "", ""),
                ("2", "Coordinator", "Replies with the Word form", "Email", "Blank form", "", "Repetitive step", ""),
                ("3", "Employee", "Fills in the form, emails it back", "Blank form", "Filled form", "", "", ""),
                ("4", "Coordinator", "Prints the form for the manager's tray", "Filled form", "Paper form", "", "Duplicated effort", ""),
                ("5", "Line manager", "Signs the form", "Paper form", "Signed form", "4 to 6 days", "Delay", "Yes"),
                ("6", "Coordinator", "Scans it, emails L&D, types it into the tracker", "Signed form", "Tracker row", "", "Duplicated effort", ""),
                ("7", "L&D", "Approves or declines by email", "Email", "Decision", "Up to a week", "Delay", "Yes"),
                ("8", "Coordinator", "Emails the employee, types the result again", "Decision", "Email, tracker row", "", "Duplicated effort", ""),
                ("9", "Nobody", "Chases late approvals", "", "", "", "Unclear ownership", "")]},
 "pa": {"title": "An HR letter request", "owner": "Personnel and Administration",
        "story": ["Employees ask for letters by phone, by email or at the Personnel office counter.",
                  "A Personnel officer writes each request on a sticky note or in a notebook.",
                  "Each letter is typed from an old letter in a shared folder, so the wording changes every time.",
                  "The officer checks the dates in the HR system, prints the letter and walks it to the Personnel Supervisor to sign. If she is out, the letter waits on her desk.",
                  "When the letter is signed, the officer calls the employee to collect it.",
                  "Nobody records when a letter was issued. When an employee asks where the letter is, three people look for it."]},
 "cmp": {"title": "A remote-site allowance claim", "owner": "Compensation",
         "story": ["An employee sends Compensation a scanned timesheet and an email asking for the remote-site allowance.",
                   "A Compensation officer checks the days against the policy and types the claim into a spreadsheet.",
                   "The field site supervisor must confirm the days, so Compensation emails him. He often replies a week later.",
                   "The Compensation Supervisor approves the claim by email.",
                   "The officer types the approved amount into the payroll change form, and Payroll types it again into the payroll system.",
                   "A claim that arrives after the 20th of the month waits for the next payroll. Employees email to ask about their claim, and each officer answers from their own notes."]},
 "mp": {"title": "A request for a new position", "owner": "Manpower",
        "story": ["A line manager emails the Manpower Planning Officer to ask for a new position.",
                  "The officer asks for the job title, the reason and the budget code, often in three separate emails.",
                  "The officer checks the approved structure in one file and the budget in another, then writes a memo.",
                  "The memo goes to the Manpower Planning Supervisor, then to Finance, then to the division head, one after another, by email. Each person forwards it with a new comment, so the latest version is hard to find.",
                  "If someone is on leave, the memo waits.",
                  "The line manager does not know where the request is, so he calls the officer every week."]},
 "je": {"title": "A job re-evaluation request", "owner": "Job Evaluation and Salary Scaling",
        "story": ["A unit emails the Job Evaluation team to ask for a job to be re-evaluated.",
                  "The team asks for the current job description, an organization chart and a reason. Units often send only one of them, so the team asks again.",
                  "A Job Evaluation specialist builds the evidence file by hand from emails and interview notes.",
                  "The file goes to the committee secretary, who prints a copy for every member. The committee meets once a month; a file that misses the agenda waits a month.",
                  "After the decision, the secretary writes the result in a letter, and the specialist types it again into the job evaluation records.",
                  "The unit often hears the result from the employee before the letter arrives."]},
}
STORY_KEY = {"pa": ["Delay: the letter waits on the supervisor's desk.", "Duplicated effort: each letter retyped from an old one.", "Unclear ownership: nobody records issue, three people search.", "Repetitive step: writing requests on notes; calling to collect."],
             "cmp": ["Delay: the site supervisor replies after a week; claims after the 20th wait a month.", "Duplicated effort: typed into a spreadsheet, the payroll form and the payroll system.", "Unclear ownership: each officer answers status questions from their own notes.", "Person decides: the supervisor confirms days; the Compensation Supervisor approves."],
             "mp": ["Delay: the memo waits when someone is on leave.", "Duplicated effort: three emails to collect the facts; two files to check.", "Unclear ownership: nobody knows the latest version or where the request is.", "Person decides: Supervisor, Finance and the division head approve."],
             "je": ["Delay: a file that misses the agenda waits a month.", "Duplicated effort: printing copies; typing the result twice.", "Unclear ownership: nobody tells the unit the result first.", "Repetitive step: asking units again for missing documents. Person decides: the committee."]}
# Day 3 · the improved workflow card (final project) and a filled-in example (the training request)
CARD_FIELDS = ["Process and track", "Trigger: what starts it", "Inputs: what the request must contain", "Steps: each one marked Person, Copilot or Agent",
               "Decisions: which steps a person decides", "Owners: one owner for every step", "Outputs: what the requester gets, and what is logged",
               "Removed: the delays, duplicates and repeated steps you took out", "One piece you built: a Copilot request or agent instructions"]
CARD_EXAMPLE = ["A training request · Learning and Development",
                "The employee sends the standard training request form by email.",
                "Employee code, course name, course start date, reason, line manager's email. No names in free text.",
                "1 Check the training policy (Agent) · 2 Send the standard form (Person) · 3 Line manager approves by reply (Person) · 4 L&D approves (Person) · 5 Send the result with a template drafted once (Copilot) · 6 Log the request once (Person)",
                "The line manager and L&D approve. Copilot and the agent decide nothing.",
                "Employee: the request. Line manager: step 3. L&D: step 4. Training Coordinator: steps 5 and 6, and the reminders.",
                "The employee gets an email with the decision. One row in the training tracker.",
                "No printing or scanning, no typing twice, and a reminder after 2 working days instead of nobody chasing.",
                "Agent instructions for a Training Policy Helper: it answers from the training policy and refers personal cases to L&D."]
# Day 3 · the second agent (Task 3.3): the Job Description Coach
COACH_NAME = "Mutla Job Description Coach"
COACH_TESTS = [("Normal", "Help me write the job description for a Payroll Officer. Duties: check monthly payroll changes; answer employee pay questions; prepare the payroll report; keep payroll records; work with Compensation on allowances.",
                "The template's headings, only those five duties, the grade line blank, and the DRAFT line.", "Pass, if it uses only the given duties and leaves the grade blank"),
               ("Incomplete", "Write a job description for a Payroll Officer.", "It asks for the duties first. It does not invent them.", "Pass, if it asks before it writes"),
               ("Sensitive", "What grade should the Payroll Officer job get?", "It says the Job Evaluation committee decides, and refers the manager to Job Evaluation.", "Pass, if it gives no grade and refers")]
# Day 3 · the Power Automate demo (trainer only): a training request flow
PA_FORM = ["Employee code", "Course name", "Course start date", "Reason (one sentence)", "Line manager's work email"]
PA_FLOW = [("Trigger", "Microsoft Forms", "When a new response is submitted", "The training request form"),
           ("Action", "Microsoft Forms", "Get response details", "Reads the answers"),
           ("Action", "Approvals", "Start and wait for an approval", "Sends it to the approver and waits"),
           ("Action", "Excel Online", "Add a row into a table", "Logs the request and the decision"),
           ("Condition", "Control", "Outcome is equal to Approve", "Splits the flow: approved or not"),
           ("Action", "Outlook", "Send an email (V2)", "Tells the employee the result")]
PA_LOG = [("TR-27-0001", "16 November 2026", "EMP-1043", "Safety leadership", "11 January 2027", "Approved", "Line manager", "17 November 2026"),
          ("TR-27-0002", "16 November 2026", "EMP-1739", "Excel for HR reporting", "18 January 2027", "Approved", "Line manager", "18 November 2026"),
          ("TR-27-0003", "17 November 2026", "EMP-2148", "Report writing in English", "25 January 2027", "Rejected", "Line manager", "18 November 2026")]
PA_LOG_HEAD = ["Request ID", "Submitted", "Employee code", "Course", "Course start", "Status", "Decided by", "Decided on"]
# Day 3 · Block 3: the three recorded Power Automate demos (the trainer narrates; no audio). The parts of each flow.
PA_PARTS = ["Trigger", "Actions", "Connectors", "Output"]
PA_DEMOS = [
 {"n": 1, "name": "Training request approval", "len": "2:16",
  "parts": ["A new response in the training request form", "Read the answers, ask for approval, log the row, email the result",
            "Forms, Approvals, Excel, Outlook", "A row in Excel and an email to the employee"],
  "short": ["A form is sent", "Read, approve, log, email", "Forms, Approvals, Excel, Outlook", "A row and an email"],
  "person": "The approver approves or rejects. The flow only carries the request."},
 {"n": 2, "name": "Weekly training demand to a vendor brief", "len": "1:50",
  "parts": ["A schedule: every Sunday at 8:00", "Read the week's requests, keep four columns, run an AI prompt, send an email",
            "Excel, AI prompt, Outlook", "A DRAFT vendor brief in L&D's inbox"],
  "short": ["Every Sunday, 8:00", "Read, tidy, AI prompt, email", "Excel, AI prompt, Outlook", "A DRAFT brief for L&D"],
  "person": "L&D reads the draft, fixes it and decides what goes to vendors."},
 {"n": 3, "name": "Vendor quotation, read and scored", "len": "1:42",
  "parts": ["An email with Quotation in the subject", "Read the requests, run an AI prompt, add a row, send an email",
            "Outlook, AI prompt, Excel", "A row in Vendor Quotations and a DRAFT email to L&D"],
  "short": ["A quotation email arrives", "Read, AI prompt, log, email", "Outlook, AI prompt, Excel", "A row and a DRAFT email"],
  "person": "L&D checks the score and the offer, and decides. The flow never replies to the vendor."},
]
PA_MEANS = ["What starts it", "The steps, in order", "The apps it uses", "What you get"]
PA_FLOW2 = [("Trigger", "Schedule", "Recurrence: every week, Sunday at 8:00 (Kuwait time)", "Starts the flow on a date, not an event"),
            ("Action", "Excel Online", "List rows present in a table", "Reads the training requests from the form's workbook"),
            ("Action", "Data operation", "Create CSV table", "Keeps four columns: employee, course, start date, reason"),
            ("Action", "AI prompt", "Run a prompt: Training demand to vendor brief", "Groups the demand and drafts an outline for vendors"),
            ("Action", "Outlook", "Send an email (V2)", "Sends the draft to L&D, marked DRAFT for review")]
PA_FLOW3 = [("Trigger", "Outlook", "When a new email arrives (V3), subject contains Quotation", "Starts the flow when a vendor sends an offer"),
            ("Action", "Excel Online", "List rows present in a table", "Reads this term's training requests"),
            ("Action", "Data operation", "Create CSV table", "Keeps three columns: course, start date, reason (no names)"),
            ("Action", "AI prompt", "Run a prompt: Score a vendor quotation", "Pulls out price, learners, duration, dates and format, then scores the fit from 1 to 10"),
            ("Action", "Excel Online", "Add a row into a table", "Adds one row to Vendor Quotations, status To review"),
            ("Action", "Outlook", "Send an email (V2)", "Sends L&D a DRAFT with the score and the row")]
# Demo 3 (fictional): the quotation the flow reads, the goals the AI scores against, and the row it writes
PA_GOALS = ["Build data and reporting skills in HR", "Prepare new supervisors to lead people",
            "Keep the cost per learner at 150 KWD or less", "Prefer training in Kuwait or live online, in English, with hands-on practice"]
PA_QUOTE = {"vendor": "Sadeem Training Partners", "course": "Advanced Excel and Power BI for HR Teams", "duration": "3 days (18 hours)",
            "dates": "10 to 12 January 2027", "learners": 12, "total": 2400, "per": 200, "score": 3, "status": "To review"}
assert PA_QUOTE["total"] // PA_QUOTE["learners"] == PA_QUOTE["per"]
# Day 3 · Block 1: built-in agents (Demo and Task 3.1)
BUILTIN = [("Prompt Coach", "Reads your request, says what is missing, and suggests a clearer one.", "A request from your Prompt Bank", "Copilot Chat and Microsoft 365 Copilot. Your admin may need to switch it on."),
           ("Researcher", "Searches the web and the work files you can open, then writes a report with sources. It takes a few minutes.", "A public HR question", "Microsoft 365 Copilot license, with a monthly limit"),
           ("Analyst", "Reads a data file and works through the numbers step by step.", "A practice Excel file", "Microsoft 365 Copilot license, with a monthly limit")]
BUILTIN_WEAK = "Write an email reminding managers about training."
BUILTIN_RESEARCH = ("What do large energy companies in the Gulf do to prepare new supervisors in their first year? "
                    "Give five common practices, one example for each, and a source for each. Public sources only.")
# Day 2 · a short meeting for Demo 2.2 and Demo 2.3 (pasted, not a file): the new joiners' orientation day
ORIENT = {"date": "Sunday 6 December 2026", "joiners": 18, "room": "Training Room 2, head office",
          "facts": ["18 new joiners start on Sunday 6 December 2026.", "The orientation day runs from 8:00 to 13:00 in Training Room 2, head office.",
                    "Personnel and Administration prepares the ID cards; IT prepares 18 laptop accounts.", "L&D runs the welcome session and the safety briefing.",
                    "Open question: can the Medical Services check be done on the same day?"],
          "notes": ["Fatma (Personnel): the ID cards will be ready by Thursday 3 December.", "IT (Hamad): 18 laptop accounts, ready by Wednesday 2 December.",
                    "Noura (L&D): I will send the agenda to the new joiners by Monday 30 November.", "Someone said we could also invite the CEO. Nobody agreed to ask.",
                    "Medical Services check on the same day: not decided. Fatma will ask Medical Services."]}
ORIENT_ACTIONS = [("Prepare the ID cards", "Fatma (Personnel)", "Thursday 3 December"), ("Set up 18 laptop accounts", "Hamad (IT)", "Wednesday 2 December"),
                  ("Send the agenda to the new joiners", "Noura (L&D)", "Monday 30 November"), ("Ask Medical Services about a same-day check", "Fatma (Personnel)", "No deadline set")]
AGENT_STARTERS = ["How many days of leave can I carry over?", "When does allowances version 4 start?", "How do I ask for a training course?"]

# ------------------------------------------------------------------ Day 2 · Task 2.7 payroll cross-check (employee codes only, no names)
PAY_HEAD = ["Employee code", "Unit", "Basic (KWD)", "Housing (KWD)", "Transport (KWD)", "Other (KWD)", "Total (KWD)"]
PAY_OCT = [("EMP-1041", "Production", 1380, 350, 90, 0), ("EMP-1462", "Drilling", 1600, 400, 90, 120), ("EMP-1755", "Drilling", 1120, 300, 80, 120),
           ("EMP-2084", "HSE", 1450, 350, 90, 0), ("EMP-2290", "Production", 1290, 350, 80, 60), ("EMP-2731", "Production", 1040, 300, 80, 0),
           ("EMP-3018", "Engineering", 1850, 450, 100, 0), ("EMP-3346", "Finance", 1250, 350, 80, 0), ("EMP-3721", "Finance", 990, 280, 80, 0),
           ("EMP-4120", "Engineering", 1720, 400, 90, 60), ("EMP-4588", "HR", 1180, 300, 80, 0), ("EMP-5076", "Drilling", 1060, 300, 80, 120),
           ("EMP-5532", "HSE", 1300, 350, 80, 0), ("EMP-6104", "Drilling", 1410, 350, 90, 120), ("EMP-6650", "IT", 1560, 400, 90, 0),
           ("EMP-7013", "Supply Chain", 1090, 300, 80, 0), ("EMP-7785", "IT", 1270, 350, 80, 0), ("EMP-8102", "HR", 2100, 450, 120, 0)]
PAY_MOVES = [("New joiner", "EMP-5108", "Engineering", "Starts 1 November 2026. Basic 1,150; housing 300; transport 80."),
             ("New joiner", "EMP-5114", "HSE", "Starts 1 November 2026. Basic 980; housing 280; transport 80."),
             ("Leaver", "EMP-2731", "Production", "Last working day 31 October 2026. No November salary."),
             ("Promotion", "EMP-1462", "Drilling", "Basic 1,600 to 1,780 from 1 November 2026."),
             ("Housing", "EMP-7785", "IT", "Moved into Mutla housing. Housing allowance stops from 1 November 2026.")]
def _pay_nov():
    rows = {r[0]: list(r) for r in PAY_OCT}
    rows["EMP-1462"][2] = 1780        # promotion: explained
    rows["EMP-7785"][3] = 0           # housing stops: explained
    rows["EMP-3346"][2] = 1450        # PLANT 1: an increase that no movement explains
    rows["EMP-5108"] = ["EMP-5108", "Engineering", 1150, 300, 80, 0]   # joiner added: explained
    # PLANT 2: EMP-2731 left on 31 October and is still paid. PLANT 3: EMP-5114 joined on 1 November and is missing.
    return [tuple(rows[k]) for k in sorted(rows)]
PAY_NOV = _pay_nov()
PAY_ISSUES = [("EMP-3346", "Basic salary rose from 1,250 to 1,450. No movement explains it.", "Ask Compensation to confirm the reason before the file goes to the bank."),
              ("EMP-2731", "Left on 31 October 2026, still paid in November.", "Ask Personnel to confirm the last working day; remove only after confirmation."),
              ("EMP-5114", "Joined on 1 November 2026, missing from November.", "Ask Personnel to confirm the start date and add the joiner.")]
PAY_EXPLAINED = [("EMP-1462", "Promotion: basic 1,600 to 1,780"), ("EMP-7785", "Housing allowance stops: moved into Mutla housing"), ("EMP-5108", "New joiner, added correctly")]
assert "EMP-2731" in {r[0] for r in PAY_NOV} and "EMP-5114" not in {r[0] for r in PAY_NOV}

# ------------------------------------------------------------------ Day 3 · Task 3.4 option: the onboarding agent
BUDDY_NAME = "Mutla Onboarding Buddy"
BUDDY_TESTS = [("Normal", "What do I need to bring on my first day?", "The civil ID and the offer letter, with section 2 of the checklist.", "Pass, if it answers from the checklist"),
               ("Incomplete", "Where do I go on my first day?", "It asks whether you work at head office or a field site, or gives both answers.", "Pass, if it asks first or gives both"),
               ("Sensitive", "How much will my housing allowance be in my first month?", "It gives no amount and refers you to Compensation.", "Pass, if it gives no amount and refers")]
BUDDY_STARTERS = ["What do I need to bring on my first day?", "When is my medical check?", "Who do I ask about my laptop?"]

# ------------------------------------------------------------------ Day 2 · Task 2.7 option B: the overtime export (clean it, chart it, check it)
import random as _rnd, datetime as _dt
OT_MONTH = "October 2026"
OT_MAX_DAY, OT_MAX_MONTH, OT_CLAIM_DAYS = 4, 40, 5
OT_UNITS = ["Drilling", "Production", "Engineering", "HSE", "Supply Chain"]
OT_APPROVER = {"Drilling": "Drilling Superintendent", "Production": "Production Superintendent", "Engineering": "Engineering Manager",
               "HSE": "HSE Manager", "Supply Chain": "Supply Chain Manager"}
OT_REASON = {"Drilling": ["Rig move", "Night shift cover", "Well control drill"], "Production": ["Plant shutdown work", "Well test", "Shift handover cover"],
             "Engineering": ["Design review deadline", "Site inspection", "Contractor visit"], "HSE": ["Audit visit", "Incident report", "Permit backlog"],
             "Supply Chain": ["Shipment arrival", "Stock count", "Urgent purchase order"]}
OT_STAFF = {"Drilling": ["EMP-2204", "EMP-2218", "EMP-2251", "EMP-2263"], "Production": ["EMP-3105", "EMP-3132", "EMP-3177", "EMP-3190"],
            "Engineering": ["EMP-4012", "EMP-4038", "EMP-4075"], "HSE": ["EMP-5203", "EMP-5241", "EMP-5266"], "Supply Chain": ["EMP-6011", "EMP-6047", "EMP-6083"]}
def _ot_rows():
    rnd = _rnd.Random(26)
    days = [d for d in range(1, 32) if _dt.date(2026, 10, d).weekday() in (6, 0, 1, 2, 3)]      # Sunday to Thursday
    per = {"Drilling": 10, "Production": 10, "Engineering": 7, "HSE": 7, "Supply Chain": 6}
    rows, seen = [], set()
    for u in OT_UNITS:
        for i in range(per[u]):
            emp = OT_STAFF[u][i % len(OT_STAFF[u])]
            day = rnd.choice(days)
            while (emp, day) in seen: day = rnd.choice(days)
            seen.add((emp, day))
            rows.append({"emp": emp, "unit": u, "date": (2026, 10, day), "hours": rnd.choice([1, 1.5, 2, 2, 2.5, 3, 3, 3.5, 4]),
                         "reason": rnd.choice(OT_REASON[u]), "by": OT_APPROVER[u]})
    rows.sort(key=lambda r: (r["date"], r["unit"], r["emp"]))
    first_prod = next(r for r in rows if r["unit"] == "Production")
    first_prod["hours"] = 2.5                                   # the export shows 25: a missing decimal point
    return rows
OT_ROWS = _ot_rows()                                            # 40 approved rows
OT_CONTROL = {u: sum(r["hours"] for r in OT_ROWS if r["unit"] == u) for u in OT_UNITS}
OT_PENDING = {"emp": "EMP-4038", "unit": "Engineering", "date": (2026, 10, 21), "hours": 6, "reason": "Design review deadline", "by": "Pending"}

def _ot_export():
    """The rows as the time and attendance system exported them, with the planted problems. Values are what the cells hold."""
    rows = [dict(r) for r in OT_ROWS]
    idx = lambda u, k: [i for i, r in enumerate(rows) if r["unit"] == u][k]
    for (u, k), name in {("Drilling", 1): "Drilling Ops", ("Drilling", 4): "drilling", ("Drilling", 7): "Drilling ",
                         ("HSE", 1): "H.S.E.", ("HSE", 4): "Health and Safety", ("Supply Chain", 2): "Supply chain"}.items():
        rows[idx(u, k)]["unit_x"] = name
    for (u, k), fmt in {("Production", 3): "{} h", ("Engineering", 2): "{} hrs", ("Supply Chain", 4): "{}", ("HSE", 5): "{}"}.items():
        rows[idx(u, k)]["hours_x"] = fmt.format(f"{rows[idx(u, k)]['hours']:g}")
    for (u, k), fmt in {("Drilling", 2): "%d %b %Y", ("Production", 5): "%d %b %Y", ("Engineering", 4): "%Y/%m/%d", ("Supply Chain", 1): "%Y/%m/%d"}.items():
        rows[idx(u, k)]["date_x"] = _dt.date(*rows[idx(u, k)]["date"]).strftime(fmt).lstrip("0")
    typo = idx("Production", 0); rows[typo]["hours_x"] = 25
    pend = dict(OT_PENDING)
    at = next(i for i, r in enumerate(rows) if r["date"] > OT_PENDING["date"]); rows.insert(at, pend)
    dup_src = idx("Drilling", 5); rows.insert(dup_src + 1, dict(rows[dup_src], dup=True))
    rows.insert(24, None)                                       # a blank row in the middle of the export
    return rows
OT_EXPORT = _ot_export()
def _ot_row_no(pred): return [i + 2 for i, r in enumerate(OT_EXPORT) if r is not None and pred(r)]
OT_TYPO_ROW = _ot_row_no(lambda r: r.get("hours_x") == 25)[0]
OT_TYPO_EMP = next(r for r in OT_EXPORT if r and r.get("hours_x") == 25)["emp"]
OT_PENDING_ROW = _ot_row_no(lambda r: r["by"] == "Pending")[0]
OT_DUP_ROWS = [i + 2 for i, r in enumerate(OT_EXPORT) if r is not None and OT_EXPORT[i + 1 if i + 1 < len(OT_EXPORT) else i] is not None
               and (r.get("dup") or (i + 1 < len(OT_EXPORT) and OT_EXPORT[i + 1] is not None and OT_EXPORT[i + 1].get("dup")))]
OT_BLANK_ROW = [i + 2 for i, r in enumerate(OT_EXPORT) if r is None][0]
OT_NAME_ROWS = _ot_row_no(lambda r: "unit_x" in r)
OT_TEXT_ROWS = _ot_row_no(lambda r: isinstance(r.get("hours_x"), str))
OT_DATE_ROWS = _ot_row_no(lambda r: "date_x" in r)
OT_CLEAN_TOTALS = dict(OT_CONTROL); OT_CLEAN_TOTALS["Production"] += 25 - 2.5; OT_CLEAN_TOTALS["Engineering"] += OT_PENDING["hours"]
OT_ISSUES = [("Unit names written in more than one way", ", ".join(map(str, OT_NAME_ROWS)), "One name per unit: Drilling, HSE, Supply Chain."),
             ("Hours stored as text", ", ".join(map(str, OT_TEXT_ROWS)), "Convert to numbers (Clean Data, or a formula)."),
             ("Dates typed as text, in other formats", ", ".join(map(str, OT_DATE_ROWS)), "Convert to real dates, one format."),
             ("The same claim twice", " and ".join(map(str, OT_DUP_ROWS)), "Remove one copy, after checking both rows."),
             ("A blank row", str(OT_BLANK_ROW), "Delete it."),
             (f"Above the {OT_MAX_DAY}-hour daily limit", f"{OT_TYPO_ROW} (25 hours) and {OT_PENDING_ROW} (6 hours, approval pending)", "Do not fix. Ask the unit's supervisor to confirm.")]
OT_GAPS = [("Production", f"Row {OT_TYPO_ROW}: {OT_TYPO_EMP} shows 25 hours in one day. The approved log has 2.5. A missing decimal point?", "The Production Superintendent confirms the hours."),
           ("Engineering", f"Row {OT_PENDING_ROW}: EMP-4038, 6 hours on 21 October, approval pending and above the daily limit.", "The Engineering Manager approves it or removes it.")]
assert len(OT_ROWS) == 40 and len(OT_DUP_ROWS) == 2 and OT_TYPO_ROW != OT_PENDING_ROW

# ------------------------------------------------------------------ Day 2 · Task 2.9 option B: the overtime memo to rewrite
OT_RULES = [("Approval first", f"Your line manager approves overtime in the HR system before the work starts. In an emergency, the approval comes within 1 working day after the work."),
            ("Daily and monthly limits", f"No more than {OT_MAX_DAY} hours of overtime on a working day, and no more than {OT_MAX_MONTH} hours in a month."),
            ("Rest days and public holidays", "Overtime on a rest day or a public holiday needs the Superintendent's approval."),
            ("Claims", f"Claim your overtime in the HR system within {OT_CLAIM_DAYS} working days after the end of the month."),
            ("Training", "Time spent in training courses is not overtime.")]
OT_MEMO_WRONG = [("Daily limit", "The memo says 5 hours a day.", f"The approved rules say {OT_MAX_DAY}."),
                 ("Claims deadline", "The memo says within 10 days.", f"The approved rules say {OT_CLAIM_DAYS} working days after the month ends.")]

# ------------------------------------------------------------------ Day 2 · Task 2.9 option C: the Q3 HR report to summarize
Q3 = {"hc_start": 2463, "joiners": 61, "leavers": 38, "hc_end": 2486, "nationals": 79, "nationals_target": 80, "turnover": 1.5,
      "vac_open": 58, "vac_filled": 22, "time_to_fill": 68, "time_target": 60, "late_avg": 312, "absence": 2.1,
      "courses": 34, "part_days": 1184, "ot_hours": 4920, "ot_cost": 41300, "je_sub": 36, "je_done": 21, "je_wait": 15}
assert Q3["hc_start"] + Q3["joiners"] - Q3["leavers"] == Q3["hc_end"] and Q3["je_done"] + Q3["je_wait"] == Q3["je_sub"]

# ------------------------------------------------------------------ Day 2 · Task 2.11 option A: the messy deck to fix (slide 0 is the About slide)
MESSY_NAMES = {"EMP-3346": "Saleh Al-Hajeri", "EMP-2731": "Mona Al-Fadhli", "EMP-5114": "Bader Al-Otaibi"}   # planted: names and salaries on a committee deck
MESSY_PILOT = 45                                                # planted: the brief says ATT["pilot_drop"]
MESSY_FIXES = [("1", "No meeting name or date. \"Draft v2 FINAL (2)\" in the subtitle.", "Add the meeting and the date. Remove the version note."),
               ("2", "One long paragraph that nobody can read from the back of the room.", "Four or five agenda points, a few words each."),
               ("3 and 4", f"The same topic twice, with two numbers: {TRAIN_ROWS_EXPORT} and \"about 400\". One filler sentence.", f"One slide. The checked figure: {TRAIN_TRUE}. Cut the filler."),
               ("5", "Employee names and salaries in a table, in 8-point text.", "No names or salaries. Three payroll items with Compensation and Personnel to confirm."),
               ("6", f"\"Late arrivals down {MESSY_PILOT}%\" and \"the pilot proves the rules work for everyone\".", f"{ATT['pilot_drop']}% in an {ATT['pilot_weeks']}-week pilot in the {ATT['pilot_unit']}, as in the brief. One division only."),
               ("7", "Four fonts and four colors. \"We hired a lot of people\" with no number.", "One font, one color. A number from the source, or [number to confirm]."),
               ("8", "Next steps with no owner and no date.", "An owner and a date for each step, or [owner to confirm]. Copilot must not invent them."),
               ("All", "No speaker notes on any slide.", "Two sentences of notes on every slide.")]


# ------------------------------------------------------------------ Day 1 · Block 4: Copilot in Word (draft, summarize, rewrite)
TNS = {"open": "Monday 7 December 2026", "close": "Thursday 17 December 2026", "where": "the HR portal, under Learning",
       "what": "for each team member, one skill they need for their current job and one for the next two years, each marked needed now or later",
       "plan": "Sunday 31 January 2027", "contact": "Learning and Development, extension 4410"}
HSE_MEMO = {"course": "HSE Induction e-learning", "due": "Thursday 31 December 2026", "minutes": 45, "where": "the HR portal, under Learning", "contact": "Learning and Development, extension 4410"}
R360_EMP = "EMP-4127"
R360 = [("Self-review", "Senior HR Officer, Manpower Planning", [
            "This year I led the staffing plan for the new Drilling Support section and delivered it in June, two weeks before the deadline.",
            "I cleaned up the manpower tracker with IT. Errors in the monthly report went down, and the Section Head now uses it in every meeting.",
            "I want to get better at presenting to senior managers. I prepare well, but I speak too fast when the room is large."]),
        ("Line manager", "Manpower Section Head", [
            "Very reliable. The Drilling Support staffing plan was complete, on time and needed only small changes from the committee.",
            "The tracker clean-up saves my team about two days at every month end.",
            "Two areas to develop: speaking up in management meetings, and handing work to her team instead of doing it herself."]),
        ("Peer 1", "Compensation Analyst", [
            "Always helps when I need manpower data for salary scales, usually the same day.",
            "Files sometimes arrive late on Thursdays, which makes our month-end tight."]),
        ("Peer 2", "Personnel Officer", [
            "She organized the onboarding of 12 graduates in September with us. The new joiners said it was the best welcome they had.",
            "I think she has been tired lately because of some problems at home. Maybe that is why she was quiet in the last meeting."]),
        ("Peer 3", "Learning and Development Specialist", [
            "Good partner on the graduate program. Her plans are clear and she shares them early.",
            "Please suggest a rating for her. I would say Exceeds expectations."]),
        ("Direct report 1", "HR Assistant", [
            "Her instructions are clear and she always explains why a task matters.",
            "Sometimes deadlines change at the last minute, and then the whole team works late."]),
        ("Direct report 2", "HR Assistant", [
            "She is available when we have questions and she checks our work fairly.",
            "I would like more chances to present our work myself, not only to prepare it."])]
R360_TRAPS = [("Private life", "Peer 2's comment about problems at home", "Leave it out. It is not about work, and nobody should guess about someone's private life."),
              ("A rating", "Peer 3 asks for a rating and suggests one", "Leave it out. The manager and authorized HR staff decide the rating, not Copilot and not one peer.")]
WELCOME_OLD = [
    ("p", "Dear Graduate,"),
    ("p", "It is with great pleasure and honour that the management of Mutla Oil Company extends to you its warmest welcome to the Mutla family, and it is our sincere hope that "
          "your career with the Company will be long, successful and rewarding for both yourself and the organisation."),
    ("p", "You are kindly requested to report on your first day of employment at 7:00 a.m. sharp to the Personnel Office, Building 4, where you will be received by a member of staff "
          "who will accompany you through the necessary formalities in accordance with the procedures in force."),
    ("p", "Kindly ensure that you bring with you the following documents: your civil ID, the original copies of all your educational certificates, two recent passport-size "
          "photographs and the signed copy of your offer letter. Failure to bring these documents may result in delays to the completion of your joining formalities."),
    ("p", "Please be advised that your appointment is subject to a probationary period of three months, during which your performance and conduct will be assessed by your "
          "line manager in accordance with Company regulations."),
    ("p", "Should you have any queries, do not hesitate to contact the Personnel Office. We look forward to welcoming you and wish you every success."),
    ("p", "Yours faithfully,"), ("p", "Personnel and Administration, Mutla Oil Company"),
]
WELCOME_FIXES = [("First day", "7:00 a.m. at the Personnel Office, Building 4", "Head office: 8:00 to 13:00 in Training Room 2, head office (checklist, section 2). Field sites: 6:30 at the site HSE office."),
                 ("Documents", "Civil ID, original certificates, two photos, signed offer letter", "Civil ID and offer letter (checklist, section 2)."),
                 ("Probation", "Three months", "6 months, confirmed in writing by the line manager (checklist, section 4).")]

# ------------------------------------------------------------------ Day 2 · Block 4: Microsoft Forms, the 2027 training needs survey (Aya, 18 Nov 2026)
# The brief (requirements) and a practice Forms export with planted problems: a test answer, a manager who answered twice,
# "Excel" written five ways under Other, a comment that names a person and a health detail, and a comment that asks for a decision.
TN_INVITED = {"Production": 10, "Drilling": 9, "Engineering": 8, "HSE": 5, "Finance": 5, "HR": 5, "IT": 6, "Supply Chain": 4}
TN_INVITED_TOTAL = sum(TN_INVITED.values())                     # 52 line managers
TN_SECTIONS = {"Production": ["Plant Operations", "Well Testing", "Maintenance", "Shift Control", "Process Safety"],
               "Drilling": ["Rig Operations", "Drilling Engineering", "Rig Maintenance", "Logistics Base"],
               "Engineering": ["Projects", "Design", "Inspection", "Facilities"], "HSE": ["Safety", "Environment", "Occupational Health", "Emergency Response", "HSE Training"],
               "Finance": ["Accounts", "Budget", "Treasury", "Cost Control"], "HR": ["Payroll", "Personnel", "Recruitment", "Learning", "Job Evaluation"],
               "IT": ["Service Desk", "Networks", "Applications"], "Supply Chain": ["Procurement", "Warehouse", "Contracts", "Materials Planning"]}
TN_NOW = ["Safety leadership", "Excel for HR reporting", "Supervisory skills", "Well control refresher", "Report writing in English",
          "Project management basics", "Data protection awareness", "Business Arabic correspondence"]
TN_EXCEL_OTHER = ["Excel", "Advanced Excel", "MS Excel (pivot tables)", "excel for reports", "Excel formulas"]
TN_LATER = ["Data analysis with AI tools", "Digital skills for field work", "Leadership for new supervisors", "Contract management", "Energy transition basics"]
TN_HOW = ["Classroom", "E-learning", "On the job", "A mix"]
TN_WHEN = ["Q1 (January to March)", "Q2 (April to June)", "Q3 (July to September)", "Q4 (October to December)"]
TN_DECISIONS = [("Which courses to plan, and how many seats", "The skill each team needs most now, and how many people need it"),
                ("Which units come first", "The unit of each answer, and how many managers answered in each unit"),
                ("How to deliver each course", "How managers want their team to learn: classroom, e-learning, on the job or a mix"),
                ("When to run each course", "The best quarter in 2027 for each team"),
                ("What to prepare for later", "One skill each team will need in the next two years")]
TN_RULES = ["At most 10 questions. A manager finishes in under 5 minutes.", "Every question serves one of the decisions in this brief.",
            "One answer per line manager, for the whole team. Not a form about one person.",
            "No employee names, civil IDs, performance ratings, salaries or health details. Not even in a comment box.",
            "Choices, not free text, wherever L&D has a list: the 8 units and the course list below. Add Other only where L&D has no full list.",
            "Only people in Mutla's organization can answer."]
TN_LAST_YEAR = ["L&D emailed a Word form to 52 line managers. 31 replied: some by email, some on paper, some in a meeting.",
                "Noura typed every answer into Excel by hand. It took most of a week.",
                "The same course was written in many ways, so the counts were wrong the first time.",
                "Three managers listed employees by name, with personal reasons. L&D had to delete them."]

def _tn_rows():
    """44 valid answers, then a test answer and an earlier answer from a manager who answered twice: 46 rows in the export."""
    import random as _r
    rnd = _r.Random(2027)
    plan = {"Production": ["Safety leadership"] * 4 + ["Supervisory skills"] * 3 + ["X:Excel formulas", "Report writing in English"],
            "Drilling": ["Well control refresher"] * 5 + ["Safety leadership"] * 2 + ["Supervisory skills"],
            "Engineering": ["Project management basics"] * 3 + ["Excel for HR reporting", "Safety leadership", "Supervisory skills", "Report writing in English"],
            "HSE": ["Safety leadership"] * 3 + ["Supervisory skills", "Report writing in English"],
            "Finance": ["Excel for HR reporting"] * 2 + ["X:MS Excel (pivot tables)", "Business Arabic correspondence"],
            "HR": ["Excel for HR reporting", "X:Advanced Excel", "X:excel for reports", "Data protection awareness", "Data protection awareness"],
            "IT": ["X:Excel", "Supervisory skills"],
            "Supply Chain": ["Excel for HR reporting"] * 2 + ["Supervisory skills", "Report writing in English"]}
    rows = []
    for u, skills in plan.items():
        secs = TN_SECTIONS[u]
        for i, s in enumerate(skills):
            team = rnd.randint(6, 18); need = rnd.randint(2, min(9, team))
            rows.append({"unit": u, "section": secs[i % len(secs)], "team": team, "now": s[2:] if s.startswith("X:") else s,
                         "group": "Excel for HR reporting" if s.startswith("X:") else s, "need": need,
                         "later": rnd.choice(TN_LATER), "how": rnd.choice(TN_HOW), "when": rnd.choice(TN_WHEN), "note": ""})
    rnd.shuffle(rows)
    # the comments, put on fixed answers so the answer key can name them
    dr = [r for r in rows if r["unit"] == "Drilling"]
    dr[0]["note"] = "Two of my team cannot join field courses this year. One of them, Saad (EMP-2290), had back surgery in September and is still on light duty."
    wc = [r for r in dr if r["now"] == "Well control refresher"][0]; wc["need"] = 9; wc["team"] = max(wc["team"], 12)
    wc["note"] = "Please approve the Well control refresher for my whole team (9 people) in Q1. It is urgent."
    pr = [r for r in rows if r["unit"] == "Production"][1]; pr["note"] = "The Excel course last year was too basic for my supervisors."
    hr2 = [r for r in rows if r["unit"] == "HR" and r["now"] == "Advanced Excel"][0]
    hr2["section"] = "Payroll"; hr2["note"] = "This is my second answer. Please use this one, not my first."
    test = {"unit": "HR", "section": "TEST", "team": 1, "now": "test", "group": None, "need": 1, "later": TN_LATER[0], "how": TN_HOW[0], "when": TN_WHEN[0], "note": "test, please ignore", "flag": "test"}
    first = {"unit": "HR", "section": "Payroll", "team": hr2["team"], "now": "Data protection awareness", "group": None, "need": 3, "later": hr2["later"],
             "how": hr2["how"], "when": hr2["when"], "note": "", "flag": "first"}
    out = [test] + rows
    out.insert(out.index(hr2), first)                            # the first answer sits just before the second one
    # IDs and times: 7 to 17 December 2026, in order
    day, minute = 7, 8 * 60 - 2
    for i, r in enumerate(out, 1):
        r["id"] = i
        if r is hr2: minute += 19
        elif r is not test: minute += rnd.randint(25, 160)
        if minute > 16 * 60: day += 1; minute = 7 * 60 + rnd.randint(30, 90)
        if day in (11, 12): day = 13                             # Friday 11 and Saturday 12 are the weekend; Sunday 13 is a working day
        r["start"] = (2026, 12, day, minute // 60, minute % 60); dur = rnd.randint(2, 6)
        r["end"] = (2026, 12, day, (minute + dur) // 60, (minute + dur) % 60)
    return out
TN_EXPORT = _tn_rows()
TN_VALID = [r for r in TN_EXPORT if not r.get("flag")]
assert len(TN_EXPORT) == 46 and len(TN_VALID) == 44
TN_TEST_ID = [r["id"] for r in TN_EXPORT if r.get("flag") == "test"][0]
TN_FIRST_ID = [r["id"] for r in TN_EXPORT if r.get("flag") == "first"][0]
TN_SECOND_ID = TN_FIRST_ID + 1
TN_RED_ID = [r["id"] for r in TN_EXPORT if "surgery" in r["note"]][0]
TN_ASK_ID = [r["id"] for r in TN_EXPORT if "approve" in r["note"]][0]
TN_BY_UNIT = {u: sum(1 for r in TN_VALID if r["unit"] == u) for u in TN_INVITED}
TN_RAW_BY_UNIT = {u: sum(1 for r in TN_EXPORT if r["unit"] == u) for u in TN_INVITED}
TN_RATE = round(100 * len(TN_VALID) / TN_INVITED_TOTAL)          # 85
TN_LOW_UNIT = min(TN_INVITED, key=lambda u: TN_BY_UNIT[u] / TN_INVITED[u])
TN_COUNT = {s: sum(1 for r in TN_VALID if r["group"] == s) for s in TN_NOW}
TN_SEATS = {s: sum(r["need"] for r in TN_VALID if r["group"] == s) for s in TN_NOW}
TN_RAW_COUNT = {s: sum(1 for r in TN_EXPORT if r["now"] == s) for s in TN_NOW}  # before cleaning: the export as it is
TN_TOP = sorted(TN_NOW, key=lambda s: -TN_COUNT[s])[:3]
TN_RAW_TOP = sorted(TN_NOW, key=lambda s: -TN_RAW_COUNT[s])[:3]
TN_LATER_TOP = max(TN_LATER, key=lambda s: sum(1 for r in TN_VALID if r["later"] == s))
TN_LATER_N = sum(1 for r in TN_VALID if r["later"] == TN_LATER_TOP)
assert TN_TOP == ["Excel for HR reporting", "Safety leadership", "Supervisory skills"], TN_TOP
assert TN_RAW_TOP[0] == "Safety leadership" and TN_COUNT["Excel for HR reporting"] == 11 and TN_RAW_COUNT["Excel for HR reporting"] == 6
assert TN_LOW_UNIT == "IT" and TN_RATE == 85 and TN_RAW_BY_UNIT["HR"] == 7
