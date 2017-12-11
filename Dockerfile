FROM ubuntu:latest
EXPOSE 8080
RUN apt-get update
RUN apt-get -y install python3-pip
ADD . /opt/www-cloud-fortress-com
WORKDIR /opt/www-cloud-fortress-com
RUN pip3 install -r ./requirements.txt
CMD cd /opt/www-cloud-fortress-com/; ./run_server.py
