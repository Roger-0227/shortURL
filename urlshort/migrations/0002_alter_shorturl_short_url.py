# Generated by Django 5.1.2 on 2024-10-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("urlshort", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shorturl",
            name="short_url",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
