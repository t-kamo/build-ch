# Findings

## Finding: H_to_I Video Rejection

The first real H_to_I Veo output was rejected.

Issues:

- Multiple people appeared.
- The main character teleported.
- Motion continuity was unstable.

Likely cause:
Using both Stage H and Stage I as reference frames can cause interpolation conflicts when the character position, pose, or scene layout differs too much.

Decision:
For near-complete reveal transitions, prefer start-frame-only image-to-video first.
Use a locked camera, one visible character, minimal movement, and lighting/reveal changes instead of large construction changes.

