"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from catalogo.views import *

urlpatterns = [
    url(r'^marcas/delete-(?P<id>[0-9]+)', marca_delete_view),
    url(r'^modelos/delete-(?P<id>[0-9]+)', modelo_delete_view),
    url(r'^coches/delete-(?P<id>[0-9]+)', coche_delete_view),
    url(r'^coches/(?P<id>[0-9]+)', coche_update_view),
    url(r'^modelos/(?P<id>[0-9]+)', modelo_update_view),
    url(r'^marcas/(?P<id>[0-9]+)', marca_update_view),
    url(r'^coches/nuevo_coche', coche_create_view),
    url(r'^marcas/nueva_marca', marca_create_view),
    url(r'^modelos/nuevo_modelo', modelo_create_view),
    url(r'^coches/dictionary', dictionary_view),
    url(r'^coches/search', search_view),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^marcas/', marcas_view, name='marcas'),
    url(r'^modelos/', modelos_view, name='modelos'),
    url(r'^coches/list', coches_view, name='coches'),
    url(r'^api/list', cocheList, name='api-coche-list'),
    url(r'^api/create', cocheCreate, name='api-coche-create'),
    url(r'^api/update/(?P<id>[0-9]+)', cocheUpdate, name='api-coche-update'),
    url(r'^api/delete/(?P<id>[0-9]+)', cocheDelete, name='api-coche-delete'),
    url(r'^api/(?P<id>[0-9]+)', cocheDetail, name='api-coche-detail'),
    url(r'^api/', apiOverview, name='api'),
    
        
]
