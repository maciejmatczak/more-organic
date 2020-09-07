#!/usr/bin/env python

import argparse
from typing import Union, Tuple
import math
from dataclasses import dataclass, asdict
from pathlib import Path
import json


OFFSET = (0, 0)

COLUMN_OFFSET = [
    5, 0, -12, -8, 18, 23,
]  # mm
U = 19.05  # mm

SCREWS_M4 = []
Xes = (0, U * 4 + U/2)
Yes = (-12, 98)
for x in Xes:
    for y in Yes:
        SCREWS_M4.append((x, y))

# helper for lower lefte M2 screws
d = (COLUMN_OFFSET[0]-COLUMN_OFFSET[1])/2
SCREWS_M2 = [
    (U*1.5 - 3, COLUMN_OFFSET[1] - U/2 - 3),
    (U*3.5 + 3, COLUMN_OFFSET[4] - U/2 - 3),
    (U/2 + d, d + U*3.5),
    (U*3.5 - 3, COLUMN_OFFSET[3] + U*3.5 + 3),
    (-20, 30)
]


@dataclass
class Element:
    x: float = 0
    y: float = 0
    angle: float = 0

    def rotate(self, angle, anchor=(0, 0)):
        ax, ay = anchor
        px, py = self.x, self.y

        self.x = ax + math.cos(math.radians(angle)) * (px - ax) - \
            -math.sin(math.radians(angle)) * (py - ay)
        self.y = ay - math.sin(math.radians(angle)) * (px - ax) + \
            +math.cos(math.radians(angle)) * (py - ay)

        self.angle = angle

    def move(self, x=0.0, y=0.0):
        self.x += x
        self.y += y


def design():
    # 30 switches, 1-24 are column staggered
    # for every switch 1 diode
    # U1 - arduino pro micro
    # U2 - TRRS
    # SW_RESET - reset switch

    cfg = {}

    # x, y, angle
    switches_coords = []
    for row in range(1, 5):
        for col in range(1, 7):
            i = 6*(row - 1) + col

            switch = Element(
                x=U * (col-1) + OFFSET[0],
                y=U * (row-1) + COLUMN_OFFSET[col-1] + OFFSET[1]
            )

            cfg[f'SW{i}'] = switch

    # thumb left key
    distance = 2.2
    SW25 = Element(
        x=OFFSET[0] + U * 0 - U/2 - distance,
        y=OFFSET[1] + COLUMN_OFFSET[0] + U * 4 + distance,
        angle=15
    )
    cfg['SW25'] = SW25

    # thumb middle key
    SW26 = Element(
        x=OFFSET[0] + U * 1 - U/2,
        y=OFFSET[1] + COLUMN_OFFSET[0] + U * 4,
    )
    cfg['SW26'] = SW26

    # thumb right key
    distance = 3.5
    SW27 = Element(
        x=SW26.x + U,
        y=SW26.y,
        angle=-30
    )
    SW27.move(distance, 5)
    cfg['SW27'] = SW27

    # following up with a diodes
    for sw_name in [key for key in cfg.keys() if key.startswith('SW')]:
        switch = cfg[sw_name]

        i = sw_name[2:]

        diode = Element(
            x=switch.x,
            y=switch.y - U/2 + 1,
        )
        diode.rotate(180 + switch.angle, anchor=(switch.x, switch.y))

        cfg[f'D{i}'] = diode

    # Arduino Pro Micro
    cfg['U1'] = Element(
        x=OFFSET[0]-24,
        y=OFFSET[1]+17.8,
        angle=-90
    )

    # TRRS
    cfg['U2'] = Element(
        x=OFFSET[0]-40,
        y=OFFSET[1]+2
    )

    # some additional reserved space for the rest of an elements
    cfg['reserved'] = Element(
        x=cfg['U1'].x + 4,
        y=cfg['U1'].y + 30
    )

    for i, (x, y) in enumerate(SCREWS_M4):
        screw = Element(
            x=x,
            y=y
        )

        cfg[f'SCREW_M4_{i}'] = screw

    for i, (x, y) in enumerate(SCREWS_M2):
        screw = Element(
            x=x,
            y=y
        )

        cfg[f'SCREW_M2_{i}'] = screw

    return cfg


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Creates json file with design data'
    )
    parser.add_argument(
        'output_path', type=lambda p: Path(p).resolve(),
        help='Output path of the design file.'
    )
    args = parser.parse_args()

    cfg = design()

    with args.output_path.open('w') as j:
        cfg_tmp = {
            key: asdict(value) for key, value in cfg.items()
        }
        json.dump(cfg_tmp, j, indent=4)
