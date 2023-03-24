from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import JsonResponse


def index_page(request):
    places = Place.objects.all()
    places_geojson = {
                "type": "FeatureCollection",
                "features": [],
    }
    for place in places:
        place_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": place.coordinates.coords
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": f'places/{place.pk}/'
            },
        }
        places_geojson['features'].append(place_data)
    return render(request, 'index.html', context={'places_geojson': places_geojson})


def get_place_info(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place_imgs_lst = [img.image.url for img in place.images.all()]
    longitude, latitude = place.coordinates
    place_info = {
        'title': place.title,
        'imgs': place_imgs_lst,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': longitude,
            'lat': latitude
            }
    }
    return JsonResponse(place_info, json_dumps_params={'ensure_ascii': False, 'indent': 2})
