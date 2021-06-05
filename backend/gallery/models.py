from django.db import models

class Tag(models.Model):

    idx = models.IntegerField()
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10)

class Comment(models.Model):

    writer = models.CharField(max_length=20)
    text = models.CharField(max_length=1024)

class GalleryComment(models.Model):

    gallery = models.ForeignKey("gallery.GalleryPhoto", on_delete=models.DO_NOTHING, related_name="gallery")
    comment = models.ForeignKey("gallery.Comment", on_delete=models.CASCADE, related_name="comment")

class GalleryPhoto(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='media/', default="/")
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, related_name="tag", null=True)

class MyGallery(models.Model):

    owner = models.ForeignKey("members.Member", on_delete=models.DO_NOTHING, related_name="owner")
    photo = models.ForeignKey(GalleryPhoto, on_delete=models.CASCADE, related_name="photo")
