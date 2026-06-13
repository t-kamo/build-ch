# AI Construction Video Generation

## Summary

Video generation converts controlled image pairs into realistic motion. Each clip should show one construction action between a start frame and an end frame.

The system depends on strict prompt control: one worker, static camera, fast timelapse, real physical workflow, ASMR material focus, and no fake shortcuts.

## Rules

### Video Generation Workflow

Generate video scene by scene. Do not create one long video in a single request.

1. Upload the start frame.
2. Upload the end frame.
3. Describe the physical transformation between them.
4. Enforce one worker, static camera, timelapse, ASMR, and realism constraints.
5. Generate the clip.
6. Reject or regenerate if motion, physics, scale, or continuity fails.

### Worker Consistency Rule

- Use one consistent worker across construction scenes.
- Keep clothing, scale, and behavior stable.
- A useful worker profile: grey hoodie, black cap, black work pants or overalls, realistic construction movement, no posing.
- Do not add extra workers unless the concept absolutely requires it.
- One worker gives the AI fewer variables and makes the process easier to control.

### Timelapse Rule

- Most construction clips should be fast realistic timelapse.
- State that the full process must remain visible.
- Motion can be accelerated, but the physical sequence must be readable.
- If the model creates slow or incomplete action, regenerate with stronger speed and process wording.

### ASMR Rule

- Include material and tool sound focus in prompts.
- Useful ASMR anchors: shovel scraping, dirt movement, gravel pouring, hammer hits, metal contact, welding sparks, tarp sliding, insulation placement, drilling screws, rubber tiles snapping.
- Even if the final platform mutes or reduces audio, ASMR language helps guide realistic tactile motion.

### Static Camera Rule

- Most build clips should use a static tripod-style camera.
- Avoid camera movement, zooms, cuts, transitions, and visual effects during construction clips.
- Static framing makes the transformation easier to read.
- Use moving camera only for intentional entry shots or final reveal shots.

### Transformation Rule

- The clip must begin in the start state and end in the end state.
- The worker action must explain the transformation.
- Never prompt vague actions like "build the bunker."
- Describe the tool, action, material, order, and final state.

### Prompt Structure

Use this order:

1. Shot type and camera: static high-angle wide shot, interior wide shot, POV reveal, etc.
2. Environment: exact location and persistent scene details.
3. Start state: what already exists at the beginning.
4. Worker identity: one worker with consistent clothing and scale.
5. Action: specific physical work in order.
6. Timelapse: fast but readable full workflow.
7. End state: what must be completed by the end.
8. Constraints: no cuts, no zoom, no extra workers, no instant transformation.
9. ASMR: specific material and tool sounds.
10. Realism: correct proportions, believable physics, consistent lighting.

## Failure Recovery Process

If a generated clip fails:

- Identify the exact failure: wrong worker, weak motion, skipped steps, camera movement, physics error, inconsistent scale, wrong material, or bad ending.
- Rewrite only the part of the prompt that failed.
- Strengthen constraints instead of adding unrelated detail.
- Regenerate from the same start/end frames.
- If repeated failures happen, simplify the action into smaller clips.

## Regeneration Process

1. Keep the same start and end frames.
2. Add a clearer action sequence.
3. Add "only one worker" if extra people appear.
4. Add "continuous static shot" if the camera moves.
5. Add "full real workflow" if the model jumps to the result.
6. Add "fast realistic timelapse" if motion is too slow.
7. Add specific tool and material sounds if motion lacks tactile realism.

## Checklist

- [ ] Does the clip use a start frame and end frame?
- [ ] Is there only one worker?
- [ ] Is the camera static for construction scenes?
- [ ] Is the action described physically and sequentially?
- [ ] Is timelapse explicitly requested?
- [ ] Is ASMR material handling included?
- [ ] Are cuts, zooms, transitions, and visual effects prohibited?
- [ ] Does the final state match the end frame?

## Examples

### Construction Clip Prompt Pattern

Cinematic static wide shot of [location], matching the start frame. The camera is locked on a tripod with no movement. One worker wearing [consistent clothing] performs the full construction step: [tool/action/material sequence]. The scene plays as fast realistic timelapse, but the complete physical workflow remains visible. By the end, [specific end state]. No cuts, no transitions, no zoom, no extra workers, no instant transformation. Strong ASMR focus on [material sounds]. Realistic proportions, natural lighting, believable physics.

### Final Reveal Prompt Pattern

Cinematic reveal shot of the completed hidden space. The camera slowly moves forward and gently looks around the room, showing the finished materials, lighting, furniture, and functional details. No people are needed unless the worker is part of the reveal. Keep movement smooth, realistic, and quiet with ambient ASMR atmosphere.

## Reusable Framework

For each video scene:

1. Pair two adjacent images.
2. Define the single action that connects them.
3. Write the prompt using worker, timelapse, static camera, ASMR, and realism constraints.
4. Generate.
5. Reject weak motion.
6. Regenerate or split the action until the clip is believable.
