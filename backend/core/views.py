from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os


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

        os.system("python3 ~/server/fast-style-transfer/evaluate.py \
    --checkpoint ~/server/model/scream.ckpt \
    --in-path ~/server/backend/media/input.jpeg \
    --out-path ~/server/backend/media/output.jpeg \
    --allow-different-dimensions")

        return Response("성공", status=200)
