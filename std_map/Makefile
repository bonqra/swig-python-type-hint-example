.PHONY: build swig

build:
	python setup.py build_ext --inplace

swig:
	swig -c++ -python example.i

all: swig build
