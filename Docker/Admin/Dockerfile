FROM ubuntu:latest

RUN apt-get update -y 
RUN apt-get install -y python3.7
RUN apt install -y python3-pip
RUN apt install -y git 
RUN apt install make 
RUN git clone https://github.com/hyperledger/fabric-sdk-py.git && cd fabric-sdk-py && make install 
RUN cd ..

ADD configtxgen bin/configtxgen
ADD execute.sh execute.sh

CMD ["./execute.sh"]









