# Generated by Django 4.1a1 on 2022-06-14 03:58

import apps.anime.models.anime_character
import apps.anime.models.anime_info
import apps.anime.models.episode
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AnimeCharacterModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mal_id", models.IntegerField(db_index=True, unique=True)),
                ("name", models.CharField(db_index=True, max_length=1024, unique=True)),
                (
                    "character_image",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=apps.anime.models.anime_character.FileField.anime_charater,
                    ),
                ),
            ],
            options={
                "verbose_name": "Anime Character",
            },
        ),
        migrations.CreateModel(
            name="AnimeGenreModel",
            fields=[
                (
                    "mal_id",
                    models.IntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, default="", max_length=50, unique=True
                    ),
                ),
                ("type", models.CharField(db_index=True, default="", max_length=50)),
            ],
            options={
                "verbose_name": "Anime Genre",
            },
        ),
        migrations.CreateModel(
            name="AnimeProducerModel",
            fields=[
                (
                    "mal_id",
                    models.IntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, default="", max_length=50, unique=True
                    ),
                ),
                ("type", models.CharField(default="", max_length=50)),
            ],
            options={
                "verbose_name": "Anime Producer",
            },
        ),
        migrations.CreateModel(
            name="AnimeStudioModel",
            fields=[
                (
                    "mal_id",
                    models.IntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, default="", max_length=50, unique=True
                    ),
                ),
                ("type", models.CharField(db_index=True, default="", max_length=50)),
            ],
            options={
                "verbose_name": "Anime Studio",
            },
        ),
        migrations.CreateModel(
            name="AnimeSynonymModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Anime Synonym",
            },
        ),
        migrations.CreateModel(
            name="AnimeThemeModel",
            fields=[
                (
                    "mal_id",
                    models.IntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, default="", max_length=50, unique=True
                    ),
                ),
                ("type", models.CharField(db_index=True, default="", max_length=50)),
            ],
            options={
                "verbose_name": "Anime Theme",
            },
        ),
        migrations.CreateModel(
            name="EpisodeCommentModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("comment_added", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Episode Comment",
                "ordering": ("-comment_added",),
            },
        ),
        migrations.CreateModel(
            name="EpisodeModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("episode_number", models.BigIntegerField(default=0)),
                ("episode_name", models.CharField(db_index=True, max_length=1024)),
                (
                    "episode_cover",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=apps.anime.models.episode.FileField.episode_cover,
                    ),
                ),
                (
                    "episode_file",
                    models.FileField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=apps.anime.models.episode.FileField.episode_upload,
                    ),
                ),
                (
                    "episode_summary",
                    models.TextField(blank=True, default="", null=True),
                ),
                (
                    "episode_comments",
                    models.ManyToManyField(blank=True, to="anime.episodecommentmodel"),
                ),
            ],
            options={
                "verbose_name": "Episode",
            },
        ),
        migrations.CreateModel(
            name="EpisodeTimestampModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.IntegerField(default=0)),
                (
                    "episode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="anime.episodemodel",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Episode Timestamp",
            },
        ),
        migrations.AddField(
            model_name="episodemodel",
            name="episode_timestamps",
            field=models.ManyToManyField(blank=True, to="anime.episodetimestampmodel"),
        ),
        migrations.CreateModel(
            name="AnimeInfoModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mal_id", models.IntegerField(unique=True)),
                (
                    "anime_name",
                    models.CharField(db_index=True, max_length=1024, unique=True),
                ),
                (
                    "anime_name_japanese",
                    models.CharField(db_index=True, max_length=1024, null=True),
                ),
                (
                    "anime_source",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("anime_aired_from", models.DateTimeField(blank=True, null=True)),
                ("anime_aired_to", models.DateTimeField(blank=True, null=True)),
                (
                    "anime_banner",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=apps.anime.models.anime_info.FileField.anime_banner,
                    ),
                ),
                (
                    "anime_cover",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=apps.anime.models.anime_info.FileField.anime_cover,
                    ),
                ),
                ("anime_synopsis", models.TextField(blank=True, null=True)),
                ("anime_background", models.TextField(blank=True, null=True)),
                (
                    "anime_rating",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("updated", models.DateTimeField(auto_now_add=True)),
                (
                    "anime_characters",
                    models.ManyToManyField(blank=True, to="anime.animecharactermodel"),
                ),
                (
                    "anime_episodes",
                    models.ManyToManyField(blank=True, to="anime.episodemodel"),
                ),
                (
                    "anime_genres",
                    models.ManyToManyField(blank=True, to="anime.animegenremodel"),
                ),
                (
                    "anime_name_synonyms",
                    models.ManyToManyField(blank=True, to="anime.animesynonymmodel"),
                ),
                (
                    "anime_producers",
                    models.ManyToManyField(blank=True, to="anime.animeproducermodel"),
                ),
                (
                    "anime_recommendation",
                    models.ManyToManyField(blank=True, to="anime.animeinfomodel"),
                ),
                (
                    "anime_studios",
                    models.ManyToManyField(blank=True, to="anime.animestudiomodel"),
                ),
                (
                    "anime_themes",
                    models.ManyToManyField(blank=True, to="anime.animethememodel"),
                ),
            ],
            options={
                "verbose_name": "Anime",
            },
        ),
    ]
