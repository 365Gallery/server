from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from core.utils import Res
from django.conf import settings
from config.tasks import convert_image


class PostViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')

        if file_obj == None or "image" not in file_obj.content_type:
            return Res.fail(400, "이미지가 아닙니다 ")

        if os.path.isfile('media/input.jpg'):
            os.remove('media/input.jpg')

        file_obj.name = "input.jpg"
        path = default_storage.save(
            str(settings.BASE_DIR) + '/media/input.jpg', ContentFile(file_obj.read()))

        model_name = self.request.query_params.get('model', 'final.ckpt-13000')
        print("[model selected : " + model_name + "]")

        convert_image.delay(model_name)

        return Res.success("성공입니다", None)
