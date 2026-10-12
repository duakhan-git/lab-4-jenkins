.PHONY: build test deploy

build:
	python3 -m py_compile app.py

test:
	python3 -m unittest discover -v

deploy:
	@echo "Sample deployment completed successfully"
