from django.contrib import admin
from .models import Place, Image
from .forms import PlaceGeoInputForm
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        if obj.image.height > 200:
            preview_width = int(obj.image.width/(obj.image.height/200))
            preview_height = 200
        else:
            preview_width = obj.image.width
            preview_height = obj.image.height
        return format_html(
            '<img src="{url}" width="{width}" height={height} />',
            url=obj.image.url,
            width=preview_width,
            height=preview_height,
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
