# -*- coding: utf-8 -*-
"""Validate the premium bilingual production portal using the Python standard library."""
from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class PortalParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.images: list[str] = []
        self.stylesheets: list[str] = []
        self.canonical = False
        self.hreflangs: set[str] = set()
        self.json_ld = False
        self.lang_dirs: list[tuple[str | None, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        if tag == "img" and values.get("src"):
            self.images.append(values["src"] or "")
        if tag == "link" and values.get("rel") == "stylesheet" and values.get("href"):
            self.stylesheets.append(values["href"] or "")
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = True
        if tag == "link" and values.get("hreflang"):
            self.hreflangs.add(values.get("hreflang") or "")
        if tag == "script" and values.get("type") == "application/ld+json":
            self.json_ld = True
        if tag in {"article", "div", "section"} and (values.get("lang") or values.get("dir")):
            self.lang_dirs.append((values.get("lang"), values.get("dir")))


def local_target(root: Path, href: str) -> Path | None:
    if not href or href.startswith(("#", "mailto:", "tel:")):
        return None
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    return (root / parsed.path).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    index = root / "index.html"
    stylesheet = root / "student-hub.css"
    issues: list[str] = []
    html = index.read_text(encoding="utf-8") if index.is_file() else ""
    css = stylesheet.read_text(encoding="utf-8") if stylesheet.is_file() else ""

    if not html:
        issues.append("index.html is missing or empty")
    if not css:
        issues.append("student-hub.css is missing or empty")

    portal = PortalParser()
    portal.feed(html)

    required_ids = {
        "main", "overview", "start", "journey", "project",
        "requirements", "assessment", "submission", "support", "architecture",
    }
    missing_ids = sorted(required_ids - portal.ids)
    if missing_ids:
        issues.append(f"Missing required section ids: {missing_ids}")

    required_assets = ["assets/meaad-logo.png", "student-hub.css"]
    for relative in required_assets:
        if not (root / relative).is_file():
            issues.append(f"Required portal asset is missing: {relative}")

    required_signals = [
        "Advanced Machine Learning Methods",
        "System Architecture",
        "SDA-DSC-211",
        "90",
        "10",
        "Notebook 99",
        "Meaad Al-Marri",
        "private cohort channel",
    ]
    for signal in required_signals:
        if signal.lower() not in html.lower():
            issues.append(f"Required portal signal is missing: {signal}")

    if "assets/meaad-logo.png" not in portal.images:
        issues.append("The supplied MEAAD logo is not used in the page")
    if "student-hub.css" not in portal.stylesheets:
        issues.append("The production stylesheet is not linked")
    if 'dir="ltr"' not in html or 'dir="rtl"' not in html:
        issues.append("Explicit LTR and RTL content is required")
    if not portal.canonical:
        issues.append("Canonical link is missing")
    if not {"ar", "en"}.issubset(portal.hreflangs):
        issues.append("Arabic and English hreflang links are required")
    if not portal.json_ld:
        issues.append("Course JSON-LD is missing")
    if "not an official SDAIA account" not in html:
        issues.append("The non-official SDAIA disclaimer is missing")
    if "prefers-reduced-motion" not in css:
        issues.append("Reduced-motion support is missing")
    if "@media(max-width" not in css.replace(" ", ""):
        issues.append("Responsive breakpoints are missing")

    missing_local: list[str] = []
    for href in portal.links + portal.images + portal.stylesheets:
        target = local_target(root, href)
        if target is not None and not target.exists():
            missing_local.append(href)
    if missing_local:
        issues.append(f"Missing local targets: {sorted(set(missing_local))}")

    report = {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
        "required_section_ids": sorted(required_ids),
        "found_section_ids": sorted(portal.ids),
        "links_checked": len(portal.links),
        "images_checked": len(portal.images),
        "stylesheets_checked": len(portal.stylesheets),
        "local_missing": sorted(set(missing_local)),
        "canonical": portal.canonical,
        "hreflangs": sorted(portal.hreflangs),
        "json_ld": portal.json_ld,
        "ltr_rtl_pairs_detected": len(portal.lang_dirs),
        "logo_path": "assets/meaad-logo.png",
    }
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
