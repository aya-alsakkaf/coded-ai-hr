# Plugin feedback (coded-workshop-builder)

Notes for the plugin owners from this build. Nothing here blocks the workshop.

1. **Final survey payload.** The engine's `surveys.py` writes the final survey with `q_dept`, `q_can1` and `q_can2`, and without
   `q_ai`, `q_safe` or a 0 to 10 recommend item. `references/surveys.md` asks for `q_company` (open workshop), `q_4`/`q_5`,
   `q_ai`, `q_safe` and `q_nps`. This build patches the payload with `_source/surveys/patch.py`. Suggest: add these to the engine.
2. **Re-running `surveys.py` overwrites the patched payloads.** A kit hook (for example `SURVEY["patch"]`) would avoid the second step.
3. **Model surveys are not readable.** `survey_get` on the newest MAP tests and final surveys from other teams returned
   `not_found_or_denied`. The skill says to read them first. Suggest: bundle one current MAP test and one final survey JSON in the plugin.
4. **Portal screens.** The intro and closing screens and the theme colors cannot be set through `survey_update`
   (the defaults are green `#00D46A` and "We'd love to hear from you"). They must be set by hand. Suggest: expose them in the tool.
5. **GitHub.** The session's `gh` token could not create a repo, so the approval asked Aya to create the empty private repo first.
6. **Licensing variance.** HR teams often have a mix of Copilot Chat (free) and Microsoft 365 Copilot (paid). The kit has no field
   for "this demo needs the paid license". This build writes it into the demo text and gives a Chat fallback on every task.
7. **Sort slide timer.** `deck.sortslide` hardcodes 8 minutes (`dur=480`). A `minutes` argument would let a kit match its lesson plan.
8. **Task timer per part.** `deck.task` takes its timer from the task's total minutes. A task split around lunch needs a `minutes`
   override; this kit sets the value for one call and restores it.
9. **Engine change, approved by Aya on 16 Nov 2026 (`_source/build/pages.py`).** Lab steps take `hints` (shown in layers: a hint,
   another hint, then the step's `prompt` with COPY), `templates` [(label, text)] with COPY, and the lab takes `name` and `lede_html`.
   `DAY_NO_TASKS = True` hides the "Your turn" list on day pages. Old kits keep their behavior. Suggest: fold these into the engine.
10. **Task slide with a custom title.** `deck.task(..., title=...)` adds the title to the kit words twice (once as `title`, once as
    `ttl`), so the validator reports "kit words missing on the site". This kit names its tasks so the default title reads well
    ("Your turn: payroll, or clean and chart."). Suggest: add the title to `kit` once.
11. **File descriptions on the site (waits for Aya's OK).** The day page lists every sample file as "Fictional file", and lab steps
    show only the file name. The kit now has `FILE_ABOUT` in `content_demos.py` (what it is, who uses it, where it is used). A small
    change in `pages.py` could show the first part under each file name. Until then the kit puts the description in the lab step
    text and in an "About this file" box inside the working files.
12. **Flaky contrast check.** `qa.cjs pages` sometimes reports one COPY button at 4.31:1 on a long lab page at 390 px; the same page
    passes on a second run. The button is white on #2F74D6 (4.57:1). It looks like a reveal animation caught mid-fade.

