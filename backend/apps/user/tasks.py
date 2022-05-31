from huey import crontab
from huey.contrib.djhuey import periodic_task, task


@task()
def count_beans(number):
    print("-- counted %s beans --" % number)
    return "Counted %s beans" % number
