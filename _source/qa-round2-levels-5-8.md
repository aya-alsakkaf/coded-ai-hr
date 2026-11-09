# AI Fundamentals for HR · Independent QA, Levels 5 to 8 · Round 2

Scores: Content coherence 5.75/10 · Tasks and demos 8.25/10 · MAP tests 6.25/10 · Final survey 9.75/10 · Language and data safety 8.0/10
(Blocking: none. Concerning: 7. Nit: 20. Weighted over these five dimensions (20/10/10/5/10): 7.07/10. FAIL: four dimensions are below 9.0.)
Scores count every open finding: the new ones and the round 1 items that are not fixed (marked "R1").

## Round 1 findings

1. License labels (b1lic, cheat sheet, runbook, facilitator, c5t1, b1t3): FIXED. Three labels, the bottom of the m365.cloud.microsoft home page, and "M365 Copilot label (Basic or Premium)" are everywhere. They match Microsoft (April 2026).
2. Excel needs OneDrive (c4t1, d24): FIXED. Both now say "a saved .xlsx workbook". This matches the Excel FAQ (12 Oct 2026).
3. Quick-check right answer always B: FIXED for letters (A 9, B 9, C 10 of 28). A new bias replaced it: see the second Concerning under Content coherence (the right answer is the longest option).
4. e3task timer 100 min across lunch: FIXED. e3task is 25 min with the hint at 8 min, and e4build is 75 min. One leftover: the Day 3 page still shows "100:00 on the clock" (new Nit under Content coherence).
5. Task 3.2 future-dated v4: NOT FIXED at the root. A date line was added to AGENT Scope and AGENT_TESTS[1], but the knowledge still holds only v4 (from 1 Jan 2027) and leaves out v3, which is in force. See the third Concerning under Content coherence.
6. Compensation case salary floor: FIXED. Fact 2 now says all 140 earn KWD 1,200 or more.
7. Story dates and numbers: PARTLY FIXED. (b) c2story is now Thursday 12 November. (c) "14 pages" is gone. (a) c3story still calls it "Khaled's" meeting and says nobody knew the owner. See the first Nit under Content coherence (c3story).
8. Card sort 8 vs 7 min: FIXED. It is 8 min in SEGMENTS, the timer, the note and Decision 13.
9. Old JD title vs "own role": FIXED. b3story now names the Personnel Clerk role.
10. "Try it pane": FIXED. No public or staff page says "pane".
11. "View prompts": PARTLY FIXED. The text now says "the prompts button below the message box". Microsoft calls it "a prompt pill or the ... button below the input box". See the Nit on the Prompt Gallery wording under Content coherence.
12. Thread traps missing from key: FIXED. THREAD_TRAPS is in data.py, the t22 answer and the d22 expected text.
13. JE evidence traps: PARTLY FIXED. JE_TRAPS is in data.py and the Day 2 backup. The d21 expected text, the c1pp speaker note and the runbook still do not name Notes 3 and 8. See the second Nit under Tasks and demos.
14. Demo 2.1 does not match Task 2.1: FIXED. d21c (compare two versions) sits before c1task.
15. Demo 2.3 does not match Task 2.3: FIXED. d23c (timeline) sits before c3task.
16. Task 3.2 extra impossible: FIXED. It is now a second scenario plus an out-of-scope test that must refer to HR.
17. Task 2.6 extra is copy and paste: FIXED. The participant now writes their own review request.
18. EMP-5532 key needs v3: FIXED. The key now says "yes from 1 January 2027", which v4 alone supports.
19. Task 1.2 general dates: FIXED. The note accepts general dates.
20. Lab flags need digits only: FIXED. The labels say "(digits only)". A new ambiguity in Day 2 step 2 is a Nit under Tasks and demos (LABS[2] step 2).
21. No redaction demo before Task 1.2: NOT FIXED. b2sort (card sort) is still the only demo before b2task. See the first Nit under Tasks and demos.
22. MAP q1 to q5 copy Day 1 checks: PARTLY FIXED. b2chk1 is now new. q5 still mirrors b3chk (first Concerning under MAP tests). q1, q2 and q4 each keep one paraphrased distractor (Nit under MAP tests).
23. MAP q6 to q10 copy Day 2 and 3 checks: PARTLY FIXED. q7, q8 and q10 no longer match a check. q9 still mirrors c3chk2 (second Concerning under MAP tests). q6 keeps a parallel distractor (same Nit).
24. MAP q11 and q12 copy e1chk and e2chk: FIXED. The stems are different. Only the agent part names overlap, which cannot be avoided.
25. q11 and q12 test recall: FIXED. Both are work moments now.
26. Arabic right answer longest in 4 of 14: FIXED. Now 1 of 14 (q13). English: 0 strict (q1 is a tie).
27. Absurd options (q1 c, q11 d): FIXED.
28. KOC in the MAP descriptions: FIXED in the portal and in patch.py. But KOC is still on a staff page of the site: see the Concerning under Language and data safety.
29. q_intro appended three times: FIXED. patch.py is idempotent.
30. final.json has duplicate ids: FIXED. The kit and the portal have 25 questions, all ids unique. A leftover gap in the build is the Nit under Final survey.
31. "program" vs "workshop": FIXED. The survey uses "workshop" and ورشة العمل with feminine verbs.
32. Arabic drops "3 days": FIXED (الأيام الثلاثة).
33. Day 1 brief, 31 words: FIXED.
34. Idioms on slides: FIXED on public slides. The spoken "Say" line on e2task still has "try to break it" (Nit under Language and data safety).
35. Insult tied to a realistic name: FIXED. The labels are now Trainer A to D.

## New findings and open round 1 findings

### Content coherence (Level 5) · 3 Concerning, 5 Nit

Concerning · day-1 deck b1t1 (key line), b1chk1 option A feedback, b1t3 definition (build_deck.py) · Wrong product fact about what Copilot can see.
- b1t1 says "It predicts. It does not look things up unless you give it the source." But Microsoft 365 Copilot Chat searches Bing by default whenever the web helps the answer. Web search is on unless an admin turns it off (Microsoft Learn, updated 3 Nov 2026). The deck's own b1lic says Copilot Chat uses "The web".
- b1t3 says "On a Basic label, it uses only the files you upload, plus the web". But the M365 Copilot (Basic) label includes standard Copilot in the apps, and every subscriber has Copilot in Outlook. In those apps Copilot works on the open file or email.
- Fix in build_deck.py:
  - b1t1 key line: "It predicts. Without the source, it guesses or searches the web, and nothing checks the answer against Mutla's policy."
  - b1chk1 option A feedback: "It may search the web, but nothing checked the result against Mutla's policy."
  - b1t3: "On a Basic label, Copilot Chat uses the web and the files you upload. In Word, Excel, PowerPoint or Outlook, it can also use the file or email that is open."

Concerning · all three public decks, 23 of 28 quick checks (build_deck.py check() calls) · The right answer is the strictly longest option in 23 of 28 checks (82%).
- It is every Day 1 check except b2chk1, 11 of 14 on Day 2, and 5 of 6 on Day 3.
- Round 1's "always B" pattern became "always the longest": a room can tap the longest option and score high without knowing the idea.
- Fix: shorten the right answers or lengthen the distractors, so that the right answer is longest in 7 checks or fewer. Examples:
  - b1chk3: "It named its section" against "It was longer and more detailed".
  - c1chk1: make the right request the shortest option.
  - e1chk: "Five inputs, a check step, a test" against two longer wrong options.

Concerning · R1-5, not fixed · day-3 deck e2t2 (key "only approved, current policies go in" and the note "version 3 of allowances: leave it out"), t32/d32 knowledge files, data.py AGENT_TESTS[1] · Logic. The assistant's binder holds allowances v4, which "applies from 1 January 2027". It leaves out v3, which is the policy in force in November 2026.
- The slide teaches "current policies only" and then does the opposite.
- The Incomplete pass mark is "KWD 60 a month for grades 1 to 8 from 1 January 2027". That tells a grade 1 to 6 employee they get nothing until January, but v3 pays them now.
- A housing question gets KWD 300, but today's cap is KWD 250.
- Fix:
  - Add mutla-allowances-policy-v3.docx to the t32 and d32 files (5 knowledge files).
  - Add to AGENT "Scope": "Allowances: version 3 applies until 31 December 2026, version 4 from 1 January 2027. Give the rule in force today, then the change and its date."
  - Set AGENT_TESTS[1] pass to: "It asks for the grade first. Grades 1 to 6 get KWD 60 now (version 3, section 3). From 1 January 2027, grades 1 to 8 get it (version 4, section 3)."
  - Change the e2t2 note to: "Both allowance versions go in, each with its dates."

Nit · R1-7a, not fixed · day-2 deck c3story (build_deck.py, story "c3story") · The story says "Khaled's staffing meeting ... Two days later, nobody knew who owned the manpower request." In mutla-meeting-transcript-staffing.docx, Yousef is the organizer. He says "Then that is yours, Khaled", Khaled answers "Agreed", and Yousef reads all four actions back at 10:19 to 10:20.
- Fix: "Yousef's staffing meeting for the new Drilling Support section ended at 10:23. The actions were said aloud, but nobody wrote them down. Two days later, Finance asked who was sending the manpower request."

Nit · day-2 deck c5story · The story is dated "Wednesday 11 November" and says "Line managers meet next week". The brief (Key dates) and the Personnel case say the meeting is Monday 23 November, two weeks later.
- Fix: write "Line managers meet on Monday 23 November."

Nit · staff day-2 deck c5t1 note and notes-day-2 · The note says "show Create a presentation from file". Microsoft's PowerPoint pages (updated Oct 2026) describe opening Copilot in PowerPoint and typing "/" in the compose box to pick the Word file. No "Create a presentation from file" command is named.
- Fix the note: "Open Copilot in PowerPoint, type / and pick the brief (saved in OneDrive), then ask for five slides."

Nit · R1-11, partly fixed · prompt sheet Day 3 (d31 setup), runbook Day 3, staff e1t1 note · "the prompts button below the message box" is not a Microsoft control name.
- Fix: "the ... button or a prompt pill below the message box".

Nit · coded-ai-hr-day-3.html, Task 3.3 card ("100 min", "100:00 on the clock") · The room runs 25:00 on e3task and 75:00 on e4build, so the page clock disagrees with both.
- Fix: add to the t33 setup in content_demos.py as the first line: "Part 1: 11:10 to 11:35 (25 min). Part 2: 12:15 to 13:30 (75 min)." Also change the stretch or title to show "100 min in two parts".

### Tasks and demos (Level 6) · 7 Nit

Nit · R1-21, not fixed · day-1 deck b2sort (Demo 1.2) then b2task (Task 1.2) · The card sort does not show the shape of the redaction task.
- Fix: add a three-step player (redact a two-line note that is not the task file) before b2task.

Nit · R1-13, partly fixed · content_demos.py d21 "expected", the staff c1pp note, runbook Day 2 · The trainer is not told to point out Note 3 (parking) and Note 8 ("deserves grade 9"). Only the backup page lists them.
- Fix: append to d21 expected: "Notes 3 and 8 stay out: parking is not evidence, and the grade 9 opinion is for the committee."

Nit · content_demos.py t26.files and t33.files → day pages "Resources and files", the Task 2.6 and 3.3 cards, the lesson-plan file map · The case files tell participants to attach files that the day does not offer:
- The Day 2 page has no mutla-attendance-rules-2026.docx (Personnel case) and no mutla-training-policy-2026.docx (L&D case).
- The Day 3 page has no mutla-jd-template-2026.docx and no mutla-job-evaluation-factors.docx (JE capstone).
- The lesson-plan map lists neither v4 for Task 2.6 or 3.3, nor the leave policy for Task 3.3.
- Fix: add F["v4"], F["attendance"], F["brief"], F["training"], F["factors"] and F["tpl"] to t26.files. Add F["v4"], F["leave"], F["training"], F["factors"] and F["tpl"] to t33.files.

Nit · content.py LABS[2] step 2 · The step suggests "Conditional Formatting, Duplicate Values", which highlights 28 rows (both copies). The flag accepts only 14.
- Fix the label: "Type how many extra rows Remove Duplicates removes (digits only)".

Nit · mutla-capstone-compensation.docx, EMP-4417 ("My colleague Jassim Al-Fadhli ...") and CAP_KEY Compensation · The planted name of a colleague is not in the key. The key says only "decline", but the self-check says no names in any prompt.
- Fix: add to CAP_KEY: "Remove the colleague's name before the question goes into a prompt. The reply names nobody."

Nit · data.py SECTIONS and NEW_SECTION, the t24 answer, Day 2 lab step 3 · The Task 2.6 case and the transcript say Drilling Support opens on 1 March 2027. Yet the Q3 2026 control totals count its 12 positions as vacancies (true total 37). A Manpower participant can argue that 25 is right for Q3, and the key does not address this.
- Fix: add a line to the Control totals sheet ("Drilling Support: structure approved September 2026; opens 1 March 2027").
- Add a note to the t24 answer: "The structure is approved, so its 12 positions count as vacancies now."

Nit · staff decks, every solo task (b2task, b3task, b4task, c2task, c3task, c5task, c6task, e1task, e2task, e3task) · The speaker note says "Ask each pair what they found so far" on tasks marked "on your own". The e3task note also expects "A finished set of outputs ..." from the 25-minute part 1, whose agenda line is "Plan and first requests".
- Fix: pass n=N(do="Start the timer. Walk the room. Ask each person what they found so far.") to the solo task() calls.
- For e3task, set expect to "A plan of steps and the first one or two requests."

### MAP tests (Level 7) · 3 Concerning, 3 Nit

Re-derivation. I derived every answer from the slides and notes of its day: 1 b (b1t1, b1llm, b1t2) · 2 c (b1scene, b1t3) · 3 c (b2groups, b2t1) · 4 a (b2t2, b2moves) · 5 d (b3t1) · 6 b (c1t1) · 7 a (c1t2) · 8 c (c2t2) · 9 b (c3t2) · 10 d (c4t2) · 11 a (e1t1) · 12 b (e2t1) · 13 d (e2tests, e2never) · 14 c (e4rule). All 14 agree with the portal key, so there is no Blocking finding. The derivation was not fully blind: the handoff, which the brief asked me to read first, prints the key.

Checks that pass:
- The portal PRE and POST equal the kit payloads in question ids, wording, options and description.
- PRE and POST are identical except the name, slug, branding title and sitting line.
- The day split is 5/5/4, with 4 options each and no "I don't know".
- Answer letters are b4 c4 a3 d3. The right answer is strictly longest in 0 of 14 (English) and 1 of 14 (Arabic).
- Fields: teacher_student, not anonymous, sectioned, cohort AIFHR-Nov/Nov-26, folder set, CODED logo, clientName null.
- The key is in the description only.

Models: RSM Albazie PRE 763ba655 (2 Nov, updated 9 Nov) is now readable, and the structure matches it. AI Essentials PRE 1a5a7f3b still returns not_found_or_denied.

Concerning · R1-22, not fixed for q5 · PRE/POST q_5 vs public day-1 check b3chk · Same stem shape: Copilot adds content that is not in the role information, so which input would have stopped it? The options are the same three in paraphrase:
- "Tone: a friendlier style" / "A friendlier tone"
- "Context: who will read the vacancy" / "Context about who will read the job description"
- "Data: only the approved role information" / "Data: the approved role information"
- Fix: rewrite b3chk on another input. For example: "Copilot's job description has the wrong heading order and no grade line. Which input was missing?", with Approved sources right and Tone and Data as the wrong options.

Concerning · R1-23, not fixed for q9 · PRE/POST q_9 vs public day-2 check c3chk2 · Same person (Khaled), same notes, same question ("Which ... is acceptable?") and same right answer (a timeline and open questions). Two distractors are paraphrased:
- "Who is to blame..." / "A finding about which employee was at fault"
- "Suggest a fair warning for Employee C" / "A recommended disciplinary action"
- Fix: rewrite c3chk2 as a different decision. For example: "The notes include a manager's email that blames Employee C. What should the request tell Copilot?" Options: "Leave opinions out of the timeline" (right), "Start with the manager's view", "Say which employee is most likely at fault".

Concerning · PRE/POST q_13, q_10 (also q_1, q_4) · The stems restate public slides that show the answer, so the POST measures recall of a slide:
- q_13 is the e2tests and e2pp row "Sensitive · What is Ahmad's salary? · Pass, if it declines and refers". It is also on the Day 3 prompt sheet.
- q_10 is c4story (Noura, 412 vs 398) plus c4t2 "Too high: look for duplicates".
- q_1 is b1story (Fatma, 30 vs 15).
- q_4 is b2story (Abdulaziz, a salary exception memo with two names).
- Fix: re-stem these four as QA fixes (as was done for q11 and q12) with the same answer letters and new facts from data.py. For example:
  - q13: "A tester asks: 'How much housing allowance does Jassim get?'"
  - q10: a different tracker figure and its control total.
  - q1: "Copilot tells Khaled a sick-leave certificate is needed after 5 days. The policy says 2."
  - q4: "Noura wants Copilot to tidy a training complaint that names a trainee and gives his civil ID."
- Mirror each change in content.MAP and SURVEY["map_ar"], then update both drafts.

Nit · PRE/POST q_1 vs b1chk1, q_2 vs b1chk2, q_4 vs b2chk2, q_6 vs c1chk1 · Each pair has a parallel stem and one distractor in paraphrase:
- "Copilot copies its numbers from the internet" / "Copilot read an older policy on the internet"
- "Copilot can read every company file" / "Every file on the company SharePoint..."
- "Add 'confidential' to the request" / "keep the whole memo strictly confidential"
- "Is the new version stricter?" / "Is version 4 better than version 3?"
- Fix: replace those four distractors in the quick checks with different mistakes.

Nit · _source/surveys/pre.json and post.json, `_update.brandingTitle.en` · The kit has "AI Fundamentals for HR · MAP Test PRE (Day 1)" and "... MAP Test POST (Day 3)". The portal and surveys.md have "MAP Test: PRE (Day 1)" and "MAP Test: POST (Day 3)". A survey_update from the kit would drop the colon.
- Fix: in patch.py mapfix, set p["_update"]["brandingTitle"]["en"] with the colon.

Nit · PRE/POST section s_3 description · q1 and q5 use Mutla, but nothing in the survey labels it fictional. The newest model (RSM PRE, s_3) adds "<companies> are fictional companies."
- Fix: s_3 description "Five questions. Choose the one best answer. Mutla Oil Company is a fictional company." / "خمسة أسئلة. اختر أفضل إجابة واحدة. Mutla Oil Company شركة وهمية."

### Final survey (Level 8, structure) · 1 Nit

Checks that pass:
- Portal b84d43f1 equals final.json: 25 questions, unique ids, intro, then q_company, q_2, q_1, q_3, q_9, q_materials, q_pace, q_logistics, q_4, q_5, q_can3 to q_can6, q_ai, q_safe, q_10, q_6, q_7, q_11, q_nps, q_12, q_13 and q_8.
- The scale is 1 to 6 with the right anchors, and q_nps is 0 to 10. Rated items are required and open text is optional.
- No name or email is collected, and there is a progress bar.
- "workshop" is used throughout, with feminine Arabic. The slug has 55 characters.
- The hands-on list, the tools and the 3 days fit this workshop. The six "I can" items equal OUTCOMES.
- The structure matches the newest model of this family (RSM final fb337765) plus the open-workshop q_nps.

Nit · _source/build/build.sh → surveys.py · Every build rewrites final.json to the unpatched form: 22 questions, q_dept, "program", and no q_ai, q_safe or q_nps.
- The validator checks that version (build-log: "survey final 22 questions"), not the 25-question payload in the portal.
- The kit matches the portal today only because patch.py was run by hand afterward.
- Fix: run `python3 ../surveys/patch.py` and then `validate_site.py` again after every build. Record the patched counts (24/24/25) in the QA report.

### Language and data safety (Level 8) · 1 Concerning, 4 Nit

Concerning · public/staff/coded-ai-hr-lesson-plan.html (content.py LESSON_INTRO) · The page reads "CODED Professionals open workshop, run for KOC demand." That puts the real client name on a page of the deployed site, behind the staff lock. It breaks the brief ("the site must never show KOC") and CLAUDE.md Decision 3 ("no client name on any page").
- Fix: LESSON_INTRO = "CODED Professionals open workshop. 10 to 25 junior and middle-level HR employees, ...". No other page shows KOC: the deck hits are inside base64 font data.

Nit · public day-3 deck e2task and day-2 deck c1task (task titles) · The slides read "Your turn: mutla HR Policy Helper." (the engine lowercases the company name) and "Your turn: what changed between v3 and v4?." (double punctuation).
- Fix: t32 title "Build the Mutla HR Policy Helper", and t21 title "What changed between v3 and v4" without the question mark.

Nit · public day-1 deck b3t1 key line · "Facts without rules drift; rules without facts invent." This is figurative and compressed, which is hard for B2 readers.
- Fix: "Without rules, Copilot ignores the template. Without facts, it invents details."

Nit · staff day-3 deck e2task "Say" line, read aloud to the room (content_demos.py t32 "say") · "Build it, then try to break it." is the idiom that round 1 removed from the slide title.
- Fix: "Build it, then test it with hard questions."

Nit · prompt sheet Day 2, Demo 2.3b COPY request (content_demos.py TL_PARTS "Data") · The request reads "...is not signed. (Shift log). Monday 2 November..." The period comes before the parenthesis in text that participants paste.
- Fix: f"{a}: {b[:-1]} (reported by {c})."

Checked and clean:
- No em or en dashes, and no "simply / just / easily / obviously" on any participant page, public deck or survey.
- American spelling throughout. No sentence over 30 words outside navigation lists.
- All 31 sample files carry the "fictional" header and footer. Civil ID and phone are all zeros.
- Lab flags are hashed. Public decks carry no notes. No key string (duplicate IDs, 37, Mubarak answer, capstone key, MAP key) appears on a public page.

## Numbers and minutes checked

- Agenda blocks and SEGMENTS add up for every block (Day 1: 60/50/80/45; Day 2: 50/40/40/45/30/60; Day 3: 30/60). The capstone runs 15 + 25 + 75 + 20.
- Every task timer equals its task minutes. The hint for e3task is at 8 min.
- File figures equal data.py:
  - 412 rows, 14 identical duplicates, 398 control total.
  - Manpower 25 in the file vs 37 true, with Drilling Support 0 vs 12.
  - Allowance changes 250 to 300, grades 1 to 6 to grades 1 to 8, and the new section 5 (renumbered 6 and 7).
  - 140 × 50 = 7,000 a month, 84,000 a year.
  - Leave errors 30/15, 5/3 and 7/14.
  - Thread messages 3, 24 and 29.
- The capstone keys (vacancy months, leave exceptions, allowance answers) recompute correctly from data.py.
- Every date's weekday is correct for 2026.

## Product-fact sources (Microsoft)

- What Copilot license do I have (three labels; label at the bottom of the m365.cloud.microsoft home page; April 2026): https://support.microsoft.com/en-US/Microsoft-365-Copilot/what-copilot-license-do-i-have
- Copilot Chat with or without a license (web reasoning in both; work data limited to uploads without a license; agents limited; updated 6 Nov 2026): https://support.microsoft.com/en-au/topic/what-s-the-difference-between-using-copilot-chat-with-or-without-a-microsoft-365-copilot-license-5810b659-fbe0-48ee-9fe6-d731fe86cdeb
- Web search in Copilot and Copilot Chat (on by default unless an admin turns it off; Copilot sends a Bing query when the web helps; updated 3 Nov 2026): https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
- Agent Builder: build agents (New agent, Configure, Try it tab, instructions 8,000 characters, name 30 characters; 26 Oct 2026): https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents
- Agent Builder: add knowledge (up to 20 files, .docx supported; 30 Sep 2026): https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- Prompt Gallery (Suggested, Your Prompts, Teams; 3 Nov 2026): https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-prompt-gallery
- Changes to Prompt Gallery (prompts open from a prompt pill or the ... button below the input box; 30 Oct 2026): https://support.microsoft.com/en-us/topic/1c192167-9250-4ef8-b488-63c474d8b84f
- Copilot in Excel FAQ (modern .xlsx; no OneDrive requirement; 12 Oct 2026): https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel
- Create a presentation with Copilot in PowerPoint (Copilot icon at the bottom right; Oct 2026): https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d
- Copilot in PowerPoint FAQ (reference the Word file by typing "/" in the compose box): https://support.microsoft.com/powerpoint/frequently-asked-questions-about-copilot-in-powerpoint
