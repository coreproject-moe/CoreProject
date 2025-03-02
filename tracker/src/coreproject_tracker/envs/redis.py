import os

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_DATABASE = os.environ.get("REDIS_DATABASE", 0)
