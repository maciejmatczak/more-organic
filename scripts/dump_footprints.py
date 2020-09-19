#!/usr/bin/env python

import argparse
from pathlib import Path
import sys
import json

import pcbnew

sys.path.append(Path(__file__).parent)
from common import path_type  # noqa


def dump_footprints(pcb_path: str, dump_path: Path):
    board = pcbnew.LoadBoard(pcb_path)

    dump = []
    for m in board.GetModules():
        name = m.GetReference()
        footprint = m.GetFPID().GetUniStringLibId()

        x, y = [pcbnew.ToMM(e) for e in m.GetPosition()]

        orientation = m.GetOrientation()/10

        print(name, footprint, x, y, orientation)
        dump.append({
            'name': name,
            'footprint': footprint,
            'x': x,
            'y': y,
            'orientation': orientation,
        })

    dump_path.write_text(json.dumps(dump, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Fooptrint placement data dumper'
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

    dump_footprints(
        str(args.pcb),
        args.placement_config
    )
