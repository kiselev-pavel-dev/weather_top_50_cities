# Generated by Django 4.1.3 on 2022-11-16 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=150, verbose_name="Название")),
                ("population", models.IntegerField(verbose_name="Население")),
            ],
        ),
        migrations.CreateModel(
            name="Weather",
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
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата прогноза"
                    ),
                ),
                (
                    "temp",
                    models.FloatField(verbose_name="Температура в градусах Цельсия"),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="weathers",
                        to="top_50.city",
                        verbose_name="Город",
                    ),
                ),
            ],
        ),
    ]
