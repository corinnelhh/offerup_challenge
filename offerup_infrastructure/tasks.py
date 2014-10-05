from __future__ import absolute_import
from celery import shared_task
from image_app.models import Image
import pHash


@shared_task
def check_for_duplicates(image_id):
    image = Image.objects.get(id=image_id)
    image_hash = pHash.imagehash(image)
    if Image.objects.filter(Hash=image_hash):
        image.Duplicate = True
    image.Hash = image_hash
    image.save(cel_save=True)
