import pcbnew
import pytest
from pathlib import Path
import datetime


def test_report_is_newer_than_pcb():
    report = Path() / 'data' / 'pcb' / 'pcb.rpt'
    pcb = Path() / 'pcb' / 'pcb.kicad_pcb'

    assert report.exists()
    assert pcb.exists()

    report_mtime = report.lstat().st_mtime
    pcb_mtime = pcb.lstat().st_mtime
    assert report_mtime > pcb_mtime,\
        f'report is older ({datetime.datetime.fromtimestamp(report_mtime)} '\
        f'than pcb {datetime.datetime.fromtimestamp(pcb_mtime)}'


def test_fab_files_are_newer_than_pcb():
    pcb = Path() / 'pcb' / 'pcb.kicad_pcb'
    assert pcb.exists()

    pcb_mtime = pcb.lstat().st_mtime

    zips = (Path() / 'FAB').glob('*.zip')
    newest_zip_mtime = max([zip_.lstat().st_mtime for zip_ in zips])

    assert newest_zip_mtime > pcb_mtime,\
        f'fab zips are older ({datetime.datetime.fromtimestamp(newest_zip_mtime)} '\
        f'than pcb {datetime.datetime.fromtimestamp(pcb_mtime)}'


@pytest.mark.parametrize('pcb_path, expected_holes_amount', [
    [Path() / 'pcb' / 'pcb.kicad_pcb', 7],
    [Path() / 'cover' / 'cover.kicad_pcb', 3],
    [Path() / 'plate' / 'plate.kicad_pcb', 8],
])
def test_pcbs_hole_numbers(pcb_path, expected_holes_amount):
    board = pcbnew.LoadBoard(str(pcb_path))

    holes_amount = 0
    for m in board.GetModules():
        footprint_id = m.GetFPID().GetUniStringLibId()

        # not being sure if there is better way to checkl what is a mounting hole?
        # holes placed by scripts does not have a ":" with a lib name in front
        if 'MountingHole' in footprint_id:
            holes_amount += 1

    assert holes_amount == expected_holes_amount, pcb_path
