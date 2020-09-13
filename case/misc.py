from solid import *
from solid.utils import *  # Not required, but the utils module is useful

arduino_pro_micro_2d = color([.004, 58.0/255, 147.0/255, .5])(
    polygon(points=[
        [-17.8,  8.9],
        [15.2,  8.9],
        [15.2, -8.9],
        [-17.8, -8.9],
    ])
)

# width of 10.7: flippable footprint
# trrs = color([.3, .3, .3])(square([10.7, 14.1], center=True))
trrs = color([.3, .3, .3])(mirror([0, 1, 0])(
    polygon(points=[
        [-5.35, 12.1],
        [5.35, 12.1],
        [5.35, 0],
        [5.1, 0],
        [5.1, -2],
        [-5.1, -2],
        [-5.1, 0],
        [-5.35, 0],
    ])
))

resistor_hybrid = polygon(points=[
    [-4.7, -1.1],
    [4.7, -1.1],
    [4.7, 1.1],
    [-4.7, 1.1],
])

switch_6mm = polygon(points=[
    [-1.5, 1.5],
    [8, 1.5],
    [8, -6],
    [-1.5, -6],
])

jumper = polygon(points=[
    [-1.65, -1.24],
    [1.65, -1.24],
    [1.65, 1.24],
    [-1.65, 1.24],
])


m4_hole = circle(r=4.5/2)

m4_screw = up(1.5)(cylinder(r=4, h=3, center=True)) +\
    down(4)(cylinder(r=2, h=8, center=True))

m2_hole = circle(r=2.5/2)

m2_screw = up(1)(cylinder(r=2, h=2, center=True)) +\
    down(4)(cylinder(r=1, h=8, center=True))
