#!/usr/bin/env python
from copy import copy
import json
import argparse
from pathlib import Path
from solid import *
from solid.utils import *  # Not required, but the utils module is useful


UNIT = 19.05


switch_cutout = polygon(
    points=[
        [0.8, 0],
        [14.8, 0],
        [14.8, 1],
        [15.6, 1],
        [15.6, 4.5],
        [14.8, 4.5],
        [14.8, 9.5],
        [15.6, 9.5],
        [15.6, 13],
        [14.8, 13],
        [14.8, 14],
        [0.8, 14],
        [0.8, 13],
        [0, 13],
        [0, 9.5],
        [0.8, 9.5],
        [0.8, 4.5],
        [0, 4.5],
        [0, 1],
        [0.8, 1],
    ]
)

switch_cutout = translate([-15.6/2, -15.6/2])(switch_cutout)
switch_bbox = color([1, 1, 1, .2])(
    up(UNIT)(
        # adding dummy distance to avoid showing issues when 2 surfaces touches
        # each other
        cube([UNIT - 0.0001, UNIT - 0.0001, UNIT/2], center=True)
    )
)


if __name__ == '__main__':
    switch = switch_cutout + switch_bbox

    scad_render_to_file(switch, include_orig_code=True)
