# Generated by Django 5.1.2 on 2024-10-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("urlshort", "0003_alter_shorturl_short_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shorturl",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
    ]