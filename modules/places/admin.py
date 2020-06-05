from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, PlacePhoto


class PlacePhotoInline(admin.TabularInline):
    model = PlacePhoto
    fields = ('photo', 'get_preview', 'order')
    readonly_fields = ('get_preview',)
    extra = 1

    @staticmethod
    def get_preview(obj):
        return mark_safe(f'<img height="200" src="{obj.photo.url}" />')


@admin.register(PlacePhoto)
class AdminPlacePhoto(admin.ModelAdmin):
    list_display = ('title', 'order',)
    list_filter = ('place__title',)
    ordering = ('order',)


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude')
    inlines = (PlacePhotoInline,)
