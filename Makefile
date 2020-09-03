.PHONY: watch-case all dev


all: build/case/case.png build/case/pcb.dxf build/case/plate.dxf


build/case/case.png: build/case/case.scad
	openscad --colorscheme DeepOcean -o $@ $<
build/case/pcb.dxf: build/case/pcb.scad
	openscad -o  $@ $<
build/case/plate.dxf: build/case/plate.scad
	openscad -o  $@ $<

build/case/case.scad: build/design/design.json $(wildcard case/*.py)
	mkdir -p build/case
	case/case.py $< build/case


build/design/design.json: design/design.py
	mkdir -p build/design
	$< $@

watch-case:
	watch -n1 make build/case/case.scad

dev:
	git submodule update --init --recursive