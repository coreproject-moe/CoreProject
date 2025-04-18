from attrs import asdict, define, field, validators
from quart import json

from coreproject_tracker.constants import PEER_TTL
from coreproject_tracker.converters import (
    convert_str_int_to_float,
)
from coreproject_tracker.functions import (
    hset,
)
from coreproject_tracker.validators import (
    validate_ip,
    validate_port,
)


@define
class RedisDatastructure:
    info_hash: str = field(
        validator=validators.instance_of(str), metadata={"asdict": False}
    )
    type: str = field(validator=validators.instance_of(str))
    peer_id: str = field(validator=validators.instance_of(str))
    peer_ip: str = field(validator=[validate_ip])
    port: int = field(converter=int, validator=[validate_port])
    left: float | None = field(converter=convert_str_int_to_float)

    async def save(self) -> None:
        """
        Save the object to Redis.
        """

        await hset(
            self.info_hash,
            f"{self.peer_ip}:{self.port}",
            json.dumps(asdict(self, recurse=True)),
            expire_time=60 if self.type == "websocket" else PEER_TTL,
        )
