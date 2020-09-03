#!/usr/bin/env python
from itertools import combinations
from copy import copy
import json
import argparse
from pathlib import Path
from solid import *
from solid.utils import *  # Not required, but the utils module is useful

from switch import switch_cutout, switch_bbox
from misc import arduino_pro_micro, trrs, m4_hole, m4_screw, m2_hole, m2_screw


OPENSCAD_HEADER = '$fa = 6;\n$fs = .1;'

UNIT = 19.05

PLATE_MELT_GROW = 16
PLATE_MELT_D = 6
PLATE_MELT_SHRINK = PLATE_MELT_GROW - PLATE_MELT_D

PCB_MELT_GROW = 16
PCB_MELT_D = 4
PCB_MELT_SHRINK = PCB_MELT_GROW - PCB_MELT_D

PCB_PLATE_Z = 5

PCB_SCREW_M4_CLEARENCE = 4
PCB_SCREW_M2_CLEARENCE = 2


def melt(obj, grow, shrink):
    return offset(-shrink)(offset(grow)(obj))


def case(design):
    # keeps all bboxes of switches
    switch_bboxes = []

    # keeps all switches cutouts
    switches_cutouts = []

    # going through all the design data about switches
    for name, switch in {k: el for k, el in design.items() if k.startswith('SW')}.items():
        sw = copy(switch_cutout)
        sw_bbox = copy(switch_bbox)

        # if name == 'SW27':
        #     sw = debug(sw)

        if switch['angle']:
            sw = rotate(switch['angle'])(sw)
            sw_bbox = rotate(switch['angle'])(sw_bbox)

        sw = translate([switch['x'], switch['y']])(sw)

        sw_bbox = translate([switch['x'], switch['y'], PCB_PLATE_Z+5])(sw_bbox)

        switches_cutouts.append(sw)
        switch_bboxes.append(sw_bbox)

    # plate -  built directly from switch cutouts - organically melted

    m4_holes = []
    m4_screws = []
    for name, m4_hole_design in {k: el for k, el in design.items() if k.startswith('SCREW_M4')}.items():
        m4_holes += translate(
            [m4_hole_design['x'], m4_hole_design['y']]
        )(m4_hole)

        m4_screws += translate(
            [m4_hole_design['x'], m4_hole_design['y']]
        )(m4_screw)

    m4_screws = up(PCB_PLATE_Z + 1.6 + .001)(m4_screws)

    m4_holes_clearence = offset(PCB_SCREW_M4_CLEARENCE)(m4_holes)

    plate = melt(switches_cutouts,
                 PLATE_MELT_GROW, PLATE_MELT_SHRINK)

    plate = melt(plate + m4_holes_clearence, 20, 20)

    m2_holes = []
    m2_screws = []
    for name, m2_hole_design in {k: el for k, el in design.items() if k.startswith('SCREW_M2')}.items():
        m2_holes += translate(
            [m2_hole_design['x'], m2_hole_design['y']]
        )(m2_hole)

        m2_screws += translate(
            [m2_hole_design['x'], m2_hole_design['y']]
        )(m2_screw)

    m2_holes_clearence = offset(PCB_SCREW_M2_CLEARENCE)(m2_holes)

    m2_screws = up(PCB_PLATE_Z + 1.6 + .001)(m2_screws)

    plate -= m4_holes
    plate -= m2_holes
    plate -= switches_cutouts
    plate = up(PCB_PLATE_Z)(
        linear_extrude(1.6)(plate)
    )

    # collisions - from switch bboxes, when it occures - it's painted red
    collisions = []
    for bbox_1, bbox_2 in combinations(switch_bboxes, r=2):
        collisions += bbox_1 * bbox_2

    collisions = color(Red)(collisions)

    # other elements
    U1_arduino_pro_micro = translate([design['U1']['x'], design['U1']['y']])(
        arduino_pro_micro
    )

    # cutting on front - elements have to be on the edge, so we can't melt there
    U1_arduino_pro_micro_cut = intersection()(
        U1_arduino_pro_micro,
        translate([0, PCB_MELT_D])(U1_arduino_pro_micro)
    )

    U2_trrs = copy(trrs)
    U2_trrs_cut = intersection()(
        U2_trrs,
        translate([0, PCB_MELT_D])(U2_trrs)
    )
    if design['U2']['angle']:
        U2_trrs = rotate(design['U2']['angle'])(U2_trrs)
        U2_trrs_cut = rotate(design['U2']['angle'])(U2_trrs_cut)

    U2_trrs = translate([design['U2']['x'], design['U2']['y']])(
        U2_trrs
    )
    U2_trrs_cut = translate([design['U2']['x'], design['U2']['y']])(
        U2_trrs_cut
    )

    pcb = melt(
        switches_cutouts + U1_arduino_pro_micro_cut + U2_trrs_cut,
        PCB_MELT_GROW, PCB_MELT_SHRINK
    )
    pcb = melt(pcb + m2_holes_clearence, 2, 2)
    pcb -= m2_holes

    pcb = linear_extrude(1.6)(pcb)

    # shown elements + coloring
    U1_arduino_pro_micro = color([.004, 58.0/255, 147.0/255, .5])(
        up(2)(linear_extrude(1.6)(U1_arduino_pro_micro)))
    U2_trrs = color([.4, .4, .4, .5])(
        up(2)(linear_extrude(1.6)(U2_trrs))
    )

    pcb = color([1, 1, .8, .5])(pcb)
    plate = color([.8, .85, 1, .5])(plate)
    m4_screws = color([.3, .3, .3, .4])(m4_screws)
    m2_screws = color([.3, .3, .3, .4])(m2_screws)

    # last union
    design_scad = pcb + plate + U1_arduino_pro_micro + \
        U2_trrs + (m4_screws + m2_screws + collisions + switch_bboxes)

    return mirror([0, 1, 0])(design_scad)


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

    # 3 files - one main/full/assembly, for png, rest is used directly to use
    # export separate pieces

    scad_render_to_file(
        case_scad, args.output_path / 'case.scad',
        file_header=OPENSCAD_HEADER,
        include_orig_code=True)

    pcb_projection = projection(cut=True)(
        case_scad
    )
    scad_render_to_file(
        pcb_projection, args.output_path / 'pcb.scad',
        file_header=OPENSCAD_HEADER,
        include_orig_code=True)

    plate_projection = projection(cut=True)(
        down(5)(case_scad)
    )
    scad_render_to_file(
        plate_projection, args.output_path / 'plate.scad',
        file_header=OPENSCAD_HEADER,
        include_orig_code=True)
