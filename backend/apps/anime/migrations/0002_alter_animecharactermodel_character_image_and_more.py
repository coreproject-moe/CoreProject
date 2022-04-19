# Generated by Django 4.0.4 on 2022-04-19 04:14

import apps.anime.models.anime_character
import apps.anime.models.anime_info
import apps.anime.models.episode
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0001_initial_squashed_0016_alter_animerecommendationmodel_anime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animecharactermodel",
            name="character_image",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to=apps.anime.models.anime_character.FileField.anime_charater,
            ),
        ),
        migrations.AlterField(
            model_name="animeinfomodel",
            name="anime_cover",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to=apps.anime.models.anime_info.FileField.anime_cover,
            ),
        ),
        migrations.AlterField(
            model_name="animerecommendationmodel",
            name="anime",
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name="episodemodel",
            name="episode_cover",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to=apps.anime.models.episode.FileField.episode_cover,
            ),
        ),
        migrations.AlterField(
            model_name="episodemodel",
            name="episode_file",
            field=models.FileField(
                blank=True,
                default=None,
                null=True,
                upload_to=apps.anime.models.episode.FileField.episode_upload,
            ),
        ),
    ]
