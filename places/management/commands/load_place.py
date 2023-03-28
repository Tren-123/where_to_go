from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.contrib.gis.geos import Point
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
import requests


class Command(BaseCommand):
    help = 'Download data to database from json files. Сommand accept at least 1 file as argument'

    def add_arguments(self, parser):
        parser.add_argument('json_files', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Download in progress...')
        try:
            for file in options['json_files']:
                response = requests.get(file)
                raw_place = response.json()
                place = Place.objects.create(
                    title=raw_place['title'],
                    description_short=raw_place.get('description_short', ''),
                    description_long=raw_place.get('description_long', ''),
                    coordinates=Point(float(raw_place['coordinates']['lng']),
                                      float(raw_place['coordinates']['lat'])),
                )
                imgs = []
                for index, img_link in enumerate(raw_place['imgs'], 1):
                    response = requests.get(img_link)
                    img_content = ContentFile(response.content)
                    img = Image(
                        place=place,
                        number=index,
                        image=ImageFile(img_content, f'{place.title}.jpg'),
                    )
                    imgs.append(img)
                Image.objects.bulk_create(imgs)
            self.stdout.write(self.style.SUCCESS('Download successfull'))
        except requests.exceptions.JSONDecodeError:
            self.stdout.write('Download not complete. Your file not json')
