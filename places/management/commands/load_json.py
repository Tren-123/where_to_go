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
        self.stdout.write(f'Download in progress...')
        try:
            for file in options["json_files"]:
                r = requests.get(file)
                data = r.json()
                place_obj = Place.objects.create(
                    title = data['title'],
                    description_short = data['description_short'],
                    description_long = data['description_long'],
                    coordinates = Point(float(data['coordinates']['lng']), float(data['coordinates']['lat'])),
                )
                img_objs_lst = []
                for index, img in enumerate(data['imgs']):
                    r = requests.get(img)
                    img_content = ContentFile(r.content)
                    img_obj = Image(place=place_obj, number=index+1)
                    img_obj.image.save(f'{place_obj.title}.jpg', img_content, save=False)
                    img_objs_lst.append(img_obj)
                Image.objects.bulk_create(img_objs_lst)
            self.stdout.write(self.style.SUCCESS('Download successfull'))
        except requests.exceptions.JSONDecodeError:
            self.stdout.write(f'Download not complete. Your file not json')