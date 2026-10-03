"""Validate that the premium portal links to the complete learner release."""
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
    "START_HERE.md", "READINESS_GUIDE.md", "DAY1_GUIDE.md", "DAY2_GUIDE.md",
    "DAY3_GUIDE.md", "DAY4_GUIDE.md", "DAY5_GUIDE.md", "COLAB_GUIDE.md",
    "GITHUB_GUIDE.md", "FAQ.md", "TROUBLESHOOTING.md", "LEARNING_RESOURCES.md",
    "GLOSSARY.md",
]
PROJECT = [
    "data/DATA_GUIDE.md", "TECHNICAL_REQUIREMENTS.md", "ADMINISTRATIVE_REQUIREMENTS.md",
    "COURSE_ALIGNMENT.md", "RUBRIC.md", "SUBMISSION_GUIDE.md", "FINAL_CHECK_GUIDE.md",
    "reports/DECISION_CARD_TEMPLATE.md", "reports/INTERPRETABILITY_REPORT_TEMPLATE.md",
    "reports/MODEL_CARD_TEMPLATE.md", "presentation/FINAL_PRESENTATION_TEMPLATE.md",
    "presentation/FINAL_PRESENTATION_GUIDE.md",
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
        issues.append("Student-template repository link is missing")
    if not ("github.com/new?template_name=sda-dsc-211-student-template" in lower_html or "/generate" in lower_html):
        issues.append("Use-template creation link is missing")

    for item in NOTEBOOKS + GUIDES + PROJECT:
        if item not in html:
            issues.append(f"Missing learner resource link: {item}")

    for signal in ("90", "10"):
        if signal not in html:
            issues.append(f"Assessment signal missing: {signal}")

    private_en = any(signal in lower_html for signal in ("submit privately", "private cohort channel", "private submission"))
    private_ar = any(signal in html for signal in ("القناة الخاصة", "التسليم الخاص", "سلّم عبر القناة الخاصة"))
    if not private_en or not private_ar:
        issues.append("Private submission route is not stated bilingually")

    if "not an official SDAIA account" not in html or "ليست حسابًا رسميًا لسدايا" not in html:
        issues.append("Bilingual SDAIA disclaimer is missing")
    if "Meaad Al-Marri" not in html or "ميعاد المري" not in html:
        issues.append("Instructor attribution is missing")
    if "System Architecture" not in html or "معمارية النظام" not in html:
        issues.append("Bilingual system architecture is missing")
    if "v1.1.0" not in notes:
        issues.append("Release notes do not identify v1.1.0")

    report = {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
        "required_notebooks": NOTEBOOKS,
        "required_guides": GUIDES,
        "required_project_and_governance": PROJECT,
        "student_entry_model": "one public portal plus one student repository template",
    }
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
