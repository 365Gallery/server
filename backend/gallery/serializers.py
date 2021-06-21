from .models import GalleryPhoto, Tag, GalleryComment, Comment
from rest_framework import serializers

class TagField(serializers.RelatedField):
    def to_representation(self, value):
        return {'idx': value.idx, 'name': value.name, 'color': value.color}

    def get_queryset(self):
        return super().get_queryset()

class CommentField(serializers.RelatedField):
    def to_representation(self, value):
        return {'writer': value.writer, 'text': value.text}

class CommentSerializer(serializers.ModelSerializer):

    photo_pk = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'writer', 'text', 'photo_pk')

class GalleryCommentSerializer(serializers.ModelSerializer):
    comment = CommentField(read_only=True)
    class Meta:
        model = GalleryComment
        fields = ('comment', )

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.ImageField(use_url=True)
    tag_idx = serializers.IntegerField(write_only=True)
    tag = TagField(read_only=True)
    comments = GalleryCommentSerializer( 
        many=True,
        read_only=True,
        source='gallery'
    )

    class Meta:
        model = GalleryPhoto
        fields = ('pk', 'created', 'file', 'tag_idx', 'tag', 'comments')
