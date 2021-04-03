from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from .evaluate import evaluate


class PostViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')

        if "image" not in file_obj.content_type:
            return Response("이미지가 아닙니다 ", status=400)

        if os.path.isfile("media/input.jpeg"):
            os.remove("media/input.jpeg")

        file_obj.name = "input.jpeg"
        path = default_storage.save(
            'media/input.jpeg', ContentFile(file_obj.read()))

        model = 'scream.ckpt'
        try:
            model = request.data['model']
        except Exception:
            model = 'scream.ckpt'

        evaluate(["--checkpoint", "/home/byol2chae/server/model/" + model,
                  "--in-path", "/home/byol2chae/server/backend/media/input.jpeg",
                  "--out-path", "/home/byol2chae/server/backend/media/output.jpeg",
                  "--allow-different-dimensions"])

        return Response("성공", status=200)
