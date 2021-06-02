from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import GalleryPhoto, MyGallery


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(ModelAdmin):
    pass

@admin.register(MyGallery)
class MyGalleryAdmin(ModelAdmin):
    pass
