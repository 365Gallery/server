from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import GalleryPhoto, MyGallery, Tag, GalleryComment, Comment

@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(ModelAdmin):
    pass

@admin.register(MyGallery)
class MyGalleryAdmin(ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    pass

@admin.register(GalleryComment)
class GalleryCommentAdmin(ModelAdmin):
    pass
