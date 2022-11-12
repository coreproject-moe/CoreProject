import subprocess
import os
import shutil
from pathlib import Path
from distutils.dir_util import copy_tree

BASE_DIR = Path(__file__).resolve().parent


def build_animecore():
    os.chdir(f"{BASE_DIR}/frontend/AnimeCore/")

    # NPM commands
    subprocess.check_call("npm install", shell=True)
    subprocess.check_call("npm run build", shell=True)

    os.makedirs(
        os.path.dirname(
            f"{BASE_DIR}/backend/django_core/apps/frontend/templates/frontend/"
        ),
        exist_ok=True,
    )
    shutil.copy(
        f"{BASE_DIR}/frontend/AnimeCore/build/app.html",
        f"{BASE_DIR}/backend/django_core/apps/frontend/templates/frontend/animecore.html",
    )
    copy_tree(
        f"{BASE_DIR}/frontend/AnimeCore/build/",
        f"{BASE_DIR}/backend/django_core/static/",
    )


build_animecore()
