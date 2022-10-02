from huey.contrib.djhuey import task

from django.core.management import call_command


@task()
def call_character_management_command(_reset: bool):

    call_command("populate_characters", headless=True, reset=_reset)
