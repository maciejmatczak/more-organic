.PHONY: dev all case watch-case-assembly design pcb-place


all: case

pcb-place: pcb/more-organic/more-organic.kicad_pcb

pcb/more-organic/more-organic.kicad_pcb: build/design/design.json
	scripts/place_footprints.py\
		pcb/more-organic/more-organic.kicad_pcb\
		build/design/design.json


case: build/case/assembly.png build/case/pcb.dxf build/case/plate.dxf

watch-case-assembly:
	watch -n1 make build/case/assembly.scad

build/case/assembly.png: build/case/assembly.scad
	openscad --colorscheme DeepOcean -o $@ $<
build/case/pcb.dxf: build/case/pcb.scad
	openscad -o  $@ $<
build/case/plate.dxf: build/case/plate.scad
	openscad -o  $@ $<

build/case/assembly.scad: build/design/design.json $(wildcard case/*.py)
	mkdir -p build/case
	case/case.py $< build/case


design: build/design/design.json

build/design/design.json: design/design.py
	mkdir -p build/design
	$< $@


dev:
	git submodule update --init --recursive