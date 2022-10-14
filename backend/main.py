import sys
from typing import Any

from fastapi import FastAPI, applications
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from api import router as api_router
from settings.settings import BASE_DIR, DATABASE_URL, MODELS, STATIC_DIR, STATIC_URL
from views import router as views_router

# Hijack path
sys.path.append(str(BASE_DIR))

app = FastAPI(default_response_class=ORJSONResponse)

# Static mounts
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(api_router)
app.include_router(views_router)


# Monkeypatch both swagger and redoc
def swagger_monkey_patch(*args: Any, **kwargs: Any) -> HTMLResponse:
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_css_url=f"{STATIC_URL}/fastapi/swagger-ui.css",
        swagger_js_url=f"{STATIC_URL}/fastapi/swagger-ui-bundle.js",
        swagger_favicon_url=f"{STATIC_URL}/fastapi/favicon.png",
    )


applications.get_swagger_ui_html = swagger_monkey_patch  # type: ignore


def redoc_monkey_patch(*args: Any, **kwargs: Any) -> HTMLResponse:
    return get_redoc_html(
        *args,
        **kwargs,
        redoc_js_url=f"{STATIC_URL}/fastapi/redoc.standalone.js",
        redoc_favicon_url=f"{STATIC_URL}/fastapi/favicon.png",
    )


applications.get_redoc_html = redoc_monkey_patch  # type: ignore

# Startup and shutdown are handled by this stupid shit
# Do not use @app.on_event('startup') and @app.on_event('shutdown')
# It wont work
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={
        "models": MODELS,
    },
    generate_schemas=True,
    add_exception_handlers=True,
)
