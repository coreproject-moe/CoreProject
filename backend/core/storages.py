from typing import Any

from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    # https://stackoverflow.com/questions/9522759/imagefield-overwrite-image-file-with-same-name
    def get_available_name(self, *args: Any, **kwargs: Any) -> str:
        self.delete(args[0])
        return super().get_available_name(*args, **kwargs)
