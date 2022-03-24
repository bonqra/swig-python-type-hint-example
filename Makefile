.PHONY: build swig

SUBDIRS = class constants std_map std_vector variables

build:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir build; \
	done

swig:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir swig; \
	done

all: swig build
