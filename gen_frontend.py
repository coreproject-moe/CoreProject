import os
import shutil
import subprocess
from multiprocessing import Process
from pathlib import Path
from shutil import copytree

BASE_DIR = Path(__file__).resolve().parent


def build_animecore():
    os.chdir(f"{BASE_DIR}/frontend/AnimeCore/")

    # NPM commands
    subprocess.check_call("npm install", shell=True)
    subprocess.check_call("npm run build:static", shell=True)

    os.makedirs(
        os.path.dirname(
            f"{BASE_DIR}/backend/django_core/apps/frontend/templates/frontend/"
        ),
        exist_ok=True,
    )
    shutil.move(
        f"{BASE_DIR}/frontend/AnimeCore/build/app.html",
        f"{BASE_DIR}/backend/django_core/apps/frontend/templates/frontend/animecore.html",
    )
    copytree(
        f"{BASE_DIR}/frontend/AnimeCore/build/",
        f"{BASE_DIR}/backend/django_core/static/",
        dirs_exist_ok=True,
    )


def build_user():
    os.chdir(f"{BASE_DIR}/frontend/User/")

    # NPM commands
    subprocess.check_call("npm install", shell=True)
    subprocess.check_call("npm run build:static", shell=True)

    os.makedirs(
        os.path.dirname(
            f"{BASE_DIR}/backend/django_core/apps/frontend/templates/frontend/"
        ),
        exist_ok=True,
    )
    shutil.move(
        f"{BASE_DIR}/frontend/User/build/app.html",
        f"{BASE_DIR}/backend/django_core/apps/frontend/templates/frontend/user.html",
    )
    copytree(
        f"{BASE_DIR}/frontend/User/build/",
        f"{BASE_DIR}/backend/django_core/static/",
        dirs_exist_ok=True,
    )


if __name__ == "__main__":
    Process(target=build_animecore).start()
    Process(target=build_user).start()
