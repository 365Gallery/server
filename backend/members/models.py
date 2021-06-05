from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey
from gallery.models import MyGallery

class Member(AbstractUser):

    mygallery = ForeignKey(MyGallery, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.username
