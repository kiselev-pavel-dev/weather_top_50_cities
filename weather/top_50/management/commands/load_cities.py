import csv
import os

from django.core.management.base import BaseCommand
from top_50.models import City
from top_50.tasks import collector

from weather.settings import BASE_DIR


class Command(BaseCommand):
    help = "Выгружаем даннные городов из csv в базу."

    def add_arguments(self, parser):
        parser.add_argument(
            "file_name", default="cities.csv", nargs="?", type=str
        )

    def handle(self, *args, **options):
        City.objects.all().delete()
        with open(os.path.join(os.path.join(BASE_DIR), options['file_name']),
                  newline="",
                  encoding="utf-8",
                  ) as csvfile:
            items = csv.reader(csvfile, delimiter=",")
            for _, city, _, pop2022, _, _ in items:
                City.objects.get_or_create(name=city, population=pop2022)
        collector.delay()
        print("Данные успешно загружены!")
