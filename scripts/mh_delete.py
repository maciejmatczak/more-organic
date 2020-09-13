#!/usr/bin/env python

import os
from pathlib import Path
import sys
import json
import dotenv

import pcbnew


dotenv.load_dotenv()


pcb_path = os.path.abspath(sys.argv[1])

if not Path(pcb_path).exists():
    print(f'PCB {pcb_path} not found, exiting')
    sys.exit(1)


board = pcbnew.LoadBoard(pcb_path)
io = pcbnew.PCB_IO()

for m in board.GetModules():
    footprint_id = m.GetFPID().GetUniStringLibId()

    # not being sure if there is better way to checkl what is a mounting hole?
    # holes placed by scripts does not have a ":" with a lib name in front
    if 'MountingHole' in footprint_id:
        print(
            f'=> Deleting {footprint_id} @ {[pcbnew.ToMM(e) for e in m.GetCenter()]} mm')
        board.Delete(m)

board.Save(board.GetFileName())
