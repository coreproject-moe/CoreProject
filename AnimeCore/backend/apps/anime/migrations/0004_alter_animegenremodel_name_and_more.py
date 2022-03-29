# Generated by Django 4.0.3 on 2022-03-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0003_alter_animeinfomodel_anime_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animegenremodel",
            name="name",
            field=models.CharField(
                db_index=True, default="", max_length=50, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="animeproducermodel",
            name="name",
            field=models.CharField(
                db_index=True, default="", max_length=50, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="animestudiomodel",
            name="name",
            field=models.CharField(
                db_index=True, default="", max_length=50, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="animethememodel",
            name="name",
            field=models.CharField(
                db_index=True, default="", max_length=50, unique=True
            ),
        ),
    ]
