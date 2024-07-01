# Generated by Django 5.0.2 on 2024-06-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fcs_parser", "0012_alter_experimentmodel_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experimentmodel",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("processing", "Processing"),
                    ("done", "Done"),
                    ("error", "Error"),
                ],
                default="new",
                max_length=50,
            ),
        ),
    ]