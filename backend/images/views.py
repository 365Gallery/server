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


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    class Meta:
        model = Image
        fields = '__all__'

    def create(self, request, *args, **kwargs):
        file_obj = request.data.get('file')
    
        print(file_obj)

        if file_obj == None or "image" not in file_obj.content_type:
            return Res.fail(400, "이미지가 아닙니다 ")

        if os.path.isfile('media/input.jpeg'):
            os.remove('media/input.jpeg')

        file_obj.name = "input.jpeg"
        path = default_storage.save(
            str(settings.BASE_DIR) + '/media/input.jpeg', ContentFile(file_obj.read()))

        model_name = self.request.query_params.get('model', 'scream.ckpt')
        isSave = self.request.query_params.get('save', 'False')

        print("[model selected : " + model_name + "]")

        is_async = self.request.query_params.get('async', 'False')
        if is_async == 'true':
            convert_image.delay(model_name)
        else:
            convert_image(model_name)

        convert_image.delay(model_name)
        if isSave == 'true' or isSave == 'True':
            output = default_storage.open(
                str(settings.BASE_DIR) + '/media/output.jpeg'
            )
            new_image = Image.objects.create(file=output)
            new_image.src = 'http://127.0.0.1:8000/' + new_image.file.name.split('/')[-1]
            new_image.save()
            return Res.success("성공입니다,", None)

        return Res.success("성공입니다", None)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return Res.success("성공입니다", super().list(request, *args, **kwargs).data)

    def retrieve(self, request, *args, **kwargs):
        return Res.success("성공입니다", super().retrieve(request, *args, **kwargs).data)