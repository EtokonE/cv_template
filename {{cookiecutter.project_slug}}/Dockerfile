FROM python:{{cookiecutter.python_version}}-slim as base

RUN apt-get update && \
    apt-get install -y curl git && \
    apt-get clean

ENV POETRY_VERSION={{cookiecutter.poetry_version}}
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app
RUN poetry install

CMD ["/bin/bash"]
