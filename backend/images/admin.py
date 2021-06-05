from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Image


@admin.register(Image)
class ImagesAdmin(ModelAdmin):
    pass
