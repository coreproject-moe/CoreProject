# Generated by Django 4.0.3 on 2022-03-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0033_alter_animeinfomodel_anime_aired_from_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animeinfomodel",
            name="anime_aired_from",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animeinfomodel",
            name="anime_aired_to",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="animeinfomodel",
            name="anime_source",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
