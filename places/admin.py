from django.contrib import admin
from .models import Place, Image
from .forms import PlaceGeoInputForm
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ['preview_image']

    def preview_image(self, img):
        if img.image.height > 200:
            preview_width = int(img.image.width/(img.image.height/200))
            preview_height = 200
        else:
            preview_width = img.image.width
            preview_height = img.image.height
        return format_html(
            '<img src="{url}" width="{width}" height={height} />',
            url=img.image.url,
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
