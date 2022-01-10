from libravatar import libravatar_raw_query
from platform import python_version
from asgiref.sync import sync_to_async

# Django imports
from django.http.response import HttpResponse

from custom.user.models import CustomUser

# PIL for image resizing
from PIL import Image
from io import BytesIO

# Monkeypatch
import pillow_avif

# Create your views here.


async def avatar(request, user_id) -> HttpResponse:
    # Get user | Note that our user model is custom
    user = await sync_to_async(CustomUser.objects.get, thread_sensitive=True)(
        id=user_id
    )

    email = user.email
    print(f"Fetching avatar for {email}")
    result = await libravatar_raw_query(email, dict(request.GET))

    # No reason. Just to be a bit more transparent
    headers = {"server": f"Python/{python_version()}"}

    # Pillow processing
    res = Image.open(BytesIO(await result.aread()))
    in_memory = BytesIO()
    res.save(in_memory, format="avif")

    return HttpResponse(
        # await result.aread(),
        in_memory.getvalue(),
        content_type="image/avif",
        headers=headers,
    )
