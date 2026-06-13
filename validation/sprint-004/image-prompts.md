# Sprint 004 — 4-Stage Transformation Image Prompts

## Purpose

Redesign the image generation workflow based on Sprint001-Sprint003 findings.

Nano Banana successfully maintains environmental consistency.

However, Nano Banana tends to skip small construction stages and aggressively infer future excavation.

This sprint replaces the fine-grained 15-scene construction workflow with a 4-stage transformation workflow.

## Strategy Shift

Optimize for:

- Environmental consistency
- Large transformation steps
- Nano Banana strengths

Instead of:

- Fine-grained construction stages
- Small surface-level edits
- Visible construction markings
- Step-by-step excavation control

## Critical Findings

### Finding #001

Avoid words:

- Entrance area
- Excavation preparation
- Expose rock

These cause premature excavation.

### Finding #002

Visible markings trigger aggressive excavation behavior.

Avoid construction markings.

## Global Environment Lock

Massive natural waterfall in a remote forest. Dark volcanic cliff face. Dense moss and vegetation. Heavy water flow. Mist near the pool. Soft daylight from camera left. Static elevated front-facing camera. Photorealistic style.

Maintain:

- Same waterfall
- Same cliff face
- Same terrain
- Same vegetation
- Same lighting direction
- Same camera position
- Same scale

Do not add construction markings unless explicitly requested.

Do not use visible paint, chalk, spray lines, flags, stakes, measurement grids, or guide marks.

---

# Stage A — Natural Waterfall

## Purpose

Create the clean base image for the entire transformation sequence.

This stage establishes the environment only.

No construction intent should be visible.

## Input Image

None. Generate as the initial base image.

## End Frame Prompt

Photorealistic cinematic wide shot of a massive natural waterfall in a remote forest. The waterfall pours heavily down a dark volcanic cliff face into a misty pool. Dense moss and vegetation cover parts of the cliff and surrounding terrain. Mist rises near the pool. Soft daylight comes from camera left. Static elevated front-facing camera. Natural untouched environment. No visible entrance. No tunnel. No construction markings. No tools. No workers. No artificial structures. No buildings. No lights. No doors. No furniture.

The image should feel like a real remote waterfall location with no visible sign of human construction.

## Validation Checklist

- Massive waterfall is clear and visually strong
- Dark volcanic cliff face is visible
- Dense moss and vegetation are present
- Mist near the pool is visible
- Soft daylight comes from camera left
- Static elevated front-facing camera is established
- No entrance visible
- No construction markings
- No artificial objects
- No worker
- Photorealistic style

## Failure Modes

### Hidden Opening Appears Too Early

The model adds a cave, tunnel, doorway, shadow entrance, hatch, or visible gap.

### Artificial Object Injection

The model adds stairs, railing, bridge, lights, tools, signs, doors, or buildings.

### Weak Base Environment

The waterfall is too small, the cliff face is unclear, or the location does not feel remote and cinematic.

---

# Stage B — Hidden Entrance

## Purpose

Create the first major transformation: a believable rough tunnel entrance behind the waterfall.

The entrance should exist, but no interior should be visible.

## Input Image

Use Stage A End Frame as the base image.

## End Frame Prompt

Use the provided image as the base image.

Keep everything else exactly the same.

Change only the hidden rock surface behind the waterfall.

Create a small rough tunnel opening behind the waterfall, just large enough for one adult person to crouch through. The opening should remain unfinished and primitive. It should look like a natural rough cut into dark volcanic rock, not a completed doorway. The tunnel mouth should be dark and shallow, with no visible interior room.

Preserve the same waterfall shape, same dark volcanic cliff face, same dense moss and vegetation outside the opening, same terrain, same mist near the pool, same soft daylight from camera left, same static elevated front-facing camera, same perspective, and same scale.

Do not add construction markings. Do not add paint, chalk, spray lines, stakes, flags, or measurement marks.

Do not reveal an interior room.

Do not add furniture.

Do not add lighting.

Do not add support beams.

Do not add doors.

Do not add artificial structures.

Do not add tools.

Do not add workers.

The final image should show the same waterfall environment with only a small primitive rough tunnel opening behind the waterfall.

## Validation Checklist

- Same waterfall shape as Stage A
- Same cliff geometry except the tunnel mouth
- Same terrain and vegetation
- Same lighting direction from camera left
- Same static elevated front-facing camera
- Same scale
- Opening is human-sized but small
- Opening is rough natural rock
- Opening looks primitive and unfinished
- No interior room visible
- No markings
- No support beams, doors, lights, furniture, tools, or workers

## Failure Modes

### Overbuilt Entrance

The opening becomes a finished doorway, framed entrance, concrete portal, metal hatch, or designed architectural feature.

### Interior Reveal

The model shows a visible room, hallway, lit cave, furniture, or luxury space inside.

### Construction Marking Regression

The model adds paint, chalk, guide lines, stakes, flags, or measurement marks.

### Environment Drift

The waterfall, cliff, lighting, camera, terrain, vegetation, or scale changes.

---

# Stage C — Interior Chamber

## Purpose

Create the second major transformation: a partially completed interior chamber inside the tunnel.

This stage should show habitability beginning, but natural rock should remain dominant.

No luxury elements yet.

## Input Image

Use Stage B End Frame as the base image.

## End Frame Prompt

Use the provided image as the base image.

Keep the waterfall location and exterior environment consistent.

Transition the view slightly inside the rough tunnel entrance, while preserving the same waterfall context, dark volcanic rock, natural material logic, and scale.

Show a partially completed interior chamber carved into dark volcanic rock behind the waterfall. Natural rough rock walls remain dominant. The chamber has a simple leveled stone floor, basic waterproof floor layer, rough unfinished wall sections, and minimal construction progress. The space should feel early-stage and partially completed, not luxurious.

The waterfall should still be visually connected to the space through the entrance or visible mist/light spill.

Do not add luxury furniture.

Do not add glass walls.

Do not add premium wood finishes.

Do not add decorative lighting.

Do not add polished surfaces.

Do not add beds, sofas, kitchen, shelves, or resort features.

Do not add a finished room.

The final image should show a believable rough interior chamber with natural rock walls still dominant and only basic early-stage construction elements.

## Validation Checklist

- Same waterfall location remains visually connected
- Natural dark volcanic rock remains dominant
- Interior chamber is visible but unfinished
- Chamber scale feels human and believable
- Basic floor or waterproof layer is present
- No luxury furniture
- No glass walls
- No premium finishes
- No decorative lighting
- No polished final room
- No sudden complete residence

## Failure Modes

### Luxury Jump

The model skips ahead to a finished luxury home with furniture, polished floors, glass, warm lighting, or decor.

### Environment Disconnect

The chamber no longer feels connected to the waterfall location.

### Artificial Overconstruction

The model adds too many beams, panels, lights, doors, stairs, or finished architectural elements.

### Scale Drift

The chamber becomes too large, too small, or inconsistent with the Stage B tunnel entrance.

---

# Stage D — Final Reveal

## Purpose

Create the final transformation: a luxury hidden waterfall residence.

This is the payoff image.

The result should feel real, desirable, and naturally integrated with the waterfall.

## Input Image

Use Stage C End Frame as the base image.

## End Frame Prompt

Use the provided image as the base image.

Keep the same waterfall location, same dark volcanic rock identity, same natural stone context, same scale, and same spatial relationship to the entrance.

Transform the partially completed interior chamber into a finished luxury hidden waterfall residence. Add warm layered lighting, natural stone integration, premium wood flooring, glass accents, comfortable furniture, refined built-in storage, soft textiles, and a calm premium atmosphere. The natural volcanic rock should still remain visible and integrated into the design.

The waterfall should remain visually connected to the residence through the entrance, mist, reflected light, or view toward the falling water.

The final image should feel like a real hidden luxury home built behind a massive waterfall, not a fantasy palace and not a sci-fi bunker.

Maintain photorealistic materials, believable proportions, and grounded architecture.

Do not change the waterfall identity.

Do not change the overall cliff environment.

Do not make the space futuristic.

Do not make it look like a generic apartment.

Do not remove all natural rock.

## Validation Checklist

- Same waterfall identity remains connected
- Natural dark volcanic rock remains visible
- Warm premium lighting is present
- Wood, glass, stone, and furniture feel realistic
- Residence feels desirable and livable
- Space does not look futuristic
- Space does not look like a generic apartment
- Scale feels believable
- Final reveal creates strong emotional payoff
- Environment remains tied to the original waterfall concept

## Failure Modes

### Generic Luxury Interior

The result looks like a normal apartment, hotel room, or generic luxury room with no waterfall identity.

### Fantasy Overdesign

The model creates an impossible palace, sci-fi bunker, glowing fantasy cave, or unrealistic mega-room.

### Natural Context Loss

The volcanic rock, waterfall connection, mist, or natural environment disappears.

### Material Inconsistency

Materials look artificial, plastic, over-polished, or inconsistent with a real hidden waterfall residence.

---

# Sprint Decision

Continue with the 4-stage transformation workflow if:

- Stage A creates a strong natural base.
- Stage B creates a believable rough entrance without overbuilding.
- Stage C creates an unfinished interior chamber without jumping to luxury.
- Stage D creates a desirable final residence while preserving waterfall identity.

Return to prompt redesign if:

- The model repeatedly creates construction markings.
- The model skips Stage C and jumps directly to final luxury.
- The model loses the waterfall environment.
- The model cannot preserve scale between stages.

