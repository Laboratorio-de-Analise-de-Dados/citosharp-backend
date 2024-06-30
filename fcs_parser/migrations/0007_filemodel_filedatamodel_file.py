# Generated by Django 5.0.2 on 2024-06-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fcs_parser", "0006_alter_experimentmodel_values"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="filedatamodel",
            name="file",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]