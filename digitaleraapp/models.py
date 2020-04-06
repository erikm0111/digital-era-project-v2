from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

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

class WebsitePerformanceAudit(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    overall_savings_ms = models.DecimalField(max_digits=20, decimal_places=8, null=True, blank=True)
    display_value = models.CharField(max_length=300, blank=True)
    business_owner = models.ForeignKey(BusinessInfo, related_name='performance_audits', on_delete=models.CASCADE)

class Template(models.Model):
    class TemplateChoice(models.TextChoices):
        EMAIL = 'EMAIL', _('E-mail')
        LETTER = 'LETTER', _('Letter')
        PITCH = 'PITCH', _('Pitch presentation')

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=6, choices=TemplateChoice.choices, default=TemplateChoice.EMAIL)
    content = models.CharField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='templates', on_delete=models.CASCADE)
