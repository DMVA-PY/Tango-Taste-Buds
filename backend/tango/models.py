from django.db import models
from django.contrib.auth.models import User


class recipes(models.Model):
    name = models.CharField("", max_length=50)
    logo_image = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__(self):
        return self.name