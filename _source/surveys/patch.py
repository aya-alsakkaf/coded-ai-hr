# Patches the engine's survey payloads to the open-workshop form in references/surveys.md (q_company, intro last line,
# day dates in the description, q_4/q_5, q_ai, q_safe, q_nps, "workshop" everywhere). Never served. See PLUGIN-FEEDBACK.md.
# Safe to run more than once: every change checks first. Run it after surveys.py:  python3 _source/surveys/patch.py
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(H, "..", "kit"), os.path.join(H, "..", "build")]
import content as C
L = lambda en, ar: {"en": en, "ar": ar}
DATES = {1: "Tue 17 Nov 2026", 2: "Wed 18 Nov 2026", 3: "Thu 19 Nov 2026"}
TITLES = {d: C.DAYS[d]["title"] for d in (1, 2, 3)}
INTRO_EN = " It is not graded: it shows us how much you learned in the workshop."
INTRO_AR = " لا يُحتسب هذا الاختبار في أي تقييم: إنه يبيّن لنا مقدار ما تعلّمته في ورشة العمل."

def load(n): return json.load(open(os.path.join(H, n + ".json")))
def save(n, p):
    t = json.dumps(p, ensure_ascii=False, indent=1)
    assert "—" not in t and "–" not in t and "KOC" not in t, n
    ids = [q["id"] for q in p["questions"]]; assert len(ids) == len(set(ids)), f"{n}: duplicate question ids"
    open(os.path.join(H, n + ".json"), "w").write(t)

def mapfix(name, sitting):
    p = load(name)
    p["sections"][0]["description"] = L("Please read this, then give us your name, work email and company so that we can match your two sittings.",
                                        "يُرجى قراءة ما يلي، ثم تزويدنا باسمك وبريدك الإلكتروني للعمل واسم شركتك لكي نطابق بين محاولتيك.")
    for q in p["questions"]:
        if q["id"] == "q_dept": q["id"] = "q_company"
        if q["id"] == "q_intro":
            if INTRO_EN.strip() not in q["label"]["en"]: q["label"]["en"] += INTRO_EN
            if INTRO_AR.strip() not in q["label"]["ar"]: q["label"]["ar"] += INTRO_AR
    FIC = L("Mutla Oil Company is a fictional company.", "شركة Mutla Oil Company شركة خيالية.")
    s3 = p["sections"][2]["description"]
    for k in ("en", "ar"):
        if FIC[k] not in s3[k]: s3[k] = s3[k] + " " + FIC[k]
    u = p["_update"]["brandingTitle"]
    u["en"] = u["en"].replace("MAP Test PRE", "MAP Test: PRE").replace("MAP Test POST", "MAP Test: POST")
    days = " · ".join(f"Day {d} ({DATES[d]}): {TITLES[d]}" for d in (1, 2, 3))
    p["description"] = (f"MAP Skills Test for the CODED Professionals open workshop \"{C.TITLE}\", 3 days, 17 to 19 November 2026, 09:00 to 15:00, CODED, Alsharekh room. "
                        f"{days}. {sitting} Part 1: 6 confidence self-ratings (never scored). Part 2: 14 knowledge questions (Day 1: 5, Day 2: 5, Day 3: 4). "
                        f"About 10 minutes. Not graded. Answer key: {C.MAP_KEY}.")
    save(name, p)

mapfix("pre", "PRE sitting: Day 1, Tue 17 Nov, 09:10, before teaching. The POST sitting (Day 3, Thu 19 Nov, 14:20) has the identical questions.")
mapfix("post", "POST sitting: Day 3, Thu 19 Nov, 14:20, before the final satisfaction survey. The PRE sitting (Day 1, Tue 17 Nov, 09:10) has the identical questions.")

# final survey: open-workshop ids, the two Copilot items, the 0 to 10 item, and the word "workshop" (feminine Arabic: ورشة العمل)
p = load("final")
scale6 = lambda: {"min": 1, "max": 6, "minLabel": L("Strongly disagree", "لا أوافق بشدة"), "maxLabel": L("Strongly agree", "أوافق بشدة")}
WORDING = {
 "q_2": L("The workshop met my expectations as a learning experience.", "لبّت ورشة العمل توقعاتي كتجربة تعليمية."),
 "q_1": L("I am satisfied with the workshop overall.", "أنا راضٍ عن ورشة العمل بشكل عام."),
 "q_pace": L("The length and pace of the 3 days were right for me.", "كانت مدة الأيام الثلاثة ووتيرتها مناسبة لي."),
 "q_10": L("I will use what I learned, and the tools from the workshop, in my work.", "سأطبّق ما تعلّمته والأدوات التي حصلت عليها في ورشة العمل في عملي."),
 "q_6": L("The instructor delivered the workshop effectively, and the teaching style was clear and easy to follow.", "قدّم المدرّب ورشة العمل بفعالية، وكان أسلوب التدريس واضحاً وسهل المتابعة."),
 "q_11": L("I would recommend this workshop to a colleague.", "أنصح زملائي بورشة العمل هذه."),
 "q_12": L("Which part of the 3 days was most useful to you, and why?", "ما الجزء الأكثر فائدة لك خلال الأيام الثلاثة، ولماذا؟"),
 "q_13": L("What would you change or add to make the workshop better?", "ما الذي تقترح تغييره أو إضافته لتحسين ورشة العمل؟"),
}
EXTRA = {
 "q_ai": {"id": "q_ai", "type": "scale", "label": L("I check Copilot's numbers and sentences before I use them.", "أتحقق من أرقام Copilot وعباراته قبل أن أستخدمها."), "required": True, "sectionId": "s_learn", "scaleConfig": scale6()},
 "q_safe": {"id": "q_safe", "type": "scale", "label": L("I know which data must never go into Copilot.", "أعرف البيانات التي لا يجوز إدخالها إلى Copilot أبداً."), "required": True, "sectionId": "s_learn", "scaleConfig": scale6()},
 "q_nps": {"id": "q_nps", "type": "scale", "label": L("How likely are you to recommend this workshop to a colleague?", "ما مدى احتمال أن تنصح زميلاً بورشة العمل هذه؟"), "required": True, "sectionId": "s_team",
           "scaleConfig": {"min": 0, "max": 10, "minLabel": L("Not at all likely", "غير محتمل إطلاقاً"), "maxLabel": L("Extremely likely", "محتمل جداً")}},
}
RENAME = {"q_dept": "q_company", "q_can1": "q_4", "q_can2": "q_5"}
out = []
NPS_NOTE = L(" The last recommend question uses 0 to 10.", " سؤال التوصية الأخير من 0 إلى 10.")
for q in [q for q in p["questions"] if q["id"] not in EXTRA]:
    q["id"] = RENAME.get(q["id"], q["id"])
    if q["id"] in WORDING: q["label"] = WORDING[q["id"]]
    if q["id"] == "intro":
        for k in ("en", "ar"):
            if NPS_NOTE[k].strip() not in q["label"][k]: q["label"][k] += NPS_NOTE[k]
    out.append(q)
    if q["id"] == "q_can6": out += [EXTRA["q_ai"], EXTRA["q_safe"]]
    if q["id"] == "q_11": out.append(EXTRA["q_nps"])
for i, q in enumerate(out): q["order"] = i
p["questions"] = out
p["description"] = (f"End-of-workshop satisfaction survey for the CODED Professionals open workshop \"{C.TITLE}\", 3 days (17 to 19 November 2026, CODED, Alsharekh room). "
                    "Taken at the end of Day 3 after the POST MAP test, about 5 minutes. Same 6-point agreement scale as other CODED programs (1 = Strongly disagree ... 6 = Strongly agree). Bilingual EN/AR.")
save("final", p)
print("patched: pre", len(load("pre")["questions"]), "· post", len(load("post")["questions"]), "· final", len(out), "questions")
