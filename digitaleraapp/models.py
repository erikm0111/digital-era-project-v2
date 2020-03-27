from django.db import models
from django.conf import settings

class BusinessInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    image_url = models.CharField(max_length=200, blank=True)
    website_url = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='businessInfos', on_delete=models.CASCADE)

    def __str__(self):
        return self.name