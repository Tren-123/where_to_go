from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.core.serializers import serialize
import json
from django.http import JsonResponse


def index_page(request):
    places = Place.objects.all()
    geojson_data = serialize(
        'geojson',
        places,
        geometry_field='coordinates',
        fields=('title', 'pk'),
    )
    encoded_geojson_data = json.loads(geojson_data)
    for item in encoded_geojson_data['features']:
        pk = item['properties'].pop('pk')
        item['properties']['placeId'] = pk
        item['properties']['detailsUrl'] = f'places/{pk}/'
    return render(request, 'index.html', context={'places_data': encoded_geojson_data})


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
