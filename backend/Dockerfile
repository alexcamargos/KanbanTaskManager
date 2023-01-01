FROM tiangolo/uvicorn-gunicorn:python3.11

COPY ./requirements-dev.txt /app/requirements-dev.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements-dev.txt

COPY ./src /app/src
COPY main.py /app/
