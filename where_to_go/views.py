from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
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
    place_obj = get_object_or_404(Place, pk=pk)
    place_imgs_qstring = Image.objects.filter(place=place_obj)
    place_imgs_lst = [image.image.url for image in place_imgs_qstring]
    place_info = {
        'title': place_obj.title,
        'imgs': place_imgs_lst,
        'description_short': place_obj.description_short,
        'description_long': place_obj.description_long,
        'coordinates': {
            'lng': place_obj.coordinates[0],
            'lat': place_obj.coordinates[1]
            }
    }
    return JsonResponse(place_info)
