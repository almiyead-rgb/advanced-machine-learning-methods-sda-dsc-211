"""Validate the bilingual production portal with only Python standard library."""
from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class PortalParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.lang_dirs: list[tuple[str | None, str | None]] = []
        self.canonical = False
        self.hreflangs: set[str] = set()
        self.json_ld = False
        self._script_type: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        if tag in {"article", "div", "td"} and (values.get("lang") or values.get("dir")):
            self.lang_dirs.append((values.get("lang"), values.get("dir")))
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = True
        if tag == "link" and values.get("hreflang"):
            self.hreflangs.add(values.get("hreflang") or "")
        if tag == "script":
            self._script_type = values.get("type")
            if self._script_type == "application/ld+json":
                self.json_ld = True


def local_target(root: Path, href: str) -> Path | None:
    if not href or href.startswith(("#", "mailto:", "tel:")):
        return None
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return None
    clean = parsed.path
    if not clean:
        return None
    return (root / clean).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    index = root / "index.html"
    css = root / "bilingual-v1.1.css"
    issues: list[str] = []

    if not index.is_file():
        issues.append("index.html is missing")
        html = ""
    else:
        html = index.read_text(encoding="utf-8")
    if not css.is_file():
        issues.append("bilingual-v1.1.css is missing")

    portal = PortalParser()
    if html:
        portal.feed(html)

    required_ids = {"main", "overview", "journey", "assessment", "submission", "support"}
    missing_ids = sorted(required_ids - portal.ids)
    if missing_ids:
        issues.append(f"Missing required section ids: {missing_ids}")

    if 'href="bilingual-v1.1.css"' not in html:
        issues.append("index.html does not reference bilingual-v1.1.css")
    if 'dir="ltr"' not in html or 'dir="rtl"' not in html:
        issues.append("Explicit LTR and RTL columns are required")
    if "English" not in html and "Advanced Machine Learning Methods" not in html:
        issues.append("English content signal is missing")
    if "العربية" not in html and "أساليب تعلم الآلة المتقدمة" not in html:
        issues.append("Arabic content signal is missing")
    if not portal.canonical:
        issues.append("Canonical link is missing")
    if not {"ar", "en"}.issubset(portal.hreflangs):
        issues.append("Arabic and English hreflang links are required")
    if not portal.json_ld:
        issues.append("Course JSON-LD is missing")
    if "not an official SDAIA account" not in html or "ليست حسابًا رسميًا لسدايا" not in html:
        issues.append("The bilingual non-official SDAIA disclaimer is missing")
    if "prefers-reduced-motion" not in (css.read_text(encoding="utf-8") if css.is_file() else ""):
        issues.append("Reduced-motion support is missing from CSS")

    missing_local: list[str] = []
    for href in portal.links:
        target = local_target(root, href)
        if target is not None and not target.exists():
            missing_local.append(href)
    if missing_local:
        issues.append(f"Missing local link targets: {sorted(set(missing_local))}")

    report = {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
        "required_section_ids": sorted(required_ids),
        "found_section_ids": sorted(portal.ids),
        "links_checked": len(portal.links),
        "local_missing": sorted(set(missing_local)),
        "canonical": portal.canonical,
        "hreflangs": sorted(portal.hreflangs),
        "json_ld": portal.json_ld,
        "ltr_rtl_pairs_detected": len(portal.lang_dirs),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
