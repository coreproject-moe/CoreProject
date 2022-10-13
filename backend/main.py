from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import models
from api import router as api_router
from views import router as view_router
from database import *
from pathlib import Path

app = FastAPI()


@app.on_event("startup")
async def run():
    async with engine.begin() as conn:
        await conn.run_sync(BASE.metadata.drop_all)
        await conn.run_sync(BASE.metadata.create_all)


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)
app.include_router(view_router)
