from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import PhotoSerializer, CommentSerializer
from .models import GalleryPhoto, Tag, Comment, GalleryComment
from django.core.files.storage import default_storage
import os
from core.utils import Res
from django.conf import settings


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    class Meta:
        model = GalleryPhoto
        fields = '__all__'

    def create(self, request, *args, **kwargs):
        photo_pk = request.data.get('photo_pk')
        writer = request.data.get('writer')
        text = request.data.get('text')

        new_comment = Comment.objects.create(writer=writer, text=text)
        gallery = GalleryPhoto.objects.get(pk=photo_pk)
        GalleryComment.objects.create(gallery=gallery, comment=new_comment)

        return Res.success("성공", None)


class GalleryViewSet(ModelViewSet):
    queryset = GalleryPhoto.objects.all()
    serializer_class = PhotoSerializer

    class Meta:
        model = GalleryPhoto
        fields = '__all__'

    def create(self, request, *args, **kwargs):
        file_obj = request.data.get('file')
        tag_idx = request.data.get('tag_idx', None)
    
        print(file_obj)

        if file_obj == None or "image" not in file_obj.content_type:
            return Res.fail(400, "이미지가 아닙니다 ")

        new_object = GalleryPhoto.objects.create(file = file_obj)
        if tag_idx is not None:
            new_object.tag = Tag.objects.get(idx=tag_idx)
            new_object.save()

        return Res.success("성공입니다", None)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Res.build(response.status_code, response.status_text, response.data)
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return Res.build(response.status_code, response.status_text, response.data)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)