# coding: utf-8
from mymodule.server import MyApplication
from mymodule.database import EngineCreater


def app():
    engine_creater = EngineCreater()
    app = MyApplication(engine_creater)
    return app
