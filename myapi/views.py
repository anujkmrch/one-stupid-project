from django.db.models.query import QuerySet
from rest_framework.decorators import action
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from datetime import datetime,  timezone

from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy


from rest_framework import viewsets

from myapi.models import Device
from myapi.serializers import DeviceSerializer

#django web based views
class RouterListView(LoginRequiredMixin, ListView):
    model = Device
    paginate_by = 100

class RouterDetailView(LoginRequiredMixin, DetailView):
    model = Device

class CreateRouterView(LoginRequiredMixin, CreateView):
    model = Device
    fields = ['sap_id', 'hostname', 'loopback', 'mac_address']


class UpdateRouterView(LoginRequiredMixin, UpdateView):
    model = Device
    fields = ['sap_id', 'hostname', 'loopback', 'mac_address']
    template_name_suffix = '_update_form'


class DeleteRouterView(LoginRequiredMixin, DeleteView):
    model = Device
    success_url = reverse_lazy('router_list')

#rest api view
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class DeviceRemoveView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class RouterList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # permission_classes = [IsAdminUser]

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = DeviceSerializer(queryset, many=True)
    #     return Response(serializer.data)


class RouterByCatList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DeviceSerializer
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        cat = self.kwargs['cat']
        return Device.objects.filter(cat__type=cat)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data)


class RouterByIP(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DeviceSerializer
    lookup_field = 'loopback'

    def get_queryset(self):
        ip = self.kwargs["loopback"]
        return Device.objects.filter(loopback=ip)

class RouterBySAP(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DeviceSerializer
    lookup_field = 'sap_id'

    def get_queryset(self):
        sap_id = self.kwargs["sap"]
        of_type = self.kwargs["type"]
        return Device.objects.filter(sap_id=sap_id).filter(of_type=of_type)

class RouterByRange(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DeviceSerializer
    lookup_field = 'loopback'

    def get_queryset(self):
        r1 = self.kwargs["r1"]
        r2 = self.kwargs["r2"]
        print(self.kwargs)
        return Device.objects.filter(loopback__lte=r2,loopback__gte=r1)


class DeviceViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Device.objects.all()
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        device = Device.objects.create(**request.data)
        return Response(data=device)
#  {
#         "sap_id": "ISwFIEZbUYTnofbK",
#         "hostname": "laptop-288",
#         "loopback": "10.195.189.90",
#         "mac_address": "e5:58:5b:ce:a2:e4"
#     }
    def retrieve(self, request, pk=None):
        queryset = Device.objects.get(id=pk)
        serializer = DeviceSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    @action(detail=True, methods=['get'])
    def router_by_ip(self, request, loopback=None):
        return Response(["some","good","data"])

