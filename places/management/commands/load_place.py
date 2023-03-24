from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.contrib.gis.geos import Point
from django.core.files.base import ContentFile
import requests


class Command(BaseCommand):
    help = 'Download data to database from json files. Сommand accept at least 1 file as argument'

    def add_arguments(self, parser):
        parser.add_argument('json_files', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Download in progress...')
        try:
            for file in options['json_files']:
                r = requests.get(file)
                data = r.json()
                place = Place.objects.create(
                    title=data['title'],
                    description_short=data['description_short'],
                    description_long=data['description_long'],
                    coordinates=Point(float(data['coordinates']['lng']),
                                      float(data['coordinates']['lat'])),
                )
                img_lst = []
                for index, img_link in enumerate(data['imgs']):
                    r = requests.get(img_link)
                    img_content = ContentFile(r.content)
                    img = Image(place=place, number=index+1)
                    img.image.save(
                        f'{place.title}.jpg',
                        img_content,
                        save=False,
                    )
                    img_lst.append(img)
                Image.objects.bulk_create(img_lst)
            self.stdout.write(self.style.SUCCESS('Download successfull'))
        except requests.exceptions.JSONDecodeError:
            self.stdout.write('Download not complete. Your file not json')
