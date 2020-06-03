from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    longitude = models.DecimalField(decimal_places=7, max_digits=9)
    latitude = models.DecimalField(decimal_places=7, max_digits=9)

    def __str__(self):
        return self.title


class PlacePhoto(models.Model):
    title = models.CharField(max_length=150)
    place = models.ForeignKey(
        to=Place,
        related_name='places',
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(upload_to='places/', blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
