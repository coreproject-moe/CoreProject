# Generated by Django 4.2.4 on 2023-08-29 04:12

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0017_remove_animemodel_anime_name_name_japanese_idx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animenamesynonymmodel",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddIndex(
            model_name="animenamesynonymmodel",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["name"], name="anime_name_synonym_idx", opclasses=["gin_trgm_ops"]
            ),
        ),
    ]
