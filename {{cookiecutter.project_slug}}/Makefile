.PHONY: install test lint format pre-commit-check

install:
\tpoetry install

test:
\tpoetry run pytest

lint:
\tpoetry run flake8 src

format:
\tpoetry run black src

pre-commit-check:
\tpoetry run pre-commit run --all-files
