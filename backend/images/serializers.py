from .models import Image
from rest_framework import serializers


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = ('file',)
