# Generated by Django 5.0b1 on 2023-10-29 05:51

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0021_alter_animemodel_banner_background_color_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animegenremodel",
            name="created_at",
            field=models.DateTimeField(
                db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="animemodel",
            name="created_at",
            field=models.DateTimeField(
                db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="animethememodel",
            name="created_at",
            field=models.DateTimeField(
                db_default=django.db.models.functions.datetime.Now()
            ),
        ),
    ]
