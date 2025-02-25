.PHONY: doc

doc:
	mkdir -p doc
	python3 -m pydoc -w `find . -name '*.py'`
	mv *.html doc


