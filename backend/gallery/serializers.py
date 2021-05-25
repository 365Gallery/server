from .models import GalleryPhoto
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.ImageField(use_url=True)

    class Meta:
        model = GalleryPhoto
        fields = ('pk', 'created', 'file', 'src')
