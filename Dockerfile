FROM python:3.10-alpine

RUN apk  update --no-cache && apk upgrade --no-cache --available

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN pip install --no-cache-dir poetry==1.7.1 && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . /code
