from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.files.storage import default_storage
from django.conf import settings
import time
import sys
sys.path.insert(0, 'images/')
from images.evaluate import evaluate
from images.models import Image


@shared_task
def convert_image(model_name, isSave):
    
    evaluate(["--checkpoint", str(settings.BASE_DIR.parents[0]) + "/model/" + model_name,
               "--in-path", str(settings.BASE_DIR) + "/media/input.jpeg",
               "--out-path", str(settings.BASE_DIR) + "/media/output.jpeg",
               "--allow-different-dimensions"])

    if isSave == 'true' or isSave == 'True':
        output = default_storage.open(
            str(settings.BASE_DIR) + '/media/output.jpeg'
        )
        new_image = Image.objects.create(file=output)
        new_image.src = 'http://34.64.152.92:8000/' + new_image.file.name.split('/')[-1]
        new_image.save()
