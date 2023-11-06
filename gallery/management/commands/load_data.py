import os
from itertools import count
from django.core.management.base import BaseCommand
import json
import shutil
from gallery.models import Painting
from config import settings


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open(f"{settings.BASE_DIR}/default_set/db.json", 'r') as f:
            data = json.load(f)

            for p in data:
                if not Painting.objects.filter(title=p['title']):
                    full_descr = ""
                    for string in p['full_description']:
                        full_descr += string + "\n"

                    painting = Painting(
                        title=p['title'],
                        short_description=p['short_description'],
                        full_description=full_descr,
                        image=f"paintings/{p['filename']}",
                        slug=p['slug']
                    )

                    source = f"default_set/images/{p['filename']}"
                    dest_path = f"{settings.MEDIA_ROOT}/paintings/"

                    try:
                        shutil.copyfile(f"{source}", f"{dest_path}/{p['filename']}")
                    except:
                        os.makedirs(os.path.dirname(dest_path))
                        shutil.copyfile(source, f"{dest_path}/{p['filename']}")
                    painting.save()