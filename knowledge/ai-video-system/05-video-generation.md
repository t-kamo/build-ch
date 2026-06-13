# AI Construction Video System — Video Generation

## Summary

Video generation is not responsible for creating the construction logic.

The image sequence already defines the construction logic.

The role of video generation is to create believable motion between two states.

Start Frame

↓

Transformation

↓

End Frame

The AI should animate the transition.

It should not invent the workflow.

---

# Core Principle

## Motion Between States

Every video clip represents movement between:

Start Frame

↓

End Frame

The generator should show:

- Physical progression
- Material interaction
- Tool usage
- Realistic movement

The generator should never skip directly to completion.

---

# Worker Consistency Rule

Always use one consistent worker.

Default worker:

- Grey hoodie
- Black baseball cap
- Black work pants

The same worker should appear throughout the entire video.

Purpose:

- Visual identity
- Believability
- Consistency

Avoid:

- Multiple workers
- Random outfits
- Different body types between scenes

---

# Timelapse Rule

All construction scenes should be generated as:

Fast realistic timelapse

The viewer must see:

Work

↓

Progress

↓

Completion

Within a short duration.

Prompt phrases:

- Fast realistic timelapse
- Accelerated construction workflow
- Visible construction progress
- Rapid but believable motion

---

# ASMR Rule

Every prompt should emphasize natural construction sounds.

Examples:

- Footsteps
- Shovel digging
- Hammer impacts
- Drilling
- Welding
- Gravel movement
- Material handling

Purpose:

Increase realism.

Prompt phrases:

- Strong ASMR work sounds
- Realistic tool impact sounds
- Natural construction audio

---

# Camera Rules

Default:

Static tripod shot

Requirements:

- No zoom
- No camera shake
- No cinematic transitions
- No unnecessary movement

Purpose:

Focus attention on transformation.

Exception:

Reveal scenes

POV entrance scenes

Interior walkthrough scenes

---

# Transformation Rule

Each scene should show:

Start State

↓

Construction Process

↓

End State

The transformation must be visible.

Avoid:

- Teleporting materials
- Sudden completion
- Missing construction steps

---

# Standard Prompt Structure

Environment

↓

Camera

↓

Worker

↓

Action

↓

Timelapse

↓

ASMR

↓

Transformation Goal

---

# Standard Video Prompt Formula

Cinematic static shot of [environment].

A worker wearing a grey hoodie, black baseball cap, and black work pants performs the construction process.

The scene plays as a fast realistic timelapse.

The worker completes the entire workflow from start state to end state.

Strong ASMR emphasis on realistic construction sounds.

No cuts.

No transitions.

No camera movement.

No teleporting materials.

The transformation must remain physically believable.

---

# Scene Workflow

For every scene:

1. Upload Start Frame
2. Upload End Frame
3. Describe construction actions
4. Generate video
5. Review realism
6. Regenerate if needed

---

# Failure Recovery

If the video:

- Ignores timelapse
- Moves unrealistically
- Skips steps
- Breaks physics
- Changes environment

Do not accept it.

Adjust prompt.

Clarify actions.

Regenerate.

---

# Quality Checklist

Before accepting a clip:

- Worker consistent?
- Camera consistent?
- Environment consistent?
- Timelapse visible?
- Construction visible?
- ASMR emphasized?
- Start frame respected?
- End frame respected?
- Physics believable?

---

# Common Mistakes

Avoid:

- Vague prompts
- Generic "build a bunker" prompts
- Multiple workers
- Camera movement
- Weak timelapse
- Missing ASMR
- Teleporting materials
- Skipping construction stages

---

# Notes

The image sequence controls logic.

The video prompt controls motion.

Strong image sequences produce strong videos.

Weak image sequences cannot be fixed during video generation.
