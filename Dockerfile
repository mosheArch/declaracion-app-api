FROM python:3.8-alpine
MAINTAINER App Delcaracion Patrimonial by Hallvaror

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /App

RUN adduser -D user
USER user
