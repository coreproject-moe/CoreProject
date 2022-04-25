# Generated by Django 4.0.4 on 2022-04-25 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0021_episodetimestampmodel_episode_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="episodetimestampmodel",
            name="episode_number",
        ),
        migrations.AddField(
            model_name="episodetimestampmodel",
            name="episode",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="anime.episodemodel",
            ),
        ),
    ]
