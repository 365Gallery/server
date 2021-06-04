from .models import GalleryPhoto, Tag
from rest_framework import serializers

class TagField(serializers.RelatedField):
    def to_representation(self, value):
        return {'idx': value.idx, 'name': value.name, 'color': value.color}


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.ImageField(use_url=True)
    tag_idx = serializers.IntegerField(write_only=True)
    tag = TagField(read_only=True)

    class Meta:
        model = GalleryPhoto
        fields = ('pk', 'created', 'file', 'tag_idx', 'tag')
