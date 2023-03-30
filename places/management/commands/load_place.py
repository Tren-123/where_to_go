from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.contrib.gis.geos import Point
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
import requests


def get_img_instance(img_url, related_model, number):
    response = requests.get(img_url)
    response.raise_for_status()
    return Image(
        place=related_model,
        number=number,
        image=ImageFile(
            ContentFile(response.content),
            f'{related_model.title}.jpg',
        ),
    )


class Command(BaseCommand):
    help = 'Download data to database from json files. Сommand accept at least 1 file url as argument'

    def add_arguments(self, parser):
        parser.add_argument('files_urls', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Download in progress...')
        try:
            for file_url in options['files_urls']:
                response = requests.get(file_url)
                response.raise_for_status()
                raw_place = response.json()

                if 'error' in raw_place:
                    raise requests.exceptions.HTTPError(raw_place['error'])

                place, _ = Place.objects.update_or_create(
                    title=raw_place['title'],
                    coordinates=Point(
                        float(raw_place['coordinates']['lng']),
                        float(raw_place['coordinates']['lat']),
                    ),
                    defaults={
                        'description_short': raw_place.get('description_short', ''),
                        'description_long': raw_place.get('description_long', ''),
                    },
                )

                imgs = []
                for index, img_url in enumerate(raw_place.get('imgs', []), 1):
                    imgs.append(get_img_instance(img_url, place, index))
                Image.objects.bulk_create(imgs)

            self.stdout.write(self.style.SUCCESS('Download successfull'))

        except requests.exceptions.JSONDecodeError:
            self.stdout.write('Download not complete. Your file not json or has invalid format')
