from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, default='')
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title


class PlacePhoto(models.Model):
    title = models.CharField(max_length=150, blank=True)
    place = models.ForeignKey(
        to=Place,
        related_name='photos',
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(upload_to='places/', blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
