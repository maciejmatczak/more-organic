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
arduino_pro_micro_3d = \
    color([.004, 58.0/255, 147.0/255, .5])(
        linear_extrude(1.6)(arduino_pro_micro_2d)
    ) +\
    up(2)(
        color([.6, .6, .6, .5])(
            linear_extrude(2)(
                polygon(points=[
                    [-19.3, -3.8],
                    [-14.2, -3.8],
                    [-14.2, 3.8],
                    [-19.3, 3.8],
                ])
            )
        )
    )

# width of 10.7: flippable footprint
# trrs = color([.3, .3, .3])(square([10.7, 14.1], center=True))
trrs = color([.3, .3, .3])(
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
)

m4_hole = circle(r=4.5/2)

m4_screw = up(1.5)(cylinder(r=4, h=3, center=True)) +\
    down(4)(cylinder(r=2, h=8, center=True))

m2_hole = circle(r=2.5/2)

m2_screw = up(1)(cylinder(r=2, h=2, center=True)) +\
    down(4)(cylinder(r=1, h=8, center=True))
