# Generated by Django 4.1.7 on 2023-03-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                help_text="Required. A valid email with a valid domain",
                max_length=254,
                unique=True,
                verbose_name="email address",
            ),
        ),
    ]
