from collections.abc import Generator
from io import BufferedReader
import mimetypes
from pathlib import Path

from django.conf import settings
from django.http import HttpResponse, StreamingHttpResponse

CHUNK_SIZE = 512  # 512 bytes


def read_files_in_chunks(
    file_object: BufferedReader,
    chunk_size: int = CHUNK_SIZE,
) -> Generator[bytes, None, None]:
    """Lazy function to read a file piece by piece."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

    file_object.close()


def sendfile(
    file_path: str | Path,
    content_type: str | None,
) -> HttpResponse | StreamingHttpResponse:
    response: HttpResponse | StreamingHttpResponse
    file_location = f"{settings.MEDIA_ROOT}/{file_path}"

    if not settings.DEBUG:
        response = HttpResponse()
        response["X-Sendfile"] = file_location
        del response["content-type"]

    else:
        opened_file = open(file_location, "rb")
        file_iterator = read_files_in_chunks(opened_file)
        response = StreamingHttpResponse(
            streaming_content=file_iterator,
        )
        response["content-type"] = (
            content_type
            if content_type
            else str(
                mimetypes.MimeTypes().guess_type(
                    url=file_location,
                )[0]
            )
        )

    return response


# def sendbytes(
#     file_blob: BufferedReader,
#     content_type: str,
# ) -> HttpResponse:
#     if not settings.DEBUG:
#         response = HttpResponse()
#         response["X-Sendfile"] = BytesIO(file_blob)
#         del response["content-type"]
#         return response

#     else:
#         data = BytesIO(file_blob)
#         return HttpResponse(data, content_type=content_type)
