FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN mkdir -p /opt/demo
WORKDIR /opt/demo
COPY requirements.pip .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.pip

ADD ./ ./

ENTRYPOINT ["python3", "app.py"]