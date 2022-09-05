# Generated by Django 4.1 on 2022-09-05 04:15

import apps.staff.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0004_alter_staffmodel_family_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="staffmodel",
            name="staff_image",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to=apps.staff.models.FileField.staff,
            ),
        ),
    ]
