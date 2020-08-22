from invoke import task
from pathlib import Path
import json
from copy import copy


PCB = './more-organic/more-organic.kicad_pcb'

OFFSET = (100, 40)

COLUMN_OFFSET = [
    -.125, 0, .25, 0, -.75, -.75-.125
]
U = 19.05
patternpattern


@task
def place_footprints(c):
    cfg = {}
    # 30 switches, 1-24 are column staggered

    for row in range(1, 6):
        for col in range(1, 7):
            i = 6*(row - 1) + col

            cfg[f'SW{i}'] = {
                'coords': [
                    U * col + OFFSET[0],
                    U * (row - COLUMN_OFFSET[col-1]) + OFFSET[1]
                ]
            }

            cfg[f'D{i}'] = {
                'coords': [
                    cfg[f'SW{i}']['coords'][0],
                    cfg[f'SW{i}']['coords'][1] - U/2 + 1,
                ],
                'orient': 180
            }
    # TRRS
    cfg['U2'] = {
        'coords': (104.15, 53.95)
    }
    # Atmega
    cfg['U1'] = {
        'coords': (88.5, 70)
    }

    cfg['SW25']['coords'][0] += - U/2 - 2.2
    cfg['SW25']['coords'][1] += + 2.2
    cfg['SW25']['orient'] = 15
    cfg['D25']['coords'][0] += - U/2 - 2.2
    cfg['D25']['coords'][1] += + 2.2
    cfg['D25']['rotate'] = {
        'anchor': cfg['SW25']['coords'],
        'angle': 15
    }

    cfg['SW26']['coords'][0] += -U/2
    cfg['SW26']['coords'][1] += -COLUMN_OFFSET[0]*U
    cfg['D26']['coords'][0] += -U/2
    cfg['D26']['coords'][1] += -COLUMN_OFFSET[0]*U

    # cfg['SW27']['coords'][0] += -U/2
    # cfg['SW27']['coords'][1] = 6*U + OFFSET[1]
    # cfg['D27']['coords'][0] += -U/2
    # cfg['D27']['coords'][1] = 6*U - U/2 + 1

    cfg['SW27']['coords'] = copy(cfg['SW26']['coords'])
    cfg['SW27']['coords'][0] += U
    cfg['D27']['coords'] = copy(cfg['D26']['coords'])
    cfg['D27']['coords'][0] += U

    cfg['SW27']['orient'] = -30
    cfg['D27']['rotate'] = {
        'anchor': cfg['SW27']['coords'],
        'angle': -30
    }
    cfg['SW27']['coords'][0] += 3.49
    cfg['D27']['coords'][0] += 3.49

    cfg['SW27']['coords'][1] += 5
    cfg['D27']['coords'][1] += 5

    with Path('cfg.json').open('w') as j:
        json.dump(cfg, j, indent=4)

    c.run(f'./scripts/place_footprints.py {PCB} cfg.json')
