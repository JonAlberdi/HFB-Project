FROM ubuntu:latest

RUN apt-get update -y \
&& apt-get install -y python3.7 

RUN apt install -y python3-pip
RUN pip3 install -U pymodbus[twisted]

ADD ServidorAsync.py ServidorAsync.py
CMD ["python3","ServidorAsync.py"]




