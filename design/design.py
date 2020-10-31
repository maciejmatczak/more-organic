#!/usr/bin/env python

from copy import copy
import argparse
from typing import Union, Tuple, List
import math
from dataclasses import dataclass, asdict
from pathlib import Path
import json


OFFSET = (0, 0)

COLUMN_OFFSET = [
    5, 0, -10, -1, 23, 28,
]  # mm
U = 19.05  # mm

# MOUNTING HOLES
MH_STANDOFF = []
Xes = (0, U * 4 + U/2 - 4)
Yes = (-12, 98)
for x in Xes:
    for y in Yes:
        MH_STANDOFF.append((x, y))

# helper for lower left M2 screws
d = (COLUMN_OFFSET[0]-COLUMN_OFFSET[1])/2
MH_PCB_TO_PLATE = [
    (U*1.5 - 3, COLUMN_OFFSET[1] - U/2 - 3),
    (U*3.5 + 3, COLUMN_OFFSET[4] - U/2 - 3),
    (U/2 + d, d + U*3.5),
    (U*3.5 - 3, COLUMN_OFFSET[3] + U*3.5 + 3),
]

MH_PCB_TO_COVER = [
    (-35, 18),
    (-25, 36),
]

MH_M2_FOOTPRINT = 'MountingHole_2.2mm_M2_Pad_Via'
MH_M4_FOOTPRINT = 'MountingHole_4.3mm_M4_Pad_Via'


@dataclass
class Element:
    name: str = ''
    footprint: str = ''
    x: float = 0
    y: float = 0
    orientation: float = 0

    def rotate(self, orientation, anchor=(0, 0)):
        ax, ay = anchor
        px, py = self.x, self.y

        self.x = ax + math.cos(math.radians(orientation)) * (px - ax) + \
            math.sin(math.radians(orientation)) * (py - ay)
        self.y = ay - math.sin(math.radians(orientation)) * (px - ax) + \
            math.cos(math.radians(orientation)) * (py - ay)

        self.orientation = orientation

    def move(self, x=0.0, y=0.0):
        self.x += x
        self.y += y


class Design:
    def __init__(self) -> None:
        self.elements: List[Element] = []

    def add(self, element: Element):
        self.elements.append(element)

    def save(self, path: Path):
        path.write_text(
            json.dumps([asdict(el) for el in self.elements], indent=4)
        )


def design_sw_and_dio():
    # 30 switches, 1-24 are column staggered
    # for every switch 1 diode

    design = Design()

    for row in range(1, 5):
        for col in range(1, 7):
            i = 6*(row - 1) + col

            switch = Element(
                name=f'SW{i}',
                x=U * (col-1) + OFFSET[0],
                y=U * (row-1) + COLUMN_OFFSET[col-1] + OFFSET[1]
            )

            design.add(switch)

    # thumb left key
    SW25 = Element(
        name='SW25',
        x=OFFSET[0] - 28,
        y=OFFSET[1] + COLUMN_OFFSET[0] + U * 4 + 11.6,
        orientation=27.6
    )
    design.add(SW25)

    # thumb middle key
    SW26 = Element(
        name='SW26',
        x=OFFSET[0] - 9.3,
        y=OFFSET[1] + COLUMN_OFFSET[0] + U * 4 + 2.7,
        orientation=18
    )
    design.add(SW26)

    # thumb right key
    SW27 = Element(
        name='SW27',
        x=OFFSET[0] + 13.4,
        y=OFFSET[1] + COLUMN_OFFSET[0] + U * 4 + 1.3,
        orientation=-6.6
    )
    design.add(SW27)

    # following up with a diodes
    for switch in copy(design.elements):
        sw_name = switch.name

        i = sw_name[2:]

        diode = Element(
            name=f'D{i}',
            x=switch.x,
            y=switch.y - U/2 + 1,
        )
        diode.rotate(180 + switch.orientation, anchor=(switch.x, switch.y))

        design.add(diode)

    return design


def design_mh_standoff():
    design = Design()
    for x, y in MH_STANDOFF:
        screw = Element(
            footprint=MH_M4_FOOTPRINT,
            x=x,
            y=y
        )

        design.add(screw)

    return design


def design_mh_pcb_to_plate():
    design = Design()
    for x, y in MH_PCB_TO_PLATE:
        screw = Element(
            footprint=MH_M2_FOOTPRINT,
            x=x,
            y=y
        )

        design.add(screw)

    return design


def design_mh_pcb_to_cover():
    design = Design()
    for x, y in MH_PCB_TO_COVER:
        screw = Element(
            footprint=MH_M2_FOOTPRINT,
            x=x,
            y=y
        )

        design.add(screw)

    return design


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Creates json files with design data'
    )
    parser.add_argument(
        'output_path', type=lambda p: Path(p).resolve(),
        help='Output path of the design folder.'
    )
    args = parser.parse_args()

    d = design_sw_and_dio()
    d.save(args.output_path / 'sw_and_dio.json')

    d = design_mh_standoff()
    d.save(args.output_path / 'mh_standoff.json')

    d = design_mh_pcb_to_plate()
    d.save(args.output_path / 'mh_pcb_to_plate.json')
