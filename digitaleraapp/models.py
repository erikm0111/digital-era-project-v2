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


class PhoneNumber(models.Model):
    str_number = models.CharField(max_length=30)
    business_owner = models.ForeignKey(BusinessInfo, related_name='phone_numbers', on_delete=models.CASCADE)

class Email(models.Model):
    email_address = models.CharField(max_length=40)
    business_owner = models.ForeignKey(BusinessInfo, related_name='emails', on_delete=models.CASCADE)