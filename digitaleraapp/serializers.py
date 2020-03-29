from rest_framework import serializers

from .models import BusinessInfo, PhoneNumber, Email, WebsitePerformanceAudit

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


class WebsitePerformanceAuditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsitePerformanceAudit
        fields = ['title', 'description', 'overall_savings_ms', 'display_value']
        read_only_fields = ('business_owner',)


class BusinessInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    phone_numbers = PhoneNumberSerializer(many=True)
    emails = EmailSerializer(many=True)
    performance_audits = WebsitePerformanceAuditsSerializer(many=True)

    class Meta:
        model = BusinessInfo
        fields = ('id', 'name', 'description', 'image_url', 'website_url', 'phone_numbers', 'emails', 'performance_audits', 'date_created', 'date_modified', 'owner')
        read_only_fields = ('id', 'date_created', 'date_modified', 'owner')

    def create(self, validated_data):
        phonenumbers_data = validated_data.pop('phone_numbers')
        emails_data = validated_data.pop('emails')
        performance_audits_data = validated_data.pop('performance_audits')
        businessInfo = BusinessInfo.objects.create(**validated_data)
        for phonenum in phonenumbers_data:
            PhoneNumber.objects.create(business_owner=businessInfo, **phonenum)
        for email in emails_data:
            Email.objects.create(business_owner=businessInfo, **email)
        for audit in performance_audits_data:
            WebsitePerformanceAudit.objects.create(business_owner=businessInfo, **audit)
        return businessInfo

    def update(self, instance, validated_data):
        phonenumbers_data = validated_data.pop('phone_numbers')
        phonenumbers = (instance.phone_numbers).all()
        phonenumbers = list(phonenumbers)

        emails_data = validated_data.pop('emails')
        emails = (instance.emails).all()
        emails = list(emails)

        performance_audits_data = validated_data.pop('performance_audits')
        performance_audits = (instance.performance_audits).all()
        performance_audits = list(performance_audits)

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.website_url = validated_data.get('website_url', instance.website_url)
        instance.save()

        for phonenum_data in phonenumbers_data:
            phonenumber = phonenumbers.pop(0)
            phonenumber.str_number = phonenum_data.get('str_number', phonenumber.str_number)
            phonenumber.save()

        for email_data in emails_data:
            email = emails.pop(0)
            email.email_address = email_data.get('email_address', email.email_address)
            email.save()

        for perf_audit_data in performance_audits_data:
            perf_audit = performance_audits.pop(0)
            perf_audit.title = perf_audit_data.get('title', perf_audit.title)
            perf_audit.description = perf_audit_data.get('description', perf_audit.description)
            perf_audit.overall_savings_ms = perf_audit_data.get('overall_savings_ms', perf_audit.overall_savings_ms)
            perf_audit.display_value = perf_audit_data.get('display_value', perf_audit.display_value)
            perf_audit.save()

        return instance