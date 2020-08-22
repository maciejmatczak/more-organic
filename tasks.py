from invoke import task, call
from pathlib import Path


BUILD = Path('./build')
FAB = BUILD / 'fab'
DESIGN = BUILD / 'design'
CASE = BUILD / 'case'

PROJECT = 'more-organic'

# look out for slug genertion!
PCBS = [
    f'pcb/{PROJECT}.kicad_pcb',
]


@task
def dev(c):
    c.run('git submodule update --init --recursive')


@task
def clean_all(c):
    print(f'==> cleaning {BUILD} directory')
    c.run(f'rm -rf {BUILD}')


@task
def clean_fab(c):
    print(f'==> cleaning {FAB} directory')
    c.run(f'rm -rf {FAB}')


@task
def clean_design(c):
    print(f'==> cleaning {DESIGN} directory')
    c.run(f'rm -rf {DESIGN}')


@task
def clean(c, build=False, fab=False, design=False, case=False):
    patterns = []
    if build:
        patterns.append(BUILD)
    else:
        if fab:
            patterns.append(FAB)
        if design:
            patterns.append(DESIGN)
        if case:
            patterns.append(CASE)

    for p in patterns:
        c.run(f'rm -rf {p}')


@task(call(clean, fab=True))
def plot_all(c):
    FAB.mkdir(parents=True)

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


# @task(call(clean, design=True))
@task(call(clean, design=True))
def design(c):
    DESIGN.mkdir(parents=True, exist_ok=True)

    c.run(f'./design/design.py {DESIGN / "design.json"}')


# @task(call(clean, case=True), design)
@task(design)
def case(c):
    plate.mkdir(parents=True, exist_ok=True)

    c.run(f'./case/plate.py {DESIGN / "design.json"} {CASE / "plate.scad"}')


@task(design)
def case_watch(c):
    cmd = f'watchmedo shell-command \'{DESIGN / "design.json"}\' -c \'echo run;inv case\''
    print(cmd)
    c.run(cmd)
