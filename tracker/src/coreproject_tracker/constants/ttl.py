from datetime import timedelta

PEER_TTL = int(timedelta(hours=1).total_seconds())
CONNECTION_TTL = int(timedelta(minutes=5).total_seconds())
