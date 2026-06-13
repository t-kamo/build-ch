# Sprint002 Findings

## Finding #001 — Change Magnitude Control Failure

## Validation Context

Sprint002 Scene04 — Rock Clearing

Objective:

Maintain environmental consistency while making only a minor surface-level modification to the marked construction area.

## Expected Result

Only minor surface cleaning inside the marked rectangle:

- Remove small amounts of moss
- Remove loose rock
- Expose slightly more bare stone

No excavation should occur.

## Actual Result

Nano Banana created a partially excavated recess inside the marked area.

The model interpreted the modification as the beginning of tunnel excavation rather than simple surface cleaning.

Environmental consistency remained successful:

- Same waterfall
- Same cliff
- Same camera angle
- Same lighting
- Same scale

However, construction progression advanced too far.

## Failure Type

Change Magnitude Control Failure

The environment remained stable, but the amount of construction change exceeded the intended scene objective.

## Root Cause

Nano Banana appears to associate the following phrases with construction activity:

- Entrance area
- Exposed rock
- Clearing

These terms implicitly suggest future excavation.

The model tends to anticipate later construction stages rather than limiting itself to the requested modification.

## Countermeasure

Avoid wording that implies future construction intent.

Prefer:

- Surface cleaning only
- Cosmetic cleaning only
- Remove vegetation only
- Preserve rock face

Avoid:

- Entrance preparation
- Entrance area
- Excavation preparation
- Expose rock for entry

## Prompt Engineering Rule

When validating environmental consistency:

1. Describe the modification only.
2. Do not describe the future purpose of the modification.
3. Explicitly state that no construction progress should occur.
4. Emphasize preservation over transformation.

## Template Update

Added to `templates/image-prompt-template.md`:

"When testing consistency, avoid language that implies future construction stages. Describe only the visual modification being requested."

