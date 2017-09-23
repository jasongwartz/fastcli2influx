# fastcli2influx
A script to make a speedtest request to Netflix's Fast.com and write the result into InfluxDB

Run using:
```
docker run --name=fastcli2influx \
  -e ENVIRONMENT_VARIABLE=value \       # see below for options
  jasongwartz/fastcli2influx
```

The default image `jasongwartz/fastcli2influx` is built for x86 devices; this is because PhantomJS (one of the dependencies of [fast-cli](https://github.com/sindresorhus/fast-cli) upon which this is based) failed to install on ARM.

Configuration:
The following parameters can be customised using environment variables:
- `INFLUX_HOST` - default is `localhost`
- `INFLUX_PORT` - default is `8086`
- `INFLUX_DATABASE` - default is `speedtest`
