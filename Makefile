install:
	uv sync

lint:
	uv run ruff check .

test:
	uv run pytest

test-cov:
	uv run pytest --cov=gendiff --cov-report=xml

check: lint test

.PHONY: install lint test test-cov check