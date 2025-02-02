# Official python docker image
FROM python:3.11 AS base

# Work directory
WORKDIR /code

COPY ./requirements.txt .

# Install dependencies
RUN python3 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt

FROM base as test

COPY ./src/ /code/
COPY ./testing/ /code/

CMD ["pytest", "-s", "-vvv", "/code/testing/unit/"]


FROM base as production

COPY . .

CMD ["fastapi", "run", "/code/src/api/main.py"]
