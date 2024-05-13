# link new image from another image of python
FROM python:3.8-alpine

COPY ./wateja/requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

# Install requirements
RUN pip install -r /requirements.txt

RUN mkdir /api
# COPY files in the host machine to the container
COPY ./wateja /api

# Change into the backend directory
WORKDIR /api
