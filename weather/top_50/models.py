from django.db import models


class City(models.Model):
    """Модель города."""
    name = models.CharField("Название", max_length=150)
    population = models.IntegerField("Население")

    def __str__(self):
        return self.name


class Weather(models.Model):
    date = models.DateTimeField("Дата прогноза", auto_now_add=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name="Город", related_name="weathers")
    temp = models.FloatField("Температура в градусах Цельсия")

    def __str__(self):
        return f"Погода в {city} - {temp} градусов Цельсия."
