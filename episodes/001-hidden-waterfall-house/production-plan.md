# Episode001 Production Plan

## Episode

001 Hidden Waterfall House

## Production Strategy

Use the Sprint004 4-stage transformation workflow.

Do not use the original 15-scene construction workflow for image generation.

Nano Banana is better at maintaining environmental consistency across larger transformation states than controlling tiny construction increments.

---

## Stage A

## Objective

Create the clean base image for the entire episode.

The image should establish a massive natural waterfall with no visible entrance and no construction intent.

## Prompt

Photorealistic cinematic wide shot of a massive natural waterfall in a remote forest. The waterfall pours heavily down a dark volcanic cliff face into a misty pool. Dense moss and vegetation cover parts of the cliff and surrounding terrain. Mist rises near the pool. Soft daylight comes from camera left. Static elevated front-facing camera. Natural untouched environment. No visible entrance. No tunnel. No construction markings. No tools. No workers. No artificial structures. No buildings. No lights. No doors. No furniture.

The image should feel like a real remote waterfall location with no visible sign of human construction.

## Success Criteria

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

## Output Filename

`stage-a-natural-waterfall.png`

---

## Stage B

## Objective

Create a believable rough tunnel entrance behind the waterfall.

The entrance should exist, but no interior should be visible.

## Prompt

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

## Success Criteria

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

## Input Image

`stage-a-natural-waterfall.png`

## Output Filename

`stage-b-hidden-entrance.png`

---

## Stage C

## Objective

Create a partially completed interior chamber inside the tunnel.

Natural rock walls should remain dominant.

No luxury elements yet.

## Prompt

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

## Success Criteria

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

## Input Image

`stage-b-hidden-entrance.png`

## Output Filename

`stage-c-interior-chamber.png`

---

## Stage D

## Objective

Create the final luxury hidden waterfall residence.

The result should feel real, desirable, and naturally integrated with the waterfall.

## Prompt

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

## Success Criteria

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

## Input Image

`stage-c-interior-chamber.png`

## Output Filename

`stage-d-final-reveal.png`

---

## Asset Flow

Stage A Output

→ Stage B Input

`stage-a-natural-waterfall.png`

→ `stage-b-hidden-entrance.png`

Stage B Output

→ Stage C Input

`stage-b-hidden-entrance.png`

→ `stage-c-interior-chamber.png`

Stage C Output

→ Stage D Input

`stage-c-interior-chamber.png`

→ `stage-d-final-reveal.png`

---

## Validation Gates

## Gate A — Base Environment

Pass if:

- The waterfall, cliff, vegetation, mist, lighting, camera, and scale are strong and clean.
- No entrance, construction marking, worker, tool, light, door, or artificial object appears.

Fail if:

- The image already suggests an entrance, cave, tunnel, building, or constructed feature.

## Gate B — Hidden Entrance

Pass if:

- Only a small primitive rough tunnel opening is added.
- The waterfall environment remains consistent.
- No interior room, furniture, support beams, door, lighting, tool, worker, or marking appears.

Fail if:

- The entrance becomes finished, framed, artificial, or too large.
- The model reveals an interior room.
- The environment drifts.

## Gate C — Interior Chamber

Pass if:

- The image shows an unfinished interior chamber with dominant natural rock.
- The chamber remains visually connected to the waterfall location.
- Basic floor or waterproofing exists, but no luxury or finished room appears.

Fail if:

- The model jumps directly to a luxury home.
- The chamber disconnects from the waterfall.
- The space becomes too polished or too generic.

## Gate D — Final Reveal

Pass if:

- The image shows a realistic luxury hidden waterfall residence.
- The waterfall identity and natural volcanic rock remain visible.
- Warm lighting, wood, glass, stone, and premium furniture feel grounded and desirable.

Fail if:

- The final image becomes a generic apartment, fantasy palace, sci-fi bunker, or loses the waterfall context.

---

## Lessons Learned

## Sprint001

Environmental consistency is possible when the prompt strongly preserves:

- Same waterfall
- Same cliff face
- Same terrain
- Same lighting direction
- Same camera position
- Same scale

## Sprint002

Nano Banana maintained environment consistency but advanced construction too aggressively during small edits.

Avoid words that imply future construction intent:

- Entrance area
- Excavation preparation
- Expose rock

When testing consistency:

1. Describe the modification only.
2. Do not describe the future purpose of the modification.
3. Explicitly state that no construction progress should occur.
4. Emphasize preservation over transformation.

## Sprint003

For tunnel creation, the prompt should define the desired scale and incompleteness clearly:

- Small rough tunnel opening
- Just large enough for one adult person to crouch through
- Unfinished and primitive
- Early-stage excavation
- No interior room
- No artificial structures

## Sprint004

The workflow should shift from fine-grained construction stages to 4 major transformation states:

1. Natural Waterfall
2. Hidden Entrance
3. Interior Chamber
4. Final Reveal

This aligns with Nano Banana strengths:

- Environmental consistency
- Larger transformation steps
- Strong visual endpoint generation

Avoid visible construction markings because they trigger aggressive excavation behavior.

