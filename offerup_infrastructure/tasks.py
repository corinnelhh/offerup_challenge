from __future__ import absolute_import
import time

from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from image_app.models import Image
import pHash


@shared_task(
    serializer='json',
    name="tasks.check_for_duplicates"
)
def check_for_duplicates(image_id, image=None):
    for i in xrange(10):
        try:
            image = Image.objects.get(pk=image_id)
            break
        except ObjectDoesNotExist:
            time.sleep(1)
    if image:
        image_hash = pHash.imagehash(image)
        if Image.objects.filter(Hash=image_hash):
            image.Duplicate = True
        image.Hash = image_hash
        image.save(cel_save=True)
    else:
        print "Could not retrieve image with this id."
