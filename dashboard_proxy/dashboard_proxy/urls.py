"""dashboard_proxy URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse
from django.views.static import serve
from app import proxy

urlpatterns = [
    url(r'^login$', proxy.login),
    url(r'^login_post$', proxy.login_post),
    url(r'^healthz$', (lambda x: JsonResponse({'status': 'ok'}, status=200))),
    url(r'^favicon.ico/$', (lambda x: JsonResponse({'status': 'ok'}, status=200))),
    url(r'^.*/$', proxy.proxy),
]
