#!/usr/bin/env python3
"""Generate stage images or dry-run placeholder outputs."""

import argparse
import base64
import json
import os
from pathlib import Path
from typing import Optional
from datetime import datetime, timezone


VALID_STAGES = {"A", "B", "C", "D", "E", "F", "G", "H", "I"}
DEFAULT_IMAGE_MODEL = "gemini-3.1-flash-image"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_prompt_data(prompts_path: Path) -> dict:
    if not prompts_path.exists():
        raise SystemExit(f"Image prompts not found: {prompts_path}")

    with prompts_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def get_stages(prompt_data: dict) -> list[dict]:
    stages = prompt_data.get("stages", [])
    if not stages:
        raise SystemExit("No image stages found in image-prompts.json")
    return stages


def filter_stages(stages: list[dict], requested_stage: Optional[str]) -> list[dict]:
    if not requested_stage:
        return stages

    stage_id = requested_stage.upper()
    if stage_id not in VALID_STAGES:
        valid = ", ".join(sorted(VALID_STAGES))
        raise SystemExit(f"Invalid --stage value: {requested_stage}. Valid stages are: {valid}")

    selected = [stage for stage in stages if stage.get("stage", "").upper() == stage_id]
    if not selected:
        available = ", ".join(stage.get("stage", "?") for stage in stages)
        raise SystemExit(
            f"Stage {stage_id} was requested, but it was not found in image-prompts.json. "
            f"Available stages: {available}"
        )
    return selected


def resolve_reference_image(root: Path, reference_image: Optional[str]) -> Optional[Path]:
    if not reference_image:
        return None

    reference_path = Path(reference_image)
    if not reference_path.is_absolute():
        reference_path = root / reference_path

    if not reference_path.exists():
        print(f"Reference image not found: {reference_path}")
        print("Generation mode: TEXT_TO_IMAGE")
        return None

    return reference_path


def generation_mode(reference_image: Optional[Path]) -> str:
    return "IMAGE_TO_IMAGE" if reference_image else "TEXT_TO_IMAGE"


def write_metadata(
    metadata_dir: Path,
    stage_id: str,
    prompt: str,
    image_model: str,
    mode: str,
    reference_image: Optional[Path],
) -> Path:
    metadata_dir.mkdir(parents=True, exist_ok=True)
    output_path = metadata_dir / f"stage_{stage_id}.json"
    payload = {
        "stage": stage_id,
        "prompt": prompt,
        "image_model": image_model,
        "generation_mode": mode,
        "reference_image_path": str(reference_image) if reference_image else None,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote metadata: {output_path}")
    return output_path


def write_placeholder_outputs(
    episode: str,
    stages: list[dict],
    output_dir: Path,
    metadata_dir: Path,
    image_model: str,
    reference_image: Optional[Path],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    mode = generation_mode(reference_image)
    print(f"Generation mode: {mode}")

    for stage in stages:
        stage_id = stage["stage"]
        name = stage["name"]
        prompt = stage["prompt"]
        output_path = output_dir / f"stage-{stage_id.lower()}.placeholder.txt"
        output_path.write_text(
            "\n".join(
                [
                    f"Episode: {episode}",
                    f"Stage: {stage_id}",
                    f"Name: {name}",
                    "",
                    "Placeholder image output.",
                    "Dry-run mode: no paid external API was called.",
                    "TODO: Replace this stub with Gemini API / Nano Banana image generation.",
                    f"Generation mode: {mode}",
                    f"Reference image: {reference_image or 'None'}",
                    "",
                    "Prompt:",
                    prompt,
                    "",
                ]
            ),
            encoding="utf-8",
        )
        print(f"Created placeholder image: {output_path}")
        write_metadata(metadata_dir, stage_id, prompt, image_model, mode, reference_image)


def load_env(root: Path) -> tuple[str, str]:
    env_path = root / ".env"
    if not env_path.exists():
        raise SystemExit(
            f"Missing .env file: {env_path}\n"
            "Create it from .env.example and set GEMINI_API_KEY before running real generation."
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

    image_model = os.getenv("IMAGE_MODEL") or DEFAULT_IMAGE_MODEL
    if not os.getenv("IMAGE_MODEL"):
        print(f"IMAGE_MODEL missing in .env. Using default: {image_model}")
    else:
        print(f"Using image model: {image_model}")

    return api_key, image_model


def create_genai_client(api_key: str):
    try:
        from google import genai
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: google-genai\n"
            "Install dependencies with: python3 -m pip install google-genai python-dotenv"
        ) from exc

    return genai.Client(api_key=api_key)


def extract_image_bytes(response) -> bytes:
    """Extract the first image bytes from a Gemini generate_content response."""
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", []) or []:
            inline_data = getattr(part, "inline_data", None)
            if not inline_data:
                continue

            data = getattr(inline_data, "data", None)
            if isinstance(data, bytes):
                return data
            if isinstance(data, str):
                return base64.b64decode(data)

    raise ValueError("No image data found in Gemini response")


def list_available_models(api_key: str) -> None:
    client = create_genai_client(api_key)
    print("Available Gemini models:")
    try:
        for model in client.models.list():
            name = getattr(model, "name", "")
            actions = getattr(model, "supported_actions", None) or getattr(model, "supported_generation_methods", None)
            print(f"- {name} {actions or ''}")
    except Exception as exc:
        raise SystemExit(f"Failed to list Gemini models: {exc}") from exc


def generate_real_images(
    stages: list[dict],
    output_dir: Path,
    metadata_dir: Path,
    api_key: str,
    model_name: str,
    reference_image: Optional[Path],
) -> None:
    client = create_genai_client(api_key)
    output_dir.mkdir(parents=True, exist_ok=True)
    mode = generation_mode(reference_image)

    # Gemini image model configuration is loaded from IMAGE_MODEL in .env.
    # Current docs list examples such as gemini-3.1-flash-image,
    # gemini-3-pro-image, and gemini-2.5-flash-image.
    print(f"Image generation model: {model_name}")
    print(f"Generation mode: {mode}")

    try:
        from google.genai import types
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: google-genai\n"
            "Install dependencies with: python3 -m pip install google-genai python-dotenv"
        ) from exc

    for stage in stages:
        stage_id = stage["stage"]
        prompt = stage["prompt"]
        output_path = output_dir / f"stage_{stage_id}.png"
        print(f"Generating Stage {stage_id} with Gemini image generation API...")

        try:
            contents = prompt
            if reference_image:
                image_bytes = reference_image.read_bytes()
                image_part = types.Part.from_bytes(data=image_bytes, mime_type="image/png")
                contents = [image_part, prompt]

            response = client.models.generate_content(
                model=model_name,
                contents=contents,
                config=types.GenerateContentConfig(response_modalities=["IMAGE"]),
            )
            image_bytes = extract_image_bytes(response)
            output_path.write_bytes(image_bytes)
            print(f"Saved image: {output_path}")
            write_metadata(metadata_dir, stage_id, prompt, model_name, mode, reference_image)
        except Exception as exc:
            print(f"API failure for Stage {stage_id}: {exc}")
            print("Continuing with the next stage.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate episode stage images.")
    parser.add_argument("--episode", help="Episode folder name, e.g. episode002")
    parser.add_argument(
        "--stage",
        help="Optional single stage to generate. Valid stages: A, B, C, D, E, F, G, H, I.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Create placeholder files without calling the Gemini image generation API.",
    )
    parser.add_argument(
        "--reference-image",
        help="Optional path to a reference image for Image-to-Image generation.",
    )
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List Gemini models available to the configured API key, then exit.",
    )
    args = parser.parse_args()

    root = repo_root()

    if args.list_models:
        api_key, _image_model = load_env(root)
        list_available_models(api_key)
        return 0

    if not args.episode:
        raise SystemExit("Missing required --episode argument unless --list-models is used.")

    episode_dir = root / "episodes" / args.episode
    prompts_path = episode_dir / "prompts" / "image-prompts.json"
    output_dir = episode_dir / "images"
    metadata_dir = episode_dir / "metadata"

    prompt_data = load_prompt_data(prompts_path)
    stages = get_stages(prompt_data)
    stages = filter_stages(stages, args.stage)
    reference_image = resolve_reference_image(root, args.reference_image)

    if args.dry_run:
        image_model = os.getenv("IMAGE_MODEL") or DEFAULT_IMAGE_MODEL
        write_placeholder_outputs(args.episode, stages, output_dir, metadata_dir, image_model, reference_image)
        return 0

    api_key, image_model = load_env(root)
    generate_real_images(stages, output_dir, metadata_dir, api_key, image_model, reference_image)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
