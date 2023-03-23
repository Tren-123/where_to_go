from django import forms
from .models import Place
from django.contrib.gis.geos import Point


class PlaceGeoInputForm(forms.ModelForm):

    latitude = forms.FloatField(
        min_value=-90,
        max_value=90,
        required=True,
    )
    longitude = forms.FloatField(
        min_value=-180,
        max_value=180,
        required=True,
    )

    class Meta(object):
        model = Place
        exclude = []
        widgets = {'coordinates': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        coordinates = self.initial.get('coordinates', None)
        if isinstance(coordinates, Point):
            self.initial['longitude'], self.initial['latitude'] = coordinates.tuple

    def clean(self):
        data = super().clean()
        latitude = data.get('latitude', False)
        longitude = data.get('longitude', False)
        data['coordinates'] = Point(longitude, latitude)
        return data
