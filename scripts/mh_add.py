#!/usr/bin/env python

import json
import argparse
from pathlib import Path
import os
import dotenv
import sys

import pcbnew

sys.path.append(Path(__file__).parent)
from common import path_type  # noqa


dotenv.load_dotenv()


def mh_add(pcb_path: str, placement_config: dict):
    board = pcbnew.LoadBoard(pcb_path)
    io = pcbnew.PCB_IO()
    mh_pretty = os.environ['KICAD_MOUNTING_HOLE_PATH']

    for placement in placement_config:
        footprint = placement['footprint']

        x = placement.get('x')
        y = placement.get('y')

        mod = io.FootprintLoad(mh_pretty, footprint)
        if not mod:
            print(f'{footprint} not found in {mh_pretty}')
            sys.exit(1)

        mod.SetPosition(pcbnew.wxPointMM(
            x,
            y,
        ))
        mod.Reference().SetText('generated')
        mod.Reference().SetVisible(False)
        mod.Value().SetVisible(False)

        print(f'=> Adding mh @ {x}; {y} mm')
        board.Add(mod)

    board.Save(board.GetFileName())


def filter_config(placement_config, footprint=None, x_lt=None, x_gt=None):
    if footprint:
        placement_config = [
            el for el in placement_config if el['footprint'] == footprint
        ]

    if x_lt is not None:
        placement_config = [
            el for el in placement_config if el['x'] < x_lt
        ]
    if x_gt is not None:
        placement_config = [
            el for el in placement_config if el['x'] > x_gt
        ]

    return placement_config


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Places mounting holes on pcb, based on placement config. '
        'Expects a KICAD_MOUNTING_HOLE_PATH environment variable to be set '
        '(.env).'
    )
    parser.add_argument(
        'pcb', type=path_type,
        help='PCB file path'
    )
    parser.add_argument(
        'placement_config', type=path_type,
        help='Placement config path'
    )
    parser.add_argument(
        '--filter-footprint', type=str, default=None,
        help='Config filter for footprint attribute'
    )
    parser.add_argument(
        '--x-lt', type=float, default=None,
        help='x lower than'
    )
    parser.add_argument(
        '--x-gt', type=float, default=None,
        help='x greater than'
    )

    args = parser.parse_args()

    placement_config = json.loads(args.placement_config.read_text())
    placement_config = filter_config(
        placement_config,
        footprint=args.filter_footprint,
        x_lt=args.x_lt,
        x_gt=args.x_gt
    )

    mh_add(
        str(args.pcb),
        placement_config
    )
