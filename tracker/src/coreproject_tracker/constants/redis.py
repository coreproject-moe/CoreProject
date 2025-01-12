import os
from datetime import timedelta

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)

HASH_EXPIRE_TIME = int(timedelta(days=1).total_seconds())
