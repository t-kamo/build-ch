#!/usr/bin/env python3
"""Generate transition videos or dry-run placeholder clips."""

import argparse
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


DEFAULT_VIDEO_MODEL = "veo-3.1-generate-preview"
VALID_TRANSITIONS = {"A_to_B", "B_to_C", "C_to_D", "D_to_E", "E_to_F", "F_to_G", "G_to_H", "H_to_I"}
POLL_INTERVAL_SECONDS = 10
MAX_POLL_ATTEMPTS = 60


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

    if requested_transition not in VALID_TRANSITIONS:
        valid = ", ".join(sorted(VALID_TRANSITIONS))
        raise SystemExit(f"Invalid --transition value: {requested_transition}. Valid transitions are: {valid}")

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
        raise SystemExit(f"Missing {label.lower()} reference image: {path}")

    return path


def generation_mode(start_image: Optional[Path], end_image: Optional[Path]) -> str:
    return "IMAGE_TO_VIDEO" if start_image else "TEXT_TO_VIDEO"


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


def load_required_env(root: Path) -> tuple[str, str]:
    env_path = root / ".env"
    if not env_path.exists():
        raise SystemExit(
            f"Missing .env file: {env_path}\n"
            "Create it from .env.example and set GEMINI_API_KEY and VIDEO_MODEL before real video generation."
        )

    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: python-dotenv\n"
            "Install dependencies with: python3 -m pip install google-genai python-dotenv"
        ) from exc

    load_dotenv(env_path)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Missing GEMINI_API_KEY in .env")

    video_model = os.getenv("VIDEO_MODEL")
    if not video_model:
        raise SystemExit("Missing VIDEO_MODEL in .env")

    print(f"Using video model: {video_model}")
    return api_key, video_model


def configured_video_model() -> str:
    model = os.getenv("VIDEO_MODEL") or DEFAULT_VIDEO_MODEL
    if os.getenv("VIDEO_MODEL"):
        print(f"Using video model: {model}")
    else:
        print(f"VIDEO_MODEL missing. Using default: {model}")
    return model


def create_genai_client(api_key: str):
    try:
        from google import genai
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: google-genai\n"
            "Install dependencies with: python3 -m pip install google-genai python-dotenv"
        ) from exc

    return genai.Client(api_key=api_key)


def image_from_path(path: Path):
    try:
        from google.genai import types
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: google-genai\n"
            "Install dependencies with: python3 -m pip install google-genai python-dotenv"
        ) from exc

    mime_type = "image/png" if path.suffix.lower() == ".png" else None
    return types.Image.from_file(location=str(path), mime_type=mime_type)


def wait_for_video_operation(client, operation):
    for attempt in range(1, MAX_POLL_ATTEMPTS + 1):
        done = getattr(operation, "done", False)
        if done:
            return operation

        print(f"Waiting for Veo operation... attempt {attempt}/{MAX_POLL_ATTEMPTS}")
        time.sleep(POLL_INTERVAL_SECONDS)
        operation = client.operations.get(operation)

    raise TimeoutError("Veo operation did not complete before the polling limit.")


def extract_video_bytes(client, operation) -> bytes:
    response = getattr(operation, "result", None) or getattr(operation, "response", None)
    generated_videos = getattr(response, "generated_videos", None) if response else None
    if not generated_videos:
        raise ValueError("No video returned by Veo API")

    video = getattr(generated_videos[0], "video", None)
    if not video:
        raise ValueError("Generated video response did not include a video object")

    video_bytes = getattr(video, "video_bytes", None)
    if video_bytes:
        return video_bytes

    try:
        return client.files.download(file=video)
    except Exception as exc:
        raise ValueError(f"Video was returned but could not be downloaded: {exc}") from exc


def write_metadata(
    metadata_dir: Path,
    transition_id: str,
    model: str,
    mode: str,
    start_image: Optional[Path],
    end_image: Optional[Path],
    prompt: str,
    start_only: bool,
) -> Path:
    metadata_dir.mkdir(parents=True, exist_ok=True)
    output_path = metadata_dir / f"{transition_id}.json"
    payload = {
        "transition": transition_id,
        "model": model,
        "generation_mode": mode,
        "start_image": str(start_image) if start_image else None,
        "end_image": str(end_image) if end_image else None,
        "start_only": start_only,
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
    start_only: bool,
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
                    f"Start only: {start_only}",
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
        write_metadata(metadata_dir, transition_id, model, mode, start_image, end_image, prompt, start_only)


def generate_real_videos(
    transitions: list[dict],
    output_dir: Path,
    metadata_dir: Path,
    api_key: str,
    model: str,
    start_image: Optional[Path],
    end_image: Optional[Path],
    start_only: bool,
) -> None:
    mode = generation_mode(start_image, end_image)
    print(f"Generation mode: {mode}")

    if start_only and not start_image:
        raise SystemExit("--start-only requires --reference-start.")

    if not start_only and ((start_image and not end_image) or (end_image and not start_image)):
        raise SystemExit("Both --reference-start and --reference-end are required for IMAGE_TO_VIDEO generation.")

    try:
        from google.genai import types
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: google-genai\n"
            "Install dependencies with: python3 -m pip install google-genai python-dotenv"
        ) from exc

    client = create_genai_client(api_key)
    output_dir.mkdir(parents=True, exist_ok=True)

    start_frame = image_from_path(start_image) if start_image else None
    end_frame = image_from_path(end_image) if end_image and not start_only else None

    for transition in transitions:
        transition_id = transition["id"]
        prompt = transition["prompt"]
        output_path = output_dir / f"{transition_id}.mp4"
        print(f"Generating transition {transition_id} with Veo API...")

        try:
            config = types.GenerateVideosConfig(
                numberOfVideos=1,
                aspectRatio="16:9",
                durationSeconds=8,
                lastFrame=end_frame,
            )
            operation = client.models.generate_videos(
                model=model,
                prompt=prompt,
                image=start_frame,
                config=config,
            )
            operation = wait_for_video_operation(client, operation)
            video_bytes = extract_video_bytes(client, operation)
            if not video_bytes:
                raise ValueError("No video bytes returned by Veo API")

            output_path.write_bytes(video_bytes)
            print(f"Saved video: {output_path}")
            write_metadata(metadata_dir, transition_id, model, mode, start_image, end_image, prompt, start_only)
        except Exception as exc:
            raise SystemExit(f"API failure for transition {transition_id}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate transition clips.")
    parser.add_argument("--episode", required=True, help="Episode folder name, e.g. episode002")
    parser.add_argument("--transition", help="Optional transition id, e.g. H_to_I")
    parser.add_argument("--reference-start", help="Optional start frame image path")
    parser.add_argument("--reference-end", help="Optional end frame image path")
    parser.add_argument(
        "--start-only",
        action="store_true",
        help="Use only --reference-start and do not send an end frame to the video model.",
    )
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
    end_image = None if args.start_only else resolve_reference(root, args.reference_end, "End")
    model = configured_video_model()

    if args.dry_run:
        write_placeholder_clips(
            args.episode,
            transitions,
            output_dir,
            metadata_dir,
            model,
            start_image,
            end_image,
            args.start_only,
        )
        return 0

    api_key, model = load_required_env(root)
    generate_real_videos(transitions, output_dir, metadata_dir, api_key, model, start_image, end_image, args.start_only)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
