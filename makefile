OUTPUT_DIR = public
FILES = $(patsubst %.ipynb,$(OUTPUT_DIR)/%.html,$(wildcard *.ipynb))

all: $(FILES) $(OUTPUT_DIR)/index.html

$(OUTPUT_DIR)/%.html: %.ipynb makefile
	jupyter nbconvert --to html --output-dir=$(OUTPUT_DIR) $<

$(OUTPUT_DIR)/index.html:
	echo '<!DOCTYPE html><head><title>10h</title><meta charset=utf8></head><body><ul>' > $@
	$(foreach page,$(FILES),echo "<li><a href=\"""$(notdir $(page))""\">$(notdir $(page))</a></li>" >> $@)
	echo "</ul></body></html>" >> $@
