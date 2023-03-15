from django.db import models
from django.contrib.gis.db import models
from django.urls import reverse
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description_short = models.TextField(verbose_name="Короткое описание")
    description_long = tinymce_models.HTMLField(verbose_name="Длинное описание")
    coordinates = models.PointField(srid=4326, blank=True, verbose_name="Координаты")
    
    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):    
        return reverse('place', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
    
class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место")
    number = models.PositiveIntegerField(default=0, blank=False, null = False, verbose_name="Позиция")
    image = models.ImageField(upload_to='media/images/places/', verbose_name="Картинка")

    def __str__(self):
         return f'{self.number} {self.place}'
    
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ['number']