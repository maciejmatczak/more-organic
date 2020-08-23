from solid import *
from solid.utils import *  # Not required, but the utils module is useful

arduino_pro_micro = color(Blue)(
    square([17.8, 33.0], center=True)
)

# width of 10.7: flippable footprint
trrs = color([.3, .3, .3])(square([10.7, 14.1], center=True))
