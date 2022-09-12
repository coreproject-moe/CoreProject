import hashlib
import mimetypes
from typing import IO, Generator

from django.contrib.auth import get_user_model
from django.http import HttpRequest, StreamingHttpResponse
import requests
from requests.utils import default_user_agent

from .models import CustomUser

SESSION = requests.session()
CHUNK_SIZE = 512  # 512 bytes


def read_files_in_chunks(
    file_object: IO[bytes],
    chunk_size: int = CHUNK_SIZE,
) -> Generator[bytes, None, None]:
    """
    Lazy function to read a file piece by piece.
    """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

    file_object.close()


def avatar_view(
    request: HttpRequest,
    user_id: int,
) -> StreamingHttpResponse:
    response: StreamingHttpResponse
    user: CustomUser = get_user_model().objects.get(id=user_id)

    if user.avatar:
        avatar_file = open(user.avatar.path, "rb")
        file_iterator = read_files_in_chunks(avatar_file)
        response = StreamingHttpResponse(
            streaming_content=file_iterator,
        )
        response["content-type"] = str(
            mimetypes.MimeTypes().guess_type(
                url=user.avatar.path,
            )[0]
        )

    else:
        # Proxy from Libravatar / Gravatar
        url = f"""https://seccdn.libravatar.org/avatar/{
            hashlib
            .md5(
                user.
                email.
                strip().
                lower().
                encode()
            )
            .hexdigest()
        }
        """
        res = SESSION.get(
            url,
            stream=True,
            params=dict(request.GET),
        )

        response = StreamingHttpResponse(
            streaming_content=res,
        )
        response["content-type"] = res.headers["content-type"]
        response["server"] = default_user_agent()

    return response
