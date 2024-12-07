# Generated by Django 5.1.3 on 2024-11-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=100)),
                ("body", models.TextField()),
                (
                    "status_type",
                    models.CharField(
                        choices=[(1, "PENDING"), (2, "COMPLETED")],
                        default=1,
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
