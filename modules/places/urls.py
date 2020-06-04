from django.urls import path

from .views import IndexView, PlaceView


urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('places/<int:place_id>', PlaceView.as_view(), name='places'),
]
