from datetime import timedelta

HASH_EXPIRE_TIME = int(timedelta(days=1).total_seconds())

# Minimum redis version we support
REDIS_SERVER_VERSION = "7.4.2"
