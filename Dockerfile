FROM python:3.10

WORKDIR /boredairflow

COPY ./requirements.txt /boredairflow/requirements.txt

RUN pip install -r requirements.txt
