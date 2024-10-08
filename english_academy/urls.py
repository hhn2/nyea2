"""
URL configuration for english_academy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# english_academy/urls.py
from django.contrib import admin
from django.urls import path, include
from academy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academy/', include('academy.urls')),
    path('', include('academy.urls')),  # This will make '' match all the patterns from academy/urls.py
    path('video/', include('video.urls')),
]