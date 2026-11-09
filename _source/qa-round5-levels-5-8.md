Scores: Content coherence 9.5/10 · Tasks and demos 10/10 · MAP tests 7.0/10 · Final survey 10/10 · Language and data safety 10/10

# AI Fundamentals for HR · Independent QA, Levels 5 to 8 · Round 5

(minus 3 per Blocking, 1 per Concerning, 0.25 per Nit. Blocking: none. Concerning: 2. Nit: 6. Weighted over these five dimensions (20/10/10/5/10): 9.27/10. FAIL: MAP tests is below 9.0.)
Scores count every open finding: the new ones and the round 4 items that are not fully fixed (round 4 M-2 and M-3 are only partly fixed; their leftovers are counted below as Nits M-3 and M-4).

Audited on 9 November 2026 against the kit as built at 19:50 (data.py, content.py, content_demos.py and build_deck.py 19:50:03; public/ and _source/kit-pages 19:50:19; survey payloads 20:05:29, after patch.py) and the portal drafts as read today (PRE updated 17:21 UTC, POST 17:24 UTC, final 17:24 UTC).

How blind the MAP derivation was: I read the 14 stems and options from the kit payload with a script that printed no description, wrote down my 14 answers from the Day 1 to Day 3 slides and notes in build_deck.py and content_demos.py, and only then opened the portal drafts and content.py MAP / map_ar. It was not fully blind: HANDOFF.md, which the brief asks me to read first, prints the original key, and Decisions 12, 17, 19 and 20 keep the same letters.

## Round 4 findings (and the round 3 items it listed as partly fixed)

Content coherence
1. Nit · C-1, SEGMENTS order: FIXED. content.py SEGMENTS now follow the deck: Day 1 Block 2 (10:55 groups and card, 11:04 sort, 11:12 redact, 11:17 Demo 1.2b), Day 2 Block 1 (09:14 concepts, 09:22 Demo 2.1, 09:28 checks and recruitment, 09:35 Demo 2.1b), Day 2 Block 3 (10:59 before and after, 11:03 Demo 2.3, 11:09 checks and timeline, 11:13 Demo 2.3b). Totals unchanged (50, 50, 40).
2. Nit · C-2, 2019 job description title: FIXED. data.py OLD_JD["title"] = "HR Officer". Slide b3story reads "the 2019 job description for the HR Officer role" and mutla-jd-hr-officer-2019.docx reads "Position: HR Officer".
3. Nit · C-3, e3story "two hours": FIXED. e3story reads "You have a new case, Copilot, and 100 minutes."

Tasks and demos
4. Nit · T-1, Demo 2.2 reply with no expected result or backup: FIXED. content_demos.py d22 expected now ends with the reply, and the backup has a "Typical reply to a staff question" block (seen on staff backup Day 2 and runbook Day 2). The thread has no current hours (checked messages 1 to 30), so the reply is right to say so. This also closes round 3 T-4.
5. Nit · T-2, AGENT_TESTS[0] pass condition: FIXED. "Pass, if it gives the rule and cites section 4" on e2tests, the Demo 3.2 player and the Day 3 answer key.

MAP tests
6. Concerning · M-1, q_1 option a defensible: FIXED. Option a is now "Copilot copied the number from another employee's chat" (AR "نسخ Copilot الرقم من محادثة موظف آخر"). b1scene and b1t3 teach that Copilot opens only your own doors, so a is false under the deck's words. Portal PRE and POST updated.
7. Concerning · M-2, q_8 recall of Day 2 Block 2 (round 3 M-1 leftover): PARTLY FIXED. The stem now uses a new actor and document (Hessa, the Eid holiday notice) and the key is no longer the c2t2 sentence, so the recall problem is gone. The test-wise cue is not: the stem says "with no date" and option c is the only option that mentions a date. Open as Nit M-3 below.
8. Nit · M-3, b1chk1 parallels q_1 (round 3 M-3 leftover): PARTLY FIXED. The two distractors are new ("Copilot learned from an older Mutla policy", "Copilot rounds leave days up to a full month"). The stem frame and the key still match q_1, which round 4 also listed. Open as Nit M-4 below.
9. Nit · M-4, e0chk1 distractor and the Payroll Officer job: FIXED. e0chk1 option 2 is "Move it to a note at the end of the draft". q_7 names a Safety Officer, a job in no sample file, slide or page (searched all 31 files and every page).
10. Nit · M-5, q_11 paraphrases e1story: FIXED. q_11 is now about three Personnel officers and a monthly reminder to managers about leave requests waiting for approval. Same letter a.

Final survey
11. Nit · F-1, no warning about the 0 to 10 item: FIXED. The intro now ends "The last recommend question uses 0 to 10." (AR "سؤال التوصية الأخير من 0 إلى 10."), in final.json and in portal b84d43f1.

Language and data safety
12. Nit · L-1, Task 2.1 "Look for: Look at": FIXED. t21 hint reads "The housing cap, the transport grades and one new section." on the Day 2 page and prompt sheet.

## New findings

### Content coherence (Level 5) · 2 Nit

Nit · C-1 · build_deck.py slide b1t3 (Day 1 deck, Block 1) · "On Copilot Chat (Basic), it uses the web, the files you upload and Outlook." reads as if Copilot Chat can use the participant's mailbox. Microsoft's comparison page (updated 6 Nov 2026) says that without a license, work data reasoning is "Limited (uploaded files)"; Copilot in Outlook is an app that is "Included", not a data source for Copilot Chat. The next slide (b1lic) says "Copilot in Outlook", so the two slides teach this point in two different ways.
- Fix: in build_deck.py b1t3, write "On Copilot Chat (Basic), it uses the web and the files you upload, and you also get Copilot in Outlook. M365 Copilot (Basic) adds Copilot in Word, Excel and PowerPoint."

Nit · C-2 · content_demos.py d22 setup (Demo 2.2 card on the Day 2 prompt sheet and the Day 2 runbook) · "(In Outlook with Copilot, open the thread and choose Summarize.)" Microsoft names the control "Summary by Copilot (or it might say Summarize) at the top of the email thread" (support page updated 18 Sep 2026). A trainer or participant who looks for "Summarize" on a current Outlook build sees "Summary by Copilot".
- Fix: "(In Outlook with Copilot, open the thread and select Summary by Copilot, or Summarize, at the top of the thread.)"

### Tasks and demos (Level 6) · none

### MAP tests (Level 7) · 2 Concerning, 4 Nit

Re-derivation from the slides and staff notes of each day (written before I read the key):
- 1 b (b1t1 "It predicts. Without the source, it guesses or searches the web, and nothing checks it", b1t2, b1llm)
- 2 c (b1scene, b1t3 "With a Microsoft 365 Copilot license, Copilot uses only what you can already open"; see M-6)
- 3 c (b2groups, b2t1)
- 4 a (b2t2, b2moves, b2chk2, Demo 1.2b)
- 5 d (b3five, b3t1 "Without facts, it invents details.", b3scene note "No data: invented duties.")
- 6 b (c1t1, c1ever)
- 7 a (c1t2 "If Copilot suggests a grade, delete it.", d21 control line)
- 8 c (c2t2 "Name what must not change.")
- 9 b (c3t2)
- 10 d (c4t2 "Too high: look for duplicates.")
- 11 a (e1story, e1t1, t31)
- 12 b (e2t1, e2chk feedback "Instructions say how to behave")
- 13 d (AGENT "Must not answer" and "Refer to HR", e2never, e2tests)
- 14 c (e4rule, e4fixes "Each fix is a missing input")

All 14 agree with the portal key "1 b · 2 c · 3 c · 4 a · 5 d · 6 b · 7 a · 8 c · 9 b · 10 d · 11 a · 12 b · 13 d · 14 c". No Blocking finding.

Concerning · M-1 · PRE/POST q_9 (content.py MAP[8], SURVEY["map_ar"][8]) · The item has no work moment ("Khaled asks Copilot to work on synthetic investigation notes. Which output is acceptable?") and all four options are taken from one printed rule:
- Cheat sheet Part 2, "Investigation notes": "Timeline and open questions. No finding, no blame, no recommended action."
- Day 2 prompt sheet, Task 2.3 request: "make a timeline of events ... Then list the open questions ... Do not give a finding, do not say who is at fault, and do not recommend an action."
- Key b "A timeline of events and a list of open questions" copies the first half; a "A finding about which employee was at fault" and c "A recommended disciplinary action" copy the second half. Slide e0chk3 ("Keep events and open questions only") repeats the rule at 09:00 on the POST day.
- The POST measures recall of a printed line, not judgment on a draft (QA rule: items test judgment at work, not recall).
- Fix (same letter b): a work moment where the participant judges concrete lines whose words are on no page. For example: "Khaled's notes on a late delivery to the main stores go into an HR case file. Which line of Copilot's draft can stay?"
  - a "The stores team is to blame for the three-hour delay."
  - b "10 November, 14:00: the truck arrived 3 hours late (gate log)."
  - c "The stores supervisor should be moved to another shift."
  - d "The driver's account is more believable than the clerk's."
  - Mirror it in map_ar[8], keep b from being the longest option in EN and AR, update both drafts. ("written warning", "careless" and "never follows procedures" are already in the Task 2.3 file and slides, so keep them out.)

Concerning · M-2 · PRE/POST q_10 (content.py MAP[9], data.py MAP_Q10, SURVEY["map_ar"][9]) · The stem is the Day 2 story with the numbers swapped, and the key is a printed rule:
- c4story: "Noura's quarterly report says 412 training requests for Q3. The training system's control total says 398." q_10: "Copilot counts 431 course nominations for Q4. The training system's control total is 415. What does Noura do first?" Same person, same system sentence, same too-high direction. The round 2 re-stem changed only the numbers.
- Key d "Look for duplicate rows in the tracker" restates the cheat sheet ("A total that is too high: look for duplicates."), slide c4t2 ("Too high: look for duplicates."), the Day 2 prompt sheet ("A total that is too high: look for duplicate request IDs.") and the Day 2 lab.
- A participant answers by recalling Task 2.4, which is the defect round 4 ranked Concerning for q_8.
- Fix (same letter d): a different actor, tracker and unit, and a key not worded like the printed rule. For example, set data.py MAP_Q10 to two numbers that appear in no file (for example 247 and 239) and write: "Khaled asks Copilot how many employees joined Mutla in Q3. Copilot says 247. The HR system's checked total is 239. What does he do first?"
  - a "Use 247, because Copilot read every row of the file"
  - b "Report 243, the number halfway between the two"
  - c "Ask Copilot to round both numbers to the nearest ten"
  - d "Ask for the rows it counted and find the 8 extra"
  - Mirror it in map_ar[9] and update both drafts.

Nit · M-3 · PRE/POST q_8 (content.py MAP[7], SURVEY["map_ar"][7]) · Round 4 M-2 leftover. The stem ends "says the office reopens 'after the holiday', with no date", and c ("copy the reopening date from the original") is the only option that mentions a date or the original. A PRE taker can match the words. The builder reference (surveys.md section 8) says a PRE that a room can answer near full marks is too easy.
- Fix (same letter c): make every option keep something from the original, so only what is kept differs, and take "date" out of the stem: "... The new version no longer says when the office reopens. Which request would have stopped this?"
  - a "Make it warmer, and keep the original greeting at the top."
  - b "Make it warmer, and keep it the same length as before."
  - c "Make it warmer, and change no day or time in it."
  - d "Make it warmer, and keep the original headings and layout."
  - Mirror it in map_ar[7] and update both drafts.

Nit · M-4 · build_deck.py slide b1chk1 (Day 1 deck) vs PRE/POST q_1 · Round 4 M-3 leftover. b1chk1 still has the q_1 frame ("Copilot tells an employee that Hajj leave is 30 days. Mutla's policy says 21.") and the q_1 key: b1chk1's right answer "It sounds sure, but nothing checked it" with the feedback "It predicts likely words. The approved policy decides." is q_1 b "It predicts likely words, and nothing checked the policy" in two parts.
- Fix: turn b1chk1 into an action check with a new frame, for example "An employee forwards you Copilot's answer: Hajj leave is 30 days. <b>What do you check before you reply?</b>" with "The Hajj section of the leave policy" (right), "How sure Copilot sounded in its answer" and "A second answer from a new Copilot chat". Update the Day 1 answer key through the kit.

Nit · M-5 · build_deck.py slide b2chk2 (Day 1 deck) vs PRE/POST q_4 · b2chk2 and q_4 have the same frame, key and distractor idea:
- b2chk2: "Fatma wants help with a reply to a sick-leave complaint. The note has the civil ID and the diagnosis. What first?" Right: "Remove the ID and diagnosis; use a role for the name". Distractor: "Use Copilot on her phone instead".
- q_4: "Khaled wants Copilot to summarize a grievance letter that names the employee, her manager and her civil ID. What does he do first?" Key: "Replace the names and remove the civil ID before he uploads it". Distractor c: "Open a new chat so that the letter stays private".
- Fix: make b2chk2 test a different redaction decision, for example "Fatma has redacted a sick-leave complaint. <b>Which detail can stay in the text she gives Copilot?</b>" with "The dates of the absence" (right; the Task 1.2 key keeps the facts), "The civil ID, since HR holds it anyway" and "The diagnosis, so the reply sounds caring".

Nit · M-6 · PRE/POST q_2 (content.py MAP[1]) and build_deck.py slides b1t3 and b1lic · The stem says Hessa has "a Microsoft 365 Copilot license", but the deck never says which label that is. Slide b1lic lists "M365 Copilot (Basic)" with "The web and files you upload". Microsoft's license page says M365 Copilot (Basic) means no add-on license and M365 Copilot (Premium) means the add-on license. A participant whose own label says "M365 Copilot (Basic)" can read the stem as their case and defend b "Only the files she uploads in this chat".
- Fix (stem and letter unchanged): in b1t3 write "With a Microsoft 365 Copilot license (the M365 Copilot (Premium) label), Copilot uses only what you can already open." (with the C-1 wording for the rest), and in the b1lic Premium row write "Your files, emails, chats and meetings (the Microsoft 365 Copilot license)".

Checks that pass:
- Portal PRE 57d00a52 and POST 310d6449 equal _source/surveys/pre.json and post.json: names, slug, description and key, all 24 question ids in order, EN and AR labels, options, scale anchors, sections and section descriptions, branding title and subtitle, cohort and folder.
- PRE and POST differ only in name, slug, branding title and the sitting line of the description (field-by-field diff of the kit payloads).
- Day split 5/5/4, one section per day. 4 options each, one key. All 20 rated and knowledge items required. No "I don't know", no pass rule, no "all of the above". Key letters a 3, b 4, c 4, d 3.
- The key is strictly the longest option in 0 of 14 in English (q_1 ties) and in 1 of 14 in Arabic (q_13; q_1 ties).
- Every label, option, section title and section description is filled in English and Arabic. No em or en dash in the payloads.
- Fields: audience teacher_student, isAnonymous false, displayMode sectioned, cohort AIFHR-Nov/Nov-26, folder a8f8146d, CODED logo top-center and left, clientName null.
- The key is only in the portal descriptions and on staff pages (Day 3 answer key). No public page, deck, prompt sheet or sample file carries it.
- No other option is defensible from the deck's words, apart from M-6. Checked in particular: q_1 a (b1scene), q_1 c (the stem names sick leave), q_11 c (starter prompts are in one agent and are not shared or tested), q_12 a (e2chk "Instructions say how to behave"), q_13 c (the knowledge files hold no records, and "Must not answer" covers personal data), q_14 a (e4rule).
- Stems with fresh work moments whose key states a taught idea in new words, not counted as recall: q_5 (shares the b3chk frame but has a different answer, so it tests Data against Approved sources), q_6, q_7, q_11, q_12, q_13, q_14. q_7 and e0chk1 share the idea "remove Copilot's decision from a committee draft", but not the frame or the words.
- Model surveys: RSM Albazie PRE 763ba655 (updated 9 Nov 2026, 14:20 UTC) read today. Our structure matches it: s_1 to s_5, the q_intro wording, name, work email, company (q_company in place of q_dept for an open workshop), the 1 to 5 confidence anchors, and the fictional-company line in s_3. RSM adds "Part 3: Work scenarios"; surveys.md section 8 asks for it only for intermediate or senior rooms, and this room is junior and middle level. KIBS Cloud PRE b379cde6 and AI Essentials in the Workplace PRE 1a5a7f3b return not_found_or_denied. Intro and closing screens keep the portal defaults (Decision 8).

### Final survey (Level 8, structure) · none

Checks that pass:
- Portal b84d43f1 equals final.json: 25 questions with unique ids, in this order: intro, q_company, q_2, q_1, q_3, q_9, q_materials, q_pace, q_logistics, q_4, q_5, q_can3 to q_can6, q_ai, q_safe, q_10, q_6, q_7, q_11, q_nps, q_12, q_13, q_8.
- Rated items are 1 to 6 with "Strongly disagree" and "Strongly agree" anchors, all required. q_nps is 0 to 10, and the intro now says so. Open text is optional. q_company is optional. collectName and collectEmail are false, and the progress bar is on.
- Sections s_1 "Your feedback", s_learn "What you can do now", s_team "Education Team", s_comments "Comments", EN and AR. Same structure and ids as the newest readable model, RSM Albazie final fb337765 (updated 9 Nov 2026), plus q_company and q_nps for an open workshop as surveys.md section 9 asks.
- "workshop" and ورشة العمل with feminine agreement throughout ("لبّت ورشة العمل", "قدّم المدرّب ورشة العمل", "بورشة العمل هذه"). Slug 55 characters.
- Fit: the hands-on item names job descriptions, policy comparisons, the HR tracker, the HR assistant and the capstone. q_logistics names Microsoft Copilot. q_pace and q_12 say 3 days. q_4, q_5 and q_can3 to q_can6 equal the six OUTCOMES word for word, and so do PRE/POST q_r1 to q_r6.

### Language and data safety (Level 8) · none

Checks that pass:
- No em or en dash on any participant page, staff page, slide, sample file or survey payload (scanned the text of all 13 public pages, 3 public decks, 18 staff pages, 31 sample files and the three payloads).
- No "simply", "easily", "obviously", "e.g.", "i.e." or "etc." on participant pages, slides or surveys. The one "just" is on the staff Day 3 answer key ("just over 6 months").
- No sentence over 30 words on participant pages, slides or surveys. The only hits are navigation lists, file lists and the card-sort and quick-check option strips.
- American spelling: no organise, colour, licence, programme, analyse, centre, behaviour or similar.
- All 30 .docx files carry "Mutla Oil Company (fictional) · training file made by CODED" in the header and the fictional line in the footer. The workbook carries it on its Notes sheet.
- Personal data: civil ID 000000000000, phone +965 0000 0000, employee codes only in the tracker and the capstone extracts, roles only in the investigation notes, Trainer A to D. The planted names (Bader Al-Hajri, Sara Al-Mutawa, Jassim Al-Fadhli, Saud) are fictional and are part of the keys.
- No "KOC" or "Kuwait Oil" on any page, file, payload or CLASS-PLAN.md. No credentials: the only "password" strings are the staff index note, the joining note and the Wi-Fi line in the facilitator kit.
- Public pages carry no key string: no duplicate request ID, no capstone answer, no MAP key. The Day 1 and Day 2 lab answers are hashed (data-h).

## What I checked and found clean

Kit fidelity
- public/ (19:50:19) was built after the last kit edit (19:50:03), and build-log.txt records "39 pages checked · PROBLEMS: 0" and the re-run after patch.py (17:05:29 UTC = 20:05:29 local, "PROBLEMS: 0"). I ran validate_site.py again on a copy of the repo in my scratchpad (nothing changed in the repo), with the patched survey payloads in place: "39 pages checked · PROBLEMS: 0". Its fidelity check compares every slide and speaker note with the kit records, so the slides and notes equal the kit word for word.
- The kit payloads (20:05:29) equal the portal drafts (updated 17:21 to 17:24 UTC), as listed above.

Outline coverage and handoff fidelity
- Every outline topic, hands-on, extra challenge and close maps to a block, slides and a task, as in round 4. All eight outline outcomes are covered: grounding and checking (Day 1 Block 4, Task 1.4), figure checks (Day 2 Block 4, Task 2.4), the second-scenario extra (t32 stretch).
- Differences from the handoff are recorded in Decisions 11 to 20 (Demos 1.2b, 2.1b, 2.3b; the 8-minute sort; both allowance versions in the assistant; 25 + 75 capstone; MAP re-stems with the same letters).

Minutes
- Every SEGMENTS block adds up and starts on time: Day 1 60 / 50 / 80 / 45; Day 2 50 / 40 / 40 / 45 / 30 / 60; Day 3 30 / 60. Each agenda day is contiguous from 09:00 to 15:00. CLASS-PLAN.md, the day pages and DAYS agree.
- Deck timers read from the built decks: b3timer 8, b5go 15, c6gallery 10, e3task 25, e4build 75, e5share 15, both MAP slides 10, and every other task timer equals its task minutes (12, 12, 25, 15, 15, 12, 12, 15, 10, 45, 10, 30, 20). The t33 card and prompt sheet give "Part 1 runs to 11:35; part 2 runs 12:15 to 13:30", matching e3task and e4build.
- Slide counts 61 / 64 / 40, equal to SLIDES and within 10% of the handoff (60 / 62 / 40).

Numbers (recomputed from the files)
- Tracker workbook (opened with openpyxl): Training 412 data rows, 398 unique request IDs, 14 duplicates, all 14 identical rows. Control totals 398 with the unit split. Manpower sheet: Drilling Support 0 / 0 / 0, vacancies 25; Control totals: Drilling Support 12 / 0 / 12, 286 approved, 249 filled, 37 vacancies.
- Thread: message 3 (1 Nov) proposes 15 November; message 24 (Monday 9 Nov) approves Tuesday 1 December; traps at messages 11 and 12 (10:12, 10:14) and 18 (11:40); message 29 is Mubarak's 6:00 request; no message states the current hours. Exported 12 November, as in c2story.
- Transcript: four actions read back at 10:19 to 10:20, one open question at 10:21, close at 10:23 on Monday 16 November.
- Capstone keys recompute from the files: Manpower October over 6 months Maintenance Technician (8) and Gas Plant Operator (9), September example 8 open and 2 over 6 months (8 and 7 months, consistent with the dates); November edge Production Engineer at exactly 6 months and 1 day. Personnel October over 15: EMP-1187, 1466, 1739, 1954; still over after planned: 1187, 1739, 1954; EMP-1502 at exactly 15. November: over 15 1187, 1466, 1739; still over 1739.
- Allowances v4 header "applies from 1 January 2027", so the EMP-5532 date in the Compensation key is findable from the one file the case gives.
- MAP q_1 uses LEAVE["sick_cert"] = 2 (leave policy section 6, "more than 2 days in a row"). q_10 uses MAP_Q10 (431, 415).
- Weekdays in stories and files are right for 2026.

Tasks and demos
- All 14 tasks have files, minutes, solo or pairs, one deliverable, a participant hint, a staff answer and a finished-early extra. Each demo uses the same file and request shape as the task after it.
- Every Task 2.6 case file names the meeting its Output 3 needs (committee 10 Dec, Finance, Head of L&D, Recruitment, line managers 23 Nov) and lists its approved files.
- Every planted item is findable and in a key, and the keys accept the defensible alternatives (as in round 4, re-checked against the rebuilt files).

Product facts (Microsoft pages, read 9 November 2026)
- What Copilot license do I have. Labels under your name at the bottom of the Microsoft 365 home page. Copilot Chat (Basic): Copilot in Outlook, no Copilot in Word, Excel, PowerPoint or OneNote. M365 Copilot (Basic): standard access to Copilot in the apps, no add-on license. M365 Copilot (Premium): the add-on license. Updated April 2026: https://support.microsoft.com/en-US/Microsoft-365-Copilot/what-copilot-license-do-i-have
- Copilot Chat with or without a license. Web data in both; work data "Limited (uploaded files)" without a license and "Full (meetings, emails, chats, files, and more)" with one; agents "Limited (no advanced agents)"; Copilot in Outlook "Included" in both; apps "Depends on your label". Updated 6 Nov 2026: https://support.microsoft.com/en-au/topic/what-s-the-difference-between-using-copilot-chat-with-or-without-a-microsoft-365-copilot-license-5810b659-fbe0-48ee-9fe6-d731fe86cdeb
- Agent Builder, build agents. New agent, Skip to configure, Configure tab, Try it after name, description and instructions; name 30, description 1,000, instructions 8,000 characters. Updated 26 Oct 2026: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents
- Agent Builder, share and manage. "After you build and test your agent ... select Create." Updated 6 Nov 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents
- Agent Builder, add knowledge. Up to 20 files uploaded from the device, .docx supported, up to 100 SharePoint files. Updated 30 Sep 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- Extensibility cost. Copilot Chat users: instruction-based agents and public sites free, SharePoint and connectors metered (supports "Agents are limited on a basic label" and the Task 3.2 fallback). Updated 5 Nov 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/cost-considerations
- Prompt Gallery. Suggested, Your Prompts, Teams. Updated 3 Nov 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-prompt-gallery
- Changes to Prompt Gallery. "Select one of the prompt pills or ... below the input box." Updated 30 Oct 2026: https://support.microsoft.com/en-us/topic/1c192167-9250-4ef8-b488-63c474d8b84f
- Create a new presentation with Copilot in PowerPoint. Copilot icon at the bottom right; Word Styles; Word files under 24 MB. Updated October 2026: https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d
- Add a slide from a file with Copilot in PowerPoint. "Select Reference a file or type / to choose the file" (supports the c5t1 note). Updated 15 Sep 2026: https://support.microsoft.com/en-us/powerpoint/copilot/add-a-slide-from-a-file-with-copilot-in-powerpoint
- Frequently asked questions about Copilot in Excel. Save as Excel Workbook (.xlsx); M365 Copilot (Basic) has standard access. Updated 12 Oct 2026: https://support.microsoft.com/en-gb/office/frequently-asked-questions-about-copilot-in-excel-7a13758f-d61e-4a56-8440-f2c9a07802ec
- Copilot in Teams meetings. Questions after the meeting need a transcript; "During and after the meeting" requires transcription; intelligent recap with the Copilot license or Teams Premium. Updated 24 Sep 2026: https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
- Summarize an email thread with Copilot in Outlook. "Select Summary by Copilot (or it might say Summarize) at the top of the email thread" (see C-2). Updated 18 Sep 2026: https://support.microsoft.com/office/summarize-an-email-thread-with-copilot-in-outlook-a79873f2-396b-46dc-b852-7fe5947ab640
- Samsung case (b2real): The Register, 6 April 2023, 3 incidents and the 1,024-byte limit, as in the handoff: https://www.theregister.com/2023/04/06/samsung_reportedly_leaked_its_own (not re-read; unchanged since the handoff).
