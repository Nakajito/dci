# Generated by Django 4.2.4 on 2023-08-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ausencias", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="licencias",
            name="motivo",
            field=models.TextField(null=True),
        ),
    ]