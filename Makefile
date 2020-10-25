PCB=pcb/pcb.kicad_pcb
PCB_PLATE=plate/plate.kicad_pcb
PCB_COVER=cover/cover.kicad_pcb


.PHONY: plot

ZIPS=$(addprefix build/fab/make-organic-,\
	$(notdir \
		$(patsubst %.kicad_pcb,%.zip,$(PCB) $(PCB_PLATE) $(PCB_COVER))\
	)\
)

plot: $(ZIPS)

.SECONDEXPANSION:
build/fab/make-organic-%.zip: $$*/$$*.kicad_pcb
	mkdir -p $(dir $@)
	
	scripts/plot_fab.py $< $(dir $@)$*
	
	7z a $@ $(dir $@)$*


.PHONY: cover-place

cover-place: 
	scripts/mh_delete.py\
		$(PCB_COVER)

	scripts/mh_add.py\
		$(PCB_COVER)\
		build/pcb/footprint_dump.json\
		--filter-footprint MountingHole_2.2mm_M2_Pad_Via\
		--x-lt 0


.PHONY: plate-place

plate-place:
	scripts/mh_delete.py\
		$(PCB_PLATE)

	scripts/mh_add.py\
		$(PCB_PLATE)	\
		data/design/mh_standoff.json


.PHONY: case case-assembly case-assembly-watch

case-assembly-watch:
	watch -n1 make case-assembly
case-assembly: data/case/assembly.scad

case: $(addprefix data/case/,\
	assembly.png\
	pcb.dxf\
	plate.dxf\
	cover.dxf\
)

data/case/%.png: data/case/%.scad
	openscad --colorscheme DeepOcean -o $@ $<

data/case/%.dxf: data/case/%.scad
	openscad -o $@ $<

scad_files=$(addprefix data/case/,\
	assembly.scad\
	pcb.scad\
	cover.scad\
	plate.scad\
)
$(scad_files): build/pcb/footprint_dump.json data/design/mh_standoff.json $(wildcard case/*.py)
	mkdir -p data/case
	case/case.py\
		--kicad-dump build/pcb/footprint_dump.json\
		--mh-standoff data/design/mh_standoff.json\
		-o data/case


.PHONY: pcb-dump pcb-place

pcb-dump: build/pcb/footprint_dump.json

build/pcb/footprint_dump.json: $(PCB)
	mkdir -p build/pcb
	scripts/dump_footprints.py $< $@

pcb-place:
	scripts/place_footprints.py\
		$(PCB)\
		data/design/sw_and_dio.json
	
	scripts/mh_delete.py\
		$(PCB)

	scripts/mh_add.py\
		$(PCB)\
		data/design/mh_pcb_to_plate.json


.PHONY: design

design_files = $(addprefix data/design/,\
	sw_and_dio.json\
	mh_pcb_to_plate.json \
	mh_standoff.json\
)

design: $(design_files)

$(design_files): design/design.py
	mkdir -p data/design
	$< data/design


dev:
	git submodule update --init --recursive


.PHONY: clean
clean:
	rm -rf build