"""room_view URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

from . import controllers

urlpatterns = [
    # Ajax Request Routes
    #############################################
    url(r'^ajax/freenow', controllers.free_now),
    url(r'^ajax/roomquery', controllers.room_query),
    #############################################
    url(r'^admin/', admin.site.urls),
    url(r'^location/(?P<id>[0-9]+)', controllers.location),
    url(r'^$', controllers.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
