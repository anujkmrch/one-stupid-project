"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views
from myapi import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'routers', views.DeviceViewSet,basename='mymodel')


urlpatterns = [

    # path('api/hello/', views.HelloView.as_view(), name='api_hello'),
    # path('api/routers/', views.RouterList.as_view(), name='api_router_list'),
    # path('api/hello/', views.HelloView.as_view(), name='api_hello'),
    path('router_by_ip/<loopback>', views.RouterByIP.as_view(),name='api-router-by-ip'),
    path('router_by_sap/<type>/<sap>', views.RouterBySAP.as_view(),name='api-router-by-sap'),
    path('router_list_by_range/<r1>-<r2>', views.RouterByRange.as_view(),name='api-router-by-range'),
    path('token-login/', obtain_auth_token, name='api_login'),
    path('admin/', admin.site.urls),

    path('', views.RouterListView.as_view(), name='router_list'),
    path('show/<pk>', views.RouterDetailView.as_view(), name='router_detail'),
    path('create/', views.CreateRouterView.as_view(), name='router_create'),
    path('update/<pk>', views.UpdateRouterView.as_view(), name='router_update'),
    path('delete/<pk>', views.DeleteRouterView.as_view(), name='router_delete'),

    path('login/', auth_views.LoginView.as_view(template_name='myapi/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')

]

urlpatterns += router.urls
