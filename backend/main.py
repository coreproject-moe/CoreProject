from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import models
from api import router as api_router
from views import router as view_router
from pathlib import Path
from tortoise import Tortoise

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)
app.include_router(view_router)
