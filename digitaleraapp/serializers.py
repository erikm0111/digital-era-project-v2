from rest_framework import serializers

from .models import BusinessInfo, PhoneNumber, Email

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['str_number']
        read_only_fields = ('business_owner',)

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['email_address']
        read_only_fields = ('business_owner',)

class BusinessInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    phone_numbers = PhoneNumberSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = BusinessInfo
        fields = ('id', 'name', 'description', 'image_url', 'website_url', 'phone_numbers', 'emails', 'date_created', 'date_modified', 'owner')
        read_only_fields = ('id', 'date_created', 'date_modified', 'owner')

    def create(self, validated_data):
        phonenumbers_data = validated_data.pop('phone_numbers')
        emails_data = validated_data.pop('emails')
        businessInfo = BusinessInfo.objects.create(**validated_data)
        for phonenum in phonenumbers_data:
            PhoneNumber.objects.create(business_owner=businessInfo, **phonenum)
        for email in emails_data:
            Email.objects.create(business_owner=businessInfo, **email)
        return businessInfo