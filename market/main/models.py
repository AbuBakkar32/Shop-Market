from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class item(models.Model):
    owner = models.ForeignKey(User, default=None, blank=True, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=512)
    
    def __str__(self):
        return self.name + " Item"
