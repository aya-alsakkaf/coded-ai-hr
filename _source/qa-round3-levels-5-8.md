# AI Fundamentals for HR · Independent QA, Levels 5 to 8 · Round 3

Scores: Content coherence 8.0/10 · Tasks and demos 9.0/10 · MAP tests 7.25/10 · Final survey 9.75/10 · Language and data safety 9.25/10
(minus 3 per Blocking, 1 per Concerning, 0.25 per Nit. Blocking: none. Concerning: 3. Nit: 15. Weighted over these five dimensions (20/10/10/5/10): 8.43/10. FAIL: two dimensions are below 9.0 (Content coherence 8.0, MAP tests 7.25); Tasks and demos sits exactly at 9.0.)
Scores count every open finding: the new ones and the round 2 items that are not fully fixed.

## Round 2 findings

Content coherence
1. Concerning · b1t1 / b1chk1 / b1t3 product facts: PARTLY FIXED. b1t1 ("guesses or searches the web") and b1chk1 are right. The new b1t3 wording overstates the Copilot Chat (Basic) label (new Concerning C-1).
2. Concerning · quick-check right answer longest in 23 of 28: FIXED. Now 0 of 28. Letters A 9, B 9, C 10 (none above 40%). A new length pattern replaced it (Nit M-5).
3. Concerning · R1-5, allowances v3 missing from the assistant: FIXED. t32/d32 hold 5 files, AGENT "Scope" has the date rule, AGENT_TESTS[1] gives both versions, the e2t2 note and key line say both go in. One leftover: the fallback says "four files" (Nit T-2).
4. Nit · c3story owner and meeting: FIXED. Yousef's meeting, ended 10:23, Finance asked who sends the request. Matches the transcript (16 Nov, read-back 10:19 to 10:20, close 10:23).
5. Nit · c5story date: FIXED ("Line managers meet on Monday 23 November").
6. Nit · c5t1 note "Create a presentation from file": FIXED ("type / in the Copilot box and pick the file").
7. Nit · Prompt Gallery control name: PARTLY FIXED. "a prompt pill" is right, but "the prompts icon" is still not a Microsoft control (Microsoft: "a prompt pill, or the ... button, below the input box"). Open as Nit C-3.
8. Nit · Day 3 page Task 3.3 "100:00 on the clock": PARTLY FIXED. The setup now says "Part 1 runs to 11:35; part 2 runs 12:15 to 13:30", but the card still shows "100 min" and "100:00 on the clock". Open as Nit C-4.

Tasks and demos
9. Nit · R1-21, no redaction demo before Task 1.2: FIXED (Demo 1.2b d12b on slide b2pp2, 3 min in SEGMENTS).
10. Nit · R1-13, Notes 3 and 8 not in d21 expected: FIXED (d21 expected names both; it flows to the c1pp note and the Day 2 runbook).
11. Nit · case files ask for files the day does not offer: PARTLY FIXED. Attendance and training policies are now on Day 2; template, factors, leave and v4 are on the Task 3.3 card. Gaps remain (Nit T-1).
12. Nit · LABS[2] step 2 flag label: FIXED ("Type how many extra rows Remove Duplicates takes out").
13. Nit · EMP-4417 colleague name missing from CAP_KEY: FIXED ("Remove the colleague's name before prompting; the reply names nobody").
14. Nit · Drilling Support counted as Q3 vacancies: FIXED. The t24 answer now says the 12 approved positions count and accepts 25 only with the 0 flagged and a reason. (The Control totals sheet note was not added; the key covers the alternative.)
15. Nit · "Ask each pair" on solo tasks; e3task expect: FIXED. Solo task() calls now say "each person"; e3task expects "A plan and the first requests".

MAP tests
16. Concerning · q5 mirrors b3chk: FIXED. b3chk now tests the layout (Approved sources).
17. Concerning · q9 mirrors c3chk2: FIXED. c3chk2 now tests Teams transcription; c3chk3 is a different decision.
18. Concerning · q13, q10, q1, q4 restate public slides: FIXED for q1 (sick-leave certificate, 5 vs 2), q4 (grievance letter, civil ID), q10 (Q4 nominations, 431 vs 415). q13 is re-stemmed, but the new stem nearly copies a public sample file (Nit M-4).
19. Nit · q1/b1chk1, q2/b1chk2, q4/b2chk2, q6/c1chk1 parallel distractors: PARTLY FIXED. q4 is clean. q2 and q1 still have a paraphrased distractor, and q3 has the same pattern with b2chk1 (Nit M-3). q6 is now worse (Concerning M-2).
20. Nit · brandingTitle colon in the kit: FIXED (pre.json and post.json `_update.brandingTitle.en` have "MAP Test: PRE/POST").
21. Nit · s_3 fictional line: FIXED ("Mutla Oil Company is a fictional company." in EN and AR, kit and portal).

Final survey
22. Nit · build rewrites final.json; validator checks the unpatched form: NOT FIXED in the record. CLAUDE.md Decision 18 now documents the patch step and the 24/24/25 counts, and the kit equals the portal. But `_source/build-log.txt` (18:32) still reports "survey final 22 questions": the validator ran before patch.py and was not run again, and QA-REPORT.md does not record the patched counts. Open as Nit F-1.

Language and data safety
23. Concerning · KOC on the staff lesson plan: FIXED. LESSON_INTRO has no client name. KOC appears nowhere on the site or in the surveys (the only byte matches are inside base64 font data in the decks).
24. Nit · task titles "mutla HR Policy Helper" and "v3 and v4?.": FIXED ("Your turn: build the Mutla HR Policy Helper.", "Your turn: what changed between v3 and v4.").
25. Nit · b3t1 key line: FIXED ("Without rules, Copilot ignores the template. Without facts, it invents details.").
26. Nit · e2task "try to break it": FIXED ("Build it, then test it with hard questions.").
27. Nit · Demo 2.3b period before the parenthesis: NOT FIXED. The COPY text still reads "...is not signed. (source: the shift log). Monday 2 November, 09:00: ... was broken. (source: Technician G)." Open as Nit L-1.

## New findings

### Content coherence (Level 5) · 1 Concerning, 4 Nit

Concerning · C-1 · day-1 deck b1t3 (build_deck.py term "b1t3"), also the staff notes c4t1 and c5t1 (notes-day-2: "Basic users attach the file in Copilot Chat", "Basic users use the outline") · b1t3 says: "On a Basic label, Copilot Chat uses the web and the files you upload; in Word, Excel, PowerPoint or Outlook it can also use the open file or email."
- Microsoft's license page (April 2026) says the **Copilot Chat (Basic)** label has "No Copilot in Word, Excel, PowerPoint, or OneNote". Copilot in Outlook is for all subscribers. In-app Copilot Chat was removed for unlicensed users on 15 April 2026.
- So the slide is wrong for the most common Basic label. It also contradicts the next slide, b1lic ("Copilot Chat (Basic): The web, and files you upload").
- The Day 2 notes use "Basic users" for people without Copilot in Excel and PowerPoint. But the M365 Copilot (Basic) label does have standard Copilot in those apps.
- Fix in build_deck.py:
  - b1t3 definition: "With a Microsoft 365 Copilot license, Copilot uses <b>only what you can already open</b>. On the Copilot Chat (Basic) label, it uses <b>the web and the files you upload</b>, and Copilot in Outlook works on the open email. M365 Copilot (Basic) adds Copilot in Word, Excel and PowerPoint, on the open file."
  - c4t1 and c5t1 expect: write "Copilot Chat (Basic) users" in place of "Basic users".

Nit · C-2 · public hub coded-ai-hr.html, stat strip "15 prompt demos" (pages.py counts every non-task DEMOS entry) · The count includes d12, the card sort. There are 14 prompt demos (d10, d11, d12b, d13, d14, d21, d21c, d22, d23, d23c, d24, d25, d31, d32).
- Fix: set HUB["stats"] in content.py with "14 prompt demos and 1 card sort", or label the number "demos".

Nit · C-3 · R2-7, prompt sheet Day 3 (Demo 3.1 setup, content_demos.py d31 setup), runbook Day 3, staff e1t1 note · "the prompts icon or a prompt pill below the message box". Microsoft's page (updated 30 Oct 2026) says "Select a prompt pill, or the '...' button, below the input box."
- Fix: "the ... button or a prompt pill below the message box" in d31 setup and the e1t1 note.

Nit · C-4 · R2-8, coded-ai-hr-day-3.html, Task 3.3 card ("Task 3.3 · 100 min", "100:00 on the clock") · The room clock runs 25:00 on e3task and 75:00 on e4build. The card's own first step now says two parts, but the clock line still says 100:00.
- Fix: in content_demos.py t33, set the title to "A tested workflow for a new case (100 min in two parts)". Ask the engine owner for a per-task clock label, or record the leftover under Decisions.

Nit · C-5 · day-2 deck, Block 3 order (build_deck.py: c3board, c3t2, then c3chk2, then c3pp2, c3task) · c3chk2 now asks about Teams transcription for a recap. It sits after the investigation-notes concept (c3board, c3t2) and right before the timeline demo. The check lands one topic too late and interrupts the investigation flow.
- Fix: move the c3chk2 call to right after c3chk1, before c3board.

### Tasks and demos (Level 6) · 4 Nit

Nit · T-1 · R2-11 leftovers: content_demos.py t26.files, t33.files, t14.files, and the lesson-plan file map · The case and capstone files ask for files that the day or the card does not offer:
- mutla-case-je-reevaluation-request.docx says "Approved files to attach: this case file, mutla-job-evaluation-factors.docx, mutla-jd-template-2026.docx". The template is not on the Day 2 page; it is only on Days 1 and 3.
- mutla-capstone-ld.docx lists "The training policy". It is missing from the Task 3.3 card and slide e3task. It is on the Day 3 page only through Task 3.2.
- Task 1.4's source-trace request names mutla-jd-template-2026.docx, but the Task 1.4 card lists only the draft, the role information and the bank.
- The lesson-plan "Sample files" map leaves out Task 2.6 for v4, the brief, the factors and the template. It also leaves out Task 3.3 for the training policy.
- Fix: add F["tpl"], F["factors"], F["v4"] and F["brief"] to t26.files; F["training"] to t33.files; F["tpl"] to t14.files.

Nit · T-2 · staff day-3 deck e2task fallback note, runbook Day 3 "If it fails", notes Day 3 (content_demos.py t32 fallback), facilitator kit fail plan (content.py FACILITATOR "No Agent Builder") · Both texts say "attach the four files" / "with the four files". The assistant's knowledge is now five files (v3 and v4).
- A trainer who rebuilds the fallback from "four" will likely drop v3. The Incomplete test then fails ("gives both dates").
- Fix: write "the five policy files" in both places.

Nit · T-3 · data.py AGENT_TESTS[1] (pass mark shown on e2tests, d32 player, Task 3.2 answer key) · The pass mark "Pass, if it asks for the grade and gives both dates" can fail a correct assistant. The instructions say "If the answer depends on the person's grade ..., ask for it before you answer". An assistant that only asks "What is your grade?" follows its script, but a trainer marks it "fix".
- Fix: pass mark "Pass, if it asks for the grade first, then gives the rule in force now and the 1 January 2027 change".

Nit · T-4 · content_demos.py d22 (Demo 2.2, slide c2pp) vs the approved handoff and Task 2.2 · The handoff says "Demo 2.2 (prompt player): thread to decisions, then a reply to an employee's request". d22 has only the decisions request. The task asks for an announcement and a reply to Mubarak, and neither is demonstrated: the reply appears only as a backup text in the debrief.
- Fix: add a second prompt to d22 ("Reply to an employee": a short reply to message 28's sender from the final rules only, no promise). Use a message other than 29, so Task 2.2 stays fresh.

### MAP tests (Level 7) · 2 Concerning, 3 Nit

Re-derivation. I derived every answer from the slides and notes of its day:
- 1 b (b1t1, b1t2, b1llm)
- 2 c (b1scene, b1t3, b1chk2)
- 3 c (b2groups, b2t1)
- 4 a (b2t2, b2moves, Demo 1.2b)
- 5 d (b3five, b3t1)
- 6 b (c1t1, c1ever)
- 7 a (c1t2 "If Copilot suggests a grade, delete it")
- 8 c (c2t2)
- 9 b (c3t2)
- 10 d (c4t2 "Too high: look for duplicates")
- 11 a (e1t1)
- 12 b (e2t1, e2never)
- 13 d (e2tests, e2never)
- 14 c (e4rule, e4fixes, t34)

All 14 agree with the portal key "1 b · 2 c · 3 c · 4 a · 5 d · 6 b · 7 a · 8 c · 9 b · 10 d · 11 a · 12 b · 13 d · 14 c". No Blocking finding. The derivation was not fully blind: content.py, which the brief asked me to read, holds the answer indexes.

Checks that pass:
- Portal PRE 57d00a52 and POST 310d6449 equal pre.json and post.json: question ids, EN and AR wording, options, sections, description and branding.
- PRE and POST are identical except the name, slug, branding title and sitting line.
- Day split 5/5/4, 4 options each, all required, no "I don't know", no pass rule. Answer letters b4 c4 a3 d3.
- The right answer is strictly the longest in 0 of 14 (English; q1 is a tie) and 1 of 14 (Arabic, q13).
- Fields: teacher_student, isAnonymous false, sectioned, cohort AIFHR-Nov/Nov-26, folder a8f8146d, CODED logo top-center and left, clientName null.
- The key is in the portal description and on staff pages only (facilitator kit, Day 3 answer key). No public page carries it.
- The structure matches RSM PRE 763ba655: sections, intro, anchors and the fictional-company line. The newer models are unreadable: KIBS Cloud PRE b379cde6 and AI Essentials PRE 1a5a7f3b return not_found_or_denied.

Concerning · M-1 · PRE/POST q_8 vs public day-2 check c2chk, term slide c2t2 and the cheat sheet (Part 2, "Warmer, same facts") · The POST measures recall of these slides:
- The stem nearly copies c2chk. Check: "Fatma needs a three-line text message version of the announcement. Which request keeps the facts?" q_8: "Fatma needs a warmer version of the attendance announcement. Which request keeps the facts?"
- The right answer (c) is the exact sentence on c2t2, the cheat sheet and the t22 prompt: "Make it warmer; keep every date, time and rule as written."
- Wrong option (a), "Make this announcement much friendlier, warmer and more exciting for staff.", paraphrases c2t2's printed weak example "Make it friendlier.". That breaks the rule "no wrong option copied from an example on the site".
- Fix: rewrite c2chk on a different decision. For example: "Copilot's warmer announcement says the new rules start 'early next month'. What do you do?" Options: "Put back Tuesday 1 December 2026, as in message 24" (right), "Keep it, since the tone is better", "Ask Copilot to be more exact".
- In MAP q_8 (same letter c), replace option a with a mistake the site does not print, for example "\"Rewrite it so it sounds like it comes from the HR Section Head.\"". Mirror the change in SURVEY["map_ar"], then update both drafts.

Concerning · M-2 · PRE/POST q_6 and q_7 vs public day-2 Block 1 (c1story, c1chk1, c1chk2, Demo 2.1 file) · Both stems restate public Block 1 content that shows the answer:
- q_6 is the c1story / Task 2.1 situation (Abdulaziz must report what changed from v3 to v4). Its right answer, "List every change between v3 and v4, with its section number.", nearly copies c1chk1's right answer, "List each change, with its section number.". c1chk1 also has a stem of the same shape ("Hamad must tell IT what changed ... Which request is best?"). Its two wrong options are the same kinds as q_6 c and d (a rewrite, a summary of the new version).
- q_7 has the same actor, artifact and closing question as c1chk2 ("Copilot's evidence notes end with ... What does Hessa do?"). Its right answer is the same (delete the grade judgment). Its "Suggested grade: 9" is Note 8 of the Demo 2.1 file. Wrong option b, "Keep the grade, because ...", parallels c1chk2's "Keep it, since ...".
- Fix: rewrite c1chk1 on a different decision. For example: "Copilot's change table lists section 6 of v4 as new. What do you check first?", with the right answer "Whether it is only renumbered from v3 section 5".
- Rewrite c1chk2 on another evidence problem. For example: "The evidence table puts the parking note under Working conditions. What do you do?", with the right answer "Remove it: it is not evidence about the job".
- Keep q_6 and q_7 as they are (approved), or re-stem them with new facts and the same letters, as was done for q1, q4, q10 and q13.

Nit · M-3 · R2-19 leftovers: PRE/POST q_1 vs b1chk1, q_2 vs b1chk2, q_3 vs b2chk1 · Each pair has a parallel stem and one distractor of the same idea:
- b1chk1 "The employee asked the question the wrong way" / q_1 c "The question did not say which kind of leave".
- b1chk2 A "Yes, if the folder is on the company SharePoint" / q_2 a "Every file on the company SharePoint, including restricted HR folders".
- b2chk1 "Drafting the course announcement" and "Summarizing last quarter's course feedback" / q_3 a "Drafting a job description ..." and b "Summarizing a long leave policy ...".
- Fix: change those distractors in the quick checks (build_deck.py) to other mistakes. For example, b1chk2 A: "Yes, if his manager has access"; b2chk1: "Booking the training room" and "Sending the joining instructions".

Nit · M-4 · PRE/POST q_13 vs public sample file mutla-capstone-compensation.docx (EMP-4417) · The re-stemmed question nearly copies a question in a downloadable capstone file:
- q_13: "How much housing allowance does my colleague Salem get?"
- EMP-4417: "My colleague Jassim Al-Fadhli gets more housing allowance than me. How much does he get?"
- Compensation-track participants answer that file's question on Day 3, just before the POST.
- Fix: same letter d, a different sensitive ask. For example: "An employee asks the HR assistant: 'Which employees in my section are on sick leave this week?'"

Nit · M-5 · all three decks, the 28 quick checks (build_deck.py check() calls) · The length fix overshot. The right answer is now never the longest option (0 of 28) and is the middle length in 19 of 28 (68%). A room that drops the longest option and picks the middle one scores about twice the 33% guess rate.
- Fix: make the right answer the longest in 4 to 7 checks and the shortest in about a third. For example, lengthen the right answers of b2chk1, c1chk2 and e0chk3.

### Final survey (Level 8, structure) · 1 Nit

Checks that pass:
- Portal b84d43f1 equals final.json: 25 questions, unique ids, in this order: intro, q_company, q_2, q_1, q_3, q_9, q_materials, q_pace, q_logistics, q_4, q_5, q_can3 to q_can6, q_ai, q_safe, q_10, q_6, q_7, q_11, q_nps, q_12, q_13, q_8.
- Rated items are 1 to 6, required, with the right anchors. q_nps is 0 to 10. Open text is optional. collectName and collectEmail are false, and the progress bar is on. Sections are s_1, s_learn, s_team and s_comments.
- "workshop" and ورشة العمل with feminine verbs are used throughout. The slug has 55 characters. The description matches surveys.md.
- The hands-on list, the tools (Microsoft Copilot), the 3 days and the six "I can" items fit OUTCOMES.
- The structure equals the RSM final fb337765 model, plus the open-workshop q_nps.

Nit · F-1 · R2-22, _source/build-log.txt and _source/QA-REPORT.md · The last build log (18:32) still validates "survey final 22 questions". patch.py ran afterwards (final.json written 100 ms later), but validate_site.py was not run again, and the QA report does not record the patched 24/24/25 counts.
- Fix: after `python3 _source/surveys/patch.py`, run `python3 _source/build/validate_site.py public` again, append its output to build-log.txt, and write "PRE 24 · POST 24 · final 25, equal to the portal" in QA-REPORT.md.

### Language and data safety (Level 8) · 3 Nit

Nit · L-1 · R2-27, prompt sheet Day 2, Demo 2.3b COPY request (content_demos.py TL_PARTS "Data") · The pasted text reads "...is not signed. (source: the shift log). ... was broken. (source: Technician G)." It has a period before the parenthesis and a second one after it.
- Fix: `" ".join(f"{a}: {b[:-1]} (source: {c})." for a, b, c in D.TL_NOTES)`.

Nit · L-2 · public decks, figurative key lines (build_deck.py) · Three lines are hard for B2 readers:
- e1t1 "…a tested request <b>on the shelf</b> for everyone." "On the shelf" is an English idiom for "unused", the opposite of the meaning here.
- b3one "Speed without inputs is fast rework."
- c3story "A meeting with no actions did not happen."
- Fix: "…a tested request that everyone can find and use."; "A fast request with no inputs means more work later."; "A meeting with no written actions is easy to forget."

Nit · L-3 · coded-ai-hr-day-1.html and prompt sheet Day 1, Task 1.4 (content_demos.py t14 hint); coded-ai-hr-day-2.html and slide c6task (t26 stretch) · Two wording slips:
- The Task 1.4 card reads "Look for: Look for a team size and a grade."
- The Task 2.6 extra says "without copying the one on this sheet" on the day page and slide, where no review request is shown.
- Fix: t14 hint "A team size and a grade."; t26 stretch "... without copying the review request on the prompt sheet."

Checked and clean:
- No em or en dashes on any participant page, public deck slide, or survey payload (EN and AR). No "simply / just / easily / obviously". American spelling.
- No sentence over 30 words outside navigation and file lists.
- All 31 sample files carry the fictional header and footer. Civil ID 000000000000 and phone +965 0000 0000. Capstone trainers are labels (Trainer A to D).
- No KOC on the site or in the surveys. No credentials: middleware.js reads STAFF_PASSWORD from the environment.
- Public pages carry no key string: the MAP key, the duplicate IDs, 37 vs 25, the redaction map, EMP-4417 and the Mubarak answer appear only under /staff.

## Numbers and minutes checked

- SEGMENTS add up for every block:
  - Day 1: 60 / 50 / 80 / 45.
  - Day 2: 50 / 40 / 40 / 45 / 30 / 60.
  - Day 3: 30 / 60.
  - Every agenda day totals 360 minutes.
- Timers match the minutes: b3timer 8, b5go 15, c6gallery 10, e3task 25:00, e4build 75:00, e5share 15. Task timers equal the task minutes. Slide counts are 61 / 64 / 40, equal to SLIDES.
- Tracker workbook:
  - 412 Training rows, 398 unique IDs, 14 identical duplicates.
  - The unit split equals the Control totals sheet.
  - Manpower shows Drilling Support at 0 vs 12 in the structure: 25 vacancies in the file vs 37 true (286 approved, 249 filled).
- Leave errors 30/15, 5/3 and 7/14 are in the answer file and LEAVE_ERRORS.
- Allowances v3/v4: housing 250 to 300, transport grades 1 to 6 to 1 to 8, the new section 5, renumbered 6 and 7. Effective dates are 1 Jan 2025 and 1 Jan 2027.
- Compensation case: 140 × 50 = 7,000 a month, 84,000 a year.
- Capstone and fresh-input keys recompute from data.py:
  - Vacancy ages as of 31 Oct and 15 Nov, including the 6-month edge for the Production Engineer.
  - Leave exceptions on the 15-day cap, including the EMP-1502 edge.
  - Allowance answers.
- Every story and file weekday is right for 2026: 1, 8, 15 and 22 Nov are Sundays; 1 Dec is a Tuesday; 10 Dec and 26 Nov are Thursdays.
- The thread (message 24 approval, message 29 Mubarak, exported 12 Nov) agrees with c2story, the brief and the cases.

## Product-fact sources (Microsoft, read 9 Nov 2026)

- What Copilot license do I have. Three labels at the bottom of the M365 home page. Copilot Chat (Basic) has no Copilot in Word, Excel, PowerPoint or OneNote. Outlook is for all subscribers. Updated April 2026: https://support.microsoft.com/en-US/Microsoft-365-Copilot/what-copilot-license-do-i-have
- Copilot Chat with or without a license. Web reasoning in both. Work data is limited to uploads without a license. Apps "depend on your label". Agents are limited. Updated 6 Nov 2026: https://support.microsoft.com/en-au/topic/what-s-the-difference-between-using-copilot-chat-with-or-without-a-microsoft-365-copilot-license-5810b659-fbe0-48ee-9fe6-d731fe86cdeb
- In-app Copilot Chat removed for unlicensed users from 15 April 2026; Outlook kept (Purdue IT notice): https://it.purdue.edu/newsroom/articles/260403-microsoft-removes-in-app-copilot-chat-features-for-non-licensesd-users.php
- Create a presentation with Copilot in PowerPoint. Copilot icon at the bottom right. Tips for building from a Word file. Updated Oct 2026: https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d
- Copilot in Teams meetings. Questions about the meeting after it ends need a transcript. Intelligent recap needs Teams Premium or a Copilot license. Updated 24 Sep 2026: https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
- Changes to Prompt Gallery. "Select a prompt pill, or the '...' button, below the input box." Updated 30 Oct 2026: https://support.microsoft.com/en-us/topic/1c192167-9250-4ef8-b488-63c474d8b84f
- Prompt Gallery. Suggested, Your Prompts, Teams; save and share. Updated 3 Nov 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-prompt-gallery
- Agent Builder, build agents. New agent, Skip to configure, Configure tab, Try it tab. Name 30, description 1,000 and instructions 8,000 characters. Updated 26 Oct 2026: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents
- Agent Builder, add knowledge. Up to 20 embedded files, .docx supported. Updated 30 Sep 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- Not re-read this round: the Excel FAQ ("a saved .xlsx workbook", verified in round 2 on 12 Oct 2026). Web search on by default in Copilot Chat was also verified in round 2 (Microsoft Learn, 3 Nov 2026).
