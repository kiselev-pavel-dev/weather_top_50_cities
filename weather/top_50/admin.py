from django.contrib import admin

from .models import City, Weather


class AdminCity(admin.ModelAdmin):
    pass


class AdminWeather(admin.ModelAdmin):
    pass


admin.site.register(City, AdminCity)
admin.site.register(Weather, AdminWeather)
