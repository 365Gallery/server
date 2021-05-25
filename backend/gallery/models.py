from django.db import models


class GalleryPhoto(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='media/', default="/")
    src = models.CharField(blank=True, null=True, max_length=512)
