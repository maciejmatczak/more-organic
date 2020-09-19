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
        footprint = placement.get('footprint')

        x = placement.get('x')
        y = placement.get('y')

        mod = io.FootprintLoad(mh_pretty, footprint)

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
    args = parser.parse_args()

    mh_add(
        str(args.pcb),
        json.loads(args.placement_config.read_text())
    )
