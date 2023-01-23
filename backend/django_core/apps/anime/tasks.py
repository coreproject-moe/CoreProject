from huey.contrib.djhuey import db_task


@db_task()
def set_animemodel_brightness(
    anime_model_pk: int,
    image="",
) -> None:
    pass
