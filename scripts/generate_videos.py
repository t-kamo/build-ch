#!/usr/bin/env python3
"""Generate transition videos or dry-run placeholder clips."""

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


DEFAULT_VIDEO_MODEL = "veo-3.1-generate-preview"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_prompt_data(prompts_path: Path) -> dict:
    if not prompts_path.exists():
        raise SystemExit(f"Video prompts not found: {prompts_path}")

    with prompts_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def get_transitions(prompt_data: dict) -> list[dict]:
    transitions = prompt_data.get("transitions", [])
    if not transitions:
        raise SystemExit("No transitions found in video-prompts.json")
    return transitions


def filter_transitions(transitions: list[dict], requested_transition: Optional[str]) -> list[dict]:
    if not requested_transition:
        return transitions

    selected = [transition for transition in transitions if transition.get("id") == requested_transition]
    if not selected:
        available = ", ".join(transition.get("id", "?") for transition in transitions)
        raise SystemExit(
            f"Invalid --transition value: {requested_transition}. "
            f"Available transitions are: {available}"
        )
    return selected


def resolve_reference(root: Path, reference_path: Optional[str], label: str) -> Optional[Path]:
    if not reference_path:
        return None

    path = Path(reference_path)
    if not path.is_absolute():
        path = root / path

    if not path.exists():
        print(f"{label} image not found: {path}")
        return None

    return path


def generation_mode(start_image: Optional[Path], end_image: Optional[Path]) -> str:
    return "IMAGE_TO_VIDEO" if start_image and end_image else "TEXT_TO_VIDEO"


def load_env_if_available(root: Path) -> None:
    env_path = root / ".env"
    if not env_path.exists():
        print(f"No .env file found at {env_path}. Using environment variables and defaults.")
        return

    try:
        from dotenv import load_dotenv
    except ImportError:
        print("python-dotenv is not installed. Using environment variables and defaults.")
        return

    load_dotenv(env_path)


def configured_video_model() -> str:
    model = os.getenv("VIDEO_MODEL") or DEFAULT_VIDEO_MODEL
    if os.getenv("VIDEO_MODEL"):
        print(f"Using video model: {model}")
    else:
        print(f"VIDEO_MODEL missing. Using default: {model}")
    return model


def write_metadata(
    metadata_dir: Path,
    transition_id: str,
    model: str,
    mode: str,
    start_image: Optional[Path],
    end_image: Optional[Path],
    prompt: str,
) -> Path:
    metadata_dir.mkdir(parents=True, exist_ok=True)
    output_path = metadata_dir / f"{transition_id}.json"
    payload = {
        "transition": transition_id,
        "model": model,
        "generation_mode": mode,
        "start_image": str(start_image) if start_image else None,
        "end_image": str(end_image) if end_image else None,
        "prompt": prompt,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote metadata: {output_path}")
    return output_path


def write_placeholder_clips(
    episode: str,
    transitions: list[dict],
    output_dir: Path,
    metadata_dir: Path,
    model: str,
    start_image: Optional[Path],
    end_image: Optional[Path],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    mode = generation_mode(start_image, end_image)
    print(f"Generation mode: {mode}")

    for transition in transitions:
        transition_id = transition["id"]
        prompt = transition["prompt"]
        action = transition["action"]
        output_path = output_dir / f"{transition_id}.placeholder.txt"
        output_path.write_text(
            "\n".join(
                [
                    f"Episode: {episode}",
                    f"Transition: {transition_id}",
                    "",
                    "Placeholder video clip output.",
                    "Dry-run mode: no paid external API was called.",
                    "TODO: Replace this stub with Veo video generation.",
                    f"Generation mode: {mode}",
                    f"Start image: {start_image or 'None'}",
                    f"End image: {end_image or 'None'}",
                    "",
                    f"Action: {action}",
                    "",
                    "Prompt:",
                    prompt,
                    "",
                ]
            ),
            encoding="utf-8",
        )
        print(f"Created placeholder clip: {output_path}")
        write_metadata(metadata_dir, transition_id, model, mode, start_image, end_image, prompt)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate transition clips.")
    parser.add_argument("--episode", required=True, help="Episode folder name, e.g. episode002")
    parser.add_argument("--transition", help="Optional transition id, e.g. H_to_I")
    parser.add_argument("--reference-start", help="Optional start frame image path")
    parser.add_argument("--reference-end", help="Optional end frame image path")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Create placeholder clips without calling the video generation API.",
    )
    args = parser.parse_args()

    root = repo_root()
    load_env_if_available(root)
    episode_dir = root / "episodes" / args.episode
    prompts_path = episode_dir / "prompts" / "video-prompts.json"
    output_dir = episode_dir / "clips"
    metadata_dir = episode_dir / "metadata"

    prompt_data = load_prompt_data(prompts_path)
    transitions = get_transitions(prompt_data)
    transitions = filter_transitions(transitions, args.transition)

    start_image = resolve_reference(root, args.reference_start, "Start")
    end_image = resolve_reference(root, args.reference_end, "End")
    model = configured_video_model()

    if args.dry_run:
        write_placeholder_clips(args.episode, transitions, output_dir, metadata_dir, model, start_image, end_image)
        return 0

    mode = generation_mode(start_image, end_image)
    print(f"Generation mode: {mode}")
    raise SystemExit(
        "Real video generation is not implemented yet. "
        "TODO: Add Gemini/Veo API integration here. Use --dry-run for the current MVP."
    )


if __name__ == "__main__":
    raise SystemExit(main())
