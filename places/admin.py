from django.contrib import admin
from django.db import models
from django.contrib.gis.db import models as geomodels
from django import forms
from .models import Place, Image

class PlaceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        geomodels.PointField: {"widget": forms.TextInput},
    }

admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)