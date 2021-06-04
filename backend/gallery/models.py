from django.db import models

class Tag(models.Model):

    idx = models.IntegerField()
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10)

class GalleryPhoto(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='media/', default="/")
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, related_name="tag", null=True)

class MyGallery(models.Model):

    owner = models.ForeignKey("members.Member", on_delete=models.DO_NOTHING, related_name="owner")
    photo = models.ForeignKey(GalleryPhoto, on_delete=models.CASCADE, related_name="photo")
