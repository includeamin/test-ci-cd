FROM ubuntu:18.04
MAINTAINER aminjamal <aminjamal10@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python3.6 python3-pip

# Setup flask application
RUN mkdir -p /deploy/app
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY . /deploy/app

RUN pip3 install -r /deploy/app/requirements.txt
RUN pip3 install gunicorn
WORKDIR /deploy/app

EXPOSE 3007

# Start gunicorn
CMD ["/usr/local/bin/gunicorn", "--config", "/deploy/gunicorn_config.py" , "app:app"]