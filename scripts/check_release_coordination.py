"""Validate that the bilingual portal links to the complete learner release."""
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
SUPPORT = [
    "START_HERE.md",
    "COLAB_GUIDE.md",
    "GITHUB_GUIDE.md",
    "FAQ.md",
    "TROUBLESHOOTING.md",
    "LEARNING_RESOURCES.md",
    "RUBRIC.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    html = (root / "index.html").read_text(encoding="utf-8")
    notes = (root / "RELEASE_NOTES.md").read_text(encoding="utf-8-sig")
    issues: list[str] = []

    if "almiyead-rgb/sda-dsc-211-student-template" not in html:
        issues.append("Student-template repository link is missing")
    for item in NOTEBOOKS:
        if item not in html:
            issues.append(f"Missing notebook link: {item}")
    for item in SUPPORT:
        if item not in html:
            issues.append(f"Missing support link: {item}")
    for signal in ("90", "10", "70", "95"):
        if signal not in html:
            issues.append(f"Assessment signal missing: {signal}")
    for signal in ("v1.1.0", "Notebook 99", "دفتر 99", "90", "10"):
        if signal not in notes:
            issues.append(f"Release-notes signal missing: {signal}")
    if "not an official SDAIA account" not in html or "ليست حسابًا رسميًا لسدايا" not in html:
        issues.append("Bilingual SDAIA disclaimer is missing")
    if "Meaad Al-Marri" not in html or "ميعاد المري" not in html:
        issues.append("Instructor attribution is missing")

    report = {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
        "required_notebooks": NOTEBOOKS,
        "required_support": SUPPORT,
    }
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
