import json

from django.shortcuts import render
from django.views.generic import ListView

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
