# Generated by Django 4.2a1 on 2023-02-06 04:09

import colorfield.fields
import dynamic_filenames

import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import (
    BtreeGinExtension,
    HStoreExtension,
    TrigramExtension,
)
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("characters", "0002_alter_charactermodel_character_image"),
        ("studios", "0001_initial"),
        ("episodes", "0002_initial"),
        ("producers", "0001_initial"),
    ]

    operations = [
        HStoreExtension(),
        BtreeGinExtension(),
        TrigramExtension(),
        migrations.CreateModel(
            name="AnimeGenreModel",
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
                ("name", models.CharField(default="", max_length=50, unique=True)),
                ("type", models.CharField(default="", max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Anime Genre",
            },
        ),
        migrations.CreateModel(
            name="AnimeNameSynonymModel",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Anime Synonym",
            },
        ),
        migrations.CreateModel(
            name="AnimeThemeModel",
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
                ("name", models.CharField(default="", max_length=50, unique=True)),
                ("type", models.CharField(default="", max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Anime Theme",
            },
        ),
        migrations.CreateModel(
            name="AnimeModel",
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
                ("mal_id", models.IntegerField(null=True, unique=True)),
                ("anilist_id", models.IntegerField(null=True, unique=True)),
                ("kitsu_id", models.IntegerField(null=True, unique=True)),
                ("name", models.CharField(max_length=1024, unique=True)),
                (
                    "name_japanese",
                    models.CharField(blank=True, default="", max_length=1024),
                ),
                ("source", models.CharField(blank=True, max_length=128, null=True)),
                ("aired_from", models.DateTimeField(blank=True, null=True)),
                ("aired_to", models.DateTimeField(blank=True, null=True)),
                (
                    "banner",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_patten="banner/{uuid:s}{ext}"
                        ),
                    ),
                ),
                (
                    "cover",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern="cover/{uuid:s}{ext}"
                        ),
                    ),
                ),
                (
                    "banner_background_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=18,
                        null=True,
                        samples=None,
                    ),
                ),
                (
                    "cover_background_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=18,
                        null=True,
                        samples=None,
                    ),
                ),
                ("synopsis", models.TextField(blank=True, null=True)),
                ("background", models.TextField(blank=True, null=True)),
                ("rating", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "theme_openings",
                    django.contrib.postgres.fields.hstore.HStoreField(
                        blank=True, default=dict
                    ),
                ),
                (
                    "theme_endings",
                    django.contrib.postgres.fields.hstore.HStoreField(
                        blank=True, default=dict
                    ),
                ),
                ("updated", models.DateTimeField(auto_now_add=True)),
                (
                    "characters",
                    models.ManyToManyField(blank=True, to="characters.charactermodel"),
                ),
                (
                    "episodes",
                    models.ManyToManyField(blank=True, to="episodes.episodemodel"),
                ),
                ("genres", models.ManyToManyField(blank=True, to="anime.animegenremodel")),
                (
                    "name_synonyms",
                    models.ManyToManyField(blank=True, to="anime.animenamesynonymmodel"),
                ),
                (
                    "producers",
                    models.ManyToManyField(blank=True, to="producers.producermodel"),
                ),
                (
                    "recommendations",
                    models.ManyToManyField(blank=True, to="anime.animemodel"),
                ),
                ("studios", models.ManyToManyField(blank=True, to="studios.studiomodel")),
                ("themes", models.ManyToManyField(blank=True, to="anime.animethememodel")),
            ],
            options={
                "verbose_name": "Anime",
            },
        ),
    ]
