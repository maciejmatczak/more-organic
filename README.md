# More organic

## Parametric design

Last time Freecad was used to achieve the parametric design of plate and rest of case parts.

Now, the whole design is more complicated - keys are orthogonal (Freecad handled that easily with multi transform), but column stagger + thumb cluster.

First step was to somehow define and parametrize the design itself and save that data (`build/design/design.json`). This data is later used as source for rest of the parts:

- case (Openscad, but with SolidPython):
  - plate
- pcb (Kicad)

## Case

Based on base design (switch coordinates), with use of SolidPython, the plate design is generated:

![Openscad plate](images/case.png)

Additionally, a collisions are shown in red (need of a manual validation):

![Openscad plate](images/case-collision.png)
