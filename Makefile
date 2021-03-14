install:
	poetry install

package-install: build
	python3 -m pip install --user dist/*.whl

run:
	poetry run gendiff $(arg)

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

publish: check
	poetry build
	poetry publish -r testpypi

# brain-games:
# 	@poetry run brain-games

.PHONY: install test lint selfcheck check build
