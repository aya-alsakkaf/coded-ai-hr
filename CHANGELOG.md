# Changelog

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
