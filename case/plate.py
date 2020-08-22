#!/usr/bin/env python
from itertools import combinations
from copy import copy
import json
import argparse
from pathlib import Path
from solid import *
from solid.utils import *  # Not required, but the utils module is useful

from switch import switch_cutout, switch_bbox

UNIT = 19.05


def case(design):
    plate = polygon(
        points=[
            [-200, -200],
            [200, -200],
            [200, 200],
            [-200, 200],
        ]
    )

    switch_bboxes = []
    switches = []
    for name, switch in {k: el for k, el in design.items() if k.startswith('SW')}.items():
        sw = copy(switch_cutout)
        sw_bbox = copy(switch_bbox)

        # if name == 'SW27':
        #     sw = debug(sw)

        if switch['angle']:
            sw = rotate(switch['angle'])(sw)
            sw_bbox = rotate(switch['angle'])(sw_bbox)

        sw = translate((switch['x'], switch['y'], 0))(sw)
        sw_bbox = translate((switch['x'], switch['y'], 0))(sw_bbox)

        switches.append(sw)
        switch_bboxes.append(sw_bbox)

    plate = offset(16)(switches)
    plate = offset(-12)(plate)
    plate -= switches

    collisions = []
    for bbox_1, bbox_2 in combinations(switch_bboxes, r=2):
        collisions += bbox_1 * bbox_2

    collisions = color(Red)(collisions)

    # plate += switch_bboxes + collisions

    # plate = linear_extrude(1.6)(plate)

    # mirror, as kicad uses y in opposite direction
    return mirror([0, 1, 0])(plate + (switch_bboxes + collisions))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Creates scad file and dxf for case'
    )
    parser.add_argument(
        'design_file', type=lambda p: Path(p).resolve(),
        help='Input path of the design file.'
    )
    parser.add_argument(
        'output_path', type=lambda p: Path(p).resolve(),
        help='Output directory of the case files.'
    )
    args = parser.parse_args()

    design = json.loads(args.design_file.read_text())

    case_scad = case(design)

    scad_render_to_file(case_scad, args.output_path, include_orig_code=True)
