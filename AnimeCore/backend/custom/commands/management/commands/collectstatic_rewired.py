import os
import json
import shutil

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Remove unnecessary files generated from Whitenoise"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.static_dir: str = os.path.join(settings.BASE_DIR, "staticfiles")
        self.count: int = 0

        self.json_data = self.__load_json()

    def __load_json(self) -> object:
        if os.path.isdir(self.static_dir):
            shutil.rmtree(self.static_dir)
        management.call_command("collectstatic")
        return json.load(
            open(os.path.join(settings.BASE_DIR, "staticfiles", "staticfiles.json"))
        )

    def __remove_and_add(self, path: str) -> None:
        try:
            os.remove(path)
            self.count += 1
        except FileNotFoundError:
            if os.path.isfile(path):
                self.count -= 1

    def handle(self):
        for file in self.json_data["paths"]:
            self.__remove_and_add(os.path.join(self.static_dir, file))
            self.__remove_and_add(os.path.join(self.static_dir, f"{file}.br"))
            self.__remove_and_add(os.path.join(self.static_dir, f"{file}.gz"))

        print(
            f"""
            Removed : {self.count} files 
                |> From '{ os.path.join(settings.BASE_DIR, 'staticfiles') }' 
                |> Using '{ os.path.join(settings.BASE_DIR, 'staticfiles', 'staticfiles.json') }'
            """
        )
