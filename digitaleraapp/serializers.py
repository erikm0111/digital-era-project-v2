from rest_framework import serializers

from .models import BusinessInfo

class BusinessInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BusinessInfo
        fields = ('id', 'name', 'description', 'image_url', 'website_url', 'date_created', 'date_modified', 'owner')
        read_only_fields = ('id', 'date_created', 'date_modified', 'owner')