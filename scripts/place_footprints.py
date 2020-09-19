#!/usr/bin/env python

import argparse
import os
from pathlib import Path
import sys
import json

import pcbnew

sys.path.append(Path(__file__).parent)
from common import path_type  # noqa


def place_footprints(pcb_path: str, placement_config: dict):
    # dictifying a placement_config, which currently is a list
    # name attribute could be empty, but that should be weird if we move around
    # existing elements
    placement_config_dict = {}
    for element in placement_config:
        name = element['name']
        if name:
            placement_config_dict[name] = element
        else:
            print(f'Ignoring unnamed: {element}')

    board = pcbnew.LoadBoard(pcb_path)

    for m in board.GetModules():
        name = m.GetReference()

        try:
            placement = placement_config_dict.pop(name)
        except KeyError:
            print(f'Footprint {name} not found in config!')
            continue

        x = placement['x']
        y = placement['y']
        angle = placement['orientation']

        m.SetPosition(pcbnew.wxPointMM(
            x,
            y,
        ))

        m.SetOrientation(angle*10)

    board.Save(board.GetFileName())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Places a footrpints accordingly to a config file'
    )
    parser.add_argument(
        'pcb', type=path_type,
        help='PCB file path'
    )
    parser.add_argument(
        'placement_config', type=path_type,
        help='Placement config path'
    )
    args = parser.parse_args()

    place_footprints(
        str(args.pcb),
        json.loads(args.placement_config.read_text())
    )
