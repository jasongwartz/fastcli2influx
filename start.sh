#!/bin/bash

while true; do python fastcli2influx.py; sleep $DAEMON_SLEEP_TIME; done
