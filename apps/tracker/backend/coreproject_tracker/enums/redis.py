from enum import Enum


class REDIS_NAMESPACE_ENUM(str, Enum):
    HTTP_UDP = "http_udp"
    WEBSOCKET = "websocket"
