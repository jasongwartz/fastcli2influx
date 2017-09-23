from influxdb import InfluxDBClient
import requests
import os
import datetime
import subprocess

INFLUX_HOST = os.environ['INFLUX_HOST'] if 'INFLUX_HOST' in os.environ else 'localhost'
INFLUX_PORT = os.environ['INFLUX_PORT'] if 'INFLUX_PORT' in os.environ else 8086
INFLUX_DATABASE = os.environ['INFLUX_DATABASE'] if 'INFLUX_DATABASE' in os.environ else 'speedtest'
#PIHOLE_API = os.environ['PIHOLE_API'] if 'PIHOLE_API' in os.environ else 'http://localhost/admin/api.php'

def get_fastcli_stats():
    return {
        "download": int(subprocess.check_output(["node", "cli.js"]).decode().split(' ')[0])
        # This assumes that the result is always in the same unit (usually Mbps)
        # TODO: handle this from the output
    }

def write_to_influx(stats_dict):
    client = InfluxDBClient(INFLUX_HOST, INFLUX_PORT, '', '', INFLUX_DATABASE)
    client.create_database(INFLUX_DATABASE)
    client.write_points([
        {
            'measurement': 'fast-cli',
            'fields': stats_dict,
        }
    ])
    print("{} Wrote fast-cli data to influxdb.".format(str(datetime.datetime.now())))

def main():
    stats = get_fastcli_stats()
    write_to_influx(stats)

if __name__ == "__main__":
    main()
