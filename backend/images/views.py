from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from core.utils import Res
from .models import Image
from .serializers import ImageSerializer
from .evaluate import evaluate
import os


class PostViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')

        if "image" not in file_obj.content_type:
            return Res.fail(400, "이미지가 아닙니다 ")

        if os.path.isfile('media/input.jpeg'):
            os.remove('media/input.jpeg')

        file_obj.name = "input.jpeg"
        path = default_storage.save(
            str(settings.BASE_DIR) + '/media/input.jpeg', ContentFile(file_obj.read()))

        model_name = self.request.query_params.get('model', 'scream.ckpt')
        print("[model selected : " + model_name + "]")

        evaluate(["--checkpoint", str(settings.BASE_DIR.parents[0]) + "/model/" + model_name,
                  "--in-path", str(settings.BASE_DIR) + "/media/input.jpeg",
                  "--out-path", str(settings.BASE_DIR) + "/media/output.jpeg",
                  "--allow-different-dimensions"])

        return Res.success("성공입니다", None)
