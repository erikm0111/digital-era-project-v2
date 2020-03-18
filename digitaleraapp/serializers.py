from rest_framework import serializers

from .models import BusinessInfo

class BusinessInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = ('id', 'name', 'description', 'image_url', 'website_url', 'date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')