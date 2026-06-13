# AI Construction Video Image Generation

## Summary

Image generation is the control layer of the entire system. Build the full scene sequence as still images before generating video. Each image becomes either a start frame or end frame for a short video segment.

The key rule is image-to-image continuity: generate the first strong frame, then modify the previous correct frame one step at a time.

## Rules

### Scene Construction Workflow

Build the scene visually before asking for motion. The practical workflow is:

1. Create the base image.
2. Edit the base image into the next construction state.
3. Continue image-to-image edits until the full scene chain is complete.
4. Pair adjacent images as start frame and end frame.
5. Send each pair to video generation as one controlled motion task.

### Start Frame Logic

- The start frame shows the current physical state before a construction action.
- It must be clear, stable, and readable.
- It should contain all persistent elements needed in the next frame.
- It should not include the result of the action that the next video clip will show.

### End Frame Logic

- The end frame shows the completed result of one specific construction action.
- It should change only what the scene step requires.
- It must preserve camera angle, environment, lighting, scale, and persistent objects.
- It becomes the start frame for the next scene.

### Image-to-Image Workflow

- Do not generate each scene from scratch.
- Upload the previous successful image.
- Ask for one logical modification.
- Keep everything else unchanged.
- Repeat until the full construction chain exists.

### Environment Consistency

- Preserve terrain, room dimensions, horizon, walls, ceiling, and object placement.
- For exterior scenes, keep the same landscape and weather.
- For interior scenes, keep the same room proportions and lighting source.
- When changing from exterior to interior, create a new interior base frame, then continue image-to-image from that point.

### Camera Consistency

- Use the same camera angle and framing within a scene chain.
- Exterior construction often works well as high-angle wide or drone-style framing.
- Interior construction works well as static wide shot, straight-on, symmetrical framing.
- Avoid switching focal length or camera position unless it is a deliberate new section.

### Lighting Consistency

- Keep lighting stable across adjacent frames.
- Exterior examples can use cold natural daylight or soft overcast light.
- Interior bunker examples can use warm practical lantern light.
- Do not let the model randomly add cinematic lighting that breaks continuity.

### Scene Progression Rules

- One image equals one physical construction state.
- Each state should be more complete than the last.
- Avoid impossible jumps, teleporting materials, or inconsistent scale.
- Include material leftovers when appropriate: dirt piles, ice chunks, removed snow, tools, beams, panels.

## Underground Construction Example

Example image chain:

1. Empty remote landscape with a marked construction zone
2. Same scene with the marking removed for a clean base option
3. Same marked area with snow or grass cleared
4. Same area with shallow excavation
5. Same area with deeper excavation
6. Steel beams placed over the pit
7. Plates installed with one visible hatch
8. Surface camouflaged with snow, soil, or grass while hatch remains readable
9. New interior base frame inside underground room
10. Floor tarp installed
11. Floor frame installed
12. Insulation installed
13. OSB floor installed
14. Wall tarp installed
15. Wall frame installed
16. Wall insulation installed
17. OSB wall panels installed
18. Electrical details installed
19. Rubber flooring installed
20. First furniture and functional objects added
21. Final decorated survival space

## Checklist

- [ ] Is every image based on the previous correct image?
- [ ] Does each step modify only one construction layer?
- [ ] Are camera angle and framing preserved?
- [ ] Is lighting consistent?
- [ ] Are materials physically plausible?
- [ ] Is the end frame usable as the next start frame?
- [ ] Are exterior and interior chains separated cleanly?

## Examples

### Image Edit Prompt Pattern

Keep the same environment, camera angle, framing, perspective, scale, and lighting. Modify only the marked construction area by adding the next physical construction step: [specific action]. Preserve all existing objects that should remain. The result should look like [clear end state].

### Interior Continuity Prompt Pattern

Maintain the same room proportions, camera angle, lantern position, wall texture, ceiling structure, and warm practical lighting. Add [specific material layer] to [floor/walls/ceiling] only. Do not change anything else in the room.

## Reusable Framework

For each episode, create:

1. Exterior base chain: location -> marking -> excavation -> cover -> camouflage.
2. Transition frame: hatch, entrance, door, or POV entry.
3. Interior base chain: raw room -> structural layers -> utilities -> surfaces -> final decor.
4. Start/end frame pairs: each adjacent pair becomes one video generation task.
