from datetime import timedelta

WEBSOCKET_PEER_TTL = int(timedelta(minutes=1).total_seconds())
WEBSOCKET_INTERVAL = WEBSOCKET_PEER_TTL / 2
