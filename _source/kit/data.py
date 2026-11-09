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

# ------------------------------------------------------------------ the five inputs (Day 1, Block 3)
INPUTS = [("Instructions", "Who Copilot should be, the task and the shape of the answer", "You are an HR officer at Mutla. Draft a job description. One page, in the template's order."),
          ("Context", "Why you need it and who will read it", "It is for the 2026 job evaluation round. The Job Evaluation committee will read it."),
          ("Data", "The facts of this case", "Use only the attached role information for the Compensation Analyst."),
          ("Tone", "How it should sound", "Formal, neutral and plain English. No sales language."),
          ("Approved sources", "The template or policy Copilot must follow", "Follow mutla-jd-template-2026.docx. Leave the grade blank.")]
GCSE = [("Goal", "Instructions"), ("Context", "Context"), ("Source", "Data and Approved sources"), ("Expectations", "Tone, and the format inside Instructions")]

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
