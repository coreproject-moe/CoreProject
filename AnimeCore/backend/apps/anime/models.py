from pathlib import Path


from django.db import models
from django.contrib.auth import get_user_model


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def anime_cover(instance, filename) -> str:
        return Path("anime_cover", filename)

    @staticmethod
    def anime_charater(instance, filename) -> str:
        return Path("anime_characters", filename)

    @staticmethod
    def episode_cover(instance, filename) -> str:
        return Path("episode_cover", filename)

    @staticmethod
    def episode_upload(instance, filename) -> str:
        return Path("episode", filename)


# Create your models here.


class EpisodeCommentModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_added = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name = "Episode Comment"
        # Sort by newest first
        ordering = ("-comment_added",)


class EpisodeTimestampModel(models.Model):
    timestamp = models.IntegerField(default=0)
    episode_number = models.IntegerField(null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_index=True)

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.user}"

    class Meta:
        verbose_name = "Episode Timestamp"


class EpisodeModel(models.Model):
    episode_number = models.BigIntegerField(default=0)
    episode_name = models.CharField(max_length=1024, db_index=True)
    episode_cover = models.ImageField(
        upload_to=FileField.episode_cover, default=None, blank=True, null=True
    )
    episode_file = models.FileField(
        upload_to=FileField.episode_upload, default=None, blank=True, null=True
    )
    episode_summary = models.TextField(default="", blank=True, null=True)
    episode_comments = models.ManyToManyField(EpisodeCommentModel, blank=True)
    episode_timestamps = models.ManyToManyField(EpisodeTimestampModel, blank=True)

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.episode_name}"

    class Meta:
        verbose_name = "Episode"


class AnimeProducerModel(models.Model):
    mal_id = models.IntegerField(
        unique=True, blank=False, null=False, primary_key=True, db_index=True
    )
    name = models.CharField(
        unique=True, max_length=50, default="", null=False, blank=False, db_index=True
    )
    type = models.CharField(max_length=50, default="", null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.mal_id}. {self.name} ({self.type})"

    class Meta:
        verbose_name = "Anime Producer"


class AnimeStudioModel(models.Model):
    mal_id = models.IntegerField(
        unique=True, blank=False, null=False, primary_key=True, db_index=True
    )
    name = models.CharField(
        unique=True, max_length=50, default="", null=False, blank=False, db_index=True
    )
    type = models.CharField(
        max_length=50, default="", null=False, blank=False, db_index=True
    )

    def __str__(self) -> str:
        return f"{self.mal_id}. {self.name} ({self.type})"

    class Meta:
        verbose_name = "Anime Studio"


class AnimeThemeModel(models.Model):
    mal_id = models.IntegerField(
        unique=True, blank=False, null=False, primary_key=True, db_index=True
    )
    name = models.CharField(
        unique=True, max_length=50, default="", null=False, blank=False, db_index=True
    )
    type = models.CharField(
        max_length=50, default="", null=False, blank=False, db_index=True
    )

    def __str__(self) -> str:
        return f"{self.mal_id}. {self.name} ({self.type})"

    class Meta:
        verbose_name = "Anime Theme"


class AnimeGenreModel(models.Model):
    mal_id = models.IntegerField(
        unique=True, blank=False, null=False, primary_key=True, db_index=True
    )
    name = models.CharField(
        unique=True, max_length=50, default="", null=False, blank=False, db_index=True
    )
    type = models.CharField(
        max_length=50, default="", null=False, blank=False, db_index=True
    )

    def __str__(self) -> str:
        return f"{self.mal_id}. {self.name} ({self.type})"

    class Meta:
        verbose_name = "Anime Genre"


class AnimeSynonymModel(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Anime Synonym"


class AnimeCharacterModel(models.Model):
    mal_id = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=1024, unique=True, db_index=True)
    character_image = models.ImageField(
        upload_to=FileField.anime_charater, default=None, blank=True, null=True
    )

    class Meta:
        verbose_name = "Anime Characters"


class AnimeInfoModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=False, null=False)
    # anilist_id = models.IntegerField(unique=True, blank=False, null=False)
    anime_name = models.CharField(max_length=1024, db_index=True)
    anime_name_japanese = models.CharField(max_length=1024, null=True, db_index=True)
    anime_source = models.CharField(max_length=128, blank=True, null=True)
    anime_aired_from = models.DateTimeField(blank=True, null=True)
    anime_aired_to = models.DateTimeField(blank=True, null=True)
    anime_cover = models.ImageField(
        upload_to=FileField.anime_cover, default=None, blank=True, null=True
    )
    anime_synopsis = models.TextField(blank=True, null=True)
    anime_background = models.TextField(blank=True, null=True)
    anime_rating = models.CharField(max_length=50, blank=True, null=True)

    anime_genres = models.ManyToManyField(AnimeGenreModel, blank=True)
    anime_themes = models.ManyToManyField(AnimeThemeModel, blank=True)
    anime_studios = models.ManyToManyField(AnimeStudioModel, blank=True)
    anime_producers = models.ManyToManyField(AnimeProducerModel, blank=True)
    anime_name_synonyms = models.ManyToManyField(AnimeSynonymModel, blank=True)
    anime_episodes = models.ManyToManyField(EpisodeModel, blank=True)

    updated = models.DateTimeField(auto_now_add=True)

    # anime_rating = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.anime_name}"

    class Meta:
        verbose_name = "Anime"


class AnimeRecommendationModel(models.Model):
    entry = models.ForeignKey(
        to=AnimeInfoModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    anime_id = models.IntegerField(db_index=True)
    mal_url = models.URLField(unique=True)

    def __str__(self) -> str:
        return f"{self.entry}"

    class Meta:
        verbose_name = "Anime Recommendations"
