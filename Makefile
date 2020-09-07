.PHONY: watch-case dev all case


all: case

case: build/case/assembly.png build/case/pcb.dxf build/case/plate.dxf


build/case/assembly.png: build/case/assembly.scad
	openscad --colorscheme DeepOcean -o $@ $<
build/case/pcb.dxf: build/case/pcb.scad
	openscad -o  $@ $<
build/case/plate.dxf: build/case/plate.scad
	openscad -o  $@ $<

build/case/assembly.scad: build/design/design.json $(wildcard case/*.py)
	mkdir -p build/case
	case/case.py $< build/case


build/design/design.json: design/design.py
	mkdir -p build/design
	$< $@

watch-case:
	watch -n1 make build/case/assembly.scad

dev:
	git submodule update --init --recursive