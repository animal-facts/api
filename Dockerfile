# Official python docker image
FROM python:3.11 AS base

# Work directory
WORKDIR /code

COPY ./requirements.txt .

# Install dependencies
RUN python3 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt


FROM base as lint

COPY ./requirements-dev.txt .
COPY ./.pre-commit-config.yaml .

RUN python3 -m pip install --no-cache-dir --upgrade -r /code/requirements-dev.txt

CMD ["pre-commit", "run", "--all-files"]

FROM base as test

COPY ./src/ /code/
COPY ./testing/ /code/

CMD ["pytest", "-s", "-vvv", "testing/unit/"]


FROM test as production

CMD ["fastapi", "run", "src/api/main.py"]
