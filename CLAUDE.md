# CLAUDE.md

AI Fundamentals for HR: a three-day CODED Professionals open workshop on Microsoft Copilot (and a Power Automate demo) for HR teams
(Tue 17 to Thu 19 November 2026, 09:00-15:00, CODED, Alsharekh room, Frontend Campus). Cohort AIFHR-Nov/Nov-26.

## How this repo works

- Everything in `public/` is generated. Edit the kit in `_source/kit/`, then run `bash _source/build/build.sh`.
  The last step (`validate_site.py`) must print `PROBLEMS: 0`.
- `_source/build/` is the CODED workshop engine. Never edit an engine file. Kit-only changes.
- `_source/kit/data.py` holds every fact (names, numbers, planted errors). `content.py` and `content_demos.py` hold the words.
  `build_deck.py` orders the slides. `gen_files.py` writes the 31 sample files into `_source/files/`.
- Survey payloads: `build.sh` runs `surveys.py`, which overwrites them. Always run `python3 _source/surveys/patch.py` after a build
  (it is safe to run more than once), then push the patched payloads to the portal drafts.
- A push to `main` redeploys production on Vercel.

## Rules

- Plain English for Gulf ESL readers (CEFR B2), American spelling, no em or en dashes.
- Fictional data only. The company is "Mutla Oil Company". Never use a real client's name on practice data.
- Participant pages give hints, never answers. Answers live only under `/staff` (password protected) and in the portal descriptions.
- Public pages never link to `/staff`. The whole site is `noindex`.
- Never hand-edit `public/`. Never push staff answers anywhere else.
- Every Copilot task must work in Copilot Chat (free, with file upload). In-app steps (Word, Outlook, Teams, Excel, PowerPoint) are
  shown as demos for people with the Microsoft 365 Copilot license, with a Chat fallback for everyone else.
- The habit: "Copilot drafts. You check. Authorized HR staff decide."
- Never choose, store or print the staff password. It is set by hand in Vercel as `STAFF_PASSWORD`.

## Decisions

1. Approval: Aya approved the handoff on 9 Nov 2026 with "Approve and ship when every check passes". That approval is also the
   confirmation to create and update the three portal survey drafts.
2. Title "AI Fundamentals for HR" (the portal product name), not "AI Essentials for Modern HR" from the outline.
3. Brand: CODED only. An open workshop run because of KOC demand. No client logo, no client name on any page or file.
4. Cohort: AIFHR-Nov/Nov-26 (17 to 19 Nov). The earlier AIHR cohort (10 to 12 Nov) is on hold and not used.
   The portal lists another trainer on the cohort; Aya teaches it. Update the cohort in the portal if needed.
5. The practice company is Mutla Oil Company, an oil and gas company with five HR unit tracks: Job Evaluation and Salary Scaling,
   Compensation, Manpower, Personnel and Administration, Learning and Development.
6. (Replaced by Decision 24.) The four-point review: Accuracy, Confidentiality, Neutrality, Source alignment.
7. The portal model surveys from other teams could not be read (not_found_or_denied). The surveys were built from the
   builder's bundled standards and the engine payloads, then patched for an open workshop by `_source/surveys/patch.py`
   (company field, q_4/q_5 ids, q_ai, q_safe and the 0 to 10 recommend item).
8. Portal theme, intro and closing screens cannot be set by the tools. They keep the portal defaults until set by hand.
9. Excel analysis stays at "summarize and check every figure". Trends and dashboards belong to the separate HR data program.
10. Recruitment appears once, at a high level, on Day 2.
11. Agent Builder may be off on some accounts. The fallback is the same instructions pasted into Copilot Chat with the files uploaded.
12. QA round 1 fixes (9 Nov 2026): MAP q11 and q12 were re-stemmed as work moments, q1 and q11 got more believable wrong options,
    and the Arabic options were rebalanced. The approval to ship covers QA fixes; the answer key letters did not change.
13. Card sort timing is 8 minutes, set by the engine's sort slide; the lesson plan says 8 (the handoff said 7).
14. Task 3.3 runs 100 minutes in two parts: 25 before lunch (slide e3task) and 75 after (slide e4build).
15. Day 2 has 64 slides after adding Demo 2.1b (compare two versions) and Demo 2.3b (a timeline, not a verdict).
    Day 1 has 61 slides after adding Demo 1.2b (redact, then ask).
16. The capstone trainer names are labels (Trainer A to D), so the insult planted in the L&D file is not tied to a realistic name.
17. QA round 2 fixes: MAP q1, q4, q10 and q13 got fresh scenarios so no stem repeats a public slide (answer letters unchanged).
    The HR assistant's knowledge holds both allowance versions (v3 until 31 December 2026, v4 from 1 January 2027), five files in all.
18. After every build, run `python3 _source/surveys/patch.py`: the engine rewrites the payloads to the unpatched form.
    The patched counts are PRE 24, POST 24, final 25 questions, and they equal the portal drafts.
19. QA round 3 fixes: MAP q6, q7, q8 and q13 got fresh scenarios (same answer letters) so no stem or option repeats a Day 2 slide.
    The Task 3.3 card on the Day 3 page shows the 100-minute total; the deck runs it as 25 + 75 minutes (title "in two parts").
20. QA round 4 fixes: MAP q1 (option a), q7 (Safety Officer), q8 (the Eid holiday notice) and q11 (Personnel reminders) changed,
    same answer letters. The 2019 job description is for an HR Officer, matching its file name.
21. QA round 5 (the last allowed round) failed on MAP tests (7.0); overall 9.60, no Blocking finding. The build was not shipped.
    After round 5: MAP q8, q9 and q10 changed (same letters; q10 uses MAP_Q10 247 vs 239), b1chk1 and b2chk2 rewritten,
    b1t3 and b1lic name the M365 Copilot (Premium) label. These fixes are not yet audited.
22. After round 5, Aya chose "Ship now as it is" (9 Nov 2026): the three surveys are published and the site deployed with the
    round 5 fixes, without a sixth audit.
23. 16 Nov 2026: the outline is now the public program page (PDF "AI Fundamentals for HR: Using Copilot and Power Automate").
    Aya approved a plan with two changes from it: protecting employee data and the green, amber, red triage move to the
    start of Day 2; Day 3 builds agents in Agent Builder, and Power Automate is a trainer demo, not a build.
24. The prompt checklist replaces the five inputs: Role, Context, Task, Data, Constraints, Tone, Output format
    (the outline's own words). Microsoft's Goal, Context, Source, Expectations map onto it (data.py GCSE).
25. Aya's content rules (16 Nov 2026) apply to every change: live demos only (no prompt-player slides), speaker notes written
    as scripts with stage directions in brackets, two exercises per build block, tool comparisons at the end of a day,
    a welcome slide about CODED and the trainer, "DRAFT · Reviewed by: ___" on outputs, nothing printed.
26. Engine changes for three-layer hints, no "Your turn" on day pages and COPY on the project page wait for Aya's OK.
    The Day 1 lab already holds `hints` and `prompt` fields for that change; the engine shows the first hint today.
27. The MAP has 14 questions: Day 1 six, Day 2 four, Day 3 four (q11 moved to Day 3 on 16 Nov). Answer key in content.py (MAP_KEY). PRE and POST in the
    portal are updated only after Aya confirms the change.
28. 16 Nov 2026: Days 2 and 3 rebuilt (round B). Day 2: safe data first, meetings, follow-ups, Excel, summary and slides, then
    process maps (Tasks 2.1 to 2.12). Day 3: two agents in Agent Builder, a trainer-only Power Automate demo, the final project
    (Tasks 3.6 and 3.7) and Copilot, agent or flow. Slides: Day 1 64, Day 2 57, Day 3 40. The Day 3 lab is the Final project page.
    The engine changes in Decision 26 are approved and in place. The final project submission form in the portal is not created
    yet: until it exists, the page says the trainer shares the link (`PROJECT_SUBMIT` in content.py).
29. 16 Nov 2026 (round C, Aya): the prompt checklist has five parts (Context, Task, Data, Constraints, Format); `five()` in
    content_demos.py folds Role into Context and Tone plus Output format into Format, so the request words do not change.
    Day 2 is "Meetings, Reporting and Presentations" (PowerPoint gets Block 6); the workflow mapping moved to Day 3, Block 4
    ("HR Agents, Workflows and an Introduction to Power Automate"). The final project is optional (Task 3.8), agents only.
    Slides: Day 1 69, Day 2 55, Day 3 46. The Power Automate demo is a recorded video: a placeholder until Aya asks to build
    and film the flow, after Copilot access is fixed with the CODED admin team.
30. Survey access: yousif.d@, moudhi@, ahmadmaher@ and ghareeb@joincoded.com are invited to PRE, POST and the final survey.

