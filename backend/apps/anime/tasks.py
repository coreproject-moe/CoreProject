from celery import shared_task


@shared_task()
def add(x, y):
    with open("test.txt", "w+") as f:
        f.write(str(x + y))
