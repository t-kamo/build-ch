# Episode001 Veo Prompt Rules

## Purpose

These rules prevent character duplication, teleportation, unstable motion, and unrealistic construction jumps during Episode001 Hidden Waterfall House video generation.

Use these rules for every Veo prompt in Storyboard v2.

## Core Rule Block

Include this block in every Veo prompt:

```text
Only one identical adult male worker is visible.
Never duplicate the character.
No additional people.
No teleportation.
No sudden time jump.
No sudden body position changes.
Same location and same camera angle.
Same waterfall, same rock wall, same forest, same entrance position.
Small realistic progress between frames.
Physically plausible manual construction.
The worker remains in the visible work area and moves continuously.
```

## Character Lock

The worker must remain:

- one adult male
- same face and body type
- same outfit across all clips
- grey hoodie
- black baseball cap
- black work pants
- brown or dark work boots
- black work gloves

Do not allow:

- second worker
- background worker
- duplicate body
- outfit change
- age change
- face change
- sudden character replacement

## Camera Lock

Default camera:

- fixed tripod
- same elevated front-facing angle
- same framing
- same scale
- same waterfall position
- same cliff position
- same entrance position

Allowed camera movement:

- very slow dolly-in for reveal moments only
- no handheld shake
- no fast zoom
- no cut
- no orbit
- no perspective jump

## Location Lock

Preserve:

- massive waterfall
- dark volcanic rock wall
- dense forest
- mist near the pool
- entrance position behind or beside the waterfall
- rock ledge and work area scale
- lighting direction

Do not change:

- waterfall shape
- cliff silhouette
- forest density
- entrance location
- room scale
- camera angle

## Progress Rule

Each clip should show one small change only.

Good progress:

- clearing a small patch
- removing a few loose rocks
- deepening the recess slightly
- moving a small pile of rubble
- placing one timber beam
- installing a small section of floor
- adding one lantern

Bad progress:

- complete cave appears suddenly
- furniture appears all at once
- multiple workers complete the build
- finished architecture replaces rough rock
- the worker jumps to a new position
- the camera cuts to a new location

## Motion Rule

Motion should be continuous and physically believable.

Use:

- slow manual digging
- carrying stones by hand
- dragging small debris
- placing timber carefully
- wiping dust
- turning on lanterns
- dust settling
- water and mist moving naturally

Avoid:

- instant material movement
- teleporting tools
- fast time jump
- impossible excavation volume
- sudden lighting change without visible cause

## Negative Prompt Block

Use this negative prompt for every Veo generation:

```text
No duplicate people.
No second worker.
No crowd.
No teleportation.
No sudden time jump.
No sudden camera cut.
No camera angle change.
No changing waterfall.
No changing cliff shape.
No changing entrance location.
No instant construction.
No sudden completed room.
No impossible excavation.
No floating objects.
No extra doors.
No extra rooms.
No major architecture transformation within one clip.
```

