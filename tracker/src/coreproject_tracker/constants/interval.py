from datetime import timedelta

ANNOUNCE_INTERVAL = int(timedelta(hours=1).total_seconds() / 60)  # 1 hour
WEBSOCKET_INTERVAL = int(timedelta(minutes=2).total_seconds())  # 2 min
