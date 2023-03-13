from django.shortcuts import render
from places.models import Place
from django.core.serializers import serialize
import json

def index_page(request):
    places = Place.objects.all()
    data = serialize('geojson', places, geometry_field='coordinates',
          fields=('title', 'pk'))
    encoded_data = json.loads(data)
    for item in encoded_data["features"]:
        item['properties']['placeId'] = item['properties'].pop('pk')
        item['properties']['detailsUrl'] = "None"
    
    return render(request, 'index.html', context={"places_data": encoded_data})

