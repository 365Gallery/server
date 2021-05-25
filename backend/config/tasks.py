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
def convert_image(model_name):
    
    evaluate(["--checkpoint", str(settings.BASE_DIR.parents[0]) + "/model/" + model_name,
               "--in-path", str(settings.BASE_DIR) + "/media/input.jpeg",
               "--out-path", str(settings.BASE_DIR) + "/media/output.jpeg",
               "--allow-different-dimensions"])
