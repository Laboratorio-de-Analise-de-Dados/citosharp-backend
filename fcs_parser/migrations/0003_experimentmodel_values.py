# Generated by Django 5.0.2 on 2024-03-20 15:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fcs_parser", "0002_filedatamodel_file_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="experimentmodel",
            name="values",
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
