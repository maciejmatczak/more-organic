.PHONY: watch-case all dev


all: images/plate.png build/case/plate.dxf


images/plate.png: build/case/plate.scad
	mkdir -p images
	openscad --colorscheme DeepOcean -o images/plate.png build/case/plate.scad

build/case/plate.dxf: build/case/plate.scad
	openscad -o build/case/plate.dxf build/case/plate.scad

build/case/plate.scad: build/design/design.json $(wildcard case/*.py)
	mkdir -p build/case
	case/plate.py build/design/design.json build/case/plate.scad


build/design/design.json: design/design.py
	mkdir -p build/design
	design/design.py build/design/design.json

watch-case:
	watchmedo shell-command -R\
		build\
		case\
		design\
		-c 'make build/case/plate.scad'

dev:
	git submodule update --init --recursive