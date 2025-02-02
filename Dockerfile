# Official python docker image
FROM python:3.11 AS base

# Work directory
WORKDIR /code

COPY ./requirements.txt .
RUN python3 -m pip install --no-cache-dir --upgrade -r ./requirements.txt

FROM base AS test

COPY ./src ./src
COPY ./testing ./testing

CMD ["pytest", "testing/unit/", "-s", "-vvv"]


FROM base AS production

COPY . .

CMD ["fastapi", "run", "src/api/main.py"]
