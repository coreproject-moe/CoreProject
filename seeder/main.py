import flet as ft

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

os.environ["DATABASE_URL"] = "sqlite:////" + str(os.path.join(BASE_DIR, "default.db"))

# This must be imported after os.environ
from src.seeder_flet.main import main  # noqa: E402

ft.app(main, assets_dir="assets/")
