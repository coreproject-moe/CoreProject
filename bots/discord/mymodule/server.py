# coding: utf-8
import random
from aiohttp import web
from mymodule.entity import Object


async def post(req):
    engine = req.app.engine
    name = random.randint(0, 1e9)
    op = Object.insert().values(name=str(name))
    async with engine.acquire() as conn:
        res = await conn.execute(op)
        row = await res.fetchone()
    return web.json_response({'id': row[0]})


class MyApplication(web.Application):

    async def _create_engine(self, app):
        self.engine = await self._engine_creater.create()

    def __init__(self, engine_creater, *args, **kwargs):
        self._engine_creater = engine_creater
        super(MyApplication, self).__init__(*args, **kwargs)
        self.on_startup.append(self._create_engine)
        self.router.add_post('/', post)
