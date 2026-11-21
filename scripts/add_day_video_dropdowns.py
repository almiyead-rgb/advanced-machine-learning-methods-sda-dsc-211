"""Add accessible daily video dropdowns to the student portal.

The video assignments mirror the verified catalogue maintained in the student
repository at resources/videos.yml. Native details/summary elements keep the
feature usable without JavaScript.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
CSS = ROOT / "student-hub.css"

DAY_VIDEOS = {
    1: [
        {
            "title_ar": "إنشاء مستودع GitHub للمشروع",
            "title_en": "Create your first GitHub repository",
            "url": "https://www.youtube.com/watch?v=-RZ03WHqkaY",
            "meta": "GitHub · 9:31 · Beginner",
            "note_ar": "مفيد قبل رفع ملفات اليوم الأول.",
        },
        {
            "title_ar": "البداية مع Google Colab",
            "title_en": "Get started with Google Colab",
            "url": "https://www.youtube.com/watch?v=inN8seMm7UI",
            "meta": "TensorFlow · 3:10 · Beginner",
            "note_ar": "تعرف على الخلايا وتشغيل Python في المتصفح.",
        },
        {
            "title_ar": "فكرة Gradient Boosting",
            "title_en": "Gradient Boosting main ideas",
            "url": "https://www.youtube.com/watch?v=3CC4N4z3GJc",
            "meta": "StatQuest · 15:52 · Intermediate",
            "note_ar": "ابنِ الفكرة قبل مقارنة نماذج التعزيز.",
        },
        {
            "title_ar": "XGBoost للتصنيف",
            "title_en": "XGBoost classification",
            "url": "https://www.youtube.com/watch?v=8b1JEDvenQU",
            "meta": "StatQuest · 25:17 · Intermediate",
            "note_ar": "راجع كيف تنتج الأشجار احتمال التصنيف.",
        },
    ],
    2: [
        {
            "title_ar": "فهم التحقق المتقاطع",
            "title_en": "Cross-validation fundamentals",
            "url": "https://www.youtube.com/watch?v=fSytzGwwBVw",
            "meta": "StatQuest · 6:04 · Intermediate",
            "note_ar": "اربط فكرة الطيات بقيود الزمن والعملاء ومنع التسرب.",
        },
    ],
    3: [
        {
            "title_ar": "ROC وAUC وعتبة القرار",
            "title_en": "ROC and AUC clearly explained",
            "url": "https://www.youtube.com/watch?v=4jRBRDbJemM",
            "meta": "StatQuest · 16:17 · Intermediate",
            "note_ar": "راجع أثر العتبة وPrecision–Recall في البيانات غير المتوازنة.",
        },
    ],
    4: [
        {
            "title_ar": "شرح SHAP من صاحب الطريقة",
            "title_en": "The science behind SHAP",
            "url": "https://www.youtube.com/watch?v=-taOhqkiuIo",
            "meta": "Microsoft Developer · 11:46 · Intermediate",
            "note_ar": "افهم إسهام الخصائص دون ادعاء السببية.",
        },
        {
            "title_ar": "المعايرة وعدم اليقين والقرار",
            "title_en": "Predictive uncertainty and calibration",
            "url": "https://www.youtube.com/watch?v=-gYnfA0e5ic",
            "meta": "PyData · 44:27 · Advanced · Optional",
            "note_ar": "محاضرة اختيارية تربط جودة الاحتمال بقرار العتبة.",
        },
    ],
    5: [
        {
            "title_ar": "تجميع Stacking للأحداث النادرة",
            "title_en": "Stacking ensembles for rare events",
            "url": "https://www.youtube.com/watch?v=6oD5K0x1k7c",
            "meta": "Enthought · 26:05 · Advanced",
            "note_ar": "قارن التجميع بالنموذج الفردي باستخدام أدلة OOF صادقة.",
        },
        {
            "title_ar": "فهم GitHub Actions والفحص النهائي",
            "title_en": "GitHub Actions for beginners",
            "url": "https://www.youtube.com/watch?v=BQrohJ3PT7I",
            "meta": "GitHub · 8:04 · Beginner",
            "note_ar": "تعرف على مكان تشغيل Final Project Check وقراءة النتيجة.",
        },
    ],
}

CSS_BLOCK = """

/* Daily video dropdowns | قوائم فيديوهات الأيام */
.video-dropdown{margin-top:1rem;border:1px solid var(--line);border-radius:.75rem;background:#fbf7ef;overflow:hidden}
.video-dropdown summary{display:flex;align-items:center;justify-content:space-between;gap:.65rem;cursor:pointer;list-style:none;padding:.75rem .85rem;font-weight:850;color:#5f4924;user-select:none}
.video-dropdown summary::-webkit-details-marker{display:none}
.video-dropdown summary:after{content:"⌄";font-size:1.15rem;line-height:1;transition:transform .18s ease}
.video-dropdown[open] summary:after{transform:rotate(180deg)}
.video-dropdown summary:focus-visible{outline:2px solid var(--gold);outline-offset:-2px}
.video-dropdown .video-count{margin-inline-start:auto;padding:.12rem .45rem;border-radius:999px;background:#ead9b6;color:#5f4924;font-size:.7rem}
.video-list{display:grid;gap:.55rem;padding:0 .7rem .75rem}
.video-link{display:grid;gap:.16rem;padding:.7rem;border:1px solid #e6d9c4;border-radius:.62rem;background:#fff;color:var(--ink);text-decoration:none}
.video-link:hover,.video-link:focus{border-color:#b99142;box-shadow:0 7px 18px rgba(55,44,28,.1);outline:2px solid var(--gold2);outline-offset:1px}
.video-link strong{font-size:.82rem;line-height:1.4}
.video-link small{color:#786f64;font-size:.7rem}
.video-link em{color:#6e5428;font-size:.72rem;font-style:normal;line-height:1.45}
@media(max-width:850px){.video-dropdown summary{padding:.7rem}.video-link{padding:.65rem}}
"""


def dropdown(day: int) -> str:
    videos = DAY_VIDEOS[day]
    links = []
    for video in videos:
        links.append(
            '<a class="video-link" target="_blank" rel="noopener noreferrer" '
            f'href="{video["url"]}">'
            f'<strong dir="rtl">{video["title_ar"]}</strong>'
            f'<strong>{video["title_en"]}</strong>'
            f'<small>{video["meta"]}</small>'
            f'<em dir="rtl">{video["note_ar"]}</em>'
            '</a>'
        )
    return (
        '<details class="video-dropdown">'
        '<summary><span>فيديوهات اليوم | Day videos</span>'
        f'<span class="video-count">{len(videos)}</span></summary>'
        f'<div class="video-list">{"".join(links)}</div>'
        '</details>'
    )


def update_index() -> bool:
    text = INDEX.read_text(encoding="utf-8")
    original = text
    for day in range(1, 6):
        pattern = re.compile(
            rf'(<article class="day-card day-{day}">.*?)(</article>)',
            re.DOTALL,
        )
        match = pattern.search(text)
        if not match:
            raise RuntimeError(f"Day {day} card was not found")
        segment = match.group(1)
        if 'class="video-dropdown"' in segment:
            continue
        text = text[: match.start()] + segment + dropdown(day) + match.group(2) + text[match.end() :]
    if text == original:
        return False
    INDEX.write_text(text, encoding="utf-8")
    return True


def update_css() -> bool:
    text = CSS.read_text(encoding="utf-8")
    if "/* Daily video dropdowns | قوائم فيديوهات الأيام */" in text:
        return False
    CSS.write_text(text.rstrip() + CSS_BLOCK + "\n", encoding="utf-8")
    return True


def main() -> int:
    changed = []
    if update_index():
        changed.append(str(INDEX.relative_to(ROOT)))
    if update_css():
        changed.append(str(CSS.relative_to(ROOT)))
    print("Updated:" if changed else "No changes required.")
    for path in changed:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
