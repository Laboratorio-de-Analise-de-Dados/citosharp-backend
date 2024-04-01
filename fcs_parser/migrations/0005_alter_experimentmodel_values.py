# Generated by Django 5.0.2 on 2024-04-01 00:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fcs_parser", "0004_experimentmodel_active_experimentmodel_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experimentmodel",
            name="values",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=100),
                blank=True,
                default=list,
                size=None,
            ),
        ),
    ]