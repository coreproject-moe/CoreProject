import asyncio

try:
    import uvloop  # type: ignore

    HAS_UVLOOP = True
except ImportError:
    HAS_UVLOOP = False

from coreproject_tracker.main import main

if HAS_UVLOOP:
    uvloop.run(main())

else:
    asyncio.run(main())
