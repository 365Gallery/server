from django.db import models


class GalleryPhoto(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='media/', default="/")
    src = models.CharField(blank=True, null=True, max_length=512)

class MyGallery(models.Model):

    owner = models.ForeignKey("members.Member", on_delete=models.DO_NOTHING, related_name="owner")
    photo = models.ForeignKey(GalleryPhoto, on_delete=models.CASCADE, related_name="photo")
