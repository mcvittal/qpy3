FROM ubuntu:latest
MAINTAINER Alex McVittie "alex@skywatch.com"
ARG DEBIAN_FRONTEND="noninteractive"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential xvfb python3-qgis qgis
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install xvfbwrapper


COPY .. /qpy
WORKDIR /qpy/tests
RUN python3 tests.py
