#!/usr/bin/env python3
"""Check ffmpeg availability and print the planned stitch command."""

import argparse
import shutil
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare ffmpeg stitching command.")
    parser.add_argument("--episode", required=True, help="Episode folder name, e.g. episode002")
    args = parser.parse_args()

    episode_dir = repo_root() / "episodes" / args.episode
    clips_dir = episode_dir / "clips"
    final_dir = episode_dir / "final"

    if not clips_dir.exists():
        raise SystemExit(f"Clips directory not found: {clips_dir}")

    final_dir.mkdir(parents=True, exist_ok=True)

    ffmpeg_path = shutil.which("ffmpeg")
    if not ffmpeg_path:
        print("ffmpeg is not installed or not available on PATH.")
        print("Install ffmpeg before final stitching. On macOS, one option is: brew install ffmpeg")
        return 0

    clips = sorted(path for path in clips_dir.iterdir() if path.is_file() and path.name.endswith(".mp4"))
    if not clips:
        print("ffmpeg found, but no .mp4 clips are available yet.")
        print("Current MVP creates placeholder .txt clips only.")
        print("TODO: After Veo integration, collect approved .mp4 clips and stitch them here.")
        return 0

    list_file = final_dir / "clips.txt"
    output_file = final_dir / f"{args.episode}-prototype.mp4"
    print("ffmpeg is available.")
    print("Command that would run:")
    print(f"{ffmpeg_path} -f concat -safe 0 -i {list_file} -c copy {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

