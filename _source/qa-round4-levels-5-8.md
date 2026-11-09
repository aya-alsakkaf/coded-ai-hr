# AI Fundamentals for HR · Independent QA, Levels 5 to 8 · Round 4

Scores: Content coherence 9.25/10 · Tasks and demos 9.5/10 · MAP tests 7.25/10 · Final survey 9.75/10 · Language and data safety 9.75/10
(minus 3 per Blocking, 1 per Concerning, 0.25 per Nit. Blocking: none. Concerning: 2. Nit: 10. Weighted over these five dimensions (20/10/10/5/10): 9.07/10. FAIL: MAP tests is below 9.0.)
Scores count every open finding: the new ones and the round 3 items that are not fully fixed.

Audited on 9 November 2026 against the kit as built at 18:51 (data.py 18:50, content_demos.py 18:50, content.py 18:51, build_deck.py 18:51, public/ 18:51:22, kit-pages records 18:51:23) and the portal drafts as read today (PRE updated 16:08 UTC, POST 16:12 UTC, final 13:59 UTC).

## Round 3 findings

Content coherence
1. Concerning · C-1, b1t3 and the Day 2 "Basic users" notes: FIXED. b1t3 now says "On Copilot Chat (Basic), it uses the web, the files you upload and Outlook. M365 Copilot (Basic) adds Copilot in Word, Excel and PowerPoint." b1lic agrees. The c4t1 and c5t1 notes say "Copilot Chat (Basic) users". This matches Microsoft's license page (April 2026).
2. Nit · C-2, hub "15 prompt demos": FIXED. content_demos.py sets HUB["stats"] without the card sort; the hub shows "14 prompt demos".
3. Nit · C-3, "the prompts icon": FIXED. d31 setup and the e1t1 note say "the More options (...) button or a prompt pill below the message box". Microsoft says "the '...' button".
4. Nit · C-4, Day 3 page "100:00 on the clock": FIXED as recorded. The title is now "A tested workflow for a new case, in two parts", the first step gives both parts, and CLAUDE.md Decision 19 records that the engine prints the clock line from the total minutes. Not counted.
5. Nit · C-5, c3chk2 position: FIXED. c3chk2 now follows c3chk1, before c3board.

Tasks and demos
6. Nit · T-1, file lists: FIXED. t26.files adds the attendance rules, training policy, template, factors, v4 and brief (every "Approved files to attach" line in the five case files is now on the card). t33.files has the training policy. t14.files has the template. The lesson-plan file map lists Task 2.6 and Task 3.3 for these files.
7. Nit · T-2, "four files": FIXED. The t32 fallback, the facilitator kit fail plan and the Day 3 runbook all say "the five policy files".
8. Nit · T-3, AGENT_TESTS[1] pass mark: FIXED. "Pass, if it asks for the grade, then gives both rules".
9. Nit · T-4, Demo 2.2 has no reply to an employee: PARTLY FIXED. d22 now has a second prompt, "Reply to a staff question", on the prompt sheet and the runbook. But the player (slide c2pp) shows only the thread request, and d22 "expected" and "backup" have nothing for the reply. Open as Nit T-1 below.

MAP tests
10. Concerning · M-1, q_8 recalls c2chk, c2t2 and the cheat sheet: PARTLY FIXED. c2chk is rewritten (the line-manager version) and wrong option a is new. The stem and key still recall public content. Open as Concerning M-2 below.
11. Concerning · M-2, q_6 and q_7 restate Day 2 Block 1: FIXED. q_6 is now about the 2025 and 2026 training policies, q_7 about a Payroll Officer line "This job should move up one grade". c1chk1 (vacancy text) and c1chk2 (the parking note) are rewritten. A new parallel with e0chk1 is listed as Nit M-4.
12. Nit · M-3, parallel distractors in b1chk1, b1chk2, b2chk1: PARTLY FIXED. b1chk2 A is now "Yes, if his manager has access to the folder" and b2chk1 has "Booking the training room" and "Checking course dates". b1chk1 still has "The employee asked the question the wrong way" (plus "The employee's question was too short"), the same idea as q_1 c. Open as Nit M-3 below.
13. Nit · M-4, q_13 copies the EMP-4417 question: FIXED. q_13 asks "Which person in my team took the most sick days this year?". No sample file, slide or sheet asks this (I searched all 31 files).
14. Nit · M-5, quick-check option lengths: FIXED. Of the 28 checks, the right answer is the longest in 5, the shortest in 9 and the middle in 14. Letters A 9, B 9, C 10.

Final survey
15. Nit · F-1, build log and QA report: FIXED. build-log.txt ends with "patched: pre 24 · post 24 · final 25 questions" and QA-REPORT.md records the counts. The "survey final 22 questions" line comes from surveys.py before the patch, and validate_site.py checks only the slug length of the payloads, so a second validator run changes nothing.

Language and data safety
16. Nit · L-1, Demo 2.3b periods: FIXED ("... is not signed (source: the shift log).").
17. Nit · L-2, three figurative lines: FIXED. e1t1 "a tested request saved for everyone", b3one "A fast answer with no inputs needs more fixing.", c3story "No written actions means no follow-up."
18. Nit · L-3, Task 1.4 "Look for: Look for" and the Task 2.6 extra: FIXED (t14 hint "A team size and a grade that the role information does not give."; t26 stretch "without copying the Review request on the prompt sheet"). The same slip is now on Task 2.1 (Nit L-1 below).

## New findings

### Content coherence (Level 5) · 3 Nit

Nit · C-1 · content.py SEGMENTS (staff lesson plan and runbooks, run of show) · Three blocks give minutes in an order the deck does not follow:
- Day 1 Block 2: "10:55, 14, Three groups, the safe-use card, redact" then "11:09, 8, Demo 1.2 card sort". In the deck the redact concept (b2t2, b2moves, b2chk2) comes after the sort (b2sort).
- Day 2 Block 1: "09:14, 11, Compare versions, evidence with no grade, recruitment" then "09:25, Demo 2.1". In the deck recruitment (c1rec, c1chk1) comes after Demo 2.1 (c1pp, c1chk2).
- Day 2 Block 3: "10:59, 8, Before and after a meeting; timeline, not verdict" then "11:07, Demo 2.3". In the deck the timeline concept (c3board, c3t2) comes after Demo 2.3 (c3pp, c3chk1, c3chk2).
- A trainer on the clock thinks the concept is done when the deck has not reached it.
- Fix (totals unchanged):
  - Day 1 Block 2: ("10:55", 9, "Three groups, the safe-use card"), ("11:04", 8, "Demo 1.2 card sort"), ("11:12", 5, "Redact in four moves"), ("11:17", 3, "Demo 1.2b: redact, then ask"), then Task 1.2 and the debrief as now.
  - Day 2 Block 1: ("09:14", 8, "Compare versions, evidence with no grade"), ("09:22", 6, "Demo 2.1"), ("09:28", 7, "Quick checks and recruitment"), ("09:35", 5, "Demo 2.1b"), then Task 2.1 and the debrief as now.
  - Day 2 Block 3: ("10:59", 4, "Before and after a meeting"), ("11:03", 6, "Demo 2.3"), ("11:09", 4, "Quick checks; timeline, not verdict"), ("11:13", 4, "Demo 2.3b"), then Task 2.3 and the debrief as now.

Nit · C-2 · day-1 deck b3story and data.py OLD_JD · The slide says "update the 2019 job description for the Personnel Clerk role", and the file content says "Position: Personnel Clerk". The file is named mutla-jd-hr-officer-2019.docx, and the handoff calls it "the 2019 HR officer job description". A participant asked to open "the HR officer file" finds a Personnel Clerk.
- Fix: set OLD_JD["title"] = "HR Officer" in data.py (the file name stays; the slide and the file text follow).

Nit · C-3 · day-3 deck e3story · "You have a new case, Copilot, and two hours." The build time is 100 minutes (25 + 75), as on the Task 3.3 card and slides e3task and e4build.
- Fix: "You have a new case, Copilot, and 100 minutes."

### Tasks and demos (Level 6) · 2 Nit

Nit · T-1 · content_demos.py d22 (Demo 2.2, slide c2pp, Day 2 runbook and backup page) · Round 3 T-4 leftover. The new "Reply to a staff question" prompt has no expected result and no backup. The trainer has nothing to check the live reply against. The answer is not obvious either: the thread gives the new core hours (8:00 to 13:00, message 24) but never states the current hours, so a correct reply must say that.
- Fix: add to d22 expected: "Reply: from Tuesday 1 December 2026, core hours are 8:00 to 13:00 (message 24). The thread does not give the current hours, so the reply says so and refers the person to Personnel and Administration." Add the same text as a backup ("h", "Typical reply to a staff question") block.

Nit · T-2 · data.py AGENT_TESTS[0] (public slide e2tests, Demo 3.2 player e2pp, prompt sheet Day 3) · The "Pass if" column for the Normal test reads only "Pass". It tells the participant nothing about what a pass looks like, while the other two rows give a condition.
- Fix: AGENT_TESTS[0][3] = "Pass, if it gives the rule and cites section 4".

### MAP tests (Level 7) · 2 Concerning, 3 Nit

Re-derivation from the slides and staff notes of each day:
- 1 b (b1t1, b1t2, b1llm; see M-1: a is also defensible)
- 2 c (b1scene, b1t3)
- 3 c (b2groups, b2t1)
- 4 a (b2t2, b2moves, b2chk2, Demo 1.2b)
- 5 d (b3five, b3t1 "Without facts, it invents details.")
- 6 b (c1t1, c1ever)
- 7 a (c1t2 "If Copilot suggests a grade, delete it.", c1pp control line)
- 8 c (c2t2)
- 9 b (c3t2)
- 10 d (c4t2 "Too high: look for duplicates.")
- 11 a (e1story, e1t1)
- 12 b (e2t1)
- 13 d (e2never, Demo 3.2 "Must not answer" and "Refer to HR", e2tests)
- 14 c (e4rule, e4fixes, Task 3.4 note)

All 14 agree with the portal key "1 b · 2 c · 3 c · 4 a · 5 d · 6 b · 7 a · 8 c · 9 b · 10 d · 11 a · 12 b · 13 d · 14 c". No Blocking finding. The derivation was not fully blind: content.py, which the brief asked me to read, holds the answer indexes.

Concerning · M-1 · PRE/POST q_1, option a (content.py MAP[0], SURVEY["map_ar"][0]) · Option a, "Copilot read an older policy on the internet", is defensible under the deck's own words. Public slide b1t1 teaches: "Without the source, it guesses or searches the web, and nothing checks it against Mutla's policy." So a participant who learned Day 1 can argue that a web search found an older policy that says 5 days. The stem asks "Why can this happen?", which invites any possible cause. The item then has two defensible answers.
- Fix: same letter b. Replace option a with a cause the deck shows is false, for example "Copilot copied the number from another employee's chat" (AR: "نسخ Copilot الرقم من محادثة موظف آخر"). b1scene and b1t3 teach that Copilot cannot open what you cannot open. Update both drafts.

Concerning · M-2 · PRE/POST q_8 (content.py MAP[7], SURVEY["map_ar"][7]) · Round 3 M-1 leftover. The POST still measures recall of Day 2 Block 2:
- The stem is the Task 2.2 and c2story situation: Fatma, the attendance announcement, a warmer version.
- The key c, "Use a warmer tone, but change no date, time or rule.", restates the strong request printed on c2t2, the cheat sheet (Part 2, "Warmer, same facts") and the t22 prompt: "Make it warmer; keep every date, time and rule as written."
- The stem's own words, "Which request keeps the facts?", point to the only option that names facts, so a PRE taker can answer by test-wiseness.
- Fix: same letter c, a new actor and document, no "keeps the facts" cue, and a key not worded like c2t2. For example: "Hessa asks Copilot to make the Eid holiday notice warmer. The new version says the office reopens 'after the holiday', with no date. Which request would have stopped this?"
  - a "Make it warmer and add a greeting for the holiday."
  - b "Rewrite it in a warmer tone for all staff."
  - c "Make it sound warmer. Copy the reopening day and time from the original."
  - d "Make it warmer and shorter, so that staff read it."
  - Mirror it in SURVEY["map_ar"][7] and update both drafts. Keep c from being the longest option in the Arabic text.

Nit · M-3 · build_deck.py b1chk1 vs PRE/POST q_1 · Round 3 M-3 leftover. b1chk1 ("Copilot tells an employee that Hajj leave is 30 days. Mutla's policy says 21. What does this show?") has the same stem shape as q_1 and two distractors about the question's wording ("The employee's question was too short", "The employee asked the question the wrong way"). q_1 c is "The question did not say which kind of leave". The right answers match too ("It sounds sure, but nothing checked it" / "nothing checked the policy").
- Fix: change the b1chk1 distractors to other mistakes, for example "Copilot was trained on an older Mutla policy" and "Copilot always rounds leave days up".

Nit · M-4 · PRE/POST q_7 vs public day-3 check e0chk1 and sample file mutla-capstone-fresh-input.docx · Two overlaps:
- e0chk1, shown at 09:00 on the day of the POST: "A draft for the Job Evaluation committee includes a pay figure that Copilot worked out. What do you do?". Its right answer is "Remove it", and its distractor "Keep it if the math is right and the factors fit" is the same idea as q_7 b "Keep the line, because Copilot followed every approved evaluation factor".
- The q_7 job, Payroll Officer, is the role sheet in the fresh-input file that Job Evaluation participants work on at 13:30, just before the POST.
- Fix: in build_deck.py, change the e0chk1 distractor to another mistake (for example "Move it to a note at the end of the draft"). In content.py MAP[6] and map_ar[6], replace "Payroll Officer" with a job that is in no file, for example "Safety Officer" ("مسؤول سلامة"). Same letter a.

Nit · M-5 · PRE/POST q_11 vs public day-3 story e1story · The stem paraphrases the story. e1story: "Mutla's L&D team sends course nominations every month. Five people write the same email five different ways". q_11: "Noura's team rewrites the same course-summary request from memory, and every version is different." Same unit (L&D), same problem, and the key is the story's headline "Write it once. Test it. Share it."
- Fix: same letter a, a different unit and task. For example: "Three Personnel officers each type their own request for the monthly attendance exceptions summary, and the results differ. What should they do?" Mirror it in map_ar[10].

Checks that pass:
- Portal PRE 57d00a52 and POST 310d6449 equal _source/surveys/pre.json and post.json: question ids, order, EN and AR labels, options, sections, section descriptions, description and key, branding title and subtitle.
- PRE and POST differ only in name, slug, branding title and the sitting line of the description (checked field by field on the kit payloads).
- Day split 5/5/4. 4 options each, one key, all 20 rated and knowledge items required, no "I don't know", no pass rule. Key letters a 3, b 4, c 4, d 3.
- The right answer is strictly the longest in 0 of 14 in English (q_1 ties) and 2 of 14 in Arabic (q_8, q_13). No "all of the above".
- Every label, option, section title and section description is filled in English and Arabic. No em or en dash in the payloads.
- Fields: audience teacher_student, isAnonymous false, displayMode sectioned, cohort AIFHR-Nov/Nov-26, folder a8f8146d, CODED logo top-center and left, clientName null.
- The key is in the portal descriptions and on staff pages only (Day 3 answer key, facilitator kit). No public page, deck or sample file carries it.
- Model surveys: KIBS Cloud PRE b379cde6 and Al Rawdatian PRE b5be0543 (the newest MAP tests in the list today) return not_found_or_denied. The structure (sections s_1 to s_5, intro statement, name, work email, company, 1 to 5 confidence anchors, fictional-company line) is unchanged since round 3 matched it to RSM PRE 763ba655. The portal intro and closing screens keep the defaults (Decision 8).

### Final survey (Level 8, structure) · 1 Nit

Nit · F-1 · portal b84d43f1 and final.json, statement "intro" (patch.py) · The intro says "For each statement, tap a number from 1 to 6." q_nps uses 0 to 10. A participant meets a different scale with no warning.
- Fix: in patch.py, add to the intro label "The last recommend question uses 0 to 10." (AR: "سؤال التوصية الأخير من 0 إلى 10."). Update the draft.

Checks that pass:
- Portal b84d43f1 equals final.json: 25 questions, unique ids, in this order: intro, q_company, q_2, q_1, q_3, q_9, q_materials, q_pace, q_logistics, q_4, q_5, q_can3 to q_can6, q_ai, q_safe, q_10, q_6, q_7, q_11, q_nps, q_12, q_13, q_8.
- Rated items are 1 to 6 with "Strongly disagree" and "Strongly agree" anchors, all required. q_nps is 0 to 10. Open text is optional. q_company is optional. collectName and collectEmail are false, and the progress bar is on.
- Sections: s_1 "Your feedback", s_learn "What you can do now", s_team "Education Team", s_comments "Comments", EN and AR.
- "workshop" and ورشة العمل with feminine agreement throughout ("لبّت ورشة العمل", "بورشة العمل هذه"). The slug has 55 characters.
- Fit: the hands-on item names job descriptions, policy comparisons, the HR tracker, the HR assistant and the capstone. q_logistics names Microsoft Copilot. q_pace and q_12 say 3 days. q_4, q_5 and q_can3 to q_can6 equal the six OUTCOMES word for word.

### Language and data safety (Level 8) · 1 Nit

Nit · L-1 · coded-ai-hr-day-2.html and prompt sheet Day 2, Task 2.1 (content_demos.py t21 hint) · The card reads "Look for: Look at the housing cap, the transport grades and one new section." The prompt sheet reads "What to look for Look at ...". The same slip was fixed on Task 1.4 in round 3.
- Fix: t21 hint "The housing cap, the transport grades and one new section."

Checks that pass:
- No em or en dash on any participant page, staff page (text), public slide or survey payload. No "simply", "easily", "obviously", "e.g." or "i.e." on participant pages or slides. The one "just" is on the staff Day 3 answer key ("just over 6 months").
- No sentence over 30 words on participant pages, slides or surveys outside navigation lists. American spelling (no organise, colour, licence, programme or similar).
- All 30 .docx files carry the fictional header ("Mutla Oil Company (fictional) · training file made by CODED") and the fictional footer. The workbook carries the fictional line on its Notes sheet.
- Personal data: civil ID 000000000000, phone +965 0000 0000. Capstone trainers are labels (Trainer A to D). The planted names (Jassim Al-Fadhli, Saud) are fictional and are part of the key.
- No KOC on any page, file or survey (the only byte matches are inside base64 font data in the decks). No credentials: the only "password" strings are the staff-page note and the Wi-Fi line in the facilitator kit.
- Public pages carry no key string: the MAP key, the 14 duplicate request IDs, "37", EMP-4417, the insult and the Mubarak answer are only under /staff. The Day 2 lab answers are hashed (data-h), not in plain text.

## What I checked and found clean

Kit fidelity
- public/ (18:51:22) was built after the last kit edit (build_deck.py 18:51:21), and build-log.txt records "39 pages checked · PROBLEMS: 0" for that build. I ran validate_site.py again on a copy of the repo (outside the repo, nothing changed in it) with the patched survey payloads in place: "39 pages checked · PROBLEMS: 0". Slides and speaker notes equal the kit records word for word.

Outline coverage and handoff fidelity
- Every outline topic, hands-on, extra challenge and close maps to a block, slides and a task: Day 1 (setup check, prediction and what Copilot sees, three groups and redaction, the five inputs with the by-hand felt problem, grounding, Prompt Bank entry 1, assumptions extra, recurring-task hook). Day 2 (Word compare and evidence, recruitment high level, Outlook thread and tone, Teams agenda, recap and investigation, Excel figure checks, PowerPoint briefing, one case four outputs, review-request extra). Day 3 (Prompt Gallery, Agent Builder with three tests and fixing, capstone core, extension and peer test, second-scenario extra, share-outs, POST, survey, certificates).
- Differences from the handoff are all recorded: Demos 1.2b, 2.1b, 2.3b (Decision 15), the sort at 8 minutes (13), v3 in the assistant (17), the 25 + 75 split (14, 19), MAP re-stems with the same letters (12, 17, 19).

Minutes
- SEGMENTS add up and start on time in every block: Day 1 60 / 50 / 80 / 45; Day 2 50 / 40 / 40 / 45 / 30 / 60; Day 3 30 / 60. Each agenda day is contiguous and totals 360 minutes.
- Timers: b3timer 8, b5go 15, c6gallery 10, e3task 25, e4build 75, e5share 15, MAP 10. Every other task timer equals its minutes (12, 12, 25, 15, 15, 12, 12, 15, 10, 45, 10, 30, 20). Slide counts 61 / 64 / 40, equal to SLIDES and within 10% of the handoff (60 / 62 / 40).

Numbers (recomputed from the files)
- Tracker workbook: Training sheet 412 rows, 398 unique request IDs, 14 identical duplicates. Control totals 398 and the unit split. Manpower: Drilling Support 0 / 0 / 0 in the file, 12 / 0 / 12 on the Control totals sheet; 25 vacancies in the file, 37 true (286 approved, 249 filled). Demo 2.4 player rows (43, 55, 46, 54) equal the export counts.
- Leave answer file: carry-over 30 vs 15, emergency 5 vs 3, notice 7 vs 14; the two correct lines (30 days a year, Hajj 21) are in the key.
- Allowances: housing KWD 250 to 300, transport grades 1 to 6 to 1 to 8, new section 5 (20% for more than 15 days), renumbered 6 and 7, dates 1 January 2025 and 1 January 2027. Compensation case 140 × 50 = 7,000 a month, 84,000 a year.
- Capstone and fresh-input keys recompute from data.py: vacancy ages at 31 October and 15 November (Production Engineer exactly 6 months and 1 day on 15 November), leave exceptions on the 15-day cap (EMP-1502 edge), the eight allowance answers.
- Thread: message 3 proposes 15 November, message 24 (Monday 9 November) approves 1 December, message 29 is Mubarak's 6:00 request, traps at messages 11 and 12 (overtime) and 18 (correction). Transcript: four actions and one open question, read back at 10:19 to 10:21, close at 10:23 on Monday 16 November.
- Story and file weekdays are right for 2026 (1, 8, 15, 22 November are Sundays; 16 November Monday; 26 November and 10 December Thursdays; 1 December Tuesday; 30 November Monday).
- MAP q_10 uses MAP_Q10 (431 vs 415); q_1 uses LEAVE["sick_cert"] = 2.

Tasks and demos
- All 14 tasks have files, minutes, solo or pairs, one deliverable, a participant hint, a staff answer and a finished-early extra. Each demo uses the same file and request shape as the task after it.
- Every planted item is findable and in a key: 3 leave errors, 6 redaction items, 2 unsupported JD lines, 3 policy changes, 2 thread traps, the investigation opinion, 14 duplicates and the 0 approved, the capstone traps (EMP-4417, the insult, the no-Excel rating, Saud, the edges, last month's 8 open).
- Keys accept the defensible alternatives: other redaction labels and general dates (t12), the version date and renumbering (t21), 25 with the 0 flagged (t24), the missing carry-over deadline (t11), either list for the 6-month edge (Manpower).

Product facts (Microsoft pages, read 9 November 2026)
- What Copilot license do I have. Labels Copilot Chat (Basic), M365 Copilot (Basic), M365 Copilot (Premium) under your name at the bottom of m365.cloud.microsoft. Copilot Chat (Basic) has no Copilot in Word, Excel, PowerPoint or OneNote; M365 Copilot (Basic) has standard access; all subscribers have Copilot in Outlook. Updated April 2026: https://support.microsoft.com/en-US/Microsoft-365-Copilot/what-copilot-license-do-i-have
- Copilot Chat with or without a license. Web data reasoning in both; work data "Limited (uploaded files)" without a license; apps "Depends on your label"; agents "Limited (no advanced agents)". Updated 6 Nov 2026: https://support.microsoft.com/en-au/topic/what-s-the-difference-between-using-copilot-chat-with-or-without-a-microsoft-365-copilot-license-5810b659-fbe0-48ee-9fe6-d731fe86cdeb
- Create a new presentation with Copilot in PowerPoint. Copilot icon at the bottom right; Word Styles tips; under 24 MB. Updated October 2026: https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d
- Add a slide from a file with Copilot in PowerPoint. "Select Reference a file or type / to choose the file" (supports the c5t1 note). Updated 15 Sep 2026: https://support.microsoft.com/en-au/topic/add-a-slide-from-a-file-with-copilot-in-powerpoint-9034b581-38df-46be-a725-986cbbd4b5d4
- Copilot in Teams meetings. Questions after the meeting need a transcript; "During and after the meeting" requires transcription; intelligent recap with Teams Premium or a Copilot license. Updated 24 Sep 2026: https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
- Summarize an email thread with Copilot in Outlook. "Summary by Copilot" at the top of the thread, "Summarize" in some versions. Updated 18 Sep 2026: https://support.microsoft.com/office/summarize-an-email-thread-with-copilot-in-outlook-a79873f2-396b-46dc-b852-7fe5947ab640
- Frequently asked questions about Copilot in Excel. Save as Excel Workbook (.xlsx); M365 Copilot (Basic) has standard access. Updated 12 Oct 2026: https://support.microsoft.com/en-gb/office/frequently-asked-questions-about-copilot-in-excel-7a13758f-d61e-4a56-8440-f2c9a07802ec
- Changes to Prompt Gallery. "Select one of the prompt pills or the '...' button below the input box." Updated 30 Oct 2026: https://support.microsoft.com/en-us/topic/1c192167-9250-4ef8-b488-63c474d8b84f
- Prompt Gallery. Suggested, Your Prompts, Teams; save and share. Updated 3 Nov 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-prompt-gallery
- Agent Builder, build agents. New agent, Skip to configure, Configure tab, Try it tab; name 30, description 1,000, instructions 8,000 characters. Updated 26 Oct 2026: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents
- Agent Builder, add knowledge. Up to 20 files uploaded from the device (.docx supported), SharePoint files and lists as knowledge. Updated 30 Sep 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- Samsung case (b2real): The Register, 6 April 2023, 3 incidents and the 1,024-byte limit, as in the handoff: https://www.theregister.com/2023/04/06/samsung_reportedly_leaked_its_own (not re-read; unchanged since the handoff).
