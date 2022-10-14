from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from api import router as api_router
from settings import DATABASE_URL, MODELS

from .views import router as view_router

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)
app.include_router(view_router)

# Startup and shutdown are handled by this stupid shit
# Do not use @app.on_event('startup') and @app.on_event('shutdown')
# It wont work
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)
