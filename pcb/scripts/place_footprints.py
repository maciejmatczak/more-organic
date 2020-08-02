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


board = pcbnew.LoadBoard(pcb_path)
io = pcbnew.PCB_IO()

for m in board.GetModules():
    name = m.GetReference()

    try:
        placement = placement_config.pop(name)
    except KeyError:
        print(f'Footpring {name} not found in config!')
        continue

    coords = placement.get('coords')
    orient = placement.get('orient')

    if coords:
        m.SetPosition(pcbnew.wxPointMM(
            coords[0],
            coords[1],
        ))

    if orient:
        m.SetOrientation(orient*10)

    # if name.startswith('SW'):
    #     print(name)

    #     try:
    #         coord = placement_config[name]
    #     except KeyError:
    #         print(f'    {name} not found in config')
    #         continue

    #     m.SetPosition(pcbnew.wxPointMM(
    #         coord[0],
    #         coord[1],
    #     ))

    #     print(f'    {name} set to {coord}')

    # if name.startswith('D'):
    #     coord = placement_config[f'SW{name[1:]}']
    #     m.SetPosition(pcbnew.wxPointMM(
    #         coord[0]-19.05/2,
    #         coord[1],
    #     ))
        # obj = m
        # for attr in dir(obj):
        #     print("obj.%s = %r" % (attr, getattr(obj, attr)))
        # m.SetOrientation(900)
        # m.Rotate(
        #     pcbnew.wxPointMM(
        #         coord[0]-19.05/2,
        #         coord[1],
        #     ),
        #     90
        # )

    # footprint_id = m.GetFPID().GetUniStringLibId()
    # print(footprint_id)
    # break

board.Save(board.GetFileName())
