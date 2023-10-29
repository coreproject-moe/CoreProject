# Generated by Django 5.0b1 on 2023-10-29 05:51

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("characters", "0004_alter_charactermodel_is_locked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="charactermodel",
            name="created_at",
            field=models.DateTimeField(
                db_default=django.db.models.functions.datetime.Now()
            ),
        ),
    ]
