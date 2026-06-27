# Episode002 Lessons Learned

## Finding — Image-to-Image Reverse Workflow

Image-to-Image generation from the accepted final image provides sufficient visual consistency for sequential construction stages.

This becomes the default workflow.

Preferred sequence:

Stage I -> Stage H -> Stage G -> ...

This is preferred over generating each image independently.

Production rule:

Generate and approve the final reveal first, then work backward through earlier stages using the accepted final image or latest approved reverse-stage image as the visual reference.

