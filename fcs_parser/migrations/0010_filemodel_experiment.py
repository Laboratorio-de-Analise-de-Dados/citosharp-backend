# Generated by Django 5.0.2 on 2024-06-30 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fcs_parser", "0009_alter_filemodel_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="filemodel",
            name="experiment",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="fcs_parser.experimentmodel",
            ),
            preserve_default=False,
        ),
    ]