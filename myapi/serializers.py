from django.urls.base import reverse
from rest_framework import serializers
from myapi.models import Device
from django.urls import reverse


class DeviceSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField('get_link')
    ip_link = serializers.SerializerMethodField('get_ip_link')
    sap_link = serializers.SerializerMethodField('get_sap_link')
    range_link = serializers.SerializerMethodField('get_range_link')

    def get_link(self, instance):
      return reverse('mymodel-detail', args=[instance.id])

    def get_ip_link(self, instance):
      return reverse('api-router-by-ip', args=[instance.loopback])

    def get_sap_link(self, instance):
      return reverse('api-router-by-sap', args=[instance.of_type,instance.sap_id])

    def get_range_link(self, instance):
        return reverse('api-router-by-range', args=[instance.loopback,instance.loopback])
    
    class Meta:
        model = Device
        exclude = ('deleted_on','created_on','updated_on' )

    def create(self, validated_data):
        device = Device.objects.create(**validated_data)
        return device
