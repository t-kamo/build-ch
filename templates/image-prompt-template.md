# AI Construction Video — Image Prompt Template

---

# Core Principle

Every image should only introduce ONE logical construction change.

The image sequence defines the transformation.

The video generation stage only animates the transformation.

---

# Image Generation Workflow

Concept

↓

Scene Breakdown

↓

Start Frame

↓

End Frame

↓

Image-to-Image

↓

Next Scene

---

# Global Consistency Rules

Maintain:

- Same camera angle
- Same framing
- Same perspective
- Same environment
- Same weather
- Same lighting direction
- Same scale

Do not change:

- Background
- Terrain
- Structure dimensions
- Camera position

Unless explicitly required.

---

# Prompt Template

## Scene Information

Scene Number:

[SCENE_NUMBER]

Scene Name:

[SCENE_NAME]

---

## Environment

[ENVIRONMENT]

Examples:

- Waterfall
- Cave
- Forest
- Cliff
- Snow Mountain
- Abandoned Tunnel

---

## Camera

Keep the same:

- Camera position
- Perspective
- Framing
- Lens style

Static tripod shot.

---

## Existing State

Describe current condition.

Example:

Rock wall with no visible entrance.

---

## Modification

Describe ONE change only.

Examples:

- Remove rocks
- Dig excavation pit
- Add steel frame
- Install insulation
- Add furniture

---

## Materials

Specify:

- Wood
- Concrete
- Steel
- Stone
- Glass
- Insulation

---

## Lighting

Keep consistent.

Specify:

- Daylight
- Overcast
- Sunset
- Interior warm lighting

---

## Realism Rules

Requirements:

- Physically believable
- Realistic proportions
- Consistent materials
- No floating objects
- No impossible geometry

---

## End State

Clearly describe expected result.

Example:

A completed excavation pit with visible steel support beams.

---

# Standard Prompt Formula

Photorealistic construction scene.

Environment:
[ENVIRONMENT]

Camera:
Maintain identical camera position, framing, perspective, and scale from the previous scene.

Current State:
[EXISTING_STATE]

Modification:
Only add or modify [SPECIFIC_CHANGE].

Materials:
[MATERIALS]

Lighting:
[LIGHTING]

Maintain environmental consistency.

Do not change weather, terrain, background, camera angle, or scale.

The result must look physically realistic and logically connected to the previous scene.

Final state:
[END_STATE]

---

# Start Frame Template

Purpose:

Show the beginning of the construction action.

Include:

- Existing environment
- Existing construction state
- Clear visibility of work area

---

# End Frame Template

Purpose:

Show completed result of current action.

Include:

- Finished modification
- Clear visual progression
- Ready for next scene

---

# Quality Checklist

Before accepting image:

- Same camera?
- Same environment?
- Same scale?
- One clear change?
- Physically realistic?
- Strong visual progression?
- Suitable as Start Frame?
- Suitable as End Frame?

---

# Common Mistakes

Avoid:

- Generating from scratch every scene
- Multiple changes at once
- Camera shifts
- Weather changes
- Random redesigns
- Unrealistic proportions
- Weak visual progression

---

# Example

Concept:

Hidden Waterfall House

Scene:

Excavation

Start State:

Rock wall behind waterfall.

Modification:

Excavate entrance tunnel.

End State:

Tunnel entrance visible with removed debris.

Environment, camera, lighting, and scale remain unchanged.
