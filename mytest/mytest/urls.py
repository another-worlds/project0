"""
URL configuration for mytest project.

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
    1. Impor    t the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  
from django.views import generic


urlpatterns = [
    path('f', generic.TemplateView.as_view(template_name='home/main.html')),
    path('hello', include('hello.urls')),
    path('posts', include('myapp.urls')),
    path('app/', include('myapp2.urls')),
    path('gview/', include('gview.urls')),
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]


