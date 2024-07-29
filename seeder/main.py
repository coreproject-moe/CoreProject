import flet as ft
import os

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./default.db"

# This must be imported after os.environ
from src.seeder_flet.main import main  # noqa: E402

ft.app(main, assets_dir="assets/")
