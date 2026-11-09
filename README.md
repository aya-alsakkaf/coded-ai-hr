# AI Fundamentals for HR

The workshop site for **AI Fundamentals for HR**, a three-day CODED Professionals open workshop on Microsoft Copilot for HR teams.
Tue 17 to Thu 19 November 2026, 09:00-15:00, CODED, Alsharekh room, Frontend Campus. Trainer: Aya. Cohort: AIFHR-Nov/Nov-26.

Live site: https://coded-ai-hr.vercel.app

## Pages

| Short link | Page | Who |
| --- | --- | --- |
| `/` | Workshop home (all 3 days, MAP QR codes, files) | Participants |
| `/day1`, `/day2`, `/day3` | Day pages: run of show, outcomes, slides, prompt sheet, lab, files | Participants |
| `/slides1`, `/slides2`, `/slides3` | Slide decks (61, 64 and 40 slides). Arrows to move, F for full screen | Room |
| `/prompt-sheet-day-1` to `-3` | Every prompt of the day with COPY buttons | Participants |
| `/lab-day-1` to `-3` | Self-paced labs with done marks and checks | Participants |
| `/cheat-sheet`, `/safe-use-card`, `/take-home-guide` | Reference pages | Participants |
| `/staff` | Trainer index (password) | Trainers |
| `/lesson-plan`, `/facilitator-kit` | Lesson plan and facilitator kit (MAP answer key inside) | Trainers |
| `/presenter-notes-day-N` | Speaker notes per slide | Trainers |
| `/answer-key-day-N`, `/demo-runbook-day-N`, `/backup-outputs-day-N` | Answer keys, demo runbooks, backup outputs | Trainers |

The 31 fictional sample files (Mutla Oil Company) are served from the site root, for example `/mutla-leave-policy-2026.docx`.

## MAP tests and survey (CODED portal)

| Short link | Form | When |
| --- | --- | --- |
| `/pre` | [Pre-MAP test](https://platform.joincoded.com/sv/coded-ai-fundamentals-for-hr-map-test-pre-day-1) | Day 1 · Tue 17 Nov · 09:10 |
| `/post` | [Post-MAP test](https://platform.joincoded.com/sv/coded-ai-fundamentals-for-hr-map-test-post-day-3) | Day 3 · Thu 19 Nov · 14:20 |
| `/survey` | [Final satisfaction survey](https://platform.joincoded.com/sv/coded-ai-fundamentals-for-hr-final-satisfaction-survey) | Day 3 · Thu 19 Nov · 14:30 |

## Build

```bash
bash _source/build/build.sh          # sample files, decks, pages, staff pages, config, survey payloads, then the validator
python3 _source/class_plan.py        # CLASS-PLAN.md from the kit
```

The validator must print `PROBLEMS: 0`. Edit the kit in `_source/kit/` only; never edit `public/` or `_source/build/` (the engine).
See `CLAUDE.md` for the rules and decisions.

## Deploy

The repo is linked to Vercel (framework Other, no build command, output `public/` from `vercel.json`). A push to `main` deploys production.
The trainer pages under `/staff` need `STAFF_PASSWORD` in Vercel → Project → Settings → Environment Variables (Production), then a redeploy.
Without it, `/staff` stays locked.
