"""
URL configuration for nesteam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


# schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [

    path('admin/', admin.site.urls),

    path('games/', include('games.urls')),

    path('userapp/', include('userapp.urls')),

    path('franchise/', include('franchise.urls')),

    path('api_schema/', get_schema_view(title='API Schema', description='test'), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ),
         name='swagger-ui'),

    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),


]
