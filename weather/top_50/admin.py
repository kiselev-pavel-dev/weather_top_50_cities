from django.contrib import admin

from .models import City, Weather


class AdminCity(admin.ModelAdmin):
    list_display = ("id", "name", "population")
    fields = ("name", "population")
    readonly_fields = ("id",)


class AdminWeather(admin.ModelAdmin):
    list_display = ("id", "city", "date", "temp")
    fields = ("id", "city", "temp", "date")
    readonly_fields = ("id", "date",)


admin.site.register(City, AdminCity)
admin.site.register(Weather, AdminWeather)
