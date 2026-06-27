# Production Workflow

## Reverse Construction Workflow

The production workflow now starts from the completed scene.

Stage I

↓

Stage H

↓

Stage G

↓

...

↓

Stage A

Reason:

Generating backwards greatly improves consistency of:

- architecture
- environment
- character
- lighting
- camera angle

This becomes the standard workflow for every future episode.

## Workflow Rule

Start by generating and approving the final reveal image.

After the final image is accepted, use it as the canonical visual reference for earlier stages through Image-to-Image generation.

Each earlier stage should remove or simplify one construction element while preserving the same world, camera, and architectural identity.

## Finding — Image-to-Image Consistency

Image-to-Image generation from the accepted final image provides sufficient visual consistency for sequential construction stages.

This becomes the default workflow.

Preferred sequence:

Stage I

↓

Stage H

↓

Stage G

↓

...

Generating backward from the accepted final image is preferred over generating each image independently.

Reason:

- stronger architectural continuity
- more stable environment
- more consistent lighting
- better camera preservation
- clearer production history

## Incremental Video Workflow

Instead of generating every image first and all videos afterwards, the project now follows an incremental workflow.

For every pair of stages:

Generate Image

↓

Review

↓

Accept

↓

Generate Transition Video

↓

Review

↓

Accept

↓

Move to previous stage.

Reason:

- Earlier detection of animation problems.
- Less regeneration work.
- Better visual consistency.

This becomes the default production workflow.

