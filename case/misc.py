from solid import *
from solid.utils import *  # Not required, but the utils module is useful

arduino_pro_micro = color(Blue)(
    square([17.8, 33.0], center=True)
)

# width of 10.7: flippable footprint
trrs = color([.3, .3, .3])(square([10.7, 14.1], center=True))

m4_hole = circle(r=4.5/2)

m4_screw = up(1.5)(cylinder(r=4, h=3, center=True)) +\
    down(4)(cylinder(r=2, h=8, center=True))

m2_hole = circle(r=2.5/2)

m2_screw = up(1)(cylinder(r=2, h=2, center=True)) +\
    down(4)(cylinder(r=1, h=8, center=True))
