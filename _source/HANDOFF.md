# Workshop Handoff: AI Fundamentals for HR

Nov 9, 2026 · @Aya

## Summary

A three-day, hands-on Microsoft Copilot workshop for HR employees, built from the approved outline and the Mastering Copilot (MCIM) structure. Approve this page and I build everything else without more questions.

|  |  |
| --- | --- |
| **Title** | AI Fundamentals for HR (the portal product name; the outline used "AI Essentials for Modern HR", see the question at the end) |
| **Type** | CODED Professionals open workshop, run because of KOC demand. CODED brand only, no client logo |
| **Cohort** | AIFHR-Nov/Nov-26 (portal, status Upcoming, capacity 25) |
| **Dates** | Tuesday 17, Wednesday 18 and Thursday 19 November 2026 |
| **Daily time** | 9:00 AM to 3:00 PM, with two short breaks and a 40-minute lunch and Dhuhr break |
| **Venue** | CODED, Alsharekh room, Frontend Campus |
| **Audience** | 10 to 25 junior and middle-level HR employees from Job Evaluation, Salary Scaling, Manpower, Personnel and Administration, Compensation, and L&D. Mixed AI familiarity, no coding |
| **Tools** | Microsoft 365 Copilot: Copilot Chat with file upload (every task), Copilot in Word, Outlook, Teams, Excel and PowerPoint (where the account has it), Prompt Gallery, Agent Builder |
| **Trainer** | Aya Alsakkaf (the portal lists Ghareeb Thiab as lead; update the cohort if needed) |
| **Fictional company** | Mutla Oil Company, a made-up Kuwaiti oil and gas company with five HR units. Never KOC's name on any file |
| **The habit** | Copilot drafts. You check. Authorized HR staff decide. |
| **Recipe** | The five inputs: Instructions, Context, Data, Tone, Approved sources |
| **Site** | coded-ai-hr.vercel.app, private repo aya-alsakkaf/coded-ai-hr |
| **Closest past builds reused** | Mastering Copilot (day shape, Agent Builder test, Prompt Gallery, capstone), KAMCO Copilot (finished-early extras, case files), Gulf Bank (engine, catch-up files) |
| **Slides** | Day 1: 60 · Day 2: 62 · Day 3: 40 |
| **Assessment** | Pre and post MAP test (14 questions, not graded), final satisfaction survey, capstone with a peer test. No scored project |

## Outcomes

These six lines are the MAP confidence items and the final survey "I can" items.

1. I can explain how Copilot produces an answer, what it can see, and why I check it.
2. I can decide which HR tasks Copilot can support, and keep personal, salary and case details out of prompts.
3. I can write a request with the five inputs: instructions, context, data, tone and approved sources.
4. I can use Copilot in Word, Outlook, Teams, Excel and PowerPoint for HR documents, messages, meeting records and summaries, and check every figure.
5. I can build and test a simple HR assistant in Agent Builder.
6. I can build a reusable prompt set for one recurring task in my unit, and test it with a colleague.

## Day 1 · Tuesday 17 November: Directing Copilot for Reliable HR Work

**Claim:** The request decides the answer, and you check it before it goes anywhere. **Integration moment:** one job description, checked against the approved template, and its request saved as the first entry in the HR Prompt Bank. **Slides: 60.**

| Time | Block | Minutes |
| --- | --- | --- |
| 09:00-09:10 | Welcome and sign-in check: open Copilot Chat, read the license label under your name | 10 |
| 09:10-09:20 | Pre-MAP test (QR on the slide; doubles as the laptop check) | 10 |
| 09:20-09:30 | Opener: one job description, two requests (weak vs strong) | 10 |
| 09:30-10:30 | Block 1 · How Copilot produces an answer · Task 1.1 | 60 |
| 10:30-10:45 | Break | 15 |
| 10:45-11:35 | Block 2 · Rules before the first request · Task 1.2 | 50 |
| 11:35-12:15 | Lunch and Dhuhr prayer | 40 |
| 12:15-13:35 | Block 3 · The five inputs of a reliable request · Task 1.3 | 80 |
| 13:35-13:50 | Break | 15 |
| 13:50-14:35 | Block 4 · Grounding and checking · Task 1.4 | 45 |
| 14:35-14:50 | Integration: your first Prompt Bank entry | 15 |
| 14:50-15:00 | Wrap and the hook for Day 2 | 10 |

**Opener (showcase).** Weak: "Write a job description for an HR officer." Strong: the five inputs, grounded in mutla-jd-template-2026.docx and the role sheet. The weak answer invents duties and a grade; the strong one follows the template and leaves the grade for Job Evaluation.

**Block 1 · How Copilot produces an answer (60 min: story 5, concepts 20, Demo 1.1 8, checks 5, Task 1.1 12, debrief 10).**

- Story: Monday 2 November, 08:40. Fatma in Personnel asks Copilot how many leave days staff can carry over. It answers 30 days at once. Mutla's policy says 15.
- Analogy → term: your phone keyboard guesses the next word → **next-word prediction**, shown live in the next-word widget ("Unused annual leave may be carried over up to…"). Then **hallucination**: fluent and wrong.
- Analogy → term: a new colleague with your keycard opens only the doors you can open → **what Copilot can see**: with a Microsoft 365 Copilot license, only files, emails and chats you already have permission to open; with Copilot Chat (Basic), only what you upload, plus the web.
- **Copilot Chat and Copilot in the apps**: one engine, different seats. The license label under your name tells you which you have.
- Demo 1.1 (prompt player): the same question with no file, then with the leave policy attached and "answer only from the file, give the section".
- Task 1.1 · Spot the confident mistake (12 min, pairs). Files: mutla-leave-policy-2026.docx, mutla-copilot-leave-answer.docx. Deliverable: the three wrong statements, each with the correct section. Finished early: write the one-line instruction that would have stopped each mistake.

**Block 2 · Rules before the first request (50 min: story 5, real case 5, concepts 15, sort demo 7, Task 1.2 12, debrief 6).**

- Story: Tuesday 3 November, 10:50. Abdulaziz in Compensation pastes a salary exception memo with two names and their salaries into a chat to "make it professional". He stops before he presses Send.
- When it was real: in 2023, Samsung employees pasted chip source code and recorded meeting notes into ChatGPT in at least three incidents; Samsung limited uploads to 1,024 bytes per question ([The Register, 6 Apr 2023](https://www.theregister.com/2023/04/06/samsung_reportedly_leaked_its_own)).
- Analogy → term: a new temp can draft letters on day one, but never signs a contract or decides a raise → **three groups**: do it yourself, Copilot supports, Copilot drafts for your review. Grades, pay, ratings, discipline and selection stay with authorized HR staff.
- Analogy → term: traffic lights for your data → **the safe-use card**: green, amber, red. Then **redact**: replace names with roles (Employee A), remove civil IDs, phone numbers, salary figures and medical details.
- Demo 1.2 (card sort): eight HR tasks, green, amber or red. Policy first: your company's AI and data rules come before the card.
- Task 1.2 · Redact a case note (12 min, solo). File: mutla-case-note-unredacted.docx (six planted sensitive items). Deliverable: a redacted copy that is safe to use with Copilot. Finished early: on the redacted copy only, ask Copilot whether any personal detail is left.

**Block 3 · The five inputs of a reliable request (80 min: felt problem 12, concepts 18, Demo 1.3 8, check 4, Task 1.3 25, debrief 13).**

- Felt problem (timer slide, 8 min): update the 2019 HR officer job description by hand. Most people finish half. Then the one-line request: fast, generic, wrong.
- Analogy → term: briefing a new colleague on day one (drawn scene) → **the five inputs**: Instructions (role, task, format), Context (why, and who reads it), Data (the facts for this case), Tone, Approved sources (the template or policy to follow). Mapped to Microsoft's Goal, Context, Source, Expectations.
- Demo 1.3 (prompt player): a five-input request for the Compensation Analyst job description.
- Task 1.3 · One job description, three ways (25 min, solo, by unit track). Files: mutla-role-information-2026.docx (one role per track), mutla-jd-template-2026.docx, mutla-jd-hr-officer-2019.docx. Deliverable: three versions (one line, structured, grounded) and one sentence on which is best and why. Finished early: turn the best version into vacancy text for a job board, keeping every duty.

**Block 4 · Grounding and checking (45 min: story 4, concepts 12, Demo 1.4 7, Task 1.4 15, debrief 7).**

- Story: Hessa's grounded job description still says "manages a team of six" and "Grade 8". Neither is in the role sheet.
- Analogy → term: an auditor ticks every line against the receipt → **source trace**: ask Copilot to show, for each duty, the line of the role sheet it came from, and to write NOT IN SOURCE when there is none.
- Unsupported claims, missing information and confident mistakes: what each looks like in a job description.
- Demo 1.4 (prompt player): the source-trace request.
- Task 1.4 · Check and save (15 min, solo). Files: the Task 1.3 job description (catch-up: mutla-catchup-jd-draft.docx), mutla-prompt-bank-template.docx. Deliverable: a corrected job description and Prompt Bank entry 1. Finished early: ask Copilot to list every assumption it made, then remove each one by adding context.

**Integration and wrap.** Two people read their Prompt Bank entry aloud. Wrap: what you built (a redacted note, a checked job description, Prompt Bank entry 1), the habit, and the hook: write one recurring task from your own unit for Day 2.

## Day 2 · Wednesday 18 November: Copilot Across HR Documents, Communication and Reporting

**Claim:** Same five inputs, five apps, one review before anything goes out. **Integration moment:** one case from your unit track turned into four reviewed outputs. **Slides: 62.**

| Time | Block | Minutes |
| --- | --- | --- |
| 09:00-09:10 | Callback quiz: three questions on Day 1 | 10 |
| 09:10-10:00 | Block 1 · Word: policies, versions and job evaluation · Task 2.1 | 50 |
| 10:00-10:40 | Block 2 · Outlook: from a long thread to a clear message · Task 2.2 | 40 |
| 10:40-10:55 | Break | 15 |
| 10:55-11:35 | Block 3 · Teams: meetings and investigation notes · Task 2.3 | 40 |
| 11:35-12:15 | Lunch and Dhuhr prayer | 40 |
| 12:15-13:00 | Block 4 · Excel: HR trackers you can check · Task 2.4 | 45 |
| 13:00-13:30 | Block 5 · PowerPoint: a briefing from a document · Task 2.5 | 30 |
| 13:30-13:40 | Break | 10 |
| 13:40-14:40 | Integration · One case, four outputs · Task 2.6 | 60 |
| 14:40-15:00 | Wrap: the Prompt Bank by task, and the hook for Day 3 | 20 |

**Block 1 · Word: policies, versions and job evaluation (50 min: story 4, concepts 14, Demo 2.1 8, checks 4, Task 2.1 15, debrief 5).**

- Story: Sunday 8 November, 09:15. The Allowances Policy v4 arrives, 14 pages. Yousef, the HR Section Head, asks Abdulaziz what changed from v3, by noon.
- Analogy → term: spot the difference between two photos → **compare versions**, with section numbers (a callback to Day 1's source trace). **Summary with section references** for long policies.
- Analogy → term: the clerk prepares the case file and the committee decides → **organize job-evaluation evidence**: Copilot sorts the evidence against Mutla's evaluation factors and leaves the grade column for the committee.
- At a high level: turning an approved job description into vacancy text and structured interview questions. Copilot never ranks or selects candidates.
- Demo 2.1 (prompt player): job-evaluation evidence into the factor table, with "Grade: for the committee".
- Task 2.1 · What changed? (15 min, pairs). Files: mutla-allowances-policy-v3.docx, mutla-allowances-policy-v4.docx (three planted changes). Deliverable: a change table with section numbers. Finished early: a three-line note to staff about the changes.

**Block 2 · Outlook: from a long thread to a clear message (40 min: felt problem 5, concepts 10, Demo 2.2 7, Task 2.2 12, debrief 6).**

- Felt problem: a 30-message thread about the new attendance rules. Who decided what? Hands up when you know.
- **Thread summary**: decisions, open questions and owners. **Tone dial**: the same facts for employees, managers and senior stakeholders (a callback to Day 1's tone input).
- Demo 2.2 (prompt player): thread to decisions, then a reply to an employee's request. The trainer also shows Copilot in Outlook on a live thread where the account allows it.
- Task 2.2 · Announce and reply (12 min, solo). File: mutla-email-thread-attendance.docx (the thread, exported). Deliverable: a staff announcement and a reply to Mubarak's request, every date and rule unchanged. Finished early: a version for line managers.

**Block 3 · Teams: meetings and investigation notes (40 min: story 4, concepts 10, Demo 2.3 7, Task 2.3 12, debrief 7).**

- Story: Khaled's staffing meeting for the new Drilling Support section ended with no actions written down. A week later, nobody had sent the headcount request.
- **Before the meeting**: agenda and background brief. **After the meeting**: recap into decisions, actions, owners and deadlines. Copilot in Teams needs the meeting transcript for a recap, so in class we use a transcript file.
- Analogy → term: a whiteboard timeline, not a verdict → **organize investigation notes**: a timeline and open questions, with no findings, no blame and no recommended action.
- Demo 2.3 (prompt player): the transcript into an actions table.
- Task 2.3 · Timeline, not verdict (12 min, solo). File: mutla-investigation-notes.docx (synthetic; it contains one manager's opinion that must not become a finding). Deliverable: a timeline and an open-questions list, checked for any conclusion. Finished early: the agenda for the follow-up meeting from mutla-meeting-transcript-staffing.docx.

**Block 4 · Excel: HR trackers you can check (45 min: story 4, concepts 12, Demo 2.4 7, check 3, Task 2.4 15, debrief 4).**

- Story: Noura reports 412 training requests for Q3. The training system's control total says 398.
- **Ask in plain language**, then **ask Copilot to show the rows or the formula** it used. **Spot-check** two figures against the control totals. A total that is too high: look for duplicates first.
- Demo 2.4 (prompt player): a question to the tracker, then "show the rows you counted".
- Task 2.4 · Two figures, checked (15 min, pairs). File: mutla-hr-trackers-q3-2026.xlsx (sheets Training, Manpower, Control totals; 14 duplicate training rows; one section's approved positions entered as 0). Deliverable: the two corrected figures and the reason for each. Finished early: ask for a chart of requests by unit and check the axis.

**Block 5 · PowerPoint: a briefing from a document (30 min: concept 8, Demo 2.5 7, Task 2.5 10, debrief 5).**

- **Document to deck**: Copilot in PowerPoint builds slides from a Word file (licensed accounts); in Copilot Chat, ask for a five-slide outline with speaker notes. Then check every number and the tone.
- Demo 2.5 (prompt player): the policy change brief into a five-slide outline.
- Task 2.5 · Five slides for the managers' meeting (10 min, solo). File: mutla-policy-change-brief.docx. Deliverable: a five-slide deck or outline, each number checked against the brief. Finished early: speaker notes in plain English.

**Integration · One case, four outputs (60 min: brief 5, Task 2.6 45, gallery 10).**

- Task 2.6 (45 min, solo, by unit track). Files: mutla-case-manpower-new-section.docx, mutla-case-compensation-allowance-update.docx, mutla-case-personnel-attendance-change.docx, mutla-case-ld-training-requests.docx, mutla-case-je-reevaluation-request.docx. Deliverable: a Word summary, an Outlook message, a meeting brief, and an Excel summary or a PowerPoint briefing, each checked against the four-point review (accuracy, confidentiality, neutrality, source alignment). Finished early: write a review request that audits your own output against the same four checks, and add it to the Prompt Bank.

**Wrap.** You built: one change table, one announcement, one timeline, two checked figures, one briefing and a case set. Hook: tomorrow your best requests become an assistant your colleagues can use.

## Day 3 · Thursday 19 November: Reusable HR Assistants and Applied Capstone

**Claim:** A request you can reuse, and a colleague can run, is worth ten you type again. **Integration moment:** the capstone workflow on a new case, passed by a colleague's peer test. **Slides: 40.**

| Time | Block | Minutes |
| --- | --- | --- |
| 09:00-09:10 | Callback quiz: three questions on Day 2 | 10 |
| 09:10-09:40 | Block 1 · Reuse before you rebuild: the Prompt Gallery · Task 3.1 | 30 |
| 09:40-10:40 | Block 2 · Build an HR assistant with Agent Builder · Task 3.2 | 60 |
| 10:40-10:55 | Break | 15 |
| 10:55-11:10 | Capstone briefing: your new case, core and extension, the self-check | 15 |
| 11:10-11:35 | Capstone build, part 1 · Task 3.3 | 25 |
| 11:35-12:15 | Lunch and Dhuhr prayer | 40 |
| 12:15-13:30 | Capstone build, part 2 · Task 3.3 | 75 |
| 13:30-13:50 | Peer test · Task 3.4 | 20 |
| 13:50-14:05 | Break | 15 |
| 14:05-14:20 | One-minute share-outs: what broke and how you fixed it | 15 |
| 14:20-14:40 | Post-MAP test, then the final survey (two QR codes) | 20 |
| 14:40-15:00 | Close and certificates | 20 |

**Block 1 · Reuse before you rebuild (30 min: story 3, concepts 8, Demo 3.1 5, Task 3.1 10, debrief 4).**

- Story: Mutla's L&D team writes the same course-nomination email five different ways every month.
- Analogy → term: a shared recipe book → **the Prompt Gallery**: Suggested prompts from Microsoft, Your Prompts (saved), and Teams (shared with your team).
- Demo 3.1 (trainer live, prompt player as the fallback): find, adapt and save one prompt.
- Task 3.1 · Save your best three (10 min, solo). File: your Prompt Bank (catch-up: mutla-catchup-prompt-bank.docx). Deliverable: three tested requests saved under Your Prompts and organized by task in the Prompt Bank. Finished early: share one with a team, if your account has one.

**Block 2 · Build an HR assistant with Agent Builder (60 min: story 3, concepts 12, Demo 3.2 8, Task 3.2 30, debrief 7).**

- Story: Fatma answers the same 20 policy questions every week, by email and by phone.
- Analogy → term: a new receptionist with an approved binder and a script that says what to answer and when to call HR → **the assistant's parts**: Instructions (role, scope, tone, what it must not answer, when to refer to HR), Knowledge (approved files), Starter prompts, and the Try it test pane.
- Steps: New agent → Configure → name, description, instructions → upload up to 20 approved files as knowledge → starter prompts → Try it → Create.
- **Test three ways**: a normal question (carry-over days), an incomplete one ("How much is my allowance?" needs a grade), and a sensitive one ("What is Ahmad's salary?" must be declined and referred).
- Demo 3.2 (prompt player): the assistant's instructions, part by part.
- Task 3.2 · Mutla HR Policy Helper (30 min, solo). Files: mutla-leave-policy-2026.docx, mutla-allowances-policy-v4.docx, mutla-attendance-rules-2026.docx, mutla-training-policy-2026.docx. Deliverable: a working assistant and a three-line test log (question, answer, pass or fix). Finished early: a fourth test where two files seem to disagree. No Agent Builder on your account: build the same instructions and files as a saved request in Copilot Chat, or pair with a neighbor.

**Capstone · A tested workflow for a new case (115 min across briefing, two build parts and the peer test).**

- Each participant gets a case from their unit track that they have not seen: mutla-capstone-je-salary.docx, mutla-capstone-compensation.docx, mutla-capstone-manpower.docx, mutla-capstone-personnel.docx, mutla-capstone-ld.docx.
- Task 3.3 · Core, for everyone (100 min, solo): complete the case by chaining at least two Copilot apps, with five-input requests grounded in the case's approved files, every output checked against the four-point review. Deliverable: the outputs and a reusable prompt set (in Word). Extension, for those who finish: connect the workflow to the morning's HR assistant, or turn it into a starter prompt.
- Task 3.4 · Peer test (20 min, pairs from different units): hand your prompt set or assistant to a colleague, who runs it on mutla-capstone-fresh-input.docx with no instructions. The owner fixes what broke. Deliverable: one fix written into the prompt set. Finished early: run a second colleague's set.
- Self-check guide (on the Day 3 lab page): five inputs present, sources attached, no personal data, every figure checked, a person decides.

**Close.** Share-outs (15 people × 1 minute), the post-MAP and survey QR codes, the habit one last time, certificates.

## Sample files

Every file belongs to Mutla Oil Company (fictional) and says so in its header. Names never change once built. Amounts are in KWD.

| File | What is in it | Used in | Planted item |
| --- | --- | --- | --- |
| mutla-leave-policy-2026.docx | Approved leave policy, numbered sections | Demo 1.1, Task 1.1, Task 3.2 | none (the source) |
| mutla-copilot-leave-answer.docx | A Copilot answer about leave | Task 1.1 | 3 errors: carry-over 30 days (policy 15), emergency leave 5 days (policy 3), annual-leave notice 7 days (policy 14) |
| mutla-case-note-unredacted.docx | A synthetic personnel case note | Task 1.2 | 6 sensitive items: 2 names, a civil ID (all zeros), a phone number, a salary, a medical reason |
| mutla-jd-hr-officer-2019.docx | An outdated job description | Block 3 felt problem, Task 1.3 | out-of-date duties and titles |
| mutla-jd-template-2026.docx | The approved job description template | Opener, Tasks 1.3, 1.4 | none |
| mutla-role-information-2026.docx | Approved role information for five roles, one per unit track | Tasks 1.3, 1.4 | none (the data) |
| mutla-catchup-jd-draft.docx | A Copilot draft with two unsupported lines | Task 1.4 catch-up | "manages a team of six" and "Grade 8" |
| mutla-prompt-bank-template.docx | The HR Prompt Bank: task, request, files, check | Tasks 1.4, 3.1, 3.3 | none |
| mutla-allowances-policy-v3.docx | Allowances policy, version 3 | Task 2.1 | none |
| mutla-allowances-policy-v4.docx | Allowances policy, version 4 | Task 2.1, Task 3.2 | 3 changes: housing allowance cap, transport eligibility grades, a new remote-site clause |
| mutla-job-evaluation-factors.docx | The five evaluation factors and their definitions | Demo 2.1, JE track | none |
| mutla-je-evidence-notes.docx | Messy evidence notes for one role | Demo 2.1 | none |
| mutla-email-thread-attendance.docx | A 30-message thread, exported | Task 2.2 | one superseded date in an early message |
| mutla-meeting-transcript-staffing.docx | A staffing meeting transcript | Demo 2.3, Task 2.3 extra | none |
| mutla-investigation-notes.docx | Synthetic investigation notes | Task 2.3 | one manager's opinion that must not become a finding |
| mutla-hr-trackers-q3-2026.xlsx | Sheets: Training, Manpower, Control totals | Demo 2.4, Task 2.4 | 14 duplicate training rows (412 vs 398); one section's approved positions entered as 0 |
| mutla-policy-change-brief.docx | A two-page brief on the attendance change | Task 2.5 | none |
| mutla-case-manpower-new-section.docx · mutla-case-compensation-allowance-update.docx · mutla-case-personnel-attendance-change.docx · mutla-case-ld-training-requests.docx · mutla-case-je-reevaluation-request.docx | One case per unit track | Task 2.6 | none |
| mutla-attendance-rules-2026.docx · mutla-training-policy-2026.docx | Two more approved policies | Task 3.2 knowledge | none |
| mutla-catchup-prompt-bank.docx | A starter Prompt Bank with eight tested requests | Catch-up for Days 2 and 3 | none |
| mutla-capstone-je-salary.docx · mutla-capstone-compensation.docx · mutla-capstone-manpower.docx · mutla-capstone-personnel.docx · mutla-capstone-ld.docx | New capstone cases, one per track | Task 3.3 | none |
| mutla-capstone-fresh-input.docx | Fresh inputs for the peer test, one per track | Task 3.4 | none |

31 files in total, all generated by the kit and served from the site.

## Take-aways

**Cheat sheet (one page, four parts).**

1. The five inputs: Instructions, Context, Data, Tone, Approved sources, each with an HR example.
2. Six HR requests that work: job description from approved data, policy version compare, warmer announcement with facts kept, meeting recap into actions, tracker figure with the rows shown, investigation timeline with no findings.
3. The four-point review: accuracy, confidentiality, neutrality, source alignment.
4. Where Copilot sits: Copilot Chat, Copilot in the apps, the Prompt Gallery, Agent Builder, and how to read your license label.

**Safe-use card.** Green: fictional data and your own drafting. Amber: internal HR information in your company's approved Copilot account, minimum data, no names. Red: never in a prompt: civil IDs, named salaries, medical details, case details that name people, personal files. Below the colors: decisions that stay with authorized HR staff (grades, pay, ratings, discipline, selection), and "your company's AI and data policy comes first".

**Take-home guide.** First week: one five-input request a day on a green task, checked with the four-point review. First month: one assistant or prompt set for a recurring task in your unit, tested by a colleague, saved in the Prompt Gallery.

**Daily prompt sheets** (one per day) with every request in teaching order and a COPY button, and **one browser lab per day**: Day 1 check a Copilot answer step by step, Day 2 spot-check the HR tracker, Day 3 the capstone self-check.

## Assessment

**MAP test, PRE (Day 1, 09:10) and POST (Day 3, 14:20).** Same questions both times, 10 minutes, not graded, no "I don't know" option. Part 1: the six outcomes as 1 to 5 confidence ratings. Part 2: 14 knowledge questions (Day 1: 5, Day 2: 5, Day 3: 4). Bilingual English and Arabic in the portal only. Name and work email to match the two sittings, plus "Your company" (open workshop).

| # | Day | Question | a | b | c | d | Key |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | Copilot tells Fatma that staff can carry over 30 days of annual leave. Mutla's leave policy says 15. Why can this happen? | Copilot read an older policy on the internet | It predicts likely words, and nothing checked the policy | Copilot always rounds numbers up to be safe | The policy file was too long for Copilot to read in full | b |
| 2 | 1 | Hessa uses Copilot with a Microsoft 365 Copilot license. Which files can it use to answer her? | Every file on the company SharePoint, including restricted HR folders | Only the files she uploads in this chat | Only files, emails and chats she already has permission to open | Public websites only, never company files | c |
| 3 | 1 | Which task stays with authorized HR staff and is not handed to Copilot? | Drafting a job description from approved role information | Summarizing a long leave policy with section numbers | Deciding the grade of a re-evaluated job | Changing the tone of a staff announcement | c |
| 4 | 1 | Abdulaziz wants Copilot to tidy a salary exception memo that names two employees. What does he do first? | Replace names, civil IDs and salary figures before he uploads it | Ask Copilot, in the prompt, to keep the whole memo strictly confidential | Open a new chat so that the memo stays private | Shorten the memo so that Copilot reads it faster | a |
| 5 | 1 | Copilot's job description lists duties that are not in Mutla's role information. Which input was missing? | A friendlier tone | Context about who will read the job description | A longer instruction | Data: the approved role information | d |
| 6 | 2 | Abdulaziz must report what changed between v3 and v4 of the allowances policy. Which request is best? | "Is version 4 better than version 3?" | "List every change between v3 and v4, with its section number." | "Summarize version 4 of the allowances policy." | "Rewrite version 4 so that it uses the same wording as version 3." | b |
| 7 | 2 | Copilot organizes job-evaluation evidence against the factors, then adds "Suggested grade: 9". What does Hessa do? | Remove the grade and send the evidence to the evaluation committee | Keep the grade, because Copilot followed every approved evaluation factor | Ask Copilot to explain the grade, then keep it | Send the grade to the employee to confirm it | a |
| 8 | 2 | Fatma needs a warmer version of the attendance announcement. Which request keeps the facts? | "Make this announcement much friendlier, warmer and more exciting for staff." | "Rewrite this announcement for all staff." | "Make it warmer; keep every date, time and rule as written." | "Improve this announcement before it goes out." | c |
| 9 | 2 | Khaled asks Copilot to work on synthetic investigation notes. Which output is acceptable? | A finding about which employee was at fault | A timeline of events and a list of open questions | A recommended disciplinary action for the manager | A judgment about which witness is telling the truth | b |
| 10 | 2 | Copilot counts 412 training requests in Q3. The training system's control total is 398. What does Noura do first? | Ask Copilot to round the total to the nearest ten | Use Copilot's number, because it read every row | Report the average of the two numbers | Look for duplicate rows in the tracker | d |
| 11 | 3 | Mutla's L&D team wants one shared set of tested prompts. Where in Copilot can they save and share them? | The Prompt Gallery | The chat history of each person | The starter prompts of one agent | The signature in Outlook | a |
| 12 | 3 | In Agent Builder, which part tells your HR assistant what it must not answer and when to refer people to HR? | Knowledge | Instructions | Starter prompts | Description | b |
| 13 | 3 | A tester asks the HR assistant: "What is Ahmad's salary?" What is the right response? | It answers from the allowances policy file | It estimates the salary from Ahmad's grade | It asks for Ahmad's employee number first | It declines and refers the person to HR | d |
| 14 | 3 | A colleague runs your prompt set on a new case with no instructions from you, and it fails. What does this tell you? | Your colleague did not use the prompt set the way you meant | Copilot cannot be trusted for HR work | The prompt set depends on something only you know | The new case was too hard to test fairly | c |

**Answer key:** 1 b · 2 c · 3 c · 4 a · 5 d · 6 b · 7 a · 8 c · 9 b · 10 d · 11 a · 12 b · 13 d · 14 c. The key goes only in the portal description and the trainer pages.

**Final satisfaction survey** (Day 3, after the POST): the full open-workshop form on the 6-point agreement scale, with "Your company", the hands-on item (job descriptions, policy comparisons, the HR tracker, the HR assistant and the capstone), the six "I can" items, the two Copilot habit items (check its numbers; know what never goes in), the trainer items, "recommend to a colleague" plus the 0 to 10 NPS item, and three open comments.

**No scored project.** The capstone has a self-check and a peer test, as in Mastering Copilot.

## Trainer material (under /staff, password locked)

- **Lesson plan:** every day's run of show with the minutes inside each block, the tasks, files and breaks.
- **Decks with speaker notes** (press N): what to do or ask, the expected answer, a line for a silent room, and a fallback for every live step.
- **Answer keys per day:** every task and quick check; the MAP key on Day 3. **Lab keys** for the three browser labs.
- **Demo runbooks per day** and a **backup result** for every live Copilot step, so a slow or limited account never stops the room.
- **Facilitator kit:** pre-flight (license labels, Agent Builder on, a test file upload, Teams not needed live), room setup, the fail plan (Copilot slow, daily limit reached, no Agent Builder, no in-app Copilot, no internet), MAP links with QR codes, and the scoring-free capstone guide.

## Coverage

Every topic and outcome in the outline maps to a block and a task. No gaps.

| Outline item | Where it is taught | Practiced in |
| --- | --- | --- |
| Starting point and setup check | Day 1 · Welcome, pre-MAP | Sign-in check, pre-MAP |
| How Copilot produces an answer; what it can see | Day 1 · Block 1 | Task 1.1 |
| Rules: what stays with people, what never goes in a prompt | Day 1 · Block 2 | Demo 1.2 sort, Task 1.2 |
| The five inputs (instructions, context, data, tone, approved sources) | Day 1 · Block 3 | Task 1.3 |
| Grounding and checking; unsupported claims | Day 1 · Block 4 | Task 1.4 |
| Job descriptions | Day 1 · Opener, Blocks 3 and 4 | Tasks 1.3, 1.4 |
| Job evaluation evidence, no grade | Day 2 · Block 1 | Demo 2.1, Task 2.6 (JE track) |
| Policies, long documents, version compare | Day 2 · Block 1 | Task 2.1 |
| Recruitment, high level | Day 2 · Block 1 | Task 1.3 extra |
| Employee communication and tone | Day 2 · Block 2 | Task 2.2 |
| Meetings: agenda, brief, recap | Day 2 · Block 3 | Demo 2.3, Task 2.3 extra |
| Investigations: timeline, no conclusions | Day 2 · Block 3 | Task 2.3 |
| Manpower, compensation and training trackers in Excel | Day 2 · Block 4 | Task 2.4 |
| Briefings in PowerPoint; reporting | Day 2 · Block 5 | Task 2.5 |
| One case, four outputs; four-point review | Day 2 · Integration | Task 2.6 |
| Prompt Gallery and Prompt Bank | Day 3 · Block 1 | Task 3.1 |
| HR assistant in Agent Builder, tested three ways | Day 3 · Block 2 | Task 3.2 |
| Capstone on a new case, core and extension | Day 3 · Capstone | Task 3.3 |
| Peer test by a colleague from another unit | Day 3 · Capstone | Task 3.4 |
| Repeat skills check, survey, certificates | Day 3 · Close | Post-MAP, survey |
| Five unit tracks | All days | Tasks 1.3, 2.6, 3.3 |
| Extra challenge every day | Every task | Finished-early extras |

## Decisions

1. **Cohort and dates.** The portal's AIHR-Nov/Nov-26 (10 to 12 Nov) is on hold; its note says the approved HR runs are 17 to 19 Nov and 20 to 24 Dec. This build uses AIFHR-Nov/Nov-26: 17 to 19 Nov, 09:00 to 15:00, CODED Alsharekh, capacity 25.
2. **Open workshop, CODED brand only.** The cohort is a public, priced product run for KOC demand, and no KOC logo is on file. The surveys ask "Your company" and include the NPS item.
3. **Fictional company: Mutla Oil Company.** An oil and gas twin with five HR units, Kuwaiti names, KWD amounts. KOC's name never appears on a file.
4. **Five unit tracks.** Job Evaluation and Salary Scaling share one track, as their work overlaps.
5. **Copilot Chat with file upload carries every task.** It works on every license level ([Microsoft: Copilot Chat with or without a license](https://support.microsoft.com/en-au/topic/what-s-the-difference-between-using-copilot-chat-with-or-without-a-microsoft-365-copilot-license-5810b659-fbe0-48ee-9fe6-d731fe86cdeb)). Copilot inside Word, Excel, PowerPoint and Teams is demonstrated, and used by anyone whose label says Premium. This avoids the Burgan problem of uneven licenses and daily limits.
6. **Teams recap uses a transcript file.** Copilot recaps in Teams need the meeting transcript ([Microsoft: Copilot in Teams meetings](https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1)), so no live meeting is needed in class. The Outlook thread is an exported file for the same reason.
7. **Agent Builder facts** taught as on Microsoft's pages today: New agent, the Configure tab, instructions up to 8,000 characters, up to 20 uploaded files as knowledge, the Try it pane ([build agents](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents), [add knowledge](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge)). Agents are limited on Copilot Chat (Basic), so every participant has a fallback.
8. **Prompt Gallery** names as on Microsoft's page: Suggested, Your Prompts, Teams ([Prompt Gallery](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-prompt-gallery)).
9. **The five inputs** are the outline's own words, mapped to Microsoft's Goal, Context, Source, Expectations so participants recognize both.
10. **Real case:** Samsung, 2023 ([The Register](https://www.theregister.com/2023/04/06/samsung_reportedly_leaked_its_own)). No Kuwaiti regulation is quoted; the slides say "your company's AI and data policy comes first".
11. **Timing:** Dhuhr is about 11:35 in Kuwait in mid-November, so each day has a 40-minute lunch and Dhuhr break at 11:35. Breaks sit at reset points; no break slides (the cup button stays).
12. **No scored project, no printable PDFs, no videos:** the outline asks for none.
13. **Trainer:** Aya. The portal lists Ghareeb Thiab as lead instructor; worth updating the cohort.
14. **Surveys:** three drafts in a new folder "AI Fundamentals for HR (Nov 26)", linked to AIFHR-Nov/Nov-26. Your approval of this page is the confirmation for creating and updating those three drafts. They are published only after QA passes.
15. **Slack:** I give you the team message to paste rather than posting it.
16. **Recruitment** stays at one Day 2 block item and one extra, as the outline asks.

## Missing facts

Three things only you can settle; they are in the question box with a default each.

1. **Title:** "AI Fundamentals for HR" (what participants registered for in the portal) or "AI Essentials for Modern HR" (the outline).
2. **Brand:** CODED only (open workshop), or the CODED and KOC mix (you would attach KOC's logo).
3. **GitHub repo:** this session cannot create repos. Please create an empty private repo named **coded-ai-hr** under your GitHub account (aya-alsakkaf), so the push at the end is not blocked.
