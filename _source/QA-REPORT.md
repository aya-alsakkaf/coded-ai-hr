# QA report: AI Fundamentals for HR

## Round 1 · FAIL (four dimensions under 9.0)

Levels 1 to 4 run by the builder with `validate_site.py` and `qa.cjs`. Levels 5 to 8 run by a fresh agent that did not build the site
(full findings in `_source/qa-round1-levels-5-8.md`).

| Dimension | Score |
| --- | --- |
| Files, links and config | 10 |
| Pages | 9.75 (one hub chip ran past its border) |
| Decks | 10 |
| Interactivity | 10 |
| Content coherence | 2.75 |
| Tasks and demos | 3.75 |
| MAP tests | 5.0 |
| Final survey | 7.75 |
| Language and data safety | 9.25 |

No Blocking finding. Fixes made for round 2: three Copilot license labels, Excel works on saved local files, Prompt Gallery and Try it
wording, quick checks rewritten so no MAP question copies a public check, right answers spread across A, B and C, capstone part 1 timer
(25 minutes), Task 3.2 date rule and the outline's extra, the compensation case salary floor, two new demos (compare two versions,
timeline not verdict), planted thread and evidence items listed in the keys, story times, idioms, fictional trainer labels,
an idempotent `patch.py` with no client name, and "workshop" in the final survey.

## Round 2 · FAIL (four dimensions under 9.0)

Levels 1 to 4: validator PROBLEMS: 0, `qa.cjs pages` and `qa.cjs decks` 0 problems. Levels 5 to 8 by a second fresh agent
(`_source/qa-round2-levels-5-8.md`): Content coherence 5.75 · Tasks and demos 8.25 · MAP tests 6.25 · Final survey 9.75 ·
Language and data safety 8.0. No Blocking finding; 7 Concerning, 20 Nits.

Fixes made for round 3: Copilot Chat can search the web (b1t1) and the Basic label wording (b1t3); quick-check option lengths
rebalanced (the right answer is now never the longest); the HR assistant's knowledge holds both allowance versions with their dates;
b3chk and c3chk2 rewritten so they no longer mirror MAP q5 and q9; MAP q1, q4, q10 and q13 re-stemmed with fresh facts (same answer
letters); the client name removed from the staff lesson plan; Demo 1.2b (redact, then ask) added; the Nits on stories, files, notes,
labels, wording and the MAP section note fixed.

## Round 3 · FAIL (two dimensions under 9.0)

Levels 1 to 4: validator PROBLEMS: 0 (after shortening the agent instructions), `qa.cjs pages` and `qa.cjs decks` 0 problems.
Levels 5 to 8 by a third fresh agent (`_source/qa-round3-levels-5-8.md`): Content coherence 8.0 · Tasks and demos 9.0 ·
MAP tests 7.25 · Final survey 9.75 · Language and data safety 9.25. Overall 9.14. No Blocking finding; 3 Concerning, 15 Nits.

Fixes made for round 4: the Copilot Chat (Basic) and M365 Copilot (Basic) labels told apart on b1t3, b1lic and the Day 2 notes;
c1chk1 (vacancy text), c1chk2 (the parking note) and c2chk (the line-manager version) rewritten; MAP q6, q7, q8 and q13 given
fresh scenarios and options (same letters); quick checks now have the right answer longest in 5 of 28; c3chk2 moved next to c3chk1;
file lists for Tasks 1.4, 2.6 and 3.3; "five policy files" everywhere; the Demo 2.2 reply prompt; the hub demo count; wording Nits.
Survey payload counts after `patch.py`: PRE 24, POST 24, final 25 (written to the end of `build-log.txt`).

## Round 4 · FAIL (MAP tests under 9.0)

Levels 1 to 4: validator PROBLEMS: 0 (re-run after `patch.py`: PROBLEMS: 0), `qa.cjs pages` 0 problems, `qa.cjs decks` 0 problems
(logs in `_source/qa-pages-r4.txt`, `_source/qa-decks-r4.txt`). Files 10 · Pages 10 · Decks 10 · Interactivity 10.
Levels 5 to 8 by a fourth fresh agent (`_source/qa-round4-levels-5-8.md`): Content coherence 9.25 · Tasks and demos 9.5 ·
MAP tests 7.25 · Final survey 9.75 · Language and data safety 9.75. Overall 9.49 (9.4875). No Blocking finding; 2 Concerning, 10 Nits.
Round 3 status: 14 fixed, 1 fixed as recorded (Decision 19), 3 partly fixed.

Fixes made for round 5: MAP q1 option a (a cause the deck shows is false), q8 on a new notice (the Eid holiday notice, no cue in the
stem), q7 on a job in no file (Safety Officer), q11 on another unit and task (same letters, Arabic mirrored); b1chk1 and e0chk1
distractors changed; SEGMENTS for Day 1 Block 2 and Day 2 Blocks 1 and 3 follow the deck order (same totals); the 2019 job
description is an HR Officer; e3story says 100 minutes; Demo 2.2 has an expected reply and a backup; the Normal test has a pass
condition; the final survey intro names the 0 to 10 item; the Task 2.1 hint wording.

## Round 5 · FAIL (MAP tests under 9.0) · the last allowed round

Levels 1 to 4: validator PROBLEMS: 0, `qa.cjs pages` 0 problems, `qa.cjs decks` 0 problems (`_source/qa-pages-r5.txt`,
`_source/qa-decks-r5.txt`). Files 10 · Pages 10 · Decks 10 · Interactivity 10.
Levels 5 to 8 by a fifth fresh agent (`_source/qa-round5-levels-5-8.md`): Content coherence 9.5 · Tasks and demos 10 ·
MAP tests 7.0 · Final survey 10 · Language and data safety 10. Overall 9.60. No Blocking finding; 2 Concerning (MAP q9, q10), 6 Nits.
Round 4 status: 10 fixed, 2 partly fixed (q8 word cue, b1chk1 frame).

The QA loop stops after 5 rounds, so the build was not shipped. Fixes made after round 5, not yet audited: MAP q9 (lines of a draft
to judge), q10 (another person, system and numbers, 247 vs 239), q8 (no "date" cue); b1chk1 (what you check before you reply),
b2chk2 (which detail can stay); b1t3 and b1lic name the M365 Copilot (Premium) label as the Microsoft 365 Copilot license and stop
listing Outlook as a data source; Demo 2.2 names "Summary by Copilot". Same answer letters. Portal drafts updated to match.

Ship decision: after round 5, Aya chose to ship the build with the round 5 fixes, without a sixth audit (9 Nov 2026).

## Level 9 · Live (9 Nov 2026, https://coded-ai-hr.vercel.app) · PASS

- `/` 200 (the hub), with the robots meta tag and `X-Robots-Tag: noindex, nofollow`.
- `/slides1` follows to the Day 1 deck: 200, 61 slides, noindex. `/prompt-sheet-day-3` and `/take-home-guide` (old kit addresses) follow to their pages: 200.
- `mutla-hr-trackers-q3-2026.xlsx` 200 with the spreadsheet content type.
- `/pre`, `/post` and `/survey` 307 to the published portal forms.
- `/staff` 503 "Staff pages are locked" until STAFF_PASSWORD is set in Vercel.
- `/_source/HANDOFF.md` 404 with the branded page.
