# Generated by Django 4.2.2 on 2023-06-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.IntegerField(null=True),
        ),
    ]
