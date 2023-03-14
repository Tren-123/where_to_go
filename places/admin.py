from django.contrib import admin
from django.contrib.gis.db import models as geomodels
from django import forms
from .models import Place, Image
from .forms import PlaceGeoInputForm
from django.utils.html import format_html

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["preview_image"]

    def preview_image(self, obj):
        if obj.image.height > 200:
            preview_width = int(obj.image.width/(obj.image.height/200))
            preview_height = 200
        else:
            preview_width = obj.image.width
            preview_height = obj.image.height
        return format_html('<img src="{url}" width="{width}" height={height} />',
            url = obj.image.url,
            width = preview_width,
            height = preview_height,
                )
    fields = ('image', 'preview_image', 'number')

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