from django.contrib import admin
from myapi.models import Device
@admin.register(Device)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("sap_id", "loopback")


