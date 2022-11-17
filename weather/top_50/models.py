from django.db import models


class City(models.Model):
    """Модель города."""
    name = models.CharField("Название", max_length=150)
    population = models.IntegerField("Население")

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Weather(models.Model):
    """Погода в топ-50 городов."""
    date = models.DateTimeField("Дата прогноза", auto_now=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name="Город", related_name="weathers")
    temp = models.FloatField("Температура в градусах Цельсия", default=0)

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Погода"
        verbose_name_plural = "Погода"

    def __str__(self):
        return str(self.city)
