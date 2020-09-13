#!/usr/bin/env python

import os
from pathlib import Path
import sys
import json

import pcbnew


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
io = pcbnew.PCB_IO()

for m in board.GetModules():
    name = m.GetReference()

    try:
        placement = placement_config_dict.pop(name)
    except KeyError:
        print(f'Footprint {name} not found in config!')
        continue

    x = placement.get('x')
    y = placement.get('y')
    angle = placement.get('angle')

    m.SetPosition(pcbnew.wxPointMM(
        x,
        y,
    ))

    m.SetOrientation(angle*10)


board.Save(board.GetFileName())
