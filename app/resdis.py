import redis
import sys

def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="redis",
            port=6379,
            password="test",
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)
