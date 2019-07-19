
### Install redis

https://medium.com/@djamaldg/install-use-redis-on-macos-sierra-432ab426640e

Example of configuration file:
6380.conf
In order to run redis with this configuration file: ```redis-server /usr/local/etc/redis.conf```


### Useful commands:

Get all redis processes:
```ps -u Dmitry -o pid,rss,command | grep redis```

Get PID of redis process:
```pgrep redis-server```

Stop some of process (in particular, redis process) 
```kill -9 <PID>```

Run redis from configuration:
```redis-server /etc/redis/6379.conf```

Connect to redis:
```redis-cli -p 6380```

In case of error “Redis is configured to save RDB snapshots, but is currently …”
then run ```redis-cli``` and inside it run: ```config set stop-writes-on-bgsave-error no```


### Source of tutorials
https://realpython.com/python-redis/