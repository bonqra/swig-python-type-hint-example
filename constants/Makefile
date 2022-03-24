.PHONY: build swig

build:
	python setup.py build_ext --inplace

swig:
	swig -python example.i

all: swig build
