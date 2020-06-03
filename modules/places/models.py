from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    longitude = models.DecimalField(decimal_places=7, max_digits=9)
    latitude = models.DecimalField(decimal_places=7, max_digits=9)

    def __str__(self):
        return self.title
