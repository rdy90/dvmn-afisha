import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View

from .models import Place


class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        features = [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude],
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.slug,
                    'detailUrl': '#',
                },
            }
            for place in Place.objects.all()
        ]

        return render(request, 'index.html', {'features': json.dumps(features)})


class PlaceView(View):
    def get(self, request, *args, **kwargs):
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        prepared_map = {
            'title': place.title,
            'imgs': [
                item.photo.url
                for item in place.photos.all()
            ],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {'lat': place.latitude, 'lng': place.longitude},

        }

        return JsonResponse(prepared_map, status=200, safe=False)
