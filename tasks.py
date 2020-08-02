from invoke import task
from pathlib import Path


PROJECT = 'knobs'
FAB = './FAB'

# look out for slug genertion!
PCBS = [
    f'pcb/{PROJECT}.kicad_pcb',
]


@task
def dev(c):
    c.run('git submodule update --init --recursive')


@task
def clean(c):
    print(f'==> cleaning {FAB} directory')
    c.run(f'rm -rf {FAB}')


@task(clean)
def plot_all(c):
    Path(FAB).mkdir(parents=True)

    # assuming first one is a pcb which needs docs files as well
    first = True
    for pcb in PCBS:
        slug = '_'.join(pcb.split('/')[0:-1])

        if not Path(pcb).exists():
            print(f'==> {pcb} not found, omitting!')
            continue
            first = False

        if first:
            c.run(f'./scripts/plot_doc.py {pcb} {FAB}/doc/{slug}')
        first = False

        c.run(f'./scripts/plot_fab.py {pcb} {FAB}/fab/{slug}')
        c.run(f'7z a {FAB}/fab/{PROJECT}_{slug}.zip ./{FAB}/fab/{slug}/*')
