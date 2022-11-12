import subprocess
import os
import shutil


def build_animecore():
    os.chdir(f'{os.getcwd()}/frontend/AnimeCore/')
    
    # NPM commands
    subprocess.check_call('npm install',shell=True)
    subprocess.check_call('npm run build',shell=True)

    shutil.copy2(f'{os.getcwd()}/frontend/AnimeCore/build',f'{os.getcwd()}/backend/django_core/static/')


build_animecore()