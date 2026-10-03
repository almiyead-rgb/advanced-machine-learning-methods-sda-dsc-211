"""Validate static delivery, crawlability and responsive QA assets for the course portal."""
from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

BASE_URL = "https://almiyead-rgb.github.io/advanced-machine-learning-methods-sda-dsc-211/"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    issues: list[str] = []

    required = [
        "index.html",
        "student-hub.css",
        "assets/meaad-logo.png",
        "robots.txt",
        "sitemap.xml",
        "404.html",
    ]
    for item in required:
        path = root / item
        if not path.is_file():
            issues.append(f"Missing required delivery asset: {item}")
        elif path.stat().st_size == 0:
            issues.append(f"Empty delivery asset: {item}")

    index = (root / "index.html").read_text(encoding="utf-8") if (root / "index.html").is_file() else ""
    css = (root / "student-hub.css").read_text(encoding="utf-8") if (root / "student-hub.css").is_file() else ""
    robots = (root / "robots.txt").read_text(encoding="utf-8") if (root / "robots.txt").is_file() else ""
    not_found = (root / "404.html").read_text(encoding="utf-8") if (root / "404.html").is_file() else ""

    if BASE_URL not in index:
        issues.append("Canonical course URL is missing from index.html")
    if f"{BASE_URL}sitemap.xml" not in robots:
        issues.append("robots.txt does not reference the canonical sitemap")
    if "User-agent: *" not in robots or "Allow: /" not in robots:
        issues.append("robots.txt does not explicitly allow crawling")
    if "assets/meaad-logo.png" not in not_found:
        issues.append("404 page does not use the MEAAD identity asset")
    if "Page not found" not in not_found or "الصفحة غير موجودة" not in not_found:
        issues.append("404 page is not bilingual")

    sitemap_path = root / "sitemap.xml"
    if sitemap_path.is_file():
        try:
            tree = ET.parse(sitemap_path)
            namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            locations = [node.text for node in tree.findall("sm:url/sm:loc", namespace)]
            if BASE_URL not in locations:
                issues.append("Canonical course URL is missing from sitemap.xml")
        except ET.ParseError as exc:
            issues.append(f"Invalid sitemap.xml: {exc}")

    responsive_signals = [
        "@media(max-width:1180px)",
        "@media(max-width:850px)",
        "@media(max-width:620px)",
        "prefers-reduced-motion",
        "overflow-wrap:anywhere",
    ]
    for signal in responsive_signals:
        if signal not in css:
            issues.append(f"Responsive/accessibility CSS signal is missing: {signal}")

    if re.search(r"width:\s*\d{4,}px", css):
        issues.append("A fixed four-digit pixel width was found in the production stylesheet")

    report = {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
        "required_assets": required,
        "canonical_url": BASE_URL,
        "responsive_signals": responsive_signals,
    }
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
