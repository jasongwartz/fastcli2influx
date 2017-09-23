FROM jasongwartz/fast-cli

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python-pip

RUN pip install influxdb

COPY fastcli2influx.py /src
COPY start.sh /src

ENV DAEMON_SLEEP_TIME=600
CMD ["./start.sh"]


