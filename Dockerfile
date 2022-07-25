FROM debian:11

RUN apt-get update -y && apt-get install -y vim python3 python3-pip
<<<<<<< HEAD
RUN pip3 install cryptography rich
=======
RUN pip3 install cryptography
>>>>>>> 9ca1889b60988470c8820949d199c7d9505e7cc8
#RUN pip3 install --upgrade pip3 setuptools
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
