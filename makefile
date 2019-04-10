OUTPUT_DIR = public
FILES = $(sort $(patsubst %.ipynb,$(OUTPUT_DIR)/%.html,$(wildcard *.ipynb)))

all: $(FILES) $(OUTPUT_DIR)/index.html

$(OUTPUT_DIR)/%.html: %.ipynb makefile
	jupyter nbconvert --to html --output-dir=$(OUTPUT_DIR) $<

$(OUTPUT_DIR)/index.html: $(FILES) makefile
	echo '<!DOCTYPE html><head><title>10h</title><meta charset=utf8>' > $@;
	echo '<meta name="viewport" content="width=device-width, initial-scale=1"></head><body><ul>' >> $@;
	$(foreach page,$(FILES),echo "<li><a href=\"""$(notdir $(page))""\">$(notdir $(page))</a></li>" >> $@;)
	echo "</ul></body></html>" >> $@

clean:
	rm $(OUTPUT_DIR)/*
