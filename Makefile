.PHONY: all
## Install python environment and dependencies
all: clean init build install install-dev test

## Test 
test:
	python -m pytest 

## Clean up the project
clean: 
	find ./src -name "*.pyc" -exec rm -f {} \;
	find ./src -type d -empty -delete

## Inittialize python environment
init: 
	python -m pip install --upgrade pip
	python -m pip install pip-tools

## Install for production
install:
	python -m pip install -e .

## Install for development 
install-dev: install
	python -m pip install -e ".[dev]"

## Build dependencies
build: 
	pip-compile --resolver=backtracking --output-file=requirements.txt pyproject.toml
	pip-compile --resolver=backtracking --extra=dev --output-file=requirements-dev.txt pyproject.toml

## Format files using black
format:
	autoflake --in-place --remove-all-unused-imports -r .
	isort .
	black .

## Run checks (ruff + test)
check:
	ruff .
	isort --check . 
	black --check .

.DEFAULT_GOAL := show-help
# See <https://gist.github.com/klmr/575726c7e05d8780505a> for explanation.
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)";echo;sed -ne"/^## /{h;s/.*//;:d" -e"H;n;s/^## //;td" -e"s/:.*//;G;s/\\n## /---/;s/\\n/ /g;p;}" ${MAKEFILE_LIST}|LC_ALL='C' sort -f|awk -F --- -v n=$$(tput cols) -v i=19 -v a="$$(tput setaf 6)" -v z="$$(tput sgr0)" '{printf"%s%*s%s ",a,-i,$$1,z;m=split($$2,w," ");l=n-i;for(j=1;j<=m;j++){l-=length(w[j])+1;if(l<= 0){l=n-i-length(w[j])-1;printf"\n%*s ",-i," ";}printf"%s ",w[j];}printf"\n";}'|more $(shell test $(shell uname) == Darwin && echo '-Xr')
