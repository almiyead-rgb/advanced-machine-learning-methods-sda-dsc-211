"""Validate that the portal exposes the simplified daily learner journey."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

NOTEBOOKS = [
    "00_readiness_check.ipynb",
    "01_baseline_boosting.ipynb",
    "02_validation_tuning.ipynb",
    "03_cost_sensitive_decision.ipynb",
    "04_explain_calibrate.ipynb",
    "05_final_model.ipynb",
    "99_final_submission_check.ipynb",
]
GUIDES = [
    "START_HERE.md",
    "DAILY_LEARNING_PATH.md",
    "EXPECTED_RESULTS.md",
    "GITHUB_GUIDE.md",
    "COLAB_GUIDE.md",
    "SUBMISSION_GUIDE.md",
    "FINAL_CHECK_GUIDE.md",
    "TECHNICAL_REQUIREMENTS.md",
    "ADMINISTRATIVE_REQUIREMENTS.md",
    "RUBRIC.md",
    "TROUBLESHOOTING.md",
]
FORBIDDEN = [
    "FINAL_PRESENTATION_TEMPLATE.md",
    "FINAL_PRESENTATION_GUIDE.md",
    "DECISION_CARD_TEMPLATE.md",
    "INTERPRETABILITY_REPORT_TEMPLATE.md",
    "MODEL_CARD_TEMPLATE.md",
    "90</strong><span>Project",
    "10</strong><span>Presentation",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    html = (root / "index.html").read_text(encoding="utf-8")
    notes = (root / "RELEASE_NOTES.md").read_text(encoding="utf-8-sig")
    lower_html = html.lower()
    issues: list[str] = []

    if "almiyead-rgb/sda-dsc-211-student-template" not in html:
        issues.append("Student repository link is missing")

    for item in NOTEBOOKS + GUIDES:
        if item not in html:
            issues.append(f"Missing learner resource link: {item}")

    required_signals = [
        "100", "80", "20", "70+", "Attendance", "الحضور",
        "Expected Results", "النتائج المتوقعة", "Daily Answer",
        "سؤال", "Submit privately", "القناة الخاصة",
        "System Architecture", "معمارية النظام",
        "No mandatory presentation", "لا يوجد عرض إلزامي",
    ]
    for signal in required_signals:
        if signal.casefold() not in html.casefold():
            issues.append(f"Missing daily-learning signal: {signal}")

    for signal in FORBIDDEN:
        if signal.casefold() in lower_html:
            issues.append(f"Obsolete template or assessment signal remains: {signal}")

    if "not an official SDAIA account" not in html or "ليست حسابًا رسميًا لسدايا" not in html:
        issues.append("Bilingual SDAIA disclaimer is missing")
    if "Meaad Al-Marri" not in html or "ميعاد المري" not in html:
        issues.append("Instructor attribution is missing")
    if "v1.1.0" not in notes:
        issues.append("Release notes do not identify v1.1.0")

    report = {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
        "required_notebooks": NOTEBOOKS,
        "required_guides": GUIDES,
        "learner_model": "daily Colab lab + expected result + one answer + same-day GitHub upload",
        "final_model": "one integrated project, Notebook 99, one formal grading cycle",
    }
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
