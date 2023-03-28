from django.contrib import admin
from .models import Place, Image
from .forms import PlaceGeoInputForm
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ['preview_image']

    def preview_image(self, img):
        return format_html(
            '<img src="{url}" height="{height}" width="auto"/>',
            url=img.image.url,
            height=200,
        )
    fields = ('image', 'preview_image', 'number')


class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    form = PlaceGeoInputForm
    search_fields = ['title']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
