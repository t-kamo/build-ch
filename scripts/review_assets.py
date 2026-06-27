#!/usr/bin/env python3
"""Review generated placeholder assets and write approved.json."""

import argparse
import json
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def candidate_files(asset_dir: Path) -> list[Path]:
    ignored = {"approved.json", ".gitkeep"}
    return sorted(path for path in asset_dir.iterdir() if path.is_file() and path.name not in ignored)


def ask_approval(path: Path) -> bool:
    while True:
        answer = input(f"Approve {path.name}? [y/n]: ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please answer y or n.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Review images or clips and write approved.json.")
    parser.add_argument("--episode", required=True, help="Episode folder name, e.g. episode002")
    parser.add_argument("--type", required=True, choices=["images", "clips"], help="Asset type to review")
    args = parser.parse_args()

    asset_dir = repo_root() / "episodes" / args.episode / args.type
    if not asset_dir.exists():
        raise SystemExit(f"Asset directory not found: {asset_dir}")

    files = candidate_files(asset_dir)
    if not files:
        raise SystemExit(f"No reviewable files found in {asset_dir}")

    approvals = {}
    interactive = sys.stdin.isatty()

    if not interactive:
        print("Non-interactive session detected. Auto-approving assets for smoke test purposes.")

    for path in files:
        approved = ask_approval(path) if interactive else True
        approvals[path.name] = {"approved": approved}

    output_path = asset_dir / "approved.json"
    output_path.write_text(json.dumps(approvals, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote approvals: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

