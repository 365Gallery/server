from django.db import models


class Image(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='media/', name="file", default="/")
