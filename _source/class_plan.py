"""Write CLASS-PLAN.md at the repo root from the kit: days, blocks, tasks, minutes and points.
Run: python3 _source/class_plan.py   (from anywhere)"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, "kit"), os.path.join(HERE, "build")]
import content as C, content_demos as CD

out = [f"# Class plan: {C.TITLE}", "",
       f"{C.DATES} · {C.HOURS} · {C.VENUE}", "",
       "Generated from the kit (`_source/kit/content.py` and `content_demos.py`) by `_source/class_plan.py`. Do not edit by hand.", ""]
for n, d in C.DAYS.items():
    out += [f"## Day {n}: {d['title']}", "", d.get("claim", ""), "", "| Time | Block | What happens |", "| --- | --- | --- |"]
    for b in d["blocks"]:
        t, name, what = (list(b) + ["", "", ""])[:3]
        out.append(f"| {t} | {name} | {what} |")
    tasks = [(k, v) for k, v in CD.DEMOS.items() if str(v.get("day")) == str(n) and v.get("kind") == "task"]
    if tasks:
        out += ["", "**Tasks**", "", "| Task | Title | Minutes | Who | Files | Point |", "| --- | --- | --- | --- | --- | --- |"]
        for k, v in tasks:
            files = ", ".join(v.get("files") or [])
            out.append(f"| {v.get('card', k)} | {v['title']} | {v.get('minutes', '')} | {v.get('solo', '')} | {files} | {v.get('point', '')} |")
    out.append("")
open(os.path.join(HERE, "..", "CLASS-PLAN.md"), "w").write("\n".join(out).rstrip() + "\n")
print("CLASS-PLAN.md written")
