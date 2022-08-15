FROM debian:bullseye-slim

WORKDIR /home/

RUN apt-get update -y && \
	apt-get install -y vim python3 python3-pip

RUN pip3 install cryptography

RUN apt-get clean && \
	rm -rf /var/lib/apt/lists/*
	
CMD ["bash"]
