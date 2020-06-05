from django.contrib import admin

from .models import Place, PlacePhoto


class PlacePhotoInline(admin.TabularInline):
    model = PlacePhoto
    fields = ('photo', 'order')
    extra = 1


@admin.register(PlacePhoto)
class AdminPlacePhoto(admin.ModelAdmin):
    list_display = ('title', 'order',)
    list_filter = ('place__title',)
    ordering = ('order',)


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude')
    inlines = (PlacePhotoInline,)
