# Generated by Django 4.1 on 2022-08-11 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0002_animeproducermodel_animestudiomodel_charactermodel_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AnimeProducerModel",
            new_name="ProducerModel",
        ),
    ]
