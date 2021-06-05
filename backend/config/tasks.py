from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.files.storage import default_storage
from django.conf import settings
import time
import sys
sys.path.insert(0, 'images/')
from images.run_test import evaluate


@shared_task
def convert_image(model_name):
    
    evaluate([  "--content", str(settings.BASE_DIR) + "/media/input.jpeg",
                "--style_model", str(settings.BASE_DIR) + "/images/model/" + model_name + "/" + model_name + ".ckpt",
               "--output", str(settings.BASE_DIR) + "/media/output.jpeg"])
