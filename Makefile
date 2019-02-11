.PHONY: all clean format

all: $(GENERATED_FILES)

clean:
	rm recent.* formatted.json metadata.csv

recent.json:
	wget --no-use-server-timestamps -O $@ \
	'https://catalog.data.gov/api/action/package_search?q=&sort=metadata_modified+desc&rows=50'


#.INTERMEDIATE: recent.csv
formatted.json: recent.json
	cat $< | python3 transform.py > $@

metadata.csv: formatted.json
	in2csv -f json $< > $@
