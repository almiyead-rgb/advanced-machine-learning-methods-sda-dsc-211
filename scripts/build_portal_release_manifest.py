"""Build a deterministic integrity manifest for the bilingual course portal."""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def collect_files(root: Path, include: list[str], exclude: list[str]) -> list[Path]:
    selected: dict[str, Path] = {}
    for pattern in include:
        for path in root.glob(pattern):
            if not path.is_file():
                continue
            relative = path.relative_to(root).as_posix()
            if any(fnmatch.fnmatch(relative, item) for item in exclude):
                continue
            selected[relative] = path
    return [selected[key] for key in sorted(selected)]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--scope", type=Path, default=Path("release/portal_release_scope.json"))
    parser.add_argument("--output", type=Path, default=Path("check-output/portal_release_manifest.candidate.json"))
    args = parser.parse_args()

    root = args.root.resolve()
    scope_path = args.scope if args.scope.is_absolute() else root / args.scope
    scope = read_json(scope_path)
    files = collect_files(root, scope["include"], scope["exclude"])
    if not files:
        raise SystemExit("Portal release scope selected no files.")

    maximum = int(scope.get("maximum_file_bytes", 10485760))
    entries: list[dict[str, Any]] = []
    aggregate = hashlib.sha256()
    for path in files:
        relative = path.relative_to(root).as_posix()
        size = path.stat().st_size
        if path.is_symlink():
            raise SystemExit(f"Symlink is not allowed: {relative}")
        if size > maximum:
            raise SystemExit(f"File exceeds size ceiling: {relative}")
        digest = file_sha256(path)
        entries.append({"path": relative, "bytes": size, "sha256": digest})
        aggregate.update(f"{relative}\0{size}\0{digest}\n".encode("utf-8"))

    manifest = {
        "schema_version": 1,
        "release_version": scope["release_version"],
        "repository": scope["repository"],
        "file_count": len(entries),
        "aggregate_sha256": aggregate.hexdigest(),
        "files": entries,
        "notes": "Integrity inventory only; final tag and exact commit SHA are recorded separately.",
    }
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "file_count": len(entries), "aggregate_sha256": manifest["aggregate_sha256"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
