import multiprocessing
import os

__all__ = ["WORKERS_COUNT"]

WORKERS_COUNT = int(
    os.environ.get(
        "WORKERS_COUNT",
        max(
            2,  # 2 is here cause of `http and websocket server` and `UDP server` each should use 1 core
            multiprocessing.cpu_count()
            - 2,  # 2 is here cause of `redis` and `UDP server` each needs 1 core
        ),
    )
)
