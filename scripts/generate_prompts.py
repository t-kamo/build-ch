#!/usr/bin/env python3
"""Validate episode prompt files for the semi-automated pipeline."""

import argparse
import json
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate episode prompt files.")
    parser.add_argument("--episode", required=True, help="Episode folder name, e.g. episode002")
    args = parser.parse_args()

    episode_dir = repo_root() / "episodes" / args.episode
    prompts_dir = episode_dir / "prompts"
    image_prompts_path = prompts_dir / "image-prompts.json"
    video_prompts_path = prompts_dir / "video-prompts.json"

    if not episode_dir.exists():
        raise SystemExit(f"Episode directory not found: {episode_dir}")

    missing = [path for path in (image_prompts_path, video_prompts_path) if not path.exists()]
    if missing:
        missing_list = "\n".join(str(path) for path in missing)
        raise SystemExit(f"Missing prompt files:\n{missing_list}")

    image_prompts = load_json(image_prompts_path)
    video_prompts = load_json(video_prompts_path)

    stage_count = len(image_prompts.get("stages", []))
    transition_count = len(video_prompts.get("transitions", []))

    print(f"Episode: {args.episode}")
    print(f"Image stages: {stage_count}")
    print(f"Video transitions: {transition_count}")
    print("Prompt files are present and valid JSON.")
    print("TODO: Add concept-to-prompt generation logic if prompts should be generated automatically.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

