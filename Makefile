.PHONY: dev all case watch-case-assembly design pcb-place


all: case

PCB=pcb/more-organic/more-organic.kicad_pcb

pcb-place:
	scripts/place_footprints.py\
		$(PCB)\
		build/design/sw_and_dio.json
	
	scripts/mh_delete.py\
		$(PCB)

	scripts/mh_add.py\
		$(PCB)\
		build/design/mh_pcb_to_plate.json
	scripts/mh_add.py\
		$(PCB)\
		build/design/mh_pcb_to_small_plate.json


case: build/case/assembly.png build/case/pcb.dxf build/case/plate.dxf

watch-case-assembly:
	watch -n1 make build/case/assembly.scad

build/case/assembly.png: build/case/assembly.scad
	openscad --colorscheme DeepOcean -o $@ $<
build/case/pcb.dxf: build/case/pcb.scad
	openscad -o  $@ $<

build/case/assembly.scad: build/design/design.json $(wildcard case/*.py)
	mkdir -p build/case
	case/case.py $< build/case


design_files = $(addprefix build/design/,\
	sw_and_dio.json\
	mh_pcb_to_plate.json \
	mh_pcb_to_small_plate.json\
	mh_standoff.json\
)

design: $(design_files)

$(design_files): design/design.py
	mkdir -p build/design
	$< build/design


dev:
	git submodule update --init --recursive