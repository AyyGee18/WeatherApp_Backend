from django.db import models

# Create your models here.


class Continent(models.Model):
    continent_name = models.CharField(max_length=20, unique=True)
    continent_img = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.continent_name


class Country(models.Model):
    conitnent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="country")
    conutry_name = models.CharField(max_length=30, unique=True)
    flag = models.TextField(blank=True)

    def __str__(self):
        return self.conutry_name


class City(models.Model):

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="city")
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name


class DateWeather(models.Model):

    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="dateweather")

    date = models.DateField()
    weather_status = models.CharField(max_length=255)
    status_icon = models.TextField(blank=True)
    wind_speed = models.IntegerField()
    humidity = models.IntegerField()
    temperature = models.IntegerField()

    # def __str__(self):
    #     return str(self.date)
