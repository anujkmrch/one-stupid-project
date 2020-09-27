from django.db import models
from datetime import datetime
from django.db.models.query import QuerySet
from django.shortcuts import reverse


class DeviceQuerySet(QuerySet):
    """
    Prevents objects from being hard-deleted. Instead, sets the
    ``date_deleted``, effectively soft-deleting the object.
    """

    def delete(self):
        for obj in self:
            obj.deleted_on = datetime.utcnow()
            obj.save()


class DeviceManager(models.Manager):

    def get_queryset(self):
        return DeviceQuerySet(self.model, using=self._db).filter(deleted_on__isnull=True)


class Device (models.Model):

    objects = DeviceManager()
    original_objects = models.Manager()

    sap_id = models.CharField(max_length=18, help_text='End SAP id')
    hostname = models.CharField(max_length=14, help_text='Hostname of user')
    loopback = models.GenericIPAddressField(verbose_name='Loopback interface')
    # models.CharField(max_length=16, help_text='Loopback interface')
    mac_address = models.CharField(max_length=17, help_text='Mac Address')
    of_type = models.CharField(max_length=10,choices=[('ag1','AG1'),('css','CSS')], default = 'css')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True, blank=True)



    def delete(self):
        self.deleted_on = datetime.now()
        self.save()

    # Metadata
    class Meta:
        ordering = ['-created_on']
        # abstract = True

    # Methods
    def get_absolute_url(self):
        return reverse('router_detail', args=[str(self.id)])

    def __str__(self):
        return self.sap_id
