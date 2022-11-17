import time

import requests

from weather.celery import app
from weather.settings import API_KEY

from .models import City, Weather


@app.task
def collector():
    cities = tuple(City.objects.all().values_list("name", flat=True))
    # for city in cities[:5]:
    #     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    #     city_obj = City.objects.get(name=city)
    #     response = requests.get(url)
    #     temp = response.json()["main"]["temp"]
    #     obj, created = Weather.objects.get_or_create(
    #         city=city_obj)
    #     obj.temp = temp
    #     obj.save()
    time.sleep(3)  # Необходимо, т.к. стоит ограничение на кол-во запросов
    print("Данные о погоде обновлены!")
