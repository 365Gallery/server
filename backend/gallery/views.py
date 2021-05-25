from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import PhotoSerializer
from .models import GalleryPhoto
from django.core.files.storage import default_storage
import os
from core.utils import Res
from django.conf import settings


class GalleryViewSet(ModelViewSet):
    queryset = GalleryPhoto.objects.all()
    serializer_class = PhotoSerializer

    class Meta:
        model = GalleryPhoto
        fields = '__all__'

    def create(self, request, *args, **kwargs):
        file_obj = request.data.get('file')
    
        print(file_obj)

        if file_obj == None or "image" not in file_obj.content_type:
            return Res.fail(400, "이미지가 아닙니다 ")

        new_object = GalleryPhoto.objects.create(file = file_obj, src = "http://34.64.152.92:8000/" + file_obj.name.split('/')[-1])

        return Res.success("성공입니다", None)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Res.build(response.status_code, response.status_text, response.data)
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return Res.build(response.status_code, response.status_text, response.data)