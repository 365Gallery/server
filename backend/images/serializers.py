from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = ('file',)
