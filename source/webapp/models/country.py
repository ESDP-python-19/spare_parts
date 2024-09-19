from django.db import models


# Модель для стран


class Country(models.Model):
    name = models.CharField(max_length=255)  # название страны

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "car_countries"
        verbose_name = 'car_countries'
        db_table = 'countries'
