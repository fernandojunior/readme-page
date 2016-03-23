# Some useful commands to create a simple readme page with mkdocs.
#
# Author: Fernando Felix do Nascimento Junior
# License: The MIT License

help:
	@echo 'Usage: make [command]'
	@echo 'Commands:'
	@echo '  env          Create a isolated development environment with its dependencies.'
	@echo '  deps         Install dependencies.'
	@echo '  readme-page       Create a simple readme GitHub Page.'
	@echo '  clean        Remove all generated artifacts.'

env:
	virtualenv env && . env/bin/activate && make deps

deps:
	pip install -r requirements.txt

readme-page: env
	. env/bin/activate && python readme_page.py

clean:
	rm mkdocs.yml
	rm -rf docs
	rm -r site
	rm -rf env
