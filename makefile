FILES = $(patsubst %.ipynb,html/%.html,$(wildcard *.ipynb))

all: $(FILES)

html/%.html: %.ipynb makefile
	jupyter nbconvert --to html --output-dir=html $<
