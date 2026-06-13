# AI Construction Video System — Image Generation

## Summary

Image generation is the foundation of the entire video system.

Do not start with video generation.

First, build the full visual sequence using images.

The objective is to create a controlled scene progression that can later be converted into video.

Bad images create bad videos.

Strong images create believable motion.

---

# Core Principle

## Image First Strategy

Before generating any video, create the full sequence as images.

Each image represents a construction stage.

The image sequence must show logical progression.

Example:

Empty location

↓

Marked area

↓

Excavated area

↓

Structural frame

↓

Insulation

↓

Interior build

↓

Final reveal

---

# Start Frame / End Frame Logic

Every video clip is created from two images:

Start Frame

↓

End Frame

The video generator creates motion between these two states.

The AI should not invent the construction logic.

The image sequence defines the logic.

---

# Image-to-Image Workflow

Do not generate every scene from scratch.

Use the previous image as the input for the next image.

Workflow:

1. Generate the first base image
2. Use that image as input
3. Modify only the next logical construction element
4. Keep everything else consistent
5. Repeat until the full sequence is complete

This prevents AI randomness.

---

# Consistency Rules

Maintain the same:

- Camera angle
- Framing
- Perspective
- Environment
- Lighting
- Scale
- Material logic

Do not randomly change:

- Background
- Weather
- Worker scale
- Camera position
- Room dimensions

---

# Scene Progression Rules

Each scene must answer:

What changed from the previous image?

The answer should be simple and physical.

Good:

- Snow removed from marked area
- Hole deepened
- Steel beams added
- Floor insulation installed
- Wall panels added

Bad:

- Random design change
- Finished structure appears suddenly
- Camera angle changes
- Materials teleport

---

# Exterior Sequence Example

For underground or hidden base videos:

1. Empty environment
2. Marked construction area
3. Surface cleared
4. First excavation
5. Deeper excavation
6. Structural frame added
7. Plates or cover added
8. Camouflage added
9. Entrance or hatch visible

---

# Interior Sequence Example

After entering underground or hidden space:

1. Empty interior base frame
2. Floor liner installed
3. Floor frame installed
4. Insulation installed
5. Floor panels installed
6. Wall liner installed
7. Wall frames installed
8. Wall insulation installed
9. Wall panels installed
10. Lighting and furniture installed
11. Finished interior reveal

---

# Prompt Structure

Each image prompt should include:

- Environment
- Camera angle
- Existing state
- Exact modification
- Materials
- Scale
- Lighting
- Consistency instructions
- Final expected result

---

# Standard Image Prompt Formula

Keep the same [environment], [camera angle], [framing], and [perspective].

Starting from the existing scene, add/change only [specific construction element].

The change should look physically realistic and consistent with the previous scene.

Maintain the same lighting, scale, material textures, and background.

Final scene should look like [clear end state].

---

# Quality Checklist

Before accepting an image:

- Does it match the previous scene?
- Is the camera consistent?
- Is the environment consistent?
- Is the change physically logical?
- Is the construction stage clear?
- Can this become a Start Frame or End Frame for video?
- Is there enough visual difference from the previous image?

---

# Common Mistakes

Avoid:

- Regenerating from scratch
- Changing camera angle
- Changing environment
- Skipping construction steps
- Creating impossible physical changes
- Adding too many changes at once
- Making the end frame unclear

---

# Notes

The image sequence is the blueprint.

The video generation step should only animate the transformation already defined by the image sequence.

If the image sequence is weak, the video will be weak.
