from attrs import define, field, validators

from coreproject_tracker.validators import (
    validate_ip,
    validate_port,
)


@define
class RedisDatastructure:
    type: str = field(validator=validators.instance_of(str))
    peer_id: str = field(validator=validators.instance_of(str))
    peer_ip: str = field(validator=[validate_ip])
    port: int = field(converter=int, validator=[validate_port])
    left: int = field(validator=validators.instance_of(int))
