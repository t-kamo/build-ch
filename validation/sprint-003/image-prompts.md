# Sprint 003 — Image Prompt Validation

## Purpose

Validate whether Nano Banana can transform a shallow excavation into a believable human-sized tunnel entrance while maintaining environmental consistency.

Sprint002 demonstrated that environmental consistency is achievable. Sprint003 focuses on controlled construction progression.

## Validation Target

Scene06 — Tunnel Entrance

## Success Criteria

- Same waterfall
- Same cliff
- Same camera
- Same lighting
- Same scale
- Only the excavation area changes

## Environment Lock

Massive natural waterfall in a remote forest. Dark volcanic cliff face. Dense moss and vegetation. Heavy water flow. Mist near the pool. Soft daylight from camera left. Static elevated front-facing camera. Photorealistic style.

Do not change:

- Waterfall shape
- Cliff geometry outside the excavation area
- Vegetation outside the excavation area
- Weather
- Terrain
- Lighting direction
- Camera position
- Scale

---

## Scene06 — Tunnel Entrance

## Prompt

Use the provided image as the base image.

Keep everything else exactly the same.

Change only the existing shallow excavation area.

The base image already shows a shallow rough recess in the dark volcanic cliff face behind the waterfall, with small broken rock chips at the base. Enlarge only that shallow recess into a small human-sized tunnel entrance. The opening should be rough natural volcanic rock, dark inside, physically believable, and just large enough for one adult person to enter.

Preserve the natural rock face around the opening. Preserve the existing marked area if visible. Preserve the same waterfall shape, same dark volcanic cliff, same dense moss and vegetation outside the opening, same terrain, same mist near the pool, same soft daylight from camera left, same static elevated front-facing camera, same perspective, and same scale.

The opening must remain a simple rough natural tunnel entrance only. Show a short dark tunnel mouth, not an interior room.

Do not reveal an interior room.

Do not add furniture.

Do not add lighting.

Do not add support beams.

Do not add doors.

Do not add artificial structures.

Do not add tools.

Do not add workers.

Do not change the waterfall, cliff, vegetation, terrain, lighting, camera, or scale.

Final image should show the same waterfall environment with only the shallow excavation changed into a believable human-sized rough tunnel entrance.

## Validation Checklist

- Same waterfall shape as the input image
- Same cliff face outside the excavation area
- Same camera position and framing
- Same lighting direction from camera left
- Same scale
- Same terrain, mist, and vegetation outside the excavation area
- Only the excavation area changes
- Opening is human-sized
- Opening is rough natural rock
- Opening is physically believable
- Only a short dark tunnel mouth is visible
- No interior room is revealed
- No furniture
- No lighting
- No support beams
- No doors
- No artificial structures
- No tools or workers

## Expected Result

The output should preserve the full Sprint002 environment while converting the existing shallow recess into a small, rough, human-sized tunnel entrance behind the waterfall.

The viewer should understand that the cliff now has a believable entrance, but should not see any finished interior, structure, lights, doors, supports, or furniture.

## Failure Modes

### Environment Drift

The waterfall, cliff shape, camera angle, terrain, lighting, vegetation, mist, or scale changes.

### Overbuilding

The model adds support beams, doors, lighting, furniture, interior rooms, stairs, floors, or decorative elements.

### Underbuilding

The recess remains too shallow and does not read as a human-sized entrance.

### Interior Reveal

The model shows a finished room, cave chamber, hallway, or living space beyond the entrance.

### Artificial Structure Injection

The model turns the natural tunnel mouth into a man-made doorway, metal hatch, concrete portal, framed opening, or designed entrance.

### Scale Failure

The entrance becomes too large, too small, or inconsistent with a single adult person entering.

