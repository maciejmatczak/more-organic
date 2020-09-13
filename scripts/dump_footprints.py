#!/usr/bin/env python

import os
from pathlib import Path
import sys
import json

import pcbnew


pcb_path = os.path.abspath(sys.argv[1])
dump_path = Path(os.path.abspath(sys.argv[2]))

if not Path(pcb_path).exists():
    print(f'PCB {pcb_path} not found, exiting')
    sys.exit(1)


board = pcbnew.LoadBoard(pcb_path)

dump = []
for m in board.GetModules():
    name = m.GetReference()
    footprint = m.GetFPID().GetUniStringLibId()

    x, y = [pcbnew.ToMM(e) for e in m.GetPosition()]

    orientation = m.GetOrientation()/10

    print(name, footprint, x, y, orientation)
    dump.append(
        [name, footprint, x, y, orientation]
    )

dump_path.write_text(json.dumps(dump, indent=4))
