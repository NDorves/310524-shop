FROM python:3

RUN apt update && \
    apt install -y default-mysql-client

WORKDIR /usr/src/app

COPY ./app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
