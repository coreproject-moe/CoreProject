import os
from watchgod import watch
from pathlib import Path, PurePath

# Point this to Django Media folder
FOLDER_PATH = Path(__file__).parent.parent

# Watch only one file type | Multiple file type causes errors
FILE_TYPE = "**/*.mp4"

# Max size before GC
GC_RANGE = 1  # Note that this is GB


for changes in watch(FOLDER_PATH):
    # Folder size. In Kbps.
    summation = 0

    for file in os.scandir(PurePath(FOLDER_PATH, "media")):
        summation += os.path.getsize(file)

    if summation > (GC_RANGE * 1024 * 1024 * 1024):
        for file in os.scandir(PurePath(FOLDER_PATH, "media")):
            try:
                print(
                    f"Garbage collected | File : {file.name} | Size : {round(os.path.getsize(file)/(1024*1024), 2)} Mb"
                )
                os.unlink(file)

            except PermissionError:
                print(f"File in use {file.name} | SKIPPING")
