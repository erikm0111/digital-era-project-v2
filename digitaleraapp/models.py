from django.db import models

class BusinessInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=200)
    website_url = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name