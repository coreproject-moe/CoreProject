from django.core.files.storage import FileSystemStorage
from typing import Self


class OverwriteStorage(FileSystemStorage):
    # https://stackoverflow.com/questions/9522759/imagefield-overwrite-image-file-with-same-name
    def get_available_name(
        self: Self,
        name: str,
        max_length: int | None = None,
    ) -> str:
        self.delete(name)
        return super().get_available_name(
            name,
            max_length,
        )
