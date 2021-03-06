#!/usr/bin/env python
from itertools import combinations
from copy import copy
import json
import argparse
from pathlib import Path
from solid import *
from solid.utils import *  # Not required, but the utils module is useful
from solid import rotate as _rotate
import sys

from switch import switch_cutout, switch_bbox, switch_courtyard
from misc import (arduino_pro_micro_2d, trrs, switch_6mm, jumper,
                  resistor_hybrid,  m4_hole, m4_screw, m2_hole, m2_screw)


OPENSCAD_HEADER = '$fa = 6;\n$fs = .1;'

UNIT = 19.05

# Plate design settings
PLATE_MELT_GROW = 16
PLATE_MELT_D = 3
PLATE_MELT_SHRINK = PLATE_MELT_GROW - PLATE_MELT_D

# PCB design settings
PCB_MELT_GROW = 16
PCB_MELT_D = 4
PCB_MELT_SHRINK = PCB_MELT_GROW - PCB_MELT_D

PCB_PLATE_Z = 5
PCB_SCREW_M4_CLEARENCE = 4
PCB_SCREW_M2_CLEARENCE = 2


def melt(obj, grow, shrink):
    return offset(-shrink)(offset(grow)(obj))


def make_switches(design):
    # keeps all bboxes of switches
    switch_bboxes = []

    # keeps all switches cutouts
    switch_cutouts = []

    # keeps all switches courtyards
    switch_courtyards = []

    for element in design:
        x = element['x']
        y = element['y']
        orientation = element['orientation']

        sw = copy(switch_cutout)
        sw_bbox = copy(switch_bbox)
        sw_courtyard = copy(switch_courtyard)

        # if name == 'SW27':
        #     sw = debug(sw)

        if orientation:
            sw = rotate(orientation)(sw)
            sw_bbox = rotate(orientation)(sw_bbox)
            sw_courtyard = rotate(orientation)(sw_courtyard)

        sw = translate([x, y])(sw)
        sw_courtyard = translate([x, y])(sw_courtyard)

        sw_bbox = translate([x, y, PCB_PLATE_Z+5])(sw_bbox)

        switch_cutouts.append(sw)
        switch_bboxes.append(sw_bbox)
        switch_courtyards.append(sw_courtyard)

    return switch_cutouts, switch_bboxes, switch_courtyards


def make_screws(design, screw_model, hole_model):
    screws = []
    holes = []

    for element in design:
        x = element['x']
        y = element['y']

        holes += translate(
            [x, y]
        )(hole_model)

        screws += translate(
            [x, y]
        )(screw_model)

    return screws, holes


def make_other_elements(design):
    full_footprint = []
    mapping = {
        'Button_Switch_THT:SW_PUSH_6mm_H7.3mm': switch_6mm,
        'Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm': jumper,
        'keebio-footprints:ArduinoProMicro': arduino_pro_micro_2d,
        'keebio-footprints:TRRS-PJ-320A-dual': trrs,
        'keebio-footprints:Resistor-Hybrid': resistor_hybrid,
    }

    for element in design:
        footprint = element['footprint']
        try:
            model = mapping[footprint]
        except KeyError:
            print(f'Unknown footprint {footprint}')
            sys.exit(1)

        x = element['x']
        y = element['y']
        orientation = element['orientation']

        if orientation:
            model = rotate(orientation)(model)

        model = translate([x, y])(model)

        full_footprint.append(model)

    return full_footprint, up(1.6 + .1)(linear_extrude(2)(full_footprint))


def case(design_switches, design_diodes, design_other_elements, design_mh_m2,
         design_mh_standoff):

    m4_screws, m4_holes = make_screws(design_mh_standoff, m4_screw, m4_hole)
    m4_holes_clearence = offset(PCB_SCREW_M4_CLEARENCE)(m4_holes)

    m4_screws = up(PCB_PLATE_Z + 1.6 + .001)(m4_screws)

    m2_screws, m2_holes = make_screws(design_mh_m2, m2_screw, m2_hole)
    m2_holes_clearence = offset(PCB_SCREW_M2_CLEARENCE)(m2_holes)

    m2_screws = up(PCB_PLATE_Z + 1.6 + .001)(m2_screws)

    switch_cutouts, switch_bboxes, switch_courtyards = make_switches(
        design_switches)

    other_elements_footprint, other_elements_representation =\
        make_other_elements(design_other_elements)

    other_elements_footprint_melted = melt(
        other_elements_footprint, 10, 10
    )
    other_elements_footprint_cut =\
        intersection()(
            other_elements_footprint_melted,
            translate([0, -PCB_MELT_D])(
                other_elements_footprint_melted
            )
        )

    plate = melt(switch_courtyards,
                 PLATE_MELT_GROW, PLATE_MELT_SHRINK)

    plate = melt(plate + m4_holes_clearence, 20, 20)

    plate -= switch_cutouts

    collisions = []
    for bbox_1, bbox_2 in combinations(switch_bboxes, r=2):
        collisions += bbox_1 * bbox_2

    pcb = melt(
        switch_cutouts + other_elements_footprint_cut,
        PCB_MELT_GROW, PCB_MELT_SHRINK
    )
    pcb = melt(pcb + m2_holes_clearence, 2, 2)

    cover = melt(
        other_elements_footprint_cut,
        PCB_MELT_GROW, PCB_MELT_SHRINK
    )
    cover = melt(
        cover + m2_holes_clearence,
        2, 2
    )
    cover -= translate([-2, 0, 0])(plate)
    cover = melt(cover, -2, -2)

    cover = linear_extrude(1.6)(cover)
    pcb = linear_extrude(1.6)(pcb)
    plate = linear_extrude(1.6)(plate)

    collisions = color(Red)(collisions)
    pcb = color([1, 1, .8, .5])(pcb)
    cover = color([.8, .85, 1, .5])(cover)
    plate = color([.8, .85, 1, .5])(plate)
    m4_screws = color([.3, .3, .3, .4])(m4_screws)
    m2_screws = color([.3, .3, .3, .4])(m2_screws)

    assembly = union()(
        pcb,
        other_elements_representation, m4_screws, m2_screws,
        up(PCB_PLATE_Z)(plate),
        up(PCB_PLATE_Z*2)(cover),
        collisions, switch_bboxes
    )

    return assembly, pcb, plate, cover


def kicad2openscad(design):
    translated_design = []

    for element in design:
        element['y'] *= -1
        element['orientation'] = (element['orientation'] + 90) % 360 - 90

        # element['orientation'] *= -1
        translated_design.append(element)

    return translated_design


def split_kicad_dump(kicad_dump):
    design_switches = []
    design_diodes = []
    design_other_elements = []
    design_mh_m2 = []

    mapping = {
        'keyswitches:Kailh_socket_MX_optional_reversible_alt': design_switches,
        'keebio-footprints:Diode-dual': design_diodes,
        'MountingHole_2.2mm_M2_Pad_Via': design_mh_m2,
        'Button_Switch_THT:SW_PUSH_6mm_H7.3mm': design_other_elements,
        'Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm': design_other_elements,
        'keebio-footprints:ArduinoProMicro': design_other_elements,
        'keebio-footprints:TRRS-PJ-320A-dual': design_other_elements,
        'keebio-footprints:Resistor-Hybrid': design_other_elements,
    }
    for element in kicad_dump:
        footprint = element['footprint']
        try:
            list_ = mapping[footprint]
            list_.append(element)
        except KeyError:
            print(f'Unknown element\'s footprint {element}')
            sys.exit(1)

    return design_switches, design_diodes, design_other_elements, design_mh_m2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Creates scad file and dxf for case'
    )
    parser.add_argument(
        '--kicad-dump', type=lambda p: Path(p).resolve(),
        required=True,
        help='Input path from kicad dump.'
    )
    parser.add_argument(
        '--mh-standoff', type=lambda p: Path(p).resolve(),
        required=True,
        help='Input path for standoffs'
    )
    parser.add_argument(
        '-o', '--output-path', type=lambda p: Path(p).resolve(),
        required=True,
        help='Output directory of the case files.'
    )
    args = parser.parse_args()

    kicad_dump = json.loads(args.kicad_dump.read_text())
    kicad_dump = kicad2openscad(kicad_dump)
    design_switches, design_diodes, design_other_elements, design_mh_m2 =\
        split_kicad_dump(kicad_dump)

    design_mh_standoff = json.loads(args.mh_standoff.read_text())
    design_mh_standoff = kicad2openscad(design_mh_standoff)

    assembly, pcb, plate, cover = case(
        design_switches, design_diodes,
        design_other_elements,
        design_mh_m2, design_mh_standoff
    )

    # 3 files - one main/full/assembly, for png, rest is used directly to use
    # export separate pieces

    scad_render_to_file(
        assembly, args.output_path / 'assembly.scad',
        file_header=OPENSCAD_HEADER,
        include_orig_code=False)

    pcb_projection = projection(cut=True)(
        pcb
    )
    scad_render_to_file(
        pcb_projection, args.output_path / 'pcb.scad',
        file_header=OPENSCAD_HEADER,
        include_orig_code=False)

    plate_projection = projection(cut=True)(
        plate
    )
    scad_render_to_file(
        plate_projection, args.output_path / 'plate.scad',
        file_header=OPENSCAD_HEADER,
        include_orig_code=False)

    cover_projection = projection(cut=True)(
        cover
    )
    scad_render_to_file(
        cover_projection, args.output_path / 'cover.scad',
        file_header=OPENSCAD_HEADER,
        include_orig_code=False)
