# AI Construction Video Best Practices

## Summary

The system works when the production remains controlled: one format, clear physical steps, consistent image chain, specific motion prompts, clean editing, and high output volume. Most failures come from asking AI to invent too much at once.

## Rules

### Common Mistakes

- Generating each scene from scratch.
- Asking for one long complete video.
- Skipping the start frame and end frame planning stage.
- Making the video too cinematic and not process-focused.
- Changing camera, lighting, scale, or environment between adjacent steps.
- Accepting weak motion instead of regenerating.

### Prompt Mistakes

- Using vague instructions like "build a secret bunker."
- Not specifying tools, materials, and action order.
- Forgetting worker consistency.
- Forgetting static camera constraints.
- Forgetting timelapse wording.
- Adding too many unrelated visual details that confuse the model.

### Scene Design Mistakes

- Jumping from empty location to finished interior too quickly.
- Missing intermediate construction layers.
- Creating a final reveal that does not answer the hook.
- Showing a normal house instead of a hidden transformation.
- Using locations that are visually bland or hard to understand.

### Physics Mistakes

- Materials appear without being carried, placed, poured, installed, or removed.
- Scale changes between worker, room, pit, hatch, or vehicle.
- Heavy objects move unrealistically.
- Excavation has no removed material nearby.
- Interior build stages ignore structural order.

### Consistency Mistakes

- Different worker clothing between clips.
- Camera moves during process scenes.
- Exterior landscape changes shape.
- Interior room proportions shift.
- Lighting changes without reason.
- Hatch, door, or entrance changes position.

### Scaling Strategy

- Build one strong episode first.
- Turn it into a series by changing location, material, or hidden final use.
- Keep the same production pipeline.
- Track performance by hook type, reveal type, and completion rate.
- Double down on the best-performing structure.

### Content Factory Strategy

- Maintain a concept database.
- Batch scene breakdowns.
- Batch image generation chains.
- Batch video generation prompts.
- Batch editing and export.
- Publish consistently across platforms.

## Checklist

- [ ] Is the idea based on a repeatable format?
- [ ] Does the first frame create curiosity?
- [ ] Is the image chain complete before video generation?
- [ ] Does every generated clip connect two planned frames?
- [ ] Are worker, camera, lighting, and scale consistent?
- [ ] Is the final edit fast, clean, and process-focused?
- [ ] Can this concept become a series?

## Examples

### Good Prompt Direction

One worker uses a shovel to clear snow from inside the marked rectangle. Removed snow piles up around the edges. The camera remains static. The clip is fast timelapse but shows the full clearing process.

Why it works: the action, material, motion, camera, and end state are all specific.

### Bad Prompt Direction

Make the worker build an underground base quickly.

Why it fails: the instruction is too broad, the physical process is undefined, and the generator may skip steps or invent impossible motion.

### Good Scaling Variation

Same structure:

Empty location -> marked area -> excavation -> hidden cover -> underground interior -> final reveal.

Variations:

- Snowfield bunker
- Desert rock bunker
- Backyard pool base
- Abandoned gas station bunker
- Forest cabin trapdoor base

## Reusable Framework

Before producing any episode, run this quality gate:

1. Format: is it a hidden build transformation?
2. Hook: is the first frame instantly curious?
3. Sequence: can the build be broken into physical steps?
4. Images: can every step be made through image-to-image edits?
5. Videos: can every action be shown by one worker in static timelapse?
6. Edit: can the finished story fit into a fast vertical process video?
7. Series: can the same structure produce multiple future episodes?

