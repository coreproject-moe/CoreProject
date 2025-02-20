# test1 = [<ACTIONS.CONNECT: 0>, 1343841263, b"\x00\x00\x04\x17'\x10\x19\x80"]
# test2 = [<ACTIONS.CONNECT: 0>, 3620577650, b"\x00\x00\x04\x17'\x10\x19\x80"]


# twisted = [b"\x00\x00\x00\x00", b"2\xf4\xe1\xab", b"\x00\x00\x04\x17'\x10\x19\x80"]
# quart =   [b'\x00\x00\x00\x00', b'\x84\xc6\xdd\x8e', b"\x00\x00\x04\x17'\x10\x19\x80"]

import asyncio
from coreproject_tracker.functions import to_uint32
# [<ACTIONS.CONNECT: 0>, 1343841263, b"\x00\x00\x04\x17'\x10\x19\x80"]


async def test():
    return b"".join(
        [
            await to_uint32(0),
            await to_uint32(1343841263),
            b"\x00\x00\x04\x17'\x10\x19\x80",
        ]
    )


print(asyncio.run(test()) == b"\x00\x00\x00\x00P\x19c\xef\x00\x00\x04\x17'\x10\x19\x80")
