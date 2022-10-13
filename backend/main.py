from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import DATABASE_URL, MODELS
import models
from api import router as api_router
from views import router as view_router
from pathlib import Path
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)
app.include_router(view_router)


@app.on_event("startup")
async def startup() -> None:
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": MODELS},
        generate_schemas=True,
        add_exception_handlers=True,
    )


@app.on_event("shutdown")
async def shutdown() -> None:
    await Tortoise.close_connections()
