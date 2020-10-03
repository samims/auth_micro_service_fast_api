FROM python:3.8-slim

MAINTAINER Samiul
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 0

#RUN useradd -ms /bin/bash sam

RUN mkdir code

WORKDIR /code/
#RUN chown -R sam:sam /code
#RUN chmod 755 /code

COPY . /code/
#USER sam


RUN pip install -r requirements.txt



