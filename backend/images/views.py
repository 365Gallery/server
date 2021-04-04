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
            '/home/byol2chae/server/backend/media/input.jpeg', ContentFile(file_obj.read()))

        model = self.request.query_params.get('model', 'scream.ckpt')
        print("[model selected : " + model + "]")

        evaluate(["--checkpoint", "/home/byol2chae/server/model/" + model,
                  "--in-path", "/home/byol2chae/server/backend/media/input.jpeg",
                  "--out-path", "/home/byol2chae/server/backend/media/output.jpeg",
                  "--allow-different-dimensions"])

        return Res.success("성공입니다" , None)
