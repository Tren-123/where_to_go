from django.db import models
from django.contrib.gis.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.PointField()
    
    def __str__(self):
        return f'{self.title}'
    
class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/images/places/')

    def __str__(self):
         return f'{self.number} {self.place}'