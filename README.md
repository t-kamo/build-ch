# build-ch

## Semi-automated Episode Production

This repository includes an MVP pipeline for semi-automated AI architecture video production.

The current implementation is safe by default:

- no paid external APIs are called
- image generation creates placeholder files
- video generation creates placeholder files
- human approval gates are kept between images, clips, and final export
- future Gemini API / Nano Banana / Veo integrations are marked with TODO comments

Intended command sequence:

```bash
python scripts/generate_prompts.py --episode episode002
python scripts/generate_images.py --episode episode002 --dry-run
python scripts/review_assets.py --episode episode002 --type images
python scripts/generate_videos.py --episode episode002
python scripts/review_assets.py --episode episode002 --type clips
python scripts/stitch_video.py --episode episode002
```

If `python` is not available on the local machine, use `python3` with the same arguments.

### Environment Setup

Create a local `.env` file from the example file:

```bash
cp .env.example .env
```

Then set:

```bash
GEMINI_API_KEY=your_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=false
IMAGE_MODEL=gemini-3.1-flash-image
VIDEO_MODEL=veo-3.1-generate-preview
```

`IMAGE_MODEL` controls the Gemini image generation model used by `scripts/generate_images.py`.

Current Gemini API image generation docs list Nano Banana image models such as:

- `gemini-3.1-flash-image`
- `gemini-3-pro-image`
- `gemini-2.5-flash-image`

### Install Dependencies

Install the dependencies needed for real Gemini image generation:

```bash
python3 -m pip install google-genai python-dotenv
```

### Image Generation

### Reverse Construction Workflow

Episode production now starts from the completed final scene and works backward:

```text
Stage I -> Stage H -> Stage G -> ... -> Stage A
```

The accepted final reveal becomes the canonical reference for architecture, environment, character, lighting, and camera angle.

This improves consistency across the whole episode.

Dry-run placeholder generation:

```bash
python3 scripts/generate_images.py --episode episode002 --dry-run
```

Dry-run a single stage:

```bash
python3 scripts/generate_images.py --episode episode002 --stage I --dry-run
```

Real Gemini image generation:

```bash
python3 scripts/generate_images.py --episode episode002
```

Real Gemini image generation for a single stage:

```bash
python3 scripts/generate_images.py --episode episode002 --stage I
```

Image-to-Image generation from an accepted reference image:

```bash
python3 scripts/generate_images.py \
  --episode episode002 \
  --stage H \
  --reference-image episodes/episode002/images/stage_I.png
```

Dry-run Image-to-Image test:

```bash
python3 scripts/generate_images.py \
  --episode episode002 \
  --stage H \
  --reference-image episodes/episode002/images/stage_I.png \
  --dry-run
```

List Gemini models available to the configured API key:

```bash
python3 scripts/generate_images.py --list-models
```

The real generation command reads `GEMINI_API_KEY` from `.env` and writes stage images to:

- `episodes/episode002/images/stage_A.png`
- `episodes/episode002/images/stage_B.png`
- `episodes/episode002/images/stage_C.png`
- `episodes/episode002/images/stage_D.png`
- `episodes/episode002/images/stage_E.png`
- `episodes/episode002/images/stage_F.png`
- `episodes/episode002/images/stage_G.png`
- `episodes/episode002/images/stage_H.png`
- `episodes/episode002/images/stage_I.png`

### Generation Metadata

Every generated image writes production metadata to:

```text
episodes/<episode>/metadata/stage_<STAGE>.json
```

Metadata includes:

- stage
- prompt
- image model
- generation mode
- reference image path
- timestamp

### Incremental Video Workflow

The project now generates and reviews each transition immediately after the relevant stage images are accepted.

Workflow:

```text
Generate Image -> Review -> Accept -> Generate Transition Video -> Review -> Accept -> Move to previous stage
```

This catches animation problems earlier, reduces regeneration work, and preserves visual consistency.

### Video Generation

Real Veo generation may consume credits. Run dry-run first and only run real generation when the start/end images have been accepted.

Dry-run Image-to-Video transition generation:

```bash
python3 scripts/generate_videos.py \
  --episode episode002 \
  --transition H_to_I \
  --reference-start episodes/episode002/images/stage_H.png \
  --reference-end episodes/episode002/images/stage_I.png \
  --dry-run
```

Real Veo Image-to-Video generation:

```bash
python3 scripts/generate_videos.py \
  --episode episode002 \
  --transition H_to_I \
  --reference-start episodes/episode002/images/stage_H.png \
  --reference-end episodes/episode002/images/stage_I.png
```

`VIDEO_MODEL` controls the Veo model used for real video generation and recorded in video metadata.

Video metadata is written to:

```text
episodes/<episode>/metadata/<TRANSITION>.json
```

Metadata includes:

- transition
- model
- generation mode
- start image
- end image
- prompt
- timestamp

Episode outputs are organized under:

- `episodes/episode002/images/`
- `episodes/episode002/clips/`
- `episodes/episode002/final/`
