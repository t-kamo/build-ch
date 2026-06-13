# Sprint 001 — Image Prompt Validation

## Episode

001 Hidden Waterfall House

## Validation Goal

Validate the first three image-generation scenes before continuing the full production sequence.

These prompts test whether the model can maintain:

- Same waterfall
- Same cliff face
- Same terrain
- Same lighting direction
- Same camera position
- Same scale
- One logical change per scene

## Global Validation Rules

- Photorealistic style only.
- Use image-to-image after Scene01 Start Frame.
- Preserve the previous image as the base for the next prompt.
- Do not change weather, terrain, waterfall shape, cliff geometry, camera angle, scale, or lighting direction.
- Do not introduce a worker yet.
- Do not introduce construction tools except where explicitly requested.
- Each End Frame must be usable as the next scene's Start Frame.

---

## Scene01 — Hook

## Purpose

Validate the base waterfall environment and subtle hidden-space hint.

## Start Frame Prompt

Photorealistic cinematic wide shot of a massive natural waterfall in a remote forest, falling down a steep dark rock cliff into a misty pool. The cliff face looks untouched and natural, with moss, wet stone, forest vegetation, water spray, and soft daylight from the same direction. Maintain realistic scale, natural terrain, and a static slightly elevated front camera angle. No visible entrance, no construction materials, no worker, no artificial objects.

## End Frame Prompt

Use the previous image as input. Keep the same waterfall, cliff face, forest terrain, mist, lighting direction, camera position, framing, perspective, and scale. Modify only the area behind the falling water by adding a very subtle dark shadow and faint natural recess behind the waterfall, barely visible through mist and water. Do not create a clear doorway yet. Final scene should still look natural, but suggest that something may exist behind the waterfall.

## Validation Checklist

- Same camera and framing as Start Frame
- Same waterfall shape and cliff geometry
- No visible man-made entrance
- Hidden recess is subtle, not obvious
- No worker or tools
- Natural photorealistic environment

## Pass Condition

The image feels like a natural waterfall, but the viewer can sense a possible hidden space behind the water.

---

## Scene02 — Discovery

## Purpose

Validate whether the hidden construction zone can be revealed without breaking environmental consistency.

## Start Frame Prompt

Use Scene01 End Frame as input. Maintain the same waterfall, cliff face, forest terrain, mist, lighting, camera angle, perspective, and scale. The scene begins with the subtle dark recess behind the waterfall still barely visible. No construction materials yet.

## End Frame Prompt

Use the previous image as input. Keep everything consistent. Modify only the hidden area behind the falling water by making a small reachable wet rock ledge visible through the mist, positioned behind the waterfall near the cliff wall. The ledge should look naturally formed, damp, and physically reachable, but still secret. Do not add markings, tools, or excavation yet. Final scene should clearly identify a hidden construction zone behind the waterfall.

## Validation Checklist

- Same camera, scale, waterfall, cliff, and terrain as Scene01
- Hidden ledge is visible but still natural
- Ledge feels physically reachable
- No construction marks yet
- No tools, worker, excavation, or artificial structure
- Mist and falling water still partially conceal the zone

## Pass Condition

The hidden ledge is readable as a possible work zone while still feeling naturally integrated behind the waterfall.

---

## Scene03 — Marking

## Purpose

Validate whether a simple entrance outline can be added without changing the waterfall environment or starting excavation too early.

## Start Frame Prompt

Use Scene02 End Frame as input. Keep the same waterfall, cliff face, hidden ledge, forest terrain, mist, lighting direction, camera angle, perspective, and scale. The hidden wet rock ledge is visible behind the water, with no construction changes yet.

## End Frame Prompt

Use the previous image as input. Modify only the wet rock wall on the hidden ledge by adding a simple rectangular entrance outline marked with bright construction chalk or paint. The outline should be physically placed on the rock wall behind the waterfall and remain partially visible through mist and water spray. Do not cut into the rock yet. Keep all terrain, waterfall, lighting, scale, and camera unchanged. Final scene should show the exact future entrance area.

## Validation Checklist

- Same camera, waterfall, cliff face, ledge, terrain, lighting, and scale as Scene02
- Only one new change: rectangular entrance outline
- No excavation or rock removal yet
- Marking is visible but affected by mist and water spray
- Entrance outline is physically plausible on the wet rock wall
- No worker or tools unless unavoidable in the generation

## Pass Condition

The future entrance area is clearly marked, while the waterfall environment remains consistent and no construction has begun yet.

---

## Sprint Decision

Continue to Scene04 only if:

- Scene01 establishes a strong natural hook.
- Scene02 reveals a believable hidden work zone.
- Scene03 adds a clear entrance outline without changing the environment.
- The three images can be placed in sequence without obvious camera, scale, lighting, or terrain jumps.

