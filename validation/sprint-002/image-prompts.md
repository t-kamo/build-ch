# Sprint 002 — Image Prompt Validation

## Purpose

Validate whether the image generation workflow can maintain environmental consistency during the first visible construction phase.

The goal is not to build the waterfall house.

The goal is to test environmental consistency during construction.

## Success Criteria

- Same waterfall
- Same cliff face
- Same terrain
- Same lighting direction
- Same camera position
- Same scale
- One logical change per scene

## Global Environment Lock

Use this exact environment description in every scene:

Massive natural waterfall in a remote forest. Dark volcanic cliff face. Dense moss and vegetation. Heavy water flow. Mist near the pool. Soft daylight from camera left. Static elevated front-facing camera. Photorealistic style.

Do not change:

- Waterfall shape
- Cliff geometry
- Vegetation
- Weather
- Terrain
- Lighting direction
- Camera position
- Scale

## Global Image-to-Image Instruction

Use the provided image as the base image.

Keep everything else exactly the same.

Change only the specified construction element.

---

## Scene04 — Rock Clearing

## Scene Number

Scene04

## Scene Name

Rock Clearing

## Start Frame Prompt

Use the Scene03 End Frame as the base image.

The base image should show: Massive natural waterfall in a remote forest. Dark volcanic cliff face. Dense moss and vegetation. Heavy water flow. Mist near the pool. Soft daylight from camera left. Static elevated front-facing camera. Photorealistic style. A simple rectangular entrance outline is marked on the wet rock wall behind the waterfall.

Do not generate a new scene from scratch.

## End Frame Prompt

Use the provided image as the base image. Keep everything else exactly the same. Change only the specified construction element.

Remove a small amount of moss, loose rock, and vegetation from inside the marked rectangular entrance area. Expose slightly more bare dark volcanic stone within the marked area. Add a few small removed moss pieces and loose stones at the base of the marked area on the wet rock ledge.

Do not excavate. Do not cut into the cliff. Do not create a tunnel. Do not create a doorway. Do not add tools, workers, beams, lights, furniture, or artificial structures.

The final image should look like the same marked entrance area after minor surface clearing only.

## Modification

Remove moss, remove loose rock, and expose more bare stone inside the marked entrance area.

## Consistency Instructions

- Use the provided image as the base image.
- Keep everything else exactly the same.
- Change only the marked entrance surface.
- Preserve the exact waterfall shape.
- Preserve the exact cliff geometry.
- Preserve dense moss and vegetation outside the marked area.
- Preserve mist near the pool.
- Preserve soft daylight from camera left.
- Preserve the static elevated front-facing camera.
- Preserve scale and perspective.

## Validation Checklist

- Same waterfall shape as Scene03
- Same cliff geometry as Scene03
- Same terrain, vegetation, and mist
- Same lighting direction from camera left
- Same static elevated front-facing camera
- Same scale
- Only minor clearing inside the marked entrance area
- No excavation
- No tunnel
- No doorway
- No artificial structure

---

## Scene05 — Initial Excavation

## Scene Number

Scene05

## Scene Name

Initial Excavation

## Start Frame Prompt

Use the Scene04 End Frame as the base image.

The base image should show: Massive natural waterfall in a remote forest. Dark volcanic cliff face. Dense moss and vegetation. Heavy water flow. Mist near the pool. Soft daylight from camera left. Static elevated front-facing camera. Photorealistic style. The marked entrance area has a small amount of moss and loose rock removed, exposing more bare stone, but there is no tunnel or doorway yet.

Do not generate a new scene from scratch.

## End Frame Prompt

Use the provided image as the base image. Keep everything else exactly the same. Change only the specified construction element.

Remove a small amount of rock from inside the marked rectangular area to create a shallow excavation. The excavation should be only a rough shallow recess in the dark volcanic cliff face, not a full tunnel. Show freshly broken wet stone and a small pile of rock chips directly below the marked area.

Do not create a full tunnel. Do not enlarge into an interior chamber. Do not add support beams, lights, furniture, tools, workers, or artificial structures.

The final image should look like the first visible entrance opening has just begun.

## Modification

Remove a small amount of rock and create a shallow opening inside the marked area.

## Consistency Instructions

- Use the provided image as the base image.
- Keep everything else exactly the same.
- Change only the rock inside the marked rectangle.
- Preserve waterfall shape, cliff geometry, vegetation, weather, terrain, mist, lighting direction, camera position, and scale.
- Keep the marked outline visible around the shallow excavation.
- Keep the excavation small and physically believable.

## Validation Checklist

- Same waterfall shape as Scene04
- Same cliff face geometry except the small shallow recess
- Same terrain and vegetation
- Same soft daylight from camera left
- Same static elevated front-facing camera
- Same scale
- Only a shallow excavation is added
- No full tunnel
- No interior room
- No support structure
- No furniture or decorative elements

---

## Scene06 — Tunnel Entrance

## Scene Number

Scene06

## Scene Name

Tunnel Entrance

## Start Frame Prompt

Use the Scene05 End Frame as the base image.

The base image should show: Massive natural waterfall in a remote forest. Dark volcanic cliff face. Dense moss and vegetation. Heavy water flow. Mist near the pool. Soft daylight from camera left. Static elevated front-facing camera. Photorealistic style. A shallow excavation exists inside the marked entrance area, with broken wet stone and small rock chips below it.

Do not generate a new scene from scratch.

## End Frame Prompt

Use the provided image as the base image. Keep everything else exactly the same. Change only the specified construction element.

Enlarge the shallow excavation into a small human-sized tunnel entrance behind the waterfall. The opening should be rough, dark, and believable, carved into the dark volcanic cliff face within the same marked area. Add realistic broken rock debris at the base of the entrance. The tunnel should only show a short dark entrance, not a full interior room.

Do not reveal an interior chamber. Do not add furniture. Do not add artificial structures. Do not add support beams. Do not add lighting. Do not change the waterfall, cliff geometry outside the opening, vegetation, terrain, weather, lighting direction, camera position, or scale.

The final image should show a believable small tunnel entrance behind the waterfall while the natural environment remains consistent.

## Modification

Enlarge the shallow excavation into a small realistic human-sized tunnel entrance.

## Consistency Instructions

- Use the provided image as the base image.
- Keep everything else exactly the same.
- Change only the excavation area inside the marked entrance.
- Preserve waterfall shape.
- Preserve cliff geometry outside the opening.
- Preserve dense moss and vegetation.
- Preserve mist near the pool.
- Preserve soft daylight from camera left.
- Preserve static elevated front-facing camera.
- Preserve scale and perspective.
- Keep the tunnel entrance small, rough, and physically believable.

## Validation Checklist

- Same waterfall shape as Scene05
- Same cliff face outside the entrance
- Same terrain, vegetation, weather, and mist
- Same lighting direction from camera left
- Same camera position and scale
- Tunnel entrance is human-sized and believable
- No interior room visible
- No furniture
- No artificial structure
- No support beams or lights
- Only one major change from Scene05

---

## Sprint Decision

Continue to the next sprint only if:

- Scene04 keeps the environment stable while clearing only the marked surface.
- Scene05 creates a shallow excavation without becoming a full tunnel.
- Scene06 creates a believable tunnel entrance without revealing an interior room.
- All three images preserve the exact waterfall, cliff face, terrain, vegetation, lighting direction, camera position, and scale.

