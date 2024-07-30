import requests

from shinobi.parser.staff import StaffParser
from shinobi.utilities.session import session

import flet as ft
import os
import asyncio

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./default.db"


from src.seeder_flet.models._engine import Session
from src.seeder_flet.models._models import Staff


from shinobi.builder.staff import StaffBuilder


builder = StaffBuilder()
dictionary = builder.build_dictionary(sort=True)


# noqa: E501


async def create():
    async with Session() as _session:
        for i in dictionary:
            db_obs = Staff(mal_id=i)
            _session.add(db_obs)
        await _session.commit()


asyncio.run(create())
