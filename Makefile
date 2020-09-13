.PHONY: dev all case watch-case-assembly design pcb-place pcb-dump


all: case


# case: build/case/assembly.png build/case/pcb.dxf build/case/plate.dxf

watch-case-assembly:
	watch -n1 make assembly

# build/case/assembly.png: build/case/assembly.scad
# 	openscad --colorscheme DeepOcean -o $@ $<
# build/case/pcb.dxf: build/case/pcb.scad
# 	openscad -o  $@ $<
.PHONY: assembly
assembly: build/case/assembly.scad
build/case/assembly.scad: build/pcb/footprint_dump.json build/design/mh_standoff.json $(wildcard case/*.py)
	mkdir -p build/case
	case/case.py\
		--kicad-dump build/pcb/footprint_dump.json\
		--mh-standoff build/design/mh_standoff.json\
		-o build/case

PCB=pcb/more-organic/more-organic.kicad_pcb


pcb-dump: build/pcb/footprint_dump.json


build/pcb/footprint_dump.json: $(PCB)
	mkdir -p build/pcb
	scripts/dump_footprints.py $< $@


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