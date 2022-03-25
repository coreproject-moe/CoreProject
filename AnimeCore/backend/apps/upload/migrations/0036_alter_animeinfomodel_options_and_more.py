# Generated by Django 4.0.3 on 2022-03-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0035_alter_animeinfomodel_anime_name_japanese"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="animeinfomodel",
            options={"ordering": ("mal_id",), "verbose_name": "Anime"},
        ),
        migrations.AddField(
            model_name="animeinfomodel",
            name="anime_background",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="animeinfomodel",
            name="anime_synopsis",
            field=models.TextField(blank=True, null=True),
        ),
    ]
