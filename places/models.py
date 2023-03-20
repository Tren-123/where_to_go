from django.db import models
from django.contrib.gis.db import models
from django.urls import reverse
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description_short = models.TextField(blank=True, verbose_name="Короткое описание")
    description_long = tinymce_models.HTMLField(blank=True, verbose_name="Длинное описание")
    coordinates = models.PointField(srid=4326, verbose_name="Координаты")
   
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):    
        return reverse('place', kwargs={'pk': self.pk})
    
class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место", related_name="images")
    number = models.PositiveIntegerField(default=0, verbose_name="Позиция")
    image = models.ImageField(upload_to='media/images/places/', verbose_name="Картинка")
    
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ['number']

    def __str__(self):
         return f'{self.number} {self.place}'