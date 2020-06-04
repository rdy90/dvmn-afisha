from django.contrib import admin

from .models import Place, PlacePhoto


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude')


@admin.register(PlacePhoto)
class AdminPlacePhoto(admin.ModelAdmin):
    list_display = ('title', 'order',)
    list_filter = ('place__title',)
    ordering = ('order',)
