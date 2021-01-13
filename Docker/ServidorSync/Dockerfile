FROM ubuntu:latest

RUN apt-get update -y \
&& apt-get install -y python3.7 

RUN apt install -y python3-pip
RUN apt install -y git
RUN pip3 install -U pymodbus[twisted]
RUN git clone https://github.com/hyperledger/fabric-sdk-py.git && cd fabric-sdk-py && make install
RUN cd ..


ADD execute.sh execute.sh
COPY sync.py /usr/local/lib/python3.8/dist-packages/pymodbus/server/

CMD ["./execute.sh"]





