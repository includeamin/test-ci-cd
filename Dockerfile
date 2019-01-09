FROM ubuntu:18.04

EXPOSE 3005

RUN apt-get update -y && \
    apt-get install -y python3.6 python3.6-dev python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/accounting/requirements.txt

WORKDIR /app/accounting

RUN pip3 install -r requirements.txt

COPY . .



CMD ["python3.6","-u","main.py"]