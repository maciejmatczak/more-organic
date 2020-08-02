from invoke import task
from pathlib import Path
import json


PCB = './more-organic/more-organic.kicad_pcb'

OFFSET = (100, 40)

COLUMN_OFFSET = [
    -.125, 0, .25, 0, -.75, -.75-.125
]
U = 19.05


@task
def place_keys(c):
    cfg = {}
    # 30 switches, 1-24 are column staggered

    for row in range(1, 6):
        for col in range(1, 7):
            i = 6*(row - 1) + col

            cfg[f'SW{i}'] = {
                'coords': (
                    U * col + OFFSET[0],
                    U * (row - COLUMN_OFFSET[col-1]) + OFFSET[1]
                )
            }

            cfg[f'D{i}'] = {
                'coords': (
                    cfg[f'SW{i}']['coords'][0] - U/2,
                    cfg[f'SW{i}']['coords'][1]
                ),
                'orient': 90
            }
    # TRRS
    cfg['U2'] = {
        'coords': (50, 80)
    }
    # Atmega
    cfg['U1'] = {
        'coords': (90, 70)
    }

    # cfg['SW26'] = (
    #     cfg['SW26'][0] - U/2,
    #     cfg['SW26'][1] - COLUMN_OFFSET[0]*U,
    # )
    # cfg['SW25'] = (
    #     cfg['SW25'][0] - U/2,
    #     cfg['SW25'][1]
    # )

    with Path('cfg.json').open('w') as j:
        json.dump(cfg, j, indent=4)

    c.run(f'./scripts/place_footprints.py {PCB} cfg.json')
