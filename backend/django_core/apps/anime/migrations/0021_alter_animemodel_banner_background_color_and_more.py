# Generated by Django 4.2.5 on 2023-09-09 04:19

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0020_alter_animegenremodel_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animemodel",
            name="banner_background_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
            ),
        ),
        migrations.AlterField(
            model_name="animemodel",
            name="cover_background_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default=None,
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
            ),
        ),
    ]
