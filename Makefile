# Some useful commands to create a simple readme page with mkdocs.
#
# Author: Fernando Felix do Nascimento Junior
# License: MIT License
# Homepage: http://fernandojunior.github.io/readme-page

help:
	@echo 'Usage: make [command]'
	@echo 'Commands:'
	@echo '  env          Create a isolated development environment with its dependencies.'
	@echo '  deps         Install dependencies.'
	@echo '  build        Create a dist package.'
	@echo '  install      Install a local dist package with pip.'
	@echo '  clean        Remove all generated artifacts.'

env:
	virtualenv env && . env/bin/activate && make deps

deps:
	pip install -r requirements.txt

build:
	python setup.py sdist

install: build
	pip install dist/*.tar.gz

clean:
	rm mkdocs.yml
	rm -rf docs
	rm -r site
	rm -rf env
