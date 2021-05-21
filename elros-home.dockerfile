FROM ubuntu:latest

ARG host=", host='0.0.0.0"

RUN apt-get update

RUN apt-get install -y python3.8

RUN apt install -y python3-pip

RUN pip3 install flask

RUN mkdir /app

COPY /website-code/ /app

WORKDIR /app

RUN sed -i 's/debug=True:.*/debug=True:$host/g' app.py

RUN cat app.py

CMD python3 app.py