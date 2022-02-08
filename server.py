import os
from pathlib import Path, PurePath
from multiprocessing import Process

FILE_LOCATION = Path(__file__).parent


def run_caddy():
    if os.name == "nt":
        os.system(
            f".\windows\caddy.exe run --watch --config {PurePath(FILE_LOCATION, 'Caddyfile')}"
        )
    elif os.name == "posix":
        os.system(f"caddy run --watch  --config {PurePath(FILE_LOCATION, 'Caddyfile')}")


def run_redis():
    if os.name == "nt":
        os.system(".\\windows\\redis-server.exe")


def run_django():
    # os.system("python .\\manage.py runserver")
    os.system('uvicorn core.asgi:application')

def run_banken():
    os.system("python .\\scripts\\banken.py")


def collect_staticfiles():
    os.system("python .\\manage.py collectstatic --no-input")


def run():
    global p1, p2, p3, p4, p5
    
    # Utility first
    p1 = Process(target=collect_staticfiles).start()

    # Main scripts
    p2 = Process(target=run_redis).start()
    p3 = Process(target=run_caddy).start()
    p4 = Process(target=run_django).start()
    p5 = Process(target=run_banken).start()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        p1.kill()
        p2.kill()
        p3.kill()
        p4.kill()
        p5.kill()
