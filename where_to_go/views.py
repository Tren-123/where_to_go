from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from places.models import Place
from django.http import JsonResponse


def index_page(request):
    places = Place.objects.all()
    places_features = []
    for place in places:
        places_features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': place.coordinates.coords,
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.pk,
                    'detailsUrl': reverse('place', args=[place.pk]),
                },
            }
        )
    places_feature_collection = {
        'type': 'FeatureCollection',
        'features': places_features,
    }
    return render(request, 'index.html', context={'places_feature_collection': places_feature_collection})


def get_place_info(request, pk):
    place = get_object_or_404(Place, pk=pk)
    longitude, latitude = place.coordinates
    place_info = {
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': longitude,
            'lat': latitude,
        },
    }
    return JsonResponse(place_info, json_dumps_params={'ensure_ascii': False, 'indent': 2})
