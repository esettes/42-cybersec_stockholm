FROM debian:11

RUN apt-get update -y && apt-get install -y vim python3 python3-pip
RUN pip3 install cryptography
#RUN pip3 install --upgrade pip3 setuptools
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
