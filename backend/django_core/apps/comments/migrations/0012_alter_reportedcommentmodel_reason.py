# Generated by Django 5.0.2 on 2024-02-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0011_reportedcommentmodel_reason_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reportedcommentmodel",
            name="reason",
            field=models.CharField(
                blank=True, choices=[("racism", "Racism")], max_length=255, null=True
            ),
        ),
    ]
