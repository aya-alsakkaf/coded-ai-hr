# Changelog

## 17 November 2026 · App features on Day 2, file descriptions

- Four new fictional files: `mutla-overtime-export-oct-2026.xlsx` (40 claims with six kinds of cleaning problem and approved
  totals), `mutla-overtime-memo-draft.docx` (a long memo with two rules that differ from the approved rules in its annex),
  `mutla-hr-quarterly-report-q3-2026.docx` (three pages, nine sections) and `mutla-q3-hr-update-messy.pptx` (nine slides, eight
  planted problems). 34 sample files.
- Excel: Demo 2.6 adds a check chart; Task 2.7 is payroll or clean, chart and check the overtime export. Word: Demo 2.8 shows
  Rewrite; Task 2.9 is three lines, rewrite the memo, or summarize the report. PowerPoint: Demo 2.10 and Task 2.10 compare a deck
  from a prompt with one from a document; Task 2.11 is fix the messy deck or your track's slides. Block 6 timings adjusted.
- Every file has a description (`FILE_ABOUT`). Lab steps start with it; Day 2 and Day 3 working files open with an "About this
  file" box or sheet. Day 1 files and agent knowledge files are byte for byte the same.
- Day 2 lab: one step per option (16 steps). Day 3: the second-agent notes now cover both choices. A few Day 2 and 3 lines reworded.

## 16 November 2026 · Day 1 wording pass (humanizer)

- Day 1 slides and speaker notes rewritten in plainer words: fewer slogans and "not X but Y" lines, no dramatic fragments
  ("Same tool. Same role." is now "One role, two requests"). Facts, timings, prompts and answers did not change.
- The Day 1 wrap and closing slide no longer promise a process map tomorrow (it moved to Day 3). The Day 1 lab hint for
  Task 1.2 starts from Context, not Role.

## 16 November 2026 · Aya's evening changes (round C)

- The prompt checklist has five parts, not seven: Context (who you are, who reads it, why), Task, Data, Constraints, Format.
  Role sits inside Context; Tone and Output format are one Format. Every request, slide, lab step, cheat sheet line and the
  MAP confidence item follow it. MAP q4 options reworded (answer still d).
- Day 1, Block 1 now opens with who used AI this week, what AI is, AI people already use (spam filter, face unlock, maps,
  fraud alerts), where LLMs fit (AI, machine learning, LLMs) and what LLM stands for, then the 30-day story and prediction.
  69 slides. Task 1.1 runs 10 minutes.
- Day 2 is now Meetings, Reporting and Presentations. The old way and the AI way (one slide after the callback).
  Task 2.7 is the payroll cross-check (October against November and the approved movements; employee codes only; three
  planted items). Block 5 is Word (a summary, then three lines for the HR team). Block 6 is PowerPoint (a deck from a
  document, a deck edited in rounds, slides for your track's meeting). 55 slides.
- Day 3 is now HR Agents, Workflows and an Introduction to Power Automate. Task 3.4 is a choice: the Job Description Coach
  or the new Onboarding Buddy. The workflow mapping moved here from Day 2 (Block 4, 12:15) with Task 3.8, an optional
  improvement marked Person, Copilot or Agent only. The Power Automate demo is a recorded video; the slide holds a
  placeholder until it is recorded. 46 slides.
- New sample files: mutla-payroll-check-oct-nov-2026.xlsx and mutla-onboarding-checklist-2026.docx (30 files).
- Portal (with Aya's OK): PRE, POST and the final survey reworded for the five parts; Day 2 and Day 3 section titles renamed;
  MAP q11 moved to the Day 3 section (6, 4, 4). Yousif, Moudhi, Ahmad Maher and Ghareeb invited to all three surveys.

## 16 November 2026 · Days 2 and 3 rebuilt to the updated outline (round B)

- Day 2 rewritten: Meetings, Reporting and Mapping Your HR Workflow. Protecting employee data first (green, amber, red card sort;
  redact, then ask); a meeting prepared and recapped into actions; a follow-up and a reminder in Outlook; two Excel figures checked
  against a control total; a management summary and five slides; the four workflow problems and a process map; each participant
  maps one HR process. Ends with "which app for which job". 57 slides, Tasks 2.1 to 2.12, two exercises per build block.
- Day 3 rewritten: HR Agents and an Introduction to Power Automate. The Mutla HR Policy Helper written with the prompt checklist,
  built in Agent Builder and tested three ways; a second agent (Mutla Job Description Coach); a trainer-only Power Automate demo
  (Forms, Excel log, approval, condition, email) with why a flow and not Copilot or an agent; the final project (improve the Day 2
  map, build and test one piece, submit); Copilot, agent or flow side by side with a card sort. 40 slides, Tasks 3.1 to 3.7.
- New sample files: mutla-process-stories.docx (five as-is processes, one per track), mutla-process-map-template.docx,
  mutla-workflow-card-template.docx (with a filled-in example) and mutla-training-request-log.xlsx (table TrainingRequests).
- Removed sample files no longer taught: the evidence notes, the investigation notes, the five capstone cases and the peer-test input.
  The case files now name Tasks 2.2 and 2.5. The catch-up bank swaps the four-point review request for "flag, do not fix".
- The Day 2 lab has one step per task; the Day 3 lab is the Final project page (the agent steps, then six project steps,
  the track options and the example card).
- Engine (approved 16 Nov): three-layer hints on lab pages, COPY templates on lab steps, lab names, and `DAY_NO_TASKS`
  (no "Your turn" list on day pages). Logged in PLUGIN-FEEDBACK.md.
- The MAP questions did not change. The portal survey titles for Days 2 and 3 already match.

## 16 November 2026 · Day 1 rebuilt to the updated outline (round A)

- The outline changed to the public program page "AI Fundamentals for HR: Using Copilot and Power Automate" (PDF, 16 Nov).
  Aya approved a plan on top of it: data protection moves to Day 2; Day 3 builds agents in Agent Builder and shows
  Power Automate as a trainer demo only (CLAUDE.md, Decisions 23 to 27).
- Day 1 rewritten: Copilot Foundations for HR Documents and Communication. Welcome slide about CODED and the trainer;
  how generative AI and Copilot work, with what stays with people; the prompt checklist (role, context, task, data,
  constraints, tone, output format); follow-up instructions and the source trace; a job description and an experience
  letter in Word; a policy summary and one announcement for three readers in Outlook; the Prompt Bank. 64 slides, Tasks 1.1 to 1.6.
- Every Day 1 demo runs live in Copilot (no prompt-player playback). Notes are trainer scripts with stage directions in brackets.
- New sample file: mutla-experience-letter-requests.docx (template, HR system record, three requests, two planted problems).
- The Day 1 lab is now one step per task, with hints, the files under each step and a check.
- The 14 MAP questions and the 6 confidence items are rewritten for the new three days (key in content.py, MAP_KEY).
  The portal PRE and POST tests are updated only after Aya confirms.
- Days 2 and 3 are unchanged in this round. They are rebuilt next.

## 9 November 2026 · First build

- Built from the approved handoff (`_source/HANDOFF.md`) for the outline "AI Essentials for Modern HR", run as
  **AI Fundamentals for HR** (CODED only, open workshop, cohort AIFHR-Nov/Nov-26, 17 to 19 November 2026).
- Site: workshop home, three day pages, three decks (61, 64 and 40 slides), three prompt sheets, three labs, cheat sheet,
  safe-use card, take-home guide, 31 fictional Mutla Oil Company sample files, and 18 staff pages under `/staff`.
- CODED portal drafts: MAP Test PRE (Day 1), MAP Test POST (Day 3) and the final satisfaction survey, all bilingual,
  linked to the cohort and filed in the workshop folder. The payloads are patched for an open workshop by `_source/surveys/patch.py`.
- QA rounds 1 to 3 failed and were fixed in the kit (see `_source/QA-REPORT.md` and `_source/qa-round*-levels-5-8.md`):
  product facts on the three Copilot license labels, MAP questions re-stemmed so no stem or option repeats a public slide,
  quick checks rebalanced, the HR assistant given both allowance versions, the capstone run as 25 + 75 minutes, and wording fixes.
- QA rounds 4 and 5 fixed in the kit. Round 5 scored 9.60 overall with MAP tests at 7.0, so the QA loop did not pass.
  Aya chose to ship with the round 5 fixes (CLAUDE.md, Decision 22).
- Shipped: the three surveys published in the portal, the repo pushed to GitHub (aya-alsakkaf/coded-ai-hr) and deployed on Vercel
  at https://coded-ai-hr.vercel.app. Every live check passed (`_source/QA-REPORT.md`, Level 9).
