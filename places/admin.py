from django.contrib import admin
from django.contrib.gis.db import models as geomodels
from django import forms
from .models import Place, Image
from .forms import PlaceGeoInputForm

class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'number')

class PlaceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        geomodels.PointField: {"widget": forms.TextInput},
    }
    inlines = [
        ImageInline,
    ]
    #form = PlaceGeoInputForm

admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)