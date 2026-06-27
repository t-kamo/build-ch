# Semi-Automated Production Pipeline

## Summary

This pipeline is designed for human-approved production of AI architecture videos.

The goal is not full automation yet. The goal is a safe, repeatable workflow where scripts prepare prompts, generate placeholder assets, organize review checkpoints, and later connect to Gemini API / Nano Banana / Veo integrations.

No paid external APIs are called in the current MVP.

## Workflow

### 1. Concept

Start from an approved episode concept.

The concept should define:

- location
- hidden build idea
- main character
- transformation stages
- final reveal
- visual rules

### 2. Prompt Generation

Generate structured image and video prompts for each episode.

Outputs:

- `prompts/image-prompts.json`
- `prompts/video-prompts.json`

The prompt files become the contract between planning and generation.

### 3. Image Generation

The image generation step creates one visual state per stage.

Current MVP:

- creates placeholder files
- does not call external APIs
- includes TODO comments for Gemini API / Nano Banana integration

Future implementation:

- call image generation API
- save generated images into `episodes/<episode>/images/`
- preserve stage naming

### 4. Human Image Review

Human review is required before video generation.

The reviewer should check:

- environment consistency
- character consistency
- believable construction progression
- no skipped stages
- no over-amplified excavation
- final image matches the intended stage

Approved image decisions are stored in:

- `episodes/<episode>/images/approved.json`

### 5. Video Generation

The video generation step creates one transition clip per stage pair.

Current MVP:

- creates placeholder clip files
- does not call external APIs
- includes TODO comments for Veo integration

Future implementation:

- use approved stage images as start/end frames
- call Veo or another video API
- save clips into `episodes/<episode>/clips/`

### 6. Human Video Review

Human review is required before final stitching.

The reviewer should check:

- camera stability
- environment continuity
- realistic motion
- clear single-action transition
- no over-building
- no sudden scale jumps

Approved clip decisions are stored in:

- `episodes/<episode>/clips/approved.json`

### 7. Stitching With ffmpeg

After clips are approved, the pipeline checks whether `ffmpeg` is installed.

Current MVP:

- checks for `ffmpeg`
- prints the command it would run
- does not silently fail

Future implementation:

- assemble approved clips
- add audio
- export final vertical short-form video

### 8. Final Export

Final exports should be stored in:

- `episodes/<episode>/final/`

Target platforms:

- TikTok
- YouTube Shorts
- Instagram Reels

## Why Not UI Automation Of Google AI Studio

UI automation is not preferred because it is fragile.

Problems:

- website layouts change
- buttons and fields move
- authentication flows interrupt automation
- browser sessions expire
- uploads and downloads are difficult to guarantee
- errors are harder to detect reliably
- paid generation can be triggered accidentally

UI automation is useful for experimentation, but it is not a stable production system.

## Why API-Based Automation Is Preferred

API-based automation is preferred because it is controllable and repeatable.

Advantages:

- explicit request and response handling
- reliable error detection
- reproducible inputs
- easier logging
- safer cost controls
- easier batching
- simpler integration with review gates
- better long-term maintainability

The intended production system should use APIs for generation and keep human approval between each major stage.

## MVP Safety Rule

Until API integration is intentionally added:

- do not call paid APIs
- generate placeholders only
- keep TODO comments in scripts
- require human approval before moving from images to video and from video to final export

