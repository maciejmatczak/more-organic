#!/usr/bin/env python

import os
from pathlib import Path
import sys
import json
import dotenv

import pcbnew


dotenv.load_dotenv()


pcb_path = os.path.abspath(sys.argv[1])
placement_config_path = os.path.abspath(sys.argv[2])

if not Path(pcb_path).exists():
    print(f'PCB {pcb_path} not found, exiting')
    sys.exit(1)

if not Path(placement_config_path).exists():
    print(
        f'Key placement config {placement_config_path} not found, exiting')
    sys.exit(1)
else:
    with Path(placement_config_path).open('r') as p:
        placement_config = json.load(p)


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
    mod.Reference().SetVisible(False)

    print(f'=> Adding mh @ {x}; {y} mm')
    board.Add(mod)

board.Save(board.GetFileName())
