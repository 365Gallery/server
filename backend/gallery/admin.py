from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import GalleryPhoto


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(ModelAdmin):
    pass
