"""Validate the unified bilingual production portal with Python standard library only."""
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
        self.lang_dirs: list[tuple[str | None, str | None]] = []
        self.canonical = False
        self.hreflangs: set[str] = set()
        self.json_ld = False

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
        if tag == "script" and values.get("type") == "application/ld+json":
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
    base_css = root / "bilingual-v1.1.css"
    hub_css = root / "student-hub.css"
    arabic_legacy = root / "ar.html"
    english_legacy = root / "en.html"
    issues: list[str] = []

    if not index.is_file():
        issues.append("index.html is missing")
        html = ""
    else:
        html = index.read_text(encoding="utf-8")
    if not base_css.is_file():
        issues.append("bilingual-v1.1.css is missing")
    if not hub_css.is_file():
        issues.append("student-hub.css is missing")

    portal = PortalParser()
    if html:
        portal.feed(html)

    required_ids = {
        "main", "overview", "start", "journey", "project", "requirements",
        "assessment", "submission", "support",
    }
    missing_ids = sorted(required_ids - portal.ids)
    if missing_ids:
        issues.append(f"Missing required section ids: {missing_ids}")

    for stylesheet in ("bilingual-v1.1.css", "student-hub.css"):
        if f'href="{stylesheet}"' not in html:
            issues.append(f"index.html does not reference {stylesheet}")
    if 'dir="ltr"' not in html or 'dir="rtl"' not in html:
        issues.append("Explicit LTR and RTL columns are required")
    if "Everything you need" not in html or "كل ما تحتاجه" not in html:
        issues.append("Unified student-hub heading is missing")
    if "Student template" not in html or "قالب مشروع المتدرب" not in html:
        issues.append("Bilingual student-template entry is missing")
    if not portal.canonical:
        issues.append("Canonical link is missing")
    if not {"ar", "en"}.issubset(portal.hreflangs):
        issues.append("Arabic and English hreflang links are required")
    if not portal.json_ld:
        issues.append("Course JSON-LD is missing")
    if "not an official SDAIA account" not in html or "ليست حسابًا رسميًا لسدايا" not in html:
        issues.append("The bilingual non-official SDAIA disclaimer is missing")
    base_css_text = base_css.read_text(encoding="utf-8") if base_css.is_file() else ""
    if "prefers-reduced-motion" not in base_css_text:
        issues.append("Reduced-motion support is missing from base CSS")

    for redirect in (arabic_legacy, english_legacy):
        if not redirect.is_file():
            issues.append(f"Legacy portal route missing: {redirect.name}")
            continue
        redirect_text = redirect.read_text(encoding="utf-8")
        if "url=./" not in redirect_text or "window.location.replace('./')" not in redirect_text:
            issues.append(f"Legacy route does not redirect to unified portal: {redirect.name}")

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
        "legacy_redirects": [arabic_legacy.name, english_legacy.name],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
