"""Verify that portal and learner-template candidate manifests still match the coordinated v1.1.0 record."""
from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected an object in {path}")
    return value


def fetch_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "sda-dsc-211-release-coordination-check"},
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = response.read(5_000_000)
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"Could not fetch {url}: {exc}") from exc
    value = json.loads(payload.decode("utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected an object from {url}")
    return value


def raw_url(repository: str, branch: str, path: str) -> str:
    return f"https://raw.githubusercontent.com/{repository}/{branch}/{path}"


def compare(label: str, expected: dict[str, Any], actual: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    checks = {
        "release_version": expected.get("release_version", "v1.1.0"),
        "repository": expected.get("repository"),
        "file_count": expected.get("file_count"),
        "aggregate_sha256": expected.get("aggregate_sha256"),
    }
    for key, expected_value in checks.items():
        actual_value = actual.get(key)
        if actual_value != expected_value:
            issues.append(
                f"{label} {key} mismatch: expected={expected_value!r}, actual={actual_value!r}"
            )
    files = actual.get("files")
    if not isinstance(files, list) or len(files) != actual.get("file_count"):
        issues.append(f"{label} files list does not match file_count")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--coordination",
        type=Path,
        default=Path("release/coordinated_candidate.json"),
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    coordination = read_json(args.coordination)
    issues: list[str] = []
    evidence: dict[str, Any] = {}

    for key in ("portal", "learner_template"):
        expected = coordination[key]
        url = raw_url(
            expected["repository"],
            expected["branch"],
            expected["manifest_path"],
        )
        actual = fetch_json(url)
        manifest_issues = compare(key, expected, actual)
        issues.extend(manifest_issues)
        evidence[key] = {
            "url": url,
            "repository": actual.get("repository"),
            "release_version": actual.get("release_version"),
            "file_count": actual.get("file_count"),
            "aggregate_sha256": actual.get("aggregate_sha256"),
            "status": "PASS" if not manifest_issues else "FAIL",
        }

    report = {
        "status": "PASS" if not issues else "FAIL",
        "release_version": coordination.get("release_version"),
        "candidate_status": coordination.get("status"),
        "issues": issues,
        "evidence": evidence,
        "manual_gates": coordination.get("manual_gates", []),
        "statement": (
            "This check verifies cross-repository candidate identity only. "
            "It does not replace hosted Colab, browser accessibility, private evaluator, "
            "private submission registry, or final publication approval."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
